# Freqtrade Hyperopt Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 5990  
**Timestamp:** 2025-09-21 21:00:14

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell buy roi",
  "random_state": 5990,
  "epochs": 200,
  "hyperopt_timerange": "20170801-20201231",
  "backtest_timerange": "20221101-20241231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 200 --spaces sell buy roi --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20201231 --random-state 5990
```

## Hyperopt Output
```
2025-09-21 18:56:36,910 - freqtrade - INFO - freqtrade 2025.7
2025-09-21 18:56:37,676 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-21 18:56:37,677 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-21 18:56:39,104 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-21 18:56:39,107 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-21 18:56:39,108 - freqtrade.loggers - INFO - Logfile configured
2025-09-21 18:56:39,108 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-21 18:56:39,109 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-21 18:56:39,109 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-21 18:56:39,110 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20201231 ...
2025-09-21 18:56:39,118 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-21 18:56:39,119 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-21 18:56:39,120 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-21 18:56:39,120 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 200 epochs ...
2025-09-21 18:56:39,121 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['sell', 'buy', 'roi']
2025-09-21 18:56:39,121 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-21 18:56:39,121 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-21 18:56:39,122 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 5990
2025-09-21 18:56:39,122 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-21 18:56:39,123 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-21 18:56:39,123 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-21 18:56:39,123 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20201231
2025-09-21 18:56:39,125 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-21 18:56:39,145 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-21 18:56:39,146 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 18:56:39,150 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-21 18:56:39,152 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-21 18:56:39,154 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-21 18:56:39,154 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-21 18:56:39,191 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-21 18:56:41,529 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-21 18:56:41,576 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-21 18:56:41,576 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-21 18:56:41,578 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-21 18:56:41,578 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-21 18:56:41,579 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-21 18:56:41,579 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-21 18:56:41,580 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-21 18:56:41,580 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-21 18:56:41,581 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.326, '432': 0.142, '803': 0.072, '1879': 0}
2025-09-21 18:56:41,581 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-21 18:56:41,581 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-21 18:56:41,582 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-21 18:56:41,582 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-21 18:56:41,582 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-21 18:56:41,583 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-21 18:56:41,583 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-21 18:56:41,583 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-21 18:56:41,584 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-21 18:56:41,585 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-21 18:56:41,586 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-21 18:56:41,587 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-21 18:56:41,587 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-21 18:56:41,588 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-21 18:56:41,588 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-21 18:56:41,588 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-21 18:56:41,589 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-21 18:56:41,589 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-21 18:56:41,590 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-21 18:56:41,590 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-21 18:56:41,591 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-21 18:56:41,591 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-21 18:56:41,591 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 18:56:41,599 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-21 18:56:41,638 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-21 18:56:41,640 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-21 18:56:41,640 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-21 18:56:41,641 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 20
2025-09-21 18:56:41,642 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.996
2025-09-21 18:56:41,642 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.923
2025-09-21 18:56:41,642 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.001
2025-09-21 18:56:41,643 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-21 18:56:41,643 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.0
2025-09-21 18:56:41,644 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.998
2025-09-21 18:56:41,645 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 9
2025-09-21 18:56:41,645 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.991
2025-09-21 18:56:41,645 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2.5
2025-09-21 18:56:41,646 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-21 18:56:41,646 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-21 18:56:41,647 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-21 18:56:41,657 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-21 18:56:41,657 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 5990
2025-09-21 18:56:41,658 - freqtrade.optimize.hyperopt.hyperopt_interface - INFO - Min roi table: {0: 0.069, 120: 0.046, 240: 0.023, 360: 0}
2025-09-21 18:56:41,659 - freqtrade.optimize.hyperopt.hyperopt_interface - INFO - Max roi table: {0: 0.711, 480: 0.252, 1200: 0.092, 2640: 0}
2025-09-21 18:56:41,707 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-21 18:56:41,771 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-21 18:56:41,783 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-21 18:56:41,825 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-21 18:56:41,880 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-21 18:56:41,932 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-21 18:56:41,943 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-21 18:56:41,963 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2020-12-31 00:00:00 (1231 days).
2025-09-21 18:56:43,118 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-21 18:56:43,120 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 18:56:43,130 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-21 18:56:45,634 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 18:56:45,646 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-21 18:56:48,711 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 18:56:48,727 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-21 18:56:51,811 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 18:56:51,826 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-21 18:56:54,431 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 18:56:54,442 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-21 18:56:56,955 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2020-12-31 00:00:00 (1231 days)..
2025-09-21 18:56:57,270 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 20 CPU cores. Let's make them scream!
2025-09-21 18:56:57,271 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-21 18:56:57,272 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-21 18:56:57,273] A new study created in memory with name: no-name-eb35355d-5ea4-402f-a0aa-a26722e1b8c5
2025-09-21 18:56:57,340 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                           ┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓                           
                           ┃ Best   ┃  Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                   Profit ┃ Avg duration ┃ Objective ┃     Max Drawdown (Acct) ┃                           
                           ┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩                           
                           │ * Best │  7/200 │     26 │    7     2    17  26.9 │     -1.24% │ -204.667 USDT  (-20.47%) │     12:23:00 │   0.18010 │ 204.667 USDT   (20.47%) │                           
                           │ * Best │ 14/200 │      2 │    1     0     1  50.0 │      0.74% │   14.566 USDT    (1.46%) │     12:00:00 │  -0.01915 │   4.523 USDT    (0.45%) │                           
                           │ * Best │ 20/200 │      3 │    2     0     1  66.7 │      2.33% │   44.645 USDT    (4.46%) │      5:20:00 │  -0.02576 │  20.764 USDT    (2.03%) │                           
                           │ Best   │ 43/200 │      3 │    3     0     0   100 │      1.23% │   36.674 USDT    (3.67%) │     11:00:00 │  -0.11569 │                      -- │                           
                           │ Best   │ 90/200 │      2 │    2     0     0   100 │      2.66% │   42.454 USDT    (4.25%) │      2:30:00 │  -0.50770 │                      -- │                           
                           └────────┴────────┴────────┴────────────────────────┴────────────┴──────────────────────────┴──────────────┴───────────┴─────────────────────────┘                           
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 200/200 100% • 0:03:15 • 0:00:00
2025-09-21 19:00:12,608 - freqtrade.optimize.hyperopt.hyperopt - INFO - 200 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-21_18-56-39.fthypt'.
2025-09-21 19:00:12,644 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

    90/200:      2 trades. 2/0/0 Wins/Draws/Losses. Avg profit   2.66%. Median profit   2.66%. Total profit 42.45381383 USDT (   4.25%). Avg duration 2:30:00 min. Objective: -0.50770

{"params":{"confirmation_candle":false,"engulfing_size_threshold":1.2,"flat_kinjun_threshold":0,"hammer_body_threshold":0.926,"hammer_head_threshold":0.911,"hammer_strength_threshold":0.031,"kinjun_proximity_threshold":0.002,"tenkan_proximity_threshold":0.002,"kinjun_threshold":0.998,"lookback_period_for_stoploss":2,"stoploss_margin":0.999,"take_profit_multiplier":1,"use_sell_signal_param":false,"use_custom_stoploss_param":true},"minimal_roi":{"0":0.427,"474":0.179,"800":0.064,"1657":0},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Hyperopt Results
```json
{
  "timestamp": "2025-09-21T21:00:14.621345",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 5990,
  "wins_draws_losses": "2/0/0",
  "avg_profit_pct": 2.66,
  "median_profit_pct": 2.66,
  "total_profit_usdt": 42.45381383,
  "avg_duration": "2:30:00",
  "objective": -0.5077,
  "avg_profit_per_day": 25.536
}
```
