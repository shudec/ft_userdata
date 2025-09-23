# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 2461  
**Timestamp:** 2025-09-23 13:56:10

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 2461,
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
2025-09-23 11:52:57,530 - freqtrade - INFO - freqtrade 2025.8
2025-09-23 11:52:58,253 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-23 11:53:01,390 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-23 11:53:01,397 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-23 11:53:01,398 - freqtrade.loggers - INFO - Logfile configured
2025-09-23 11:53:01,398 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-23 11:53:01,399 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-23 11:53:01,399 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-23 11:53:01,401 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-23 11:53:01,401 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20251231 ...
2025-09-23 11:53:01,802 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-23 11:53:01,805 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-23 11:53:01,806 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-23 11:53:01,806 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-23 11:53:01,807 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-23 11:53:01,808 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20251231
2025-09-23 11:53:01,809 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-23 11:53:01,821 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-23 11:53:01,821 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 11:53:01,826 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-23 11:53:01,827 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-23 11:53:01,828 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-23 11:53:01,849 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-23 11:53:04,413 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-23 11:53:04,537 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-23 11:53:04,540 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-23 11:53:04,545 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-23 11:53:04,546 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-23 11:53:04,547 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-23 11:53:04,547 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-23 11:53:04,548 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-23 11:53:04,548 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-23 11:53:04,549 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-23 11:53:04,549 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-23 11:53:04,550 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-23 11:53:04,551 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-23 11:53:04,551 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-23 11:53:04,552 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-23 11:53:04,553 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-23 11:53:04,553 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-23 11:53:04,554 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-23 11:53:04,555 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-23 11:53:04,555 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-23 11:53:04,556 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-23 11:53:04,556 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-23 11:53:04,557 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-23 11:53:04,558 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-23 11:53:04,559 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-23 11:53:04,559 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-23 11:53:04,560 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-23 11:53:04,561 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-23 11:53:04,562 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-23 11:53:04,562 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-23 11:53:04,563 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-23 11:53:04,564 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 11:53:04,594 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-23 11:53:04,623 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-23 11:53:04,693 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 11:53:04,809 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 11:53:04,893 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 11:53:04,973 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-23 11:53:04,973 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 11:53:05,043 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 11:53:05,081 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 11:53:05,349 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 11:53:06,148 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 11:53:06,879 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 11:53:07,581 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-23 11:53:07,581 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 11:53:08,277 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 11:53:11,241 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-23 11:53:11,247 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-23 11:53:11,247 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-23 11:53:11,248 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.1
2025-09-23 11:53:11,249 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-23 11:53:11,249 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = True
2025-09-23 11:53:11,250 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-23 11:53:11,250 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-09-23 11:53:11,251 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.811
2025-09-23 11:53:11,252 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.28
2025-09-23 11:53:11,252 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.008
2025-09-23 11:53:11,252 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-23 11:53:11,253 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-23 11:53:11,253 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-23 11:53:11,254 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1
2025-09-23 11:53:11,254 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-23 11:53:11,255 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 3
2025-09-23 11:53:11,255 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 1.0
2025-09-23 11:53:11,256 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-23 11:53:11,256 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-23 11:53:11,257 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-23 11:53:11,257 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-23 11:53:11,257 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-23 11:55:24,238 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 11:56:08,846 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-23_11-56-08.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ LTC/USDT │     53 │         0.27 │          98.585 │         9.86 │     11:09:00 │   21     0    32  39.6 │
│ XRP/USDT │     39 │         0.49 │          84.958 │          8.5 │     14:06:00 │   13     0    26  33.3 │
│ BTC/USDT │     56 │         0.04 │          -3.974 │         -0.4 │     12:17:00 │   20     0    36  35.7 │
│ BNB/USDT │     54 │        -0.33 │        -218.607 │       -21.86 │     12:51:00 │   11     0    43  20.4 │
│ ETH/USDT │     41 │        -0.59 │        -264.134 │       -26.41 │      8:55:00 │    9     0    32  22.0 │
│    TOTAL │    243 │        -0.02 │        -303.171 │       -30.32 │     11:53:00 │   74     0   169  30.5 │
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
│ engulfing_rebond │     162 │         0.04 │        -141.715 │       -14.17 │     14:47:00 │   49     0   113  30.2 │
│    hammer_rebond │      81 │        -0.16 │        -161.456 │       -16.15 │      6:04:00 │   25     0    56  30.9 │
│            TOTAL │     243 │        -0.02 │        -303.171 │       -30.32 │     11:53:00 │   74     0   169  30.5 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │    74 │         3.93 │        2156.000 │        215.6 │     18:37:00 │   74     0     0   100 │
│      stop_loss │   169 │        -1.76 │       -2459.171 │      -245.92 │      8:56:00 │    0     0   169     0 │
│          TOTAL │   243 │        -0.02 │        -303.171 │       -30.32 │     11:53:00 │   74     0   169  30.5 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                            MIXED TAG STATS                                                             
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │ take_profit_2R │     49 │         4.36 │        1448.836 │       144.88 │ 1 day, 1:14:00 │   49     0     0   100 │
│    hammer_rebond │ take_profit_2R │     25 │         3.08 │         707.165 │        70.72 │        5:38:00 │   25     0     0   100 │
│    hammer_rebond │      stop_loss │     56 │         -1.6 │        -868.621 │       -86.86 │        6:16:00 │    0     0    56     0 │
│ engulfing_rebond │      stop_loss │    113 │        -1.83 │       -1590.551 │      -159.06 │       10:16:00 │    0     0   113     0 │
│            TOTAL │                │    243 │        -0.02 │        -303.171 │       -30.32 │       11:53:00 │   74     0   169  30.5 │
└──────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2018-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 243 / 0.09                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 696.829 USDT                   │
│ Absolute profit               │ -303.171 USDT                  │
│ Total profit %                │ -30.32%                        │
│ CAGR %                        │ -4.59%                         │
│ Sortino                       │ -0.32                          │
│ Sharpe                        │ -0.09                          │
│ Calmar                        │ -0.43                          │
│ SQN                           │ -0.89                          │
│ Profit factor                 │ 0.88                           │
│ Expectancy (Ratio)            │ -1.25 (-0.09)                  │
│ Avg. daily profit             │ -0.108 USDT                    │
│ Avg. stake amount             │ 858.965 USDT                   │
│ Total trade volume            │ 417989.172 USDT                │
│                               │                                │
│ Best Pair                     │ LTC/USDT 9.86%                 │
│ Worst Pair                    │ ETH/USDT -26.41%               │
│ Best trade                    │ BNB/USDT 13.11%                │
│ Worst trade                   │ LTC/USDT -6.89%                │
│ Best day                      │ 71.813 USDT                    │
│ Worst day                     │ -43.023 USDT                   │
│ Days win/draw/lose            │ 73 / 2569 / 157                │
│ Min/Max/Avg. Duration Winners │ 0d 00:20 / 6d 11:50 / 0d 18:37 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 2d 17:50 / 0d 08:56 │
│ Max Consecutive Wins / Loss   │ 3 / 12                         │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 645.339 USDT                   │
│ Max balance                   │ 1251.624 USDT                  │
│ Max % of account underwater   │ 48.44%                         │
│ Absolute drawdown             │ 606.285 USDT (48.44%)          │
│ Drawdown duration             │ 1803 days 10:25:00             │
│ Profit at drawdown start      │ 251.624 USDT                   │
│ Profit at drawdown end        │ -354.661 USDT                  │
│ Drawdown start                │ 2020-02-12 11:00:00            │
│ Drawdown end                  │ 2025-01-19 21:25:00            │
│ Market change                 │ 2372.94%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    243 │        -0.02 │        -303.171 │       -30.32 │     11:53:00 │   74     0   169  30.5 │ 606.285 USDT  48.44% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-23T13:56:10.752571",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 2461,
  "total_daily_avg_trades": "243 / 0.09",
  "absolute_profit_usdt": -303.171,
  "total_profit_pct": -30.32,
  "cagr_pct": -4.59,
  "sortino": -0.32,
  "sharpe": -0.09,
  "calmar": -0.43,
  "sqn": -0.89,
  "max_consecutive_wins_loss": "3 / 12",
  "min_balance_usdt": 645.339,
  "max_balance_usdt": 1251.624,
  "absolute_drawdown_pct": 48.44,
  "market_change_pct": 2372.94,
  "win_draw_loss_winpct": "74 0 169 30.5"
}
```
