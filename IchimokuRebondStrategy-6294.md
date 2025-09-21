# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 16 / 0.01, Median: 3.81%, Total profit: -7.21%, Sortino: -0.37, Sharpe: -0.05, Calmar: -0.87, Drawdown: 11.69%)

---
            
**Strategy:** IchimokuRebondStrategy  
**Random State:** 6294  
**Timestamp:** 2025-09-18 20:57:27

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 6294,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 6294
```

## Hyperopt Output
```
2025-09-18 18:54:51,053 - freqtrade - INFO - freqtrade 2025.7
2025-09-18 18:54:51,855 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-18 18:54:51,856 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-18 18:54:53,524 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-18 18:54:53,528 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-18 18:54:53,529 - freqtrade.loggers - INFO - Logfile configured
2025-09-18 18:54:53,529 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-18 18:54:53,530 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-18 18:54:53,530 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-18 18:54:53,530 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-18 18:54:53,539 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-18 18:54:53,539 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-18 18:54:53,540 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-18 18:54:53,540 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 100 epochs ...
2025-09-18 18:54:53,541 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-18 18:54:53,541 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-18 18:54:53,542 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-18 18:54:53,542 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 6294
2025-09-18 18:54:53,542 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-18 18:54:53,543 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-18 18:54:53,543 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-18 18:54:53,544 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-18 18:54:53,545 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-18 18:54:53,565 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-18 18:54:53,566 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 18:54:53,570 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-18 18:54:53,571 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-18 18:54:53,573 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-18 18:54:53,574 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-18 18:54:53,622 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-18 18:54:56,062 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-18 18:54:56,107 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-18 18:54:56,108 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-18 18:54:56,109 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-18 18:54:56,109 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-18 18:54:56,110 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-18 18:54:56,110 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-18 18:54:56,110 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-18 18:54:56,111 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-18 18:54:56,111 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-18 18:54:56,112 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-18 18:54:56,112 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-18 18:54:56,113 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-18 18:54:56,113 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-18 18:54:56,114 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-18 18:54:56,114 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-18 18:54:56,115 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-18 18:54:56,115 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-18 18:54:56,116 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-18 18:54:56,116 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-18 18:54:56,117 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-18 18:54:56,118 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-18 18:54:56,118 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-18 18:54:56,119 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-18 18:54:56,120 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-18 18:54:56,120 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-18 18:54:56,121 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-18 18:54:56,122 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-18 18:54:56,122 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-18 18:54:56,123 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-18 18:54:56,124 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-18 18:54:56,124 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-18 18:54:56,125 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 18:54:56,132 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-18 18:54:56,172 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-18 18:54:56,174 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-18 18:54:56,175 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.642
2025-09-18 18:54:56,175 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.265
2025-09-18 18:54:56,176 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.009
2025-09-18 18:54:56,176 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 6
2025-09-18 18:54:56,177 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 0
2025-09-18 18:54:56,177 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.994
2025-09-18 18:54:56,178 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2.5
2025-09-18 18:54:56,178 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-18 18:54:56,179 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-18 18:54:56,179 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-18 18:54:56,192 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-18 18:54:56,193 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 6294
2025-09-18 18:54:56,242 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-18 18:54:56,311 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-18 18:54:56,320 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-18 18:54:56,370 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-18 18:54:56,417 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-18 18:54:56,456 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-18 18:54:56,468 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-18 18:54:56,488 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-18 18:54:57,360 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-18 18:54:57,363 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 18:54:57,376 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-18 18:54:59,025 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 18:54:59,035 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-18 18:55:00,620 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 18:55:00,630 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-18 18:55:02,054 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 18:55:02,064 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-18 18:55:03,284 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 18:55:03,299 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-18 18:55:04,782 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-18 18:55:05,073 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 20 CPU cores. Let's make them scream!
2025-09-18 18:55:05,073 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-18 18:55:05,075 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-18 18:55:05,075] A new study created in memory with name: no-name-ca09873c-ff89-41be-bb3c-a79fd3e0ece7
2025-09-18 18:55:05,129 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                           Hyperopt results                                                                                             
                          ┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓                           
                          ┃ Best   ┃  Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃   Avg duration ┃ Objective ┃     Max Drawdown (Acct) ┃                           
                          ┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩                           
                          │ * Best │  5/100 │     19 │    6     0    13  31.6 │      0.38% │ 120.436 USDT   (12.04%) │       19:03:00 │  -0.06631 │ 105.881 USDT   (10.00%) │                           
                          │ * Best │ 27/100 │      9 │    5     0     4  55.6 │      2.22% │ 233.525 USDT   (23.35%) │ 1 day, 5:40:00 │  -0.12425 │  26.384 USDT    (2.09%) │                           
                          │ Best   │ 43/100 │     12 │    7     0     5  58.3 │      1.73% │ 244.940 USDT   (24.49%) │       22:40:00 │  -0.15131 │  46.562 USDT    (4.39%) │                           
                          │ Best   │ 67/100 │     12 │    7     0     5  58.3 │      1.75% │ 252.414 USDT   (25.24%) │       22:30:00 │  -0.15184 │  45.970 USDT    (4.32%) │                           
                          │ Best   │ 70/100 │     18 │   10     0     8  55.6 │      1.60% │ 297.455 USDT   (29.75%) │       13:20:00 │  -0.17756 │  41.872 USDT    (4.13%) │                           
                          │ Best   │ 99/100 │     16 │   10     0     6  62.5 │      2.56% │ 379.592 USDT   (37.96%) │       17:26:00 │  -0.22019 │  29.737 USDT    (2.11%) │                           
                          └────────┴────────┴────────┴────────────────────────┴────────────┴─────────────────────────┴────────────────┴───────────┴─────────────────────────┘                           
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100/100 100% • 0:01:48 • 0:00:00
2025-09-18 18:56:53,957 - freqtrade.optimize.hyperopt.hyperopt - INFO - 100 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-18_18-54-53.fthypt'.
2025-09-18 18:56:53,992 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

    99/100:     16 trades. 10/0/6 Wins/Draws/Losses. Avg profit   2.56%. Median profit   3.81%. Total profit 379.59214547 USDT (  37.96%). Avg duration 17:26:00 min. Objective: -0.22019

{"params":{"confirmation_candle":true,"hammer_body_threshold":0.516,"hammer_head_threshold":0.974,"hammer_strength_threshold":0.009,"kinjun_threshold":2,"lookback_period_for_stoploss":3,"stoploss_margin":0.995,"take_profit_multiplier":1.5,"use_sell_signal_param":true,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231
```

## Backtesting Output
```
2025-09-18 18:56:57,249 - freqtrade - INFO - freqtrade 2025.7
2025-09-18 18:56:57,611 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-18 18:56:57,612 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-18 18:56:59,527 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-18 18:56:59,530 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-18 18:56:59,530 - freqtrade.loggers - INFO - Logfile configured
2025-09-18 18:56:59,531 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-18 18:56:59,531 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-18 18:56:59,532 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-18 18:56:59,532 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-18 18:56:59,532 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-18 18:56:59,540 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-18 18:56:59,540 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-18 18:56:59,541 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-18 18:56:59,541 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-18 18:56:59,542 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-18 18:56:59,542 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-18 18:56:59,543 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-18 18:56:59,563 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-18 18:56:59,564 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 18:56:59,568 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-18 18:56:59,570 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-18 18:56:59,570 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-18 18:56:59,606 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-18 18:57:02,011 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-18 18:57:02,049 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-18 18:57:02,050 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-18 18:57:02,051 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-18 18:57:02,051 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-18 18:57:02,052 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-18 18:57:02,052 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-18 18:57:02,053 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-18 18:57:02,053 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-18 18:57:02,053 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-18 18:57:02,054 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-18 18:57:02,054 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-18 18:57:02,055 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-18 18:57:02,055 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-18 18:57:02,055 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-18 18:57:02,056 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-18 18:57:02,056 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-18 18:57:02,057 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-18 18:57:02,057 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-18 18:57:02,058 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-18 18:57:02,058 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-18 18:57:02,058 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-18 18:57:02,059 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-18 18:57:02,059 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-18 18:57:02,060 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-18 18:57:02,060 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-18 18:57:02,061 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-18 18:57:02,061 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-18 18:57:02,062 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-18 18:57:02,062 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-18 18:57:02,063 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-18 18:57:02,063 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 18:57:02,068 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-18 18:57:02,103 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-18 18:57:02,138 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-18 18:57:02,192 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-18 18:57:02,242 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-18 18:57:02,292 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-18 18:57:02,344 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-18 18:57:02,376 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-18 18:57:02,461 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-18 18:57:02,697 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-18 18:57:02,943 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-18 18:57:03,175 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-18 18:57:03,427 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-18 18:57:05,085 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-18 18:57:05,086 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-18 18:57:05,086 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-18 18:57:05,087 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-18 18:57:05,087 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.516
2025-09-18 18:57:05,088 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.974
2025-09-18 18:57:05,088 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.009
2025-09-18 18:57:05,089 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 2
2025-09-18 18:57:05,089 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 3
2025-09-18 18:57:05,089 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.995
2025-09-18 18:57:05,090 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-18 18:57:05,090 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-18 18:57:05,090 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-18 18:57:05,090 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-18 18:57:05,092 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 18:57:05,101 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-18 18:57:08,026 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 18:57:08,035 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-18 18:57:10,960 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 18:57:10,968 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-18 18:57:14,107 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 18:57:14,116 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-18 18:57:17,195 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 18:57:17,203 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-18 18:57:19,905 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-18 18:57:25,945 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-18_18-57-25.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │      3 │         1.88 │          39.024 │          3.9 │ 1 day, 20:03:00 │    2     0     1  66.7 │
│ ETH/USDT │      0 │          0.0 │           0.000 │          0.0 │            0:00 │    0     0     0     0 │
│ BNB/USDT │      4 │         0.78 │          -1.608 │        -0.16 │         9:26:00 │    2     0     2  50.0 │
│ XRP/USDT │      6 │        -1.38 │         -52.907 │        -5.29 │        12:25:00 │    1     0     5  16.7 │
│ LTC/USDT │      3 │        -2.08 │         -56.607 │        -5.66 │         5:25:00 │    0     0     3     0 │
│    TOTAL │     16 │        -0.36 │         -72.097 │        -7.21 │        16:18:00 │    5     0    11  31.2 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                ENTER TAG STATS                                                
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │      16 │        -0.36 │         -72.097 │        -7.21 │     16:18:00 │    5     0    11  31.2 │
│     TOTAL │      16 │        -0.36 │         -72.097 │        -7.21 │     16:18:00 │    5     0    11  31.2 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                   EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │     5 │         3.63 │         120.258 │        12.03 │ 1 day, 11:21:00 │    5     0     0   100 │
│      exit_signal │     2 │        -2.74 │         -25.171 │        -2.52 │        14:00:00 │    0     0     2     0 │
│        stop_loss │     9 │        -2.05 │        -167.184 │       -16.72 │         6:13:00 │    0     0     9     0 │
│            TOTAL │    16 │        -0.36 │         -72.097 │        -7.21 │        16:18:00 │    5     0    11  31.2 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                          MIXED TAG STATS                                                           
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1.5R │      5 │         3.63 │         120.258 │        12.03 │ 1 day, 11:21:00 │    5     0     0   100 │
│           │      exit_signal │      2 │        -2.74 │         -25.171 │        -2.52 │        14:00:00 │    0     0     2     0 │
│           │        stop_loss │      9 │        -2.05 │        -167.184 │       -16.72 │         6:13:00 │    0     0     9     0 │
│     TOTAL │                  │     16 │        -0.36 │         -72.097 │        -7.21 │        16:18:00 │    5     0    11  31.2 │
└───────────┴──────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-11 17:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 16 / 0.01                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 927.903 USDT                   │
│ Absolute profit               │ -72.097 USDT                   │
│ Total profit %                │ -7.21%                         │
│ CAGR %                        │ -2.00%                         │
│ Sortino                       │ -0.37                          │
│ Sharpe                        │ -0.05                          │
│ Calmar                        │ -0.87                          │
│ SQN                           │ -0.86                          │
│ Profit factor                 │ 0.63                           │
│ Expectancy (Ratio)            │ -4.51 (-0.26)                  │
│ Avg. daily profit             │ -0.053 USDT                    │
│ Avg. stake amount             │ 773.863 USDT                   │
│ Total trade volume            │ 24740.954 USDT                 │
│                               │                                │
│ Best Pair                     │ BTC/USDT 3.90%                 │
│ Worst Pair                    │ LTC/USDT -5.66%                │
│ Best trade                    │ BTC/USDT 4.48%                 │
│ Worst trade                   │ XRP/USDT -3.00%                │
│ Best day                      │ 33.98 USDT                     │
│ Worst day                     │ -21.83 USDT                    │
│ Days win/draw/lose            │ 4 / 1115 / 11                  │
│ Min/Max/Avg. Duration Winners │ 0d 09:20 / 4d 01:45 / 1d 11:21 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:20 / 0d 21:00 / 0d 07:38 │
│ Max Consecutive Wins / Loss   │ 3 / 7                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 889.416 USDT                   │
│ Max balance                   │ 1007.164 USDT                  │
│ Max % of account underwater   │ 11.69%                         │
│ Absolute Drawdown (Account)   │ 11.69%                         │
│ Absolute Drawdown             │ 117.748 USDT                   │
│ Drawdown high                 │ 7.164 USDT                     │
│ Drawdown low                  │ -110.584 USDT                  │
│ Drawdown Start                │ 2022-07-07 14:35:00            │
│ Drawdown End                  │ 2024-02-16 14:50:00            │
│ Market change                 │ 94.84%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     16 │        -0.36 │         -72.097 │        -7.21 │     16:18:00 │    5     0    11  31.2 │ 117.748 USDT  11.69% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
