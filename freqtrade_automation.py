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
import argparse
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
        """Execute a shell command and return stdout, stderr, return_code with real-time output"""
        try:
            logger.info(f"Executing command: {' '.join(command)}")
            print("=" * 80)
            print(f"🚀 Running: {' '.join(command[:5])}{'...' if len(command) > 5 else ''}")
            print("=" * 80)
            
            # Use Popen for real-time output streaming
            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,  # Combine stderr with stdout
                text=True,
                bufsize=1,  # Line buffered
                universal_newlines=True
            )
            
            stdout_lines = []
            stderr_lines = []
            
            # Read output line by line and display in real-time
            for line in iter(process.stdout.readline, ''):
                if line:
                    # Print to console with timestamp
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    print(f"[{timestamp}] {line.rstrip()}")
                    stdout_lines.append(line)
            
            # Wait for process to complete
            return_code = process.wait()
            
            # Combine all output
            stdout = ''.join(stdout_lines)
            stderr = ""  # Since we combined stderr with stdout
            
            print("=" * 80)
            if return_code == 0:
                print("✅ Command completed successfully!")
            else:
                print(f"❌ Command failed with return code: {return_code}")
            print("=" * 80)
            
            return stdout, stderr, return_code
            
        except subprocess.TimeoutExpired:
            logger.error("Command timed out after 1 hour")
            return "", "Command timed out", 1
        except Exception as e:
            logger.error(f"Error executing command: {e}")
            return "", str(e), 1
    
    def run_hyperopt(self) -> Optional[Dict]:
        """Execute hyperopt and return parsed results"""
        print("\n" + "=" * 30)
        print("🔍 HYPEROPT OPTIMIZATION STARTING")
        print("=" * 30)
        logger.info("Starting hyperopt optimization...")
        
        # Build hyperopt command
        command = [
            'docker', 'compose', 'run', '--rm', 'freqtrade', 'hyperopt', '-j', '8',
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
        
        # Display hyperopt configuration
        print(f"📊 Strategy: {self.config['strategy']}")
        print(f"📈 Timeframe: {self.config['timeframe']}")
        print(f"🎯 Loss Function: {self.config['hyperopt_loss']}")
        print(f"🔢 Epochs: {self.config.get('epochs', 100)}")
        print(f"🎲 Random State: {self.config['random_state']}")
        print(f"💹 Spaces: {self.config['spaces']}")
        print(f"📅 Date Range: {self.config.get('hyperopt_timerange', '20170801-20191231')}")
        
        # Store command for logging
        self.hyperopt_command = ' '.join(command)
        
        stdout, stderr, return_code = self.execute_command(command)
        
        # Store output for logging
        self.hyperopt_output = stdout if stdout else stderr
        
        if return_code != 0:
            print("❌ HYPEROPT FAILED!")
            logger.error(f"Hyperopt failed with return code {return_code}")
            logger.error(f"Error output: {stderr}")
            return None
        
        print("✅ HYPEROPT COMPLETED!")
        print("=" * 30)
        return self.parse_hyperopt_output(stdout)
    
    def parse_hyperopt_output(self, output: str) -> Optional[Dict]:
        """Parse hyperopt output to extract metrics and parameters"""
        try:
            print("🔍 Parsing hyperopt results...")
            
            # Extract the best result line - updated pattern to handle "X days, HH:MM:SS" format
            best_result_pattern = r'(\d+/\d+):\s+(\d+) trades\.\s+(\d+)/(\d+)/(\d+) Wins/Draws/Losses\.\s+Avg profit\s+([\d.-]+)%\.\s+Median profit\s+([\d.-]+)%\.\s+Total profit\s+([\d.-]+) USDT\s+\(\s*([\d.-]+)%\)\.\s+Avg duration\s+(.+?)\s+min\.\s+Objective:\s+([\d.-]+)'
            
            match = re.search(best_result_pattern, output)
            if not match:
                print("❌ Could not find best result pattern in hyperopt output")
                print("🔍 Trying alternative patterns...")
                logger.error("Could not find best result pattern in hyperopt output")
                
                # Let's try to extract individual components with more flexible patterns
                epoch_pattern = r'(\d+/\d+):'
                trades_pattern = r'(\d+) trades\.'
                wins_pattern = r'(\d+)/(\d+)/(\d+) Wins/Draws/Losses\.'
                avg_profit_pattern = r'Avg profit\s+([\d.-]+)%\.'
                median_profit_pattern = r'Median profit\s+([\d.-]+)%\.'
                total_profit_pattern = r'Total profit\s+([\d.-]+) USDT\s+\(\s*([\d.-]+)%\)\.'
                duration_pattern = r'Avg duration\s+(.+?)\s+min\.'
                objective_pattern = r'Objective:\s+([\d.-]+)'
                
                # Try to match each component
                epoch_match = re.search(epoch_pattern, output)
                trades_match = re.search(trades_pattern, output)
                wins_match = re.search(wins_pattern, output)
                avg_profit_match = re.search(avg_profit_pattern, output)
                median_profit_match = re.search(median_profit_pattern, output)
                total_profit_match = re.search(total_profit_pattern, output)
                duration_match = re.search(duration_pattern, output)
                objective_match = re.search(objective_pattern, output)
                
                if not all([epoch_match, trades_match, wins_match, avg_profit_match, 
                           median_profit_match, total_profit_match, duration_match, objective_match]):
                    print("❌ Could not parse individual components either")
                    return None
                
                # Build match object manually for consistency with the rest of the code
                class ManualMatch:
                    def __init__(self):
                        self.groups = [
                            epoch_match.group(1),  # epoch
                            trades_match.group(1),  # trades
                            wins_match.group(1),  # wins
                            wins_match.group(2),  # draws
                            wins_match.group(3),  # losses
                            avg_profit_match.group(1),  # avg profit
                            median_profit_match.group(1),  # median profit
                            total_profit_match.group(1),  # total profit USDT
                            total_profit_match.group(2),  # total profit %
                            duration_match.group(1),  # duration
                            objective_match.group(1)  # objective
                        ]
                    
                    def group(self, index):
                        return self.groups[index - 1]
                
                match = ManualMatch()
                print("✅ Successfully parsed using alternative patterns")
            else:
                print("✅ Found best result metrics")
            
            # Extract JSON parameters (robust: find first valid JSON object)
            print("🔍 Searching for optimization parameters...")
            json_match = None
            # Try to find a JSON block (even if not wrapped)
            json_candidates = re.findall(r'\{[\s\S]*?\}', output)
            for candidate in json_candidates:
                try:
                    params_data = json.loads(candidate)
                    json_match = candidate
                    print("✅ Found and parsed parameters JSON")
                    break
                except Exception:
                    continue
            if not json_match:
                print("❌ Could not find JSON parameters in hyperopt output")
                logger.error("Could not find JSON parameters in hyperopt output")
                return None
            
            # Parse duration string to calculate daily profit
            avg_duration_str = match.group(10)
            
            # Parse the profit percentage for daily calculation
            try:
                avg_profit_pct = float(match.group(6))
            except (ValueError, TypeError):
                print(f"⚠️  Warning: Could not parse avg profit percentage '{match.group(6)}', using 0")
                avg_profit_pct = 0.0
            
            # Parse duration - handle both "HH:MM:SS" and "X days, HH:MM:SS" formats
            avg_duration_hours = 0
            try:
                if 'day' in avg_duration_str:
                    # Format: "2 days, 1:27:00" or "1 day, 23" (incomplete time)
                    parts = avg_duration_str.split(', ')
                    days_part = parts[0].strip()
                    time_part = parts[1].strip() if len(parts) > 1 else "0:00:00"
                    
                    # Extract days from "X day" or "X days"
                    days_match = re.search(r'(\d+)\s+days?', days_part)
                    days = int(days_match.group(1)) if days_match else 0
                    
                    # Parse time part more robustly
                    if ':' in time_part:
                        # Standard time format "HH:MM:SS" or "HH:MM"
                        time_parts = time_part.split(':')
                        hours = int(time_parts[0]) if time_parts[0].isdigit() else 0
                        minutes = int(time_parts[1]) if len(time_parts) > 1 and time_parts[1].isdigit() else 0
                        seconds = int(time_parts[2]) if len(time_parts) > 2 and time_parts[2].isdigit() else 0
                    else:
                        # Just hours or malformed - assume it's hours
                        hours = int(time_part) if time_part.isdigit() else 0
                        minutes = 0
                        seconds = 0
                    
                    avg_duration_hours = days * 24 + hours + minutes / 60 + seconds / 3600
                else:
                    # Format: "1:27:00" or just "23" (hours only)
                    if ':' in avg_duration_str:
                        time_parts = avg_duration_str.split(':')
                        hours = int(time_parts[0]) if time_parts[0].isdigit() else 0
                        minutes = int(time_parts[1]) if len(time_parts) > 1 and time_parts[1].isdigit() else 0
                        seconds = int(time_parts[2]) if len(time_parts) > 2 and time_parts[2].isdigit() else 0
                        avg_duration_hours = hours + minutes / 60 + seconds / 3600
                    else:
                        # Just a number - assume it's hours
                        avg_duration_hours = float(avg_duration_str) if avg_duration_str.replace('.', '').isdigit() else 0
            except (ValueError, AttributeError, IndexError) as e:
                print(f"⚠️  Warning: Could not parse duration '{avg_duration_str}', using 0. Error: {e}")
                logger.warning(f"Could not parse duration '{avg_duration_str}', using 0. Error: {e}")
                avg_duration_hours = 0
            
            avg_profit_per_day = (avg_profit_pct * 24 / avg_duration_hours) if avg_duration_hours > 0 else 0

            # Helper function to safely convert to float
            def safe_float(value, default=0.0):
                try:
                    return float(value)
                except (ValueError, TypeError):
                    return default

            result = {
                'timestamp': datetime.now().isoformat(),
                'strategy': self.config['strategy'],
                'random_state': self.config['random_state'],
                'wins_draws_losses': f"{match.group(3)}/{match.group(4)}/{match.group(5)}",
                'avg_profit_pct': safe_float(match.group(6)),
                'median_profit_pct': safe_float(match.group(7)),
                'total_profit_usdt': safe_float(match.group(8)),
                'avg_duration': avg_duration_str,
                'objective': safe_float(match.group(11)),
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
            
            print("✅ Successfully parsed hyperopt results")
            logger.info("Successfully parsed hyperopt results")
            return result
            
        except Exception as e:
            print(f"❌ Error parsing hyperopt output: {e}")
            logger.error(f"Error parsing hyperopt output: {e}")
            return None
    
    def run_backtesting(self) -> Optional[Dict]:
        """Execute backtesting and return parsed results"""
        print("\n" + "=" * 30)
        print("📈 BACKTESTING STARTING")
        print("=" * 30)
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
        
        # Display backtesting configuration
        print(f"📊 Strategy: {self.config['strategy']}")
        print(f"📈 Timeframe: {self.config['timeframe']}")
        print(f"💰 Pairs: BTC/USDT, ETH/USDT, LTC/USDT, XRP/USDT, BNB/USDT")
        print(f"📅 Date Range: {self.config.get('backtest_timerange', '20220101-20221231')}")
        
        # Store command for logging
        self.backtest_command = ' '.join(command)
        
        stdout, stderr, return_code = self.execute_command(command)
        
        # Store output for logging
        self.backtest_output = stdout if stdout else stderr
        
        if return_code != 0:
            print("❌ BACKTESTING FAILED!")
            logger.error(f"Backtesting failed with return code {return_code}")
            logger.error(f"Error output: {stderr}")
            return None
        
        print("✅ BACKTESTING COMPLETED!")
        print("=" * 30)
        return self.parse_backtest_output(stdout)
    
    def parse_backtest_output(self, output: str) -> Optional[Dict]:
        """Parse backtesting output to extract summary metrics"""
        try:
            print("🔍 Parsing backtest results...")
            
            # Helper function to safely convert to float
            def safe_float(value, default=0.0):
                try:
                    return float(value)
                except (ValueError, TypeError):
                    return default
            
            result = {
                'timestamp': datetime.now().isoformat(),
                'strategy': self.config['strategy'],
                'random_state': self.config['random_state']
            }
            
            print("📊 Extracting trading metrics...")
            
            # Extract Total/Daily Avg Trades
            trades_pattern = r'Total/Daily Avg Trades\s+│\s+(\d+)\s+/\s+([\d.]+)'
            match = re.search(trades_pattern, output)
            if match:
                result['total_daily_avg_trades'] = f"{match.group(1)} / {match.group(2)}"
            
            # Extract Absolute profit
            profit_pattern = r'Absolute profit\s+│\s+([\d.-]+) USDT'
            match = re.search(profit_pattern, output)
            if match:
                result['absolute_profit_usdt'] = safe_float(match.group(1))
            
            # Extract Total profit %
            total_profit_pattern = r'Total profit %\s+│\s+([\d.-]+)%'
            match = re.search(total_profit_pattern, output)
            if match:
                result['total_profit_pct'] = safe_float(match.group(1))
            
            print("📈 Extracting performance ratios...")
            
            # Extract CAGR %
            cagr_pattern = r'CAGR %\s+│\s+([\d.-]+)%'
            match = re.search(cagr_pattern, output)
            if match:
                result['cagr_pct'] = safe_float(match.group(1))
            
            # Extract Sortino
            sortino_pattern = r'Sortino\s+│\s+([\d.-]+)'
            match = re.search(sortino_pattern, output)
            if match:
                result['sortino'] = safe_float(match.group(1))
            
            # Extract Sharpe
            sharpe_pattern = r'Sharpe\s+│\s+([\d.-]+)'
            match = re.search(sharpe_pattern, output)
            if match:
                result['sharpe'] = safe_float(match.group(1))
            
            # Extract Calmar
            calmar_pattern = r'Calmar\s+│\s+([\d.-]+)'
            match = re.search(calmar_pattern, output)
            if match:
                result['calmar'] = safe_float(match.group(1))
            
            # Extract SQN
            sqn_pattern = r'SQN\s+│\s+([\d.-]+)'
            match = re.search(sqn_pattern, output)
            if match:
                result['sqn'] = safe_float(match.group(1))
            
            print("🎯 Extracting risk metrics...")
            
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
            
            # Extract Absolute Drawdown
            drawdown_pattern = r'Absolute drawdown\s+│\s+[\d.-]+\s+[A-Z]+\s+\(([\d.-]+)%\)'
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
            
            print("✅ Successfully parsed backtesting results")
            logger.info("Successfully parsed backtesting results")
            return result
            
        except Exception as e:
            print(f"❌ Error parsing backtesting output: {e}")
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
            
            # Extract metrics from backtesting results or output
            total_profit_pct = backtest_results.get('total_profit_pct', 0)
            sortino = backtest_results.get('sortino', 0)
            sharpe = backtest_results.get('sharpe', 0)
            calmar = backtest_results.get('calmar', 0)
            absolute_drawdown_pct = backtest_results.get('absolute_drawdown_pct', 0)
            total_trades = backtest_results.get('total_daily_avg_trades', 'N/A')
            
            # If not in results, try to extract from output
            if not total_profit_pct:
                total_profit_pattern = r'Total profit %\s+│\s+([\d.-]+)%'
                match = re.search(total_profit_pattern, self.backtest_output)
                if match:
                    total_profit_pct = float(match.group(1))
            
            if not sortino:
                sortino_pattern = r'Sortino\s+│\s+([\d.-]+)'
                match = re.search(sortino_pattern, self.backtest_output)
                if match:
                    sortino = float(match.group(1))
            
            if not sharpe:
                sharpe_pattern = r'Sharpe\s+│\s+([\d.-]+)'
                match = re.search(sharpe_pattern, self.backtest_output)
                if match:
                    sharpe = float(match.group(1))
            
            if not calmar:
                calmar_pattern = r'Calmar\s+│\s+([\d.-]+)'
                match = re.search(calmar_pattern, self.backtest_output)
                if match:
                    calmar = float(match.group(1))
            
            if not absolute_drawdown_pct:
                drawdown_pattern = r'Absolute drawdown\s+│\s+[\d.-]+\s+[A-Z]+\s+\(([\d.-]+)%\)'
                match = re.search(drawdown_pattern, self.backtest_output)
                if match:
                    absolute_drawdown_pct = float(match.group(1))
            
            if total_trades == 'N/A' or not total_trades:
                trades_pattern = r'Total/Daily Avg Trades\s+│\s+(\d+)\s+/\s+([\d.]+)'
                match = re.search(trades_pattern, self.backtest_output)
                if match:
                    total_trades = f"{match.group(1)} / {match.group(2)}"
            
            # Evaluate performance based on criteria
            # Good criteria: median_profit >= 0.2%, total_profit >= 5%, sortino >= 1.0, sharpe >= 0.5, calmar >= 0.5, drawdown <= 20%
            good_conditions = [
                median_profit >= 0.2,
                total_profit_pct >= 5.0,
                sortino >= 1.0,
                sharpe >= 0.5,
                calmar >= 0.5,
                abs(absolute_drawdown_pct) <= 20.0
            ]
            
            metrics_summary = f"Total trades: {total_trades}, Median: {median_profit}%, Total profit: {total_profit_pct}%, Sortino: {sortino}, Sharpe: {sharpe}, Calmar: {calmar}, Drawdown: {absolute_drawdown_pct}%"
            
            if sum(good_conditions) >= 5:  # At least 5 out of 6 criteria met
                return "� GREEN", f"Excellent Performance ({metrics_summary})"
            elif sum(good_conditions) >= 3:  # At least 3 out of 6 criteria met
                return "🟠 ORANGE", f"Moderate Performance ({metrics_summary})"
            else:
                return "🔴 RED", f"Poor Performance ({metrics_summary})"
                
        except Exception as e:
            logger.error(f"Error evaluating performance: {e}")
            return "⚪ UNKNOWN", "Performance evaluation failed"
    
    def save_hyperopt_log(self, hyperopt_output: str, hyperopt_command: str, hyperopt_results: Dict = None) -> bool:
        """Save hyperopt-only log to markdown file"""
        try:
            strategy = self.config['strategy']
            random_state = self.config['random_state']
            log_filename = f"{strategy}-{random_state}-hyperopt.md"
            
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            log_content = f"""# Freqtrade Hyperopt Log

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

## Hyperopt Results
```json
{json.dumps(hyperopt_results, indent=2) if hyperopt_results else 'No results parsed'}
```
"""
            
            with open(log_filename, 'w', encoding='utf-8') as f:
                f.write(log_content)
            
            logger.info(f"Successfully saved hyperopt log to {log_filename}")
            return True
            
        except Exception as e:
            logger.error(f"Error saving hyperopt log: {e}")
            return False

    def save_backtest_log(self, backtest_output: str, backtest_command: str, backtest_results: Dict = None) -> bool:
        """Save backtest-only log to markdown file"""
        try:
            strategy = self.config['strategy']
            random_state = self.config.get('random_state', 'unknown')
            log_filename = f"{strategy}-{random_state}-backtest.md"
            
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            log_content = f"""# Freqtrade Backtest Log

**Strategy:** {strategy}  
**Random State:** {random_state}  
**Timestamp:** {timestamp}

## Configuration
```json
{json.dumps(self.config, indent=2)}
```

## Backtesting Command
```bash
{backtest_command}
```

## Backtesting Output
```
{backtest_output}
```

## Backtest Results
```json
{json.dumps(backtest_results, indent=2) if backtest_results else 'No results parsed'}
```
"""
            
            with open(log_filename, 'w', encoding='utf-8') as f:
                f.write(log_content)
            
            logger.info(f"Successfully saved backtest log to {log_filename}")
            return True
            
        except Exception as e:
            logger.error(f"Error saving backtest log: {e}")
            return False

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
    
    def run_hyperopt_only(self) -> bool:
        """Run only hyperopt optimization"""
        print("\n" + "🚀" * 50)
        print("🤖 FREQTRADE HYPEROPT ONLY")
        print("🚀" * 50)
        
        logger.info(f"Starting hyperopt-only for strategy: {self.config['strategy']}")
        logger.info(f"Random state: {self.config['random_state']}")
        
        print(f"🎯 Strategy: {self.config['strategy']}")
        print(f"🎲 Random State: {self.config['random_state']}")
        print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Run hyperopt
        print("\n📍 Running Hyperoptimization...")
        hyperopt_results = self.run_hyperopt()
        if not hyperopt_results:
            print("💥 HYPEROPT FAILED")
            logger.error("Hyperopt failed")
            return False
        
        # Save hyperopt results
        print("\n📍 Saving Hyperopt Results...")
        if self.save_to_csv(hyperopt_results, self.hyperopt_csv):
            print(f"✅ Hyperopt results saved to {self.hyperopt_csv}")
        else:
            print("⚠️  Warning: Failed to save hyperopt results to CSV")
            logger.warning("Failed to save hyperopt results to CSV")
        
        # Save hyperopt log
        strategy = self.config['strategy']
        random_state = self.config['random_state']
        log_filename = f"{strategy}-{random_state}-hyperopt.md"
        
        if self.save_hyperopt_log(self.hyperopt_output, self.hyperopt_command, hyperopt_results):
            print(f"✅ Hyperopt report saved to {log_filename}")
        else:
            print("⚠️  Warning: Failed to save hyperopt log file")
            logger.warning("Failed to save hyperopt log file")
        
        print("\n" + "🎉" * 50)
        print("✅ HYPEROPT COMPLETED SUCCESSFULLY!")
        print("🎉" * 50)
        print(f"⏰ Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        logger.info("Hyperopt-only completed successfully!")
        return True

    def run_backtest_only(self) -> bool:
        """Run only backtesting (assuming hyperopt was done previously)"""
        print("\n" + "🚀" * 50)
        print("🤖 FREQTRADE BACKTEST ONLY")
        print("🚀" * 50)
        
        logger.info(f"Starting backtest-only for strategy: {self.config['strategy']}")
        
        print(f"🎯 Strategy: {self.config['strategy']}")
        print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Run backtesting
        print("\n📍 Running Backtesting...")
        backtest_results = self.run_backtesting()
        if not backtest_results:
            print("💥 BACKTESTING FAILED")
            logger.error("Backtesting failed")
            return False
        
        # Save backtesting results
        print("\n📍 Saving Backtest Results...")
        if self.save_to_csv(backtest_results, self.backtest_csv):
            print(f"✅ Backtest results saved to {self.backtest_csv}")
        else:
            print("⚠️  Warning: Failed to save backtest results to CSV")
            logger.warning("Failed to save backtesting results to CSV")
        
        # Save backtest log
        strategy = self.config['strategy']
        random_state = self.config.get('random_state', 'unknown')
        log_filename = f"{strategy}-{random_state}-backtest.md"
        
        if self.save_backtest_log(self.backtest_output, self.backtest_command, backtest_results):
            print(f"✅ Backtest report saved to {log_filename}")
        else:
            print("⚠️  Warning: Failed to save backtest log file")
            logger.warning("Failed to save backtest log file")
        
        print("\n" + "🎉" * 50)
        print("✅ BACKTEST COMPLETED SUCCESSFULLY!")
        print("🎉" * 50)
        print(f"⏰ Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        logger.info("Backtest-only completed successfully!")
        return True
    
    def run_full_automation(self) -> bool:
        """Run the complete hyperopt -> backtesting workflow"""
        print("\n" + "🚀" * 50)
        print("🤖 FREQTRADE AUTOMATION STARTED")
        print("🚀" * 50)
        
        logger.info(f"Starting full automation for strategy: {self.config['strategy']}")
        logger.info(f"Random state: {self.config['random_state']}")
        
        print(f"🎯 Strategy: {self.config['strategy']}")
        print(f"🎲 Random State: {self.config['random_state']}")
        print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Step 1: Run hyperopt
        print("\n📍 STEP 1/5: Running Hyperoptimization...")
        hyperopt_results = self.run_hyperopt()
        if not hyperopt_results:
            print("💥 AUTOMATION STOPPED: Hyperopt failed")
            logger.error("Hyperopt failed, stopping automation")
            return False
        
        # Step 2: Save hyperopt results
        print("\n📍 STEP 2/5: Saving Hyperopt Results...")
        if self.save_to_csv(hyperopt_results, self.hyperopt_csv):
            print(f"✅ Hyperopt results saved to {self.hyperopt_csv}")
        else:
            print("⚠️  Warning: Failed to save hyperopt results to CSV")
            logger.warning("Failed to save hyperopt results to CSV")
        
        # Step 3: Run backtesting
        print("\n📍 STEP 3/5: Running Backtesting...")
        backtest_results = self.run_backtesting()
        if not backtest_results:
            print("💥 AUTOMATION STOPPED: Backtesting failed")
            logger.error("Backtesting failed, stopping automation")
            return False
        
        # Step 4: Save backtesting results
        print("\n📍 STEP 4/5: Saving Backtest Results...")
        if self.save_to_csv(backtest_results, self.backtest_csv):
            print(f"✅ Backtest results saved to {self.backtest_csv}")
        else:
            print("⚠️  Warning: Failed to save backtest results to CSV")
            logger.warning("Failed to save backtesting results to CSV")
        
        # Step 5: Save formatted log with command outputs and performance evaluation
        print("\n📍 STEP 5/5: Generating Report and Evaluation...")
        strategy = self.config['strategy']
        random_state = self.config['random_state']
        log_filename = f"{strategy}-{random_state}.md"
        
        if self.save_formatted_log(self.hyperopt_output, self.backtest_output, 
                                 self.hyperopt_command, self.backtest_command,
                                 hyperopt_results, backtest_results):
            print(f"✅ Detailed report saved to {log_filename}")
        else:
            print("⚠️  Warning: Failed to save formatted log file")
            logger.warning("Failed to save formatted log file")
        
        # Step 6: Evaluate and display performance in console
        print("\n" + "=" * 50)
        print("📊 PERFORMANCE EVALUATION")
        print("=" * 50)

        performance_status, performance_description = self.evaluate_performance(hyperopt_results, backtest_results)
        print(f"Status: {performance_status}")
        print(f"Details: {performance_description}")
        
        logger.info("=" * 60)
        logger.info(f"PERFORMANCE EVALUATION: {performance_status}")
        logger.info(f"Details: {performance_description}")
        logger.info("=" * 60)
        
        print("\n" + "🎉" * 50)
        print("✅ AUTOMATION COMPLETED SUCCESSFULLY!")
        print("🎉" * 50)
        print(f"⏰ Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        logger.info("Full automation completed successfully!")
        return True

def main():
    """Main entry point"""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Freqtrade Automation Script')
    parser.add_argument('--mode', choices=['full', 'hyperopt', 'backtest'], default='full',
                       help='Run mode: full (hyperopt+backtest), hyperopt only, or backtest only')
    parser.add_argument('--strategy', type=str, default='IchimokuRebondStrategy',
                       help='Trading strategy to use')
    parser.add_argument('--timeframe', type=str, default='1h',
                       help='Timeframe for analysis')
    parser.add_argument('--epochs', type=int, default=100,
                       help='Number of hyperopt epochs')
    parser.add_argument('--random-state', type=int, default=None,
                       help='Random state for reproducibility (auto-generated if not specified)')
    
    args = parser.parse_args()
    
    # Print startup banner
    print("=" * 80)
    print("🤖 FREQTRADE AUTOMATION SCRIPT")
    if args.mode == 'full':
        print("🔥 Hyperopt + Backtesting Workflow")
    elif args.mode == 'hyperopt':
        print("🔍 Hyperopt Only")
    elif args.mode == 'backtest':
        print("📊 Backtest Only")
    print("=" * 80)
    
    # Configuration - modify these parameters as needed
    config = {
        'strategy': args.strategy,
        'timeframe': args.timeframe,
        'hyperopt_loss': 'OnlyProfitHyperOptLoss',
        # 'hyperopt_loss': 'SharpeHyperOptLoss',
        # 'hyperopt_loss': 'SortinoHyperOptLoss',
        # 'hyperopt_loss': 'CalmarHyperOptLoss',
        # 'spaces': 'sell buy',
        'spaces': 'roi',
        'random_state': args.random_state if args.random_state else Random().randint(1, 10000),
        'epochs': args.epochs,
        'hyperopt_timerange': '20170801-20231231',
        'backtest_timerange': '20170801-20231231'
        # 'backtest_timerange': '20240101-20251231'
    }
    
    print("⚙️  CONFIGURATION:")
    for key, value in config.items():
        print(f"   {key}: {value}")
    print(f"   mode: {args.mode}")
    print("=" * 80)
    
    # Initialize automation
    automation = FreqtradeAutomation(config)
    
    # Run based on mode
    if args.mode == 'full':
        success = automation.run_full_automation()
        result_files = [automation.hyperopt_csv, automation.backtest_csv]
        workflow = "FULL AUTOMATION"
    elif args.mode == 'hyperopt':
        success = automation.run_hyperopt_only()
        result_files = [automation.hyperopt_csv]
        workflow = "HYPEROPT"
    elif args.mode == 'backtest':
        success = automation.run_backtest_only()
        result_files = [automation.backtest_csv]
        workflow = "BACKTEST"
    
    if success:
        print("\n" + "🎉" * 20)
        print(f"✅ {workflow} COMPLETED SUCCESSFULLY!")
        print("📊 Results saved to:")
        for file in result_files:
            print(f"   - {file}")
        print("🎉" * 20)
    else:
        print("\n" + "💥" * 20)
        print(f"❌ {workflow} FAILED")
        print("📋 Check logs for details:")
        print("   - freqtrade_automation.log")
        print("💥" * 20)
        sys.exit(1)

if __name__ == "__main__":
    main()