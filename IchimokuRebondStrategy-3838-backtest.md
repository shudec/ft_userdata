# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 3838  
**Timestamp:** 2025-09-22 17:29:53

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 3838,
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
2025-09-22 15:26:54,705 - freqtrade - INFO - freqtrade 2025.8
2025-09-22 15:26:54,995 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-22 15:26:56,383 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-22 15:26:56,390 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-22 15:26:56,391 - freqtrade.loggers - INFO - Logfile configured
2025-09-22 15:26:56,391 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-22 15:26:56,391 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-22 15:26:56,392 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-22 15:26:56,392 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-22 15:26:56,393 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20251231 ...
2025-09-22 15:26:56,660 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-22 15:26:56,662 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-22 15:26:56,663 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-22 15:26:56,663 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-22 15:26:56,664 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-22 15:26:56,664 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20251231
2025-09-22 15:26:56,665 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-22 15:26:56,674 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-22 15:26:56,675 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-22 15:26:56,677 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-22 15:26:56,678 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-22 15:26:56,679 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-22 15:26:56,699 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-22 15:27:00,702 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-22 15:27:00,791 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-22 15:27:00,794 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-22 15:27:00,798 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-22 15:27:00,798 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-22 15:27:00,799 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-22 15:27:00,799 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-22 15:27:00,799 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-22 15:27:00,800 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-22 15:27:00,800 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-22 15:27:00,800 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-22 15:27:00,801 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-22 15:27:00,801 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-22 15:27:00,802 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-22 15:27:00,802 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-22 15:27:00,803 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-22 15:27:00,803 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-22 15:27:00,803 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-22 15:27:00,804 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-22 15:27:00,804 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-22 15:27:00,804 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-22 15:27:00,805 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-22 15:27:00,805 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-22 15:27:00,806 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-22 15:27:00,806 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-22 15:27:00,807 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-22 15:27:00,807 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-22 15:27:00,807 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-22 15:27:00,807 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-22 15:27:00,808 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-22 15:27:00,808 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-22 15:27:00,808 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-22 15:27:00,824 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-22 15:27:00,846 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-22 15:27:00,895 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 15:27:00,970 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 15:27:01,032 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 15:27:01,102 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-22 15:27:01,103 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 15:27:01,172 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 15:27:01,207 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-22 15:27:01,422 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 15:27:01,991 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 15:27:02,515 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 15:27:03,041 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-22 15:27:03,042 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 15:27:03,554 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 15:27:05,932 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-22 15:27:05,937 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-22 15:27:05,938 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-22 15:27:05,938 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.193
2025-09-22 15:27:05,939 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-22 15:27:05,940 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = True
2025-09-22 15:27:05,940 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-22 15:27:05,941 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 0
2025-09-22 15:27:05,941 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.652
2025-09-22 15:27:05,941 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.956
2025-09-22 15:27:05,942 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.001
2025-09-22 15:27:05,942 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-22 15:27:05,943 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-22 15:27:05,943 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-22 15:27:05,944 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 9
2025-09-22 15:27:05,944 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.99
2025-09-22 15:27:05,945 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-22 15:27:05,945 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-22 15:27:05,946 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-22 15:27:05,946 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-22 15:27:05,949 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 15:27:05,971 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 15:27:20,150 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 15:27:20,165 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 15:27:32,947 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 15:27:32,963 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 15:27:45,984 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 15:27:45,998 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-22 15:27:45,998 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 15:27:57,918 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 15:27:57,935 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 15:28:11,809 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-22 15:29:51,854 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-22_15-29-51.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │     87 │         0.49 │          94.971 │          9.5 │     13:45:00 │   29     0    58  33.3 │
│ BTC/USDT │    145 │         0.26 │          72.997 │          7.3 │     17:12:00 │   44     0   101  30.3 │
│ LTC/USDT │     95 │        -0.07 │          -0.982 │         -0.1 │     14:45:00 │   28     0    67  29.5 │
│ BNB/USDT │    130 │        -0.06 │         -25.280 │        -2.53 │     14:26:00 │   36     0    94  27.7 │
│ ETH/USDT │    109 │        -0.18 │         -41.255 │        -4.13 │     15:21:00 │   32     0    77  29.4 │
│    TOTAL │    566 │         0.08 │         100.452 │        10.05 │     15:16:00 │  169     0   397  29.9 │
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
│    hammer_rebond │     184 │         0.51 │         184.608 │        18.46 │     14:29:00 │   60     0   124  32.6 │
│ engulfing_rebond │     382 │        -0.13 │         -84.156 │        -8.42 │     15:39:00 │  109     0   273  28.5 │
│            TOTAL │     566 │         0.08 │         100.452 │        10.05 │     15:16:00 │  169     0   397  29.9 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │    38 │        10.49 │         840.283 │        84.03 │ 1 day, 0:31:00 │   38     0     0   100 │
│    exit_signal │   528 │        -0.67 │        -739.831 │       -73.98 │       14:36:00 │  131     0   397  24.8 │
│          TOTAL │   566 │         0.08 │         100.452 │        10.05 │       15:16:00 │  169     0   397  29.9 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                            MIXED TAG STATS                                                             
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │ take_profit_1R │     21 │        10.43 │         467.244 │        46.72 │ 1 day, 1:06:00 │   21     0     0   100 │
│    hammer_rebond │ take_profit_1R │     17 │        10.56 │         373.039 │         37.3 │       23:48:00 │   17     0     0   100 │
│    hammer_rebond │    exit_signal │    167 │        -0.51 │        -188.431 │       -18.84 │       13:32:00 │   43     0   124  25.7 │
│ engulfing_rebond │    exit_signal │    361 │        -0.74 │        -551.400 │       -55.14 │       15:06:00 │   88     0   273  24.4 │
│            TOTAL │                │    566 │         0.08 │         100.452 │        10.05 │       15:16:00 │  169     0   397  29.9 │
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
│ Total/Daily Avg Trades        │ 566 / 0.2                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1100.452 USDT                  │
│ Absolute profit               │ 100.452 USDT                   │
│ Total profit %                │ 10.05%                         │
│ CAGR %                        │ 1.25%                          │
│ Sortino                       │ 0.27                           │
│ Sharpe                        │ 0.10                           │
│ Calmar                        │ 0.37                           │
│ SQN                           │ 0.60                           │
│ Profit factor                 │ 1.08                           │
│ Expectancy (Ratio)            │ 0.18 (0.06)                    │
│ Avg. daily profit             │ 0.036 USDT                     │
│ Avg. stake amount             │ 206.073 USDT                   │
│ Total trade volume            │ 233842.403 USDT                │
│                               │                                │
│ Best Pair                     │ XRP/USDT 9.50%                 │
│ Worst Pair                    │ ETH/USDT -4.13%                │
│ Best trade                    │ LTC/USDT 12.02%                │
│ Worst trade                   │ LTC/USDT -7.75%                │
│ Best day                      │ 39.494 USDT                    │
│ Worst day                     │ -17.562 USDT                   │
│ Days win/draw/lose            │ 135 / 2331 / 315               │
│ Min/Max/Avg. Duration Winners │ 0d 02:40 / 3d 02:00 / 1d 02:43 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 1d 21:00 / 0d 10:23 │
│ Max Consecutive Wins / Loss   │ 6 / 23                         │
│ Rejected Entry signals        │ 48                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 986.239 USDT                   │
│ Max balance                   │ 1249.024 USDT                  │
│ Max % of account underwater   │ 18.42%                         │
│ Absolute drawdown             │ 230.123 USDT (18.42%)          │
│ Drawdown duration             │ 1533 days 11:15:00             │
│ Profit at drawdown start      │ 249.024 USDT                   │
│ Profit at drawdown end        │ 18.902 USDT                    │
│ Drawdown start                │ 2020-04-29 16:45:00            │
│ Drawdown end                  │ 2024-07-11 04:00:00            │
│ Market change                 │ 2372.94%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    566 │         0.08 │         100.452 │        10.05 │     15:16:00 │  169     0   397  29.9 │ 230.123 USDT  18.42% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-22T17:29:53.437773",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 3838,
  "total_daily_avg_trades": "566 / 0.2",
  "absolute_profit_usdt": 100.452,
  "total_profit_pct": 10.05,
  "cagr_pct": 1.25,
  "sortino": 0.27,
  "sharpe": 0.1,
  "calmar": 0.37,
  "sqn": 0.6,
  "max_consecutive_wins_loss": "6 / 23",
  "min_balance_usdt": 986.239,
  "max_balance_usdt": 1249.024,
  "market_change_pct": 2372.94,
  "win_draw_loss_winpct": "169 0 397 29.9"
}
```
