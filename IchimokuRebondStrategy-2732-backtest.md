# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 2732  
**Timestamp:** 2025-09-21 22:21:47

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "sell buy",
  "random_state": 2732,
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
2025-09-21 20:21:15,910 - freqtrade - INFO - freqtrade 2025.7
2025-09-21 20:21:16,283 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-21 20:21:16,283 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-21 20:21:17,786 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-21 20:21:17,789 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-21 20:21:17,789 - freqtrade.loggers - INFO - Logfile configured
2025-09-21 20:21:17,790 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-21 20:21:17,790 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-21 20:21:17,790 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-21 20:21:17,791 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-21 20:21:17,791 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20210101-20241231 ...
2025-09-21 20:21:17,799 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-21 20:21:17,800 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-21 20:21:17,800 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-21 20:21:17,800 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-21 20:21:17,801 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-21 20:21:17,801 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20210101-20241231
2025-09-21 20:21:17,803 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-21 20:21:17,822 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-21 20:21:17,822 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 20:21:17,826 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-21 20:21:17,828 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-21 20:21:17,828 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-21 20:21:17,867 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-21 20:21:20,085 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-21 20:21:20,123 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-21 20:21:20,124 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-21 20:21:20,125 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-21 20:21:20,125 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-21 20:21:20,126 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-21 20:21:20,126 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-21 20:21:20,126 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-21 20:21:20,127 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.672, '469': 0.23, '668': 0.076, '1337': 0}
2025-09-21 20:21:20,127 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-21 20:21:20,128 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-21 20:21:20,128 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-21 20:21:20,128 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-21 20:21:20,129 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-21 20:21:20,129 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-21 20:21:20,129 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-21 20:21:20,130 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-21 20:21:20,130 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-21 20:21:20,130 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-21 20:21:20,131 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-21 20:21:20,131 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-21 20:21:20,132 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-21 20:21:20,132 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-21 20:21:20,133 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-21 20:21:20,133 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-21 20:21:20,133 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-21 20:21:20,134 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-21 20:21:20,134 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-21 20:21:20,134 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-21 20:21:20,135 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-21 20:21:20,135 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-21 20:21:20,135 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 20:21:20,141 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-21 20:21:20,175 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-21 20:21:20,377 - freqtrade.optimize.backtesting - INFO - Loading data from 2021-01-01 00:00:00 up to 2024-12-31 00:00:00 (1460 days).
2025-09-21 20:21:22,845 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-21 20:21:22,849 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-21 20:21:22,850 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-21 20:21:22,850 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.1
2025-09-21 20:21:22,851 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 18
2025-09-21 20:21:22,851 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.913
2025-09-21 20:21:22,851 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.781
2025-09-21 20:21:22,852 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.044
2025-09-21 20:21:22,852 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.0
2025-09-21 20:21:22,853 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.001
2025-09-21 20:21:22,853 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.995
2025-09-21 20:21:22,854 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 2
2025-09-21 20:21:22,854 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.99
2025-09-21 20:21:22,855 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-21 20:21:22,855 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-21 20:21:22,855 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-21 20:21:22,856 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-21 20:21:22,858 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 20:21:25,633 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 20:21:28,428 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 20:21:31,101 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 20:21:33,745 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 20:21:36,466 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2021-01-01 00:00:00 up to 2024-12-31 00:00:00 (1460 days).
2025-09-21 20:21:46,244 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-21_20-21-46.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │      7 │         0.45 │          37.257 │         3.73 │     12:05:00 │    3     0     4  42.9 │
│ ETH/USDT │     11 │         0.69 │          36.952 │          3.7 │     17:36:00 │    4     2     5  36.4 │
│ BNB/USDT │     12 │        -0.33 │         -37.947 │        -3.79 │     17:08:00 │    4     4     4  33.3 │
│ LTC/USDT │      9 │        -0.68 │         -53.499 │        -5.35 │     14:46:00 │    3     1     5  33.3 │
│ BTC/USDT │     11 │        -0.81 │         -70.741 │        -7.07 │     14:58:00 │    3     2     6  27.3 │
│    TOTAL │     50 │        -0.17 │         -87.978 │         -8.8 │     15:38:00 │   17     9    24  34.0 │
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
│ engulfing_rebond │      50 │        -0.17 │         -87.978 │         -8.8 │     15:38:00 │   17     9    24  34.0 │
│            TOTAL │      50 │        -0.17 │         -87.978 │         -8.8 │     15:38:00 │   17     9    24  34.0 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│            roi │    23 │          1.2 │         206.838 │        20.68 │     23:04:00 │   14     9     0   100 │
│ take_profit_3R │     3 │         5.15 │         138.870 │        13.89 │     12:58:00 │    3     0     0   100 │
│      stop_loss │    24 │        -2.15 │        -433.686 │       -43.37 │      8:49:00 │    0     0    24     0 │
│          TOTAL │    50 │        -0.17 │         -87.978 │         -8.8 │     15:38:00 │   17     9    24  34.0 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                           MIXED TAG STATS                                                            
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │            roi │     23 │          1.2 │         206.838 │        20.68 │     23:04:00 │   14     9     0   100 │
│ engulfing_rebond │ take_profit_3R │      3 │         5.15 │         138.870 │        13.89 │     12:58:00 │    3     0     0   100 │
│ engulfing_rebond │      stop_loss │     24 │        -2.15 │        -433.686 │       -43.37 │      8:49:00 │    0     0    24     0 │
│            TOTAL │                │     50 │        -0.17 │         -87.978 │         -8.8 │     15:38:00 │   17     9    24  34.0 │
└──────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2021-01-01 00:00:00            │
│ Backtesting to                │ 2024-12-31 00:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 50 / 0.03                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 912.022 USDT                   │
│ Absolute profit               │ -87.978 USDT                   │
│ Total profit %                │ -8.80%                         │
│ CAGR %                        │ -2.28%                         │
│ Sortino                       │ -0.37                          │
│ Sharpe                        │ -0.06                          │
│ Calmar                        │ -0.70                          │
│ SQN                           │ -0.62                          │
│ Profit factor                 │ 0.80                           │
│ Expectancy (Ratio)            │ -1.76 (-0.28)                  │
│ Avg. daily profit             │ -0.06 USDT                     │
│ Avg. stake amount             │ 882.967 USDT                   │
│ Total trade volume            │ 88385.362 USDT                 │
│                               │                                │
│ Best Pair                     │ XRP/USDT 3.73%                 │
│ Worst Pair                    │ BTC/USDT -7.07%                │
│ Best trade                    │ ETH/USDT 7.59%                 │
│ Worst trade                   │ LTC/USDT -4.09%                │
│ Best day                      │ 53.554 USDT                    │
│ Worst day                     │ -22.302 USDT                   │
│ Days win/draw/lose            │ 17 / 1376 / 24                 │
│ Min/Max/Avg. Duration Winners │ 0d 06:15 / 0d 22:20 / 0d 20:07 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:45 / 0d 21:05 / 0d 08:49 │
│ Max Consecutive Wins / Loss   │ 2 / 7                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 877.046 USDT                   │
│ Max balance                   │ 1048.45 USDT                   │
│ Max % of account underwater   │ 16.35%                         │
│ Absolute Drawdown (Account)   │ 16.35%                         │
│ Absolute Drawdown             │ 171.404 USDT                   │
│ Drawdown high                 │ 48.45 USDT                     │
│ Drawdown low                  │ -122.954 USDT                  │
│ Drawdown Start                │ 2021-01-06 23:45:00            │
│ Drawdown End                  │ 2023-09-06 17:05:00            │
│ Market change                 │ 630.36%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2021-01-01 00:00:00 -> 2024-12-31 00:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     50 │        -0.17 │         -87.978 │         -8.8 │     15:38:00 │   17     9    24  34.0 │ 171.404 USDT  16.35% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-21T22:21:47.342959",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 2732,
  "total_daily_avg_trades": "50 / 0.03",
  "absolute_profit_usdt": -87.978,
  "total_profit_pct": -8.8,
  "cagr_pct": -2.28,
  "sortino": -0.37,
  "sharpe": -0.06,
  "calmar": -0.7,
  "sqn": -0.62,
  "max_consecutive_wins_loss": "2 / 7",
  "min_balance_usdt": 877.046,
  "max_balance_usdt": 1048.45,
  "absolute_drawdown_pct": 16.35,
  "market_change_pct": 630.36,
  "win_draw_loss_winpct": "17 9 24 34.0"
}
```
