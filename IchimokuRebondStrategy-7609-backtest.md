# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 7609  
**Timestamp:** 2025-09-20 22:31:19

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell buy roi",
  "random_state": 7609,
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
2025-09-20 20:31:00,950 - freqtrade - INFO - freqtrade 2025.7
2025-09-20 20:31:01,337 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-20 20:31:01,338 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-20 20:31:02,977 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-20 20:31:02,980 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-20 20:31:02,980 - freqtrade.loggers - INFO - Logfile configured
2025-09-20 20:31:02,981 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-20 20:31:02,981 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-20 20:31:02,982 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-20 20:31:02,982 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-20 20:31:02,982 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20221101-20241231 ...
2025-09-20 20:31:02,991 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-20 20:31:02,992 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-20 20:31:02,992 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-20 20:31:02,993 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-20 20:31:02,994 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-20 20:31:02,994 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20221101-20241231
2025-09-20 20:31:02,996 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-20 20:31:03,017 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-20 20:31:03,018 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-20 20:31:03,022 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-20 20:31:03,023 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-20 20:31:03,024 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-20 20:31:03,064 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-20 20:31:05,435 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-20 20:31:05,479 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-20 20:31:05,480 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-20 20:31:05,481 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-20 20:31:05,481 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-20 20:31:05,482 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-20 20:31:05,482 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-20 20:31:05,483 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-20 20:31:05,483 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.326, '432': 0.142, '803': 0.072, '1879': 0}
2025-09-20 20:31:05,483 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-20 20:31:05,484 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-20 20:31:05,484 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-20 20:31:05,484 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-20 20:31:05,485 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-20 20:31:05,485 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-20 20:31:05,485 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-20 20:31:05,486 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-20 20:31:05,486 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-20 20:31:05,487 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-20 20:31:05,487 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-20 20:31:05,487 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-20 20:31:05,488 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-20 20:31:05,488 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-20 20:31:05,488 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-20 20:31:05,489 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-20 20:31:05,489 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-20 20:31:05,490 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-20 20:31:05,490 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-20 20:31:05,490 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-20 20:31:05,491 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-20 20:31:05,491 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-20 20:31:05,492 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-20 20:31:05,498 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-20 20:31:05,529 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-20 20:31:05,725 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-11-01 00:00:00 up to 2024-12-31 00:00:00 (791 days).
2025-09-20 20:31:07,369 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-20 20:31:07,374 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-20 20:31:07,374 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-20 20:31:07,375 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-20 20:31:07,375 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 20
2025-09-20 20:31:07,376 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.996
2025-09-20 20:31:07,376 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.923
2025-09-20 20:31:07,377 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.001
2025-09-20 20:31:07,377 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-20 20:31:07,378 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.0
2025-09-20 20:31:07,378 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.998
2025-09-20 20:31:07,379 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 9
2025-09-20 20:31:07,379 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.991
2025-09-20 20:31:07,380 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2.5
2025-09-20 20:31:07,380 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-20 20:31:07,380 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-20 20:31:07,381 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-20 20:31:07,383 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-11-01 00:00:00 to 2024-12-31 00:00:00
2025-09-20 20:31:08,976 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-11-01 00:00:00 to 2024-12-31 00:00:00
2025-09-20 20:31:10,570 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-11-01 00:00:00 to 2024-12-31 00:00:00
2025-09-20 20:31:12,128 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-11-01 00:00:00 to 2024-12-31 00:00:00
2025-09-20 20:31:13,699 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-11-01 00:00:00 to 2024-12-31 00:00:00
2025-09-20 20:31:15,298 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-11-01 00:00:00 up to 2024-12-31 00:00:00 (791 days).
2025-09-20 20:31:18,228 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-20_20-31-18.meta.json"
Result for strategy IchimokuRebondStrategy
                                              BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │      2 │         0.94 │          17.910 │         1.79 │ 1 day, 7:20:00 │    2     0     0   100 │
│ XRP/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│ BNB/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│ LTC/USDT │      2 │        -1.62 │         -31.784 │        -3.18 │        4:25:00 │    0     0     2     0 │
│ ETH/USDT │      3 │        -1.38 │         -39.808 │        -3.98 │        8:40:00 │    0     0     3     0 │
│    TOTAL │      7 │        -0.79 │         -53.683 │        -5.37 │       13:56:00 │    2     0     5  28.6 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                  ENTER TAG STATS                                                  
┏━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ hammer_rebond │       7 │        -0.79 │         -53.683 │        -5.37 │     13:56:00 │    2     0     5  28.6 │
│         TOTAL │       7 │        -0.79 │         -53.683 │        -5.37 │     13:56:00 │    2     0     5  28.6 │
└───────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│         roi │     2 │         0.94 │          17.910 │         1.79 │ 1 day, 7:20:00 │    2     0     0   100 │
│   stop_loss │     5 │        -1.48 │         -71.592 │        -7.16 │        6:58:00 │    0     0     5     0 │
│       TOTAL │     7 │        -0.79 │         -53.683 │        -5.37 │       13:56:00 │    2     0     5  28.6 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                          
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ hammer_rebond │         roi │      2 │         0.94 │          17.910 │         1.79 │ 1 day, 7:20:00 │    2     0     0   100 │
│ hammer_rebond │   stop_loss │      5 │        -1.48 │         -71.592 │        -7.16 │        6:58:00 │    0     0     5     0 │
│         TOTAL │             │      7 │        -0.79 │         -53.683 │        -5.37 │       13:56:00 │    2     0     5  28.6 │
└───────────────┴─────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-11-01 00:00:00            │
│ Backtesting to                │ 2024-12-31 00:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 7 / 0.01                       │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 946.317 USDT                   │
│ Absolute profit               │ -53.683 USDT                   │
│ Total profit %                │ -5.37%                         │
│ CAGR %                        │ -2.51%                         │
│ Sortino                       │ -0.47                          │
│ Sharpe                        │ -0.12                          │
│ Calmar                        │ -2.42                          │
│ SQN                           │ -1.72                          │
│ Profit factor                 │ 0.25                           │
│ Expectancy (Ratio)            │ -7.67 (-0.54)                  │
│ Avg. daily profit             │ -0.068 USDT                    │
│ Avg. stake amount             │ 961.228 USDT                   │
│ Total trade volume            │ 13430.343 USDT                 │
│                               │                                │
│ Best Pair                     │ BTC/USDT 1.79%                 │
│ Worst Pair                    │ ETH/USDT -3.98%                │
│ Best trade                    │ BTC/USDT 1.31%                 │
│ Worst trade                   │ LTC/USDT -1.90%                │
│ Best day                      │ 12.403 USDT                    │
│ Worst day                     │ -18.869 USDT                   │
│ Days win/draw/lose            │ 2 / 441 / 5                    │
│ Min/Max/Avg. Duration Winners │ 1d 07:20 / 1d 07:20 / 1d 07:20 │
│ Min/Max/Avg. Duration Losers  │ 0d 02:30 / 0d 11:40 / 0d 06:58 │
│ Max Consecutive Wins / Loss   │ 2 / 3                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 946.317 USDT                   │
│ Max balance                   │ 981.131 USDT                   │
│ Max % of account underwater   │ 5.37%                          │
│ Absolute Drawdown (Account)   │ 5.37%                          │
│ Absolute Drawdown             │ 53.683 USDT                    │
│ Drawdown high                 │ -18.869 USDT                   │
│ Drawdown low                  │ -53.683 USDT                   │
│ Drawdown Start                │ 2022-11-30 17:20:00            │
│ Drawdown End                  │ 2024-02-20 09:45:00            │
│ Market change                 │ 199.97%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-11-01 00:00:00 -> 2024-12-31 00:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │      7 │        -0.79 │         -53.683 │        -5.37 │     13:56:00 │    2     0     5  28.6 │ 53.683 USDT  5.37% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-20T22:31:19.338577",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 7609,
  "total_daily_avg_trades": "7 / 0.01",
  "absolute_profit_usdt": -53.683,
  "total_profit_pct": -5.37,
  "cagr_pct": -2.51,
  "sortino": -0.47,
  "sharpe": -0.12,
  "calmar": -2.42,
  "sqn": -1.72,
  "max_consecutive_wins_loss": "2 / 3",
  "min_balance_usdt": 946.317,
  "max_balance_usdt": 981.131,
  "absolute_drawdown_pct": 5.37,
  "market_change_pct": 199.97,
  "win_draw_loss_winpct": "2 0 5 28.6"
}
```
