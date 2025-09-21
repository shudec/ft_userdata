# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 8665  
**Timestamp:** 2025-09-21 22:04:27

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SortinoHyperOptLoss",
  "spaces": "sell buy roi",
  "random_state": 8665,
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
2025-09-21 20:03:51,570 - freqtrade - INFO - freqtrade 2025.7
2025-09-21 20:03:51,944 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-21 20:03:51,944 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-21 20:03:53,618 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-21 20:03:53,622 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-21 20:03:53,623 - freqtrade.loggers - INFO - Logfile configured
2025-09-21 20:03:53,624 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-21 20:03:53,624 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-21 20:03:53,625 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-21 20:03:53,625 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-21 20:03:53,625 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20210101-20241231 ...
2025-09-21 20:03:53,634 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-21 20:03:53,635 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-21 20:03:53,636 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-21 20:03:53,636 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-21 20:03:53,637 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-21 20:03:53,638 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20210101-20241231
2025-09-21 20:03:53,639 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-21 20:03:53,659 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-21 20:03:53,660 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 20:03:53,664 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-21 20:03:53,665 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-21 20:03:53,665 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-21 20:03:53,698 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-21 20:03:56,159 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-21 20:03:56,201 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-21 20:03:56,202 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-21 20:03:56,203 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-21 20:03:56,203 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-21 20:03:56,204 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-21 20:03:56,204 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-21 20:03:56,205 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-21 20:03:56,205 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.263, '183': 0.142, '783': 0.045, '2148': 0}
2025-09-21 20:03:56,205 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-21 20:03:56,206 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-21 20:03:56,206 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-21 20:03:56,206 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-21 20:03:56,207 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-21 20:03:56,207 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-21 20:03:56,208 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-21 20:03:56,208 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-21 20:03:56,208 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-21 20:03:56,209 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-21 20:03:56,209 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-21 20:03:56,209 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-21 20:03:56,210 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-21 20:03:56,210 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-21 20:03:56,210 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-21 20:03:56,211 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-21 20:03:56,211 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-21 20:03:56,211 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-21 20:03:56,212 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-21 20:03:56,212 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-21 20:03:56,213 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-21 20:03:56,213 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-21 20:03:56,213 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 20:03:56,219 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-21 20:03:56,251 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-21 20:03:56,475 - freqtrade.optimize.backtesting - INFO - Loading data from 2021-01-01 00:00:00 up to 2024-12-31 00:00:00 (1460 days).
2025-09-21 20:03:58,887 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-21 20:03:58,890 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-21 20:03:58,890 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-21 20:03:58,891 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.1
2025-09-21 20:03:58,891 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 18
2025-09-21 20:03:58,891 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.501
2025-09-21 20:03:58,892 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.097
2025-09-21 20:03:58,892 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.049
2025-09-21 20:03:58,892 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.0
2025-09-21 20:03:58,893 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.001
2025-09-21 20:03:58,893 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-21 20:03:58,893 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 10
2025-09-21 20:03:58,894 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.99
2025-09-21 20:03:58,894 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-21 20:03:58,894 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-21 20:03:58,895 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-21 20:03:58,895 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-21 20:03:58,897 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 20:04:01,586 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 20:04:04,279 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 20:04:06,940 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 20:04:09,605 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 20:04:12,330 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2021-01-01 00:00:00 up to 2024-12-31 00:00:00 (1460 days).
2025-09-21 20:04:26,552 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-21_20-04-26.meta.json"
Result for strategy IchimokuRebondStrategy
                                              BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │      7 │         1.51 │          38.207 │         3.82 │       20:46:00 │    4     1     2  57.1 │
│ ETH/USDT │     11 │         0.35 │           0.795 │         0.08 │ 1 day, 4:41:00 │    4     2     5  36.4 │
│ LTC/USDT │      9 │        -0.29 │           0.139 │         0.01 │ 1 day, 0:57:00 │    4     1     4  44.4 │
│ BNB/USDT │     12 │        -0.22 │          -7.258 │        -0.73 │ 1 day, 9:36:00 │    6     3     3  50.0 │
│ BTC/USDT │     11 │        -1.11 │         -41.515 │        -4.15 │ 1 day, 4:40:00 │    4     2     5  36.4 │
│    TOTAL │     50 │        -0.06 │          -9.632 │        -0.96 │ 1 day, 4:05:00 │   22     9    19  44.0 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                    ENTER TAG STATS                                                     
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │      50 │        -0.06 │          -9.632 │        -0.96 │ 1 day, 4:05:00 │   22     9    19  44.0 │
│            TOTAL │      50 │        -0.06 │          -9.632 │        -0.96 │ 1 day, 4:05:00 │   22     9    19  44.0 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│            roi │    30 │         1.84 │         308.974 │         30.9 │ 1 day, 7:28:00 │   21     9     0   100 │
│ take_profit_3R │     1 │         5.59 │          50.823 │         5.08 │        8:45:00 │    1     0     0   100 │
│      stop_loss │    19 │        -3.36 │        -369.429 │       -36.94 │       23:45:00 │    0     0    19     0 │
│          TOTAL │    50 │        -0.06 │          -9.632 │        -0.96 │ 1 day, 4:05:00 │   22     9    19  44.0 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                            MIXED TAG STATS                                                             
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │            roi │     30 │         1.84 │         308.974 │         30.9 │ 1 day, 7:28:00 │   21     9     0   100 │
│ engulfing_rebond │ take_profit_3R │      1 │         5.59 │          50.823 │         5.08 │        8:45:00 │    1     0     0   100 │
│ engulfing_rebond │      stop_loss │     19 │        -3.36 │        -369.429 │       -36.94 │       23:45:00 │    0     0    19     0 │
│            TOTAL │                │     50 │        -0.06 │          -9.632 │        -0.96 │ 1 day, 4:05:00 │   22     9    19  44.0 │
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
│ Total/Daily Avg Trades        │ 50 / 0.03                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 990.368 USDT                   │
│ Absolute profit               │ -9.632 USDT                    │
│ Total profit %                │ -0.96%                         │
│ CAGR %                        │ -0.24%                         │
│ Sortino                       │ -0.03                          │
│ Sharpe                        │ -0.01                          │
│ Calmar                        │ -0.10                          │
│ SQN                           │ -0.07                          │
│ Profit factor                 │ 0.97                           │
│ Expectancy (Ratio)            │ -0.19 (-0.19)                  │
│ Avg. daily profit             │ -0.007 USDT                    │
│ Avg. stake amount             │ 663.224 USDT                   │
│ Total trade volume            │ 66445.57 USDT                  │
│                               │                                │
│ Best Pair                     │ XRP/USDT 3.82%                 │
│ Worst Pair                    │ BTC/USDT -4.15%                │
│ Best trade                    │ ETH/USDT 6.93%                 │
│ Worst trade                   │ LTC/USDT -6.94%                │
│ Best day                      │ 50.823 USDT                    │
│ Worst day                     │ -21.688 USDT                   │
│ Days win/draw/lose            │ 21 / 1377 / 19                 │
│ Min/Max/Avg. Duration Winners │ 0d 08:45 / 1d 11:50 / 1d 02:51 │
│ Min/Max/Avg. Duration Losers  │ 0d 05:00 / 2d 20:05 / 0d 23:45 │
│ Max Consecutive Wins / Loss   │ 3 / 5                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 892.34 USDT                    │
│ Max balance                   │ 1028.191 USDT                  │
│ Max % of account underwater   │ 13.21%                         │
│ Absolute Drawdown (Account)   │ 13.21%                         │
│ Absolute Drawdown             │ 135.851 USDT                   │
│ Drawdown high                 │ 28.191 USDT                    │
│ Drawdown low                  │ -107.66 USDT                   │
│ Drawdown Start                │ 2021-08-15 04:50:00            │
│ Drawdown End                  │ 2023-09-06 17:05:00            │
│ Market change                 │ 630.36%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2021-01-01 00:00:00 -> 2024-12-31 00:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                  
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     50 │        -0.06 │          -9.632 │        -0.96 │ 1 day, 4:05:00 │   22     9    19  44.0 │ 135.851 USDT  13.21% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-21T22:04:27.686242",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 8665,
  "total_daily_avg_trades": "50 / 0.03",
  "absolute_profit_usdt": -9.632,
  "total_profit_pct": -0.96,
  "cagr_pct": -0.24,
  "sortino": -0.03,
  "sharpe": -0.01,
  "calmar": -0.1,
  "sqn": -0.07,
  "max_consecutive_wins_loss": "3 / 5",
  "min_balance_usdt": 892.34,
  "max_balance_usdt": 1028.191,
  "absolute_drawdown_pct": 13.21,
  "market_change_pct": 630.36,
  "win_draw_loss_winpct": "0 0 0 0"
}
```
