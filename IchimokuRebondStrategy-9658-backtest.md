# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 9658  
**Timestamp:** 2025-09-21 21:36:27

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell buy roi",
  "random_state": 9658,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20201231",
  "backtest_timerange": "20210101-20241231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20210101-20241231
```

## Backtesting Output
```
2025-09-21 19:32:59,317 - freqtrade - INFO - freqtrade 2025.7
2025-09-21 19:32:59,650 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-21 19:32:59,651 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-21 19:33:01,085 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-21 19:33:01,088 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-21 19:33:01,089 - freqtrade.loggers - INFO - Logfile configured
2025-09-21 19:33:01,089 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-21 19:33:01,090 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-21 19:33:01,090 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-21 19:33:01,090 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-21 19:33:01,091 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20210101-20241231 ...
2025-09-21 19:33:01,099 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-21 19:33:01,100 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-21 19:33:01,100 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-21 19:33:01,101 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-21 19:33:01,101 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-21 19:33:01,102 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20210101-20241231
2025-09-21 19:33:01,103 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-21 19:33:01,123 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-21 19:33:01,124 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 19:33:01,127 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-21 19:33:01,129 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-21 19:33:01,129 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-21 19:33:01,163 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-21 19:33:03,814 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-21 19:33:03,850 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-21 19:33:03,851 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-21 19:33:03,852 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-21 19:33:03,852 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-21 19:33:03,853 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-21 19:33:03,853 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-21 19:33:03,854 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-21 19:33:03,854 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.427, '474': 0.179, '800': 0.064, '1657': 0}
2025-09-21 19:33:03,854 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-21 19:33:03,855 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-21 19:33:03,855 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-21 19:33:03,856 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-21 19:33:03,856 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-21 19:33:03,856 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-21 19:33:03,857 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-21 19:33:03,857 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-21 19:33:03,857 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-21 19:33:03,858 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-21 19:33:03,858 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-21 19:33:03,858 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-21 19:33:03,859 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-21 19:33:03,859 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-21 19:33:03,859 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-21 19:33:03,860 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-21 19:33:03,860 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-21 19:33:03,860 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-21 19:33:03,861 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-21 19:33:03,861 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-21 19:33:03,862 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-21 19:33:03,862 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-21 19:33:03,862 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 19:33:03,868 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-21 19:33:03,899 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-21 19:33:04,102 - freqtrade.optimize.backtesting - INFO - Loading data from 2021-01-01 00:00:00 up to 2024-12-31 00:00:00 (1460 days).
2025-09-21 19:33:06,428 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-21 19:33:06,431 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-21 19:33:06,431 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-21 19:33:06,432 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.2
2025-09-21 19:33:06,432 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 0
2025-09-21 19:33:06,433 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.926
2025-09-21 19:33:06,433 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.911
2025-09-21 19:33:06,433 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.031
2025-09-21 19:33:06,433 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-21 19:33:06,434 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-21 19:33:06,434 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.998
2025-09-21 19:33:06,435 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 2
2025-09-21 19:33:06,435 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-09-21 19:33:06,435 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-21 19:33:06,436 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-21 19:33:06,436 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-21 19:33:06,436 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-21 19:33:06,438 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:33:09,227 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:33:11,888 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:33:14,573 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:33:17,268 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:33:19,973 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2021-01-01 00:00:00 up to 2024-12-31 00:00:00 (1460 days).
2025-09-21 19:36:25,737 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-21_19-36-25.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │    396 │        -0.02 │         -44.303 │        -4.43 │      7:24:00 │  182     7   207  46.0 │
│ BNB/USDT │    353 │        -0.21 │         -77.243 │        -7.72 │      6:36:00 │  145     7   201  41.1 │
│ XRP/USDT │    386 │        -0.16 │        -215.315 │       -21.53 │      6:04:00 │  158     6   222  40.9 │
│ LTC/USDT │    411 │        -0.41 │        -289.172 │       -28.92 │      7:08:00 │  171     6   234  41.6 │
│ BTC/USDT │    437 │         -0.2 │        -323.083 │       -32.31 │      7:39:00 │  191     6   240  43.7 │
│    TOTAL │   1983 │         -0.2 │        -949.115 │       -94.91 │      7:00:00 │  847    32  1104  42.7 │
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
│ engulfing_rebond │    1983 │         -0.2 │        -949.115 │       -94.91 │      7:00:00 │  847    32  1104  42.7 │
│            TOTAL │    1983 │         -0.2 │        -949.115 │       -94.91 │      7:00:00 │  847    32  1104  42.7 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │   793 │         1.82 │        5075.092 │       507.51 │        5:53:00 │  793     0     0   100 │
│            roi │    86 │         0.73 │         163.007 │         16.3 │ 1 day, 4:52:00 │   54    32     0   100 │
│      stop_loss │  1104 │        -1.73 │       -6187.215 │      -618.72 │        6:06:00 │    0     0  1104     0 │
│          TOTAL │  1983 │         -0.2 │        -949.115 │       -94.91 │        7:00:00 │  847    32  1104  42.7 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                            MIXED TAG STATS                                                             
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │ take_profit_1R │    793 │         1.82 │        5075.092 │       507.51 │        5:53:00 │  793     0     0   100 │
│ engulfing_rebond │            roi │     86 │         0.73 │         163.007 │         16.3 │ 1 day, 4:52:00 │   54    32     0   100 │
│ engulfing_rebond │      stop_loss │   1104 │        -1.73 │       -6187.215 │      -618.72 │        6:06:00 │    0     0  1104     0 │
│            TOTAL │                │   1983 │         -0.2 │        -949.115 │       -94.91 │        7:00:00 │  847    32  1104  42.7 │
└──────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2021-01-01 00:00:00            │
│ Backtesting to                │ 2024-12-31 00:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 1983 / 1.36                    │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 50.885 USDT                    │
│ Absolute profit               │ -949.115 USDT                  │
│ Total profit %                │ -94.91%                        │
│ CAGR %                        │ -52.51%                        │
│ Sortino                       │ -2.13                          │
│ Sharpe                        │ -1.48                          │
│ Calmar                        │ -1.30                          │
│ SQN                           │ -2.55                          │
│ Profit factor                 │ 0.85                           │
│ Expectancy (Ratio)            │ -0.48 (-0.10)                  │
│ Avg. daily profit             │ -0.65 USDT                     │
│ Avg. stake amount             │ 329.878 USDT                   │
│ Total trade volume            │ 1309965.657 USDT               │
│                               │                                │
│ Best Pair                     │ ETH/USDT -4.43%                │
│ Worst Pair                    │ BTC/USDT -32.31%               │
│ Best trade                    │ XRP/USDT 8.14%                 │
│ Worst trade                   │ XRP/USDT -10.99%               │
│ Best day                      │ 68.208 USDT                    │
│ Worst day                     │ -83.32 USDT                    │
│ Days win/draw/lose            │ 388 / 514 / 555                │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 1d 03:40 / 0d 07:15 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 4d 09:20 / 0d 06:06 │
│ Max Consecutive Wins / Loss   │ 9 / 11                         │
│ Rejected Entry signals        │ 424                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 50.885 USDT                    │
│ Max balance                   │ 1094.983 USDT                  │
│ Max % of account underwater   │ 95.35%                         │
│ Absolute Drawdown (Account)   │ 95.35%                         │
│ Absolute Drawdown             │ 1044.099 USDT                  │
│ Drawdown high                 │ 94.983 USDT                    │
│ Drawdown low                  │ -949.115 USDT                  │
│ Drawdown Start                │ 2021-05-05 19:55:00            │
│ Drawdown End                  │ 2024-12-30 13:10:00            │
│ Market change                 │ 630.36%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2021-01-01 00:00:00 -> 2024-12-31 00:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                  
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃              Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │   1983 │        -0.20 │        -949.115 │       -94.91 │      7:00:00 │  847    32  1104  42.7 │ 1044.099 USDT  95.35% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴───────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-21T21:36:27.367547",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 9658,
  "total_daily_avg_trades": "1983 / 1.36",
  "absolute_profit_usdt": -949.115,
  "total_profit_pct": -94.91,
  "cagr_pct": -52.51,
  "sortino": -2.13,
  "sharpe": -1.48,
  "calmar": -1.3,
  "sqn": -2.55,
  "max_consecutive_wins_loss": "9 / 11",
  "min_balance_usdt": 50.885,
  "max_balance_usdt": 1094.983,
  "absolute_drawdown_pct": 95.35,
  "market_change_pct": 630.36,
  "win_draw_loss_winpct": "847 32 1104 42.7"
}
```
