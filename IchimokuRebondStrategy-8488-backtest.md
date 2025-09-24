# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 8488  
**Timestamp:** 2025-09-24 13:54:23

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 8488,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20200101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20200101-20251231
```

## Backtesting Output
```
2025-09-24 11:46:52,130 - freqtrade - INFO - freqtrade 2025.8
2025-09-24 11:46:52,658 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-24 11:46:55,313 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-24 11:46:55,319 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-24 11:46:55,320 - freqtrade.loggers - INFO - Logfile configured
2025-09-24 11:46:55,320 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-24 11:46:55,321 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-24 11:46:55,321 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-24 11:46:55,322 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-24 11:46:55,323 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20200101-20251231 ...
2025-09-24 11:46:55,856 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-24 11:46:55,858 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-24 11:46:55,859 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-24 11:46:55,859 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-24 11:46:55,860 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-24 11:46:55,861 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20200101-20251231
2025-09-24 11:46:55,862 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-24 11:46:55,876 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-24 11:46:55,878 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 11:46:55,881 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-24 11:46:55,882 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-24 11:46:55,883 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-24 11:46:55,908 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-24 11:46:58,202 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-24 11:46:58,321 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-24 11:46:58,324 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-24 11:46:58,330 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-24 11:46:58,332 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-24 11:46:58,332 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-24 11:46:58,333 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-24 11:46:58,333 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-24 11:46:58,334 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-24 11:46:58,335 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-24 11:46:58,335 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-24 11:46:58,336 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-24 11:46:58,336 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-24 11:46:58,336 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-24 11:46:58,337 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-24 11:46:58,337 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-24 11:46:58,338 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-24 11:46:58,338 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-24 11:46:58,339 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-24 11:46:58,339 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-24 11:46:58,339 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-24 11:46:58,340 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-24 11:46:58,340 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-24 11:46:58,341 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-24 11:46:58,341 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-24 11:46:58,342 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-24 11:46:58,342 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-24 11:46:58,342 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-24 11:46:58,343 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-24 11:46:58,344 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-24 11:46:58,345 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-24 11:46:58,345 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 11:46:58,372 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-24 11:46:58,399 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-24 11:46:58,455 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 11:46:58,537 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 11:46:58,616 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 11:46:58,690 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 11:46:58,766 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 11:46:58,810 - freqtrade.optimize.backtesting - INFO - Loading data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 11:46:59,116 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 11:46:59,632 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 11:47:00,149 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 11:47:00,656 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 11:47:01,220 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 11:47:03,081 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-24 11:47:03,088 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-24 11:47:03,088 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-24 11:47:03,089 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-24 11:47:03,089 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-24 11:47:03,090 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-24 11:47:03,090 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-24 11:47:03,091 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_adx_threshold = 20
2025-09-24 11:47:03,091 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-24 11:47:03,092 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-24 11:47:03,092 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-24 11:47:03,093 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-24 11:47:03,093 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-24 11:47:03,094 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-09-24 11:47:03,094 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-09-24 11:47:03,094 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-24 11:47:03,095 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-24 11:47:03,095 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-24 11:47:03,096 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-24 11:47:03,096 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): custom_sell_atr_factor = 4.5
2025-09-24 11:47:03,097 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-24 11:47:03,097 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 8
2025-09-24 11:47:03,098 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-24 11:47:03,098 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-24 11:47:03,098 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-24 11:47:03,099 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-24 11:47:03,099 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_sell_ichimoku_cloud_signal = True
2025-09-24 11:47:03,099 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_sell_ichimoku_futur_cloud_signal = False
2025-09-24 11:47:03,100 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_sell_kinjun_signal = False
2025-09-24 11:47:03,100 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-24 11:47:03,101 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-24 11:47:03,104 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 11:47:03,122 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 11:47:03,141 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 11:47:03,165 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 11:47:19,787 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 11:47:19,803 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 11:47:19,818 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 11:47:19,841 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 11:47:36,228 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 11:47:36,244 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 11:47:36,259 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 11:47:36,283 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-15 00:00:00
2025-09-24 11:47:51,880 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 11:47:51,897 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 11:47:51,914 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 11:47:51,937 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 11:48:06,595 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 11:48:06,611 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 11:48:06,627 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 11:48:06,649 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 11:48:21,865 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 11:54:21,913 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-24_11-54-21.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │    121 │         1.74 │        1209.758 │       120.98 │ 2 days, 17:05:00 │   55     0    66  45.5 │
│ BTC/USDT │    132 │         1.09 │         881.223 │        88.12 │ 2 days, 18:19:00 │   60     0    72  45.5 │
│ BNB/USDT │    107 │         0.74 │         269.039 │         26.9 │  2 days, 8:30:00 │   36     0    71  33.6 │
│ XRP/USDT │     88 │         0.84 │          12.432 │         1.24 │  1 day, 23:21:00 │   16     0    72  18.2 │
│ LTC/USDT │     94 │        -0.24 │        -100.254 │       -10.03 │  2 days, 4:03:00 │   30     0    64  31.9 │
│    TOTAL │    542 │         0.89 │        2272.197 │       227.22 │ 2 days, 10:33:00 │  197     0   345  36.3 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         2.39 │          38.324 │         3.83 │ 3 days, 20:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         2.39 │          38.324 │         3.83 │ 3 days, 20:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                        ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │     414 │         1.04 │        2034.252 │       203.43 │ 2 days, 11:27:00 │  155     0   259  37.4 │
│         hammer_rebond │      75 │         0.56 │         154.308 │        15.43 │  2 days, 6:32:00 │   24     0    51  32.0 │
│      engulfing_rebond │      53 │         0.26 │          83.636 │         8.36 │  2 days, 9:10:00 │   18     0    35  34.0 │
│                 TOTAL │     542 │         0.89 │        2272.197 │       227.22 │ 2 days, 10:33:00 │  197     0   345  36.3 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                         EXIT REASON STATS                                                         
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                 Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│              take_profit_3R │    52 │        17.61 │        5400.797 │       540.08 │ 3 days, 17:29:00 │   52     0     0   100 │
│                  force_exit │     1 │         2.39 │          38.324 │         3.83 │ 3 days, 20:00:00 │    1     0     0   100 │
│                   stop_loss │    31 │        -5.65 │       -1255.191 │      -125.52 │         18:42:00 │    0     0    31     0 │
│ ichimoku_cloud_crossed_exit │   458 │        -0.56 │       -1911.734 │      -191.17 │  2 days, 9:40:00 │  144     0   314  31.4 │
│                       TOTAL │   542 │         0.89 │        2272.197 │       227.22 │ 2 days, 10:33:00 │  197     0   345  36.3 │
└─────────────────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                                      MIXED TAG STATS                                                                       
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃                 Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │              take_profit_3R │     43 │        17.75 │        4459.896 │       445.99 │ 3 days, 17:56:00 │   43     0     0   100 │
│         hammer_rebond │              take_profit_3R │      5 │        17.94 │         607.566 │        60.76 │ 3 days, 19:27:00 │    5     0     0   100 │
│      engulfing_rebond │              take_profit_3R │      4 │        15.65 │         333.335 │        33.33 │ 3 days, 10:11:00 │    4     0     0   100 │
│ strong_bullish_rebond │                  force_exit │      1 │         2.39 │          38.324 │         3.83 │ 3 days, 20:00:00 │    1     0     0   100 │
│      engulfing_rebond │ ichimoku_cloud_crossed_exit │     46 │        -0.62 │        -117.088 │       -11.71 │  2 days, 9:52:00 │   14     0    32  30.4 │
│         hammer_rebond │                   stop_loss │      3 │        -5.31 │        -119.892 │       -11.99 │         10:38:00 │    0     0     3     0 │
│      engulfing_rebond │                   stop_loss │      3 │        -6.83 │        -132.611 │       -13.26 │         12:57:00 │    0     0     3     0 │
│         hammer_rebond │ ichimoku_cloud_crossed_exit │     67 │        -0.48 │        -333.367 │       -33.34 │  2 days, 5:45:00 │   19     0    48  28.4 │
│ strong_bullish_rebond │                   stop_loss │     25 │        -5.55 │       -1002.689 │      -100.27 │         20:21:00 │    0     0    25     0 │
│ strong_bullish_rebond │ ichimoku_cloud_crossed_exit │    345 │        -0.57 │       -1461.279 │      -146.13 │ 2 days, 10:24:00 │  111     0   234  32.2 │
│                 TOTAL │                             │    542 │         0.89 │        2272.197 │       227.22 │ 2 days, 10:33:00 │  197     0   345  36.3 │
└───────────────────────┴─────────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2020-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 542 / 0.26                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 3272.197 USDT                  │
│ Absolute profit               │ 2272.197 USDT                  │
│ Total profit %                │ 227.22%                        │
│ CAGR %                        │ 23.14%                         │
│ Sortino                       │ 1.47                           │
│ Sharpe                        │ 0.48                           │
│ Calmar                        │ 10.54                          │
│ SQN                           │ 2.23                           │
│ Profit factor                 │ 1.34                           │
│ Expectancy (Ratio)            │ 4.19 (0.21)                    │
│ Avg. daily profit             │ 1.093 USDT                     │
│ Avg. stake amount             │ 738.273 USDT                   │
│ Total trade volume            │ 804166.87 USDT                 │
│                               │                                │
│ Best Pair                     │ ETH/USDT 120.98%               │
│ Worst Pair                    │ LTC/USDT -10.03%               │
│ Best trade                    │ XRP/USDT 65.72%                │
│ Worst trade                   │ LTC/USDT -11.67%               │
│ Best day                      │ 199.34 USDT                    │
│ Worst day                     │ -109.633 USDT                  │
│ Days win/draw/lose            │ 148 / 1649 / 243               │
│ Min/Max/Avg. Duration Winners │ 0d 18:30 / 9d 20:25 / 3d 23:22 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 4d 10:00 / 1d 13:32 │
│ Max Consecutive Wins / Loss   │ 5 / 15                         │
│ Rejected Entry signals        │ 1128                           │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 876.376 USDT                   │
│ Max balance                   │ 3416.117 USDT                  │
│ Max % of account underwater   │ 23.20%                         │
│ Absolute drawdown             │ 676.875 USDT (19.81%)          │
│ Drawdown duration             │ 153 days 02:10:00              │
│ Profit at drawdown start      │ 2416.117 USDT                  │
│ Profit at drawdown end        │ 1739.242 USDT                  │
│ Drawdown start                │ 2024-12-02 00:50:00            │
│ Drawdown end                  │ 2025-05-04 03:00:00            │
│ Market change                 │ 2537.81%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2020-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    542 │         0.89 │        2272.197 │       227.22 │ 2 days, 10:33:00 │  197     0   345  36.3 │ 676.875 USDT  19.81% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-24T13:54:23.689299",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 8488,
  "total_daily_avg_trades": "542 / 0.26",
  "absolute_profit_usdt": 2272.197,
  "total_profit_pct": 227.22,
  "cagr_pct": 23.14,
  "sortino": 1.47,
  "sharpe": 0.48,
  "calmar": 10.54,
  "sqn": 2.23,
  "max_consecutive_wins_loss": "5 / 15",
  "min_balance_usdt": 876.376,
  "max_balance_usdt": 3416.117,
  "absolute_drawdown_pct": 19.81,
  "market_change_pct": 2537.81
}
```
