# Freqtrade Hyperopt Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 4160  
**Timestamp:** 2025-09-19 21:44:53

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy",
  "random_state": 4160,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 100 --spaces buy --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 4160
```

## Hyperopt Output
```
2025-09-19 19:43:22,253 - freqtrade - INFO - freqtrade 2025.7
2025-09-19 19:43:22,920 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-19 19:43:22,920 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-19 19:43:24,271 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-19 19:43:24,274 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-19 19:43:24,275 - freqtrade.loggers - INFO - Logfile configured
2025-09-19 19:43:24,275 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-19 19:43:24,275 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-19 19:43:24,276 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-19 19:43:24,276 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-19 19:43:24,284 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-19 19:43:24,285 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-19 19:43:24,285 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-19 19:43:24,286 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 100 epochs ...
2025-09-19 19:43:24,286 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy']
2025-09-19 19:43:24,287 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-19 19:43:24,287 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-19 19:43:24,287 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 4160
2025-09-19 19:43:24,288 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-19 19:43:24,288 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-19 19:43:24,288 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-19 19:43:24,289 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-19 19:43:24,290 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-19 19:43:24,309 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-19 19:43:24,310 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 19:43:24,314 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-19 19:43:24,316 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-19 19:43:24,318 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-19 19:43:24,318 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-19 19:43:24,352 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-19 19:43:26,751 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-19 19:43:26,801 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-19 19:43:26,802 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-19 19:43:26,804 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-19 19:43:26,804 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-19 19:43:26,805 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-19 19:43:26,805 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-19 19:43:26,806 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-19 19:43:26,806 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-19 19:43:26,807 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-19 19:43:26,807 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-19 19:43:26,808 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-19 19:43:26,808 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-19 19:43:26,809 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-19 19:43:26,809 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-19 19:43:26,810 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-19 19:43:26,810 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-19 19:43:26,811 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-19 19:43:26,811 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-19 19:43:26,812 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-19 19:43:26,812 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-19 19:43:26,813 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-19 19:43:26,813 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-19 19:43:26,814 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-19 19:43:26,814 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-19 19:43:26,815 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-19 19:43:26,815 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-19 19:43:26,816 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-19 19:43:26,816 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-19 19:43:26,817 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-19 19:43:26,817 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-19 19:43:26,818 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 19:43:26,824 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-19 19:43:26,863 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-19 19:43:26,866 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-19 19:43:26,866 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-19 19:43:26,867 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 1
2025-09-19 19:43:26,868 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.5
2025-09-19 19:43:26,868 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-09-19 19:43:26,869 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.025
2025-09-19 19:43:26,869 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-19 19:43:26,870 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.001
2025-09-19 19:43:26,871 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-19 19:43:26,871 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 2
2025-09-19 19:43:26,872 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-09-19 19:43:26,872 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-19 19:43:26,873 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-19 19:43:26,873 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-19 19:43:26,873 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-19 19:43:26,883 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-19 19:43:26,883 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 4160
2025-09-19 19:43:26,926 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-19 19:43:26,984 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-19 19:43:26,994 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-19 19:43:27,032 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-19 19:43:27,074 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-19 19:43:27,113 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-19 19:43:27,121 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-19 19:43:27,137 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-19 19:43:27,887 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-19 19:43:27,888 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 19:43:27,898 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-19 19:43:29,493 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 19:43:29,503 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-19 19:43:31,117 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 19:43:31,127 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-19 19:43:32,528 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 19:43:32,538 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-19 19:43:33,651 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 19:43:33,661 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-19 19:43:35,150 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-19 19:43:35,444 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 20 CPU cores. Let's make them scream!
2025-09-19 19:43:35,445 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-19 19:43:35,446 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-19 19:43:35,447] A new study created in memory with name: no-name-bd2e9524-7000-4c5d-96dc-3b5b9b33827b
2025-09-19 19:43:35,500 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                           Hyperopt results                                                                                             
                            ┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓                             
                            ┃ Best   ┃  Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                 Profit ┃ Avg duration ┃ Objective ┃    Max Drawdown (Acct) ┃                             
                            ┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩                             
                            │ * Best │  2/100 │      2 │    1     0     1  50.0 │      1.18% │ 23.458 USDT    (2.35%) │     13:30:00 │  -0.02257 │ 11.226 USDT    (1.12%) │                             
                            │ * Best │  4/100 │     11 │    3     0     8  27.3 │      0.30% │ 35.846 USDT    (3.58%) │      2:55:00 │  -0.03581 │ 43.925 USDT    (4.24%) │                             
                            │ * Best │  9/100 │      7 │    3     0     4  42.9 │      1.06% │ 73.587 USDT    (7.36%) │      4:09:00 │  -0.06347 │ 32.534 USDT    (3.08%) │                             
                            │ Best   │ 96/100 │     13 │    4     0     9  30.8 │      0.91% │ 82.175 USDT    (8.22%) │      4:14:00 │  -0.06476 │ 45.891 USDT    (4.24%) │                             
                            │ Best   │ 99/100 │     13 │    4     0     9  30.8 │      0.93% │ 84.742 USDT    (8.47%) │      4:00:00 │  -0.06633 │ 46.806 USDT    (4.24%) │                             
                            └────────┴────────┴────────┴────────────────────────┴────────────┴────────────────────────┴──────────────┴───────────┴────────────────────────┘                             
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100/100 100% • 0:01:16 • 0:00:00
2025-09-19 19:44:51,671 - freqtrade.optimize.hyperopt.hyperopt - INFO - 100 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-19_19-43-24.fthypt'.
2025-09-19 19:44:51,708 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

    99/100:     13 trades. 4/0/9 Wins/Draws/Losses. Avg profit   0.93%. Median profit  -0.57%. Total profit 84.74177768 USDT (   8.47%). Avg duration 4:00:00 min. Objective: -0.06633

{"params":{"confirmation_candle":true,"engulfing_size_threshold":1.2,"flat_kinjun_threshold":7,"hammer_body_threshold":0.41,"hammer_head_threshold":0.967,"hammer_strength_threshold":0.012,"kinjun_proximity_threshold":0.001,"tenkan_proximity_threshold":0.001,"kinjun_threshold":1.0,"lookback_period_for_stoploss":2,"stoploss_margin":0.999,"take_profit_multiplier":3,"use_custom_stoploss_param":true,"use_sell_signal_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Hyperopt Results
```json
{
  "timestamp": "2025-09-19T21:44:53.765065",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 4160,
  "wins_draws_losses": "4/0/9",
  "avg_profit_pct": 0.93,
  "median_profit_pct": -0.57,
  "total_profit_usdt": 84.74177768,
  "avg_duration": "4:00:00",
  "objective": -0.06633,
  "avg_profit_per_day": 5.58
}
```
