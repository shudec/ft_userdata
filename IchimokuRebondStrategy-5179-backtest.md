# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 5179  
**Timestamp:** 2025-09-25 21:58:17

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 5179,
  "epochs": 100,
  "hyperopt_timerange": "20220101-20231231",
  "backtest_timerange": "20240101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20240101-20251231
```

## Backtesting Output
```
2025-09-25 19:56:51,734 - freqtrade - INFO - freqtrade 2025.7
2025-09-25 19:56:52,174 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-25 19:56:52,175 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-25 19:56:54,312 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-25 19:56:54,316 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-25 19:56:54,317 - freqtrade.loggers - INFO - Logfile configured
2025-09-25 19:56:54,317 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-25 19:56:54,318 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-25 19:56:54,318 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-25 19:56:54,318 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-25 19:56:54,319 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20240101-20251231 ...
2025-09-25 19:56:54,340 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-25 19:56:54,341 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-25 19:56:54,341 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-25 19:56:54,342 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-25 19:56:54,342 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-25 19:56:54,343 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20240101-20251231
2025-09-25 19:56:54,345 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-25 19:56:54,366 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-25 19:56:54,367 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 19:56:54,371 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-25 19:56:54,372 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-25 19:56:54,372 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-25 19:56:54,407 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-25 19:56:56,830 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-25 19:56:56,876 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-25 19:56:56,877 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-25 19:56:56,878 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-25 19:56:56,878 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-25 19:56:56,879 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-25 19:56:56,879 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-25 19:56:56,880 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-25 19:56:56,880 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-25 19:56:56,881 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-25 19:56:56,881 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-25 19:56:56,882 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-25 19:56:56,882 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-25 19:56:56,883 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-25 19:56:56,884 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-25 19:56:56,884 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-25 19:56:56,884 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-25 19:56:56,885 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-25 19:56:56,885 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-25 19:56:56,886 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-25 19:56:56,886 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-25 19:56:56,886 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-25 19:56:56,887 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-25 19:56:56,887 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-25 19:56:56,887 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-25 19:56:56,888 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-25 19:56:56,888 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-25 19:56:56,888 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-25 19:56:56,889 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-25 19:56:56,889 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-25 19:56:56,889 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-25 19:56:56,890 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 19:56:56,895 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-25 19:56:56,927 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-25 19:56:56,961 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-25 19:56:57,007 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-25 19:56:57,048 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-25 19:56:57,088 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-25 19:56:57,129 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-25 19:56:57,149 - freqtrade.optimize.backtesting - INFO - Loading data from 2024-01-01 00:00:00 up to 2025-09-11 17:00:00 (619 days).
2025-09-25 19:56:57,234 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-25 19:56:57,400 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-25 19:56:57,564 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-25 19:56:57,704 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-25 19:56:57,859 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-25 19:56:58,551 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-25 19:56:58,552 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-25 19:56:58,552 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-25 19:56:58,553 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.25
2025-09-25 19:56:58,553 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-25 19:56:58,553 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = True
2025-09-25 19:56:58,554 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-25 19:56:58,554 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 10
2025-09-25 19:56:58,554 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 1
2025-09-25 19:56:58,555 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.568
2025-09-25 19:56:58,555 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.565
2025-09-25 19:56:58,556 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.023
2025-09-25 19:56:58,556 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.003
2025-09-25 19:56:58,556 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-25 19:56:58,557 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-25 19:56:58,557 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.5
2025-09-25 19:56:58,557 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.0
2025-09-25 19:56:58,558 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 2.5
2025-09-25 19:56:58,558 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1
2025-09-25 19:56:58,558 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-09-25 19:56:58,559 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-25 19:56:58,559 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 4
2025-09-25 19:56:58,559 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-25 19:56:58,560 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-25 19:56:58,560 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-09-25 19:56:58,560 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-25 19:56:58,560 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = atr
2025-09-25 19:56:58,561 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-09-25 19:56:58,561 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-25 19:56:58,561 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-25 19:56:58,562 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-25 19:56:58,563 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-25 19:56:58,564 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 19:56:58,574 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-25 19:56:58,596 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 19:56:58,615 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-25 19:57:01,689 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 19:57:01,699 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-25 19:57:01,722 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 19:57:01,741 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-25 19:57:04,714 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 19:57:04,724 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-25 19:57:04,745 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 19:57:04,764 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-25 19:57:07,688 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 19:57:07,698 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-25 19:57:07,718 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 19:57:07,740 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-25 19:57:10,637 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 19:57:10,649 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-25 19:57:10,671 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 19:57:10,692 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-25 19:57:13,693 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2024-01-01 00:00:00 up to 2025-09-11 17:00:00 (619 days).
2025-09-25 19:58:16,735 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-25_19-58-16.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │     13 │         2.62 │         117.047 │         11.7 │ 19 days, 6:13:00 │    5     0     8  38.5 │
│ BNB/USDT │     12 │         2.58 │         103.577 │        10.36 │ 8 days, 12:40:00 │    5     0     7  41.7 │
│ ETH/USDT │     11 │         4.14 │          77.083 │         7.71 │  4 days, 6:48:00 │    5     0     6  45.5 │
│ XRP/USDT │      5 │        -1.01 │         -27.973 │         -2.8 │ 7 days, 14:32:00 │    1     0     4  20.0 │
│ LTC/USDT │      8 │        -2.51 │         -88.323 │        -8.83 │   1 day, 6:16:00 │    1     0     7  12.5 │
│    TOTAL │     49 │         1.74 │         181.410 │        18.14 │  9 days, 3:24:00 │   17     0    32  34.7 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         5.39 │          16.258 │         1.63 │ 25 days, 16:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         5.39 │          16.258 │         1.63 │ 25 days, 16:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                        ENTER TAG STATS                                                         
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│      engulfing_rebond │       8 │         5.05 │         135.045 │         13.5 │ 11 days, 15:49:00 │    4     0     4  50.0 │
│ strong_bullish_rebond │      41 │          1.1 │          46.365 │         4.64 │  8 days, 15:37:00 │   13     0    28  31.7 │
│                 TOTAL │      49 │         1.74 │         181.410 │        18.14 │   9 days, 3:24:00 │   17     0    32  34.7 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                   EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │    16 │        15.37 │         852.178 │        85.22 │ 13 days, 12:32:00 │   16     0     0   100 │
│     force_exit │     1 │         5.39 │          16.258 │         1.63 │ 25 days, 16:00:00 │    1     0     0   100 │
│      stop_loss │    32 │        -5.19 │        -687.027 │        -68.7 │  6 days, 10:26:00 │    0     0    32     0 │
│          TOTAL │    49 │         1.74 │         181.410 │        18.14 │   9 days, 3:24:00 │   17     0    32  34.7 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                                MIXED TAG STATS                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_3R │     12 │         15.4 │         625.361 │        62.54 │ 10 days, 15:42:00 │   12     0     0   100 │
│      engulfing_rebond │ take_profit_3R │      4 │        15.28 │         226.818 │        22.68 │  22 days, 3:04:00 │    4     0     0   100 │
│ strong_bullish_rebond │     force_exit │      1 │         5.39 │          16.258 │         1.63 │ 25 days, 16:00:00 │    1     0     0   100 │
│      engulfing_rebond │      stop_loss │      4 │        -5.19 │         -91.773 │        -9.18 │    1 day, 4:34:00 │    0     0     4     0 │
│ strong_bullish_rebond │      stop_loss │     28 │        -5.19 │        -595.253 │       -59.53 │   7 days, 4:25:00 │    0     0    28     0 │
│                 TOTAL │                │     49 │         1.74 │         181.410 │        18.14 │   9 days, 3:24:00 │   17     0    32  34.7 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                          SUMMARY METRICS                           
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                            ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2024-01-01 00:00:00              │
│ Backtesting to                │ 2025-09-11 17:00:00              │
│ Trading Mode                  │ Spot                             │
│ Max open trades               │ 3                                │
│                               │                                  │
│ Total/Daily Avg Trades        │ 49 / 0.08                        │
│ Starting balance              │ 1000 USDT                        │
│ Final balance                 │ 1181.41 USDT                     │
│ Absolute profit               │ 181.41 USDT                      │
│ Total profit %                │ 18.14%                           │
│ CAGR %                        │ 10.33%                           │
│ Sortino                       │ 1.70                             │
│ Sharpe                        │ 0.16                             │
│ Calmar                        │ 2.09                             │
│ SQN                           │ 0.72                             │
│ Profit factor                 │ 1.26                             │
│ Expectancy (Ratio)            │ 3.70 (0.17)                      │
│ Avg. daily profit             │ 0.293 USDT                       │
│ Avg. stake amount             │ 389.397 USDT                     │
│ Total trade volume            │ 38419.104 USDT                   │
│                               │                                  │
│ Best Pair                     │ BTC/USDT 11.70%                  │
│ Worst Pair                    │ LTC/USDT -8.83%                  │
│ Best trade                    │ LTC/USDT 16.24%                  │
│ Worst trade                   │ BTC/USDT -5.19%                  │
│ Best day                      │ 106.825 USDT                     │
│ Worst day                     │ -46.642 USDT                     │
│ Days win/draw/lose            │ 15 / 535 / 28                    │
│ Min/Max/Avg. Duration Winners │ 0d 17:20 / 69d 01:35 / 14d 05:41 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:30 / 45d 15:45 / 6d 10:26  │
│ Max Consecutive Wins / Loss   │ 4 / 9                            │
│ Rejected Entry signals        │ 12                               │
│ Entry/Exit Timeouts           │ 0 / 0                            │
│                               │                                  │
│ Min balance                   │ 916.545 USDT                     │
│ Max balance                   │ 1252.952 USDT                    │
│ Max % of account underwater   │ 26.85%                           │
│ Absolute Drawdown (Account)   │ 26.85%                           │
│ Absolute Drawdown             │ 336.407 USDT                     │
│ Drawdown high                 │ 252.952 USDT                     │
│ Drawdown low                  │ -83.455 USDT                     │
│ Drawdown Start                │ 2024-02-28 13:25:00              │
│ Drawdown End                  │ 2024-10-15 15:05:00              │
│ Market change                 │ 178.91%                          │
└───────────────────────────────┴──────────────────────────────────┘

Backtested 2024-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     49 │         1.74 │         181.410 │        18.14 │ 9 days, 3:24:00 │   17     0    32  34.7 │ 336.407 USDT  26.85% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-25T21:58:17.848849",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 5179,
  "total_daily_avg_trades": "49 / 0.08",
  "absolute_profit_usdt": 181.41,
  "total_profit_pct": 18.14,
  "cagr_pct": 10.33,
  "sortino": 1.7,
  "sharpe": 0.16,
  "calmar": 2.09,
  "sqn": 0.72,
  "max_consecutive_wins_loss": "4 / 9",
  "min_balance_usdt": 916.545,
  "max_balance_usdt": 1252.952,
  "market_change_pct": 178.91
}
```
