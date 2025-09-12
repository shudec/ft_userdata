# Freqtrade Automation Script Usage Guide

## Overview
This script automates the process of running Freqtrade hyperopt optimization followed by backtesting. It saves results to CSV files that can be analyzed to compare different optimization runs.

## Files Created
- `freqtrade_automation.py` - Main automation script
- `automation_config_examples.py` - Configuration examples
- `hyperopt_results.csv` - Hyperopt results (created automatically)
- `backtest_results.csv` - Backtesting results (created automatically)
- `freqtrade_automation.log` - Execution log

## Quick Start

### 1. Basic Usage
```bash
python freqtrade_automation.py
```

### 2. Modify Configuration
Edit the `config` dictionary in `freqtrade_automation.py`:

```python
config = {
    'strategy': 'YourStrategyName',
    'timeframe': '15m',
    'hyperopt_loss': 'SharpeHyperOptLoss',
    'spaces': 'buy sell roi stoploss',
    'random_state': 42,
    'epochs': 100,
    'hyperopt_timerange': '20170801-20191231',
    'backtest_timerange': '20220101-20221231'
}
```

### 3. Run Multiple Optimizations
To test different parameters, run the script multiple times with different configurations:

```bash
# Run 1: Sharpe optimization
python freqtrade_automation.py

# Edit config for Sortino optimization and run again
python freqtrade_automation.py

# Edit config for different random state and run again
python freqtrade_automation.py
```

Each run will **append** results to the CSV files, so you can compare multiple optimizations.

## Configuration Parameters

### Required Parameters
- `strategy`: Name of your Freqtrade strategy
- `timeframe`: Trading timeframe (1m, 5m, 15m, 1h, etc.)
- `hyperopt_loss`: Optimization objective function
- `spaces`: What to optimize (buy, sell, roi, stoploss)
- `random_state`: Random seed for reproducible results

### Optional Parameters
- `epochs`: Number of hyperopt iterations (default: 100)
- `hyperopt_timerange`: Date range for optimization (default: '20170801-20191231')
- `backtest_timerange`: Date range for backtesting (default: '20220101-20221231')

## Output Files

### hyperopt_results.csv
Contains optimization results with columns:
- `random_state`: Random seed used
- `wins_draws_losses`: Win/Draw/Loss counts
- `avg_profit_pct`: Average profit percentage
- `median_profit_pct`: Median profit percentage
- `total_profit_usdt`: Total profit in USDT
- `avg_duration`: Average trade duration
- `objective`: Optimization objective value
- `avg_profit_per_day`: Calculated daily profit
- `param_*`: All optimized parameters
- `minimal_roi`: ROI table (JSON)
- `stoploss`: Stoploss value
- `timestamp`: When the optimization was run

### backtest_results.csv
Contains backtesting results with columns:
- `random_state`: Corresponding random seed
- `strategy`: Strategy name
- `total_daily_avg_trades`: Total and daily average trades
- `absolute_profit_usdt`: Absolute profit in USDT
- `total_profit_pct`: Total profit percentage
- `cagr_pct`: Compound Annual Growth Rate
- `sortino`: Sortino ratio
- `sharpe`: Sharpe ratio
- `calmar`: Calmar ratio
- `sqn`: System Quality Number
- `max_consecutive_wins_loss`: Max consecutive wins/losses
- `min_balance_usdt`: Minimum balance reached
- `max_balance_usdt`: Maximum balance reached
- `absolute_drawdown_pct`: Maximum drawdown percentage
- `market_change_pct`: Market change during period
- `win_draw_loss_winpct`: Win/Draw/Loss statistics
- `timestamp`: When the backtest was run

## Example Workflow

1. **Test different optimization objectives:**
   ```python
   # Run with Sharpe optimization
   config['hyperopt_loss'] = 'SharpeHyperOptLoss'
   config['random_state'] = 42
   
   # Run with Sortino optimization  
   config['hyperopt_loss'] = 'SortinoHyperOptLoss'
   config['random_state'] = 43
   
   # Run with Calmar optimization
   config['hyperopt_loss'] = 'CalmarHyperOptLoss'
   config['random_state'] = 44
   ```

2. **Test different optimization spaces:**
   ```python
   # Optimize everything
   config['spaces'] = 'buy sell roi stoploss'
   
   # Only optimize buy signals
   config['spaces'] = 'buy'
   
   # Only optimize ROI and stoploss
   config['spaces'] = 'roi stoploss'
   ```

3. **Test different timeframes:**
   ```python
   # 15-minute timeframe
   config['timeframe'] = '15m'
   
   # 1-hour timeframe
   config['timeframe'] = '1h'
   
   # 4-hour timeframe
   config['timeframe'] = '4h'
   ```

4. **Analyze results:**
   ```python
   import pandas as pd
   
   # Load and compare hyperopt results
   hyperopt_df = pd.read_csv('hyperopt_results.csv')
   print(hyperopt_df.sort_values('objective', ascending=False))
   
   # Load and compare backtest results
   backtest_df = pd.read_csv('backtest_results.csv')
   print(backtest_df.sort_values('total_profit_pct', ascending=False))
   ```

## Troubleshooting

### Common Issues
1. **Docker not running**: Make sure Docker and docker-compose are running
2. **Strategy not found**: Ensure the strategy file exists in user_data/strategies/
3. **Data missing**: Ensure you have downloaded data for the specified pairs and timeframes
4. **Permissions**: Make sure the script has write permissions for CSV files

### Logs
Check `freqtrade_automation.log` for detailed execution logs and error messages.

### Manual Testing
You can test the Docker commands manually:
```bash
# Test hyperopt command
docker compose run --rm freqtrade hyperopt --config /freqtrade/user_data/config.json --strategy RSIDivergenceBullishStrategy --timeframe 15m --epochs 1

# Test backtesting command  
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy RSIDivergenceBullishStrategy --timeframe 15m
```

## Advanced Usage

### Custom Optimization Loop
For running multiple optimizations programmatically:

```python
from freqtrade_automation import FreqtradeAutomation

# Define different configurations
configs = [
    {'strategy': 'Strategy1', 'random_state': 42, 'hyperopt_loss': 'SharpeHyperOptLoss'},
    {'strategy': 'Strategy1', 'random_state': 43, 'hyperopt_loss': 'SortinoHyperOptLoss'},
    {'strategy': 'Strategy2', 'random_state': 44, 'hyperopt_loss': 'SharpeHyperOptLoss'},
]

# Run all configurations
for i, config in enumerate(configs):
    print(f"Running configuration {i+1}/{len(configs)}")
    automation = FreqtradeAutomation(config)
    automation.run_full_automation()
```

This allows you to run batch optimizations and compare different strategies, parameters, and optimization objectives systematically.