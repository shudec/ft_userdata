# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 4042  
**Timestamp:** 2025-09-24 17:45:49

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 4042,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20240101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20240101-20251231
```

## Backtesting Output
```
2025-09-24 15:42:48,004 - freqtrade - INFO - freqtrade 2025.8
2025-09-24 15:42:48,407 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-24 15:42:50,628 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-24 15:42:50,661 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-24 15:42:50,662 - freqtrade.loggers - INFO - Logfile configured
2025-09-24 15:42:50,664 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-24 15:42:50,665 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-24 15:42:50,666 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-24 15:42:50,670 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-24 15:42:50,671 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20240101-20251231 ...
2025-09-24 15:42:52,276 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-24 15:42:52,280 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-24 15:42:52,281 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-24 15:42:52,282 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-24 15:42:52,282 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-24 15:42:52,283 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20240101-20251231
2025-09-24 15:42:52,296 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-24 15:42:52,358 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-24 15:42:52,360 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 15:42:52,375 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-24 15:42:52,377 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-24 15:42:52,388 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-24 15:42:52,452 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-24 15:42:55,219 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-24 15:42:55,360 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-24 15:42:55,363 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-24 15:42:55,368 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-24 15:42:55,369 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-24 15:42:55,370 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-24 15:42:55,370 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-24 15:42:55,371 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-24 15:42:55,372 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-24 15:42:55,373 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-24 15:42:55,374 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-24 15:42:55,375 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-24 15:42:55,376 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-24 15:42:55,378 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-24 15:42:55,379 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-24 15:42:55,379 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-24 15:42:55,380 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-24 15:42:55,381 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-24 15:42:55,381 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-24 15:42:55,382 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-24 15:42:55,383 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-24 15:42:55,383 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-24 15:42:55,384 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-24 15:42:55,385 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-24 15:42:55,385 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-24 15:42:55,386 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-24 15:42:55,386 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-24 15:42:55,387 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-24 15:42:55,387 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-24 15:42:55,388 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-24 15:42:55,389 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-24 15:42:55,390 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 15:42:55,415 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-24 15:42:55,454 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-24 15:42:55,539 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 15:42:55,626 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 15:42:55,715 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 15:42:55,807 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 15:42:55,909 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 15:42:55,947 - freqtrade.optimize.backtesting - INFO - Loading data from 2024-01-01 00:00:00 up to 2025-09-10 08:00:00 (618 days).
2025-09-24 15:42:56,384 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 15:42:57,153 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 15:42:57,830 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 15:42:58,408 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 15:42:59,204 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 15:43:01,035 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-24 15:43:01,129 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-24 15:43:01,131 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-24 15:43:01,133 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-24 15:43:01,141 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-24 15:43:01,142 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-24 15:43:01,143 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-24 15:43:01,144 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 10
2025-09-24 15:43:01,145 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-24 15:43:01,147 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-24 15:43:01,148 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-24 15:43:01,149 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-24 15:43:01,150 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-24 15:43:01,151 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-24 15:43:01,152 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-24 15:43:01,153 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-24 15:43:01,154 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-24 15:43:01,155 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.25
2025-09-24 15:43:01,163 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1.5
2025-09-24 15:43:01,166 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-09-24 15:43:01,168 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.998
2025-09-24 15:43:01,169 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 1
2025-09-24 15:43:01,171 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.996
2025-09-24 15:43:01,172 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-24 15:43:01,174 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-24 15:43:01,180 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = none
2025-09-24 15:43:01,181 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-09-24 15:43:01,181 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-24 15:43:01,182 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-24 15:43:01,183 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-24 15:43:01,184 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-24 15:43:01,196 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 15:43:01,287 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 15:43:01,331 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 15:43:01,463 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 15:43:21,591 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 15:43:22,058 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 15:43:22,150 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 15:43:23,138 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 15:43:37,452 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 15:43:37,495 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 15:43:37,529 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 15:43:37,601 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-15 00:00:00
2025-09-24 15:43:47,985 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 15:43:48,009 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 15:43:48,035 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 15:43:48,076 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 15:43:54,760 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 15:43:54,786 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 15:43:54,818 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 15:43:54,870 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 15:43:59,965 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2024-01-01 00:00:00 up to 2025-09-10 08:00:00 (618 days).
2025-09-24 15:45:47,603 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-24_15-45-47.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │     47 │         1.38 │         128.463 │        12.85 │  3 days, 7:21:00 │   21     0    26  44.7 │
│ LTC/USDT │     31 │          0.7 │          53.976 │          5.4 │  2 days, 3:24:00 │   11     0    20  35.5 │
│ ETH/USDT │     38 │         0.64 │          48.258 │         4.83 │ 2 days, 19:41:00 │   17     0    21  44.7 │
│ XRP/USDT │     39 │         0.54 │          45.620 │         4.56 │  1 day, 21:44:00 │    7     0    32  17.9 │
│ BNB/USDT │     55 │         0.03 │          -7.107 │        -0.71 │  2 days, 6:51:00 │   15     0    40  27.3 │
│    TOTAL │    210 │         0.63 │         269.210 │        26.92 │ 2 days, 12:27:00 │   71     0   139  33.8 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                            LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         3.08 │           7.706 │         0.77 │ 4 days, 6:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         3.08 │           7.706 │         0.77 │ 4 days, 6:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                        ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │     172 │         0.87 │         321.444 │        32.14 │ 2 days, 13:08:00 │   60     0   112  34.9 │
│         hammer_rebond │      13 │        -0.76 │         -24.821 │        -2.48 │  2 days, 6:14:00 │    3     0    10  23.1 │
│      engulfing_rebond │      25 │        -0.24 │         -27.413 │        -2.74 │ 2 days, 10:59:00 │    8     0    17  32.0 │
│                 TOTAL │     210 │         0.63 │         269.210 │        26.92 │ 2 days, 12:27:00 │   71     0   139  33.8 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                         EXIT REASON STATS                                                         
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                 Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│              take_profit_3R │     3 │        32.25 │         228.709 │        22.87 │  2 days, 7:45:00 │    3     0     0   100 │
│ ichimoku_cloud_crossed_exit │   205 │         0.21 │          60.755 │         6.08 │ 2 days, 12:31:00 │   67     0   138  32.7 │
│                  force_exit │     1 │         3.08 │           7.706 │         0.77 │  4 days, 6:00:00 │    1     0     0   100 │
│                   stop_loss │     1 │       -10.18 │         -27.960 │         -2.8 │         19:25:00 │    0     0     1     0 │
│                       TOTAL │   210 │         0.63 │         269.210 │        26.92 │ 2 days, 12:27:00 │   71     0   139  33.8 │
└─────────────────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                                      MIXED TAG STATS                                                                       
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃                 Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │              take_profit_3R │      3 │        32.25 │         228.709 │        22.87 │  2 days, 7:45:00 │    3     0     0   100 │
│ strong_bullish_rebond │ ichimoku_cloud_crossed_exit │    168 │         0.29 │          85.029 │          8.5 │ 2 days, 13:00:00 │   56     0   112  33.3 │
│ strong_bullish_rebond │                  force_exit │      1 │         3.08 │           7.706 │         0.77 │  4 days, 6:00:00 │    1     0     0   100 │
│      engulfing_rebond │ ichimoku_cloud_crossed_exit │     24 │         0.17 │           0.546 │         0.05 │ 2 days, 12:38:00 │    8     0    16  33.3 │
│         hammer_rebond │ ichimoku_cloud_crossed_exit │     13 │        -0.76 │         -24.821 │        -2.48 │  2 days, 6:14:00 │    3     0    10  23.1 │
│      engulfing_rebond │                   stop_loss │      1 │       -10.18 │         -27.960 │         -2.8 │         19:25:00 │    0     0     1     0 │
│                 TOTAL │                             │    210 │         0.63 │         269.210 │        26.92 │ 2 days, 12:27:00 │   71     0   139  33.8 │
└───────────────────────┴─────────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2024-01-01 00:00:00             │
│ Backtesting to                │ 2025-09-10 08:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 210 / 0.34                      │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 1269.21 USDT                    │
│ Absolute profit               │ 269.21 USDT                     │
│ Total profit %                │ 26.92%                          │
│ CAGR %                        │ 15.12%                          │
│ Sortino                       │ 2.03                            │
│ Sharpe                        │ 0.59                            │
│ Calmar                        │ 4.67                            │
│ SQN                           │ 1.31                            │
│ Profit factor                 │ 1.35                            │
│ Expectancy (Ratio)            │ 1.28 (0.23)                     │
│ Avg. daily profit             │ 0.436 USDT                      │
│ Avg. stake amount             │ 230.67 USDT                     │
│ Total trade volume            │ 97345.039 USDT                  │
│                               │                                 │
│ Best Pair                     │ BTC/USDT 12.85%                 │
│ Worst Pair                    │ BNB/USDT -0.71%                 │
│ Best trade                    │ XRP/USDT 33.77%                 │
│ Worst trade                   │ BTC/USDT -10.18%                │
│ Best day                      │ 159.064 USDT                    │
│ Worst day                     │ -31.283 USDT                    │
│ Days win/draw/lose            │ 47 / 437 / 93                   │
│ Min/Max/Avg. Duration Winners │ 0d 23:40 / 10d 15:00 / 4d 13:22 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 3d 07:00 / 1d 11:28  │
│ Max Consecutive Wins / Loss   │ 7 / 15                          │
│ Rejected Entry signals        │ 804                             │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 1005.166 USDT                   │
│ Max balance                   │ 1386.023 USDT                   │
│ Max % of account underwater   │ 17.83%                          │
│ Absolute drawdown             │ 247.11 USDT (17.83%)            │
│ Drawdown duration             │ 218 days 00:20:00               │
│ Profit at drawdown start      │ 386.023 USDT                    │
│ Profit at drawdown end        │ 138.913 USDT                    │
│ Drawdown start                │ 2024-12-02 14:40:00             │
│ Drawdown end                  │ 2025-07-08 15:00:00             │
│ Market change                 │ 174.13%                         │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2024-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃            Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    210 │         0.63 │         269.210 │        26.92 │ 2 days, 12:27:00 │   71     0   139  33.8 │ 247.11 USDT  17.83% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┴─────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-24T17:45:49.048054",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 4042,
  "total_daily_avg_trades": "210 / 0.34",
  "absolute_profit_usdt": 269.21,
  "total_profit_pct": 26.92,
  "cagr_pct": 15.12,
  "sortino": 2.03,
  "sharpe": 0.59,
  "calmar": 4.67,
  "sqn": 1.31,
  "max_consecutive_wins_loss": "7 / 15",
  "min_balance_usdt": 1005.166,
  "max_balance_usdt": 1386.023,
  "absolute_drawdown_pct": 17.83,
  "market_change_pct": 174.13
}
```
