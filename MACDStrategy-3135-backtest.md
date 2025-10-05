# Freqtrade Backtest Log

**Strategy:** MACDStrategy  
**Random State:** 3135  
**Timestamp:** 2025-10-04 22:26:08

## Configuration
```json
{
  "strategy": "MACDStrategy",
  "timeframe": "1h",
  "pairs": [
    "ADA/USDT",
    "SOL/USDT",
    "DOGE/USDT",
    "TRX/USDT"
  ],
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 3135,
  "epochs": 100,
  "hyperopt_timerange": "20220101-20231231",
  "backtest_timerange": "20220101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy MACDStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs ADA/USDT SOL/USDT DOGE/USDT TRX/USDT --timerange 20220101-20251231 --export trades
```

## Backtesting Output
```
2025-10-04 20:25:46,633 - freqtrade - INFO - freqtrade 2025.7
2025-10-04 20:25:47,011 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-10-04 20:25:47,011 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-04 20:25:48,888 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-04 20:25:48,892 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-04 20:25:48,892 - freqtrade.loggers - INFO - Logfile configured
2025-10-04 20:25:48,893 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-04 20:25:48,893 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-10-04 20:25:48,894 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-04 20:25:48,894 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-04 20:25:48,894 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-10-04 20:25:48,904 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-04 20:25:48,905 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-04 20:25:48,905 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-04 20:25:48,906 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-04 20:25:48,906 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-04 20:25:48,907 - freqtrade.configuration.configuration - INFO - Using pairs ['ADA/USDT', 'SOL/USDT', 'DOGE/USDT', 'TRX/USDT']
2025-10-04 20:25:48,907 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-10-04 20:25:48,909 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-04 20:25:48,929 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-04 20:25:48,930 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-04 20:25:48,934 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-04 20:25:48,935 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-04 20:25:48,936 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-10-04 20:25:48,972 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-04 20:25:51,525 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-04 20:25:51,593 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy MACDStrategy from '/freqtrade/user_data/strategies/MACD_strategy.py'...
2025-10-04 20:25:51,593 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/MACD_strategy.json
2025-10-04 20:25:51,595 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-10-04 20:25:51,595 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-04 20:25:51,595 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-04 20:25:51,596 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-04 20:25:51,596 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-04 20:25:51,597 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-04 20:25:51,597 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-10-04 20:25:51,598 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-10-04 20:25:51,598 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-04 20:25:51,598 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-04 20:25:51,599 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-04 20:25:51,599 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-04 20:25:51,600 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-04 20:25:51,600 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'market', 'stoploss_on_exchange': False}
2025-10-04 20:25:51,601 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-04 20:25:51,601 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-04 20:25:51,601 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-04 20:25:51,602 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 200
2025-10-04 20:25:51,602 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-04 20:25:51,603 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-10-04 20:25:51,603 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-04 20:25:51,604 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-04 20:25:51,604 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-04 20:25:51,605 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-04 20:25:51,605 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-04 20:25:51,605 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-04 20:25:51,606 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-04 20:25:51,606 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-04 20:25:51,607 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-04 20:25:51,612 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-04 20:25:51,642 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-04 20:25:51,644 - freqtrade.data.history.history_utils - INFO - Using indicator startup period: 200 ...
2025-10-04 20:25:51,679 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-04 20:25:51,732 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-04 20:25:51,782 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-04 20:25:51,827 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-04 20:25:51,856 - freqtrade.optimize.backtesting - INFO - Loading data from 2021-12-23 16:00:00 up to 2025-10-02 17:00:00 (1379 days).
2025-10-04 20:25:51,934 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-04 20:25:52,188 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-04 20:25:52,440 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-04 20:25:52,705 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-04 20:25:53,967 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-04 20:25:53,968 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-04 20:25:53,969 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy MACDStrategy
2025-10-04 20:25:53,970 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 5
2025-10-04 20:25:53,970 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-10-04 20:25:53,971 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-10-04 20:25:53,971 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1
2025-10-04 20:25:53,972 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1.5
2025-10-04 20:25:53,973 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 4.5
2025-10-04 20:25:53,973 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-10-04 20:25:53,974 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-10-04 20:25:53,974 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-10-04 20:25:53,975 - freqtrade.strategy.hyper - INFO - Strategy Parameter: trailing_custom_stop = True
2025-10-04 20:25:53,975 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-10-04 20:25:53,976 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-10-04 20:25:53,976 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower and atr
2025-10-04 20:25:53,977 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-10-04 20:25:53,977 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-04 20:25:53,980 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-04 20:25:53,992 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-04 20:25:54,013 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-04 20:25:54,033 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-04 20:25:54,070 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-04 20:25:54,081 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-04 20:25:54,101 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-04 20:25:54,121 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-04 20:25:54,159 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-04 20:25:54,169 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-04 20:25:54,192 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-04 20:25:54,212 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-04 20:25:54,248 - freqtrade.data.dataprovider - INFO - Loading data for TRX/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-04 20:25:54,258 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-04 20:25:54,277 - freqtrade.data.dataprovider - INFO - Loading data for TRX/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-04 20:25:54,297 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-04 20:25:54,346 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-10-02 17:00:00 (1370 days).
2025-10-04 20:26:06,943 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-04_20-26-06.meta.json"
Result for strategy MACDStrategy
                                              BACKTESTING REPORT                                              
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ DOGE/USDT │     64 │         -0.2 │         -23.527 │        -2.35 │      4:34:00 │   35     0    29  54.7 │
│  TRX/USDT │     73 │        -0.32 │         -40.028 │         -4.0 │      5:21:00 │   34     0    39  46.6 │
│  ADA/USDT │     45 │        -0.78 │         -62.732 │        -6.27 │      5:39:00 │   19     0    26  42.2 │
│  SOL/USDT │     55 │        -0.73 │         -73.023 │         -7.3 │      5:53:00 │   28     0    27  50.9 │
│     TOTAL │    237 │        -0.47 │        -199.310 │       -19.93 │      5:19:00 │  116     0   121  48.9 │
└───────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                ENTER TAG STATS                                                
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │     237 │        -0.47 │        -199.310 │       -19.93 │      5:19:00 │  116     0   121  48.9 │
│     TOTAL │     237 │        -0.47 │        -199.310 │       -19.93 │      5:19:00 │  116     0   121  48.9 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                               EXIT REASON STATS                                               
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ exit_signal │   237 │        -0.47 │        -199.310 │       -19.93 │      5:19:00 │  116     0   121  48.9 │
│       TOTAL │   237 │        -0.47 │        -199.310 │       -19.93 │      5:19:00 │  116     0   121  48.9 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                      MIXED TAG STATS                                                       
┏━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ exit_signal │    237 │        -0.47 │        -199.310 │       -19.93 │      5:19:00 │  116     0   121  48.9 │
│     TOTAL │             │    237 │        -0.47 │        -199.310 │       -19.93 │      5:19:00 │  116     0   121  48.9 │
└───────────┴─────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2025-10-02 17:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 237 / 0.17                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 800.69 USDT                    │
│ Absolute profit               │ -199.31 USDT                   │
│ Total profit %                │ -19.93%                        │
│ CAGR %                        │ -5.75%                         │
│ Sortino                       │ -1.05                          │
│ Sharpe                        │ -0.85                          │
│ Calmar                        │ -1.37                          │
│ SQN                           │ -3.96                          │
│ Profit factor                 │ 0.49                           │
│ Expectancy (Ratio)            │ -0.84 (-0.26)                  │
│ Avg. daily profit             │ -0.145 USDT                    │
│ Avg. stake amount             │ 178.224 USDT                   │
│ Total trade volume            │ 84447.701 USDT                 │
│                               │                                │
│ Best Pair                     │ DOGE/USDT -2.35%               │
│ Worst Pair                    │ SOL/USDT -7.30%                │
│ Best trade                    │ TRX/USDT 4.45%                 │
│ Worst trade                   │ DOGE/USDT -7.63%               │
│ Best day                      │ 8.649 USDT                     │
│ Worst day                     │ -12.476 USDT                   │
│ Days win/draw/lose            │ 72 / 1168 / 99                 │
│ Min/Max/Avg. Duration Winners │ 0d 01:00 / 0d 17:00 / 0d 04:29 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 0d 23:00 / 0d 06:07 │
│ Max Consecutive Wins / Loss   │ 7 / 8                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 798.355 USDT                   │
│ Max balance                   │ 1000.783 USDT                  │
│ Max % of account underwater   │ 20.23%                         │
│ Absolute Drawdown (Account)   │ 20.23%                         │
│ Absolute Drawdown             │ 202.427 USDT                   │
│ Drawdown high                 │ 0.783 USDT                     │
│ Drawdown low                  │ -201.645 USDT                  │
│ Drawdown Start                │ 2022-02-09 08:00:00            │
│ Drawdown End                  │ 2025-09-15 19:00:00            │
│ Market change                 │ 99.71%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-10-02 17:00:00 | Max open trades : 3
                                                            STRATEGY SUMMARY                                                            
┏━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃     Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ MACDStrategy │    237 │        -0.47 │        -199.310 │       -19.93 │      5:19:00 │  116     0   121  48.9 │ 202.427 USDT  20.23% │
└──────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-04T22:26:08.120286",
  "strategy": "MACDStrategy",
  "random_state": 3135,
  "total_daily_avg_trades": "237 / 0.17",
  "absolute_profit_usdt": -199.31,
  "total_profit_pct": -19.93,
  "cagr_pct": -5.75,
  "sortino": -1.05,
  "sharpe": -0.85,
  "calmar": -1.37,
  "sqn": -3.96,
  "max_consecutive_wins_loss": "7 / 8",
  "min_balance_usdt": 798.355,
  "max_balance_usdt": 1000.783,
  "market_change_pct": 99.71,
  "win_draw_loss_winpct": "116 0 121 48.9"
}
```
