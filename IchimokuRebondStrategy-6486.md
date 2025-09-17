# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 63 / 0.05, Median: -0.6%, Total profit: -5.99%, Sortino: -0.24, Sharpe: -0.06, Calmar: -0.53, Drawdown: 0%)

---
            
**Strategy:** IchimokuRebondStrategy  
**Random State:** 6486  
**Timestamp:** 2025-09-17 17:48:49

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 6486,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 6486
```

## Hyperopt Output
```
2025-09-17 15:45:45,025 - freqtrade - INFO - freqtrade 2025.8
2025-09-17 15:45:45,976 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-17 15:45:48,974 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-17 15:45:48,982 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-17 15:45:48,983 - freqtrade.loggers - INFO - Logfile configured
2025-09-17 15:45:48,984 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-17 15:45:48,985 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-17 15:45:48,985 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-17 15:45:48,986 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-17 15:45:49,382 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-17 15:45:49,386 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-17 15:45:49,387 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-17 15:45:49,387 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 100 epochs ...
2025-09-17 15:45:49,387 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-17 15:45:49,388 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-17 15:45:49,388 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-17 15:45:49,389 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 6486
2025-09-17 15:45:49,389 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-17 15:45:49,390 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-17 15:45:49,390 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-17 15:45:49,391 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-17 15:45:49,393 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-17 15:45:49,409 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-17 15:45:49,410 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 15:45:49,413 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-17 15:45:49,423 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-17 15:45:49,431 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-17 15:45:49,432 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-17 15:45:49,466 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-17 15:45:51,692 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-17 15:45:51,796 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-17 15:45:51,798 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2025-09-17 15:45:51,799 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-17 15:45:51,799 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-17 15:45:51,799 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-17 15:45:51,800 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-17 15:45:51,800 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-17 15:45:51,801 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-17 15:45:51,801 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-17 15:45:51,801 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-17 15:45:51,802 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-17 15:45:51,802 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-17 15:45:51,802 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-17 15:45:51,803 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-17 15:45:51,803 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-17 15:45:51,803 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-17 15:45:51,804 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-17 15:45:51,804 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-17 15:45:51,805 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-17 15:45:51,805 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-17 15:45:51,806 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-17 15:45:51,806 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-17 15:45:51,807 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-17 15:45:51,807 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-17 15:45:51,807 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-17 15:45:51,808 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-17 15:45:51,808 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-17 15:45:51,808 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-17 15:45:51,809 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-17 15:45:51,809 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-17 15:45:51,810 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-17 15:45:51,810 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 15:45:51,836 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-17 15:45:51,861 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-17 15:45:51,862 - freqtrade.strategy.hyper - INFO - No params for buy found, using default values.
2025-09-17 15:45:51,863 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): hammer_body_threshold = 0.2
2025-09-17 15:45:51,863 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): hammer_head_threshold = 0.1
2025-09-17 15:45:51,864 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): hammer_strength_threshold = 0.01
2025-09-17 15:45:51,864 - freqtrade.strategy.hyper - INFO - No params for sell found, using default values.
2025-09-17 15:45:51,864 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): kinjun_threshold = 2
2025-09-17 15:45:51,865 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): lookback_period_for_stoploss = 5
2025-09-17 15:45:51,865 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): stoploss_margin = 0.999
2025-09-17 15:45:51,865 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): take_profit_multiplier = 2
2025-09-17 15:45:51,866 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_stoploss_param = True
2025-09-17 15:45:51,866 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_sell_signal_param = True
2025-09-17 15:45:51,866 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-17 15:45:51,888 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-17 15:45:51,889 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 6486
2025-09-17 15:45:51,946 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-17 15:45:52,004 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-17 15:45:52,013 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-17 15:45:52,058 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-17 15:45:52,108 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-17 15:45:52,158 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-17 15:45:52,165 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-17 15:45:52,177 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-17 15:45:52,805 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-17 15:45:52,808 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 15:45:52,823 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-17 15:45:54,603 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 15:45:54,619 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-17 15:45:56,629 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 15:45:56,646 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-17 15:45:58,681 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 15:45:58,701 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-17 15:46:00,155 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 15:46:00,170 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-17 15:46:01,740 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-17 15:46:02,179 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 16 CPU cores. Let's make them scream!
2025-09-17 15:46:02,180 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-17 15:46:02,181 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-17 15:46:02,182] A new study created in memory with name: no-name-0575f91e-9a9f-4425-8387-27b0e3f1854c
2025-09-17 15:46:02,251 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                           Hyperopt results                                                                                             
                         ┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓                          
                         ┃ Best   ┃  Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃     Avg duration ┃ Objective ┃     Max Drawdown (Acct) ┃                          
                         ┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩                          
                         │ * Best │  1/100 │     13 │    6     0     7  46.2 │      0.39% │  -2.605 USDT   (-0.26%) │ 87 days, 4:18:00 │   0.00287 │  68.739 USDT    (6.45%) │                          
                         │ * Best │  4/100 │      4 │    2     0     2  50.0 │      2.35% │  50.452 USDT    (5.05%) │          8:45:00 │  -0.03200 │  44.345 USDT    (4.05%) │                          
                         │ * Best │  5/100 │     79 │   36     0    43  45.6 │      0.23% │  82.512 USDT    (8.25%) │          6:55:00 │  -0.09003 │ 162.215 USDT   (13.36%) │                          
                         │ * Best │ 14/100 │     41 │   15     0    26  36.6 │      0.45% │ 133.480 USDT   (13.35%) │          8:25:00 │  -0.13479 │  54.509 USDT    (4.79%) │                          
                         │ Best   │ 34/100 │     71 │   24     0    47  33.8 │      0.57% │ 303.336 USDT   (30.33%) │         18:18:00 │  -0.17088 │ 219.493 USDT   (14.69%) │                          
                         │ Best   │ 72/100 │     53 │   22     0    31  41.5 │      0.52% │ 223.701 USDT   (22.37%) │          6:55:00 │  -0.24158 │ 112.613 USDT    (9.82%) │                          
                         └────────┴────────┴────────┴────────────────────────┴────────────┴─────────────────────────┴──────────────────┴───────────┴─────────────────────────┘                          
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100/100 100% • 0:02:09 • 0:00:00
2025-09-17 15:48:11,463 - freqtrade.optimize.hyperopt.hyperopt - INFO - 100 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-17_15-45-49.fthypt'.
2025-09-17 15:48:11,650 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

    72/100:     53 trades. 22/0/31 Wins/Draws/Losses. Avg profit   0.52%. Median profit  -0.60%. Total profit 223.70129446 USDT (  22.37%). Avg duration 6:55:00 min. Objective: -0.24158

{"params":{"hammer_body_threshold":0.454,"hammer_head_threshold":0.256,"hammer_strength_threshold":0.003,"kinjun_threshold":1,"lookback_period_for_stoploss":6,"stoploss_margin":0.999,"take_profit_multiplier":1.5,"use_sell_signal_param":true,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231
```

## Backtesting Output
```
2025-09-17 15:48:16,145 - freqtrade - INFO - freqtrade 2025.8
2025-09-17 15:48:16,534 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-17 15:48:18,194 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-17 15:48:18,199 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-17 15:48:18,200 - freqtrade.loggers - INFO - Logfile configured
2025-09-17 15:48:18,200 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-17 15:48:18,201 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-17 15:48:18,201 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-17 15:48:18,201 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-17 15:48:18,202 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-17 15:48:18,464 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-17 15:48:18,467 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-17 15:48:18,467 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-17 15:48:18,468 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-17 15:48:18,468 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-17 15:48:18,469 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-17 15:48:18,470 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-17 15:48:18,482 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-17 15:48:18,483 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 15:48:18,486 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-17 15:48:18,487 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-17 15:48:18,487 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-17 15:48:18,513 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-17 15:48:20,931 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-17 15:48:21,059 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-17 15:48:21,063 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-17 15:48:21,070 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-17 15:48:21,071 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-17 15:48:21,071 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-17 15:48:21,072 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-17 15:48:21,072 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-17 15:48:21,073 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-17 15:48:21,074 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-17 15:48:21,074 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-17 15:48:21,075 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-17 15:48:21,075 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-17 15:48:21,076 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-17 15:48:21,076 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-17 15:48:21,077 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-17 15:48:21,078 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-17 15:48:21,079 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-17 15:48:21,080 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-17 15:48:21,081 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-17 15:48:21,082 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-17 15:48:21,082 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-17 15:48:21,084 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-17 15:48:21,085 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-17 15:48:21,086 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-17 15:48:21,087 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-17 15:48:21,088 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-17 15:48:21,089 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-17 15:48:21,089 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-17 15:48:21,090 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-17 15:48:21,091 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-17 15:48:21,092 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 15:48:21,132 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-17 15:48:21,171 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-17 15:48:21,236 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 15:48:21,308 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 15:48:21,379 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 15:48:21,469 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 15:48:21,548 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 15:48:21,589 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-17 15:48:21,867 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 15:48:22,386 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 15:48:22,932 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 15:48:23,376 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 15:48:23,892 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 15:48:25,500 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-17 15:48:25,506 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-17 15:48:25,507 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-17 15:48:25,508 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.454
2025-09-17 15:48:25,508 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.256
2025-09-17 15:48:25,509 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.003
2025-09-17 15:48:25,509 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1
2025-09-17 15:48:25,510 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 6
2025-09-17 15:48:25,511 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-09-17 15:48:25,511 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-17 15:48:25,512 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-17 15:48:25,512 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-17 15:48:25,513 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-17 15:48:25,519 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 15:48:25,542 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 15:48:28,856 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 15:48:28,873 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 15:48:32,204 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 15:48:32,219 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 15:48:35,790 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 15:48:35,804 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 15:48:38,645 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 15:48:38,660 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 15:48:41,730 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-17 15:48:48,254 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-17_15-48-48.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │     17 │         0.59 │         102.492 │        10.25 │      8:49:00 │   10     0     7  58.8 │
│ LTC/USDT │     10 │         0.24 │          28.252 │         2.83 │      5:45:00 │    5     0     5  50.0 │
│ BTC/USDT │     13 │        -0.42 │         -52.282 │        -5.23 │      8:48:00 │    2     0    11  15.4 │
│ ETH/USDT │     12 │        -0.53 │         -66.931 │        -6.69 │      3:53:00 │    3     0     9  25.0 │
│ XRP/USDT │     11 │        -0.82 │         -71.395 │        -7.14 │      5:00:00 │    2     0     9  18.2 │
│    TOTAL │     63 │        -0.13 │         -59.864 │        -5.99 │      6:43:00 │   22     0    41  34.9 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
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
│     OTHER │      63 │        -0.13 │         -59.864 │        -5.99 │      6:43:00 │   22     0    41  34.9 │
│     TOTAL │      63 │        -0.13 │         -59.864 │        -5.99 │      6:43:00 │   22     0    41  34.9 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │    22 │         1.62 │         356.204 │        35.62 │      8:41:00 │   22     0     0   100 │
│      exit_signal │     7 │        -1.37 │         -71.676 │        -7.17 │     10:34:00 │    0     0     7     0 │
│        stop_loss │    34 │        -1.01 │        -344.392 │       -34.44 │      4:39:00 │    0     0    34     0 │
│            TOTAL │    63 │        -0.13 │         -59.864 │        -5.99 │      6:43:00 │   22     0    41  34.9 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1.5R │     22 │         1.62 │         356.204 │        35.62 │      8:41:00 │   22     0     0   100 │
│           │      exit_signal │      7 │        -1.37 │         -71.676 │        -7.17 │     10:34:00 │    0     0     7     0 │
│           │        stop_loss │     34 │        -1.01 │        -344.392 │       -34.44 │      4:39:00 │    0     0    34     0 │
│     TOTAL │                  │     63 │        -0.13 │         -59.864 │        -5.99 │      6:43:00 │   22     0    41  34.9 │
└───────────┴──────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 63 / 0.05                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 940.136 USDT                   │
│ Absolute profit               │ -59.864 USDT                   │
│ Total profit %                │ -5.99%                         │
│ CAGR %                        │ -1.66%                         │
│ Sortino                       │ -0.24                          │
│ Sharpe                        │ -0.06                          │
│ Calmar                        │ -0.53                          │
│ SQN                           │ -0.55                          │
│ Profit factor                 │ 0.86                           │
│ Expectancy (Ratio)            │ -0.95 (-0.09)                  │
│ Avg. daily profit             │ -0.044 USDT                    │
│ Avg. stake amount             │ 980.922 USDT                   │
│ Total trade volume            │ 123783.68 USDT                 │
│                               │                                │
│ Best Pair                     │ BNB/USDT 10.25%                │
│ Worst Pair                    │ XRP/USDT -7.14%                │
│ Best trade                    │ LTC/USDT 3.29%                 │
│ Worst trade                   │ LTC/USDT -2.57%                │
│ Best day                      │ 33.201 USDT                    │
│ Worst day                     │ -24.913 USDT                   │
│ Days win/draw/lose            │ 22 / 1156 / 38                 │
│ Min/Max/Avg. Duration Winners │ 0d 00:25 / 1d 07:20 / 0d 08:41 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:10 / 1d 01:00 / 0d 05:40 │
│ Max Consecutive Wins / Loss   │ 3 / 7                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 926.342 USDT                   │
│ Max balance                   │ 1102.415 USDT                  │
│ Max % of account underwater   │ 15.97%                         │
│ Absolute drawdown             │ 176.073 USDT (15.97%)          │
│ Drawdown duration             │ 831 days 11:10:00              │
│ Profit at drawdown start      │ 102.415 USDT                   │
│ Profit at drawdown end        │ -73.658 USDT                   │
│ Drawdown start                │ 2022-08-06 17:35:00            │
│ Drawdown end                  │ 2024-11-15 04:45:00            │
│ Market change                 │ 91.49%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     63 │        -0.13 │         -59.864 │        -5.99 │      6:43:00 │   22     0    41  34.9 │ 176.073 USDT  15.97% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
