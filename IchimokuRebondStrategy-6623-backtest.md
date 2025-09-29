# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 6623  
**Timestamp:** 2025-09-29 10:09:08

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 6623,
  "epochs": 100,
  "hyperopt_timerange": "20220101-20231231",
  "backtest_timerange": "20220101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231 --export trades --export-filename backtest-result.csv
```

## Backtesting Output
```
2025-09-29 08:06:41,102 - freqtrade - INFO - freqtrade 2025.8
2025-09-29 08:06:41,844 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-29 08:06:44,602 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-29 08:06:44,610 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-29 08:06:44,611 - freqtrade.loggers - INFO - Logfile configured
2025-09-29 08:06:44,611 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-29 08:06:44,612 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-29 08:06:44,612 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-29 08:06:44,613 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-29 08:06:44,613 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-29 08:06:45,221 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-29 08:06:45,223 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-29 08:06:45,224 - freqtrade.configuration.configuration - INFO - Storing backtest results to backtest-result.csv ...
2025-09-29 08:06:45,224 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-29 08:06:45,225 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-09-29 08:06:45,225 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-29 08:06:45,226 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-29 08:06:45,226 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-29 08:06:45,228 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-29 08:06:45,244 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-29 08:06:45,244 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-29 08:06:45,248 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-29 08:06:45,249 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-29 08:06:45,249 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-29 08:06:45,273 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-29 08:06:55,804 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-29 08:06:55,967 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-29 08:06:55,970 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-29 08:06:55,975 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-29 08:06:55,976 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-29 08:06:55,977 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-29 08:06:55,977 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-29 08:06:55,978 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-29 08:06:55,979 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-29 08:06:55,979 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-29 08:06:55,980 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-29 08:06:55,981 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-29 08:06:55,981 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-29 08:06:55,982 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-29 08:06:55,983 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-29 08:06:55,984 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-29 08:06:55,985 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-29 08:06:55,986 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-29 08:06:55,987 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-29 08:06:55,987 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-29 08:06:55,988 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-29 08:06:55,989 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-29 08:06:55,990 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-29 08:06:55,991 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-29 08:06:55,992 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-29 08:06:55,993 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-29 08:06:55,993 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-29 08:06:55,994 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-29 08:06:55,995 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-29 08:06:55,995 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-29 08:06:55,996 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-29 08:06:55,997 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-29 08:06:56,029 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-29 08:06:56,069 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-29 08:06:56,212 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-29 08:06:56,364 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-29 08:06:56,456 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-29 08:06:56,533 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-29 08:06:56,607 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-29 08:06:56,633 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-29 08:06:57,038 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-29 08:06:57,613 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-29 08:06:58,100 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-29 08:06:58,617 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-29 08:06:59,100 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-29 08:07:00,486 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-29 08:07:00,494 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-29 08:07:00,495 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-29 08:07:00,495 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.4
2025-09-29 08:07:00,496 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-29 08:07:00,496 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-29 08:07:00,497 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-29 08:07:00,497 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_strength_threshold = 0.02
2025-09-29 08:07:00,498 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 5
2025-09-29 08:07:00,498 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-09-29 08:07:00,499 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 1
2025-09-29 08:07:00,499 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-09-29 08:07:00,499 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.02
2025-09-29 08:07:00,500 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.003
2025-09-29 08:07:00,500 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-29 08:07:00,501 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-29 08:07:00,501 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_size_threshold = 2
2025-09-29 08:07:00,501 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_strength_threshold = 0.02
2025-09-29 08:07:00,502 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.409
2025-09-29 08:07:00,502 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.003
2025-09-29 08:07:00,502 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_engulfing_entry = False
2025-09-29 08:07:00,503 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_hammer_entry = True
2025-09-29 08:07:00,503 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_strong_bullish_entry = False
2025-09-29 08:07:00,504 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 2.5
2025-09-29 08:07:00,504 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 0.5
2025-09-29 08:07:00,505 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-09-29 08:07:00,505 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-29 08:07:00,505 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 6
2025-09-29 08:07:00,506 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-29 08:07:00,506 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-29 08:07:00,507 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-09-29 08:07:00,507 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-29 08:07:00,508 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-29 08:07:00,509 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-09-29 08:07:00,509 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-29 08:07:00,510 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-29 08:07:00,511 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-29 08:07:00,511 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-29 08:07:00,514 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 08:07:00,539 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-29 08:07:00,569 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 08:07:00,601 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-29 08:07:13,434 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 08:07:13,458 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-29 08:07:13,473 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 08:07:13,498 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-29 08:07:23,708 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 08:07:23,729 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-29 08:07:23,748 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 08:07:23,780 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-15 00:00:00
2025-09-29 08:07:34,240 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 08:07:34,264 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-29 08:07:34,294 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 08:07:34,341 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-29 08:07:45,120 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 08:07:45,151 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-29 08:07:45,172 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 08:07:45,203 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-29 08:07:55,810 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-29 08:09:07,527 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-29_08-09-07.meta.json"
Logging 19 entries for {'pair': 'BTC/USDT'} with tag hammer_rebond
Logging 14 entries for {'pair': 'ETH/USDT'} with tag hammer_rebond
Logging 39 entries for {'pair': 'LTC/USDT'} with tag hammer_rebond
Logging 46 entries for {'pair': 'XRP/USDT'} with tag hammer_rebond
Logging 16 entries for {'pair': 'BNB/USDT'} with tag hammer_rebond
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │     15 │         0.56 │          21.950 │         2.19 │ 5 days, 17:07:00 │    7     0     8  46.7 │
│ BNB/USDT │     14 │         0.58 │          18.020 │          1.8 │  2 days, 8:01:00 │    6     0     8  42.9 │
│ ETH/USDT │     13 │         0.55 │           9.866 │         0.99 │  1 day, 21:28:00 │    5     0     8  38.5 │
│ XRP/USDT │     39 │         -0.6 │         -76.512 │        -7.65 │ 2 days, 11:22:00 │   15     0    24  38.5 │
│ LTC/USDT │     33 │        -1.09 │        -204.963 │        -20.5 │ 4 days, 10:34:00 │    7     0    26  21.2 │
│    TOTAL │    114 │        -0.31 │        -231.638 │       -23.16 │  3 days, 9:16:00 │   40     0    74  35.1 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ LTC/USDT │      1 │        -0.53 │          -0.686 │        -0.07 │ 52 days, 9:00:00 │    0     0     1     0 │
│    TOTAL │      1 │        -0.53 │          -0.686 │        -0.07 │ 52 days, 9:00:00 │    0     0     1     0 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                   ENTER TAG STATS                                                    
┏━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ hammer_rebond │     114 │        -0.31 │        -231.638 │       -23.16 │ 3 days, 9:16:00 │   40     0    74  35.1 │
│         TOTAL │     114 │        -0.31 │        -231.638 │       -23.16 │ 3 days, 9:16:00 │   40     0    74  35.1 │
└───────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                   EXIT REASON STATS                                                    
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │    40 │         7.83 │         878.703 │        87.87 │ 2 days, 17:33:00 │   40     0     0   100 │
│       force_exit │     1 │        -0.53 │          -0.686 │        -0.07 │ 52 days, 9:00:00 │    0     0     1     0 │
│        stop_loss │    73 │        -4.77 │       -1109.656 │      -110.97 │  3 days, 1:46:00 │    0     0    73     0 │
│            TOTAL │   114 │        -0.31 │        -231.638 │       -23.16 │  3 days, 9:16:00 │   40     0    74  35.1 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                             MIXED TAG STATS                                                             
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ hammer_rebond │ take_profit_1.5R │     40 │         7.83 │         878.703 │        87.87 │ 2 days, 17:33:00 │   40     0     0   100 │
│ hammer_rebond │       force_exit │      1 │        -0.53 │          -0.686 │        -0.07 │ 52 days, 9:00:00 │    0     0     1     0 │
│ hammer_rebond │        stop_loss │     73 │        -4.77 │       -1109.656 │      -110.97 │  3 days, 1:46:00 │    0     0    73     0 │
│         TOTAL │                  │    114 │        -0.31 │        -231.638 │       -23.16 │  3 days, 9:16:00 │   40     0    74  35.1 │
└───────────────┴──────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00             │
│ Backtesting to                │ 2025-09-10 08:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 114 / 0.08                      │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 768.362 USDT                    │
│ Absolute profit               │ -231.638 USDT                   │
│ Total profit %                │ -23.16%                         │
│ CAGR %                        │ -6.89%                          │
│ Sortino                       │ -0.73                           │
│ Sharpe                        │ -0.18                           │
│ Calmar                        │ -1.16                           │
│ SQN                           │ -1.16                           │
│ Profit factor                 │ 0.79                            │
│ Expectancy (Ratio)            │ -2.03 (-0.14)                   │
│ Avg. daily profit             │ -0.172 USDT                     │
│ Avg. stake amount             │ 352.553 USDT                    │
│ Total trade volume            │ 80310.837 USDT                  │
│                               │                                 │
│ Best Pair                     │ BTC/USDT 2.19%                  │
│ Worst Pair                    │ LTC/USDT -20.50%                │
│ Best trade                    │ LTC/USDT 22.95%                 │
│ Worst trade                   │ XRP/USDT -14.87%                │
│ Best day                      │ 50.197 USDT                     │
│ Worst day                     │ -39 USDT                        │
│ Days win/draw/lose            │ 36 / 1231 / 62                  │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 12d 17:30 / 2d 17:33 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 52d 09:00 / 3d 17:45 │
│ Max Consecutive Wins / Loss   │ 6 / 11                          │
│ Rejected Entry signals        │ 24                              │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 747.851 USDT                    │
│ Max balance                   │ 1044.607 USDT                   │
│ Max % of account underwater   │ 28.41%                          │
│ Absolute drawdown             │ 296.756 USDT (28.41%)           │
│ Drawdown duration             │ 1008 days 06:00:00              │
│ Profit at drawdown start      │ 44.607 USDT                     │
│ Profit at drawdown end        │ -252.149 USDT                   │
│ Drawdown start                │ 2022-02-07 22:25:00             │
│ Drawdown end                  │ 2024-11-12 04:25:00             │
│ Market change                 │ 91.49%                          │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    114 │        -0.31 │        -231.638 │       -23.16 │ 3 days, 9:16:00 │   40     0    74  35.1 │ 296.756 USDT  28.41% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-29T10:09:08.916916",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 6623,
  "total_daily_avg_trades": "114 / 0.08",
  "absolute_profit_usdt": -231.638,
  "total_profit_pct": -23.16,
  "cagr_pct": -6.89,
  "sortino": -0.73,
  "sharpe": -0.18,
  "calmar": -1.16,
  "sqn": -1.16,
  "max_consecutive_wins_loss": "6 / 11",
  "min_balance_usdt": 747.851,
  "max_balance_usdt": 1044.607,
  "absolute_drawdown_pct": 28.41,
  "market_change_pct": 91.49
}
```
