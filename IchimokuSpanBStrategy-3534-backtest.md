# Freqtrade Backtest Log

**Strategy:** IchimokuSpanBStrategy  
**Random State:** 3534  
**Timestamp:** 2025-09-24 14:55:50

## Configuration
```json
{
  "strategy": "IchimokuSpanBStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 3534,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20200101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuSpanBStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20200101-20251231
```

## Backtesting Output
```
2025-09-24 12:27:40,281 - freqtrade - INFO - freqtrade 2025.8
2025-09-24 12:27:40,905 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-24 12:27:43,844 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-24 12:27:43,854 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-24 12:27:43,855 - freqtrade.loggers - INFO - Logfile configured
2025-09-24 12:27:43,856 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-24 12:27:43,857 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-24 12:27:43,858 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-24 12:27:43,860 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-24 12:27:43,861 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20200101-20251231 ...
2025-09-24 12:27:44,625 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-24 12:27:44,632 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-24 12:27:44,633 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-24 12:27:44,634 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-24 12:27:44,635 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-24 12:27:44,636 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20200101-20251231
2025-09-24 12:27:44,639 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-24 12:27:44,666 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-24 12:27:44,668 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 12:27:44,672 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-24 12:27:44,674 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-24 12:27:44,675 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-24 12:27:44,720 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-24 12:27:47,391 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-24 12:27:47,544 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuSpanBStrategy from '/freqtrade/user_data/strategies/IchimokuSpanBStrategy.py'...
2025-09-24 12:27:47,547 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2025-09-24 12:27:47,548 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-24 12:27:47,549 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-24 12:27:47,550 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-24 12:27:47,551 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-24 12:27:47,552 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-24 12:27:47,552 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-24 12:27:47,553 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-24 12:27:47,554 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-24 12:27:47,555 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-24 12:27:47,555 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-24 12:27:47,556 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-24 12:27:47,557 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: False
2025-09-24 12:27:47,557 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-24 12:27:47,558 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'market', 'stoploss_on_exchange': False}
2025-09-24 12:27:47,559 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-24 12:27:47,560 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-24 12:27:47,561 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-24 12:27:47,561 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 200
2025-09-24 12:27:47,562 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-24 12:27:47,563 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-24 12:27:47,564 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-24 12:27:47,565 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-24 12:27:47,565 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-24 12:27:47,566 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-24 12:27:47,567 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-24 12:27:47,568 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-24 12:27:47,570 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-24 12:27:47,571 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-24 12:27:47,571 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 12:27:47,600 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-24 12:27:47,647 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-24 12:27:47,893 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 12:27:47,999 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 12:27:48,093 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 12:27:48,186 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 12:27:48,328 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 12:27:48,403 - freqtrade.optimize.backtesting - INFO - Loading data from 2019-12-23 16:00:00 up to 2025-09-10 08:00:00 (2087 days).
2025-09-24 12:27:48,864 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 12:27:49,707 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 12:27:50,504 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 12:27:51,344 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 12:27:52,220 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 12:27:55,197 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-24 12:27:55,211 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-24 12:27:55,211 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuSpanBStrategy
2025-09-24 12:27:55,212 - freqtrade.strategy.hyper - INFO - No params for buy found, using default values.
2025-09-24 12:27:55,212 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): buy_rsi = 30
2025-09-24 12:27:55,213 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): exit_short_rsi = 30
2025-09-24 12:27:55,214 - freqtrade.strategy.hyper - INFO - No params for sell found, using default values.
2025-09-24 12:27:55,214 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): sell_rsi = 70
2025-09-24 12:27:55,215 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): short_rsi = 70
2025-09-24 12:27:55,215 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-24 12:27:55,365 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 12:55:43,249 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-24_12-55-43.meta.json"
Result for strategy IchimokuSpanBStrategy
                                              BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │    684 │         0.46 │        1765.081 │       176.51 │ 1 day, 1:28:00 │  128     0   556  18.7 │
│ XRP/USDT │    762 │         0.09 │         932.457 │        93.25 │       17:34:00 │  122     0   640  16.0 │
│ ETH/USDT │    889 │         0.25 │         584.250 │        58.43 │ 1 day, 0:20:00 │  173     0   716  19.5 │
│ BTC/USDT │    911 │         0.14 │        -120.735 │       -12.07 │ 1 day, 1:06:00 │  164     0   747  18.0 │
│ LTC/USDT │    832 │        -0.02 │       -1139.966 │       -114.0 │       21:20:00 │  145     0   687  17.4 │
│    TOTAL │   4078 │         0.17 │        2021.088 │       202.11 │       22:49:00 │  732     0  3346  17.9 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │      1 │         5.07 │          48.983 │          4.9 │ 2 days, 20:00:00 │    1     0     0   100 │
│ BNB/USDT │      1 │         3.08 │          30.297 │         3.03 │  4 days, 6:00:00 │    1     0     0   100 │
│ BTC/USDT │      1 │          0.7 │           6.732 │         0.67 │          4:00:00 │    1     0     0   100 │
│    TOTAL │      3 │         2.95 │          86.012 │          8.6 │ 2 days, 10:00:00 │    3     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                ENTER TAG STATS                                                
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │    4078 │         0.17 │        2021.088 │       202.11 │     22:49:00 │  732     0  3346  17.9 │
│     TOTAL │    4078 │         0.17 │        2021.088 │       202.11 │     22:49:00 │  732     0  3346  17.9 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ exit_signal │  4057 │         0.22 │        4078.734 │       407.87 │         22:48:00 │  729     0  3328  18.0 │
│  force_exit │     3 │         2.95 │          86.012 │          8.6 │ 2 days, 10:00:00 │    3     0     0   100 │
│   stop_loss │    18 │       -10.18 │       -2143.658 │      -214.37 │         21:00:00 │    0     0    18     0 │
│       TOTAL │  4078 │         0.17 │        2021.088 │       202.11 │         22:49:00 │  732     0  3346  17.9 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ exit_signal │   4057 │         0.22 │        4078.734 │       407.87 │         22:48:00 │  729     0  3328  18.0 │
│           │  force_exit │      3 │         2.95 │          86.012 │          8.6 │ 2 days, 10:00:00 │    3     0     0   100 │
│           │   stop_loss │     18 │       -10.18 │       -2143.658 │      -214.37 │         21:00:00 │    0     0    18     0 │
│     TOTAL │             │   4078 │         0.17 │        2021.088 │       202.11 │         22:49:00 │  732     0  3346  17.9 │
└───────────┴─────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2020-01-01 00:00:00             │
│ Backtesting to                │ 2025-09-10 08:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 4078 / 1.96                     │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 3021.088 USDT                   │
│ Absolute profit               │ 2021.088 USDT                   │
│ Total profit %                │ 202.11%                         │
│ CAGR %                        │ 21.42%                          │
│ Sortino                       │ 0.95                            │
│ Sharpe                        │ 0.26                            │
│ Calmar                        │ 2.43                            │
│ SQN                           │ 0.43                            │
│ Profit factor                 │ 1.04                            │
│ Expectancy (Ratio)            │ 0.50 (0.04)                     │
│ Avg. daily profit             │ 0.972 USDT                      │
│ Avg. stake amount             │ 1123.987 USDT                   │
│ Total trade volume            │ 9187611.875 USDT                │
│                               │                                 │
│ Best Pair                     │ BNB/USDT 176.51%                │
│ Worst Pair                    │ LTC/USDT -114.00%               │
│ Best trade                    │ BNB/USDT 187.14%                │
│ Worst trade                   │ LTC/USDT -10.18%                │
│ Best day                      │ 2647.905 USDT                   │
│ Worst day                     │ -774.329 USDT                   │
│ Days win/draw/lose            │ 356 / 763 / 961                 │
│ Min/Max/Avg. Duration Winners │ 0d 01:00 / 17d 10:00 / 3d 13:50 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:05 / 4d 16:00 / 0d 09:02  │
│ Max Consecutive Wins / Loss   │ 6 / 44                          │
│ Rejected Entry signals        │ 22236                           │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 989.308 USDT                    │
│ Max balance                   │ 9805.368 USDT                   │
│ Max % of account underwater   │ 76.29%                          │
│ Absolute drawdown             │ 7480.718 USDT (76.29%)          │
│ Drawdown duration             │ 1135 days 06:00:00              │
│ Profit at drawdown start      │ 8805.368 USDT                   │
│ Profit at drawdown end        │ 1324.65 USDT                    │
│ Drawdown start                │ 2021-09-07 01:00:00             │
│ Drawdown end                  │ 2024-10-16 07:00:00             │
│ Market change                 │ 2537.81%                        │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2020-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃              Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃              Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuSpanBStrategy │   4078 │         0.17 │        2021.088 │       202.11 │     22:49:00 │  732     0  3346  17.9 │ 7480.718 USDT  76.29% │
└───────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴───────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-24T14:55:50.063923",
  "strategy": "IchimokuSpanBStrategy",
  "random_state": 3534,
  "total_daily_avg_trades": "4078 / 1.96",
  "absolute_profit_usdt": 2021.088,
  "total_profit_pct": 202.11,
  "cagr_pct": 21.42,
  "sortino": 0.95,
  "sharpe": 0.26,
  "calmar": 2.43,
  "sqn": 0.43,
  "max_consecutive_wins_loss": "6 / 44",
  "min_balance_usdt": 989.308,
  "max_balance_usdt": 9805.368,
  "absolute_drawdown_pct": 76.29,
  "market_change_pct": 2537.81,
  "win_draw_loss_winpct": "732 0 3346 17.9"
}
```
