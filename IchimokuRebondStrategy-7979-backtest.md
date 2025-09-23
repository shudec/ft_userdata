# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 7979  
**Timestamp:** 2025-09-23 22:10:26

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 7979,
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
2025-09-23 20:09:10,340 - freqtrade - INFO - freqtrade 2025.7
2025-09-23 20:09:10,763 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-23 20:09:10,763 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-23 20:09:12,629 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-23 20:09:12,631 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-23 20:09:12,632 - freqtrade.loggers - INFO - Logfile configured
2025-09-23 20:09:12,632 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-23 20:09:12,633 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-23 20:09:12,633 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-23 20:09:12,633 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-23 20:09:12,634 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20240101-20251231 ...
2025-09-23 20:09:12,642 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-23 20:09:12,643 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-23 20:09:12,643 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-23 20:09:12,644 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-23 20:09:12,644 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-23 20:09:12,645 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20240101-20251231
2025-09-23 20:09:12,646 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-23 20:09:12,665 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-23 20:09:12,666 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 20:09:12,670 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-23 20:09:12,671 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-23 20:09:12,672 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-23 20:09:12,706 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-23 20:09:15,173 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-23 20:09:15,220 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-23 20:09:15,220 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-23 20:09:15,222 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-23 20:09:15,222 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-23 20:09:15,223 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-23 20:09:15,223 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-23 20:09:15,224 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-23 20:09:15,225 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-23 20:09:15,225 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-23 20:09:15,226 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-23 20:09:15,226 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-23 20:09:15,226 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-23 20:09:15,227 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-23 20:09:15,227 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-23 20:09:15,228 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-23 20:09:15,228 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-23 20:09:15,229 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-23 20:09:15,229 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-23 20:09:15,230 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-23 20:09:15,230 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-23 20:09:15,231 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-23 20:09:15,231 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-23 20:09:15,232 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-23 20:09:15,232 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-23 20:09:15,232 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-23 20:09:15,233 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-23 20:09:15,234 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-23 20:09:15,235 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-23 20:09:15,235 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-23 20:09:15,236 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-23 20:09:15,237 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 20:09:15,244 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-23 20:09:15,288 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-23 20:09:15,322 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 20:09:15,367 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 20:09:15,403 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 20:09:15,442 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 20:09:15,479 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 20:09:15,497 - freqtrade.optimize.backtesting - INFO - Loading data from 2024-01-01 00:00:00 up to 2025-09-11 17:00:00 (619 days).
2025-09-23 20:09:15,567 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 20:09:15,708 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 20:09:15,864 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 20:09:16,040 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 20:09:16,183 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 20:09:16,881 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-23 20:09:16,882 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-23 20:09:16,882 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-23 20:09:16,883 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-23 20:09:16,883 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-23 20:09:16,883 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-23 20:09:16,884 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-23 20:09:16,884 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-23 20:09:16,884 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-23 20:09:16,885 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-23 20:09:16,885 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-23 20:09:16,885 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-23 20:09:16,885 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-09-23 20:09:16,886 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-09-23 20:09:16,886 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-23 20:09:16,886 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-23 20:09:16,887 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-23 20:09:16,887 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-23 20:09:16,888 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-23 20:09:16,888 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 1
2025-09-23 20:09:16,888 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-23 20:09:16,889 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-23 20:09:16,889 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-23 20:09:16,889 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower
2025-09-23 20:09:16,890 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-23 20:09:16,890 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-23 20:09:16,891 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:09:16,900 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 20:09:16,917 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:09:16,934 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 20:09:20,051 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:09:20,058 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 20:09:20,074 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:09:20,092 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 20:09:23,003 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:09:23,010 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 20:09:23,025 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:09:23,042 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 20:09:25,976 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:09:25,984 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 20:09:26,000 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:09:26,018 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 20:09:28,976 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:09:28,984 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 20:09:29,001 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:09:29,019 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 20:09:31,963 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2024-01-01 00:00:00 up to 2025-09-11 17:00:00 (619 days).
2025-09-23 20:10:25,553 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-23_20-10-25.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │     75 │         0.43 │          57.270 │         5.73 │ 1 day, 12:01:00 │   25     0    50  33.3 │
│ XRP/USDT │     47 │         0.45 │          46.979 │          4.7 │  1 day, 0:19:00 │   13     0    34  27.7 │
│ LTC/USDT │     39 │         0.17 │          10.212 │         1.02 │  1 day, 6:45:00 │   11     0    28  28.2 │
│ ETH/USDT │     51 │        -0.03 │          -6.323 │        -0.63 │  1 day, 7:29:00 │   17     0    34  33.3 │
│ BNB/USDT │     72 │        -0.35 │         -55.399 │        -5.54 │  1 day, 6:54:00 │   15     0    57  20.8 │
│    TOTAL │    284 │         0.12 │          52.739 │         5.27 │  1 day, 7:15:00 │   81     0   203  28.5 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                            LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         1.31 │           2.748 │         0.27 │ 1 day, 14:00:00 │    1     0     0   100 │
│ BTC/USDT │      1 │        -0.12 │          -0.257 │        -0.03 │        13:00:00 │    0     0     1     0 │
│ LTC/USDT │      1 │        -3.08 │          -6.458 │        -0.65 │        17:00:00 │    0     0     1     0 │
│    TOTAL │      3 │        -0.63 │          -3.967 │         -0.4 │        22:40:00 │    1     0     2  33.3 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                       ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │     230 │         0.15 │          61.587 │         6.16 │  1 day, 7:38:00 │   63     0   167  27.4 │
│      engulfing_rebond │      34 │         0.85 │          56.725 │         5.67 │ 1 day, 11:35:00 │   16     0    18  47.1 │
│         hammer_rebond │      20 │        -1.56 │         -65.573 │        -6.56 │        19:27:00 │    2     0    18  10.0 │
│                 TOTAL │     284 │         0.12 │          52.739 │         5.27 │  1 day, 7:15:00 │   81     0   203  28.5 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │    26 │        10.34 │         552.052 │        55.21 │ 1 day, 20:02:00 │   26     0     0   100 │
│     force_exit │     3 │        -0.63 │          -3.967 │         -0.4 │        22:40:00 │    1     0     2  33.3 │
│      stop_loss │     1 │       -10.18 │         -23.420 │        -2.34 │        19:25:00 │    0     0     1     0 │
│    exit_signal │   254 │        -0.88 │        -471.926 │       -47.19 │  1 day, 6:05:00 │   54     0   200  21.3 │
│          TOTAL │   284 │         0.12 │          52.739 │         5.27 │  1 day, 7:15:00 │   81     0   203  28.5 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                               MIXED TAG STATS                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_1R │     22 │        10.32 │         464.328 │        46.43 │ 1 day, 21:32:00 │   22     0     0   100 │
│      engulfing_rebond │ take_profit_1R │      4 │        10.42 │          87.724 │         8.77 │ 1 day, 11:51:00 │    4     0     0   100 │
│      engulfing_rebond │     force_exit │      1 │        -0.12 │          -0.257 │        -0.03 │        13:00:00 │    0     0     1     0 │
│ strong_bullish_rebond │     force_exit │      2 │        -0.89 │          -3.710 │        -0.37 │  1 day, 3:30:00 │    1     0     1  50.0 │
│      engulfing_rebond │    exit_signal │     28 │        -0.09 │          -7.322 │        -0.73 │ 1 day, 12:56:00 │   12     0    16  42.9 │
│      engulfing_rebond │      stop_loss │      1 │       -10.18 │         -23.420 │        -2.34 │        19:25:00 │    0     0     1     0 │
│         hammer_rebond │    exit_signal │     20 │        -1.56 │         -65.573 │        -6.56 │        19:27:00 │    2     0    18  10.0 │
│ strong_bullish_rebond │    exit_signal │    206 │        -0.92 │        -399.031 │        -39.9 │  1 day, 6:11:00 │   40     0   166  19.4 │
│                 TOTAL │                │    284 │         0.12 │          52.739 │         5.27 │  1 day, 7:15:00 │   81     0   203  28.5 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2024-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-11 17:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 284 / 0.46                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1052.739 USDT                  │
│ Absolute profit               │ 52.739 USDT                    │
│ Total profit %                │ 5.27%                          │
│ CAGR %                        │ 3.08%                          │
│ Sortino                       │ 0.51                           │
│ Sharpe                        │ 0.20                           │
│ Calmar                        │ 1.01                           │
│ SQN                           │ 0.39                           │
│ Profit factor                 │ 1.07                           │
│ Expectancy (Ratio)            │ 0.19 (0.05)                    │
│ Avg. daily profit             │ 0.085 USDT                     │
│ Avg. stake amount             │ 205.193 USDT                   │
│ Total trade volume            │ 116835.952 USDT                │
│                               │                                │
│ Best Pair                     │ BTC/USDT 5.73%                 │
│ Worst Pair                    │ BNB/USDT -5.54%                │
│ Best trade                    │ XRP/USDT 11.33%                │
│ Worst trade                   │ BTC/USDT -10.18%               │
│ Best day                      │ 46.345 USDT                    │
│ Worst day                     │ -23.42 USDT                    │
│ Days win/draw/lose            │ 58 / 393 / 129                 │
│ Min/Max/Avg. Duration Winners │ 0d 04:50 / 5d 04:00 / 2d 07:35 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 2d 13:00 / 0d 21:32 │
│ Max Consecutive Wins / Loss   │ 6 / 13                         │
│ Rejected Entry signals        │ 552                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 952.677 USDT                   │
│ Max balance                   │ 1167.068 USDT                  │
│ Max % of account underwater   │ 16.16%                         │
│ Absolute Drawdown (Account)   │ 16.16%                         │
│ Absolute Drawdown             │ 188.614 USDT                   │
│ Drawdown high                 │ 167.068 USDT                   │
│ Drawdown low                  │ -21.546 USDT                   │
│ Drawdown Start                │ 2024-12-01 19:50:00            │
│ Drawdown End                  │ 2025-07-08 15:00:00            │
│ Market change                 │ 178.91%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2024-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                  
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    284 │         0.12 │          52.739 │         5.27 │ 1 day, 7:15:00 │   81     0   203  28.5 │ 188.614 USDT  16.16% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-23T22:10:26.635069",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 7979,
  "total_daily_avg_trades": "284 / 0.46",
  "absolute_profit_usdt": 52.739,
  "total_profit_pct": 5.27,
  "cagr_pct": 3.08,
  "sortino": 0.51,
  "sharpe": 0.2,
  "calmar": 1.01,
  "sqn": 0.39,
  "max_consecutive_wins_loss": "6 / 13",
  "min_balance_usdt": 952.677,
  "max_balance_usdt": 1167.068,
  "market_change_pct": 178.91,
  "win_draw_loss_winpct": "1 0 2 33.3"
}
```
