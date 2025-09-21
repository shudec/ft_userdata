# Freqtrade Hyperopt Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 1986  
**Timestamp:** 2025-09-21 22:26:11

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 1986,
  "epochs": 200,
  "hyperopt_timerange": "20170801-20201231",
  "backtest_timerange": "20210101-20241231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss OnlyProfitHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 200 --spaces roi --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20201231 --random-state 1986
```

## Hyperopt Output
```
2025-09-21 20:22:44,436 - freqtrade - INFO - freqtrade 2025.7
2025-09-21 20:22:45,040 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-21 20:22:45,040 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-21 20:22:46,423 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-21 20:22:46,426 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-21 20:22:46,427 - freqtrade.loggers - INFO - Logfile configured
2025-09-21 20:22:46,427 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-21 20:22:46,427 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-21 20:22:46,428 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-21 20:22:46,428 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20201231 ...
2025-09-21 20:22:46,436 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-21 20:22:46,437 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-21 20:22:46,438 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-21 20:22:46,438 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 200 epochs ...
2025-09-21 20:22:46,439 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['roi']
2025-09-21 20:22:46,439 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-21 20:22:46,440 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-21 20:22:46,440 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 1986
2025-09-21 20:22:46,440 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-21 20:22:46,441 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: OnlyProfitHyperOptLoss
2025-09-21 20:22:46,441 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-21 20:22:46,442 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20201231
2025-09-21 20:22:46,443 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-21 20:22:46,463 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-21 20:22:46,464 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 20:22:46,468 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-21 20:22:46,469 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-21 20:22:46,477 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-21 20:22:46,478 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-21 20:22:46,510 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-21 20:22:49,443 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-21 20:22:49,480 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-21 20:22:49,480 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-21 20:22:49,481 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-21 20:22:49,481 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-21 20:22:49,482 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-21 20:22:49,482 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-21 20:22:49,483 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-21 20:22:49,483 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.672, '469': 0.23, '668': 0.076, '1337': 0}
2025-09-21 20:22:49,483 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-21 20:22:49,484 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-21 20:22:49,484 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-21 20:22:49,484 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-21 20:22:49,485 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-21 20:22:49,485 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-21 20:22:49,485 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-21 20:22:49,486 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-21 20:22:49,486 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-21 20:22:49,486 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-21 20:22:49,487 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-21 20:22:49,487 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-21 20:22:49,488 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-21 20:22:49,488 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-21 20:22:49,489 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-21 20:22:49,489 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-21 20:22:49,489 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-21 20:22:49,490 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-21 20:22:49,490 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-21 20:22:49,491 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-21 20:22:49,491 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-21 20:22:49,491 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-21 20:22:49,492 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 20:22:49,497 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-21 20:22:49,531 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-21 20:22:49,533 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-21 20:22:49,534 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.1
2025-09-21 20:22:49,534 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 18
2025-09-21 20:22:49,535 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.913
2025-09-21 20:22:49,535 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.781
2025-09-21 20:22:49,536 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.044
2025-09-21 20:22:49,536 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.0
2025-09-21 20:22:49,537 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.001
2025-09-21 20:22:49,538 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.995
2025-09-21 20:22:49,538 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 2
2025-09-21 20:22:49,539 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.99
2025-09-21 20:22:49,539 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-21 20:22:49,540 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-21 20:22:49,540 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-21 20:22:49,540 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-21 20:22:49,551 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss OnlyProfitHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_onlyprofit.py'...
2025-09-21 20:22:49,552 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 1986
2025-09-21 20:22:49,553 - freqtrade.optimize.hyperopt.hyperopt_interface - INFO - Min roi table: {0: 0.069, 120: 0.046, 240: 0.023, 360: 0}
2025-09-21 20:22:49,553 - freqtrade.optimize.hyperopt.hyperopt_interface - INFO - Max roi table: {0: 0.711, 480: 0.252, 1200: 0.092, 2640: 0}
2025-09-21 20:22:49,583 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-21 20:22:49,637 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-21 20:22:49,647 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-21 20:22:49,679 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-21 20:22:49,721 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-21 20:22:49,763 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-21 20:22:49,772 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-21 20:22:49,792 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2020-12-31 00:00:00 (1231 days).
2025-09-21 20:22:50,895 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-21 20:22:50,897 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 20:22:50,904 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-21 20:22:53,231 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 20:22:53,238 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-21 20:22:55,491 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 20:22:55,497 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-21 20:22:57,537 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 20:22:57,543 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-21 20:22:59,323 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 20:22:59,331 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-21 20:23:01,473 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2020-12-31 00:00:00 (1231 days)..
2025-09-21 20:23:01,781 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 20 CPU cores. Let's make them scream!
2025-09-21 20:23:01,782 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-21 20:23:01,783 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-21 20:23:01,784] A new study created in memory with name: no-name-91026829-f17e-43c3-a191-47f6267159ef
2025-09-21 20:23:01,835 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                           ┏━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓                           
                           ┃ Best   ┃   Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃ Avg duration ┃  Objective ┃    Max Drawdown (Acct) ┃                           
                           ┡━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩                           
                           │ * Best │   1/200 │     20 │    9     1    10  45.0 │      1.24% │ 210.811 USDT   (21.08%) │     13:12:00 │ -210.81096 │ 88.179 USDT    (7.93%) │                           
                           │ * Best │   2/200 │     20 │    8     2    10  40.0 │      1.28% │ 219.211 USDT   (21.92%) │     13:48:00 │ -219.21115 │ 87.956 USDT    (7.93%) │                           
                           │ * Best │   4/200 │     20 │    9     1    10  45.0 │      1.36% │ 235.072 USDT   (23.51%) │     14:30:00 │ -235.07186 │ 87.256 USDT    (7.93%) │                           
                           │ * Best │   8/200 │     20 │   10     0    10  50.0 │      1.41% │ 251.578 USDT   (25.16%) │     15:15:00 │ -251.57772 │ 87.235 USDT    (7.93%) │                           
                           │ * Best │  23/200 │     20 │    9     1    10  45.0 │      1.43% │ 253.048 USDT   (25.30%) │     14:48:00 │ -253.04764 │ 87.927 USDT    (7.93%) │                           
                           │ Best   │  31/200 │     20 │   10     0    10  50.0 │      1.59% │ 293.621 USDT   (29.36%) │     15:45:00 │ -293.62085 │ 88.544 USDT    (7.93%) │                           
                           │ Best   │  73/200 │     20 │   10     0    10  50.0 │      1.60% │ 301.220 USDT   (30.12%) │     16:33:00 │ -301.21993 │ 88.594 USDT    (7.93%) │                           
                           │ Best   │  99/200 │     20 │   10     0    10  50.0 │      1.83% │ 353.636 USDT   (35.36%) │     16:06:00 │ -353.63601 │ 88.338 USDT    (7.93%) │                           
                           │ Best   │ 183/200 │     20 │   10     0    10  50.0 │      1.85% │ 358.026 USDT   (35.80%) │     16:12:00 │ -358.02609 │ 88.481 USDT    (7.93%) │                           
                           └────────┴─────────┴────────┴────────────────────────┴────────────┴─────────────────────────┴──────────────┴────────────┴────────────────────────┘                           
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 200/200 100% • 0:03:07 • 0:00:00
2025-09-21 20:26:09,220 - freqtrade.optimize.hyperopt.hyperopt - INFO - 200 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-21_20-22-46.fthypt'.
2025-09-21 20:26:09,263 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

   183/200:     20 trades. 10/0/10 Wins/Draws/Losses. Avg profit   1.85%. Median profit  -0.19%. Total profit 358.02608546 USDT (  35.80%). Avg duration 16:12:00 min. Objective: -358.02609

{"params":{"confirmation_candle":false,"engulfing_size_threshold":1.1,"flat_kinjun_threshold":18,"hammer_body_threshold":0.913,"hammer_head_threshold":0.781,"hammer_strength_threshold":0.044,"kinjun_proximity_threshold":0.0,"tenkan_proximity_threshold":0.001,"kinjun_threshold":0.995,"lookback_period_for_stoploss":2,"stoploss_margin":0.99,"take_profit_multiplier":3,"use_custom_stoploss_param":true,"use_sell_signal_param":false},"minimal_roi":{"0":0.524,"438":0.144,"1133":0.057,"2477":0},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Hyperopt Results
```json
{
  "timestamp": "2025-09-21T22:26:11.112807",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 1986,
  "wins_draws_losses": "10/0/10",
  "avg_profit_pct": 1.85,
  "median_profit_pct": -0.19,
  "total_profit_usdt": 358.02608546,
  "avg_duration": "16:12:00",
  "objective": -358.02609,
  "avg_profit_per_day": 2.7407
}
```
