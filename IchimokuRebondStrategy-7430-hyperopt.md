# Freqtrade Hyperopt Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 7430  
**Timestamp:** 2025-09-19 15:05:34

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 7430,
  "epochs": 500,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 500 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 7430
```

## Hyperopt Output
```
2025-09-19 12:55:58,406 - freqtrade - INFO - freqtrade 2025.8
2025-09-19 12:55:58,955 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-19 12:56:00,338 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-19 12:56:00,344 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-19 12:56:00,345 - freqtrade.loggers - INFO - Logfile configured
2025-09-19 12:56:00,345 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-19 12:56:00,345 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-19 12:56:00,346 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-19 12:56:00,346 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-19 12:56:00,685 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-19 12:56:00,688 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-19 12:56:00,689 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-19 12:56:00,689 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 500 epochs ...
2025-09-19 12:56:00,690 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-19 12:56:00,690 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-19 12:56:00,691 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-19 12:56:00,691 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 7430
2025-09-19 12:56:00,691 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-19 12:56:00,692 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-19 12:56:00,692 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-19 12:56:00,692 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-19 12:56:00,694 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-19 12:56:00,708 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-19 12:56:00,708 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 12:56:00,712 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-19 12:56:00,718 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-19 12:56:00,725 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-19 12:56:00,725 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-19 12:56:00,749 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-19 12:56:04,576 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-19 12:56:04,669 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-19 12:56:04,671 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-19 12:56:04,677 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-19 12:56:04,677 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-19 12:56:04,678 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-19 12:56:04,678 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-19 12:56:04,679 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-19 12:56:04,679 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-19 12:56:04,680 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-19 12:56:04,680 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-19 12:56:04,680 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-19 12:56:04,681 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-19 12:56:04,681 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-19 12:56:04,681 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-19 12:56:04,682 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-19 12:56:04,682 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-19 12:56:04,683 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-19 12:56:04,683 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-19 12:56:04,683 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-19 12:56:04,683 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-19 12:56:04,684 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-19 12:56:04,684 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-19 12:56:04,685 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-19 12:56:04,685 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-19 12:56:04,686 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-19 12:56:04,686 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-19 12:56:04,686 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-19 12:56:04,687 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-19 12:56:04,687 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-19 12:56:04,687 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-19 12:56:04,688 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-19 12:56:04,688 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 12:56:04,706 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-19 12:56:04,731 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-19 12:56:04,732 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-19 12:56:04,733 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-19 12:56:04,733 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 8
2025-09-19 12:56:04,734 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.936
2025-09-19 12:56:04,734 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.716
2025-09-19 12:56:04,735 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.048
2025-09-19 12:56:04,735 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.005
2025-09-19 12:56:04,735 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): tenkan_proximity_threshold = 0.01
2025-09-19 12:56:04,736 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.996
2025-09-19 12:56:04,736 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 10
2025-09-19 12:56:04,737 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 1.0
2025-09-19 12:56:04,737 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-19 12:56:04,737 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-19 12:56:04,738 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-19 12:56:04,738 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-19 12:56:04,759 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-19 12:56:04,759 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 7430
2025-09-19 12:56:04,810 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-19 12:56:04,874 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-19 12:56:04,882 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-19 12:56:04,931 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-19 12:56:04,984 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-19 12:56:05,035 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-19 12:56:05,041 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-19 12:56:05,052 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-19 12:56:05,635 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-19 12:56:05,637 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 12:56:05,652 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-19 12:56:07,311 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 12:56:07,326 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-19 12:56:09,160 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 12:56:09,175 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-19 12:56:10,920 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 12:56:10,939 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-19 12:56:12,293 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 12:56:12,310 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-19 12:56:13,846 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-19 12:56:14,290 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 16 CPU cores. Let's make them scream!
2025-09-19 12:56:14,291 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-19 12:56:14,292 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-19 12:56:14,293] A new study created in memory with name: no-name-08f6c783-2044-4ade-953b-e51a4e2e8571
2025-09-19 12:56:14,339 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                          ┏━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓                          
                          ┃ Best   ┃   Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃    Avg duration ┃ Objective ┃    Max Drawdown (Acct) ┃                          
                          ┡━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩                          
                          │ * Best │   1/500 │      2 │    0     0     2     0 │     -1.67% │ -32.808 USDT   (-3.28%) │        10:00:00 │   0.18013 │ 32.808 USDT    (3.28%) │                          
                          │ * Best │   2/500 │      3 │    1     0     2  33.3 │     -0.13% │  -3.757 USDT   (-0.38%) │        10:00:00 │   0.00331 │ 37.807 USDT    (3.66%) │                          
                          │ * Best │  15/500 │      3 │    1     0     2  33.3 │      3.47% │  15.025 USDT    (1.50%) │ 2 days, 4:20:00 │  -0.00859 │ 44.643 USDT    (4.21%) │                          
                          │ * Best │  17/500 │      3 │    1     0     2  33.3 │      1.55% │  25.742 USDT    (2.57%) │         4:40:00 │  -0.02509 │ 14.052 USDT    (1.35%) │                          
                          │ * Best │  24/500 │      3 │    1     0     2  33.3 │      3.01% │  42.415 USDT    (4.24%) │        14:20:00 │  -0.02694 │ 20.348 USDT    (1.91%) │                          
                          │ Best   │ 107/500 │      3 │    1     0     2  33.3 │      1.55% │  37.206 USDT    (3.72%) │         4:40:00 │  -0.02708 │ 17.184 USDT    (1.63%) │                          
                          │ Best   │ 132/500 │      3 │    1     0     2  33.3 │      2.80% │  31.943 USDT    (3.19%) │         5:20:00 │  -0.02898 │ 12.534 USDT    (1.20%) │                          
                          │ Best   │ 155/500 │      3 │    1     0     2  33.3 │      3.22% │  47.533 USDT    (4.75%) │        11:20:00 │  -0.03121 │ 15.230 USDT    (1.43%) │                          
                          │ Best   │ 158/500 │      3 │    1     0     2  33.3 │      2.80% │  50.447 USDT    (5.04%) │         5:20:00 │  -0.03173 │ 15.384 USDT    (1.44%) │                          
                          │ Best   │ 203/500 │      3 │    1     0     2  33.3 │      2.80% │  67.362 USDT    (6.74%) │         5:20:00 │  -0.03441 │ 15.718 USDT    (1.45%) │                          
                          │ Best   │ 255/500 │      3 │    1     0     2  33.3 │      2.80% │  73.257 USDT    (7.33%) │         5:20:00 │  -0.03451 │ 16.889 USDT    (1.55%) │                          
                          └────────┴─────────┴────────┴────────────────────────┴────────────┴─────────────────────────┴─────────────────┴───────────┴────────────────────────┘                          
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 500/500 100% • 0:09:17 • 0:00:00
2025-09-19 13:05:31,942 - freqtrade.optimize.hyperopt.hyperopt - INFO - 500 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-19_12-56-00.fthypt'.
2025-09-19 13:05:32,118 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

   255/500:      3 trades. 1/0/2 Wins/Draws/Losses. Avg profit   2.80%. Median profit  -0.09%. Total profit 73.25678369 USDT (   7.33%). Avg duration 5:20:00 min. Objective: -0.03451

{"params":{"confirmation_candle":false,"engulfing_size_threshold":1.5,"flat_kinjun_threshold":1,"hammer_body_threshold":0.933,"hammer_head_threshold":0.533,"hammer_strength_threshold":0.025,"kinjun_proximity_threshold":0.008,"tenkan_proximity_threshold":0.029,"kinjun_threshold":1.0,"lookback_period_for_stoploss":2,"stoploss_margin":0.995,"take_profit_multiplier":3,"use_sell_signal_param":true,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Hyperopt Results
```json
{
  "timestamp": "2025-09-19T15:05:34.407594",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 7430,
  "wins_draws_losses": "1/0/2",
  "avg_profit_pct": 2.8,
  "median_profit_pct": -0.09,
  "total_profit_usdt": 73.25678369,
  "avg_duration": "5:20:00",
  "objective": -0.03451,
  "avg_profit_per_day": 12.6
}
```
