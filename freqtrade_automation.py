#!/usr/bin/env python3
"""
Freqtrade Hyperopt and Backtesting Automation Script

This script automates the process of running hyperopt optimization followed by backtesting,
and saves the results to CSV files for analysis.

Features:
- Executes hyperopt with configurable parameters
- Runs backtesting with optimized parameters
- Parses output and extracts key metrics
- Appends results to CSV files (doesn't overwrite)
- Robust error handling and logging
"""

from random import Random
import subprocess
import json
import re
import csv
import os
import logging
import sys
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import pandas as pd

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('freqtrade_automation.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class FreqtradeAutomation:
    """Main automation class for Freqtrade hyperopt and backtesting"""
    
    def __init__(self, config: Dict):
        """Initialize with configuration parameters"""
        self.config = config
        self.hyperopt_csv = 'hyperopt_results.csv'
        self.backtest_csv = 'backtest_results.csv'
        self.hyperopt_output = ""
        self.backtest_output = ""
        self.hyperopt_command = ""
        self.backtest_command = ""
        
        # Validate required config
        required_keys = ['strategy', 'timeframe', 'hyperopt_loss', 'spaces', 'random_state']
        for key in required_keys:
            if key not in config:
                raise ValueError(f"Missing required config key: {key}")
    
    def execute_command(self, command: List[str]) -> Tuple[str, str, int]:
        """Execute a shell command and return stdout, stderr, return_code"""
        try:
            logger.info(f"Executing command: {' '.join(command)}")
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=3600  # 1 hour timeout
            )
            return result.stdout, result.stderr, result.returncode
        except subprocess.TimeoutExpired:
            logger.error("Command timed out after 1 hour")
            return "", "Command timed out", 1
        except Exception as e:
            logger.error(f"Error executing command: {e}")
            return "", str(e), 1
    
    def run_hyperopt(self) -> Optional[Dict]:
        """Execute hyperopt and return parsed results"""
        logger.info("Starting hyperopt optimization...")
        
        # Build hyperopt command
        command = [
            'docker', 'compose', 'run', '--rm', 'freqtrade', 'hyperopt',
            '--config', '/freqtrade/user_data/config.json',
            '--print-json',
            '--hyperopt-loss', self.config['hyperopt_loss'],
            '--strategy', self.config['strategy'],
            '--timeframe', self.config['timeframe'],
            '--epochs', str(self.config.get('epochs', 100)),
            '--spaces'
        ]
        
        # Add spaces as separate arguments
        spaces = self.config['spaces'].split() if isinstance(self.config['spaces'], str) else self.config['spaces']
        command.extend(spaces)
        
        # Add remaining arguments
        command.extend([
            '--pairs', 'BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT',
            '--timerange', self.config.get('hyperopt_timerange', '20170801-20191231'),
            '--random-state', str(self.config['random_state'])
        ])
        
        # Store command for logging
        self.hyperopt_command = ' '.join(command)
        
        stdout, stderr, return_code = self.execute_command(command)
        
        # Store output for logging
        self.hyperopt_output = stdout if stdout else stderr
        
        if return_code != 0:
            logger.error(f"Hyperopt failed with return code {return_code}")
            logger.error(f"Error output: {stderr}")
            return None
        
        return self.parse_hyperopt_output(stdout)
    
    def parse_hyperopt_output(self, output: str) -> Optional[Dict]:
        """Parse hyperopt output to extract metrics and parameters"""
        try:
            # Extract the best result line
            best_result_pattern = r'(\d+/\d+):\s+(\d+) trades\.\s+(\d+)/(\d+)/(\d+) Wins/Draws/Losses\.\s+Avg profit\s+([\d.-]+)%\.\s+Median profit\s+([\d.-]+)%\.\s+Total profit\s+([\d.-]+) USDT\s+\(\s*([\d.-]+)%\)\.\s+Avg duration\s+([\d:]+)\s+min\.\s+Objective:\s+([\d.-]+)'
            
            match = re.search(best_result_pattern, output)
            if not match:
                logger.error("Could not find best result pattern in hyperopt output")
                return None
            
            # Extract JSON parameters (robust: find first valid JSON object)
            json_match = None
            # Try to find a JSON block (even if not wrapped)
            json_candidates = re.findall(r'\{[\s\S]*?\}', output)
            for candidate in json_candidates:
                try:
                    params_data = json.loads(candidate)
                    json_match = candidate
                    break
                except Exception:
                    continue
            if not json_match:
                logger.error("Could not find JSON parameters in hyperopt output")
                return None
            
            # Calculate avg profit per day (approximation based on avg duration)
            avg_duration_str = match.group(10)
            avg_profit_pct = float(match.group(6))
            
            # Convert duration to hours
            time_parts = avg_duration_str.split(':')
            avg_duration_hours = int(time_parts[0]) + int(time_parts[1]) / 60
            avg_profit_per_day = (avg_profit_pct * 24 / avg_duration_hours) if avg_duration_hours > 0 else 0

            result = {
                'timestamp': datetime.now().isoformat(),
                'strategy': self.config['strategy'],
                'random_state': self.config['random_state'],
                'wins_draws_losses': f"{match.group(3)}/{match.group(4)}/{match.group(5)}",
                'avg_profit_pct': float(match.group(6)),
                'median_profit_pct': float(match.group(7)),
                'total_profit_usdt': float(match.group(8)),
                'avg_duration': avg_duration_str,
                'objective': float(match.group(11)),
                'avg_profit_per_day': round(avg_profit_per_day, 4)
            }
            
            # Add all parameters from JSON
            if 'params' in params_data:
                for key, value in params_data['params'].items():
                    result[f'param_{key}'] = value
            
            # Add ROI and other settings
            if 'minimal_roi' in params_data:
                result['minimal_roi'] = json.dumps(params_data['minimal_roi'])
            if 'stoploss' in params_data:
                result['stoploss'] = params_data['stoploss']
            
            logger.info("Successfully parsed hyperopt results")
            return result
            
        except Exception as e:
            logger.error(f"Error parsing hyperopt output: {e}")
            return None
    
    def run_backtesting(self) -> Optional[Dict]:
        """Execute backtesting and return parsed results"""
        logger.info("Starting backtesting...")
        
        # Build backtesting command
        command = [
            'docker', 'compose', 'run', '--rm', 'freqtrade', 'backtesting',
            '--config', '/freqtrade/user_data/config.json',
            '--strategy', self.config['strategy'],
            '--timeframe', self.config['timeframe'],
            '--timeframe-detail', '5m',
            '--datadir', '/freqtrade/user_data/data/binance',
            '--pairs', 'BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT',
            '--timerange', self.config.get('backtest_timerange', '20220101-20221231')
        ]
        
        # Store command for logging
        self.backtest_command = ' '.join(command)
        
        stdout, stderr, return_code = self.execute_command(command)
        
        # Store output for logging
        self.backtest_output = stdout if stdout else stderr
        
        if return_code != 0:
            logger.error(f"Backtesting failed with return code {return_code}")
            logger.error(f"Error output: {stderr}")
            return None
        
        return self.parse_backtest_output(stdout)
    
    def parse_backtest_output(self, output: str) -> Optional[Dict]:
        """Parse backtesting output to extract summary metrics"""
        try:
            result = {
                'timestamp': datetime.now().isoformat(),
                'strategy': self.config['strategy'],
                'random_state': self.config['random_state']
            }
            
            # Extract Total/Daily Avg Trades
            trades_pattern = r'Total/Daily Avg Trades\s+│\s+(\d+)\s+/\s+([\d.]+)'
            match = re.search(trades_pattern, output)
            if match:
                result['total_daily_avg_trades'] = f"{match.group(1)} / {match.group(2)}"
            
            # Extract Absolute profit
            profit_pattern = r'Absolute profit\s+│\s+([\d.-]+) USDT'
            match = re.search(profit_pattern, output)
            if match:
                result['absolute_profit_usdt'] = float(match.group(1))
            
            # Extract Total profit %
            total_profit_pattern = r'Total profit %\s+│\s+([\d.-]+)%'
            match = re.search(total_profit_pattern, output)
            if match:
                result['total_profit_pct'] = float(match.group(1))
            
            # Extract CAGR %
            cagr_pattern = r'CAGR %\s+│\s+([\d.-]+)%'
            match = re.search(cagr_pattern, output)
            if match:
                result['cagr_pct'] = float(match.group(1))
            
            # Extract Sortino
            sortino_pattern = r'Sortino\s+│\s+([\d.-]+)'
            match = re.search(sortino_pattern, output)
            if match:
                result['sortino'] = float(match.group(1))
            
            # Extract Sharpe
            sharpe_pattern = r'Sharpe\s+│\s+([\d.-]+)'
            match = re.search(sharpe_pattern, output)
            if match:
                result['sharpe'] = float(match.group(1))
            
            # Extract Calmar
            calmar_pattern = r'Calmar\s+│\s+([\d.-]+)'
            match = re.search(calmar_pattern, output)
            if match:
                result['calmar'] = float(match.group(1))
            
            # Extract SQN
            sqn_pattern = r'SQN\s+│\s+([\d.-]+)'
            match = re.search(sqn_pattern, output)
            if match:
                result['sqn'] = float(match.group(1))
            
            # Extract Max Consecutive Wins / Loss
            consecutive_pattern = r'Max Consecutive Wins / Loss\s+│\s+(\d+)\s+/\s+(\d+)'
            match = re.search(consecutive_pattern, output)
            if match:
                result['max_consecutive_wins_loss'] = f"{match.group(1)} / {match.group(2)}"
            
            # Extract Min balance
            min_balance_pattern = r'Min balance\s+│\s+([\d.-]+) USDT'
            match = re.search(min_balance_pattern, output)
            if match:
                result['min_balance_usdt'] = float(match.group(1))
            
            # Extract Max balance
            max_balance_pattern = r'Max balance\s+│\s+([\d.-]+) USDT'
            match = re.search(max_balance_pattern, output)
            if match:
                result['max_balance_usdt'] = float(match.group(1))
            
            # Extract Absolute Drawdown (Account)
            drawdown_pattern = r'Absolute Drawdown \(Account\)\s+│\s+([\d.-]+)%'
            match = re.search(drawdown_pattern, output)
            if match:
                result['absolute_drawdown_pct'] = float(match.group(1))
            
            # Extract Market change
            market_change_pattern = r'Market change\s+│\s+([\d.-]+)%'
            match = re.search(market_change_pattern, output)
            if match:
                result['market_change_pct'] = float(match.group(1))
            
            # Extract Win Draw Loss Win% from TOTAL row
            total_stats_pattern = r'│\s+TOTAL\s+│\s+\d+\s+│\s+[\d.-]+\s+│\s+[\d.-]+\s+│\s+[\d.-]+\s+│\s+[\d:]+\s+│\s+(\d+)\s+(\d+)\s+(\d+)\s+([\d.]+)'
            match = re.search(total_stats_pattern, output)
            if match:
                result['win_draw_loss_winpct'] = f"{match.group(1)} {match.group(2)} {match.group(3)} {match.group(4)}"
            
            logger.info("Successfully parsed backtesting results")
            return result
            
        except Exception as e:
            logger.error(f"Error parsing backtesting output: {e}")
            return None
    
    def save_to_csv(self, data: Dict, filename: str) -> bool:
        """Save data to CSV file, appending if file exists"""
        try:
            file_exists = os.path.exists(filename)
            
            # Create DataFrame
            df_new = pd.DataFrame([data])
            
            if file_exists:
                # Read existing data and append
                df_existing = pd.read_csv(filename)
                df_combined = pd.concat([df_existing, df_new], ignore_index=True)
            else:
                df_combined = df_new
            
            # Save to CSV
            df_combined.to_csv(filename, index=False)
            logger.info(f"Successfully saved data to {filename}")
            return True
            
        except Exception as e:
            logger.error(f"Error saving data to {filename}: {e}")
            return False
    
    def evaluate_performance(self, hyperopt_results: Dict, backtest_results: Dict) -> Tuple[str, str]:
        """Evaluate performance and return status color and description"""
        try:
            median_profit = hyperopt_results.get('median_profit_pct', 0)
            
            # Extract profit factor from backtesting output
            profit_factor = None
            profit_factor_pattern = r'Profit factor\s+│\s+([\d.-]+)'
            match = re.search(profit_factor_pattern, self.backtest_output)
            if match:
                profit_factor = float(match.group(1))
            else:
                profit_factor = 0
            
            # Evaluate performance based on criteria
            if median_profit >= 0.2 and profit_factor >= 1.5:
                return "🟢 GREEN", f"Excellent Performance (Median Profit: {median_profit}%, Profit Factor: {profit_factor})"
            elif median_profit < 0.2 or profit_factor < 1.5:
                return "🔴 RED", f"Poor Performance (Median Profit: {median_profit}%, Profit Factor: {profit_factor})"
            else:
                return "🟠 ORANGE", f"Moderate Performance (Median Profit: {median_profit}%, Profit Factor: {profit_factor})"
                
        except Exception as e:
            logger.error(f"Error evaluating performance: {e}")
            return "⚪ UNKNOWN", "Performance evaluation failed"
    
    def save_formatted_log(self, hyperopt_output: str, backtest_output: str, hyperopt_command: str, backtest_command: str, hyperopt_results: Dict = None, backtest_results: Dict = None) -> bool:
        """Save formatted command outputs to markdown log file"""
        try:
            strategy = self.config['strategy']
            random_state = self.config['random_state']
            log_filename = f"{strategy}-{random_state}.md"
            
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Evaluate performance if results are available
            performance_status = "⚪ UNKNOWN"
            performance_description = "No results available for evaluation"
            if hyperopt_results and backtest_results:
                performance_status, performance_description = self.evaluate_performance(hyperopt_results, backtest_results)
            
            log_content = f"""# Freqtrade Automation Log

## Performance Indicator
**Status:** {performance_status}  
**Description:** {performance_description}

---
            
**Strategy:** {strategy}  
**Random State:** {random_state}  
**Timestamp:** {timestamp}

## Configuration
```json
{json.dumps(self.config, indent=2)}
```

## Hyperopt Command
```bash
{hyperopt_command}
```

## Hyperopt Output
```
{hyperopt_output}
```

## Backtesting Command
```bash
{backtest_command}
```

## Backtesting Output
```
{backtest_output}
```
"""
            
            with open(log_filename, 'w', encoding='utf-8') as f:
                f.write(log_content)
            
            logger.info(f"Successfully saved formatted log to {log_filename}")
            return True
            
        except Exception as e:
            logger.error(f"Error saving formatted log: {e}")
            return False
    
    def run_full_automation(self) -> bool:
        """Run the complete hyperopt -> backtesting workflow"""
        logger.info(f"Starting full automation for strategy: {self.config['strategy']}")
        logger.info(f"Random state: {self.config['random_state']}")
        
        # Step 1: Run hyperopt
        hyperopt_results = self.run_hyperopt()
        if not hyperopt_results:
            logger.error("Hyperopt failed, stopping automation")
            return False
        
        # Step 2: Save hyperopt results
        if not self.save_to_csv(hyperopt_results, self.hyperopt_csv):
            logger.warning("Failed to save hyperopt results to CSV")
        
        # Step 3: Run backtesting
        backtest_results = self.run_backtesting()
        if not backtest_results:
            logger.error("Backtesting failed, stopping automation")
            return False
        
        # Step 4: Save backtesting results
        if not self.save_to_csv(backtest_results, self.backtest_csv):
            logger.warning("Failed to save backtesting results to CSV")
        
        # Step 5: Save formatted log with command outputs and performance evaluation
        if not self.save_formatted_log(self.hyperopt_output, self.backtest_output, 
                                     self.hyperopt_command, self.backtest_command,
                                     hyperopt_results, backtest_results):
            logger.warning("Failed to save formatted log file")
        
        # Step 6: Evaluate and display performance in console
        performance_status, performance_description = self.evaluate_performance(hyperopt_results, backtest_results)
        logger.info("=" * 60)
        logger.info(f"PERFORMANCE EVALUATION: {performance_status}")
        logger.info(f"Details: {performance_description}")
        logger.info("=" * 60)
        
        logger.info("Full automation completed successfully!")
        return True

def main():
    """Main entry point"""
    # Configuration - modify these parameters as needed
    config = {
        'strategy': 'RSIDivergenceBullishStrategy',
        'timeframe': '1h',
        'hyperopt_loss': 'SharpeHyperOptLoss',
        'spaces': 'buy',
        'random_state': Random().randint(1, 10000),  # Random state for reproducibility
        'epochs': 100,
        'hyperopt_timerange': '20170801-20191231',
        'backtest_timerange': '20220101-20221231'
    }
    
    # Initialize and run automation
    automation = FreqtradeAutomation(config)
    success = automation.run_full_automation()
    
    if success:
        print("✅ Automation completed successfully!")
        print(f"📊 Results saved to:")
        print(f"   - Hyperopt: {automation.hyperopt_csv}")
        print(f"   - Backtest: {automation.backtest_csv}")
    else:
        print("❌ Automation failed. Check logs for details.")
        sys.exit(1)

if __name__ == "__main__":
    main()