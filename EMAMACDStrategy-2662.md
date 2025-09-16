# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 26 / 0.07, Median: -2.28%, Total profit: -0.35%, Sortino: -0.04, Sharpe: -0.01, Calmar: -0.11, Drawdown: 0%)

---
            
**Strategy:** EMAMACDStrategy  
**Random State:** 2662  
**Timestamp:** 2025-09-16 15:54:14

## Configuration
```json
{
  "strategy": "EMAMACDStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 2662,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy EMAMACDStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 2662
```

## Hyperopt Output
```
2025-09-16 13:52:18,783 - freqtrade - INFO - freqtrade 2025.8
2025-09-16 13:52:19,605 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-16 13:52:22,057 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-16 13:52:22,064 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-16 13:52:22,065 - freqtrade.loggers - INFO - Logfile configured
2025-09-16 13:52:22,065 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-16 13:52:22,066 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-16 13:52:22,067 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-16 13:52:22,067 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-16 13:52:22,437 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-16 13:52:22,439 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-16 13:52:22,440 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-16 13:52:22,440 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 100 epochs ...
2025-09-16 13:52:22,441 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-16 13:52:22,441 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-16 13:52:22,442 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-16 13:52:22,442 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 2662
2025-09-16 13:52:22,442 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-16 13:52:22,443 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-16 13:52:22,443 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-16 13:52:22,444 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-16 13:52:22,446 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-16 13:52:22,458 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-16 13:52:22,459 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 13:52:22,462 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-16 13:52:22,469 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-16 13:52:22,476 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-16 13:52:22,477 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-16 13:52:22,500 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-16 13:52:25,026 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-16 13:52:25,104 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy EMAMACDStrategy from '/freqtrade/user_data/strategies/EMAMACDStrategy.py'...
2025-09-16 13:52:25,108 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/EMAMACDStrategy.json
2025-09-16 13:52:25,112 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-16 13:52:25,113 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-16 13:52:25,114 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-16 13:52:25,114 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-16 13:52:25,115 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-16 13:52:25,116 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-16 13:52:25,116 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-16 13:52:25,117 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-16 13:52:25,117 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-16 13:52:25,117 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-16 13:52:25,118 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-16 13:52:25,118 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-16 13:52:25,118 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-16 13:52:25,119 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-16 13:52:25,119 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-16 13:52:25,119 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-16 13:52:25,120 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-16 13:52:25,120 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-16 13:52:25,121 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-16 13:52:25,121 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-16 13:52:25,121 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-16 13:52:25,122 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-16 13:52:25,122 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-16 13:52:25,122 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-16 13:52:25,123 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-16 13:52:25,123 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-16 13:52:25,123 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-16 13:52:25,124 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-16 13:52:25,124 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-16 13:52:25,125 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 13:52:25,154 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-16 13:52:25,180 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-16 13:52:25,183 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): macd_threshold = 0
2025-09-16 13:52:25,184 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.406
2025-09-16 13:52:25,185 - freqtrade.strategy.hyper - INFO - Strategy Parameter: window_macd_cross = 3
2025-09-16 13:52:25,186 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-09-16 13:52:25,186 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-16 13:52:25,187 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-16 13:52:25,187 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-16 13:52:25,188 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-16 13:52:25,210 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-16 13:52:25,211 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 2662
2025-09-16 13:52:25,268 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-16 13:52:25,334 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-16 13:52:25,342 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-16 13:52:25,393 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-16 13:52:25,461 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-16 13:52:25,542 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-16 13:52:25,552 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-16 13:52:25,566 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-16 13:52:26,269 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-16 13:52:34,717 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-16 13:52:35,105 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 16 CPU cores. Let's make them scream!
2025-09-16 13:52:35,106 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-16 13:52:35,107 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-16 13:52:35,107] A new study created in memory with name: no-name-46924a01-5760-4045-a106-f8091ca3cc06
2025-09-16 13:52:35,166 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                           Hyperopt results                                                                                             
                          ┏━━━━━━━━┳━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓                           
                          ┃ Best   ┃ Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃     Avg duration ┃ Objective ┃    Max Drawdown (Acct) ┃                           
                          ┡━━━━━━━━╇━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩                           
                          │ * Best │ 9/100 │     13 │    3     0    10  23.1 │     -1.79% │ -58.660 USDT   (-5.87%) │ 2 days, 16:55:00 │   0.05612 │ 91.293 USDT    (9.13%) │                           
                          └────────┴───────┴────────┴────────────────────────┴────────────┴─────────────────────────┴──────────────────┴───────────┴────────────────────────┘                           
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100/100 100% • 0:01:09 • 0:00:00
2025-09-16 13:53:44,536 - freqtrade.optimize.hyperopt.hyperopt - INFO - 100 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_EMAMACDStrategy_2025-09-16_13-52-22.fthypt'.
2025-09-16 13:53:44,883 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/EMAMACDStrategy.json

Best result:

*    9/100:     13 trades. 3/0/10 Wins/Draws/Losses. Avg profit  -1.79%. Median profit  -2.28%. Total profit -58.66023528 USDT (  -5.87%). Avg duration 2 days, 16:55:00 min. Objective: 0.05612

{"params":{"macd_threshold":0,"volume_factor":1.201,"window_macd_cross":7,"stoploss_margin":0.998,"lookback_period_for_stoploss":5,"take_profit_multiplier":2,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy EMAMACDStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20221231
```

## Backtesting Output
```
2025-09-16 13:53:49,398 - freqtrade - INFO - freqtrade 2025.8
2025-09-16 13:53:49,772 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-16 13:53:51,481 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-16 13:53:51,490 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-16 13:53:51,491 - freqtrade.loggers - INFO - Logfile configured
2025-09-16 13:53:51,491 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-16 13:53:51,492 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-16 13:53:51,493 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-16 13:53:51,494 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-16 13:53:51,495 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20221231 ...
2025-09-16 13:53:51,907 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-16 13:53:51,910 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-16 13:53:51,911 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-16 13:53:51,911 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-16 13:53:51,912 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-16 13:53:51,913 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20221231
2025-09-16 13:53:51,915 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-16 13:53:51,930 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-16 13:53:51,931 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 13:53:51,934 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-16 13:53:51,935 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-16 13:53:51,936 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-16 13:53:51,971 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-16 13:53:54,280 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-16 13:53:54,357 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy EMAMACDStrategy from '/freqtrade/user_data/strategies/EMAMACDStrategy.py'...
2025-09-16 13:53:54,359 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/EMAMACDStrategy.json
2025-09-16 13:53:54,362 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-16 13:53:54,363 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-16 13:53:54,363 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-16 13:53:54,363 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-16 13:53:54,364 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-16 13:53:54,364 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-16 13:53:54,365 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-16 13:53:54,365 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-16 13:53:54,365 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-16 13:53:54,366 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-16 13:53:54,366 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-16 13:53:54,366 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-16 13:53:54,367 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-16 13:53:54,367 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-16 13:53:54,367 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-16 13:53:54,368 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-16 13:53:54,369 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-16 13:53:54,369 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-16 13:53:54,371 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-16 13:53:54,372 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-16 13:53:54,373 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-16 13:53:54,373 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-16 13:53:54,374 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-16 13:53:54,375 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-16 13:53:54,375 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-16 13:53:54,376 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-16 13:53:54,376 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-16 13:53:54,377 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-16 13:53:54,377 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 13:53:54,403 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-16 13:53:54,442 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-16 13:53:54,745 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2022-12-31 00:00:00 (364 days).
2025-09-16 13:53:56,700 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-16 13:53:56,723 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy EMAMACDStrategy
2025-09-16 13:53:56,725 - freqtrade.strategy.hyper - INFO - Strategy Parameter: macd_threshold = 0
2025-09-16 13:53:56,726 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1.201
2025-09-16 13:53:56,727 - freqtrade.strategy.hyper - INFO - Strategy Parameter: window_macd_cross = 7
2025-09-16 13:53:56,728 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-09-16 13:53:56,728 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-16 13:53:56,729 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-16 13:53:56,730 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-16 13:53:56,730 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-16 13:54:01,006 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2022-12-31 00:00:00 (364 days).
2025-09-16 13:54:13,021 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-16_13-54-13.meta.json"
Result for strategy EMAMACDStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │      3 │         8.62 │          83.583 │         8.36 │ 9 days, 17:37:00 │    3     0     0   100 │
│ XRP/USDT │      7 │         1.03 │          34.078 │         3.41 │  2 days, 1:05:00 │    3     0     4  42.9 │
│ LTC/USDT │      5 │         1.29 │          30.126 │         3.01 │   1 day, 9:52:00 │    2     0     3  40.0 │
│ BNB/USDT │      4 │        -1.29 │         -17.880 │        -1.79 │  2 days, 8:55:00 │    1     0     3  25.0 │
│ BTC/USDT │      7 │        -3.63 │        -133.418 │       -13.34 │ 2 days, 10:15:00 │    0     0     7     0 │
│    TOTAL │     26 │         0.35 │          -3.511 │        -0.35 │ 2 days, 23:07:00 │    9     0    17  34.6 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                  ENTER TAG STATS                                                  
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │      26 │         0.35 │          -3.511 │        -0.35 │ 2 days, 23:07:00 │    9     0    17  34.6 │
│     TOTAL │      26 │         0.35 │          -3.511 │        -0.35 │ 2 days, 23:07:00 │    9     0    17  34.6 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │     9 │         7.69 │         296.396 │        29.64 │ 4 days, 12:10:00 │    9     0     0   100 │
│      stop_loss │    17 │        -3.54 │        -299.907 │       -29.99 │  2 days, 3:31:00 │    0     0    17     0 │
│          TOTAL │    26 │         0.35 │          -3.511 │        -0.35 │ 2 days, 23:07:00 │    9     0    17  34.6 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                          MIXED TAG STATS                                                          
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │      9 │         7.69 │         296.396 │        29.64 │ 4 days, 12:10:00 │    9     0     0   100 │
│           │      stop_loss │     17 │        -3.54 │        -299.907 │       -29.99 │  2 days, 3:31:00 │    0     0    17     0 │
│     TOTAL │                │     26 │         0.35 │          -3.511 │        -0.35 │ 2 days, 23:07:00 │    9     0    17  34.6 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00             │
│ Backtesting to                │ 2022-12-31 00:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 26 / 0.07                       │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 996.489 USDT                    │
│ Absolute profit               │ -3.511 USDT                     │
│ Total profit %                │ -0.35%                          │
│ CAGR %                        │ -0.35%                          │
│ Sortino                       │ -0.04                           │
│ Sharpe                        │ -0.01                           │
│ Calmar                        │ -0.11                           │
│ SQN                           │ -0.03                           │
│ Profit factor                 │ 0.99                            │
│ Expectancy (Ratio)            │ -0.14 (-0.01)                   │
│ Avg. daily profit             │ -0.01 USDT                      │
│ Avg. stake amount             │ 538.937 USDT                    │
│ Total trade volume            │ 28077.327 USDT                  │
│                               │                                 │
│ Best Pair                     │ ETH/USDT 8.36%                  │
│ Worst Pair                    │ BTC/USDT -13.34%                │
│ Best trade                    │ ETH/USDT 17.30%                 │
│ Worst trade                   │ XRP/USDT -5.43%                 │
│ Best day                      │ 41.224 USDT                     │
│ Worst day                     │ -31.869 USDT                    │
│ Days win/draw/lose            │ 8 / 327 / 16                    │
│ Min/Max/Avg. Duration Winners │ 0d 01:35 / 27d 18:40 / 4d 12:10 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 8d 11:20 / 2d 03:31  │
│ Max Consecutive Wins / Loss   │ 2 / 6                           │
│ Rejected Entry signals        │ 0                               │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 909.595 USDT                    │
│ Max balance                   │ 1084.361 USDT                   │
│ Max % of account underwater   │ 16.12%                          │
│ Absolute drawdown             │ 174.766 USDT (16.12%)           │
│ Drawdown duration             │ 181 days 02:20:00               │
│ Profit at drawdown start      │ 84.361 USDT                     │
│ Profit at drawdown end        │ -90.405 USDT                    │
│ Drawdown start                │ 2022-03-24 15:40:00             │
│ Drawdown end                  │ 2022-09-21 18:00:00             │
│ Market change                 │ -59.72%                         │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                               STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃        Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ EMAMACDStrategy │     26 │         0.35 │          -3.511 │        -0.35 │ 2 days, 23:07:00 │    9     0    17  34.6 │ 174.766 USDT  16.12% │
└─────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┴──────────────────────┘

```
