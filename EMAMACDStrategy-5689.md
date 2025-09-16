# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 5 / 0.01, Median: -4.22%, Total profit: -2.59%, Sortino: -0.35, Sharpe: -0.06, Calmar: -2.62, Drawdown: 0%)

---
            
**Strategy:** EMAMACDStrategy  
**Random State:** 5689  
**Timestamp:** 2025-09-16 15:57:11

## Configuration
```json
{
  "strategy": "EMAMACDStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 5689,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy EMAMACDStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 5689
```

## Hyperopt Output
```
2025-09-16 13:55:27,703 - freqtrade - INFO - freqtrade 2025.8
2025-09-16 13:55:28,201 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-16 13:55:29,487 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-16 13:55:29,493 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-16 13:55:29,494 - freqtrade.loggers - INFO - Logfile configured
2025-09-16 13:55:29,494 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-16 13:55:29,494 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-16 13:55:29,495 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-16 13:55:29,495 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-16 13:55:29,781 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-16 13:55:29,784 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-16 13:55:29,785 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-16 13:55:29,785 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 100 epochs ...
2025-09-16 13:55:29,785 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-16 13:55:29,786 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-16 13:55:29,786 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-16 13:55:29,787 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 5689
2025-09-16 13:55:29,787 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-16 13:55:29,787 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-16 13:55:29,788 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-16 13:55:29,788 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-16 13:55:29,789 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-16 13:55:29,799 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-16 13:55:29,800 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 13:55:29,802 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-16 13:55:29,809 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-16 13:55:29,815 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-16 13:55:29,815 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-16 13:55:29,835 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-16 13:55:33,793 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-16 13:55:33,844 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy EMAMACDStrategy from '/freqtrade/user_data/strategies/EMAMACDStrategy.py'...
2025-09-16 13:55:33,845 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2025-09-16 13:55:33,846 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-16 13:55:33,846 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-16 13:55:33,847 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-16 13:55:33,847 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-16 13:55:33,847 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-16 13:55:33,848 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-16 13:55:33,848 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-16 13:55:33,848 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-16 13:55:33,849 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-16 13:55:33,849 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-16 13:55:33,849 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-16 13:55:33,850 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-16 13:55:33,850 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-16 13:55:33,850 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-16 13:55:33,850 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-16 13:55:33,851 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-16 13:55:33,851 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-16 13:55:33,852 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-16 13:55:33,852 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-16 13:55:33,852 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-16 13:55:33,853 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-16 13:55:33,853 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-16 13:55:33,853 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-16 13:55:33,854 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-16 13:55:33,854 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-16 13:55:33,854 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-16 13:55:33,854 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-16 13:55:33,855 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-16 13:55:33,855 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-16 13:55:33,855 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 13:55:33,871 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-16 13:55:33,894 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-16 13:55:33,895 - freqtrade.strategy.hyper - INFO - No params for buy found, using default values.
2025-09-16 13:55:33,896 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): macd_threshold = 0
2025-09-16 13:55:33,896 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): volume_factor = 1.0
2025-09-16 13:55:33,896 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): window_macd_cross = 5
2025-09-16 13:55:33,897 - freqtrade.strategy.hyper - INFO - No params for sell found, using default values.
2025-09-16 13:55:33,897 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): lookback_period_for_stoploss = 5
2025-09-16 13:55:33,897 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): stoploss_margin = 0.999
2025-09-16 13:55:33,898 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): take_profit_multiplier = 2
2025-09-16 13:55:33,898 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_stoploss_param = True
2025-09-16 13:55:33,898 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-16 13:55:33,913 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-16 13:55:33,914 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 5689
2025-09-16 13:55:33,959 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-16 13:55:34,011 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-16 13:55:34,018 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-16 13:55:34,060 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-16 13:55:34,104 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-16 13:55:34,152 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-16 13:55:34,160 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-16 13:55:34,170 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-16 13:55:34,743 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-16 13:55:42,580 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-16 13:55:42,960 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 16 CPU cores. Let's make them scream!
2025-09-16 13:55:42,960 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-16 13:55:42,961 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-16 13:55:42,962] A new study created in memory with name: no-name-a7d25a47-f015-478d-bac3-dcb41993d4a7
2025-09-16 13:55:43,009 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                          ┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓                          
                          ┃ Best   ┃  Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃     Avg duration ┃ Objective ┃    Max Drawdown (Acct) ┃                          
                          ┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩                          
                          │ * Best │ 13/100 │      6 │    2     0     4  33.3 │     -1.37% │ -10.901 USDT   (-1.09%) │ 6 days, 18:30:00 │   0.00869 │ 63.558 USDT    (6.04%) │                          
                          │ Best   │ 51/100 │      7 │    3     0     4  42.9 │      0.53% │  29.905 USDT    (2.99%) │  6 days, 8:34:00 │  -0.02168 │ 66.186 USDT    (6.04%) │                          
                          │ Best   │ 71/100 │      7 │    3     0     4  42.9 │      0.47% │  29.970 USDT    (3.00%) │  7 days, 8:00:00 │  -0.02185 │ 66.084 USDT    (6.03%) │                          
                          └────────┴────────┴────────┴────────────────────────┴────────────┴─────────────────────────┴──────────────────┴───────────┴────────────────────────┘                          
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100/100 100% • 0:01:06 • 0:00:00
2025-09-16 13:56:49,742 - freqtrade.optimize.hyperopt.hyperopt - INFO - 100 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_EMAMACDStrategy_2025-09-16_13-55-29.fthypt'.
2025-09-16 13:56:49,906 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/EMAMACDStrategy.json

Best result:

    71/100:      7 trades. 3/0/4 Wins/Draws/Losses. Avg profit   0.47%. Median profit  -4.22%. Total profit 29.96959502 USDT (   3.00%). Avg duration 7 days, 8:00:00 min. Objective: -0.02185

{"params":{"macd_threshold":-1,"volume_factor":0.333,"window_macd_cross":4,"stoploss_margin":0.995,"lookback_period_for_stoploss":5,"take_profit_multiplier":2,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy EMAMACDStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20221231
```

## Backtesting Output
```
2025-09-16 13:56:54,036 - freqtrade - INFO - freqtrade 2025.8
2025-09-16 13:56:54,402 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-16 13:56:56,104 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-16 13:56:56,111 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-16 13:56:56,112 - freqtrade.loggers - INFO - Logfile configured
2025-09-16 13:56:56,112 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-16 13:56:56,113 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-16 13:56:56,113 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-16 13:56:56,114 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-16 13:56:56,114 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20221231 ...
2025-09-16 13:56:56,477 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-16 13:56:56,479 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-16 13:56:56,479 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-16 13:56:56,479 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-16 13:56:56,480 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-16 13:56:56,480 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20221231
2025-09-16 13:56:56,481 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-16 13:56:56,494 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-16 13:56:56,494 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 13:56:56,497 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-16 13:56:56,497 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-16 13:56:56,498 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-16 13:56:56,518 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-16 13:56:58,983 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-16 13:56:59,054 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy EMAMACDStrategy from '/freqtrade/user_data/strategies/EMAMACDStrategy.py'...
2025-09-16 13:56:59,057 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/EMAMACDStrategy.json
2025-09-16 13:56:59,062 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-16 13:56:59,063 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-16 13:56:59,063 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-16 13:56:59,064 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-16 13:56:59,064 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-16 13:56:59,065 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-16 13:56:59,066 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-16 13:56:59,066 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-16 13:56:59,067 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-16 13:56:59,067 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-16 13:56:59,068 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-16 13:56:59,068 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-16 13:56:59,069 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-16 13:56:59,069 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-16 13:56:59,070 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-16 13:56:59,071 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-16 13:56:59,071 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-16 13:56:59,072 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-16 13:56:59,072 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-16 13:56:59,073 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-16 13:56:59,073 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-16 13:56:59,074 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-16 13:56:59,074 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-16 13:56:59,075 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-16 13:56:59,076 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-16 13:56:59,077 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-16 13:56:59,078 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-16 13:56:59,079 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-16 13:56:59,080 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 13:56:59,101 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-16 13:56:59,130 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-16 13:56:59,425 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2022-12-31 00:00:00 (364 days).
2025-09-16 13:57:01,585 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-16 13:57:01,605 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy EMAMACDStrategy
2025-09-16 13:57:01,605 - freqtrade.strategy.hyper - INFO - Strategy Parameter: macd_threshold = -1
2025-09-16 13:57:01,606 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.333
2025-09-16 13:57:01,606 - freqtrade.strategy.hyper - INFO - Strategy Parameter: window_macd_cross = 4
2025-09-16 13:57:01,607 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-09-16 13:57:01,608 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.995
2025-09-16 13:57:01,608 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-16 13:57:01,609 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-16 13:57:01,609 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-16 13:57:06,145 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2022-12-31 00:00:00 (364 days).
2025-09-16 13:57:10,012 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-16_13-57-09.meta.json"
Result for strategy EMAMACDStrategy
                                               BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │      0 │          0.0 │           0.000 │          0.0 │            0:00 │    0     0     0     0 │
│ LTC/USDT │      0 │          0.0 │           0.000 │          0.0 │            0:00 │    0     0     0     0 │
│ XRP/USDT │      0 │          0.0 │           0.000 │          0.0 │            0:00 │    0     0     0     0 │
│ BNB/USDT │      0 │          0.0 │           0.000 │          0.0 │            0:00 │    0     0     0     0 │
│ BTC/USDT │      5 │         1.58 │         -25.902 │        -2.59 │ 4 days, 4:19:00 │    1     0     4  20.0 │
│    TOTAL │      5 │         1.58 │         -25.902 │        -2.59 │ 4 days, 4:19:00 │    1     0     4  20.0 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 ENTER TAG STATS                                                  
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │       5 │         1.58 │         -25.902 │        -2.59 │ 4 days, 4:19:00 │    1     0     4  20.0 │
│     TOTAL │       5 │         1.58 │         -25.902 │        -2.59 │ 4 days, 4:19:00 │    1     0     4  20.0 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                   EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │     1 │        17.57 │          37.748 │         3.77 │ 19 days, 12:50:00 │    1     0     0   100 │
│      stop_loss │     4 │        -2.42 │         -63.650 │        -6.36 │           8:11:00 │    0     0     4     0 │
│          TOTAL │     5 │         1.58 │         -25.902 │        -2.59 │   4 days, 4:19:00 │    1     0     4  20.0 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                          MIXED TAG STATS                                                           
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │      1 │        17.57 │          37.748 │         3.77 │ 19 days, 12:50:00 │    1     0     0   100 │
│           │      stop_loss │      4 │        -2.42 │         -63.650 │        -6.36 │           8:11:00 │    0     0     4     0 │
│     TOTAL │                │      5 │         1.58 │         -25.902 │        -2.59 │   4 days, 4:19:00 │    1     0     4  20.0 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                           SUMMARY METRICS                           
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                             ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00               │
│ Backtesting to                │ 2022-12-31 00:00:00               │
│ Trading Mode                  │ Spot                              │
│ Max open trades               │ 3                                 │
│                               │                                   │
│ Total/Daily Avg Trades        │ 5 / 0.01                          │
│ Starting balance              │ 1000 USDT                         │
│ Final balance                 │ 974.098 USDT                      │
│ Absolute profit               │ -25.902 USDT                      │
│ Total profit %                │ -2.59%                            │
│ CAGR %                        │ -2.60%                            │
│ Sortino                       │ -0.35                             │
│ Sharpe                        │ -0.06                             │
│ Calmar                        │ -2.62                             │
│ SQN                           │ -0.48                             │
│ Profit factor                 │ 0.59                              │
│ Expectancy (Ratio)            │ -5.18 (-0.33)                     │
│ Avg. daily profit             │ -0.071 USDT                       │
│ Avg. stake amount             │ 701.085 USDT                      │
│ Total trade volume            │ 6998.928 USDT                     │
│                               │                                   │
│ Best Pair                     │ ETH/USDT 0.00%                    │
│ Worst Pair                    │ BTC/USDT -2.59%                   │
│ Best trade                    │ BTC/USDT 17.57%                   │
│ Worst trade                   │ BTC/USDT -5.20%                   │
│ Best day                      │ 37.748 USDT                       │
│ Worst day                     │ -20.552 USDT                      │
│ Days win/draw/lose            │ 1 / 325 / 4                       │
│ Min/Max/Avg. Duration Winners │ 19d 12:50 / 19d 12:50 / 19d 12:50 │
│ Min/Max/Avg. Duration Losers  │ 0d 07:30 / 0d 09:20 / 0d 08:11    │
│ Max Consecutive Wins / Loss   │ 1 / 3                             │
│ Rejected Entry signals        │ 0                                 │
│ Entry/Exit Timeouts           │ 0 / 0                             │
│                               │                                   │
│ Min balance                   │ 948.1 USDT                        │
│ Max balance                   │ 985.847 USDT                      │
│ Max % of account underwater   │ 5.19%                             │
│ Absolute drawdown             │ 51.9 USDT (5.19%)                 │
│ Drawdown duration             │ 76 days 13:10:00                  │
│ Profit at drawdown start      │ -20.552 USDT                      │
│ Profit at drawdown end        │ -51.9 USDT                        │
│ Drawdown start                │ 2022-01-24 09:20:00               │
│ Drawdown end                  │ 2022-04-10 22:30:00               │
│ Market change                 │ -59.72%                           │
└───────────────────────────────┴───────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                             STRATEGY SUMMARY                                                             
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃        Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃         Drawdown ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ EMAMACDStrategy │      5 │         1.58 │         -25.902 │        -2.59 │ 4 days, 4:19:00 │    1     0     4  20.0 │ 51.9 USDT  5.19% │
└─────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴──────────────────┘

```
