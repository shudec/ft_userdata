# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 5473  
**Timestamp:** 2025-09-25 16:08:40

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 5473,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20231231",
  "backtest_timerange": "20170801-20231231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20231231
```

## Backtesting Output
```
2025-09-25 14:00:14,023 - freqtrade - INFO - freqtrade 2025.8
2025-09-25 14:00:14,544 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-25 14:00:17,333 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-25 14:00:17,339 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-25 14:00:17,340 - freqtrade.loggers - INFO - Logfile configured
2025-09-25 14:00:17,340 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-25 14:00:17,341 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-25 14:00:17,341 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-25 14:00:17,342 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-25 14:00:17,342 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20231231 ...
2025-09-25 14:00:17,942 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-25 14:00:17,945 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-25 14:00:17,945 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-25 14:00:17,946 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-25 14:00:17,947 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-25 14:00:17,947 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20231231
2025-09-25 14:00:17,949 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-25 14:00:17,962 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-25 14:00:17,963 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 14:00:17,967 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-25 14:00:17,968 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-25 14:00:17,968 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-25 14:00:17,993 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-25 14:00:20,294 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-25 14:00:20,402 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-25 14:00:20,404 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-25 14:00:20,408 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-25 14:00:20,408 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-25 14:00:20,408 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-25 14:00:20,409 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-25 14:00:20,409 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-25 14:00:20,410 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-25 14:00:20,410 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-25 14:00:20,410 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-25 14:00:20,411 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-25 14:00:20,411 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-25 14:00:20,411 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-25 14:00:20,412 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-25 14:00:20,412 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-25 14:00:20,412 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-25 14:00:20,412 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-25 14:00:20,413 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-25 14:00:20,413 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-25 14:00:20,413 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-25 14:00:20,413 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-25 14:00:20,414 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-25 14:00:20,414 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-25 14:00:20,414 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-25 14:00:20,415 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-25 14:00:20,415 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-25 14:00:20,416 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-25 14:00:20,416 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-25 14:00:20,416 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-25 14:00:20,417 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-25 14:00:20,417 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 14:00:20,441 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-25 14:00:20,464 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-25 14:00:20,517 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-25 14:00:20,589 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-25 14:00:20,599 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-25 14:00:20,646 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-25 14:00:20,700 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-25 14:00:20,753 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-25 14:00:20,765 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-25 14:00:20,784 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2023-12-31 00:00:00 (2326 days).
2025-09-25 14:00:21,013 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data starts at 2017-08-17 04:00:00
2025-09-25 14:00:21,517 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data starts at 2017-08-17 04:00:00
2025-09-25 14:00:21,660 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 5m, spot between two candles of 48.50% detected.
2025-09-25 14:00:22,019 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data starts at 2017-12-13 03:30:00
2025-09-25 14:00:22,511 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-25 14:00:22,955 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data starts at 2017-11-06 03:50:00
2025-09-25 14:00:23,096 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 5m, spot between two candles of 23.53% detected.
2025-09-25 14:00:25,105 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-25 14:00:25,123 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-25 14:00:25,124 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-25 14:00:25,125 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-25 14:00:25,125 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-25 14:00:25,126 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-25 14:00:25,126 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 5
2025-09-25 14:00:25,127 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-25 14:00:25,127 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-25 14:00:25,127 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-25 14:00:25,128 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-25 14:00:25,128 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.007
2025-09-25 14:00:25,129 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-25 14:00:25,129 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-25 14:00:25,129 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-25 14:00:25,130 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.007
2025-09-25 14:00:25,131 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.25
2025-09-25 14:00:25,131 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 0.5
2025-09-25 14:00:25,132 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 6
2025-09-25 14:00:25,132 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.998
2025-09-25 14:00:25,133 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 2
2025-09-25 14:00:25,134 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.99
2025-09-25 14:00:25,134 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-25 14:00:25,135 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = False
2025-09-25 14:00:25,135 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-25 14:00:25,136 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-25 14:00:25,136 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-09-25 14:00:25,136 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-25 14:00:25,137 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-25 14:00:25,137 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-25 14:00:25,137 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-25 14:00:25,141 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 14:00:25,159 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-25 14:00:25,183 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 14:00:25,207 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data starts at 2017-08-17 04:00:00
2025-09-25 14:00:42,987 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 14:00:43,015 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-25 14:00:43,048 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 14:00:43,083 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data starts at 2017-08-17 04:00:00
2025-09-25 14:00:43,088 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 4h, spot between two candles of 48.50% detected.
2025-09-25 14:01:02,062 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 14:01:02,079 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-25 14:01:02,101 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 14:01:02,125 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data starts at 2017-12-13 00:00:00
2025-09-25 14:01:19,256 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 14:01:19,273 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-25 14:01:19,300 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 14:01:19,329 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data starts at 2018-05-04 08:00:00
2025-09-25 14:01:35,881 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 14:01:35,898 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-25 14:01:35,917 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 14:01:35,938 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data starts at 2017-11-06 00:00:00
2025-09-25 14:01:35,941 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 4h, spot between two candles of 23.53% detected.
2025-09-25 14:01:54,129 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2017-08-17 04:00:00 up to 2023-12-31 00:00:00 (2326 days).
2025-09-25 14:08:38,204 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-25_14-08-38.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │    148 │         3.02 │       12155.110 │      1215.51 │  2 days, 9:04:00 │   50     0    98  33.8 │
│ ETH/USDT │    178 │         1.36 │        7421.789 │       742.18 │  2 days, 7:40:00 │   59     0   119  33.1 │
│ BTC/USDT │    161 │         1.95 │        7355.435 │       735.54 │ 2 days, 15:47:00 │   60     0   101  37.3 │
│ XRP/USDT │     76 │         2.16 │        2488.693 │       248.87 │  2 days, 1:11:00 │   22     0    54  28.9 │
│ LTC/USDT │    107 │        -0.63 │       -6867.009 │       -686.7 │  1 day, 19:08:00 │   29     0    78  27.1 │
│    TOTAL │    670 │         1.64 │       22554.017 │       2255.4 │  2 days, 7:11:00 │  220     0   450  32.8 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                       ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│         hammer_rebond │     118 │         1.97 │       12949.049 │       1294.9 │ 1 day, 20:39:00 │   30     0    88  25.4 │
│ strong_bullish_rebond │     497 │         1.69 │        5724.361 │       572.44 │ 2 days, 9:59:00 │  170     0   327  34.2 │
│      engulfing_rebond │      55 │         0.49 │        3880.608 │       388.06 │ 2 days, 4:39:00 │   20     0    35  36.4 │
│                 TOTAL │     670 │         1.64 │       22554.017 │       2255.4 │ 2 days, 7:11:00 │  220     0   450  32.8 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                        EXIT REASON STATS                                                         
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                 Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ichimoku_cloud_crossed_exit │   433 │         4.51 │       75502.942 │      7550.29 │ 3 days, 3:05:00 │  220     0   213  50.8 │
│                   stop_loss │   237 │        -3.59 │      -52948.924 │     -5294.89 │        18:51:00 │    0     0   237     0 │
│                       TOTAL │   670 │         1.64 │       22554.017 │       2255.4 │ 2 days, 7:11:00 │  220     0   450  32.8 │
└─────────────────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                                      MIXED TAG STATS                                                                       
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃                 Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ ichimoku_cloud_crossed_exit │    349 │         4.11 │       42512.441 │      4251.24 │  3 days, 1:39:00 │  170     0   179  48.7 │
│         hammer_rebond │ ichimoku_cloud_crossed_exit │     47 │         8.98 │       25105.050 │      2510.51 │ 3 days, 17:55:00 │   30     0    17  63.8 │
│      engulfing_rebond │ ichimoku_cloud_crossed_exit │     37 │         2.52 │        7885.451 │       788.55 │ 2 days, 21:44:00 │   20     0    17  54.1 │
│      engulfing_rebond │                   stop_loss │     18 │        -3.66 │       -4004.843 │      -400.48 │         17:32:00 │    0     0    18     0 │
│         hammer_rebond │                   stop_loss │     71 │        -2.67 │      -12156.001 │      -1215.6 │         14:41:00 │    0     0    71     0 │
│ strong_bullish_rebond │                   stop_loss │    148 │        -4.02 │      -36788.080 │     -3678.81 │         21:01:00 │    0     0   148     0 │
│                 TOTAL │                             │    670 │         1.64 │       22554.017 │       2255.4 │  2 days, 7:11:00 │  220     0   450  32.8 │
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
│ Total/Daily Avg Trades        │ 670 / 0.29                      │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 23554.017 USDT                  │
│ Absolute profit               │ 22554.017 USDT                  │
│ Total profit %                │ 2255.40%                        │
│ CAGR %                        │ 64.17%                          │
│ Sortino                       │ 0.95                            │
│ Sharpe                        │ 0.30                            │
│ Calmar                        │ 35.95                           │
│ SQN                           │ 1.42                            │
│ Profit factor                 │ 1.28                            │
│ Expectancy (Ratio)            │ 33.66 (0.19)                    │
│ Avg. daily profit             │ 9.696 USDT                      │
│ Avg. stake amount             │ 6507.19 USDT                    │
│ Total trade volume            │ 8759690.001 USDT                │
│                               │                                 │
│ Best Pair                     │ BNB/USDT 1215.51%               │
│ Worst Pair                    │ LTC/USDT -686.70%               │
│ Best trade                    │ BNB/USDT 166.24%                │
│ Worst trade                   │ BNB/USDT -20.56%                │
│ Best day                      │ 7225.805 USDT                   │
│ Worst day                     │ -1418.493 USDT                  │
│ Days win/draw/lose            │ 161 / 1785 / 323                │
│ Min/Max/Avg. Duration Winners │ 1d 04:00 / 16d 07:00 / 4d 16:41 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:05 / 4d 09:00 / 1d 03:05  │
│ Max Consecutive Wins / Loss   │ 10 / 32                         │
│ Rejected Entry signals        │ 3871                            │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 986.393 USDT                    │
│ Max balance                   │ 40815.616 USDT                  │
│ Max % of account underwater   │ 51.54%                          │
│ Absolute drawdown             │ 21035.192 USDT (51.54%)         │
│ Drawdown duration             │ 714 days 20:30:00               │
│ Profit at drawdown start      │ 39815.616 USDT                  │
│ Profit at drawdown end        │ 18780.424 USDT                  │
│ Drawdown start                │ 2021-11-10 20:00:00             │
│ Drawdown end                  │ 2023-10-26 16:30:00             │
│ Market change                 │ 4006.86%                        │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2017-08-17 04:00:00 -> 2023-12-31 00:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                    
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃               Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    670 │         1.64 │       22554.017 │       2255.4 │ 2 days, 7:11:00 │  220     0   450  32.8 │ 21035.192 USDT  51.54% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴────────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-25T16:08:39.997276",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 5473,
  "total_daily_avg_trades": "670 / 0.29",
  "absolute_profit_usdt": 22554.017,
  "total_profit_pct": 2255.4,
  "cagr_pct": 64.17,
  "sortino": 0.95,
  "sharpe": 0.3,
  "calmar": 35.95,
  "sqn": 1.42,
  "max_consecutive_wins_loss": "10 / 32",
  "min_balance_usdt": 986.393,
  "max_balance_usdt": 40815.616,
  "absolute_drawdown_pct": 51.54,
  "market_change_pct": 4006.86,
  "win_draw_loss_winpct": "0 0 0 0"
}
```
