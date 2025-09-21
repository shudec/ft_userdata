# Freqtrade Hyperopt Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 6443  
**Timestamp:** 2025-09-21 22:01:33

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SortinoHyperOptLoss",
  "spaces": "sell buy roi",
  "random_state": 6443,
  "epochs": 200,
  "hyperopt_timerange": "20170801-20201231",
  "backtest_timerange": "20210101-20241231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SortinoHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 200 --spaces sell buy roi --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20201231 --random-state 6443
```

## Hyperopt Output
```
2025-09-21 19:58:00,445 - freqtrade - INFO - freqtrade 2025.7
2025-09-21 19:58:01,132 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-21 19:58:01,133 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-21 19:58:02,479 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-21 19:58:02,482 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-21 19:58:02,483 - freqtrade.loggers - INFO - Logfile configured
2025-09-21 19:58:02,483 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-21 19:58:02,484 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-21 19:58:02,484 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-21 19:58:02,484 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20201231 ...
2025-09-21 19:58:02,492 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-21 19:58:02,493 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-21 19:58:02,494 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-21 19:58:02,494 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 200 epochs ...
2025-09-21 19:58:02,495 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['sell', 'buy', 'roi']
2025-09-21 19:58:02,495 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-21 19:58:02,495 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-21 19:58:02,496 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 6443
2025-09-21 19:58:02,496 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-21 19:58:02,497 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SortinoHyperOptLoss
2025-09-21 19:58:02,497 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-21 19:58:02,498 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20201231
2025-09-21 19:58:02,499 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-21 19:58:02,518 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-21 19:58:02,519 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 19:58:02,523 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-21 19:58:02,524 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-21 19:58:02,532 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-21 19:58:02,532 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-21 19:58:02,566 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-21 19:58:04,841 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-21 19:58:04,876 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-21 19:58:04,877 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-21 19:58:04,878 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-21 19:58:04,878 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-21 19:58:04,878 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-21 19:58:04,879 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-21 19:58:04,879 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-21 19:58:04,880 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-21 19:58:04,880 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.587, '136': 0.19, '722': 0.029, '2143': 0}
2025-09-21 19:58:04,881 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-21 19:58:04,881 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-21 19:58:04,881 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-21 19:58:04,881 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-21 19:58:04,882 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-21 19:58:04,882 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-21 19:58:04,883 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-21 19:58:04,883 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-21 19:58:04,883 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-21 19:58:04,884 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-21 19:58:04,884 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-21 19:58:04,884 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-21 19:58:04,885 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-21 19:58:04,885 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-21 19:58:04,885 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-21 19:58:04,886 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-21 19:58:04,886 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-21 19:58:04,886 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-21 19:58:04,887 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-21 19:58:04,887 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-21 19:58:04,888 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-21 19:58:04,888 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-21 19:58:04,889 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 19:58:04,894 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-21 19:58:04,927 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-21 19:58:04,929 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-21 19:58:04,929 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 3
2025-09-21 19:58:04,930 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-09-21 19:58:04,930 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.633
2025-09-21 19:58:04,931 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.713
2025-09-21 19:58:04,931 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.045
2025-09-21 19:58:04,931 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-21 19:58:04,932 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.0
2025-09-21 19:58:04,932 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.996
2025-09-21 19:58:04,933 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 8
2025-09-21 19:58:04,933 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.992
2025-09-21 19:58:04,933 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2.5
2025-09-21 19:58:04,934 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-21 19:58:04,934 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-21 19:58:04,934 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-21 19:58:04,941 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SortinoHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sortino.py'...
2025-09-21 19:58:04,941 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 6443
2025-09-21 19:58:04,942 - freqtrade.optimize.hyperopt.hyperopt_interface - INFO - Min roi table: {0: 0.069, 120: 0.046, 240: 0.023, 360: 0}
2025-09-21 19:58:04,943 - freqtrade.optimize.hyperopt.hyperopt_interface - INFO - Max roi table: {0: 0.711, 480: 0.252, 1200: 0.092, 2640: 0}
2025-09-21 19:58:04,975 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-21 19:58:05,028 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-21 19:58:05,037 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-21 19:58:05,071 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-21 19:58:05,115 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-21 19:58:05,156 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-21 19:58:05,167 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-21 19:58:05,184 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2020-12-31 00:00:00 (1231 days).
2025-09-21 19:58:06,228 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-21 19:58:06,229 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 19:58:06,236 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-21 19:58:08,633 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 19:58:08,642 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-21 19:58:11,163 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 19:58:11,169 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-21 19:58:13,286 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 19:58:13,293 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-21 19:58:15,196 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 19:58:15,204 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-21 19:58:17,497 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2020-12-31 00:00:00 (1231 days)..
2025-09-21 19:58:17,812 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 20 CPU cores. Let's make them scream!
2025-09-21 19:58:17,813 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-21 19:58:17,814 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-21 19:58:17,815] A new study created in memory with name: no-name-3778d979-42f0-4e39-a567-a1b2d65244bd
2025-09-21 19:58:17,873 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                           Hyperopt results                                                                                             
                          ┏━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓                           
                          ┃ Best   ┃   Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃   Avg duration ┃ Objective ┃    Max Drawdown (Acct) ┃                           
                          ┡━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩                           
                          │ * Best │   1/200 │     18 │    5     0    13  27.8 │     -0.20% │ -16.836 USDT   (-1.68%) │        6:10:00 │   0.05811 │ 60.147 USDT    (6.01%) │                           
                          │ * Best │   2/200 │      7 │    3     1     3  42.9 │     -0.08% │  -8.658 USDT   (-0.87%) │        9:51:00 │   0.02575 │ 38.380 USDT    (3.82%) │                           
                          │ * Best │   5/200 │     26 │    8     4    14  30.8 │     -0.36% │  26.877 USDT    (2.69%) │       23:55:00 │  -0.17305 │ 82.216 USDT    (7.56%) │                           
                          │ * Best │  13/200 │     43 │   21     0    22  48.8 │      0.06% │  65.692 USDT    (6.57%) │        7:45:00 │  -0.18976 │ 89.831 USDT    (8.98%) │                           
                          │ Best   │  53/200 │     26 │    9     3    14  34.6 │     -0.05% │  85.520 USDT    (8.55%) │       16:02:00 │  -0.29324 │ 76.934 USDT    (7.62%) │                           
                          │ Best   │  56/200 │     23 │   10     1    12  43.5 │      0.08% │  81.819 USDT    (8.18%) │       13:10:00 │  -0.31815 │ 75.849 USDT    (7.48%) │                           
                          │ Best   │  78/200 │     37 │   19     4    14  51.4 │      0.53% │ 306.327 USDT   (30.63%) │ 1 day, 1:47:00 │  -0.83416 │ 65.626 USDT    (5.53%) │                           
                          │ Best   │  80/200 │     35 │   15     5    15  42.9 │      0.39% │ 245.934 USDT   (24.59%) │       22:41:00 │  -1.07381 │ 81.260 USDT    (7.38%) │                           
                          │ Best   │ 113/200 │     19 │   10     1     8  52.6 │      0.35% │  97.473 USDT    (9.75%) │       17:09:00 │  -1.78196 │ 61.994 USDT    (6.14%) │                           
                          │ Best   │ 157/200 │     35 │   18     4    13  51.4 │      0.73% │ 364.677 USDT   (36.47%) │ 1 day, 1:38:00 │  -2.08746 │ 68.103 USDT    (5.53%) │                           
                          │ Best   │ 175/200 │     19 │   11     1     7  57.9 │      0.95% │ 144.516 USDT   (14.45%) │       20:13:00 │  -3.22985 │ 65.170 USDT    (6.13%) │                           
                          └────────┴─────────┴────────┴────────────────────────┴────────────┴─────────────────────────┴────────────────┴───────────┴────────────────────────┘                           
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 200/200 100% • 0:03:13 • 0:00:00
2025-09-21 20:01:31,749 - freqtrade.optimize.hyperopt.hyperopt - INFO - 200 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-21_19-58-02.fthypt'.
2025-09-21 20:01:31,791 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

   175/200:     19 trades. 11/1/7 Wins/Draws/Losses. Avg profit   0.95%. Median profit   1.63%. Total profit 144.51615805 USDT (  14.45%). Avg duration 20:13:00 min. Objective: -3.22985

{"params":{"confirmation_candle":true,"engulfing_size_threshold":1.1,"flat_kinjun_threshold":18,"hammer_body_threshold":0.501,"hammer_head_threshold":0.097,"hammer_strength_threshold":0.049,"kinjun_proximity_threshold":0.0,"tenkan_proximity_threshold":0.001,"kinjun_threshold":0.999,"lookback_period_for_stoploss":10,"stoploss_margin":0.99,"take_profit_multiplier":3,"use_sell_signal_param":false,"use_custom_stoploss_param":true},"minimal_roi":{"0":0.263,"183":0.142,"783":0.045,"2148":0},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Hyperopt Results
```json
{
  "timestamp": "2025-09-21T22:01:33.826227",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 6443,
  "wins_draws_losses": "11/1/7",
  "avg_profit_pct": 0.95,
  "median_profit_pct": 1.63,
  "total_profit_usdt": 144.51615805,
  "avg_duration": "20:13:00",
  "objective": -3.22985,
  "avg_profit_per_day": 1.1278
}
```
