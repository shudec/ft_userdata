# Freqtrade Hyperopt Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 2000  
**Timestamp:** 2025-09-19 12:30:00

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 2000,
  "epochs": 200,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 200 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 2000
```

## Hyperopt Output
```
2025-09-19 10:27:10,345 - freqtrade - INFO - freqtrade 2025.8
2025-09-19 10:27:10,849 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-19 10:27:12,059 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-19 10:27:12,065 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-19 10:27:12,065 - freqtrade.loggers - INFO - Logfile configured
2025-09-19 10:27:12,066 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-19 10:27:12,066 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-19 10:27:12,067 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-19 10:27:12,067 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-19 10:27:12,352 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-19 10:27:12,355 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-19 10:27:12,356 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-19 10:27:12,356 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 200 epochs ...
2025-09-19 10:27:12,356 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-19 10:27:12,356 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-19 10:27:12,357 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-19 10:27:12,357 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 2000
2025-09-19 10:27:12,357 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-19 10:27:12,358 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-19 10:27:12,358 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-19 10:27:12,358 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-19 10:27:12,359 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-19 10:27:12,369 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-19 10:27:12,369 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 10:27:12,372 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-19 10:27:12,378 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-19 10:27:12,384 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-19 10:27:12,384 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-19 10:27:12,403 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-19 10:27:16,344 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-19 10:27:16,459 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-19 10:27:16,462 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-19 10:27:16,467 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-19 10:27:16,468 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-19 10:27:16,468 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-19 10:27:16,469 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-19 10:27:16,470 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-19 10:27:16,470 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-19 10:27:16,471 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-19 10:27:16,472 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-19 10:27:16,472 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-19 10:27:16,473 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-19 10:27:16,474 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-19 10:27:16,475 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-19 10:27:16,475 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-19 10:27:16,476 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-19 10:27:16,477 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-19 10:27:16,477 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-19 10:27:16,478 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-19 10:27:16,479 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-19 10:27:16,479 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-19 10:27:16,480 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-19 10:27:16,481 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-19 10:27:16,481 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-19 10:27:16,482 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-19 10:27:16,482 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-19 10:27:16,483 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-19 10:27:16,483 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-19 10:27:16,483 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-19 10:27:16,484 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-19 10:27:16,484 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-19 10:27:16,485 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 10:27:16,504 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-19 10:27:16,530 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-19 10:27:16,531 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-19 10:27:16,532 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-19 10:27:16,533 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 3
2025-09-19 10:27:16,533 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.962
2025-09-19 10:27:16,534 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.064
2025-09-19 10:27:16,534 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.035
2025-09-19 10:27:16,534 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.019
2025-09-19 10:27:16,535 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-19 10:27:16,535 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 2
2025-09-19 10:27:16,536 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-09-19 10:27:16,536 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-19 10:27:16,536 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-19 10:27:16,537 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-19 10:27:16,537 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-19 10:27:16,557 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-19 10:27:16,558 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 2000
2025-09-19 10:27:16,620 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-19 10:27:16,695 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-19 10:27:16,704 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-19 10:27:16,750 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-19 10:27:16,803 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-19 10:27:16,859 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-19 10:27:16,868 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-19 10:27:16,886 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-19 10:27:17,474 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-19 10:27:17,476 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 10:27:17,494 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-19 10:27:19,118 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 10:27:19,131 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-19 10:27:20,669 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 10:27:20,682 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-19 10:27:22,017 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 10:27:22,031 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-19 10:27:23,199 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 10:27:23,215 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-19 10:27:24,890 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-19 10:27:25,362 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 16 CPU cores. Let's make them scream!
2025-09-19 10:27:25,363 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-19 10:27:25,364 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-19 10:27:25,364] A new study created in memory with name: no-name-3a528390-eee0-4cec-b26e-3161bae9325b
2025-09-19 10:27:25,412 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                            ┏━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓                            
                            ┃ Best   ┃   Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                 Profit ┃ Avg duration ┃ Objective ┃    Max Drawdown (Acct) ┃                            
                            ┡━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩                            
                            │ * Best │   1/200 │      2 │    1     0     1  50.0 │     -0.34% │ -8.512 USDT   (-0.85%) │     18:30:00 │   0.02900 │ 10.739 USDT    (1.07%) │                            
                            │ * Best │   2/200 │      2 │    1     0     1  50.0 │      0.09% │ -1.864 USDT   (-0.19%) │     15:30:00 │   0.00750 │  6.423 USDT    (0.64%) │                            
                            │ * Best │   4/200 │      2 │    1     0     1  50.0 │      1.87% │ 36.742 USDT    (3.67%) │      5:30:00 │  -0.03372 │  5.694 USDT    (0.57%) │                            
                            │ * Best │  12/200 │      3 │    2     0     1  66.7 │      0.91% │ 26.963 USDT    (2.70%) │      9:20:00 │  -0.03543 │ 14.779 USDT    (1.48%) │                            
                            │ * Best │  28/200 │      3 │    2     0     1  66.7 │      1.58% │ 47.005 USDT    (4.70%) │     10:20:00 │  -0.04916 │ 13.801 USDT    (1.38%) │                            
                            │ Best   │ 193/200 │      3 │    2     0     1  66.7 │      1.61% │ 48.044 USDT    (4.80%) │     10:20:00 │  -0.05132 │ 12.822 USDT    (1.28%) │                            
                            └────────┴─────────┴────────┴────────────────────────┴────────────┴────────────────────────┴──────────────┴───────────┴────────────────────────┘                            
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 200/200 100% • 0:02:32 • 0:00:00
2025-09-19 10:29:57,841 - freqtrade.optimize.hyperopt.hyperopt - INFO - 200 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-19_10-27-12.fthypt'.
2025-09-19 10:29:58,057 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

   193/200:      3 trades. 2/0/1 Wins/Draws/Losses. Avg profit   1.61%. Median profit   2.59%. Total profit 48.04415791 USDT (   4.80%). Avg duration 10:20:00 min. Objective: -0.05132

{"params":{"confirmation_candle":false,"engulfing_size_threshold":2,"flat_kinjun_threshold":3,"hammer_body_threshold":0.858,"hammer_head_threshold":0.261,"hammer_strength_threshold":0.025,"kinjun_proximity_threshold":0.017,"kinjun_threshold":0.999,"lookback_period_for_stoploss":10,"stoploss_margin":1.0,"take_profit_multiplier":1.5,"use_sell_signal_param":false,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Hyperopt Results
```json
{
  "timestamp": "2025-09-19T12:30:00.504087",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 2000,
  "wins_draws_losses": "2/0/1",
  "avg_profit_pct": 1.61,
  "median_profit_pct": 2.59,
  "total_profit_usdt": 48.04415791,
  "avg_duration": "10:20:00",
  "objective": -0.05132,
  "avg_profit_per_day": 3.7394
}
```
