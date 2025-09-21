# Freqtrade Hyperopt Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 6158  
**Timestamp:** 2025-09-20 22:30:43

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell buy roi",
  "random_state": 6158,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20201231",
  "backtest_timerange": "20221101-20241231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 100 --spaces sell buy roi --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20201231 --random-state 6158
```

## Hyperopt Output
```
2025-09-20 20:28:48,240 - freqtrade - INFO - freqtrade 2025.7
2025-09-20 20:28:48,948 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-20 20:28:48,949 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-20 20:28:50,360 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-20 20:28:50,363 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-20 20:28:50,364 - freqtrade.loggers - INFO - Logfile configured
2025-09-20 20:28:50,364 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-20 20:28:50,365 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-20 20:28:50,365 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-20 20:28:50,365 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20201231 ...
2025-09-20 20:28:50,373 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-20 20:28:50,374 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-20 20:28:50,375 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-20 20:28:50,375 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 100 epochs ...
2025-09-20 20:28:50,376 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['sell', 'buy', 'roi']
2025-09-20 20:28:50,376 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-20 20:28:50,377 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-20 20:28:50,377 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 6158
2025-09-20 20:28:50,378 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-20 20:28:50,378 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-20 20:28:50,379 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-20 20:28:50,379 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20201231
2025-09-20 20:28:50,380 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-20 20:28:50,400 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-20 20:28:50,401 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-20 20:28:50,404 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-20 20:28:50,405 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-20 20:28:50,407 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-20 20:28:50,408 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-20 20:28:50,440 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-20 20:28:53,022 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-20 20:28:53,061 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-20 20:28:53,061 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-20 20:28:53,062 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-20 20:28:53,063 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-20 20:28:53,063 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-20 20:28:53,063 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-20 20:28:53,064 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-20 20:28:53,064 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-20 20:28:53,065 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.49, '456': 0.214, '795': 0.085, '1564': 0}
2025-09-20 20:28:53,065 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-20 20:28:53,065 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-20 20:28:53,066 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-20 20:28:53,066 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-20 20:28:53,066 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-20 20:28:53,067 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-20 20:28:53,067 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-20 20:28:53,067 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-20 20:28:53,068 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-20 20:28:53,068 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-20 20:28:53,068 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-20 20:28:53,068 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-20 20:28:53,069 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-20 20:28:53,069 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-20 20:28:53,070 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-20 20:28:53,070 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-20 20:28:53,070 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-20 20:28:53,071 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-20 20:28:53,071 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-20 20:28:53,071 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-20 20:28:53,072 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-20 20:28:53,072 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-20 20:28:53,072 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-20 20:28:53,078 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-20 20:28:53,110 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-20 20:28:53,112 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-20 20:28:53,113 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.1
2025-09-20 20:28:53,114 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 16
2025-09-20 20:28:53,114 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.523
2025-09-20 20:28:53,115 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.85
2025-09-20 20:28:53,115 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.022
2025-09-20 20:28:53,116 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.0
2025-09-20 20:28:53,116 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.001
2025-09-20 20:28:53,117 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-20 20:28:53,117 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 6
2025-09-20 20:28:53,118 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.992
2025-09-20 20:28:53,118 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-20 20:28:53,118 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-20 20:28:53,119 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-20 20:28:53,119 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-20 20:28:53,130 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-20 20:28:53,130 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 6158
2025-09-20 20:28:53,131 - freqtrade.optimize.hyperopt.hyperopt_interface - INFO - Min roi table: {0: 0.069, 120: 0.046, 240: 0.023, 360: 0}
2025-09-20 20:28:53,132 - freqtrade.optimize.hyperopt.hyperopt_interface - INFO - Max roi table: {0: 0.711, 480: 0.252, 1200: 0.092, 2640: 0}
2025-09-20 20:28:53,168 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-20 20:28:53,222 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-20 20:28:53,235 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-20 20:28:53,279 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-20 20:28:53,339 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-20 20:28:53,387 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-20 20:28:53,398 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-20 20:28:53,420 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2020-12-31 00:00:00 (1231 days).
2025-09-20 20:28:54,551 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-20 20:28:54,553 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-20 20:28:54,559 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-20 20:28:56,955 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-20 20:28:56,962 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-20 20:28:59,349 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-20 20:28:59,357 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-20 20:29:01,576 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-20 20:29:01,584 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-20 20:29:03,592 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-20 20:29:03,601 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-20 20:29:05,896 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2020-12-31 00:00:00 (1231 days)..
2025-09-20 20:29:06,205 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 20 CPU cores. Let's make them scream!
2025-09-20 20:29:06,205 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-20 20:29:06,206 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-20 20:29:06,207] A new study created in memory with name: no-name-d6c94835-dc6e-47d2-aac8-fc135d36c09e
2025-09-20 20:29:06,268 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                            ┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓                            
                            ┃ Best   ┃  Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃ Avg duration ┃ Objective ┃    Max Drawdown (Acct) ┃                            
                            ┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩                            
                            │ * Best │  1/100 │      4 │    0     1     3     0 │     -2.10% │ -61.431 USDT   (-6.14%) │     14:45:00 │   0.10707 │ 61.431 USDT    (6.14%) │                            
                            │ * Best │ 13/100 │      5 │    1     1     3  20.0 │     -0.43% │ -39.033 USDT   (-3.90%) │      5:48:00 │   0.05084 │ 39.033 USDT    (3.90%) │                            
                            │ * Best │ 19/100 │      9 │    2     1     6  22.2 │     -0.36% │ -18.957 USDT   (-1.90%) │      9:00:00 │   0.01611 │ 44.804 USDT    (4.37%) │                            
                            │ Best   │ 32/100 │      8 │    3     3     2  37.5 │      1.26% │  64.969 USDT    (6.50%) │     22:22:00 │  -0.04177 │ 40.399 USDT    (4.04%) │                            
                            └────────┴────────┴────────┴────────────────────────┴────────────┴─────────────────────────┴──────────────┴───────────┴────────────────────────┘                            
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100/100 100% • 0:01:34 • 0:00:00
2025-09-20 20:30:41,391 - freqtrade.optimize.hyperopt.hyperopt - INFO - 100 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-20_20-28-50.fthypt'.
2025-09-20 20:30:41,429 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

    32/100:      8 trades. 3/3/2 Wins/Draws/Losses. Avg profit   1.26%. Median profit   0.00%. Total profit 64.96859225 USDT (   6.50%). Avg duration 22:22:00 min. Objective: -0.04177

{"params":{"confirmation_candle":true,"engulfing_size_threshold":1.5,"flat_kinjun_threshold":20,"hammer_body_threshold":0.996,"hammer_head_threshold":0.923,"hammer_strength_threshold":0.001,"kinjun_proximity_threshold":0.001,"tenkan_proximity_threshold":0.0,"kinjun_threshold":0.998,"lookback_period_for_stoploss":9,"stoploss_margin":0.991,"take_profit_multiplier":2.5,"use_sell_signal_param":false,"use_custom_stoploss_param":true},"minimal_roi":{"0":0.326,"432":0.142,"803":0.072,"1879":0},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Hyperopt Results
```json
{
  "timestamp": "2025-09-20T22:30:43.441965",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 6158,
  "wins_draws_losses": "3/3/2",
  "avg_profit_pct": 1.26,
  "median_profit_pct": 0.0,
  "total_profit_usdt": 64.96859225,
  "avg_duration": "22:22:00",
  "objective": -0.04177,
  "avg_profit_per_day": 1.352
}
```
