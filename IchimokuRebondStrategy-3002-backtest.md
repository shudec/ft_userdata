# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 3002  
**Timestamp:** 2025-09-21 21:48:32

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell buy roi",
  "random_state": 3002,
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
2025-09-21 19:48:01,450 - freqtrade - INFO - freqtrade 2025.7
2025-09-21 19:48:01,793 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-21 19:48:01,793 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-21 19:48:03,415 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-21 19:48:03,418 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-21 19:48:03,418 - freqtrade.loggers - INFO - Logfile configured
2025-09-21 19:48:03,419 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-21 19:48:03,419 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-21 19:48:03,420 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-21 19:48:03,420 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-21 19:48:03,420 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20210101-20241231 ...
2025-09-21 19:48:03,430 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-21 19:48:03,431 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-21 19:48:03,431 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-21 19:48:03,432 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-21 19:48:03,432 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-21 19:48:03,433 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20210101-20241231
2025-09-21 19:48:03,434 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-21 19:48:03,453 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-21 19:48:03,454 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 19:48:03,458 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-21 19:48:03,459 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-21 19:48:03,459 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-21 19:48:03,493 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-21 19:48:05,840 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-21 19:48:05,889 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-21 19:48:05,890 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-21 19:48:05,891 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-21 19:48:05,892 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-21 19:48:05,893 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-21 19:48:05,893 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-21 19:48:05,894 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-21 19:48:05,894 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.427, '474': 0.179, '800': 0.064, '1657': 0}
2025-09-21 19:48:05,895 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-21 19:48:05,895 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-21 19:48:05,896 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-21 19:48:05,896 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-21 19:48:05,897 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-21 19:48:05,897 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-21 19:48:05,898 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-21 19:48:05,898 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-21 19:48:05,898 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-21 19:48:05,899 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-21 19:48:05,899 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-21 19:48:05,900 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-21 19:48:05,900 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-21 19:48:05,901 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-21 19:48:05,901 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-21 19:48:05,902 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-21 19:48:05,902 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-21 19:48:05,902 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-21 19:48:05,903 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-21 19:48:05,903 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-21 19:48:05,904 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-21 19:48:05,904 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-21 19:48:05,905 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 19:48:05,910 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-21 19:48:05,945 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-21 19:48:06,158 - freqtrade.optimize.backtesting - INFO - Loading data from 2021-01-01 00:00:00 up to 2024-12-31 00:00:00 (1460 days).
2025-09-21 19:48:08,575 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-21 19:48:08,579 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-21 19:48:08,580 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-21 19:48:08,580 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.2
2025-09-21 19:48:08,580 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 0
2025-09-21 19:48:08,581 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.926
2025-09-21 19:48:08,581 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.911
2025-09-21 19:48:08,582 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.031
2025-09-21 19:48:08,582 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-21 19:48:08,582 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-21 19:48:08,583 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.998
2025-09-21 19:48:08,583 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 2
2025-09-21 19:48:08,584 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-09-21 19:48:08,584 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-21 19:48:08,584 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-21 19:48:08,585 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-21 19:48:08,585 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-21 19:48:08,587 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:48:11,413 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:48:14,296 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:48:17,077 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:48:19,867 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:48:22,778 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2021-01-01 00:00:00 up to 2024-12-31 00:00:00 (1460 days).
2025-09-21 19:48:31,190 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-21_19-48-31.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │     21 │         0.12 │          19.195 │         1.92 │      5:45:00 │    9     1    11  42.9 │
│ XRP/USDT │     15 │         0.22 │          11.599 │         1.16 │      5:08:00 │    6     0     9  40.0 │
│ LTC/USDT │     20 │        -0.03 │           0.048 │          0.0 │      4:16:00 │    9     0    11  45.0 │
│ BNB/USDT │     14 │        -0.12 │         -14.609 │        -1.46 │      3:20:00 │    6     0     8  42.9 │
│ BTC/USDT │     26 │        -0.16 │         -36.238 │        -3.62 │      4:50:00 │   11     0    15  42.3 │
│    TOTAL │     96 │        -0.01 │         -20.006 │         -2.0 │      4:45:00 │   41     1    54  42.7 │
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
│ engulfing_rebond │      96 │        -0.01 │         -20.006 │         -2.0 │      4:45:00 │   41     1    54  42.7 │
│            TOTAL │      96 │        -0.01 │         -20.006 │         -2.0 │      4:45:00 │   41     1    54  42.7 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │    41 │         1.48 │         588.457 │        58.85 │        4:06:00 │   41     0     0   100 │
│            roi │     1 │          0.0 │           0.000 │          0.0 │ 1 day, 6:35:00 │    0     1     0     0 │
│      stop_loss │    54 │        -1.14 │        -608.464 │       -60.85 │        4:46:00 │    0     0    54     0 │
│          TOTAL │    96 │        -0.01 │         -20.006 │         -2.0 │        4:45:00 │   41     1    54  42.7 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                            MIXED TAG STATS                                                             
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │ take_profit_1R │     41 │         1.48 │         588.457 │        58.85 │        4:06:00 │   41     0     0   100 │
│ engulfing_rebond │            roi │      1 │          0.0 │           0.000 │          0.0 │ 1 day, 6:35:00 │    0     1     0     0 │
│ engulfing_rebond │      stop_loss │     54 │        -1.14 │        -608.464 │       -60.85 │        4:46:00 │    0     0    54     0 │
│            TOTAL │                │     96 │        -0.01 │         -20.006 │         -2.0 │        4:45:00 │   41     1    54  42.7 │
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
│ Total/Daily Avg Trades        │ 96 / 0.07                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 979.994 USDT                   │
│ Absolute profit               │ -20.006 USDT                   │
│ Total profit %                │ -2.00%                         │
│ CAGR %                        │ -0.50%                         │
│ Sortino                       │ -0.06                          │
│ Sharpe                        │ -0.02                          │
│ Calmar                        │ -0.13                          │
│ SQN                           │ -0.15                          │
│ Profit factor                 │ 0.97                           │
│ Expectancy (Ratio)            │ -0.21 (-0.03)                  │
│ Avg. daily profit             │ -0.014 USDT                    │
│ Avg. stake amount             │ 995.599 USDT                   │
│ Total trade volume            │ 191517.613 USDT                │
│                               │                                │
│ Best Pair                     │ ETH/USDT 1.92%                 │
│ Worst Pair                    │ BTC/USDT -3.62%                │
│ Best trade                    │ LTC/USDT 4.56%                 │
│ Worst trade                   │ LTC/USDT -3.22%                │
│ Best day                      │ 38.251 USDT                    │
│ Worst day                     │ -22.182 USDT                   │
│ Days win/draw/lose            │ 39 / 1348 / 53                 │
│ Min/Max/Avg. Duration Winners │ 0d 00:10 / 0d 14:15 / 0d 04:06 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:20 / 1d 04:10 / 0d 04:46 │
│ Max Consecutive Wins / Loss   │ 5 / 6                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 914.387 USDT                   │
│ Max balance                   │ 1140.004 USDT                  │
│ Max % of account underwater   │ 19.79%                         │
│ Absolute Drawdown (Account)   │ 19.79%                         │
│ Absolute Drawdown             │ 225.618 USDT                   │
│ Drawdown high                 │ 140.004 USDT                   │
│ Drawdown low                  │ -85.613 USDT                   │
│ Drawdown Start                │ 2022-11-26 01:10:00            │
│ Drawdown End                  │ 2024-10-15 11:35:00            │
│ Market change                 │ 630.36%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2021-01-01 00:00:00 -> 2024-12-31 00:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     96 │        -0.01 │         -20.006 │         -2.0 │      4:45:00 │   41     1    54  42.7 │ 225.618 USDT  19.79% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-21T21:48:32.328372",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 3002,
  "total_daily_avg_trades": "96 / 0.07",
  "absolute_profit_usdt": -20.006,
  "total_profit_pct": -2.0,
  "cagr_pct": -0.5,
  "sortino": -0.06,
  "sharpe": -0.02,
  "calmar": -0.13,
  "sqn": -0.15,
  "max_consecutive_wins_loss": "5 / 6",
  "min_balance_usdt": 914.387,
  "max_balance_usdt": 1140.004,
  "absolute_drawdown_pct": 19.79,
  "market_change_pct": 630.36,
  "win_draw_loss_winpct": "41 1 54 42.7"
}
```
