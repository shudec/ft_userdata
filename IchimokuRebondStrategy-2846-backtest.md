# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 2846  
**Timestamp:** 2025-09-23 14:49:39

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 2846,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20180101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20180101-20251231
```

## Backtesting Output
```
2025-09-23 12:43:49,045 - freqtrade - INFO - freqtrade 2025.8
2025-09-23 12:43:50,099 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-23 12:43:55,117 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-23 12:43:55,136 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-23 12:43:55,141 - freqtrade.loggers - INFO - Logfile configured
2025-09-23 12:43:55,144 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-23 12:43:55,146 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-23 12:43:55,147 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-23 12:43:55,148 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-23 12:43:55,149 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20251231 ...
2025-09-23 12:43:55,917 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-23 12:43:55,921 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-23 12:43:55,922 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-23 12:43:55,924 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-23 12:43:55,927 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-23 12:43:55,929 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20251231
2025-09-23 12:43:55,930 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-23 12:43:55,950 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-23 12:43:55,951 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 12:43:55,955 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-23 12:43:55,957 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-23 12:43:55,959 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-23 12:43:56,000 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-23 12:43:59,865 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-23 12:44:00,096 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-23 12:44:00,102 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-23 12:44:00,113 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-23 12:44:00,114 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-23 12:44:00,115 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-23 12:44:00,116 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-23 12:44:00,117 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-23 12:44:00,118 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-23 12:44:00,120 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-23 12:44:00,121 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-23 12:44:00,122 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-23 12:44:00,124 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-23 12:44:00,126 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-23 12:44:00,127 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-23 12:44:00,129 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-23 12:44:00,130 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-23 12:44:00,132 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-23 12:44:00,136 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-23 12:44:00,137 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-23 12:44:00,139 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-23 12:44:00,140 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-23 12:44:00,142 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-23 12:44:00,145 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-23 12:44:00,148 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-23 12:44:00,152 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-23 12:44:00,153 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-23 12:44:00,155 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-23 12:44:00,157 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-23 12:44:00,159 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-23 12:44:00,161 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-23 12:44:00,163 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 12:44:00,217 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-23 12:44:00,273 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-23 12:44:00,409 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:44:00,661 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:44:00,863 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:44:01,089 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-23 12:44:01,091 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:44:01,367 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:44:01,503 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 12:44:02,110 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:44:03,633 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:44:05,022 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:44:06,394 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-23 12:44:06,397 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:44:07,655 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:44:13,688 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-23 12:44:13,701 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-23 12:44:13,702 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-23 12:44:13,703 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.1
2025-09-23 12:44:13,705 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-23 12:44:13,708 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-23 12:44:13,710 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-23 12:44:13,713 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-09-23 12:44:13,715 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.8
2025-09-23 12:44:13,717 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.25
2025-09-23 12:44:13,718 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.008
2025-09-23 12:44:13,720 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-23 12:44:13,721 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-23 12:44:13,724 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1
2025-09-23 12:44:13,726 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1
2025-09-23 12:44:13,729 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-23 12:44:13,731 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 3
2025-09-23 12:44:13,732 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 1.0
2025-09-23 12:44:13,733 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-23 12:44:13,734 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-23 12:44:13,735 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-23 12:44:13,737 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-23 12:44:13,738 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-23 12:48:54,144 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 12:49:34,980 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-23_12-49-34.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │     10 │         1.47 │          86.824 │         8.68 │     10:45:00 │    4     0     6  40.0 │
│ ETH/USDT │     14 │        -0.11 │         -26.088 │        -2.61 │      7:19:00 │    4     0    10  28.6 │
│ LTC/USDT │     19 │        -0.59 │         -45.717 │        -4.57 │      9:14:00 │    4     0    15  21.1 │
│ BNB/USDT │     21 │        -0.63 │         -90.523 │        -9.05 │      6:49:00 │    3     0    18  14.3 │
│ BTC/USDT │     11 │         -1.1 │        -104.552 │       -10.46 │      9:49:00 │    2     0     9  18.2 │
│    TOTAL │     75 │        -0.31 │        -180.056 │       -18.01 │      8:29:00 │   17     0    58  22.7 │
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
│    hammer_rebond │      12 │         0.13 │         -24.651 │        -2.47 │      5:24:00 │    3     0     9  25.0 │
│ engulfing_rebond │      63 │         -0.4 │        -155.406 │       -15.54 │      9:04:00 │   14     0    49  22.2 │
│            TOTAL │      75 │        -0.31 │        -180.056 │       -18.01 │      8:29:00 │   17     0    58  22.7 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │    14 │         5.11 │         502.819 │        50.28 │      7:26:00 │   14     0     0   100 │
│    exit_signal │    29 │         -0.9 │        -173.641 │       -17.36 │     14:23:00 │    3     0    26  10.3 │
│      stop_loss │    32 │        -2.15 │        -509.234 │       -50.92 │      3:36:00 │    0     0    32     0 │
│          TOTAL │    75 │        -0.31 │        -180.056 │       -18.01 │      8:29:00 │   17     0    58  22.7 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                           MIXED TAG STATS                                                            
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │ take_profit_2R │     11 │         4.91 │         390.779 │        39.08 │      8:00:00 │   11     0     0   100 │
│    hammer_rebond │ take_profit_2R │      3 │         5.84 │         112.041 │         11.2 │      5:22:00 │    3     0     0   100 │
│    hammer_rebond │    exit_signal │      3 │        -0.96 │         -25.406 │        -2.54 │      6:40:00 │    0     0     3     0 │
│    hammer_rebond │      stop_loss │      6 │        -2.18 │        -111.285 │       -11.13 │      4:48:00 │    0     0     6     0 │
│ engulfing_rebond │    exit_signal │     26 │        -0.89 │        -148.235 │       -14.82 │     15:16:00 │    3     0    23  11.5 │
│ engulfing_rebond │      stop_loss │     26 │        -2.14 │        -397.949 │       -39.79 │      3:20:00 │    0     0    26     0 │
│            TOTAL │                │     75 │        -0.31 │        -180.056 │       -18.01 │      8:29:00 │   17     0    58  22.7 │
└──────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2018-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 75 / 0.03                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 819.944 USDT                   │
│ Absolute profit               │ -180.056 USDT                  │
│ Total profit %                │ -18.01%                        │
│ CAGR %                        │ -2.55%                         │
│ Sortino                       │ -0.17                          │
│ Sharpe                        │ -0.06                          │
│ Calmar                        │ -0.47                          │
│ SQN                           │ -1.03                          │
│ Profit factor                 │ 0.74                           │
│ Expectancy (Ratio)            │ -2.40 (-0.20)                  │
│ Avg. daily profit             │ -0.064 USDT                    │
│ Avg. stake amount             │ 785.042 USDT                   │
│ Total trade volume            │ 117811.637 USDT                │
│                               │                                │
│ Best Pair                     │ XRP/USDT 8.68%                 │
│ Worst Pair                    │ BTC/USDT -10.46%               │
│ Best trade                    │ LTC/USDT 9.10%                 │
│ Worst trade                   │ LTC/USDT -4.29%                │
│ Best day                      │ 52.213 USDT                    │
│ Worst day                     │ -26.34 USDT                    │
│ Days win/draw/lose            │ 17 / 2626 / 53                 │
│ Min/Max/Avg. Duration Winners │ 0d 00:20 / 1d 05:05 / 0d 10:11 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 1d 07:00 / 0d 07:59 │
│ Max Consecutive Wins / Loss   │ 2 / 15                         │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 803.965 USDT                   │
│ Max balance                   │ 1089.574 USDT                  │
│ Max % of account underwater   │ 26.21%                         │
│ Absolute drawdown             │ 285.609 USDT (26.21%)          │
│ Drawdown duration             │ 1818 days 15:00:00             │
│ Profit at drawdown start      │ 89.574 USDT                    │
│ Profit at drawdown end        │ -196.035 USDT                  │
│ Drawdown start                │ 2020-02-09 04:00:00            │
│ Drawdown end                  │ 2025-01-31 19:00:00            │
│ Market change                 │ 2372.94%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     75 │        -0.31 │        -180.056 │       -18.01 │      8:29:00 │   17     0    58  22.7 │ 285.609 USDT  26.21% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-23T14:49:39.035119",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 2846,
  "total_daily_avg_trades": "75 / 0.03",
  "absolute_profit_usdt": -180.056,
  "total_profit_pct": -18.01,
  "cagr_pct": -2.55,
  "sortino": -0.17,
  "sharpe": -0.06,
  "calmar": -0.47,
  "sqn": -1.03,
  "max_consecutive_wins_loss": "2 / 15",
  "min_balance_usdt": 803.965,
  "max_balance_usdt": 1089.574,
  "absolute_drawdown_pct": 26.21,
  "market_change_pct": 2372.94,
  "win_draw_loss_winpct": "17 0 58 22.7"
}
```
