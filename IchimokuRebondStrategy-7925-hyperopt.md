# Freqtrade Hyperopt Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 7925  
**Timestamp:** 2025-09-18 11:24:14

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 7925,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 7925
```

## Hyperopt Output
```
2025-09-18 09:22:11,022 - freqtrade - INFO - freqtrade 2025.8
2025-09-18 09:22:11,920 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-18 09:22:14,160 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-18 09:22:14,167 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-18 09:22:14,167 - freqtrade.loggers - INFO - Logfile configured
2025-09-18 09:22:14,168 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-18 09:22:14,168 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-18 09:22:14,168 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-18 09:22:14,169 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-18 09:22:14,441 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-18 09:22:14,443 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-18 09:22:14,444 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-18 09:22:14,444 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 100 epochs ...
2025-09-18 09:22:14,445 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-18 09:22:14,445 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-18 09:22:14,446 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-18 09:22:14,446 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 7925
2025-09-18 09:22:14,447 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-18 09:22:14,447 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-18 09:22:14,448 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-18 09:22:14,448 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-18 09:22:14,450 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-18 09:22:14,460 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-18 09:22:14,461 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 09:22:14,463 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-18 09:22:14,469 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-18 09:22:14,474 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-18 09:22:14,474 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-18 09:22:14,494 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-18 09:22:17,145 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-18 09:22:17,302 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-18 09:22:17,305 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-18 09:22:17,310 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-18 09:22:17,311 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-18 09:22:17,312 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-18 09:22:17,312 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-18 09:22:17,313 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-18 09:22:17,314 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-18 09:22:17,315 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-18 09:22:17,317 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-18 09:22:17,317 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-18 09:22:17,318 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-18 09:22:17,319 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-18 09:22:17,320 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-18 09:22:17,321 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-18 09:22:17,321 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-18 09:22:17,322 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-18 09:22:17,322 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-18 09:22:17,323 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-18 09:22:17,324 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-18 09:22:17,324 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-18 09:22:17,325 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-18 09:22:17,325 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-18 09:22:17,326 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-18 09:22:17,327 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-18 09:22:17,327 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-18 09:22:17,328 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-18 09:22:17,329 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-18 09:22:17,330 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-18 09:22:17,330 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-18 09:22:17,331 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-18 09:22:17,334 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 09:22:17,379 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-18 09:22:17,432 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-18 09:22:17,437 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-18 09:22:17,438 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.491
2025-09-18 09:22:17,438 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.909
2025-09-18 09:22:17,439 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.009
2025-09-18 09:22:17,440 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 2
2025-09-18 09:22:17,441 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 4
2025-09-18 09:22:17,442 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.991
2025-09-18 09:22:17,443 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-18 09:22:17,444 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-18 09:22:17,444 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-18 09:22:17,445 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-18 09:22:17,479 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-18 09:22:17,480 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 7925
2025-09-18 09:22:17,594 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-18 09:22:17,696 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-18 09:22:17,705 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-18 09:22:17,755 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-18 09:22:17,812 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-18 09:22:17,871 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-18 09:22:17,879 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-18 09:22:17,901 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-18 09:22:18,577 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-18 09:22:18,580 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 09:22:18,598 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-18 09:22:21,153 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 09:22:21,171 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-18 09:22:23,286 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 09:22:23,303 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-18 09:22:24,834 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 09:22:24,851 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-18 09:22:26,154 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 09:22:26,169 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-18 09:22:28,084 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-18 09:22:28,562 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 16 CPU cores. Let's make them scream!
2025-09-18 09:22:28,563 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-18 09:22:28,565 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-18 09:22:28,566] A new study created in memory with name: no-name-69efab16-33e5-44a9-996c-abdcf50cab6f
2025-09-18 09:22:28,643 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                           Hyperopt results                                                                                             
                          ┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓                           
                          ┃ Best   ┃  Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃    Avg duration ┃ Objective ┃    Max Drawdown (Acct) ┃                           
                          ┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩                           
                          │ * Best │  1/100 │     28 │   12     0    16  42.9 │     -0.27% │ -37.092 USDT   (-3.71%) │         3:43:00 │   0.05985 │ 92.255 USDT    (8.82%) │                           
                          │ * Best │  9/100 │      3 │    1     0     2  33.3 │     -1.60% │ -20.524 USDT   (-2.05%) │         7:00:00 │   0.02297 │ 41.595 USDT    (4.07%) │                           
                          │ * Best │ 14/100 │      3 │    2     0     1  66.7 │      9.05% │ 150.531 USDT   (15.05%) │        17:40:00 │  -0.06314 │ 20.212 USDT    (2.02%) │                           
                          │ Best   │ 35/100 │     24 │    8     0    16  33.3 │      0.32% │ 138.970 USDT   (13.90%) │        16:10:00 │  -0.09175 │ 95.309 USDT    (9.53%) │                           
                          │ Best   │ 47/100 │     35 │   15     0    20  42.9 │      4.84% │ 124.216 USDT   (12.42%) │ 3 days, 4:07:00 │  -0.22420 │ 41.822 USDT    (4.03%) │                           
                          └────────┴────────┴────────┴────────────────────────┴────────────┴─────────────────────────┴─────────────────┴───────────┴────────────────────────┘                           
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100/100 100% • 0:01:42 • 0:00:00
2025-09-18 09:24:11,390 - freqtrade.optimize.hyperopt.hyperopt - INFO - 100 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-18_09-22-14.fthypt'.
2025-09-18 09:24:11,536 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

    47/100:     35 trades. 15/0/20 Wins/Draws/Losses. Avg profit   4.84%. Median profit  -2.00%. Total profit 124.21587190 USDT (  12.42%). Avg duration 3 days, 4:07:00 min. Objective: -0.22420

{"params":{"confirmation_candle":false,"hammer_body_threshold":0.923,"hammer_head_threshold":0.716,"hammer_strength_threshold":0.01,"kinjun_threshold":3,"lookback_period_for_stoploss":0,"stoploss_margin":0.993,"take_profit_multiplier":2,"use_sell_signal_param":true,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Hyperopt Results
```json
{
  "timestamp": "2025-09-18T11:24:14.464786",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 7925,
  "wins_draws_losses": "15/0/20",
  "avg_profit_pct": 4.84,
  "median_profit_pct": -2.0,
  "total_profit_usdt": 124.2158719,
  "avg_duration": "3 days, 4:07:00",
  "objective": -0.2242,
  "avg_profit_per_day": 1.5261
}
```
