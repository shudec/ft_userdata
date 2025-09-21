# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 6738  
**Timestamp:** 2025-09-21 21:30:46

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell buy roi",
  "random_state": 6738,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20201231",
  "backtest_timerange": "20180101-20241231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20180101-20241231
```

## Backtesting Output
```
2025-09-21 19:23:07,277 - freqtrade - INFO - freqtrade 2025.7
2025-09-21 19:23:07,651 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-21 19:23:07,652 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-21 19:23:09,244 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-21 19:23:09,248 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-21 19:23:09,249 - freqtrade.loggers - INFO - Logfile configured
2025-09-21 19:23:09,249 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-21 19:23:09,250 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-21 19:23:09,251 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-21 19:23:09,251 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-21 19:23:09,251 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20241231 ...
2025-09-21 19:23:09,261 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-21 19:23:09,262 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-21 19:23:09,263 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-21 19:23:09,263 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-21 19:23:09,264 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-21 19:23:09,264 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20241231
2025-09-21 19:23:09,266 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-21 19:23:09,286 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-21 19:23:09,287 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 19:23:09,291 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-21 19:23:09,292 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-21 19:23:09,292 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-21 19:23:09,326 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-21 19:23:11,998 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-21 19:23:12,050 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-21 19:23:12,051 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-21 19:23:12,053 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-21 19:23:12,054 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-21 19:23:12,054 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-21 19:23:12,055 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-21 19:23:12,055 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-21 19:23:12,056 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.427, '474': 0.179, '800': 0.064, '1657': 0}
2025-09-21 19:23:12,056 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-21 19:23:12,057 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-21 19:23:12,057 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-21 19:23:12,058 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-21 19:23:12,058 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-21 19:23:12,059 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-21 19:23:12,059 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-21 19:23:12,059 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-21 19:23:12,060 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-21 19:23:12,060 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-21 19:23:12,061 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-21 19:23:12,061 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-21 19:23:12,062 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-21 19:23:12,062 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-21 19:23:12,063 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-21 19:23:12,063 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-21 19:23:12,064 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-21 19:23:12,064 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-21 19:23:12,065 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-21 19:23:12,065 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-21 19:23:12,066 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-21 19:23:12,066 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-21 19:23:12,067 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 19:23:12,074 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-21 19:23:12,112 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-21 19:23:12,379 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-21 19:23:12,468 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2024-12-31 00:00:00 (2556 days).
2025-09-21 19:23:13,794 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-21 19:23:16,922 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-21 19:23:16,927 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-21 19:23:16,927 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-21 19:23:16,928 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.2
2025-09-21 19:23:16,928 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 0
2025-09-21 19:23:16,929 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.926
2025-09-21 19:23:16,929 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.911
2025-09-21 19:23:16,930 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.031
2025-09-21 19:23:16,930 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-21 19:23:16,930 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-21 19:23:16,931 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.998
2025-09-21 19:23:16,931 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 2
2025-09-21 19:23:16,932 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-09-21 19:23:16,932 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-21 19:23:16,933 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-21 19:23:16,933 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-21 19:23:16,933 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-21 19:23:16,937 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2018-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:23:21,673 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2018-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:23:26,469 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2018-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:23:31,211 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2018-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:23:31,221 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-21 19:23:35,739 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2018-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:23:40,480 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2024-12-31 00:00:00 (2556 days).
2025-09-21 19:30:45,094 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-21_19-30-45.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │    675 │        -0.28 │         -78.962 │         -7.9 │      7:32:00 │  290    15   370  43.0 │
│ BNB/USDT │    565 │        -0.37 │        -139.779 │       -13.98 │      6:41:00 │  242     9   314  42.8 │
│ LTC/USDT │    578 │         -0.2 │        -143.972 │        -14.4 │      7:57:00 │  258    11   309  44.6 │
│ XRP/USDT │    504 │        -0.18 │        -175.445 │       -17.54 │      6:44:00 │  204    11   289  40.5 │
│ BTC/USDT │    832 │        -0.25 │        -456.294 │       -45.63 │      8:16:00 │  350    23   459  42.1 │
│    TOTAL │   3154 │        -0.26 │        -994.451 │       -99.45 │      7:31:00 │ 1344    69  1741  42.6 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                   ENTER TAG STATS                                                    
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│    hammer_rebond │       2 │         2.52 │          23.820 │         2.38 │      1:50:00 │    2     0     0   100 │
│ engulfing_rebond │    3152 │        -0.26 │       -1018.271 │      -101.83 │      7:31:00 │ 1342    69  1741  42.6 │
│            TOTAL │    3154 │        -0.26 │        -994.451 │       -99.45 │      7:31:00 │ 1344    69  1741  42.6 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │  1257 │          2.2 │        2676.665 │       267.67 │        6:19:00 │ 1257     0     0   100 │
│            roi │   156 │         0.84 │         120.681 │        12.07 │ 1 day, 6:47:00 │   87    69     0   100 │
│      stop_loss │  1741 │        -2.13 │       -3791.797 │      -379.18 │        6:19:00 │    0     0  1741     0 │
│          TOTAL │  3154 │        -0.26 │        -994.451 │       -99.45 │        7:31:00 │ 1344    69  1741  42.6 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                            MIXED TAG STATS                                                             
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │ take_profit_1R │   1255 │          2.2 │        2652.845 │       265.28 │        6:19:00 │ 1255     0     0   100 │
│ engulfing_rebond │            roi │    156 │         0.84 │         120.681 │        12.07 │ 1 day, 6:47:00 │   87    69     0   100 │
│    hammer_rebond │ take_profit_1R │      2 │         2.52 │          23.820 │         2.38 │        1:50:00 │    2     0     0   100 │
│ engulfing_rebond │      stop_loss │   1741 │        -2.13 │       -3791.797 │      -379.18 │        6:19:00 │    0     0  1741     0 │
│            TOTAL │                │   3154 │        -0.26 │        -994.451 │       -99.45 │        7:31:00 │ 1344    69  1741  42.6 │
└──────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2018-01-01 00:00:00            │
│ Backtesting to                │ 2024-12-31 00:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 3154 / 1.23                    │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 5.549 USDT                     │
│ Absolute profit               │ -994.451 USDT                  │
│ Total profit %                │ -99.45%                        │
│ CAGR %                        │ -52.37%                        │
│ Sortino                       │ -1.82                          │
│ Sharpe                        │ -1.60                          │
│ Calmar                        │ -0.75                          │
│ SQN                           │ -3.82                          │
│ Profit factor                 │ 0.74                           │
│ Expectancy (Ratio)            │ -0.32 (-0.17)                  │
│ Avg. daily profit             │ -0.389 USDT                    │
│ Avg. stake amount             │ 97.419 USDT                    │
│ Total trade volume            │ 614754.937 USDT                │
│                               │                                │
│ Best Pair                     │ ETH/USDT -7.90%                │
│ Worst Pair                    │ BTC/USDT -45.63%               │
│ Best trade                    │ XRP/USDT 16.49%                │
│ Worst trade                   │ BNB/USDT -38.37%               │
│ Best day                      │ 73.553 USDT                    │
│ Worst day                     │ -74.777 USDT                   │
│ Days win/draw/lose            │ 561 / 122 / 787                │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 1d 03:40 / 0d 07:37 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 8d 04:45 / 0d 06:19 │
│ Max Consecutive Wins / Loss   │ 11 / 12                        │
│ Rejected Entry signals        │ 716                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 5.549 USDT                     │
│ Max balance                   │ 1152.918 USDT                  │
│ Max % of account underwater   │ 99.52%                         │
│ Absolute Drawdown (Account)   │ 99.52%                         │
│ Absolute Drawdown             │ 1147.369 USDT                  │
│ Drawdown high                 │ 152.918 USDT                   │
│ Drawdown low                  │ -994.451 USDT                  │
│ Drawdown Start                │ 2018-01-13 17:20:00            │
│ Drawdown End                  │ 2022-01-09 10:15:00            │
│ Market change                 │ 1866.17%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2024-12-31 00:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                  
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃              Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │   3154 │        -0.26 │        -994.451 │       -99.45 │      7:31:00 │ 1344    69  1741  42.6 │ 1147.369 USDT  99.52% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴───────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-21T21:30:46.811265",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 6738,
  "total_daily_avg_trades": "3154 / 1.23",
  "absolute_profit_usdt": -994.451,
  "total_profit_pct": -99.45,
  "cagr_pct": -52.37,
  "sortino": -1.82,
  "sharpe": -1.6,
  "calmar": -0.75,
  "sqn": -3.82,
  "max_consecutive_wins_loss": "11 / 12",
  "min_balance_usdt": 5.549,
  "max_balance_usdt": 1152.918,
  "absolute_drawdown_pct": 99.52,
  "market_change_pct": 1866.17,
  "win_draw_loss_winpct": "1344 69 1741 42.6"
}
```
