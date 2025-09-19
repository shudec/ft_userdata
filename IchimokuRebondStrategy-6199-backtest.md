# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 6199  
**Timestamp:** 2025-09-19 17:49:17

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 6199,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231
```

## Backtesting Output
```
2025-09-19 15:45:34,889 - freqtrade - INFO - freqtrade 2025.8
2025-09-19 15:45:35,275 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-19 15:45:37,094 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-19 15:45:37,100 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-19 15:45:37,100 - freqtrade.loggers - INFO - Logfile configured
2025-09-19 15:45:37,101 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-19 15:45:37,101 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-19 15:45:37,102 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-19 15:45:37,102 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-19 15:45:37,103 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-19 15:45:37,404 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-19 15:45:37,406 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-19 15:45:37,406 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-19 15:45:37,407 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-19 15:45:37,407 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-19 15:45:37,408 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-19 15:45:37,409 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-19 15:45:37,420 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-19 15:45:37,421 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 15:45:37,423 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-19 15:45:37,424 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-19 15:45:37,425 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-19 15:45:37,445 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-19 15:45:41,325 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-19 15:45:41,420 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-19 15:45:41,422 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-19 15:45:41,427 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-19 15:45:41,428 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-19 15:45:41,428 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-19 15:45:41,428 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-19 15:45:41,429 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-19 15:45:41,430 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-19 15:45:41,430 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-19 15:45:41,430 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-19 15:45:41,431 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-19 15:45:41,432 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-19 15:45:41,433 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-19 15:45:41,433 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-19 15:45:41,434 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-19 15:45:41,435 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-19 15:45:41,436 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-19 15:45:41,436 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-19 15:45:41,436 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-19 15:45:41,437 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-19 15:45:41,437 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-19 15:45:41,438 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-19 15:45:41,438 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-19 15:45:41,438 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-19 15:45:41,439 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-19 15:45:41,439 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-19 15:45:41,440 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-19 15:45:41,440 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-19 15:45:41,441 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-19 15:45:41,441 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-19 15:45:41,442 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 15:45:41,465 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-19 15:45:41,496 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-19 15:45:41,557 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 15:45:41,628 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 15:45:41,685 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 15:45:41,740 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 15:45:41,800 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 15:45:41,827 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-19 15:45:42,101 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 15:45:42,581 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 15:45:43,007 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 15:45:43,443 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 15:45:43,863 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 15:45:45,350 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-19 15:45:45,356 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-19 15:45:45,357 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-19 15:45:45,357 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-19 15:45:45,358 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-19 15:45:45,358 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 1
2025-09-19 15:45:45,359 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.5
2025-09-19 15:45:45,359 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-09-19 15:45:45,360 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.025
2025-09-19 15:45:45,361 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-19 15:45:45,361 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.001
2025-09-19 15:45:45,363 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-19 15:45:45,363 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 2
2025-09-19 15:45:45,365 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-09-19 15:45:45,365 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-19 15:45:45,366 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-19 15:45:45,366 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-19 15:45:45,367 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-19 15:45:45,370 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 15:45:45,395 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 15:45:48,423 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 15:45:48,440 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 15:45:52,395 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 15:45:52,416 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 15:45:56,277 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 15:45:56,295 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 15:45:59,268 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 15:45:59,286 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 15:46:02,489 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-19 15:49:15,364 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-19_15-49-15.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │    380 │        -0.22 │        -155.694 │       -15.57 │      3:50:00 │   96     0   284  25.3 │
│ LTC/USDT │    412 │        -0.24 │        -173.165 │       -17.32 │      3:55:00 │  114     0   298  27.7 │
│ BNB/USDT │    516 │        -0.22 │        -181.260 │       -18.13 │      4:12:00 │  127     0   389  24.6 │
│ ETH/USDT │    451 │        -0.16 │        -227.109 │       -22.71 │      4:03:00 │  114     0   337  25.3 │
│ BTC/USDT │    612 │         -0.2 │        -250.384 │       -25.04 │      5:01:00 │  134     0   478  21.9 │
│    TOTAL │   2371 │        -0.21 │        -987.612 │       -98.76 │      4:17:00 │  585     0  1786  24.7 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                           LEFT OPEN TRADES REPORT                                           
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         0.05 │           0.006 │          0.0 │      5:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         0.05 │           0.006 │          0.0 │      5:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                ENTER TAG STATS                                                
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │    2371 │        -0.21 │        -987.612 │       -98.76 │      4:17:00 │  585     0  1786  24.7 │
│     TOTAL │    2371 │        -0.21 │        -987.612 │       -98.76 │      4:17:00 │  585     0  1786  24.7 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │   527 │         1.51 │        1379.874 │       137.99 │      5:10:00 │  527     0     0   100 │
│     force_exit │     1 │         0.05 │           0.006 │          0.0 │      5:00:00 │    1     0     0   100 │
│    exit_signal │   698 │        -0.53 │        -610.425 │       -61.04 │      6:44:00 │   57     0   641   8.2 │
│      stop_loss │  1145 │         -0.8 │       -1757.066 │      -175.71 │      2:22:00 │    0     0  1145     0 │
│          TOTAL │  2371 │        -0.21 │        -987.612 │       -98.76 │      4:17:00 │  585     0  1786  24.7 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │    527 │         1.51 │        1379.874 │       137.99 │      5:10:00 │  527     0     0   100 │
│           │     force_exit │      1 │         0.05 │           0.006 │          0.0 │      5:00:00 │    1     0     0   100 │
│           │    exit_signal │    698 │        -0.53 │        -610.425 │       -61.04 │      6:44:00 │   57     0   641   8.2 │
│           │      stop_loss │   1145 │         -0.8 │       -1757.066 │      -175.71 │      2:22:00 │    0     0  1145     0 │
│     TOTAL │                │   2371 │        -0.21 │        -987.612 │       -98.76 │      4:17:00 │  585     0  1786  24.7 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 2371 / 1.76                    │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 12.388 USDT                    │
│ Absolute profit               │ -987.612 USDT                  │
│ Total profit %                │ -98.76%                        │
│ CAGR %                        │ -69.55%                        │
│ Sortino                       │ -6.17                          │
│ Sharpe                        │ -4.09                          │
│ Calmar                        │ -1.42                          │
│ SQN                           │ -5.93                          │
│ Profit factor                 │ 0.59                           │
│ Expectancy (Ratio)            │ -0.42 (-0.31)                  │
│ Avg. daily profit             │ -0.733 USDT                    │
│ Avg. stake amount             │ 170.033 USDT                   │
│ Total trade volume            │ 806919.109 USDT                │
│                               │                                │
│ Best Pair                     │ XRP/USDT -15.57%               │
│ Worst Pair                    │ BTC/USDT -25.04%               │
│ Best trade                    │ ETH/USDT 7.95%                 │
│ Worst trade                   │ XRP/USDT -4.32%                │
│ Best day                      │ 48.782 USDT                    │
│ Worst day                     │ -32.419 USDT                   │
│ Days win/draw/lose            │ 259 / 446 / 640                │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 2d 03:00 / 0d 06:31 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 1d 10:00 / 0d 03:33 │
│ Max Consecutive Wins / Loss   │ 6 / 24                         │
│ Rejected Entry signals        │ 60                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 12.376 USDT                    │
│ Max balance                   │ 996.575 USDT                   │
│ Max % of account underwater   │ 98.76%                         │
│ Absolute drawdown             │ 987.624 USDT (98.76%)          │
│ Drawdown duration             │ 1339 days 16:00:00             │
│ Profit at drawdown start      │ -3.425 USDT                    │
│ Profit at drawdown end        │ -987.624 USDT                  │
│ Drawdown start                │ 2022-01-05 06:00:00            │
│ Drawdown end                  │ 2025-09-05 22:00:00            │
│ Market change                 │ 91.49%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │   2371 │        -0.21 │        -987.612 │       -98.76 │      4:17:00 │  585     0  1786  24.7 │ 987.624 USDT  98.76% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-19T17:49:17.039958",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 6199,
  "total_daily_avg_trades": "2371 / 1.76",
  "absolute_profit_usdt": -987.612,
  "total_profit_pct": -98.76,
  "cagr_pct": -69.55,
  "sortino": -6.17,
  "sharpe": -4.09,
  "calmar": -1.42,
  "sqn": -5.93,
  "max_consecutive_wins_loss": "6 / 24",
  "min_balance_usdt": 12.376,
  "max_balance_usdt": 996.575,
  "market_change_pct": 91.49,
  "win_draw_loss_winpct": "585 0 1786 24.7"
}
```
