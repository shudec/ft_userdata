# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 6564  
**Timestamp:** 2025-09-24 17:33:57

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 6564,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20170801-20231231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20231231
```

## Backtesting Output
```
2025-09-24 15:27:21,149 - freqtrade - INFO - freqtrade 2025.8
2025-09-24 15:27:21,651 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-24 15:27:23,809 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-24 15:27:23,818 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-24 15:27:23,819 - freqtrade.loggers - INFO - Logfile configured
2025-09-24 15:27:23,820 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-24 15:27:23,821 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-24 15:27:23,821 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-24 15:27:23,822 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-24 15:27:23,823 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20231231 ...
2025-09-24 15:27:24,601 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-24 15:27:24,604 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-24 15:27:24,605 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-24 15:27:24,605 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-24 15:27:24,606 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-24 15:27:24,607 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20231231
2025-09-24 15:27:24,609 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-24 15:27:24,629 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-24 15:27:24,630 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 15:27:24,634 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-24 15:27:24,636 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-24 15:27:24,637 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-24 15:27:24,673 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-24 15:27:26,991 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-24 15:27:27,096 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-24 15:27:27,099 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-24 15:27:27,105 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-24 15:27:27,105 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-24 15:27:27,106 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-24 15:27:27,106 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-24 15:27:27,107 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-24 15:27:27,107 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-24 15:27:27,108 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-24 15:27:27,108 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-24 15:27:27,109 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-24 15:27:27,110 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-24 15:27:27,110 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-24 15:27:27,111 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-24 15:27:27,111 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-24 15:27:27,112 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-24 15:27:27,112 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-24 15:27:27,113 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-24 15:27:27,113 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-24 15:27:27,114 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-24 15:27:27,114 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-24 15:27:27,115 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-24 15:27:27,115 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-24 15:27:27,116 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-24 15:27:27,116 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-24 15:27:27,116 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-24 15:27:27,117 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-24 15:27:27,117 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-24 15:27:27,117 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-24 15:27:27,118 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-24 15:27:27,118 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 15:27:27,138 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-24 15:27:27,166 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-24 15:27:27,238 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-24 15:27:27,330 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-24 15:27:27,341 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-24 15:27:27,414 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-24 15:27:27,494 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-24 15:27:27,567 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-24 15:27:27,583 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-24 15:27:27,612 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2023-12-31 00:00:00 (2326 days).
2025-09-24 15:27:27,991 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data starts at 2017-08-17 04:00:00
2025-09-24 15:27:28,723 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data starts at 2017-08-17 04:00:00
2025-09-24 15:27:28,912 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 5m, spot between two candles of 48.50% detected.
2025-09-24 15:27:29,407 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data starts at 2017-12-13 03:30:00
2025-09-24 15:27:30,025 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-24 15:27:30,633 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data starts at 2017-11-06 03:50:00
2025-09-24 15:27:30,826 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 5m, spot between two candles of 23.53% detected.
2025-09-24 15:27:32,979 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-24 15:27:32,995 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-24 15:27:32,996 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-24 15:27:32,997 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-24 15:27:32,997 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-24 15:27:32,998 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-24 15:27:32,998 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 10
2025-09-24 15:27:32,999 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-24 15:27:32,999 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-24 15:27:33,000 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-24 15:27:33,000 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-24 15:27:33,001 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-24 15:27:33,001 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-24 15:27:33,002 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-24 15:27:33,002 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-24 15:27:33,003 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-24 15:27:33,003 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.25
2025-09-24 15:27:33,004 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1.5
2025-09-24 15:27:33,005 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-09-24 15:27:33,005 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.998
2025-09-24 15:27:33,005 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 1
2025-09-24 15:27:33,006 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.996
2025-09-24 15:27:33,006 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-24 15:27:33,006 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-24 15:27:33,007 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = none
2025-09-24 15:27:33,008 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-09-24 15:27:33,009 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-24 15:27:33,010 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-24 15:27:33,010 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-24 15:27:33,011 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-24 15:27:33,015 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 15:27:33,035 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-24 15:27:33,057 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 15:27:33,090 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data starts at 2017-08-17 04:00:00
2025-09-24 15:27:43,844 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 15:27:43,874 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-24 15:27:43,890 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 15:27:43,916 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data starts at 2017-08-17 04:00:00
2025-09-24 15:27:43,921 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 4h, spot between two candles of 48.50% detected.
2025-09-24 15:27:54,574 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 15:27:54,593 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-24 15:27:54,606 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 15:27:54,631 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data starts at 2017-12-13 00:00:00
2025-09-24 15:28:04,324 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 15:28:04,343 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-24 15:28:04,359 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 15:28:04,388 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data starts at 2018-05-04 08:00:00
2025-09-24 15:28:13,469 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 15:28:13,493 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-24 15:28:13,513 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 15:28:13,542 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data starts at 2017-11-06 00:00:00
2025-09-24 15:28:13,548 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 4h, spot between two candles of 23.53% detected.
2025-09-24 15:28:24,741 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2017-08-17 04:00:00 up to 2023-12-31 00:00:00 (2326 days).
2025-09-24 15:33:55,751 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-24_15-33-55.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │    164 │         1.69 │        1316.323 │       131.63 │ 2 days, 14:19:00 │   70     0    94  42.7 │
│ BNB/USDT │    135 │         1.73 │        1151.183 │       115.12 │ 2 days, 13:36:00 │   52     0    83  38.5 │
│ BTC/USDT │    175 │         1.46 │         985.789 │        98.58 │ 2 days, 16:32:00 │   72     0   103  41.1 │
│ XRP/USDT │    109 │         0.64 │         329.105 │        32.91 │  1 day, 19:14:00 │   29     0    80  26.6 │
│ LTC/USDT │    111 │         0.11 │         -55.883 │        -5.59 │  2 days, 3:19:00 │   39     0    72  35.1 │
│    TOTAL │    694 │         1.22 │        3726.517 │       372.65 │  2 days, 9:59:00 │  262     0   432  37.8 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │     524 │         0.98 │        2094.327 │       209.43 │  2 days, 9:31:00 │  198     0   326  37.8 │
│      engulfing_rebond │      67 │         2.81 │         869.264 │        86.93 │ 2 days, 15:53:00 │   27     0    40  40.3 │
│         hammer_rebond │     103 │         1.43 │         762.926 │        76.29 │  2 days, 8:28:00 │   37     0    66  35.9 │
│                 TOTAL │     694 │         1.22 │        3726.517 │       372.65 │  2 days, 9:59:00 │  262     0   432  37.8 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                        EXIT REASON STATS                                                         
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                 Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│              take_profit_3R │    29 │        30.69 │        3749.835 │       374.98 │ 4 days, 2:56:00 │   29     0     0   100 │
│ ichimoku_cloud_crossed_exit │   643 │         0.26 │         597.575 │        59.76 │ 2 days, 9:22:00 │  232     0   411  36.1 │
│   ichimoku_cloud_futur_exit │     1 │         5.48 │          46.258 │         4.63 │         1:00:00 │    1     0     0   100 │
│                   stop_loss │    21 │       -10.18 │        -667.151 │       -66.72 │        23:05:00 │    0     0    21     0 │
│                       TOTAL │   694 │         1.22 │        3726.517 │       372.65 │ 2 days, 9:59:00 │  262     0   432  37.8 │
└─────────────────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                                      MIXED TAG STATS                                                                       
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃                 Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │              take_profit_3R │     19 │        30.73 │        2443.846 │       244.38 │ 3 days, 20:37:00 │   19     0     0   100 │
│         hammer_rebond │              take_profit_3R │      5 │        30.36 │         763.614 │        76.36 │ 4 days, 21:03:00 │    5     0     0   100 │
│      engulfing_rebond │              take_profit_3R │      5 │        30.83 │         542.375 │        54.24 │  4 days, 8:48:00 │    5     0     0   100 │
│      engulfing_rebond │ ichimoku_cloud_crossed_exit │     62 │         0.56 │         326.889 │        32.69 │ 2 days, 12:35:00 │   22     0    40  35.5 │
│         hammer_rebond │ ichimoku_cloud_crossed_exit │     92 │         0.61 │         204.289 │        20.43 │  2 days, 7:46:00 │   32     0    60  34.8 │
│ strong_bullish_rebond │ ichimoku_cloud_crossed_exit │    489 │         0.16 │          66.398 │         6.64 │  2 days, 9:15:00 │  178     0   311  36.4 │
│ strong_bullish_rebond │   ichimoku_cloud_futur_exit │      1 │         5.48 │          46.258 │         4.63 │          1:00:00 │    1     0     0   100 │
│         hammer_rebond │                   stop_loss │      6 │       -10.18 │        -204.976 │        -20.5 │         16:52:00 │    0     0     6     0 │
│ strong_bullish_rebond │                   stop_loss │     15 │       -10.18 │        -462.175 │       -46.22 │   1 day, 1:34:00 │    0     0    15     0 │
│                 TOTAL │                             │    694 │         1.22 │        3726.517 │       372.65 │  2 days, 9:59:00 │  262     0   432  37.8 │
└───────────────────────┴─────────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2017-08-17 04:00:00             │
│ Backtesting to                │ 2023-12-31 00:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 694 / 0.3                       │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 4726.517 USDT                   │
│ Absolute profit               │ 3726.517 USDT                   │
│ Total profit %                │ 372.65%                         │
│ CAGR %                        │ 27.60%                          │
│ Sortino                       │ 2.32                            │
│ Sharpe                        │ 0.73                            │
│ Calmar                        │ 23.46                           │
│ SQN                           │ 3.37                            │
│ Profit factor                 │ 1.57                            │
│ Expectancy (Ratio)            │ 5.37 (0.35)                     │
│ Avg. daily profit             │ 1.602 USDT                      │
│ Avg. stake amount             │ 538.152 USDT                    │
│ Total trade volume            │ 752184.988 USDT                 │
│                               │                                 │
│ Best Pair                     │ ETH/USDT 131.63%                │
│ Worst Pair                    │ LTC/USDT -5.59%                 │
│ Best trade                    │ BNB/USDT 32.70%                 │
│ Worst trade                   │ LTC/USDT -10.18%                │
│ Best day                      │ 397.07 USDT                     │
│ Worst day                     │ -107.843 USDT                   │
│ Days win/draw/lose            │ 184 / 1803 / 292                │
│ Min/Max/Avg. Duration Winners │ 0d 01:00 / 14d 12:00 / 4d 03:36 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 4d 06:00 / 1d 08:45  │
│ Max Consecutive Wins / Loss   │ 10 / 14                         │
│ Rejected Entry signals        │ 2472                            │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 906.335 USDT                    │
│ Max balance                   │ 4757.382 USDT                   │
│ Max % of account underwater   │ 21.63%                          │
│ Absolute drawdown             │ 609.921 USDT (13.05%)           │
│ Drawdown duration             │ 245 days 16:00:00               │
│ Profit at drawdown start      │ 3674.478 USDT                   │
│ Profit at drawdown end        │ 3064.556 USDT                   │
│ Drawdown start                │ 2023-01-24 23:00:00             │
│ Drawdown end                  │ 2023-09-27 15:00:00             │
│ Market change                 │ 4006.86%                        │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2017-08-17 04:00:00 -> 2023-12-31 00:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    694 │         1.22 │        3726.517 │       372.65 │ 2 days, 9:59:00 │  262     0   432  37.8 │ 609.921 USDT  13.05% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-24T17:33:57.131711",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 6564,
  "total_daily_avg_trades": "694 / 0.3",
  "absolute_profit_usdt": 3726.517,
  "total_profit_pct": 372.65,
  "cagr_pct": 27.6,
  "sortino": 2.32,
  "sharpe": 0.73,
  "calmar": 23.46,
  "sqn": 3.37,
  "max_consecutive_wins_loss": "10 / 14",
  "min_balance_usdt": 906.335,
  "max_balance_usdt": 4757.382,
  "absolute_drawdown_pct": 13.05,
  "market_change_pct": 4006.86,
  "win_draw_loss_winpct": "0 0 0 0"
}
```
