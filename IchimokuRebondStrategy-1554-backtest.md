# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 1554  
**Timestamp:** 2025-09-24 21:29:32

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 1554,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20231231",
  "backtest_timerange": "20240101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20240101-20251231
```

## Backtesting Output
```
2025-09-24 19:27:10,929 - freqtrade - INFO - freqtrade 2025.7
2025-09-24 19:27:11,258 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-24 19:27:11,259 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-24 19:27:12,742 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-24 19:27:12,746 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-24 19:27:12,746 - freqtrade.loggers - INFO - Logfile configured
2025-09-24 19:27:12,747 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-24 19:27:12,747 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-24 19:27:12,748 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-24 19:27:12,748 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-24 19:27:12,749 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20240101-20251231 ...
2025-09-24 19:27:12,758 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-24 19:27:12,759 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-24 19:27:12,759 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-24 19:27:12,760 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-24 19:27:12,760 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-24 19:27:12,761 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20240101-20251231
2025-09-24 19:27:12,763 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-24 19:27:12,782 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-24 19:27:12,783 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 19:27:12,786 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-24 19:27:12,787 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-24 19:27:12,788 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-24 19:27:12,819 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-24 19:27:15,623 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-24 19:27:15,661 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-24 19:27:15,662 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-24 19:27:15,663 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-24 19:27:15,663 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-24 19:27:15,664 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-24 19:27:15,664 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-24 19:27:15,665 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-24 19:27:15,665 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-24 19:27:15,666 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-24 19:27:15,666 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-24 19:27:15,666 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-24 19:27:15,667 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-24 19:27:15,667 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-24 19:27:15,667 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-24 19:27:15,668 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-24 19:27:15,668 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-24 19:27:15,668 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-24 19:27:15,669 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-24 19:27:15,669 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-24 19:27:15,670 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-24 19:27:15,670 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-24 19:27:15,670 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-24 19:27:15,671 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-24 19:27:15,671 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-24 19:27:15,672 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-24 19:27:15,672 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-24 19:27:15,672 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-24 19:27:15,673 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-24 19:27:15,673 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-24 19:27:15,674 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-24 19:27:15,674 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 19:27:15,680 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-24 19:27:15,713 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-24 19:27:15,744 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-24 19:27:15,786 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-24 19:27:15,829 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-24 19:27:15,875 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-24 19:27:15,919 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-24 19:27:15,941 - freqtrade.optimize.backtesting - INFO - Loading data from 2024-01-01 00:00:00 up to 2025-09-11 17:00:00 (619 days).
2025-09-24 19:27:16,017 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-24 19:27:16,165 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-24 19:27:16,298 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-24 19:27:16,427 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-24 19:27:16,565 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-24 19:27:17,314 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-24 19:27:17,315 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-24 19:27:17,316 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-24 19:27:17,316 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-24 19:27:17,317 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-24 19:27:17,317 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-24 19:27:17,318 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-24 19:27:17,318 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 10
2025-09-24 19:27:17,318 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-24 19:27:17,319 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-24 19:27:17,319 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-24 19:27:17,320 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-24 19:27:17,320 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.007
2025-09-24 19:27:17,320 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-24 19:27:17,321 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-24 19:27:17,321 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-24 19:27:17,321 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.007
2025-09-24 19:27:17,322 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.25
2025-09-24 19:27:17,322 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1.5
2025-09-24 19:27:17,323 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-09-24 19:27:17,323 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.998
2025-09-24 19:27:17,323 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 1
2025-09-24 19:27:17,324 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.996
2025-09-24 19:27:17,324 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-24 19:27:17,325 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-24 19:27:17,325 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = none
2025-09-24 19:27:17,325 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-09-24 19:27:17,326 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-24 19:27:17,326 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-24 19:27:17,327 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-24 19:27:17,327 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-24 19:27:17,329 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 19:27:17,339 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-24 19:27:17,357 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 19:27:17,374 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-24 19:27:21,043 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 19:27:21,050 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-24 19:27:21,067 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 19:27:21,084 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-24 19:27:24,448 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 19:27:24,456 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-24 19:27:24,474 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 19:27:24,493 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-24 19:27:27,928 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 19:27:27,936 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-24 19:27:27,953 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 19:27:27,973 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-24 19:27:32,054 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 19:27:32,064 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-24 19:27:32,084 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 19:27:32,105 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-24 19:27:36,777 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2024-01-01 00:00:00 up to 2025-09-11 17:00:00 (619 days).
2025-09-24 19:29:31,218 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-24_19-29-31.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │     48 │         3.45 │         434.858 │        43.49 │  2 days, 2:30:00 │   12     0    36  25.0 │
│ BTC/USDT │     62 │         0.92 │         125.675 │        12.57 │ 2 days, 22:06:00 │   25     0    37  40.3 │
│ ETH/USDT │     48 │         0.72 │          85.357 │         8.54 │ 2 days, 15:06:00 │   20     0    28  41.7 │
│ LTC/USDT │     50 │         0.23 │          15.005 │          1.5 │  2 days, 1:18:00 │   17     0    33  34.0 │
│ BNB/USDT │     72 │         0.13 │         -13.248 │        -1.32 │ 2 days, 11:54:00 │   24     0    48  33.3 │
│    TOTAL │    280 │         0.99 │         647.647 │        64.76 │ 2 days, 11:12:00 │   98     0   182  35.0 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         4.38 │          14.179 │         1.42 │ 5 days, 15:00:00 │    1     0     0   100 │
│ BTC/USDT │      1 │         0.27 │           0.872 │         0.09 │   1 day, 3:00:00 │    1     0     0   100 │
│ XRP/USDT │      1 │        -0.99 │          -3.196 │        -0.32 │  2 days, 9:00:00 │    0     0     1     0 │
│    TOTAL │      3 │         1.22 │          11.855 │         1.19 │  3 days, 1:00:00 │    2     0     1  66.7 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                        ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │     232 │         0.87 │         512.800 │        51.28 │ 2 days, 11:05:00 │   80     0   152  34.5 │
│      engulfing_rebond │      22 │         3.01 │         137.147 │        13.71 │ 2 days, 22:30:00 │   10     0    12  45.5 │
│         hammer_rebond │      26 │         0.34 │          -2.301 │        -0.23 │  2 days, 2:48:00 │    8     0    18  30.8 │
│                 TOTAL │     280 │         0.99 │         647.647 │        64.76 │ 2 days, 11:12:00 │   98     0   182  35.0 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                         EXIT REASON STATS                                                         
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                 Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│              take_profit_3R │    12 │        30.94 │         976.888 │        97.69 │ 3 days, 22:17:00 │   12     0     0   100 │
│                  force_exit │     3 │         1.22 │          11.855 │         1.19 │  3 days, 1:00:00 │    2     0     1  66.7 │
│ ichimoku_cloud_crossed_exit │   259 │        -0.14 │        -157.491 │       -15.75 │ 2 days, 10:16:00 │   84     0   175  32.4 │
│                   stop_loss │     6 │       -10.18 │        -183.605 │       -18.36 │         22:26:00 │    0     0     6     0 │
│                       TOTAL │   280 │         0.99 │         647.647 │        64.76 │ 2 days, 11:12:00 │   98     0   182  35.0 │
└─────────────────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                                      MIXED TAG STATS                                                                       
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃                 Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │              take_profit_3R │      9 │        31.17 │         774.762 │        77.48 │  3 days, 6:33:00 │    9     0     0   100 │
│      engulfing_rebond │              take_profit_3R │      2 │        30.35 │         133.942 │        13.39 │ 4 days, 20:55:00 │    2     0     0   100 │
│         hammer_rebond │              take_profit_3R │      1 │         30.1 │          68.184 │         6.82 │ 7 days, 22:35:00 │    1     0     0   100 │
│ strong_bullish_rebond │                  force_exit │      3 │         1.22 │          11.855 │         1.19 │  3 days, 1:00:00 │    2     0     1  66.7 │
│      engulfing_rebond │ ichimoku_cloud_crossed_exit │     20 │         0.28 │           3.205 │         0.32 │ 2 days, 17:51:00 │    8     0    12  40.0 │
│         hammer_rebond │                   stop_loss │      1 │       -10.18 │         -34.611 │        -3.46 │         11:10:00 │    0     0     1     0 │
│         hammer_rebond │ ichimoku_cloud_crossed_exit │     24 │        -0.47 │         -35.874 │        -3.59 │  1 day, 22:38:00 │    7     0    17  29.2 │
│ strong_bullish_rebond │ ichimoku_cloud_crossed_exit │    215 │        -0.14 │        -124.822 │       -12.48 │ 2 days, 10:52:00 │   69     0   146  32.1 │
│ strong_bullish_rebond │                   stop_loss │      5 │       -10.18 │        -148.994 │        -14.9 │   1 day, 0:41:00 │    0     0     5     0 │
│                 TOTAL │                             │    280 │         0.99 │         647.647 │        64.76 │ 2 days, 11:12:00 │   98     0   182  35.0 │
└───────────────────────┴─────────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2024-01-01 00:00:00             │
│ Backtesting to                │ 2025-09-11 17:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 280 / 0.45                      │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 1647.647 USDT                   │
│ Absolute profit               │ 647.647 USDT                    │
│ Total profit %                │ 64.76%                          │
│ CAGR %                        │ 34.24%                          │
│ Sortino                       │ 3.26                            │
│ Sharpe                        │ 0.98                            │
│ Calmar                        │ 9.97                            │
│ SQN                           │ 1.89                            │
│ Profit factor                 │ 1.52                            │
│ Expectancy (Ratio)            │ 2.31 (0.34)                     │
│ Avg. daily profit             │ 1.046 USDT                      │
│ Avg. stake amount             │ 267.179 USDT                    │
│ Total trade volume            │ 150568.581 USDT                 │
│                               │                                 │
│ Best Pair                     │ XRP/USDT 43.49%                 │
│ Worst Pair                    │ BNB/USDT -1.32%                 │
│ Best trade                    │ XRP/USDT 33.77%                 │
│ Worst trade                   │ LTC/USDT -10.18%                │
│ Best day                      │ 184.427 USDT                    │
│ Worst day                     │ -35.648 USDT                    │
│ Days win/draw/lose            │ 63 / 406 / 116                  │
│ Min/Max/Avg. Duration Winners │ 0d 23:40 / 10d 15:00 / 4d 05:18 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 3d 21:00 / 1d 12:32  │
│ Max Consecutive Wins / Loss   │ 7 / 16                          │
│ Rejected Entry signals        │ 3544                            │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 997.088 USDT                    │
│ Max balance                   │ 1754.888 USDT                   │
│ Max % of account underwater   │ 20.05%                          │
│ Absolute Drawdown (Account)   │ 20.05%                          │
│ Absolute Drawdown             │ 351.777 USDT                    │
│ Drawdown high                 │ 754.888 USDT                    │
│ Drawdown low                  │ 403.111 USDT                    │
│ Drawdown Start                │ 2024-12-02 14:40:00             │
│ Drawdown End                  │ 2025-07-08 15:00:00             │
│ Market change                 │ 178.91%                         │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2024-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    280 │         0.99 │         647.647 │        64.76 │ 2 days, 11:12:00 │   98     0   182  35.0 │ 351.777 USDT  20.05% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-24T21:29:32.382030",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 1554,
  "total_daily_avg_trades": "280 / 0.45",
  "absolute_profit_usdt": 647.647,
  "total_profit_pct": 64.76,
  "cagr_pct": 34.24,
  "sortino": 3.26,
  "sharpe": 0.98,
  "calmar": 9.97,
  "sqn": 1.89,
  "max_consecutive_wins_loss": "7 / 16",
  "min_balance_usdt": 997.088,
  "max_balance_usdt": 1754.888,
  "market_change_pct": 178.91
}
```
