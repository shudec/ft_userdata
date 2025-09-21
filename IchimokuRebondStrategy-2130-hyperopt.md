# Freqtrade Hyperopt Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 2130  
**Timestamp:** 2025-09-21 22:08:40

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "CalmarHyperOptLoss",
  "spaces": "sell buy roi",
  "random_state": 2130,
  "epochs": 200,
  "hyperopt_timerange": "20170801-20201231",
  "backtest_timerange": "20210101-20241231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss CalmarHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 200 --spaces sell buy roi --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20201231 --random-state 2130
```

## Hyperopt Output
```
2025-09-21 20:05:11,480 - freqtrade - INFO - freqtrade 2025.7
2025-09-21 20:05:12,065 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-21 20:05:12,066 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-21 20:05:13,381 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-21 20:05:13,385 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-21 20:05:13,386 - freqtrade.loggers - INFO - Logfile configured
2025-09-21 20:05:13,386 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-21 20:05:13,387 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-21 20:05:13,388 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-21 20:05:13,388 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20201231 ...
2025-09-21 20:05:13,399 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-21 20:05:13,400 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-21 20:05:13,401 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-21 20:05:13,401 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 200 epochs ...
2025-09-21 20:05:13,402 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['sell', 'buy', 'roi']
2025-09-21 20:05:13,402 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-21 20:05:13,403 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-21 20:05:13,403 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 2130
2025-09-21 20:05:13,404 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-21 20:05:13,404 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: CalmarHyperOptLoss
2025-09-21 20:05:13,405 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-21 20:05:13,405 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20201231
2025-09-21 20:05:13,407 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-21 20:05:13,427 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-21 20:05:13,428 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 20:05:13,432 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-21 20:05:13,433 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-21 20:05:13,441 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-21 20:05:13,442 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-21 20:05:13,479 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-21 20:05:15,681 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-21 20:05:15,717 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-21 20:05:15,718 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-21 20:05:15,719 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-21 20:05:15,720 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-21 20:05:15,720 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-21 20:05:15,720 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-21 20:05:15,721 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-21 20:05:15,721 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-21 20:05:15,721 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.263, '183': 0.142, '783': 0.045, '2148': 0}
2025-09-21 20:05:15,722 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-21 20:05:15,722 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-21 20:05:15,722 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-21 20:05:15,723 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-21 20:05:15,723 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-21 20:05:15,723 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-21 20:05:15,724 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-21 20:05:15,724 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-21 20:05:15,725 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-21 20:05:15,725 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-21 20:05:15,725 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-21 20:05:15,726 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-21 20:05:15,726 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-21 20:05:15,726 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-21 20:05:15,727 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-21 20:05:15,727 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-21 20:05:15,727 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-21 20:05:15,728 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-21 20:05:15,728 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-21 20:05:15,728 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-21 20:05:15,729 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-21 20:05:15,729 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-21 20:05:15,729 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 20:05:15,734 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-21 20:05:15,767 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-21 20:05:15,768 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-21 20:05:15,769 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.1
2025-09-21 20:05:15,769 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 18
2025-09-21 20:05:15,769 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.501
2025-09-21 20:05:15,770 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.097
2025-09-21 20:05:15,770 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.049
2025-09-21 20:05:15,770 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.0
2025-09-21 20:05:15,771 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.001
2025-09-21 20:05:15,771 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-21 20:05:15,772 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 10
2025-09-21 20:05:15,772 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.99
2025-09-21 20:05:15,772 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-21 20:05:15,773 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-21 20:05:15,773 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-21 20:05:15,773 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-21 20:05:15,780 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss CalmarHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_calmar.py'...
2025-09-21 20:05:15,780 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 2130
2025-09-21 20:05:15,781 - freqtrade.optimize.hyperopt.hyperopt_interface - INFO - Min roi table: {0: 0.069, 120: 0.046, 240: 0.023, 360: 0}
2025-09-21 20:05:15,782 - freqtrade.optimize.hyperopt.hyperopt_interface - INFO - Max roi table: {0: 0.711, 480: 0.252, 1200: 0.092, 2640: 0}
2025-09-21 20:05:15,813 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-21 20:05:15,864 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-21 20:05:15,875 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-21 20:05:15,915 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-21 20:05:15,961 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-21 20:05:16,002 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-21 20:05:16,015 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-21 20:05:16,034 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2020-12-31 00:00:00 (1231 days).
2025-09-21 20:05:17,012 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-21 20:05:17,014 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 20:05:17,022 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-21 20:05:19,414 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 20:05:19,422 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-21 20:05:21,703 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 20:05:21,711 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-21 20:05:23,782 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 20:05:23,791 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-21 20:05:25,601 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 20:05:25,608 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-21 20:05:27,749 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2020-12-31 00:00:00 (1231 days)..
2025-09-21 20:05:28,056 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 20 CPU cores. Let's make them scream!
2025-09-21 20:05:28,057 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-21 20:05:28,058 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-21 20:05:28,058] A new study created in memory with name: no-name-c3dcefb8-b6ee-4460-83b7-405ab220b86f
2025-09-21 20:05:28,111 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                            ┏━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓                            
                            ┃ Best   ┃   Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                 Profit ┃ Avg duration ┃ Objective ┃    Max Drawdown (Acct) ┃                            
                            ┡━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩                            
                            │ * Best │   1/200 │     35 │   12     0    23  34.3 │     -0.46% │ -3.363 USDT   (-0.34%) │     12:02:00 │   0.05672 │ 95.974 USDT    (9.20%) │                            
                            │ * Best │   7/200 │     10 │    3     0     7  30.0 │      0.61% │ 33.798 USDT    (3.38%) │      7:36:00 │  -0.89323 │ 62.631 USDT    (5.87%) │                            
                            │ * Best │  12/200 │      4 │    2     1     1  50.0 │      0.23% │ 12.510 USDT    (1.25%) │     21:30:00 │ -12.21773 │  1.589 USDT    (0.16%) │                            
                            │ Best   │ 111/200 │      4 │    3     0     1  75.0 │      1.17% │ 13.153 USDT    (1.32%) │     16:15:00 │ -14.63977 │  1.409 USDT    (0.14%) │                            
                            │ Best   │ 139/200 │      4 │    3     0     1  75.0 │      0.98% │ 12.735 USDT    (1.27%) │     19:15:00 │ -14.64487 │  1.358 USDT    (0.13%) │                            
                            │ Best   │ 146/200 │      4 │    2     0     2  50.0 │      0.78% │ 15.541 USDT    (1.55%) │     22:15:00 │ -16.91593 │  1.439 USDT    (0.14%) │                            
                            │ Best   │ 171/200 │      7 │    3     1     3  42.9 │      0.70% │ 23.120 USDT    (2.31%) │     14:34:00 │ -24.70987 │  1.452 USDT    (0.15%) │                            
                            │ Best   │ 187/200 │      6 │    3     1     2  50.0 │      1.15% │ 26.544 USDT    (2.65%) │     17:00:00 │ -28.14238 │  1.464 USDT    (0.15%) │                            
                            └────────┴─────────┴────────┴────────────────────────┴────────────┴────────────────────────┴──────────────┴───────────┴────────────────────────┘                            
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 200/200 100% • 0:03:09 • 0:00:00
2025-09-21 20:08:38,049 - freqtrade.optimize.hyperopt.hyperopt - INFO - 200 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-21_20-05-13.fthypt'.
2025-09-21 20:08:38,098 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

   187/200:      6 trades. 3/1/2 Wins/Draws/Losses. Avg profit   1.15%. Median profit   1.06%. Total profit 26.54402438 USDT (   2.65%). Avg duration 17:00:00 min. Objective: -28.14238

{"params":{"confirmation_candle":false,"engulfing_size_threshold":2.5,"flat_kinjun_threshold":5,"hammer_body_threshold":0.974,"hammer_head_threshold":0.293,"hammer_strength_threshold":0.01,"kinjun_proximity_threshold":0.001,"tenkan_proximity_threshold":0.0,"kinjun_threshold":0.999,"lookback_period_for_stoploss":0,"stoploss_margin":0.996,"take_profit_multiplier":3,"use_sell_signal_param":true,"use_custom_stoploss_param":true},"minimal_roi":{"0":0.672,"469":0.23,"668":0.076,"1337":0},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Hyperopt Results
```json
{
  "timestamp": "2025-09-21T22:08:40.244082",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 2130,
  "wins_draws_losses": "3/1/2",
  "avg_profit_pct": 1.15,
  "median_profit_pct": 1.06,
  "total_profit_usdt": 26.54402438,
  "avg_duration": "17:00:00",
  "objective": -28.14238,
  "avg_profit_per_day": 1.6235
}
```
