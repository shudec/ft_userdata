# Freqtrade Hyperopt Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 539  
**Timestamp:** 2025-09-18 11:57:34

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 539,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 539
```

## Hyperopt Output
```
2025-09-18 09:55:50,755 - freqtrade - INFO - freqtrade 2025.8
2025-09-18 09:55:51,249 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-18 09:55:52,450 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-18 09:55:52,456 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-18 09:55:52,457 - freqtrade.loggers - INFO - Logfile configured
2025-09-18 09:55:52,457 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-18 09:55:52,458 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-18 09:55:52,458 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-18 09:55:52,459 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-18 09:55:52,750 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-18 09:55:52,753 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-18 09:55:52,753 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-18 09:55:52,754 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 100 epochs ...
2025-09-18 09:55:52,754 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-18 09:55:52,754 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-18 09:55:52,755 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-18 09:55:52,755 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 539
2025-09-18 09:55:52,756 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-18 09:55:52,756 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-18 09:55:52,757 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-18 09:55:52,757 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-18 09:55:52,758 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-18 09:55:52,769 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-18 09:55:52,769 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 09:55:52,772 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-18 09:55:52,780 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-18 09:55:52,788 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-18 09:55:52,788 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-18 09:55:52,814 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-18 09:55:55,363 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-18 09:55:55,460 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-18 09:55:55,463 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-18 09:55:55,467 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-18 09:55:55,467 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-18 09:55:55,468 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-18 09:55:55,468 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-18 09:55:55,468 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-18 09:55:55,469 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-18 09:55:55,469 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-18 09:55:55,470 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-18 09:55:55,470 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-18 09:55:55,471 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-18 09:55:55,471 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-18 09:55:55,471 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-18 09:55:55,472 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-18 09:55:55,472 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-18 09:55:55,472 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-18 09:55:55,473 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-18 09:55:55,473 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-18 09:55:55,474 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-18 09:55:55,474 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-18 09:55:55,474 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-18 09:55:55,475 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-18 09:55:55,476 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-18 09:55:55,476 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-18 09:55:55,477 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-18 09:55:55,477 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-18 09:55:55,478 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-18 09:55:55,478 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-18 09:55:55,479 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-18 09:55:55,479 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-18 09:55:55,479 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 09:55:55,498 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-18 09:55:55,531 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-18 09:55:55,532 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-18 09:55:55,533 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): flat_kinjun_threshold = 4
2025-09-18 09:55:55,533 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.923
2025-09-18 09:55:55,534 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.716
2025-09-18 09:55:55,534 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.01
2025-09-18 09:55:55,534 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 3
2025-09-18 09:55:55,535 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 0
2025-09-18 09:55:55,535 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-18 09:55:55,536 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-18 09:55:55,536 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-18 09:55:55,536 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-18 09:55:55,537 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-18 09:55:55,558 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-18 09:55:55,558 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 539
2025-09-18 09:55:55,616 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-18 09:55:55,674 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-18 09:55:55,684 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-18 09:55:55,732 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-18 09:55:55,790 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-18 09:55:55,845 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-18 09:55:55,854 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-18 09:55:55,869 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-18 09:55:56,596 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-18 09:55:56,599 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 09:55:56,618 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-18 09:55:58,016 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 09:55:58,029 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-18 09:55:59,273 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 09:55:59,288 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-18 09:56:00,352 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 09:56:00,366 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-18 09:56:01,276 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 09:56:01,291 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-18 09:56:02,413 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-18 09:56:02,855 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 16 CPU cores. Let's make them scream!
2025-09-18 09:56:02,856 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-18 09:56:02,858 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-18 09:56:02,858] A new study created in memory with name: no-name-628f2c05-b9cf-41fb-94af-0876b43402d2
2025-09-18 09:56:02,910 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                           Hyperopt results                                                                                             
                           ┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓                            
                           ┃ Best   ┃  Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃ Avg duration ┃ Objective ┃     Max Drawdown (Acct) ┃                            
                           ┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩                            
                           │ * Best │  1/100 │      2 │    0     0     2     0 │     -3.68% │ -25.401 USDT   (-2.54%) │      6:00:00 │   0.07204 │  25.401 USDT    (2.54%) │                            
                           │ * Best │  4/100 │     12 │    5     0     7  41.7 │      1.20% │  64.815 USDT    (6.48%) │      8:50:00 │  -0.04508 │  61.694 USDT    (5.74%) │                            
                           │ Best   │ 38/100 │     10 │    3     0     7  30.0 │      1.12% │  98.002 USDT    (9.80%) │     15:36:00 │  -0.05972 │  95.344 USDT    (7.99%) │                            
                           │ Best   │ 92/100 │     50 │   20     0    30  40.0 │      0.75% │ 139.671 USDT   (13.97%) │      9:02:00 │  -0.10153 │ 213.793 USDT   (16.73%) │                            
                           └────────┴────────┴────────┴────────────────────────┴────────────┴─────────────────────────┴──────────────┴───────────┴─────────────────────────┘                            
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100/100 100% • 0:01:28 • 0:00:00
2025-09-18 09:57:31,245 - freqtrade.optimize.hyperopt.hyperopt - INFO - 100 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-18_09-55-52.fthypt'.
2025-09-18 09:57:31,420 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

    92/100:     50 trades. 20/0/30 Wins/Draws/Losses. Avg profit   0.75%. Median profit  -1.64%. Total profit 139.67060153 USDT (  13.97%). Avg duration 9:02:00 min. Objective: -0.10153

{"params":{"confirmation_candle":false,"flat_kinjun_threshold":4,"hammer_body_threshold":0.796,"hammer_head_threshold":0.971,"hammer_strength_threshold":0.013,"kinjun_threshold":10,"lookback_period_for_stoploss":5,"stoploss_margin":0.995,"take_profit_multiplier":1.5,"use_sell_signal_param":false,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Hyperopt Results
```json
{
  "timestamp": "2025-09-18T11:57:34.503123",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 539,
  "wins_draws_losses": "20/0/30",
  "avg_profit_pct": 0.75,
  "median_profit_pct": -1.64,
  "total_profit_usdt": 139.67060153,
  "avg_duration": "9:02:00",
  "objective": -0.10153,
  "avg_profit_per_day": 1.9926
}
```
