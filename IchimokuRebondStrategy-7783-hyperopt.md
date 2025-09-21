# Freqtrade Hyperopt Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 7783  
**Timestamp:** 2025-09-19 22:17:44

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 7783,
  "epochs": 200,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 200 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 7783
```

## Hyperopt Output
```
2025-09-19 20:14:19,320 - freqtrade - INFO - freqtrade 2025.7
2025-09-19 20:14:19,957 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-19 20:14:19,958 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-19 20:14:21,387 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-19 20:14:21,390 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-19 20:14:21,391 - freqtrade.loggers - INFO - Logfile configured
2025-09-19 20:14:21,391 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-19 20:14:21,391 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-19 20:14:21,392 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-19 20:14:21,392 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-19 20:14:21,400 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-19 20:14:21,401 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-19 20:14:21,401 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-19 20:14:21,402 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 200 epochs ...
2025-09-19 20:14:21,402 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['sell']
2025-09-19 20:14:21,402 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-19 20:14:21,403 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-19 20:14:21,403 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 7783
2025-09-19 20:14:21,403 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-19 20:14:21,404 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-19 20:14:21,404 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-19 20:14:21,405 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-19 20:14:21,406 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-19 20:14:21,425 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-19 20:14:21,426 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 20:14:21,430 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-19 20:14:21,431 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-19 20:14:21,436 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-19 20:14:21,437 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-19 20:14:21,470 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-19 20:14:23,908 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-19 20:14:23,947 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-19 20:14:23,947 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-19 20:14:23,949 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-19 20:14:23,949 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-19 20:14:23,949 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-19 20:14:23,950 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-19 20:14:23,950 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-19 20:14:23,951 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-19 20:14:23,951 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-19 20:14:23,952 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-19 20:14:23,952 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-19 20:14:23,952 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-19 20:14:23,953 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-19 20:14:23,953 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-19 20:14:23,953 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-19 20:14:23,954 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-19 20:14:23,954 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-19 20:14:23,955 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-19 20:14:23,955 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-19 20:14:23,955 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-19 20:14:23,956 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-19 20:14:23,956 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-19 20:14:23,956 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-19 20:14:23,957 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-19 20:14:23,957 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-19 20:14:23,957 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-19 20:14:23,958 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-19 20:14:23,958 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-19 20:14:23,958 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-19 20:14:23,959 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-19 20:14:23,959 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-19 20:14:23,960 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 20:14:23,965 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-19 20:14:24,002 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-19 20:14:24,004 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-19 20:14:24,004 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-19 20:14:24,005 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 4
2025-09-19 20:14:24,006 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.55
2025-09-19 20:14:24,006 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.9
2025-09-19 20:14:24,007 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.03
2025-09-19 20:14:24,007 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-19 20:14:24,008 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.001
2025-09-19 20:14:24,008 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-19 20:14:24,009 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 2
2025-09-19 20:14:24,010 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-09-19 20:14:24,010 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-19 20:14:24,010 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-19 20:14:24,011 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-19 20:14:24,011 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-19 20:14:24,019 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-19 20:14:24,020 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 7783
2025-09-19 20:14:24,056 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-19 20:14:24,106 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-19 20:14:24,114 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-19 20:14:24,151 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-19 20:14:24,198 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-19 20:14:24,236 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-19 20:14:24,244 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-19 20:14:24,262 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-19 20:14:25,084 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-19 20:14:25,086 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 20:14:25,094 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-19 20:14:26,840 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 20:14:26,847 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-19 20:14:28,570 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 20:14:28,577 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-19 20:14:30,119 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 20:14:30,125 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-19 20:14:31,338 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 20:14:31,344 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-19 20:14:32,931 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-19 20:14:33,226 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 20 CPU cores. Let's make them scream!
2025-09-19 20:14:33,226 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-19 20:14:33,228 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-19 20:14:33,228] A new study created in memory with name: no-name-6a8b9130-7524-4771-9c72-62707cbebdd3
2025-09-19 20:14:33,275 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                           ┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓                           
                           ┃ Best   ┃  Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃   Avg duration ┃ Objective ┃    Max Drawdown (Acct) ┃                           
                           ┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩                           
                           │ * Best │  1/200 │      9 │    6     0     3  66.7 │      2.11% │ 171.216 USDT   (17.12%) │        7:00:00 │  -0.12892 │ 53.634 USDT    (4.71%) │                           
                           │ * Best │  2/200 │      9 │    6     0     3  66.7 │      2.21% │ 186.772 USDT   (18.68%) │       12:13:00 │  -0.13471 │ 44.703 USDT    (3.92%) │                           
                           │ * Best │  3/200 │      9 │    6     0     3  66.7 │      2.66% │ 246.722 USDT   (24.67%) │       14:13:00 │  -0.15458 │ 58.837 USDT    (5.11%) │                           
                           │ * Best │  6/200 │      9 │    6     0     3  66.7 │      3.18% │ 264.217 USDT   (26.42%) │       17:33:00 │  -0.15966 │ 61.243 USDT    (5.29%) │                           
                           │ Best   │ 37/200 │      9 │    6     0     3  66.7 │      2.86% │ 270.627 USDT   (27.06%) │       22:47:00 │  -0.16265 │ 60.825 USDT    (5.26%) │                           
                           │ Best   │ 81/200 │      9 │    6     0     3  66.7 │      3.54% │ 331.583 USDT   (33.16%) │ 1 day, 2:13:00 │  -0.17352 │ 62.529 USDT    (5.35%) │                           
                           └────────┴────────┴────────┴────────────────────────┴────────────┴─────────────────────────┴────────────────┴───────────┴────────────────────────┘                           
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 200/200 100% • 0:03:09 • 0:00:00
2025-09-19 20:17:42,666 - freqtrade.optimize.hyperopt.hyperopt - INFO - 200 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-19_20-14-21.fthypt'.
2025-09-19 20:17:42,707 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

    81/200:      9 trades. 6/0/3 Wins/Draws/Losses. Avg profit   3.54%. Median profit   5.55%. Total profit 331.58300370 USDT (  33.16%). Avg duration 1 day, 2:13:00 min. Objective: -0.17352

{"params":{"confirmation_candle":true,"engulfing_size_threshold":1.5,"flat_kinjun_threshold":4,"hammer_body_threshold":0.55,"hammer_head_threshold":0.9,"hammer_strength_threshold":0.03,"kinjun_proximity_threshold":0.001,"tenkan_proximity_threshold":0.001,"kinjun_threshold":1.0,"lookback_period_for_stoploss":8,"stoploss_margin":0.994,"take_profit_multiplier":3,"use_sell_signal_param":false,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Hyperopt Results
```json
{
  "timestamp": "2025-09-19T22:17:44.757089",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 7783,
  "wins_draws_losses": "6/0/3",
  "avg_profit_pct": 3.54,
  "median_profit_pct": 5.55,
  "total_profit_usdt": 331.5830037,
  "avg_duration": "1 day, 2:13:00",
  "objective": -0.17352,
  "avg_profit_per_day": 3.2407
}
```
