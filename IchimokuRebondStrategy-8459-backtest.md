# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 8459  
**Timestamp:** 2025-09-21 21:43:05

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell buy roi",
  "random_state": 8459,
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
2025-09-21 19:42:02,456 - freqtrade - INFO - freqtrade 2025.7
2025-09-21 19:42:02,806 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-21 19:42:02,806 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-21 19:42:04,399 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-21 19:42:04,402 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-21 19:42:04,402 - freqtrade.loggers - INFO - Logfile configured
2025-09-21 19:42:04,403 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-21 19:42:04,403 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-21 19:42:04,404 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-21 19:42:04,404 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-21 19:42:04,404 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20210101-20241231 ...
2025-09-21 19:42:04,413 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-21 19:42:04,414 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-21 19:42:04,414 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-21 19:42:04,415 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-21 19:42:04,416 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-21 19:42:04,416 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20210101-20241231
2025-09-21 19:42:04,418 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-21 19:42:04,438 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-21 19:42:04,439 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 19:42:04,442 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-21 19:42:04,443 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-21 19:42:04,444 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-21 19:42:04,477 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-21 19:42:06,878 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-21 19:42:06,915 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-21 19:42:06,915 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-21 19:42:06,916 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-21 19:42:06,917 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-21 19:42:06,917 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-21 19:42:06,917 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-21 19:42:06,918 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-21 19:42:06,918 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.427, '474': 0.179, '800': 0.064, '1657': 0}
2025-09-21 19:42:06,918 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-21 19:42:06,919 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-21 19:42:06,919 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-21 19:42:06,919 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-21 19:42:06,920 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-21 19:42:06,920 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-21 19:42:06,920 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-21 19:42:06,921 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-21 19:42:06,921 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-21 19:42:06,922 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-21 19:42:06,922 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-21 19:42:06,922 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-21 19:42:06,922 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-21 19:42:06,923 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-21 19:42:06,923 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-21 19:42:06,924 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-21 19:42:06,924 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-21 19:42:06,924 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-21 19:42:06,924 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-21 19:42:06,925 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-21 19:42:06,925 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-21 19:42:06,926 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-21 19:42:06,926 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 19:42:06,931 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-21 19:42:06,964 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-21 19:42:07,183 - freqtrade.optimize.backtesting - INFO - Loading data from 2021-01-01 00:00:00 up to 2024-12-31 00:00:00 (1460 days).
2025-09-21 19:42:09,695 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-21 19:42:09,697 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-21 19:42:09,698 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-21 19:42:09,698 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.2
2025-09-21 19:42:09,699 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 0
2025-09-21 19:42:09,699 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.926
2025-09-21 19:42:09,699 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.911
2025-09-21 19:42:09,700 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.031
2025-09-21 19:42:09,700 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-21 19:42:09,700 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-21 19:42:09,701 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.998
2025-09-21 19:42:09,701 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 2
2025-09-21 19:42:09,701 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-09-21 19:42:09,702 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-21 19:42:09,702 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-21 19:42:09,702 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-21 19:42:09,703 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-21 19:42:09,705 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:42:12,600 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:42:15,449 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:42:18,260 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:42:21,082 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2021-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:42:23,994 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2021-01-01 00:00:00 up to 2024-12-31 00:00:00 (1460 days).
2025-09-21 19:43:03,731 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-21_19-43-03.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │    128 │        -0.03 │         -46.585 │        -4.66 │      5:28:00 │   61     4    63  47.7 │
│ BTC/USDT │    128 │        -0.11 │         -49.421 │        -4.94 │      5:58:00 │   59     1    68  46.1 │
│ XRP/USDT │    122 │        -0.02 │         -82.571 │        -8.26 │      5:22:00 │   53     0    69  43.4 │
│ BNB/USDT │    104 │        -0.03 │         -89.334 │        -8.93 │      5:39:00 │   43     3    58  41.3 │
│ LTC/USDT │    116 │         -0.2 │        -208.448 │       -20.84 │      5:10:00 │   47     2    67  40.5 │
│    TOTAL │    598 │        -0.08 │        -476.359 │       -47.64 │      5:32:00 │  263    10   325  44.0 │
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
│ engulfing_rebond │     598 │        -0.08 │        -476.359 │       -47.64 │      5:32:00 │  263    10   325  44.0 │
│            TOTAL │     598 │        -0.08 │        -476.359 │       -47.64 │      5:32:00 │  263    10   325  44.0 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │   255 │         1.63 │        3297.124 │       329.71 │        4:37:00 │  255     0     0   100 │
│            roi │    18 │         0.63 │          63.939 │         6.39 │ 1 day, 5:16:00 │    8    10     0   100 │
│      stop_loss │   325 │        -1.46 │       -3837.421 │      -383.74 │        4:56:00 │    0     0   325     0 │
│          TOTAL │   598 │        -0.08 │        -476.359 │       -47.64 │        5:32:00 │  263    10   325  44.0 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                            MIXED TAG STATS                                                             
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │ take_profit_1R │    255 │         1.63 │        3297.124 │       329.71 │        4:37:00 │  255     0     0   100 │
│ engulfing_rebond │            roi │     18 │         0.63 │          63.939 │         6.39 │ 1 day, 5:16:00 │    8    10     0   100 │
│ engulfing_rebond │      stop_loss │    325 │        -1.46 │       -3837.421 │      -383.74 │        4:56:00 │    0     0   325     0 │
│            TOTAL │                │    598 │        -0.08 │        -476.359 │       -47.64 │        5:32:00 │  263    10   325  44.0 │
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
│ Total/Daily Avg Trades        │ 598 / 0.41                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 523.641 USDT                   │
│ Absolute profit               │ -476.359 USDT                  │
│ Total profit %                │ -47.64%                        │
│ CAGR %                        │ -14.93%                        │
│ Sortino                       │ -0.87                          │
│ Sharpe                        │ -0.43                          │
│ Calmar                        │ -0.94                          │
│ SQN                           │ -1.35                          │
│ Profit factor                 │ 0.88                           │
│ Expectancy (Ratio)            │ -0.80 (-0.08)                  │
│ Avg. daily profit             │ -0.326 USDT                    │
│ Avg. stake amount             │ 825.373 USDT                   │
│ Total trade volume            │ 988645.307 USDT                │
│                               │                                │
│ Best Pair                     │ ETH/USDT -4.66%                │
│ Worst Pair                    │ LTC/USDT -20.84%               │
│ Best trade                    │ XRP/USDT 7.39%                 │
│ Worst trade                   │ XRP/USDT -10.29%               │
│ Best day                      │ 73.464 USDT                    │
│ Worst day                     │ -54.855 USDT                   │
│ Days win/draw/lose            │ 196 / 987 / 265                │
│ Min/Max/Avg. Duration Winners │ 0d 00:10 / 1d 03:40 / 0d 05:17 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 2d 02:10 / 0d 04:56 │
│ Max Consecutive Wins / Loss   │ 7 / 9                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 523.641 USDT                   │
│ Max balance                   │ 1566.763 USDT                  │
│ Max % of account underwater   │ 66.58%                         │
│ Absolute Drawdown (Account)   │ 66.58%                         │
│ Absolute Drawdown             │ 1043.121 USDT                  │
│ Drawdown high                 │ 566.763 USDT                   │
│ Drawdown low                  │ -476.359 USDT                  │
│ Drawdown Start                │ 2021-10-05 19:15:00            │
│ Drawdown End                  │ 2024-12-23 13:30:00            │
│ Market change                 │ 630.36%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2021-01-01 00:00:00 -> 2024-12-31 00:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                  
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃              Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    598 │        -0.08 │        -476.359 │       -47.64 │      5:32:00 │  263    10   325  44.0 │ 1043.121 USDT  66.58% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴───────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-21T21:43:05.059497",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 8459,
  "total_daily_avg_trades": "598 / 0.41",
  "absolute_profit_usdt": -476.359,
  "total_profit_pct": -47.64,
  "cagr_pct": -14.93,
  "sortino": -0.87,
  "sharpe": -0.43,
  "calmar": -0.94,
  "sqn": -1.35,
  "max_consecutive_wins_loss": "7 / 9",
  "min_balance_usdt": 523.641,
  "max_balance_usdt": 1566.763,
  "absolute_drawdown_pct": 66.58,
  "market_change_pct": 630.36,
  "win_draw_loss_winpct": "263 10 325 44.0"
}
```
