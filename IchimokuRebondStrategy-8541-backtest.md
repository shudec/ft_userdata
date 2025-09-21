# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 8541  
**Timestamp:** 2025-09-21 21:54:10

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell buy roi",
  "random_state": 8541,
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
2025-09-21 19:53:41,573 - freqtrade - INFO - freqtrade 2025.7
2025-09-21 19:53:41,963 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-21 19:53:41,964 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-21 19:53:43,658 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-21 19:53:43,662 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-21 19:53:43,663 - freqtrade.loggers - INFO - Logfile configured
2025-09-21 19:53:43,663 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-21 19:53:43,664 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-21 19:53:43,664 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-21 19:53:43,664 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-21 19:53:43,665 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20210101-20241231 ...
2025-09-21 19:53:43,675 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-21 19:53:43,677 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-21 19:53:43,677 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-21 19:53:43,678 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-21 19:53:43,678 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-21 19:53:43,679 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20210101-20241231
2025-09-21 19:53:43,680 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-21 19:53:43,699 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-21 19:53:43,700 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 19:53:43,704 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-21 19:53:43,705 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-21 19:53:43,705 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-21 19:53:43,739 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-21 19:53:46,492 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-21 19:53:46,536 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-21 19:53:46,536 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-21 19:53:46,537 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-21 19:53:46,538 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-21 19:53:46,538 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-21 19:53:46,539 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-21 19:53:46,539 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-21 19:53:46,540 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.587, '136': 0.19, '722': 0.029, '2143': 0}
2025-09-21 19:53:46,540 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-21 19:53:46,541 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-21 19:53:46,541 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-21 19:53:46,541 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-21 19:53:46,542 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-21 19:53:46,542 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-21 19:53:46,543 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-21 19:53:46,543 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-21 19:53:46,544 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-21 19:53:46,545 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-21 19:53:46,545 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-21 19:53:46,545 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-21 19:53:46,546 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-21 19:53:46,546 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-21 19:53:46,547 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-21 19:53:46,548 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-21 19:53:46,548 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-21 19:53:46,549 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-21 19:53:46,549 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-21 19:53:46,550 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-21 19:53:46,551 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-21 19:53:46,551 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-21 19:53:46,552 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 19:53:46,560 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-21 19:53:46,600 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-21 19:53:46,871 - freqtrade.optimize.backtesting - INFO - Loading data from 2021-01-01 00:00:00 up to 2024-12-31 00:00:00 (1460 days).
2025-09-21 19:53:49,378 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-21 19:53:49,382 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-21 19:53:49,383 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-21 19:53:49,383 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 3
2025-09-21 19:53:49,384 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-09-21 19:53:49,384 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.633
2025-09-21 19:53:49,385 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.713
2025-09-21 19:53:49,385 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.045
2025-09-21 19:53:49,385 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-21 19:53:49,386 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.0
2025-09-21 19:53:49,386 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.996
2025-09-21 19:53:49,387 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 8
2025-09-21 19:53:49,387 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.992
2025-09-21 19:53:49,387 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2.5
2025-09-21 19:53:49,388 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-21 19:53:49,388 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-21 19:53:49,389 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-21 19:53:49,391 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:53:52,251 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:53:55,163 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:53:58,028 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:54:00,892 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:54:03,734 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2021-01-01 00:00:00 up to 2024-12-31 00:00:00 (1460 days).
2025-09-21 19:54:08,984 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-21_19-54-08.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │      3 │         1.85 │          55.420 │         5.54 │     12:10:00 │    2     0     1  66.7 │
│ LTC/USDT │      1 │         4.69 │          49.832 │         4.98 │      9:40:00 │    1     0     0   100 │
│ BNB/USDT │      1 │          2.9 │          29.950 │          3.0 │     13:15:00 │    1     0     0   100 │
│ ETH/USDT │      2 │        -0.72 │         -16.006 │         -1.6 │     21:08:00 │    0     1     1     0 │
│ XRP/USDT │      1 │        -1.75 │         -19.237 │        -1.92 │     15:35:00 │    0     0     1     0 │
│    TOTAL │      8 │         1.24 │          99.959 │         10.0 │     14:39:00 │    4     1     3  50.0 │
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
│ engulfing_rebond │       8 │         1.24 │          99.959 │         10.0 │     14:39:00 │    4     1     3  50.0 │
│            TOTAL │       8 │         1.24 │          99.959 │         10.0 │     14:39:00 │    4     1     3  50.0 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2.5R │     2 │         4.52 │          93.047 │          9.3 │     10:20:00 │    2     0     0   100 │
│              roi │     3 │         1.93 │          60.629 │         6.06 │     21:08:00 │    2     1     0   100 │
│        stop_loss │     3 │        -1.64 │         -53.717 │        -5.37 │     11:03:00 │    0     0     3     0 │
│            TOTAL │     8 │         1.24 │          99.959 │         10.0 │     14:39:00 │    4     1     3  50.0 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                            MIXED TAG STATS                                                             
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │ take_profit_2.5R │      2 │         4.52 │          93.047 │          9.3 │     10:20:00 │    2     0     0   100 │
│ engulfing_rebond │              roi │      3 │         1.93 │          60.629 │         6.06 │     21:08:00 │    2     1     0   100 │
│ engulfing_rebond │        stop_loss │      3 │        -1.64 │         -53.717 │        -5.37 │     11:03:00 │    0     0     3     0 │
│            TOTAL │                  │      8 │         1.24 │          99.959 │         10.0 │     14:39:00 │    4     1     3  50.0 │
└──────────────────┴──────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2021-01-01 00:00:00            │
│ Backtesting to                │ 2024-12-31 00:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 8 / 0.01                       │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1099.959 USDT                  │
│ Absolute profit               │ 99.959 USDT                    │
│ Total profit %                │ 10.00%                         │
│ CAGR %                        │ 2.41%                          │
│ Sortino                       │ 0.95                           │
│ Sharpe                        │ 0.05                           │
│ Calmar                        │ 2.73                           │
│ SQN                           │ 1.22                           │
│ Profit factor                 │ 2.86                           │
│ Expectancy (Ratio)            │ 12.49 (0.57)                   │
│ Avg. daily profit             │ 0.068 USDT                     │
│ Avg. stake amount             │ 1062.981 USDT                  │
│ Total trade volume            │ 17141.902 USDT                 │
│                               │                                │
│ Best Pair                     │ BTC/USDT 5.54%                 │
│ Worst Pair                    │ XRP/USDT -1.92%                │
│ Best trade                    │ LTC/USDT 4.69%                 │
│ Worst trade                   │ XRP/USDT -1.75%                │
│ Best day                      │ 49.832 USDT                    │
│ Worst day                     │ -19.237 USDT                   │
│ Days win/draw/lose            │ 4 / 1339 / 3                   │
│ Min/Max/Avg. Duration Winners │ 0d 09:40 / 0d 14:25 / 0d 12:05 │
│ Min/Max/Avg. Duration Losers  │ 0d 06:30 / 0d 15:35 / 0d 11:03 │
│ Max Consecutive Wins / Loss   │ 3 / 4                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 1043.216 USDT                  │
│ Max balance                   │ 1122.997 USDT                  │
│ Max % of account underwater   │ 4.78%                          │
│ Absolute Drawdown (Account)   │ 4.78%                          │
│ Absolute Drawdown             │ 53.717 USDT                    │
│ Drawdown high                 │ 122.997 USDT                   │
│ Drawdown low                  │ 69.28 USDT                     │
│ Drawdown Start                │ 2023-01-09 00:40:00            │
│ Drawdown End                  │ 2024-05-19 19:05:00            │
│ Market change                 │ 630.36%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2021-01-01 00:00:00 -> 2024-12-31 00:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │      8 │         1.24 │          99.959 │         10.0 │     14:39:00 │    4     1     3  50.0 │ 53.717 USDT  4.78% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-21T21:54:10.108439",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 8541,
  "total_daily_avg_trades": "8 / 0.01",
  "absolute_profit_usdt": 99.959,
  "total_profit_pct": 10.0,
  "cagr_pct": 2.41,
  "sortino": 0.95,
  "sharpe": 0.05,
  "calmar": 2.73,
  "sqn": 1.22,
  "max_consecutive_wins_loss": "3 / 4",
  "min_balance_usdt": 1043.216,
  "max_balance_usdt": 1122.997,
  "absolute_drawdown_pct": 4.78,
  "market_change_pct": 630.36,
  "win_draw_loss_winpct": "4 1 3 50.0"
}
```
