# Freqtrade Automation Log

## Performance Indicator
**Status:** � GREEN  
**Description:** Excellent Performance (Total trades: 16 / 0.01, Median: 30.81%, Total profit: 11.74%, Sortino: 1.05, Sharpe: 0.06, Calmar: 1.81, Drawdown: 9.19%)

---
            
**Strategy:** IchimokuRebondStrategy  
**Random State:** 5761  
**Timestamp:** 2025-09-17 22:09:29

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 5761,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 5761
```

## Hyperopt Output
```
2025-09-17 19:57:01,178 - freqtrade - INFO - freqtrade 2025.7
2025-09-17 19:57:02,090 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-17 19:57:02,091 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-17 19:57:04,597 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-17 19:57:04,602 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-17 19:57:04,603 - freqtrade.loggers - INFO - Logfile configured
2025-09-17 19:57:04,603 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-17 19:57:04,604 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-17 19:57:04,605 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-17 19:57:04,605 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-17 19:57:04,617 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-17 19:57:04,618 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-17 19:57:04,619 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-17 19:57:04,620 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 100 epochs ...
2025-09-17 19:57:04,621 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-17 19:57:04,622 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-17 19:57:04,623 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-17 19:57:04,623 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 5761
2025-09-17 19:57:04,624 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-17 19:57:04,625 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-17 19:57:04,625 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-17 19:57:04,626 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-17 19:57:04,628 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-17 19:57:04,652 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-17 19:57:04,653 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 19:57:04,659 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-17 19:57:04,660 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-17 19:57:04,662 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-17 19:57:04,663 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-17 19:57:04,709 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-17 19:57:07,879 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-17 19:57:07,934 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-17 19:57:07,935 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-17 19:57:07,936 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-17 19:57:07,937 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-17 19:57:07,937 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-17 19:57:07,938 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-17 19:57:07,938 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-17 19:57:07,939 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-17 19:57:07,939 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-17 19:57:07,940 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-17 19:57:07,940 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-17 19:57:07,941 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-17 19:57:07,942 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-17 19:57:07,942 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-17 19:57:07,943 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-17 19:57:07,943 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-17 19:57:07,944 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-17 19:57:07,944 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-17 19:57:07,945 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-17 19:57:07,945 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-17 19:57:07,946 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-17 19:57:07,946 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-17 19:57:07,946 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-17 19:57:07,947 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-17 19:57:07,947 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-17 19:57:07,948 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-17 19:57:07,948 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-17 19:57:07,949 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-17 19:57:07,949 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-17 19:57:07,950 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-17 19:57:07,950 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-17 19:57:07,951 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 19:57:07,957 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-17 19:57:08,002 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-17 19:57:08,005 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): confirmation_candle = True
2025-09-17 19:57:08,006 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.655
2025-09-17 19:57:08,007 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.937
2025-09-17 19:57:08,007 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.007
2025-09-17 19:57:08,008 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0
2025-09-17 19:57:08,009 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 4
2025-09-17 19:57:08,009 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.996
2025-09-17 19:57:08,010 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2.5
2025-09-17 19:57:08,010 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-17 19:57:08,011 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-17 19:57:08,012 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-17 19:57:08,025 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-17 19:57:08,026 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 5761
2025-09-17 19:57:08,081 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-17 19:57:08,160 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-17 19:57:08,174 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-17 19:57:08,226 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-17 19:57:08,280 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-17 19:57:08,334 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-17 19:57:08,345 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-17 19:57:08,365 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-17 19:57:09,419 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-17 19:57:09,421 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 19:57:09,434 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-17 19:57:11,896 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 19:57:11,909 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-17 19:57:14,406 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 19:57:14,444 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-17 19:57:16,602 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 19:57:16,615 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-17 19:57:18,310 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 19:57:18,323 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-17 19:57:20,651 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-17 19:57:20,956 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 20 CPU cores. Let's make them scream!
2025-09-17 19:57:20,957 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-17 19:57:20,958 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-17 19:57:20,959] A new study created in memory with name: no-name-8677acd9-324c-4eec-9f6c-250735609543
2025-09-17 19:57:21,028 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                         ┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓                         
                         ┃ Best   ┃  Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃      Avg duration ┃ Objective ┃     Max Drawdown (Acct) ┃                         
                         ┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩                         
                         │ * Best │  2/100 │      3 │    1     0     2  33.3 │      0.02% │  -0.381 USDT   (-0.04%) │           8:00:00 │   0.00032 │  37.055 USDT    (3.71%) │                         
                         │ * Best │  9/100 │      8 │    4     0     4  50.0 │      1.87% │ 169.281 USDT   (16.93%) │          17:22:00 │  -0.09637 │  29.897 USDT    (2.99%) │                         
                         │ * Best │ 19/100 │     21 │    9     0    12  42.9 │     19.63% │ 199.639 USDT   (19.96%) │  54 days, 6:46:00 │  -0.12315 │ 120.893 USDT   (10.72%) │                         
                         │ Best   │ 33/100 │     16 │    7     0     9  43.8 │      1.12% │ 219.762 USDT   (21.98%) │          15:38:00 │  -0.13577 │  45.054 USDT    (4.51%) │                         
                         │ Best   │ 79/100 │     15 │    8     0     7  53.3 │     32.43% │ 275.067 USDT   (27.51%) │ 51 days, 14:20:00 │  -0.15643 │  65.850 USDT    (5.84%) │                         
                         └────────┴────────┴────────┴────────────────────────┴────────────┴─────────────────────────┴───────────────────┴───────────┴─────────────────────────┘                         
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100/100 100% • 0:02:08 • 0:00:00
2025-09-17 19:59:29,866 - freqtrade.optimize.hyperopt.hyperopt - INFO - 100 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-17_19-57-04.fthypt'.
2025-09-17 19:59:29,911 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

    79/100:     15 trades. 8/0/7 Wins/Draws/Losses. Avg profit  32.43%. Median profit  30.81%. Total profit 275.06715227 USDT (  27.51%). Avg duration 51 days, 14:20:00 min. Objective: -0.15643

{"params":{"confirmation_candle":false,"hammer_body_threshold":0.642,"hammer_head_threshold":0.265,"hammer_strength_threshold":0.009,"kinjun_threshold":6,"lookback_period_for_stoploss":0,"stoploss_margin":0.994,"take_profit_multiplier":2.5,"use_sell_signal_param":false,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231
```

## Backtesting Output
```
2025-09-17 19:59:33,840 - freqtrade - INFO - freqtrade 2025.7
2025-09-17 19:59:34,349 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-17 19:59:34,350 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-17 19:59:37,051 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-17 19:59:37,056 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-17 19:59:37,057 - freqtrade.loggers - INFO - Logfile configured
2025-09-17 19:59:37,057 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-17 19:59:37,058 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-17 19:59:37,058 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-17 19:59:37,059 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-17 19:59:37,059 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-17 19:59:37,072 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-17 19:59:37,073 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-17 19:59:37,074 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-17 19:59:37,075 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-17 19:59:37,076 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-17 19:59:37,076 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-17 19:59:37,079 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-17 19:59:37,102 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-17 19:59:37,104 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 19:59:37,108 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-17 19:59:37,110 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-17 19:59:37,111 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-17 19:59:37,159 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-17 19:59:40,109 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-17 19:59:40,160 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-17 19:59:40,160 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-17 19:59:40,162 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-17 19:59:40,162 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-17 19:59:40,163 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-17 19:59:40,163 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-17 19:59:40,164 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-17 19:59:40,165 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-17 19:59:40,165 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-17 19:59:40,166 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-17 19:59:40,166 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-17 19:59:40,167 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-17 19:59:40,167 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-17 19:59:40,168 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-17 19:59:40,169 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-17 19:59:40,169 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-17 19:59:40,170 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-17 19:59:40,171 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-17 19:59:40,171 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-17 19:59:40,172 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-17 19:59:40,172 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-17 19:59:40,173 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-17 19:59:40,174 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-17 19:59:40,174 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-17 19:59:40,175 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-17 19:59:40,175 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-17 19:59:40,176 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-17 19:59:40,176 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-17 19:59:40,177 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-17 19:59:40,177 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-17 19:59:40,178 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 19:59:40,186 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-17 19:59:40,228 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-17 19:59:40,279 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-17 19:59:40,360 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-17 19:59:40,433 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-17 19:59:40,495 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-17 19:59:40,555 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-17 19:59:40,591 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-17 19:59:40,688 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-17 19:59:41,023 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-17 19:59:41,320 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-17 19:59:41,656 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-17 19:59:41,991 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-17 19:59:44,114 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-17 19:59:44,115 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-17 19:59:44,116 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-17 19:59:44,116 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-17 19:59:44,117 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.642
2025-09-17 19:59:44,118 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.265
2025-09-17 19:59:44,118 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.009
2025-09-17 19:59:44,119 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 6
2025-09-17 19:59:44,119 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 0
2025-09-17 19:59:44,120 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.994
2025-09-17 19:59:44,120 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2.5
2025-09-17 19:59:44,121 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-17 19:59:44,121 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-17 19:59:44,122 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-17 19:59:44,125 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 19:59:44,140 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-17 19:59:47,712 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 19:59:47,725 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-17 19:59:51,265 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 19:59:51,279 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-17 19:59:54,701 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 19:59:54,714 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-17 19:59:58,153 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 19:59:58,166 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-17 20:00:01,580 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-17 20:09:28,156 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-17_20-09-28.meta.json"
Result for strategy IchimokuRebondStrategy
                                                BACKTESTING REPORT                                                 
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃       Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      4 │        31.65 │         104.298 │        10.43 │ 158 days, 10:59:00 │    3     0     1  75.0 │
│ LTC/USDT │      4 │        12.29 │          51.520 │         5.15 │   66 days, 3:46:00 │    2     0     2  50.0 │
│ BTC/USDT │      3 │        31.32 │          48.320 │         4.83 │ 246 days, 18:58:00 │    2     0     1  66.7 │
│ ETH/USDT │      2 │       -23.56 │         -32.925 │        -3.29 │  29 days, 14:35:00 │    0     0     2     0 │
│ XRP/USDT │      3 │       -16.42 │         -53.839 │        -5.38 │   55 days, 9:57:00 │    0     0     3     0 │
│    TOTAL │     16 │        10.83 │         117.374 │        11.74 │ 116 days, 12:26:00 │    7     0     9  43.8 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────────┴────────────────────────┘
                                              LEFT OPEN TRADES REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃       Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │        69.05 │          32.123 │         3.21 │  548 days, 4:00:00 │    1     0     0   100 │
│ BTC/USDT │      1 │        31.33 │          18.826 │         1.88 │  303 days, 2:00:00 │    1     0     0   100 │
│    TOTAL │      2 │        50.19 │          50.950 │         5.09 │ 425 days, 15:00:00 │    2     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────────┴────────────────────────┘
                                                   ENTER TAG STATS                                                   
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃       Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │      16 │        10.83 │         117.374 │        11.74 │ 116 days, 12:26:00 │    7     0     9  43.8 │
│     TOTAL │      16 │        10.83 │         117.374 │        11.74 │ 116 days, 12:26:00 │    7     0     9  43.8 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴────────────────────┴────────────────────────┘
                                                    EXIT REASON STATS                                                     
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃       Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2.5R │     5 │         48.3 │         224.478 │        22.45 │  113 days, 7:09:00 │    5     0     0   100 │
│       force_exit │     2 │        50.19 │          50.950 │         5.09 │ 425 days, 15:00:00 │    2     0     0   100 │
│        stop_loss │     9 │       -18.73 │        -158.054 │       -15.81 │  49 days, 14:48:00 │    0     0     9     0 │
│            TOTAL │    16 │        10.83 │         117.374 │        11.74 │ 116 days, 12:26:00 │    7     0     9  43.8 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────────┴────────────────────────┘
                                                            MIXED TAG STATS                                                            
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃       Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2.5R │      5 │         48.3 │         224.478 │        22.45 │  113 days, 7:09:00 │    5     0     0   100 │
│           │       force_exit │      2 │        50.19 │          50.950 │         5.09 │ 425 days, 15:00:00 │    2     0     0   100 │
│           │        stop_loss │      9 │       -18.73 │        -158.054 │       -15.81 │  49 days, 14:48:00 │    0     0     9     0 │
│     TOTAL │                  │     16 │        10.83 │         117.374 │        11.74 │ 116 days, 12:26:00 │    7     0     9  43.8 │
└───────────┴──────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────────┴────────────────────────┘
                            SUMMARY METRICS                            
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                               ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00                 │
│ Backtesting to                │ 2025-09-11 17:00:00                 │
│ Trading Mode                  │ Spot                                │
│ Max open trades               │ 3                                   │
│                               │                                     │
│ Total/Daily Avg Trades        │ 16 / 0.01                           │
│ Starting balance              │ 1000 USDT                           │
│ Final balance                 │ 1117.374 USDT                       │
│ Absolute profit               │ 117.374 USDT                        │
│ Total profit %                │ 11.74%                              │
│ CAGR %                        │ 3.05%                               │
│ Sortino                       │ 1.05                                │
│ Sharpe                        │ 0.06                                │
│ Calmar                        │ 1.81                                │
│ SQN                           │ 0.98                                │
│ Profit factor                 │ 1.74                                │
│ Expectancy (Ratio)            │ 7.34 (0.42)                         │
│ Avg. daily profit             │ 0.087 USDT                          │
│ Avg. stake amount             │ 98.149 USDT                         │
│ Total trade volume            │ 3264.67 USDT                        │
│                               │                                     │
│ Best Pair                     │ BNB/USDT 10.43%                     │
│ Worst Pair                    │ XRP/USDT -5.38%                     │
│ Best trade                    │ BTC/USDT 75.62%                     │
│ Worst trade                   │ ETH/USDT -33.31%                    │
│ Best day                      │ 50.95 USDT                          │
│ Worst day                     │ -37.642 USDT                        │
│ Days win/draw/lose            │ 6 / 1209 / 8                        │
│ Min/Max/Avg. Duration Winners │ 19d 06:05 / 548d 04:00 / 202d 12:49 │
│ Min/Max/Avg. Duration Losers  │ 4d 18:20 / 155d 02:05 / 49d 14:48   │
│ Max Consecutive Wins / Loss   │ 4 / 5                               │
│ Rejected Entry signals        │ 0                                   │
│ Entry/Exit Timeouts           │ 0 / 0                               │
│                               │                                     │
│ Min balance                   │ 908.076 USDT                        │
│ Max balance                   │ 1117.374 USDT                       │
│ Max % of account underwater   │ 9.19%                               │
│ Absolute Drawdown (Account)   │ 9.19%                               │
│ Absolute Drawdown             │ 91.924 USDT                         │
│ Drawdown high                 │ -16.742 USDT                        │
│ Drawdown low                  │ -91.924 USDT                        │
│ Drawdown Start                │ 2022-05-08 02:15:00                 │
│ Drawdown End                  │ 2023-01-02 01:05:00                 │
│ Market change                 │ 94.84%                              │
└───────────────────────────────┴─────────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃       Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     16 │        10.83 │         117.374 │        11.74 │ 116 days, 12:26:00 │    7     0     9  43.8 │ 91.924 USDT  9.19% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────────┴────────────────────────┴────────────────────┘

```
