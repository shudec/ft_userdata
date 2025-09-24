# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 8934  
**Timestamp:** 2025-09-24 11:21:03

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 8934,
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
2025-09-24 09:07:12,138 - freqtrade - INFO - freqtrade 2025.8
2025-09-24 09:07:12,766 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-24 09:07:15,623 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-24 09:07:15,631 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-24 09:07:15,632 - freqtrade.loggers - INFO - Logfile configured
2025-09-24 09:07:15,632 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-24 09:07:15,633 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-24 09:07:15,633 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-24 09:07:15,634 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-24 09:07:15,635 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20200101-20251231 ...
2025-09-24 09:07:16,133 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-24 09:07:16,136 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-24 09:07:16,137 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-24 09:07:16,138 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-24 09:07:16,138 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-24 09:07:16,139 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20200101-20251231
2025-09-24 09:07:16,141 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-24 09:07:16,153 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-24 09:07:16,154 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 09:07:16,157 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-24 09:07:16,158 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-24 09:07:16,159 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-24 09:07:16,182 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-24 09:07:18,777 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-24 09:07:18,919 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-24 09:07:18,922 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-24 09:07:18,928 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-24 09:07:18,929 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-24 09:07:18,930 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-24 09:07:18,930 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-24 09:07:18,931 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-24 09:07:18,931 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-24 09:07:18,932 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-24 09:07:18,932 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-24 09:07:18,932 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-24 09:07:18,933 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-24 09:07:18,933 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-24 09:07:18,933 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-24 09:07:18,934 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-24 09:07:18,934 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-24 09:07:18,935 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-24 09:07:18,936 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-24 09:07:18,936 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-24 09:07:18,937 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-24 09:07:18,938 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-24 09:07:18,938 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-24 09:07:18,939 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-24 09:07:18,939 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-24 09:07:18,939 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-24 09:07:18,940 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-24 09:07:18,940 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-24 09:07:18,941 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-24 09:07:18,941 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-24 09:07:18,942 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-24 09:07:18,943 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 09:07:18,975 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-24 09:07:19,007 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-24 09:07:19,098 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 09:07:19,256 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 09:07:19,359 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 09:07:19,454 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 09:07:19,557 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 09:07:19,615 - freqtrade.optimize.backtesting - INFO - Loading data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 09:07:20,093 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 09:07:20,806 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 09:07:21,512 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 09:07:22,558 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 09:07:23,519 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 09:07:25,963 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-24 09:07:25,969 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-24 09:07:25,970 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-24 09:07:25,971 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-24 09:07:25,971 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-24 09:07:25,971 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-24 09:07:25,972 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-24 09:07:25,972 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-24 09:07:25,973 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-24 09:07:25,973 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-24 09:07:25,973 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-24 09:07:25,974 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-24 09:07:25,975 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-09-24 09:07:25,975 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-09-24 09:07:25,976 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-24 09:07:25,976 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-24 09:07:25,976 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-24 09:07:25,977 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-24 09:07:25,978 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): custom_sell_atr_factor = 4.5
2025-09-24 09:07:25,979 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-24 09:07:25,979 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 8
2025-09-24 09:07:25,980 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-24 09:07:25,980 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-24 09:07:25,981 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-24 09:07:25,981 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-24 09:07:25,982 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-24 09:07:25,982 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-24 09:07:25,986 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 09:07:26,005 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 09:07:26,022 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 09:07:26,048 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 09:07:46,565 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 09:07:46,583 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 09:07:46,603 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 09:07:46,630 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 09:08:07,215 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 09:08:07,239 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 09:08:07,267 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 09:08:07,297 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-15 00:00:00
2025-09-24 09:08:27,241 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 09:08:27,265 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 09:08:27,287 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 09:08:27,319 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 09:08:43,910 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 09:08:43,930 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 09:08:43,950 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 09:08:43,976 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 09:09:01,009 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 09:21:01,792 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-24_09-21-01.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │    224 │         0.39 │         321.494 │        32.15 │ 1 day, 17:58:00 │  104     0   120  46.4 │
│ BNB/USDT │    180 │         0.53 │         195.062 │        19.51 │ 1 day, 22:36:00 │   71     0   109  39.4 │
│ ETH/USDT │    184 │         0.36 │         194.552 │        19.46 │ 1 day, 20:23:00 │   83     0   101  45.1 │
│ XRP/USDT │    132 │         0.63 │         172.795 │        17.28 │ 1 day, 12:21:00 │   44     0    88  33.3 │
│ LTC/USDT │    136 │        -0.21 │        -242.578 │       -24.26 │ 1 day, 17:03:00 │   49     0    87  36.0 │
│    TOTAL │    856 │         0.35 │         641.324 │        64.13 │ 1 day, 18:27:00 │  351     0   505  41.0 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                            LEFT OPEN TRADES REPORT                                            
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         0.07 │           0.585 │         0.06 │ 1 day, 1:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         0.07 │           0.585 │         0.06 │ 1 day, 1:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                       ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │     684 │         0.26 │         288.667 │        28.87 │ 1 day, 17:10:00 │  283     0   401  41.4 │
│         hammer_rebond │      86 │         0.93 │         234.882 │        23.49 │ 2 days, 3:19:00 │   35     0    51  40.7 │
│      engulfing_rebond │      86 │         0.55 │         117.775 │        11.78 │ 1 day, 19:43:00 │   33     0    53  38.4 │
│                 TOTAL │     856 │         0.35 │         641.324 │        64.13 │ 1 day, 18:27:00 │  351     0   505  41.0 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                       EXIT REASON STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃               Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ sell_ichimoku_futur_cloud │   205 │         4.94 │        4828.459 │       482.85 │  1 day, 4:21:00 │  205     0     0   100 │
│            take_profit_3R │    16 │        20.55 │        1329.869 │       132.99 │ 3 days, 9:43:00 │   16     0     0   100 │
│                force_exit │     1 │         0.07 │           0.585 │         0.06 │  1 day, 1:00:00 │    1     0     0   100 │
│                 stop_loss │    38 │        -5.64 │       -1163.542 │      -116.35 │        21:31:00 │    0     0    38     0 │
│               exit_signal │   596 │        -1.38 │       -4354.048 │       -435.4 │ 1 day, 23:36:00 │  129     0   467  21.6 │
│                     TOTAL │   856 │         0.35 │         641.324 │        64.13 │ 1 day, 18:27:00 │  351     0   505  41.0 │
└───────────────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                                     MIXED TAG STATS                                                                      
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃               Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ sell_ichimoku_futur_cloud │    173 │         4.77 │        3910.024 │        391.0 │   1 day, 2:55:00 │  173     0     0   100 │
│ strong_bullish_rebond │            take_profit_3R │     11 │        19.33 │         906.112 │        90.61 │  3 days, 3:40:00 │   11     0     0   100 │
│      engulfing_rebond │ sell_ichimoku_futur_cloud │     22 │         5.61 │         577.613 │        57.76 │  1 day, 15:14:00 │   22     0     0   100 │
│         hammer_rebond │ sell_ichimoku_futur_cloud │     10 │         6.42 │         340.822 │        34.08 │   1 day, 5:21:00 │   10     0     0   100 │
│         hammer_rebond │            take_profit_3R │      4 │        20.91 │         329.271 │        32.93 │ 4 days, 12:12:00 │    4     0     0   100 │
│      engulfing_rebond │            take_profit_3R │      1 │        32.49 │          94.487 │         9.45 │  1 day, 18:20:00 │    1     0     0   100 │
│ strong_bullish_rebond │                force_exit │      1 │         0.07 │           0.585 │         0.06 │   1 day, 1:00:00 │    1     0     0   100 │
│      engulfing_rebond │                 stop_loss │      3 │        -8.23 │         -97.371 │        -9.74 │         18:15:00 │    0     0     3     0 │
│         hammer_rebond │                 stop_loss │      5 │        -4.89 │        -147.501 │       -14.75 │         18:10:00 │    0     0     5     0 │
│         hammer_rebond │               exit_signal │     67 │        -0.65 │        -287.710 │       -28.77 │  2 days, 5:40:00 │   21     0    46  31.3 │
│      engulfing_rebond │               exit_signal │     60 │        -1.39 │        -456.953 │        -45.7 │  1 day, 22:40:00 │   10     0    50  16.7 │
│ strong_bullish_rebond │                 stop_loss │     30 │         -5.5 │        -918.669 │       -91.87 │         22:24:00 │    0     0    30     0 │
│ strong_bullish_rebond │               exit_signal │    469 │        -1.48 │       -3609.384 │      -360.94 │  1 day, 22:52:00 │   98     0   371  20.9 │
│                 TOTAL │                           │    856 │         0.35 │         641.324 │        64.13 │  1 day, 18:27:00 │  351     0   505  41.0 │
└───────────────────────┴───────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2020-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 856 / 0.41                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1641.324 USDT                  │
│ Absolute profit               │ 641.324 USDT                   │
│ Total profit %                │ 64.13%                         │
│ CAGR %                        │ 9.09%                          │
│ Sortino                       │ 0.64                           │
│ Sharpe                        │ 0.25                           │
│ Calmar                        │ 1.58                           │
│ SQN                           │ 0.91                           │
│ Profit factor                 │ 1.09                           │
│ Expectancy (Ratio)            │ 0.75 (0.05)                    │
│ Avg. daily profit             │ 0.308 USDT                     │
│ Avg. stake amount             │ 546.15 USDT                    │
│ Total trade volume            │ 937523.471 USDT                │
│                               │                                │
│ Best Pair                     │ BTC/USDT 32.15%                │
│ Worst Pair                    │ LTC/USDT -24.26%               │
│ Best trade                    │ BNB/USDT 38.12%                │
│ Worst trade                   │ LTC/USDT -11.67%               │
│ Best day                      │ 132.114 USDT                   │
│ Worst day                     │ -88.941 USDT                   │
│ Days win/draw/lose            │ 229 / 1476 / 335               │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 7d 08:55 / 2d 05:20 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:15 / 3d 23:00 / 1d 10:53 │
│ Max Consecutive Wins / Loss   │ 10 / 13                        │
│ Rejected Entry signals        │ 1696                           │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 893.837 USDT                   │
│ Max balance                   │ 2344.321 USDT                  │
│ Max % of account underwater   │ 37.32%                         │
│ Absolute drawdown             │ 874.983 USDT (37.32%)          │
│ Drawdown duration             │ 1270 days 06:00:00             │
│ Profit at drawdown start      │ 1344.321 USDT                  │
│ Profit at drawdown end        │ 469.338 USDT                   │
│ Drawdown start                │ 2021-11-10 21:00:00            │
│ Drawdown end                  │ 2025-05-04 03:00:00            │
│ Market change                 │ 2537.81%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2020-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    856 │         0.35 │         641.324 │        64.13 │ 1 day, 18:27:00 │  351     0   505  41.0 │ 874.983 USDT  37.32% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-24T11:21:03.862133",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 8934,
  "total_daily_avg_trades": "856 / 0.41",
  "absolute_profit_usdt": 641.324,
  "total_profit_pct": 64.13,
  "cagr_pct": 9.09,
  "sortino": 0.64,
  "sharpe": 0.25,
  "calmar": 1.58,
  "sqn": 0.91,
  "max_consecutive_wins_loss": "10 / 13",
  "min_balance_usdt": 893.837,
  "max_balance_usdt": 2344.321,
  "absolute_drawdown_pct": 37.32,
  "market_change_pct": 2537.81
}
```
