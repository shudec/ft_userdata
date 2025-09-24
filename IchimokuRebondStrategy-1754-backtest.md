# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 1754  
**Timestamp:** 2025-09-24 22:20:11

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 1754,
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
2025-09-24 20:10:48,008 - freqtrade - INFO - freqtrade 2025.7
2025-09-24 20:10:48,338 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-24 20:10:48,339 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-24 20:10:49,806 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-24 20:10:49,809 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-24 20:10:49,809 - freqtrade.loggers - INFO - Logfile configured
2025-09-24 20:10:49,809 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-24 20:10:49,810 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-24 20:10:49,810 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-24 20:10:49,811 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-24 20:10:49,811 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20231231 ...
2025-09-24 20:10:49,820 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-24 20:10:49,821 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-24 20:10:49,821 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-24 20:10:49,822 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-24 20:10:49,822 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-24 20:10:49,823 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20231231
2025-09-24 20:10:49,824 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-24 20:10:49,844 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-24 20:10:49,845 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 20:10:49,849 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-24 20:10:49,850 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-24 20:10:49,850 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-24 20:10:49,883 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-24 20:10:53,010 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-24 20:10:53,050 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-24 20:10:53,051 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-24 20:10:53,052 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-24 20:10:53,052 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-24 20:10:53,053 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-24 20:10:53,053 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-24 20:10:53,054 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-24 20:10:53,054 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-24 20:10:53,055 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-24 20:10:53,055 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-24 20:10:53,056 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-24 20:10:53,056 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-24 20:10:53,056 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-24 20:10:53,057 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-24 20:10:53,057 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-24 20:10:53,058 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-24 20:10:53,058 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-24 20:10:53,059 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-24 20:10:53,059 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-24 20:10:53,059 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-24 20:10:53,060 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-24 20:10:53,060 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-24 20:10:53,061 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-24 20:10:53,061 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-24 20:10:53,062 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-24 20:10:53,062 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-24 20:10:53,062 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-24 20:10:53,063 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-24 20:10:53,063 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-24 20:10:53,064 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-24 20:10:53,064 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 20:10:53,069 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-24 20:10:53,101 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-24 20:10:53,132 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-24 20:10:53,197 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-24 20:10:53,209 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-24 20:10:53,247 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-24 20:10:53,297 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-24 20:10:53,344 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-24 20:10:53,360 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-24 20:10:53,392 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2023-12-31 00:00:00 (2326 days).
2025-09-24 20:10:53,476 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data starts at 2017-08-17 04:00:00
2025-09-24 20:10:53,893 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data starts at 2017-08-17 04:00:00
2025-09-24 20:10:54,031 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 5m, spot between two candles of 48.50% detected.
2025-09-24 20:10:54,251 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data starts at 2017-12-13 03:30:00
2025-09-24 20:10:54,584 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-24 20:10:54,890 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data starts at 2017-11-06 03:50:00
2025-09-24 20:10:55,033 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 5m, spot between two candles of 23.53% detected.
2025-09-24 20:10:57,592 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-24 20:10:57,595 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-24 20:10:57,596 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-24 20:10:57,596 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-24 20:10:57,597 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-24 20:10:57,597 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-24 20:10:57,597 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 10
2025-09-24 20:10:57,598 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-24 20:10:57,598 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-24 20:10:57,599 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-24 20:10:57,599 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-24 20:10:57,599 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.007
2025-09-24 20:10:57,600 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-24 20:10:57,600 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-24 20:10:57,601 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-24 20:10:57,601 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.007
2025-09-24 20:10:57,602 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.25
2025-09-24 20:10:57,602 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1.5
2025-09-24 20:10:57,603 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-09-24 20:10:57,603 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.998
2025-09-24 20:10:57,604 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 1
2025-09-24 20:10:57,604 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.996
2025-09-24 20:10:57,605 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-24 20:10:57,605 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-24 20:10:57,606 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = none
2025-09-24 20:10:57,606 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-09-24 20:10:57,606 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-24 20:10:57,607 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-24 20:10:57,607 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-24 20:10:57,608 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-24 20:10:57,612 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 20:10:57,623 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-24 20:10:57,650 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 20:10:57,670 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data starts at 2017-08-17 04:00:00
2025-09-24 20:11:11,463 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 20:11:11,473 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-24 20:11:11,495 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 20:11:11,513 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data starts at 2017-08-17 04:00:00
2025-09-24 20:11:11,518 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 4h, spot between two candles of 48.50% detected.
2025-09-24 20:11:25,014 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 20:11:25,022 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-24 20:11:25,041 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 20:11:25,059 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data starts at 2017-12-13 00:00:00
2025-09-24 20:11:37,549 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 20:11:37,560 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-24 20:11:37,584 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 20:11:37,602 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data starts at 2018-05-04 08:00:00
2025-09-24 20:11:49,970 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 20:11:49,981 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-24 20:11:50,008 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 20:11:50,029 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data starts at 2017-11-06 00:00:00
2025-09-24 20:11:50,037 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 4h, spot between two candles of 23.53% detected.
2025-09-24 20:12:03,632 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2017-08-17 04:00:00 up to 2023-12-31 00:00:00 (2326 days).
2025-09-24 20:20:09,895 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-24_20-20-09.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │    208 │         2.31 │        4193.153 │       419.32 │  2 days, 9:11:00 │   79     0   129  38.0 │
│ ETH/USDT │    213 │         1.88 │        3947.798 │       394.78 │ 2 days, 15:52:00 │   86     0   127  40.4 │
│ XRP/USDT │    136 │         1.43 │        2848.399 │       284.84 │  1 day, 20:37:00 │   46     0    90  33.8 │
│ BTC/USDT │    227 │         1.65 │        2805.935 │       280.59 │ 2 days, 19:42:00 │   86     0   141  37.9 │
│ LTC/USDT │    158 │         0.25 │         490.395 │        49.04 │  2 days, 5:08:00 │   55     0   103  34.8 │
│    TOTAL │    942 │         1.58 │       14285.681 │      1428.57 │ 2 days, 10:44:00 │  352     0   590  37.4 │
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
│ strong_bullish_rebond │     729 │          1.5 │       10147.897 │      1014.79 │ 2 days, 12:12:00 │  275     0   454  37.7 │
│      engulfing_rebond │      71 │         2.35 │        2264.665 │       226.47 │ 2 days, 13:44:00 │   32     0    39  45.1 │
│         hammer_rebond │     142 │         1.59 │        1873.119 │       187.31 │  2 days, 1:44:00 │   45     0    97  31.7 │
│                 TOTAL │     942 │         1.58 │       14285.681 │      1428.57 │ 2 days, 10:44:00 │  352     0   590  37.4 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                         EXIT REASON STATS                                                         
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                 Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│              take_profit_3R │    50 │        30.97 │       14695.022 │       1469.5 │ 3 days, 19:48:00 │   50     0     0   100 │
│ ichimoku_cloud_crossed_exit │   857 │         0.33 │        2633.056 │       263.31 │ 2 days, 10:24:00 │  301     0   556  35.1 │
│   ichimoku_cloud_futur_exit │     1 │         5.48 │         149.195 │        14.92 │          1:00:00 │    1     0     0   100 │
│                   stop_loss │    34 │       -10.18 │       -3191.592 │      -319.16 │         20:06:00 │    0     0    34     0 │
│                       TOTAL │   942 │         1.58 │       14285.681 │      1428.57 │ 2 days, 10:44:00 │  352     0   590  37.4 │
└─────────────────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                                      MIXED TAG STATS                                                                       
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃                 Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │              take_profit_3R │     35 │        30.95 │        9477.929 │       947.79 │ 3 days, 20:06:00 │   35     0     0   100 │
│         hammer_rebond │              take_profit_3R │     12 │        30.85 │        3951.686 │       395.17 │ 3 days, 14:25:00 │   12     0     0   100 │
│ strong_bullish_rebond │ ichimoku_cloud_crossed_exit │    671 │         0.34 │        2773.674 │       277.37 │ 2 days, 11:52:00 │  239     0   432  35.6 │
│      engulfing_rebond │              take_profit_3R │      3 │        31.69 │        1265.407 │       126.54 │ 4 days, 13:40:00 │    3     0     0   100 │
│      engulfing_rebond │ ichimoku_cloud_crossed_exit │     67 │         1.22 │        1240.225 │       124.02 │ 2 days, 12:12:00 │   29     0    38  43.3 │
│ strong_bullish_rebond │   ichimoku_cloud_futur_exit │      1 │         5.48 │         149.195 │        14.92 │          1:00:00 │    1     0     0   100 │
│      engulfing_rebond │                   stop_loss │      1 │       -10.18 │        -240.968 │        -24.1 │         20:55:00 │    0     0     1     0 │
│         hammer_rebond │                   stop_loss │     11 │       -10.18 │        -697.723 │       -69.77 │         15:51:00 │    0     0    11     0 │
│         hammer_rebond │ ichimoku_cloud_crossed_exit │    119 │        -0.27 │       -1380.844 │      -138.08 │  2 days, 1:10:00 │   33     0    86  27.7 │
│ strong_bullish_rebond │                   stop_loss │     22 │       -10.18 │       -2252.901 │      -225.29 │         22:11:00 │    0     0    22     0 │
│                 TOTAL │                             │    942 │         1.58 │       14285.681 │      1428.57 │ 2 days, 10:44:00 │  352     0   590  37.4 │
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
│ Total/Daily Avg Trades        │ 942 / 0.4                       │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 15285.681 USDT                  │
│ Absolute profit               │ 14285.681 USDT                  │
│ Total profit %                │ 1428.57%                        │
│ CAGR %                        │ 53.41%                          │
│ Sortino                       │ 2.75                            │
│ Sharpe                        │ 0.96                            │
│ Calmar                        │ 57.88                           │
│ SQN                           │ 3.80                            │
│ Profit factor                 │ 1.58                            │
│ Expectancy (Ratio)            │ 15.17 (0.36)                    │
│ Avg. daily profit             │ 6.142 USDT                      │
│ Avg. stake amount             │ 1446.148 USDT                   │
│ Total trade volume            │ 2744311.848 USDT                │
│                               │                                 │
│ Best Pair                     │ BNB/USDT 419.32%                │
│ Worst Pair                    │ LTC/USDT 49.04%                 │
│ Best trade                    │ BNB/USDT 35.61%                 │
│ Worst trade                   │ BNB/USDT -10.18%                │
│ Best day                      │ 1126.181 USDT                   │
│ Worst day                     │ -457.613 USDT                   │
│ Days win/draw/lose            │ 253 / 1657 / 369                │
│ Min/Max/Avg. Duration Winners │ 0d 01:00 / 14d 12:00 / 4d 05:14 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:35 / 5d 09:00 / 1d 09:23  │
│ Max Consecutive Wins / Loss   │ 7 / 17                          │
│ Rejected Entry signals        │ 9816                            │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 996.87 USDT                     │
│ Max balance                   │ 15285.681 USDT                  │
│ Max % of account underwater   │ 20.27%                          │
│ Absolute Drawdown (Account)   │ 20.27%                          │
│ Absolute Drawdown             │ 2788.026 USDT                   │
│ Drawdown high                 │ 12753.377 USDT                  │
│ Drawdown low                  │ 9965.35 USDT                    │
│ Drawdown Start                │ 2021-11-10 22:00:00             │
│ Drawdown End                  │ 2022-07-10 19:00:00             │
│ Market change                 │ 4006.86%                        │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2017-08-17 04:00:00 -> 2023-12-31 00:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                    
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃              Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    942 │         1.58 │       14285.681 │      1428.57 │ 2 days, 10:44:00 │  352     0   590  37.4 │ 2788.026 USDT  20.27% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┴───────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-24T22:20:11.218461",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 1754,
  "total_daily_avg_trades": "942 / 0.4",
  "absolute_profit_usdt": 14285.681,
  "total_profit_pct": 1428.57,
  "cagr_pct": 53.41,
  "sortino": 2.75,
  "sharpe": 0.96,
  "calmar": 57.88,
  "sqn": 3.8,
  "max_consecutive_wins_loss": "7 / 17",
  "min_balance_usdt": 996.87,
  "max_balance_usdt": 15285.681,
  "market_change_pct": 4006.86,
  "win_draw_loss_winpct": "0 0 0 0"
}
```
