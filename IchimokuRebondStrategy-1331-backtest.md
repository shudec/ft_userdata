# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 1331  
**Timestamp:** 2025-09-21 22:16:21

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "CalmarHyperOptLoss",
  "spaces": "sell buy roi",
  "random_state": 1331,
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
2025-09-21 20:15:57,170 - freqtrade - INFO - freqtrade 2025.7
2025-09-21 20:15:57,501 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-21 20:15:57,502 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-21 20:15:59,063 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-21 20:15:59,066 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-21 20:15:59,067 - freqtrade.loggers - INFO - Logfile configured
2025-09-21 20:15:59,067 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-21 20:15:59,068 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-21 20:15:59,068 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-21 20:15:59,068 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-21 20:15:59,069 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20210101-20241231 ...
2025-09-21 20:15:59,078 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-21 20:15:59,079 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-21 20:15:59,080 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-21 20:15:59,080 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-21 20:15:59,081 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-21 20:15:59,082 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20210101-20241231
2025-09-21 20:15:59,083 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-21 20:15:59,103 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-21 20:15:59,104 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 20:15:59,108 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-21 20:15:59,109 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-21 20:15:59,109 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-21 20:15:59,146 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-21 20:16:01,956 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-21 20:16:01,991 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-21 20:16:01,991 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-21 20:16:01,992 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-21 20:16:01,992 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-21 20:16:01,993 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-21 20:16:01,993 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-21 20:16:01,994 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-21 20:16:01,994 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.672, '469': 0.23, '668': 0.076, '1337': 0}
2025-09-21 20:16:01,994 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-21 20:16:01,995 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-21 20:16:01,995 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-21 20:16:01,995 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-21 20:16:01,995 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-21 20:16:01,996 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-21 20:16:01,996 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-21 20:16:01,996 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-21 20:16:01,997 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-21 20:16:01,997 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-21 20:16:01,997 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-21 20:16:01,998 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-21 20:16:01,998 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-21 20:16:01,998 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-21 20:16:01,999 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-21 20:16:01,999 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-21 20:16:01,999 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-21 20:16:02,000 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-21 20:16:02,000 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-21 20:16:02,000 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-21 20:16:02,001 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-21 20:16:02,001 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-21 20:16:02,001 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 20:16:02,006 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-21 20:16:02,039 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-21 20:16:02,240 - freqtrade.optimize.backtesting - INFO - Loading data from 2021-01-01 00:00:00 up to 2024-12-31 00:00:00 (1460 days).
2025-09-21 20:16:04,575 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-21 20:16:04,578 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-21 20:16:04,578 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-21 20:16:04,579 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-21 20:16:04,579 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 5
2025-09-21 20:16:04,580 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.974
2025-09-21 20:16:04,580 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.293
2025-09-21 20:16:04,580 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.01
2025-09-21 20:16:04,581 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-21 20:16:04,581 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.0
2025-09-21 20:16:04,582 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-21 20:16:04,582 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 0
2025-09-21 20:16:04,582 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.996
2025-09-21 20:16:04,583 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-21 20:16:04,583 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-21 20:16:04,583 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-21 20:16:04,584 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-21 20:16:04,586 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 20:16:06,798 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 20:16:08,983 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 20:16:11,169 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 20:16:13,368 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 20:16:15,567 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2021-01-01 00:00:00 up to 2024-12-31 00:00:00 (1460 days).
2025-09-21 20:16:20,873 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-21_20-16-20.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      3 │         0.45 │           2.539 │         0.25 │     18:27:00 │    1     0     2  33.3 │
│ LTC/USDT │      2 │        -1.09 │          -1.602 │        -0.16 │      3:30:00 │    0     0     2     0 │
│ ETH/USDT │      2 │        -0.69 │          -2.397 │        -0.24 │      9:30:00 │    0     0     2     0 │
│ BTC/USDT │      6 │        -0.22 │          -2.483 │        -0.25 │      8:13:00 │    1     0     5  16.7 │
│ XRP/USDT │      2 │        -0.61 │          -2.485 │        -0.25 │      7:00:00 │    0     0     2     0 │
│    TOTAL │     15 │        -0.32 │          -6.428 │        -0.64 │      9:39:00 │    2     0    13  13.3 │
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
│    hammer_rebond │       4 │        -0.58 │          -2.310 │        -0.23 │     11:30:00 │    0     0     4     0 │
│ engulfing_rebond │      11 │        -0.22 │          -4.118 │        -0.41 │      8:58:00 │    2     0     9  18.2 │
│            TOTAL │      15 │        -0.32 │          -6.428 │        -0.64 │      9:39:00 │    2     0    13  13.3 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                               EXIT REASON STATS                                               
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│         roi │     2 │         2.52 │           5.253 │         0.53 │     22:20:00 │    2     0     0   100 │
│ exit_signal │    13 │        -0.75 │         -11.681 │        -1.17 │      7:42:00 │    0     0    13     0 │
│       TOTAL │    15 │        -0.32 │          -6.428 │        -0.64 │      9:39:00 │    2     0    13  13.3 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                          MIXED TAG STATS                                                          
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │         roi │      2 │         2.52 │           5.253 │         0.53 │     22:20:00 │    2     0     0   100 │
│    hammer_rebond │ exit_signal │      4 │        -0.58 │          -2.310 │        -0.23 │     11:30:00 │    0     0     4     0 │
│ engulfing_rebond │ exit_signal │      9 │        -0.83 │          -9.371 │        -0.94 │      6:00:00 │    0     0     9     0 │
│            TOTAL │             │     15 │        -0.32 │          -6.428 │        -0.64 │      9:39:00 │    2     0    13  13.3 │
└──────────────────┴─────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2021-01-01 00:00:00            │
│ Backtesting to                │ 2024-12-31 00:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 15 / 0.01                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 993.572 USDT                   │
│ Absolute profit               │ -6.428 USDT                    │
│ Total profit %                │ -0.64%                         │
│ CAGR %                        │ -0.16%                         │
│ Sortino                       │ -0.16                          │
│ Sharpe                        │ -0.06                          │
│ Calmar                        │ -0.81                          │
│ SQN                           │ -1.19                          │
│ Profit factor                 │ 0.45                           │
│ Expectancy (Ratio)            │ -0.43 (-0.48)                  │
│ Avg. daily profit             │ -0.004 USDT                    │
│ Avg. stake amount             │ 133.659 USDT                   │
│ Total trade volume            │ 4011.358 USDT                  │
│                               │                                │
│ Best Pair                     │ BNB/USDT 0.25%                 │
│ Worst Pair                    │ XRP/USDT -0.25%                │
│ Best trade                    │ BTC/USDT 2.99%                 │
│ Worst trade                   │ BTC/USDT -1.25%                │
│ Best day                      │ 3.574 USDT                     │
│ Worst day                     │ -2.249 USDT                    │
│ Days win/draw/lose            │ 2 / 1334 / 12                  │
│ Min/Max/Avg. Duration Winners │ 0d 22:20 / 0d 22:20 / 0d 22:20 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 0d 21:00 / 0d 07:42 │
│ Max Consecutive Wins / Loss   │ 1 / 11                         │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 991.892 USDT                   │
│ Max balance                   │ 1002.275 USDT                  │
│ Max % of account underwater   │ 1.04%                          │
│ Absolute Drawdown (Account)   │ 1.04%                          │
│ Absolute Drawdown             │ 10.383 USDT                    │
│ Drawdown high                 │ 2.275 USDT                     │
│ Drawdown low                  │ -8.108 USDT                    │
│ Drawdown Start                │ 2022-10-05 05:20:00            │
│ Drawdown End                  │ 2024-07-23 05:00:00            │
│ Market change                 │ 630.36%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2021-01-01 00:00:00 -> 2024-12-31 00:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     15 │        -0.32 │          -6.428 │        -0.64 │      9:39:00 │    2     0    13  13.3 │ 10.383 USDT  1.04% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-21T22:16:21.976345",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 1331,
  "total_daily_avg_trades": "15 / 0.01",
  "absolute_profit_usdt": -6.428,
  "total_profit_pct": -0.64,
  "cagr_pct": -0.16,
  "sortino": -0.16,
  "sharpe": -0.06,
  "calmar": -0.81,
  "sqn": -1.19,
  "max_consecutive_wins_loss": "1 / 11",
  "min_balance_usdt": 991.892,
  "max_balance_usdt": 1002.275,
  "absolute_drawdown_pct": 1.04,
  "market_change_pct": 630.36,
  "win_draw_loss_winpct": "2 0 13 13.3"
}
```
