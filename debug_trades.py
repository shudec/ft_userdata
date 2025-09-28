#!/usr/bin/env python3

import json
import zipfile
import os

# Find the newest backtest results zip file
backtest_dir = "user_data/backtest_results"
zip_files = [f for f in os.listdir(backtest_dir) if f.endswith('.zip')]
if not zip_files:
    print("No zip files found in backtest_results")
    exit(1)

zip_files.sort(reverse=True)  # Get the most recent
zip_path = os.path.join(backtest_dir, zip_files[0])
trades_file_path = zip_files[0].replace('.zip', '.json')

print(f"[+] Using backtest file: {zip_path}")
print(f"[+] Looking for trades file: {trades_file_path}")

# Load the trades data
try:
    with zipfile.ZipFile(zip_path, 'r') as z:
        with z.open(trades_file_path) as f:
            trades_data = json.load(f)
    
    print(f"trades_data type: {type(trades_data)}")
    
    if isinstance(trades_data, dict):
        print(f"Top-level keys: {list(trades_data.keys())}")
        
        # Explore strategy_comparison in detail
        if 'strategy_comparison' in trades_data:
            strategy_comp = trades_data['strategy_comparison']
            print(f"strategy_comparison: {type(strategy_comp)} with {len(strategy_comp)} items")
            for i, item in enumerate(strategy_comp):
                print(f"  Item {i}: {type(item)}")
                if isinstance(item, dict):
                    print(f"    Keys: {list(item.keys())}")
                    for key, value in item.items():
                        print(f"      {key}: {type(value)}")
                        if key == 'trades' and isinstance(value, int):
                            print(f"        trades count: {value}")
        
        # Let's also explore the strategy section 
        if 'strategy' in trades_data:
            strategy_data = trades_data['strategy']
            print(f"\nstrategy section: {type(strategy_data)}")
            for strategy_name, strategy_content in strategy_data.items():
                print(f"  Strategy '{strategy_name}': {type(strategy_content)}")
                if isinstance(strategy_content, dict):
                    print(f"    Keys: {list(strategy_content.keys())}")
                    if 'trades' in strategy_content:
                        trades_val = strategy_content['trades']
                        print(f"      trades: {type(trades_val)}")
                        if isinstance(trades_val, list):
                            print(f"        trades list length: {len(trades_val)}")
                            if len(trades_val) > 0:
                                print(f"        first trade: {trades_val[0]}")
                    # Look for any list that might contain trades
                    for key, value in strategy_content.items():
                        if isinstance(value, list) and len(value) > 0:
                            print(f"      {key}: list with {len(value)} items")
                            if isinstance(value[0], dict):
                                print(f"        first item keys: {list(value[0].keys())}")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
