# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 8573  
**Timestamp:** 2025-09-23 13:21:06

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 8573,
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
2025-09-23 11:18:07,768 - freqtrade - INFO - freqtrade 2025.8
2025-09-23 11:18:08,184 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-23 11:18:09,896 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-23 11:18:09,903 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-23 11:18:09,904 - freqtrade.loggers - INFO - Logfile configured
2025-09-23 11:18:09,904 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-23 11:18:09,905 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-23 11:18:09,905 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-23 11:18:09,906 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-23 11:18:09,906 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20251231 ...
2025-09-23 11:18:10,337 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-23 11:18:10,339 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-23 11:18:10,339 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-23 11:18:10,340 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-23 11:18:10,340 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-23 11:18:10,341 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20251231
2025-09-23 11:18:10,342 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-23 11:18:10,355 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-23 11:18:10,356 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 11:18:10,358 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-23 11:18:10,359 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-23 11:18:10,361 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-23 11:18:10,388 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-23 11:18:12,874 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-23 11:18:12,967 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-23 11:18:12,970 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-23 11:18:12,974 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-23 11:18:12,975 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-23 11:18:12,975 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-23 11:18:12,975 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-23 11:18:12,976 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-23 11:18:12,976 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-23 11:18:12,977 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-23 11:18:12,978 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-23 11:18:12,978 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-23 11:18:12,979 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-23 11:18:12,979 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-23 11:18:12,980 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-23 11:18:12,980 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-23 11:18:12,981 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-23 11:18:12,981 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-23 11:18:12,982 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-23 11:18:12,982 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-23 11:18:12,983 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-23 11:18:12,983 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-23 11:18:12,984 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-23 11:18:12,984 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-23 11:18:12,985 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-23 11:18:12,985 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-23 11:18:12,986 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-23 11:18:12,986 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-23 11:18:12,987 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-23 11:18:12,987 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-23 11:18:12,988 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-23 11:18:12,988 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 11:18:13,010 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-23 11:18:13,036 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-23 11:18:13,091 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 11:18:13,200 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 11:18:13,273 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 11:18:13,343 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-23 11:18:13,344 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 11:18:13,411 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 11:18:13,451 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 11:18:13,705 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 11:18:14,322 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 11:18:15,009 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 11:18:15,751 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-23 11:18:15,752 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 11:18:16,398 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 11:18:19,301 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-23 11:18:19,308 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-23 11:18:19,309 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-23 11:18:19,310 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.1
2025-09-23 11:18:19,310 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-23 11:18:19,311 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = True
2025-09-23 11:18:19,312 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-23 11:18:19,312 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-09-23 11:18:19,313 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.811
2025-09-23 11:18:19,313 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.28
2025-09-23 11:18:19,314 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.008
2025-09-23 11:18:19,314 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-23 11:18:19,315 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-23 11:18:19,316 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-23 11:18:19,318 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 2
2025-09-23 11:18:19,319 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-23 11:18:19,321 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 3
2025-09-23 11:18:19,323 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 1.0
2025-09-23 11:18:19,324 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-23 11:18:19,325 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-23 11:18:19,326 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower
2025-09-23 11:18:19,326 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-23 11:18:19,327 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-23 11:18:19,333 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 11:18:19,356 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 11:18:40,259 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 11:18:40,276 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 11:19:02,307 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 11:19:02,330 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 11:19:28,276 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 11:19:28,294 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-23 11:19:28,295 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 11:19:49,178 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 11:19:49,199 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 11:20:18,705 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 11:21:05,279 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-23_11-21-05.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ LTC/USDT │     55 │         0.29 │         117.484 │        11.75 │     10:19:00 │   23     0    32  41.8 │
│ XRP/USDT │     40 │         0.54 │         111.461 │        11.15 │     12:38:00 │   15     0    25  37.5 │
│ BTC/USDT │     58 │         0.13 │          53.038 │          5.3 │     14:10:00 │   22     0    36  37.9 │
│ BNB/USDT │     54 │        -0.23 │        -200.877 │       -20.09 │     12:59:00 │   12     0    42  22.2 │
│ ETH/USDT │     41 │        -0.49 │        -230.340 │       -23.03 │      7:35:00 │   10     0    31  24.4 │
│    TOTAL │    248 │         0.05 │        -149.233 │       -14.92 │     11:43:00 │   82     0   166  33.1 │
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
│    hammer_rebond │      83 │         0.06 │          16.650 │         1.67 │      4:31:00 │   32     0    51  38.6 │
│ engulfing_rebond │     165 │         0.05 │        -165.884 │       -16.59 │     15:20:00 │   50     0   115  30.3 │
│            TOTAL │     248 │         0.05 │        -149.233 │       -14.92 │     11:43:00 │   82     0   166  33.1 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │    82 │          3.5 │        2288.988 │        228.9 │     18:47:00 │   82     0     0   100 │
│      stop_loss │   166 │        -1.65 │       -2438.221 │      -243.82 │      8:14:00 │    0     0   166     0 │
│          TOTAL │   248 │         0.05 │        -149.233 │       -14.92 │     11:43:00 │   82     0   166  33.1 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                            MIXED TAG STATS                                                             
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │ take_profit_2R │     50 │         4.27 │        1564.667 │       156.47 │ 1 day, 4:00:00 │   50     0     0   100 │
│    hammer_rebond │ take_profit_2R │     32 │          2.3 │         724.321 │        72.43 │        4:23:00 │   32     0     0   100 │
│    hammer_rebond │      stop_loss │     51 │        -1.35 │        -707.670 │       -70.77 │        4:36:00 │    0     0    51     0 │
│ engulfing_rebond │      stop_loss │    115 │        -1.78 │       -1730.551 │      -173.06 │        9:50:00 │    0     0   115     0 │
│            TOTAL │                │    248 │         0.05 │        -149.233 │       -14.92 │       11:43:00 │   82     0   166  33.1 │
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
│ Total/Daily Avg Trades        │ 248 / 0.09                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 850.767 USDT                   │
│ Absolute profit               │ -149.233 USDT                  │
│ Total profit %                │ -14.92%                        │
│ CAGR %                        │ -2.08%                         │
│ Sortino                       │ -0.16                          │
│ Sharpe                        │ -0.05                          │
│ Calmar                        │ -0.26                          │
│ SQN                           │ -0.43                          │
│ Profit factor                 │ 0.94                           │
│ Expectancy (Ratio)            │ -0.60 (-0.04)                  │
│ Avg. daily profit             │ -0.053 USDT                    │
│ Avg. stake amount             │ 933.552 USDT                   │
│ Total trade volume            │ 463819.456 USDT                │
│                               │                                │
│ Best Pair                     │ LTC/USDT 11.75%                │
│ Worst Pair                    │ ETH/USDT -23.03%               │
│ Best trade                    │ BNB/USDT 13.11%                │
│ Worst trade                   │ LTC/USDT -6.89%                │
│ Best day                      │ 70.797 USDT                    │
│ Worst day                     │ -39.093 USDT                   │
│ Days win/draw/lose            │ 79 / 2568 / 152                │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 7d 23:10 / 0d 18:47 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 2d 17:50 / 0d 08:14 │
│ Max Consecutive Wins / Loss   │ 5 / 12                         │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 775.604 USDT                   │
│ Max balance                   │ 1276.533 USDT                  │
│ Max % of account underwater   │ 39.24%                         │
│ Absolute drawdown             │ 500.929 USDT (39.24%)          │
│ Drawdown duration             │ 1803 days 10:25:00             │
│ Profit at drawdown start      │ 276.533 USDT                   │
│ Profit at drawdown end        │ -224.396 USDT                  │
│ Drawdown start                │ 2020-02-12 11:00:00            │
│ Drawdown end                  │ 2025-01-19 21:25:00            │
│ Market change                 │ 2372.94%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    248 │         0.05 │        -149.233 │       -14.92 │     11:43:00 │   82     0   166  33.1 │ 500.929 USDT  39.24% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-23T13:21:06.762222",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 8573,
  "total_daily_avg_trades": "248 / 0.09",
  "absolute_profit_usdt": -149.233,
  "total_profit_pct": -14.92,
  "cagr_pct": -2.08,
  "sortino": -0.16,
  "sharpe": -0.05,
  "calmar": -0.26,
  "sqn": -0.43,
  "max_consecutive_wins_loss": "5 / 12",
  "min_balance_usdt": 775.604,
  "max_balance_usdt": 1276.533,
  "absolute_drawdown_pct": 39.24,
  "market_change_pct": 2372.94,
  "win_draw_loss_winpct": "82 0 166 33.1"
}
```
