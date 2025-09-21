# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 4672  
**Timestamp:** 2025-09-19 22:26:43

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell buy roi",
  "random_state": 4672,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20201231",
  "backtest_timerange": "20221101-20241231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20221101-20241231
```

## Backtesting Output
```
2025-09-19 20:26:22,934 - freqtrade - INFO - freqtrade 2025.7
2025-09-19 20:26:23,309 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-19 20:26:23,309 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-19 20:26:24,930 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-19 20:26:24,933 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-19 20:26:24,933 - freqtrade.loggers - INFO - Logfile configured
2025-09-19 20:26:24,934 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-19 20:26:24,934 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-19 20:26:24,935 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-19 20:26:24,935 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-19 20:26:24,935 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20221101-20241231 ...
2025-09-19 20:26:24,943 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-19 20:26:24,945 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-19 20:26:24,945 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-19 20:26:24,946 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-19 20:26:24,947 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-19 20:26:24,947 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20221101-20241231
2025-09-19 20:26:24,949 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-19 20:26:24,970 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-19 20:26:24,971 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 20:26:24,976 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-19 20:26:24,977 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-19 20:26:24,978 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-19 20:26:25,018 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-19 20:26:27,464 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-19 20:26:27,505 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-19 20:26:27,506 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-19 20:26:27,507 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-19 20:26:27,508 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-19 20:26:27,508 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-19 20:26:27,509 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-19 20:26:27,510 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-19 20:26:27,510 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.49, '456': 0.214, '795': 0.085, '1564': 0}
2025-09-19 20:26:27,511 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-19 20:26:27,511 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-19 20:26:27,511 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-19 20:26:27,512 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-19 20:26:27,512 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-19 20:26:27,513 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-19 20:26:27,513 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-19 20:26:27,513 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-19 20:26:27,514 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-19 20:26:27,514 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-19 20:26:27,515 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-19 20:26:27,515 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-19 20:26:27,515 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-19 20:26:27,516 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-19 20:26:27,516 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-19 20:26:27,517 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-19 20:26:27,517 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-19 20:26:27,517 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-19 20:26:27,518 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-19 20:26:27,518 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-19 20:26:27,519 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-19 20:26:27,519 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-19 20:26:27,520 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 20:26:27,546 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-19 20:26:27,580 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-19 20:26:27,784 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-11-01 00:00:00 up to 2024-12-31 00:00:00 (791 days).
2025-09-19 20:26:29,408 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-19 20:26:29,412 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-19 20:26:29,413 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-19 20:26:29,413 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.1
2025-09-19 20:26:29,414 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 16
2025-09-19 20:26:29,414 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.523
2025-09-19 20:26:29,415 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.85
2025-09-19 20:26:29,415 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.022
2025-09-19 20:26:29,415 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.0
2025-09-19 20:26:29,416 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.001
2025-09-19 20:26:29,416 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-19 20:26:29,417 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 6
2025-09-19 20:26:29,417 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.992
2025-09-19 20:26:29,417 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-19 20:26:29,418 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-19 20:26:29,418 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-19 20:26:29,419 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-19 20:26:29,420 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-11-01 00:00:00 to 2024-12-31 00:00:00
2025-09-19 20:26:31,003 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-11-01 00:00:00 to 2024-12-31 00:00:00
2025-09-19 20:26:32,540 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-11-01 00:00:00 to 2024-12-31 00:00:00
2025-09-19 20:26:34,111 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-11-01 00:00:00 to 2024-12-31 00:00:00
2025-09-19 20:26:35,651 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-11-01 00:00:00 to 2024-12-31 00:00:00
2025-09-19 20:26:37,212 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-11-01 00:00:00 up to 2024-12-31 00:00:00 (791 days).
2025-09-19 20:26:41,917 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-19_20-26-41.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │      6 │         0.89 │          36.777 │         3.68 │      7:43:00 │    3     0     3  50.0 │
│ LTC/USDT │      3 │         1.47 │          10.524 │         1.05 │     12:10:00 │    1     0     2  33.3 │
│ BNB/USDT │      6 │         0.06 │           2.612 │         0.26 │      8:25:00 │    3     0     3  50.0 │
│ BTC/USDT │      7 │        -0.26 │         -14.195 │        -1.42 │     13:34:00 │    2     0     5  28.6 │
│ ETH/USDT │      9 │        -0.26 │         -23.249 │        -2.32 │      9:24:00 │    2     0     7  22.2 │
│    TOTAL │     31 │         0.19 │          12.468 │         1.25 │     10:05:00 │   11     0    20  35.5 │
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
│     OTHER │      31 │         0.19 │          12.468 │         1.25 │     10:05:00 │   11     0    20  35.5 │
│     TOTAL │      31 │         0.19 │          12.468 │         1.25 │     10:05:00 │   11     0    20  35.5 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │     8 │         3.03 │         185.992 │         18.6 │     10:13:00 │    8     0     0   100 │
│      exit_signal │    16 │        -0.54 │         -80.357 │        -8.04 │     11:52:00 │    3     0    13  18.8 │
│        stop_loss │     7 │        -1.37 │         -93.167 │        -9.32 │      5:52:00 │    0     0     7     0 │
│            TOTAL │    31 │         0.19 │          12.468 │         1.25 │     10:05:00 │   11     0    20  35.5 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1.5R │      8 │         3.03 │         185.992 │         18.6 │     10:13:00 │    8     0     0   100 │
│           │      exit_signal │     16 │        -0.54 │         -80.357 │        -8.04 │     11:52:00 │    3     0    13  18.8 │
│           │        stop_loss │      7 │        -1.37 │         -93.167 │        -9.32 │      5:52:00 │    0     0     7     0 │
│     TOTAL │                  │     31 │         0.19 │          12.468 │         1.25 │     10:05:00 │   11     0    20  35.5 │
└───────────┴──────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-11-01 00:00:00            │
│ Backtesting to                │ 2024-12-31 00:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 31 / 0.04                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1012.468 USDT                  │
│ Absolute profit               │ 12.468 USDT                    │
│ Total profit %                │ 1.25%                          │
│ CAGR %                        │ 0.57%                          │
│ Sortino                       │ 0.08                           │
│ Sharpe                        │ 0.02                           │
│ Calmar                        │ 0.29                           │
│ SQN                           │ 0.15                           │
│ Profit factor                 │ 1.07                           │
│ Expectancy (Ratio)            │ 0.40 (0.05)                    │
│ Avg. daily profit             │ 0.016 USDT                     │
│ Avg. stake amount             │ 915.066 USDT                   │
│ Total trade volume            │ 56860.191 USDT                 │
│                               │                                │
│ Best Pair                     │ XRP/USDT 3.68%                 │
│ Worst Pair                    │ ETH/USDT -2.32%                │
│ Best trade                    │ LTC/USDT 6.72%                 │
│ Worst trade                   │ ETH/USDT -1.75%                │
│ Best day                      │ 33.486 USDT                    │
│ Worst day                     │ -16.815 USDT                   │
│ Days win/draw/lose            │ 11 / 703 / 20                  │
│ Min/Max/Avg. Duration Winners │ 0d 02:45 / 1d 02:00 / 0d 14:15 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 0d 20:00 / 0d 07:48 │
│ Max Consecutive Wins / Loss   │ 3 / 12                         │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 924.855 USDT                   │
│ Max balance                   │ 1033.486 USDT                  │
│ Max % of account underwater   │ 10.51%                         │
│ Absolute Drawdown (Account)   │ 10.51%                         │
│ Absolute Drawdown             │ 108.631 USDT                   │
│ Drawdown high                 │ 33.486 USDT                    │
│ Drawdown low                  │ -75.145 USDT                   │
│ Drawdown Start                │ 2022-11-05 11:40:00            │
│ Drawdown End                  │ 2023-09-06 06:00:00            │
│ Market change                 │ 199.97%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-11-01 00:00:00 -> 2024-12-31 00:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     31 │         0.19 │          12.468 │         1.25 │     10:05:00 │   11     0    20  35.5 │ 108.631 USDT  10.51% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-19T22:26:43.015421",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 4672,
  "total_daily_avg_trades": "31 / 0.04",
  "absolute_profit_usdt": 12.468,
  "total_profit_pct": 1.25,
  "cagr_pct": 0.57,
  "sortino": 0.08,
  "sharpe": 0.02,
  "calmar": 0.29,
  "sqn": 0.15,
  "max_consecutive_wins_loss": "3 / 12",
  "min_balance_usdt": 924.855,
  "max_balance_usdt": 1033.486,
  "absolute_drawdown_pct": 10.51,
  "market_change_pct": 199.97,
  "win_draw_loss_winpct": "11 0 20 35.5"
}
```
