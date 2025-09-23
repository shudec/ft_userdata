# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 5621  
**Timestamp:** 2025-09-23 22:07:59

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 5621,
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
2025-09-23 20:06:27,129 - freqtrade - INFO - freqtrade 2025.7
2025-09-23 20:06:27,464 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-23 20:06:27,464 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-23 20:06:28,971 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-23 20:06:28,974 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-23 20:06:28,974 - freqtrade.loggers - INFO - Logfile configured
2025-09-23 20:06:28,975 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-23 20:06:28,975 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-23 20:06:28,975 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-23 20:06:28,976 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-23 20:06:28,976 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20240101-20251231 ...
2025-09-23 20:06:28,984 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-23 20:06:28,985 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-23 20:06:28,986 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-23 20:06:28,986 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-23 20:06:28,987 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-23 20:06:28,987 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20240101-20251231
2025-09-23 20:06:28,989 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-23 20:06:29,008 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-23 20:06:29,009 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 20:06:29,012 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-23 20:06:29,014 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-23 20:06:29,014 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-23 20:06:29,049 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-23 20:06:31,454 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-23 20:06:31,493 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-23 20:06:31,493 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-23 20:06:31,494 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-23 20:06:31,495 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-23 20:06:31,495 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-23 20:06:31,496 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-23 20:06:31,496 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-23 20:06:31,496 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-23 20:06:31,497 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-23 20:06:31,497 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-23 20:06:31,497 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-23 20:06:31,498 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-23 20:06:31,498 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-23 20:06:31,498 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-23 20:06:31,499 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-23 20:06:31,499 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-23 20:06:31,499 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-23 20:06:31,500 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-23 20:06:31,500 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-23 20:06:31,500 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-23 20:06:31,501 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-23 20:06:31,501 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-23 20:06:31,501 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-23 20:06:31,502 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-23 20:06:31,502 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-23 20:06:31,502 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-23 20:06:31,503 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-23 20:06:31,503 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-23 20:06:31,503 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-23 20:06:31,504 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-23 20:06:31,504 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 20:06:31,509 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-23 20:06:31,541 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-23 20:06:31,571 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 20:06:31,612 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 20:06:31,648 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 20:06:31,684 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 20:06:31,719 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 20:06:31,737 - freqtrade.optimize.backtesting - INFO - Loading data from 2024-01-01 00:00:00 up to 2025-09-11 17:00:00 (619 days).
2025-09-23 20:06:31,809 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 20:06:31,948 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 20:06:32,087 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 20:06:32,218 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 20:06:32,349 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 20:06:33,005 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-23 20:06:33,006 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-23 20:06:33,006 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-23 20:06:33,007 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-23 20:06:33,007 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-23 20:06:33,008 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-23 20:06:33,008 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-23 20:06:33,008 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-23 20:06:33,009 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-23 20:06:33,009 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-23 20:06:33,009 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-23 20:06:33,010 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-23 20:06:33,010 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-09-23 20:06:33,010 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-09-23 20:06:33,011 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-23 20:06:33,011 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-23 20:06:33,011 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-23 20:06:33,012 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-23 20:06:33,012 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-23 20:06:33,012 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 1
2025-09-23 20:06:33,013 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-23 20:06:33,013 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-23 20:06:33,013 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-23 20:06:33,014 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower
2025-09-23 20:06:33,014 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-23 20:06:33,014 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-23 20:06:33,016 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:06:33,025 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 20:06:33,041 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:06:33,058 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 20:06:36,049 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:06:36,056 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 20:06:36,071 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:06:36,088 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 20:06:38,974 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:06:38,981 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 20:06:38,997 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:06:39,015 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 20:06:42,047 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:06:42,054 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 20:06:42,070 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:06:42,086 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 20:06:45,010 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:06:45,017 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 20:06:45,032 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:06:45,048 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 20:06:48,047 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2024-01-01 00:00:00 up to 2025-09-11 17:00:00 (619 days).
2025-09-23 20:07:58,896 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-23_20-07-58.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │     54 │         0.88 │          91.807 │         9.18 │ 2 days, 19:03:00 │   23     0    31  42.6 │
│ LTC/USDT │     32 │         1.21 │          84.008 │          8.4 │  1 day, 22:52:00 │   12     0    20  37.5 │
│ ETH/USDT │     43 │         0.18 │          11.822 │         1.18 │  2 days, 5:29:00 │   19     0    24  44.2 │
│ XRP/USDT │     43 │        -0.07 │          -5.859 │        -0.59 │  1 day, 15:17:00 │   10     0    33  23.3 │
│ BNB/USDT │     59 │        -0.19 │         -31.105 │        -3.11 │  1 day, 23:53:00 │   14     0    45  23.7 │
│    TOTAL │    231 │         0.35 │         150.672 │        15.07 │  2 days, 3:40:00 │   78     0   153  33.8 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         4.38 │           9.978 │          1.0 │ 5 days, 15:00:00 │    1     0     0   100 │
│ BTC/USDT │      1 │        -0.12 │          -0.280 │        -0.03 │         13:00:00 │    0     0     1     0 │
│ LTC/USDT │      1 │        -3.08 │          -7.017 │         -0.7 │         17:00:00 │    0     0     1     0 │
│    TOTAL │      3 │         0.39 │           2.681 │         0.27 │  2 days, 7:00:00 │    1     0     2  33.3 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                       ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │     192 │         0.32 │         115.452 │        11.55 │ 2 days, 3:56:00 │   66     0   126  34.4 │
│      engulfing_rebond │      26 │         1.23 │          65.744 │         6.57 │ 2 days, 3:35:00 │    9     0    17  34.6 │
│         hammer_rebond │      13 │        -1.02 │         -30.524 │        -3.05 │ 1 day, 23:53:00 │    3     0    10  23.1 │
│                 TOTAL │     231 │         0.35 │         150.672 │        15.07 │ 2 days, 3:40:00 │   78     0   153  33.8 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │    32 │        10.42 │         721.481 │        72.15 │ 2 days, 6:19:00 │   32     0     0   100 │
│     force_exit │     3 │         0.39 │           2.681 │         0.27 │ 2 days, 7:00:00 │    1     0     2  33.3 │
│      stop_loss │     2 │       -10.18 │         -49.481 │        -4.95 │  1 day, 1:28:00 │    0     0     2     0 │
│    exit_signal │   194 │        -1.21 │        -524.009 │        -52.4 │ 2 days, 3:27:00 │   45     0   149  23.2 │
│          TOTAL │   231 │         0.35 │         150.672 │        15.07 │ 2 days, 3:40:00 │   78     0   153  33.8 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                                MIXED TAG STATS                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_1R │     25 │        10.44 │         561.415 │        56.14 │  2 days, 4:07:00 │   25     0     0   100 │
│      engulfing_rebond │ take_profit_1R │      6 │        10.37 │         136.610 │        13.66 │ 2 days, 17:49:00 │    6     0     0   100 │
│         hammer_rebond │ take_profit_1R │      1 │        10.13 │          23.457 │         2.35 │  1 day, 16:05:00 │    1     0     0   100 │
│ strong_bullish_rebond │     force_exit │      2 │         0.65 │           2.961 │          0.3 │  3 days, 4:00:00 │    1     0     1  50.0 │
│      engulfing_rebond │     force_exit │      1 │        -0.12 │          -0.280 │        -0.03 │         13:00:00 │    0     0     1     0 │
│         hammer_rebond │      stop_loss │      1 │       -10.18 │         -24.617 │        -2.46 │   1 day, 7:30:00 │    0     0     1     0 │
│      engulfing_rebond │      stop_loss │      1 │       -10.18 │         -24.864 │        -2.49 │         19:25:00 │    0     0     1     0 │
│         hammer_rebond │    exit_signal │     11 │         -1.2 │         -29.364 │        -2.94 │  2 days, 2:05:00 │    2     0     9  18.2 │
│      engulfing_rebond │    exit_signal │     18 │        -1.11 │         -45.721 │        -4.57 │  2 days, 2:47:00 │    3     0    15  16.7 │
│ strong_bullish_rebond │    exit_signal │    165 │        -1.22 │        -448.923 │       -44.89 │  2 days, 3:37:00 │   40     0   125  24.2 │
│                 TOTAL │                │    231 │         0.35 │         150.672 │        15.07 │  2 days, 3:40:00 │   78     0   153  33.8 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2024-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-11 17:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 231 / 0.37                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1150.672 USDT                  │
│ Absolute profit               │ 150.672 USDT                   │
│ Total profit %                │ 15.07%                         │
│ CAGR %                        │ 8.63%                          │
│ Sortino                       │ 1.13                           │
│ Sharpe                        │ 0.45                           │
│ Calmar                        │ 2.94                           │
│ SQN                           │ 0.96                           │
│ Profit factor                 │ 1.19                           │
│ Expectancy (Ratio)            │ 0.65 (0.12)                    │
│ Avg. daily profit             │ 0.243 USDT                     │
│ Avg. stake amount             │ 218.004 USDT                   │
│ Total trade volume            │ 101070.415 USDT                │
│                               │                                │
│ Best Pair                     │ BTC/USDT 9.18%                 │
│ Worst Pair                    │ BNB/USDT -3.11%                │
│ Best trade                    │ LTC/USDT 12.16%                │
│ Worst trade                   │ BTC/USDT -10.18%               │
│ Best day                      │ 64.649 USDT                    │
│ Worst day                     │ -30.746 USDT                   │
│ Days win/draw/lose            │ 54 / 425 / 99                  │
│ Min/Max/Avg. Duration Winners │ 0d 04:50 / 6d 21:00 / 3d 10:13 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 4d 07:00 / 1d 12:05 │
│ Max Consecutive Wins / Loss   │ 8 / 15                         │
│ Rejected Entry signals        │ 751                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 1005.166 USDT                  │
│ Max balance                   │ 1237.882 USDT                  │
│ Max % of account underwater   │ 15.82%                         │
│ Absolute Drawdown (Account)   │ 15.82%                         │
│ Absolute Drawdown             │ 195.881 USDT                   │
│ Drawdown high                 │ 237.882 USDT                   │
│ Drawdown low                  │ 42.001 USDT                    │
│ Drawdown Start                │ 2024-12-01 19:50:00            │
│ Drawdown End                  │ 2025-05-04 03:00:00            │
│ Market change                 │ 178.91%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2024-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    231 │         0.35 │         150.672 │        15.07 │ 2 days, 3:40:00 │   78     0   153  33.8 │ 195.881 USDT  15.82% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-23T22:07:59.965990",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 5621,
  "total_daily_avg_trades": "231 / 0.37",
  "absolute_profit_usdt": 150.672,
  "total_profit_pct": 15.07,
  "cagr_pct": 8.63,
  "sortino": 1.13,
  "sharpe": 0.45,
  "calmar": 2.94,
  "sqn": 0.96,
  "max_consecutive_wins_loss": "8 / 15",
  "min_balance_usdt": 1005.166,
  "max_balance_usdt": 1237.882,
  "market_change_pct": 178.91
}
```
