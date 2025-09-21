# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 2142  
**Timestamp:** 2025-09-21 22:27:01

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 2142,
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
2025-09-21 20:26:27,465 - freqtrade - INFO - freqtrade 2025.7
2025-09-21 20:26:27,824 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-21 20:26:27,825 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-21 20:26:29,322 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-21 20:26:29,325 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-21 20:26:29,326 - freqtrade.loggers - INFO - Logfile configured
2025-09-21 20:26:29,326 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-21 20:26:29,327 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-21 20:26:29,327 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-21 20:26:29,327 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-21 20:26:29,328 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20210101-20241231 ...
2025-09-21 20:26:29,336 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-21 20:26:29,337 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-21 20:26:29,337 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-21 20:26:29,338 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-21 20:26:29,338 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-21 20:26:29,339 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20210101-20241231
2025-09-21 20:26:29,340 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-21 20:26:29,359 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-21 20:26:29,360 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 20:26:29,364 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-21 20:26:29,365 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-21 20:26:29,365 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-21 20:26:29,401 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-21 20:26:31,757 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-21 20:26:31,794 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-21 20:26:31,794 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-21 20:26:31,795 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-21 20:26:31,796 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-21 20:26:31,796 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-21 20:26:31,797 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-21 20:26:31,797 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-21 20:26:31,797 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.524, '438': 0.144, '1133': 0.057, '2477': 0}
2025-09-21 20:26:31,798 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-21 20:26:31,798 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-21 20:26:31,798 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-21 20:26:31,799 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-21 20:26:31,799 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-21 20:26:31,800 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-21 20:26:31,800 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-21 20:26:31,800 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-21 20:26:31,801 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-21 20:26:31,801 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-21 20:26:31,802 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-21 20:26:31,802 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-21 20:26:31,802 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-21 20:26:31,803 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-21 20:26:31,803 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-21 20:26:31,803 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-21 20:26:31,804 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-21 20:26:31,804 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-21 20:26:31,804 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-21 20:26:31,805 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-21 20:26:31,805 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-21 20:26:31,805 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-21 20:26:31,806 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 20:26:31,811 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-21 20:26:31,845 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-21 20:26:32,087 - freqtrade.optimize.backtesting - INFO - Loading data from 2021-01-01 00:00:00 up to 2024-12-31 00:00:00 (1460 days).
2025-09-21 20:26:34,490 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-21 20:26:34,493 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-21 20:26:34,493 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-21 20:26:34,494 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.1
2025-09-21 20:26:34,494 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 18
2025-09-21 20:26:34,494 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.913
2025-09-21 20:26:34,495 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.781
2025-09-21 20:26:34,495 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.044
2025-09-21 20:26:34,495 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.0
2025-09-21 20:26:34,496 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.001
2025-09-21 20:26:34,496 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.995
2025-09-21 20:26:34,497 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 2
2025-09-21 20:26:34,497 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.99
2025-09-21 20:26:34,497 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-21 20:26:34,497 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-21 20:26:34,498 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-21 20:26:34,498 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-21 20:26:34,500 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 20:26:37,187 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 20:26:39,992 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 20:26:42,692 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 20:26:45,414 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 20:26:48,135 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2021-01-01 00:00:00 up to 2024-12-31 00:00:00 (1460 days).
2025-09-21 20:27:00,196 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-21_20-27-00.meta.json"
Result for strategy IchimokuRebondStrategy
                                              BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │     11 │         0.96 │          56.421 │         5.64 │ 1 day, 0:59:00 │    4     1     6  36.4 │
│ XRP/USDT │      7 │         0.07 │          10.851 │         1.09 │       16:02:00 │    2     0     5  28.6 │
│ LTC/USDT │      8 │        -0.13 │         -17.261 │        -1.73 │       19:22:00 │    2     1     5  25.0 │
│ BNB/USDT │     12 │        -0.66 │         -70.376 │        -7.04 │ 1 day, 3:40:00 │    4     0     8  33.3 │
│ BTC/USDT │     11 │        -1.13 │        -100.251 │       -10.03 │       20:55:00 │    2     1     8  18.2 │
│    TOTAL │     49 │        -0.21 │        -120.617 │       -12.06 │       22:32:00 │   14     3    32  28.6 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
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
│ engulfing_rebond │      49 │        -0.21 │        -120.617 │       -12.06 │     22:32:00 │   14     3    32  28.6 │
│            TOTAL │      49 │        -0.21 │        -120.617 │       -12.06 │     22:32:00 │   14     3    32  28.6 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│            roi │    13 │         2.55 │         263.207 │        26.32 │ 1 day, 13:30:00 │   10     3     0   100 │
│ take_profit_3R │     4 │         5.84 │         183.441 │        18.34 │        17:11:00 │    4     0     0   100 │
│      stop_loss │    32 │        -2.09 │        -567.265 │       -56.73 │        17:07:00 │    0     0    32     0 │
│          TOTAL │    49 │        -0.21 │        -120.617 │       -12.06 │        22:32:00 │   14     3    32  28.6 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                             MIXED TAG STATS                                                             
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │            roi │     13 │         2.55 │         263.207 │        26.32 │ 1 day, 13:30:00 │   10     3     0   100 │
│ engulfing_rebond │ take_profit_3R │      4 │         5.84 │         183.441 │        18.34 │        17:11:00 │    4     0     0   100 │
│ engulfing_rebond │      stop_loss │     32 │        -2.09 │        -567.265 │       -56.73 │        17:07:00 │    0     0    32     0 │
│            TOTAL │                │     49 │        -0.21 │        -120.617 │       -12.06 │        22:32:00 │   14     3    32  28.6 │
└──────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2021-01-01 00:00:00            │
│ Backtesting to                │ 2024-12-31 00:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 49 / 0.03                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 879.383 USDT                   │
│ Absolute profit               │ -120.617 USDT                  │
│ Total profit %                │ -12.06%                        │
│ CAGR %                        │ -3.16%                         │
│ Sortino                       │ -0.49                          │
│ Sharpe                        │ -0.07                          │
│ Calmar                        │ -0.77                          │
│ SQN                           │ -0.72                          │
│ Profit factor                 │ 0.79                           │
│ Expectancy (Ratio)            │ -2.46 (-0.20)                  │
│ Avg. daily profit             │ -0.083 USDT                    │
│ Avg. stake amount             │ 869.437 USDT                   │
│ Total trade volume            │ 85254.505 USDT                 │
│                               │                                │
│ Best Pair                     │ ETH/USDT 5.64%                 │
│ Worst Pair                    │ BTC/USDT -10.03%               │
│ Best trade                    │ ETH/USDT 9.58%                 │
│ Worst trade                   │ LTC/USDT -4.09%                │
│ Best day                      │ 61.131 USDT                    │
│ Worst day                     │ -22.487 USDT                   │
│ Days win/draw/lose            │ 14 / 1370 / 32                 │
│ Min/Max/Avg. Duration Winners │ 0d 06:15 / 1d 17:20 / 1d 06:08 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:45 / 2d 02:25 / 0d 17:07 │
│ Max Consecutive Wins / Loss   │ 2 / 7                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 844.349 USDT                   │
│ Max balance                   │ 1061.131 USDT                  │
│ Max % of account underwater   │ 20.43%                         │
│ Absolute Drawdown (Account)   │ 20.43%                         │
│ Absolute Drawdown             │ 216.782 USDT                   │
│ Drawdown high                 │ 61.131 USDT                    │
│ Drawdown low                  │ -155.651 USDT                  │
│ Drawdown Start                │ 2021-01-07 03:45:00            │
│ Drawdown End                  │ 2023-10-31 15:15:00            │
│ Market change                 │ 630.36%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2021-01-01 00:00:00 -> 2024-12-31 00:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     49 │        -0.21 │        -120.617 │       -12.06 │     22:32:00 │   14     3    32  28.6 │ 216.782 USDT  20.43% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-21T22:27:01.303604",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 2142,
  "total_daily_avg_trades": "49 / 0.03",
  "absolute_profit_usdt": -120.617,
  "total_profit_pct": -12.06,
  "cagr_pct": -3.16,
  "sortino": -0.49,
  "sharpe": -0.07,
  "calmar": -0.77,
  "sqn": -0.72,
  "max_consecutive_wins_loss": "2 / 7",
  "min_balance_usdt": 844.349,
  "max_balance_usdt": 1061.131,
  "absolute_drawdown_pct": 20.43,
  "market_change_pct": 630.36,
  "win_draw_loss_winpct": "14 3 32 28.6"
}
```
