#!/usr/bin/env python3
"""
Freqtrade Interactive Daemon Script
Provides an interactive menu for running Freqtrade commands with Podman Compose
"""

import os
import sys
import json
import subprocess
import glob
import ast
import inspect
from pathlib import Path
from typing import List, Dict, Optional


class FreqtradeDaemon:
    def __init__(self):
        self.strategy = None
        self.pairs = []
        self.timeframe = None
        self.backtest_timerange = None
        self.hyperopt_timerange = None
        self.user_data_path = "user_data"
        self.config_path = "user_data/config.json"
        self.strategies_path = "user_data/strategies"
        
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def get_available_strategies(self) -> List[str]:
        """Get list of available strategies from the strategies folder by parsing class names"""
        try:
            strategy_files = glob.glob(f"{self.strategies_path}/*.py")
            strategies = []
            
            for file_path in strategy_files:
                filename = os.path.basename(file_path)
                if filename.startswith('__'):
                    continue
                    
                try:
                    # Read and parse the Python file
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Parse the AST to find class definitions
                    tree = ast.parse(content)
                    
                    for node in ast.walk(tree):
                        if isinstance(node, ast.ClassDef):
                            # Check if class inherits from IStrategy
                            for base in node.bases:
                                if (isinstance(base, ast.Name) and base.id == 'IStrategy') or \
                                   (isinstance(base, ast.Attribute) and base.attr == 'IStrategy'):
                                    strategies.append(node.name)
                                    break
                                    
                except Exception as e:
                    print(f"Error parsing {file_path}: {e}")
                    # Fallback to filename if parsing fails
                    strategy_name = filename.replace('.py', '')
                    if strategy_name != '__init__':
                        strategies.append(strategy_name)
            
            return sorted(strategies)
        except Exception as e:
            print(f"Error reading strategies folder: {e}")
            return []
    
    def get_pairs_from_config(self) -> List[str]:
        """Get pairs from config.json file"""
        try:
            with open(self.config_path, 'r') as f:
                config = json.load(f)
                return config.get('exchange', {}).get('pair_whitelist', [])
        except Exception as e:
            print(f"Error reading config.json: {e}")
            return []
    
    def select_strategy(self) -> bool:
        """Let user select a strategy"""
        strategies = self.get_available_strategies()
        if not strategies:
            print("No strategies found in the strategies folder!")
            return False
            
        print("\n=== Select Strategy ===")
        for i, strategy in enumerate(strategies, 1):
            print(f"{i}. {strategy}")
        
        try:
            choice = int(input(f"\nSelect strategy (1-{len(strategies)}): "))
            if 1 <= choice <= len(strategies):
                self.strategy = strategies[choice - 1]
                print(f"Selected strategy: {self.strategy}")
                return True
            else:
                print("Invalid choice!")
                return False
        except ValueError:
            print("Please enter a valid number!")
            return False
    
    def select_pairs(self) -> bool:
        """Let user select pairs from config.json"""
        available_pairs = self.get_pairs_from_config()
        if not available_pairs:
            print("No pairs found in config.json!")
            return False
            
        print("\n=== Select Pairs ===")
        print("Available pairs from config.json:")
        for i, pair in enumerate(available_pairs, 1):
            print(f"{i}. {pair}")
        
        print(f"\n{len(available_pairs) + 1}. Use all pairs")
        
        try:
            choice = input(f"\nSelect pairs (1-{len(available_pairs) + 1}, or comma-separated numbers): ")
            
            if choice.strip() == str(len(available_pairs) + 1):
                self.pairs = available_pairs
                print("Selected all pairs")
                return True
            
            # Handle comma-separated choices
            choices = [int(x.strip()) for x in choice.split(',')]
            selected_pairs = []
            
            for c in choices:
                if 1 <= c <= len(available_pairs):
                    selected_pairs.append(available_pairs[c - 1])
                else:
                    print(f"Invalid choice: {c}")
                    return False
            
            if selected_pairs:
                self.pairs = selected_pairs
                print(f"Selected pairs: {', '.join(self.pairs)}")
                return True
            else:
                print("No pairs selected!")
                return False
                
        except ValueError:
            print("Please enter valid numbers!")
            return False
    
    def select_timeframe(self) -> bool:
        """Let user select timeframe"""
        timeframes = ["1m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d", "3d", "1w"]
        
        print("\n=== Select Timeframe ===")
        for i, tf in enumerate(timeframes, 1):
            print(f"{i}. {tf}")
        
        try:
            choice = int(input(f"\nSelect timeframe (1-{len(timeframes)}): "))
            if 1 <= choice <= len(timeframes):
                self.timeframe = timeframes[choice - 1]
                print(f"Selected timeframe: {self.timeframe}")
                return True
            else:
                print("Invalid choice!")
                return False
        except ValueError:
            print("Please enter a valid number!")
            return False
    
    def select_timerange(self, operation_type: str) -> str:
        """Let user select timerange for specific operation"""
        print(f"\n=== Select Timerange for {operation_type} ===")
        
        # Predefined timeranges
        timeranges = [
            ("Last 7 days", "7"),
            ("Last 30 days", "30"),
            ("Last 3 months", "90"),
            ("Last 6 months", "180"),
            ("Last year", "365"),
            ("Custom range", "custom")
        ]
        
        print("Available timeranges:")
        for i, (description, _) in enumerate(timeranges, 1):
            print(f"{i}. {description}")
        
        print(f"{len(timeranges) + 1}. No timerange (use all available data)")
        
        try:
            choice = int(input(f"\nSelect timerange (1-{len(timeranges) + 1}): "))
            
            if choice == len(timeranges) + 1:
                print("Selected: No timerange (all data)")
                return None
            elif 1 <= choice <= len(timeranges):
                description, timerange_value = timeranges[choice - 1]
                
                if timerange_value == "custom":
                    print("\nEnter custom timerange:")
                    print("Format examples:")
                    print("  20240101-20241231 (from Jan 1 to Dec 31, 2024)")
                    print("  20240601- (from June 1, 2024 to present)")
                    print("  -20241201 (from beginning to Dec 1, 2024)")
                    
                    custom_range = input("Enter timerange: ").strip()
                    if custom_range:
                        print(f"Selected custom timerange: {custom_range}")
                        return custom_range
                    else:
                        print("No timerange entered!")
                        return None
                else:
                    # For predefined ranges, calculate actual dates
                    from datetime import datetime, timedelta
                    
                    end_date = datetime.now()
                    start_date = end_date - timedelta(days=int(timerange_value))
                    
                    timerange = f"{start_date.strftime('%Y%m%d')}-"
                    print(f"Selected: {description} ({timerange})")
                    return timerange
            else:
                print("Invalid choice!")
                return None
                
        except ValueError:
            print("Please enter a valid number!")
            return None

    def setup_parameters(self) -> bool:
        """Setup initial parameters"""
        print("=== Freqtrade Daemon Setup ===\n")
        
        # Check if paths exist
        if not os.path.exists(self.config_path):
            print(f"Config file not found: {self.config_path}")
            return False
            
        if not os.path.exists(self.strategies_path):
            print(f"Strategies folder not found: {self.strategies_path}")
            return False
        
        # Select strategy
        if not self.select_strategy():
            return False
        
        # Select pairs
        if not self.select_pairs():
            return False
            
        # Select timeframe
        if not self.select_timeframe():
            return False
        
        # Select timerange for backtesting
        self.backtest_timerange = self.select_timerange("Backtesting")
        if self.backtest_timerange is False:  # User cancelled
            return False
        
        # Select timerange for hyperopt
        self.hyperopt_timerange = self.select_timerange("Hyperopt")
        if self.hyperopt_timerange is False:  # User cancelled
            return False
        
        print(f"\n=== Configuration Complete ===")
        print(f"Strategy: {self.strategy}")
        print(f"Pairs: {', '.join(self.pairs)}")
        print(f"Timeframe: {self.timeframe}")
        print(f"Backtest Timerange: {self.backtest_timerange if self.backtest_timerange else 'All available data'}")
        print(f"Hyperopt Timerange: {self.hyperopt_timerange if self.hyperopt_timerange else 'All available data'}")
        
        return True
    
    def get_latest_backtest_file(self) -> Optional[str]:
        """Get the latest backtest result file from .last_result.json"""
        backtest_dir = f"{self.user_data_path}/backtest_results"
        last_result_file = f"{backtest_dir}/.last_result.json"
        
        if not os.path.exists(last_result_file):
            print(f"No .last_result.json file found in {backtest_dir}")
            return None
            
        try:
            with open(last_result_file, 'r') as f:
                last_result = json.load(f)
                latest_filename = last_result.get('latest_backtest')
                
                if not latest_filename:
                    print("No latest_backtest entry found in .last_result.json")
                    return None
                
                # Construct full path
                latest_file_path = f"{backtest_dir}/{latest_filename}"
                
                if not os.path.exists(latest_file_path):
                    print(f"Latest backtest file not found: {latest_file_path}")
                    return None
                    
                return latest_file_path
                
        except Exception as e:
            print(f"Error reading .last_result.json: {e}")
            return None

    def run_backtesting_analysis(self):
        """Run backtesting analysis on latest result"""
        latest_file = self.get_latest_backtest_file()
        
        if not latest_file:
            print("No backtest result files found!")
            return
        
        print(f"\nAnalyzing latest backtest result: {os.path.basename(latest_file)}")
        
        # Convert local path to container path for the backtest file
        # container_file_path = latest_file.replace(self.user_data_path, "/freqtrade/user_data").replace("\\", "/")
        
        cmd = [
            "podman-compose", "run", "--rm", "freqtrade", "backtesting-analysis",
            "--config", "/freqtrade/user_data/config.json",
            "--analysis-groups"
        ]
        
        # Add analysis groups as separate arguments
        cmd.extend(["0", "1", "2", "3", "4", "5"])
        
        # Add remaining arguments
        cmd.extend([
            "--enter-reason-list", "all",
            "--exit-reason-list", "all", 
            "--indicator-list", "all",
            "--backtest-filename", latest_file
        ])
        
        print(f"Command: {' '.join(cmd)}")
        
        try:
            result = subprocess.run(cmd, check=True, capture_output=False)
            print("\nBacktesting analysis completed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Backtesting analysis failed with error code {e.returncode}")
        except Exception as e:
            print(f"Error running backtesting analysis: {e}")

    def run_backtesting(self):
        """Run backtesting command"""
        pairs_str = " ".join(self.pairs)
        cmd = [
            "podman-compose", "run", "--rm", "freqtrade", "backtesting",
            "--config", "/freqtrade/user_data/config.json",
            "--strategy", self.strategy,
            "--timeframe", self.timeframe,
            "--export", "signals",
            "--pairs"] + self.pairs
        
        # Add timerange if specified
        if self.backtest_timerange:
            cmd.extend(["--timerange", self.backtest_timerange])
        
        print(f"\nRunning backtesting...")
        print(f"Command: {' '.join(cmd)}")
        
        try:
            result = subprocess.run(cmd, check=True, capture_output=False)
            print("\nBacktesting completed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Backtesting failed with error code {e.returncode}")
        except Exception as e:
            print(f"Error running backtesting: {e}")

    def run_hyperopt(self):
        """Run hyperopt with user-selected parameters"""
        print("\n=== Hyperopt Configuration ===")
        
        # Select hyperopt loss function
        loss_functions = [
            "SharpeHyperOptLoss",
            "SortinoHyperOptLoss", 
            "CalmarHyperOptLoss",
            "MaxDrawDownHyperOptLoss",
            "ProfitLoss",
            "ShortTradeDurHyperOptLoss"
        ]
        
        print("Available hyperopt loss functions:")
        for i, loss in enumerate(loss_functions, 1):
            print(f"{i}. {loss}")
        
        try:
            choice = int(input(f"\nSelect loss function (1-{len(loss_functions)}): "))
            if 1 <= choice <= len(loss_functions):
                loss_function = loss_functions[choice - 1]
            else:
                print("Invalid choice! Using default SharpeHyperOptLoss")
                loss_function = "SharpeHyperOptLoss"
        except ValueError:
            print("Invalid input! Using default SharpeHyperOptLoss")
            loss_function = "SharpeHyperOptLoss"
        
        # Select hyperopt spaces
        print("\n=== Select Hyperopt Spaces ===")
        spaces = [
            ("buy", "Optimize buy signal parameters"),
            ("sell", "Optimize sell signal parameters"),
            ("roi", "Optimize ROI table"),
            ("stoploss", "Optimize stoploss"),
            ("trailing", "Optimize trailing stoploss"),
            ("protection", "Optimize protection parameters")
        ]
        
        print("Available spaces:")
        for i, (space, description) in enumerate(spaces, 1):
            print(f"{i}. {space} - {description}")
        
        print(f"{len(spaces) + 1}. All spaces")
        
        try:
            choice = input(f"\nSelect spaces (1-{len(spaces) + 1}, or comma-separated numbers): ")
            
            if choice.strip() == str(len(spaces) + 1):
                selected_spaces = [space for space, _ in spaces]
                print("Selected all spaces")
            else:
                # Handle comma-separated choices
                choices = [int(x.strip()) for x in choice.split(',')]
                selected_spaces = []
                
                for c in choices:
                    if 1 <= c <= len(spaces):
                        selected_spaces.append(spaces[c - 1][0])
                    else:
                        print(f"Invalid choice: {c}")
                        return
                
                if not selected_spaces:
                    print("No spaces selected!")
                    return
                    
                print(f"Selected spaces: {', '.join(selected_spaces)}")
                
        except ValueError:
            print("Invalid input! Using all spaces")
            selected_spaces = [space for space, _ in spaces]
        
        # Get number of epochs
        try:
            epochs = int(input("Enter number of epochs (default 100): ") or "100")
        except ValueError:
            print("Invalid input! Using default 100 epochs")
            epochs = 100
        
        pairs_str = " ".join(self.pairs)
        cmd = [
            "podman-compose", "run", "--rm", "freqtrade", "hyperopt",
            "--config", "/freqtrade/user_data/config.json",
            "--hyperopt-loss", loss_function,
            "--strategy", self.strategy,
            "--timeframe", self.timeframe,
            "--epochs", str(epochs),
            "--spaces"] + selected_spaces + [
            "--pairs"] + self.pairs
        
        # Add timerange if specified
        if self.hyperopt_timerange:
            cmd.extend(["--timerange", self.hyperopt_timerange])
        
        print(f"\nRunning hyperopt...")
        print(f"Loss function: {loss_function}")
        print(f"Spaces: {', '.join(selected_spaces)}")
        print(f"Epochs: {epochs}")
        print(f"Command: {' '.join(cmd)}")
        
        try:
            result = subprocess.run(cmd, check=True, capture_output=False)
            print("\nHyperopt completed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Hyperopt failed with error code {e.returncode}")
        except Exception as e:
            print(f"Error running hyperopt: {e}")

    def show_main_menu(self):
        """Show main menu and handle user choice"""
        while True:
            self.clear_screen()
            print("=== Freqtrade Daemon ===")
            print(f"Strategy: {self.strategy}")
            print(f"Pairs: {', '.join(self.pairs)}")
            print(f"Timeframe: {self.timeframe}")
            print(f"Backtest Timerange: {self.backtest_timerange if self.backtest_timerange else 'All data'}")
            print(f"Hyperopt Timerange: {self.hyperopt_timerange if self.hyperopt_timerange else 'All data'}")
            print("\n=== Main Menu ===")
            print("1. Run Backtesting")
            print("2. Run Backtesting Analysis")
            print("3. Run Hyperopt")
            print("4. Reconfigure Parameters")
            print("5. Quit")
            
            try:
                choice = input("\nSelect option (1-5): ")
                
                if choice == "1":
                    self.run_backtesting()
                    input("\nPress Enter to continue...")
                    
                elif choice == "2":
                    self.run_backtesting_analysis()
                    input("\nPress Enter to continue...")
                    
                elif choice == "3":
                    self.run_hyperopt()
                    input("\nPress Enter to continue...")
                    
                elif choice == "4":
                    if not self.setup_parameters():
                        input("\nSetup failed! Press Enter to continue...")
                    
                elif choice == "5":
                    print("\nGoodbye!")
                    sys.exit(0)
                    
                else:
                    print("Invalid choice! Please select 1-5.")
                    input("Press Enter to continue...")
                    
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                sys.exit(0)
    
    def run(self):
        """Main entry point"""
        try:
            self.clear_screen()
            if not self.setup_parameters():
                print("Setup failed! Exiting...")
                sys.exit(1)
            
            input("\nPress Enter to continue to main menu...")
            self.show_main_menu()
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"Unexpected error: {e}")
            sys.exit(1)


if __name__ == "__main__":
    daemon = FreqtradeDaemon()
    daemon.run()