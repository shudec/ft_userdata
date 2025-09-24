# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 9279  
**Timestamp:** 2025-09-24 11:46:28

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 9279,
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
2025-09-24 09:38:11,579 - freqtrade - INFO - freqtrade 2025.8
2025-09-24 09:38:12,120 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-24 09:38:14,787 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-24 09:38:14,794 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-24 09:38:14,795 - freqtrade.loggers - INFO - Logfile configured
2025-09-24 09:38:14,795 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-24 09:38:14,796 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-24 09:38:14,797 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-24 09:38:14,797 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-24 09:38:14,798 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20200101-20251231 ...
2025-09-24 09:38:15,287 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-24 09:38:15,290 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-24 09:38:15,290 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-24 09:38:15,291 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-24 09:38:15,292 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-24 09:38:15,292 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20200101-20251231
2025-09-24 09:38:15,295 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-24 09:38:15,308 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-24 09:38:15,309 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 09:38:15,312 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-24 09:38:15,313 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-24 09:38:15,313 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-24 09:38:15,336 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-24 09:38:17,826 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-24 09:38:17,938 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-24 09:38:17,940 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-24 09:38:17,945 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-24 09:38:17,946 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-24 09:38:17,947 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-24 09:38:17,947 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-24 09:38:17,947 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-24 09:38:17,948 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-24 09:38:17,948 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-24 09:38:17,949 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-24 09:38:17,949 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-24 09:38:17,949 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-24 09:38:17,950 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-24 09:38:17,950 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-24 09:38:17,950 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-24 09:38:17,951 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-24 09:38:17,951 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-24 09:38:17,951 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-24 09:38:17,952 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-24 09:38:17,952 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-24 09:38:17,953 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-24 09:38:17,953 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-24 09:38:17,954 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-24 09:38:17,954 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-24 09:38:17,954 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-24 09:38:17,955 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-24 09:38:17,955 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-24 09:38:17,956 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-24 09:38:17,956 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-24 09:38:17,956 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-24 09:38:17,957 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 09:38:17,984 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-24 09:38:18,013 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-24 09:38:18,081 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 09:38:18,163 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 09:38:18,222 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 09:38:18,279 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 09:38:18,346 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 09:38:18,376 - freqtrade.optimize.backtesting - INFO - Loading data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 09:38:18,652 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 09:38:19,172 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 09:38:19,655 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 09:38:20,118 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 09:38:20,619 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 09:38:22,454 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-24 09:38:22,460 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-24 09:38:22,460 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-24 09:38:22,461 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-24 09:38:22,461 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-24 09:38:22,462 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-24 09:38:22,462 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-24 09:38:22,463 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-24 09:38:22,464 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-24 09:38:22,464 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-24 09:38:22,465 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-24 09:38:22,465 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-24 09:38:22,466 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-09-24 09:38:22,467 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-09-24 09:38:22,467 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-24 09:38:22,468 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-24 09:38:22,468 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-24 09:38:22,469 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-24 09:38:22,469 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): custom_sell_atr_factor = 4.5
2025-09-24 09:38:22,470 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-24 09:38:22,470 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 8
2025-09-24 09:38:22,470 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-24 09:38:22,471 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-24 09:38:22,471 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-24 09:38:22,471 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-24 09:38:22,472 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-24 09:38:22,472 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-24 09:38:22,476 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 09:38:22,491 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 09:38:22,506 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 09:38:22,531 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 09:38:36,719 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 09:38:36,734 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 09:38:36,748 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 09:38:36,768 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 09:38:50,702 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 09:38:50,720 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 09:38:50,734 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 09:38:50,758 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-15 00:00:00
2025-09-24 09:39:04,750 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 09:39:04,764 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 09:39:04,779 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 09:39:04,799 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 09:39:19,320 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 09:39:19,335 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 09:39:19,348 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 09:39:19,369 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 09:39:33,599 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 09:46:26,196 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-24_09-46-26.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │    150 │         1.21 │        1047.356 │       104.74 │ 2 days, 12:30:00 │   64     0    86  42.7 │
│ BTC/USDT │    173 │         0.81 │         814.312 │        81.43 │ 2 days, 13:01:00 │   73     0   100  42.2 │
│ BNB/USDT │    152 │         0.98 │         399.562 │        39.96 │  2 days, 8:00:00 │   51     0   101  33.6 │
│ LTC/USDT │    113 │         -0.0 │         -25.784 │        -2.58 │  2 days, 1:29:00 │   39     0    74  34.5 │
│ XRP/USDT │    115 │         0.29 │        -240.978 │        -24.1 │  1 day, 21:15:00 │   24     0    91  20.9 │
│    TOTAL │    703 │         0.72 │        1994.468 │       199.45 │  2 days, 7:23:00 │  251     0   452  35.7 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                            LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         3.08 │          45.024 │          4.5 │ 4 days, 6:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         3.08 │          45.024 │          4.5 │ 4 days, 6:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                        ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │     555 │         0.55 │        1081.256 │       108.13 │  2 days, 6:36:00 │  196     0   359  35.3 │
│      engulfing_rebond │      73 │         1.49 │         502.885 │        50.29 │ 2 days, 11:52:00 │   26     0    47  35.6 │
│         hammer_rebond │      75 │         1.23 │         410.327 │        41.03 │  2 days, 8:54:00 │   29     0    46  38.7 │
│                 TOTAL │     703 │         0.72 │        1994.468 │       199.45 │  2 days, 7:23:00 │  251     0   452  35.7 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │    61 │         17.3 │        6417.133 │       641.71 │ 3 days, 16:21:00 │   61     0     0   100 │
│     force_exit │     1 │         3.08 │          45.024 │          4.5 │  4 days, 6:00:00 │    1     0     0   100 │
│      stop_loss │    35 │        -5.72 │       -1466.779 │      -146.68 │         20:23:00 │    0     0    35     0 │
│    exit_signal │   606 │        -0.58 │       -3000.910 │      -300.09 │  2 days, 6:01:00 │  189     0   417  31.2 │
│          TOTAL │   703 │         0.72 │        1994.468 │       199.45 │  2 days, 7:23:00 │  251     0   452  35.7 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                                MIXED TAG STATS                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_3R │     48 │         16.5 │        4885.198 │       488.52 │ 3 days, 12:33:00 │   48     0     0   100 │
│      engulfing_rebond │ take_profit_3R │      7 │        20.36 │         832.689 │        83.27 │  4 days, 9:39:00 │    7     0     0   100 │
│         hammer_rebond │ take_profit_3R │      6 │        20.17 │         699.246 │        69.92 │  4 days, 2:31:00 │    6     0     0   100 │
│ strong_bullish_rebond │     force_exit │      1 │         3.08 │          45.024 │          4.5 │  4 days, 6:00:00 │    1     0     0   100 │
│         hammer_rebond │    exit_signal │     65 │        -0.13 │        -128.430 │       -12.84 │  2 days, 7:32:00 │   23     0    42  35.4 │
│      engulfing_rebond │      stop_loss │      3 │        -8.53 │        -150.270 │       -15.03 │         22:23:00 │    0     0     3     0 │
│         hammer_rebond │      stop_loss │      4 │        -5.13 │        -160.489 │       -16.05 │         16:44:00 │    0     0     4     0 │
│      engulfing_rebond │    exit_signal │     63 │        -0.13 │        -179.534 │       -17.95 │  2 days, 8:33:00 │   19     0    44  30.2 │
│ strong_bullish_rebond │      stop_loss │     28 │         -5.5 │       -1156.020 │       -115.6 │         20:41:00 │    0     0    28     0 │
│ strong_bullish_rebond │    exit_signal │    478 │         -0.7 │       -2692.945 │      -269.29 │  2 days, 5:28:00 │  147     0   331  30.8 │
│                 TOTAL │                │    703 │         0.72 │        1994.468 │       199.45 │  2 days, 7:23:00 │  251     0   452  35.7 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2020-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 703 / 0.34                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 2994.468 USDT                  │
│ Absolute profit               │ 1994.468 USDT                  │
│ Total profit %                │ 199.45%                        │
│ CAGR %                        │ 21.23%                         │
│ Sortino                       │ 1.32                           │
│ Sharpe                        │ 0.43                           │
│ Calmar                        │ 6.76                           │
│ SQN                           │ 1.77                           │
│ Profit factor                 │ 1.23                           │
│ Expectancy (Ratio)            │ 2.84 (0.15)                    │
│ Avg. daily profit             │ 0.959 USDT                     │
│ Avg. stake amount             │ 803.729 USDT                   │
│ Total trade volume            │ 1134303.839 USDT               │
│                               │                                │
│ Best Pair                     │ ETH/USDT 104.74%               │
│ Worst Pair                    │ XRP/USDT -24.10%               │
│ Best trade                    │ BNB/USDT 38.12%                │
│ Worst trade                   │ LTC/USDT -11.67%               │
│ Best day                      │ 188.819 USDT                   │
│ Worst day                     │ -118.514 USDT                  │
│ Days win/draw/lose            │ 184 / 1558 / 298               │
│ Min/Max/Avg. Duration Winners │ 0d 10:20 / 9d 20:25 / 3d 20:23 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:15 / 4d 07:00 / 1d 10:51 │
│ Max Consecutive Wins / Loss   │ 8 / 21                         │
│ Rejected Entry signals        │ 2319                           │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 932.631 USDT                   │
│ Max balance                   │ 3384.948 USDT                  │
│ Max % of account underwater   │ 27.13%                         │
│ Absolute drawdown             │ 857.16 USDT (27.13%)           │
│ Drawdown duration             │ 255 days 06:00:00              │
│ Profit at drawdown start      │ 2159.897 USDT                  │
│ Profit at drawdown end        │ 1302.737 USDT                  │
│ Drawdown start                │ 2023-01-15 09:00:00            │
│ Drawdown end                  │ 2023-09-27 15:00:00            │
│ Market change                 │ 2537.81%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2020-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                  
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃            Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    703 │         0.72 │        1994.468 │       199.45 │ 2 days, 7:23:00 │  251     0   452  35.7 │ 857.16 USDT  27.13% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴─────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-24T11:46:28.278354",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 9279,
  "total_daily_avg_trades": "703 / 0.34",
  "absolute_profit_usdt": 1994.468,
  "total_profit_pct": 199.45,
  "cagr_pct": 21.23,
  "sortino": 1.32,
  "sharpe": 0.43,
  "calmar": 6.76,
  "sqn": 1.77,
  "max_consecutive_wins_loss": "8 / 21",
  "min_balance_usdt": 932.631,
  "max_balance_usdt": 3384.948,
  "absolute_drawdown_pct": 27.13,
  "market_change_pct": 2537.81
}
```
