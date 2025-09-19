# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 8472  
**Timestamp:** 2025-09-19 16:17:36

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 8472,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231
```

## Backtesting Output
```
2025-09-19 14:17:00,796 - freqtrade - INFO - freqtrade 2025.8
2025-09-19 14:17:01,362 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-19 14:17:03,955 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-19 14:17:03,961 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-19 14:17:03,962 - freqtrade.loggers - INFO - Logfile configured
2025-09-19 14:17:03,962 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-19 14:17:03,963 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-19 14:17:03,964 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-19 14:17:03,964 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-19 14:17:03,965 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-19 14:17:04,358 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-19 14:17:04,360 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-19 14:17:04,361 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-19 14:17:04,361 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-19 14:17:04,362 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-19 14:17:04,362 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-19 14:17:04,364 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-19 14:17:04,378 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-19 14:17:04,379 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 14:17:04,381 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-19 14:17:04,383 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-19 14:17:04,383 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-19 14:17:04,408 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-19 14:17:08,282 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-19 14:17:08,384 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-19 14:17:08,387 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-19 14:17:08,392 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-19 14:17:08,392 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-19 14:17:08,392 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-19 14:17:08,393 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-19 14:17:08,393 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-19 14:17:08,394 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-19 14:17:08,395 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-19 14:17:08,395 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-19 14:17:08,396 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-19 14:17:08,396 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-19 14:17:08,396 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-19 14:17:08,397 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-19 14:17:08,397 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-19 14:17:08,398 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-19 14:17:08,398 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-19 14:17:08,399 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-19 14:17:08,399 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-19 14:17:08,400 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-19 14:17:08,400 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-19 14:17:08,400 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-19 14:17:08,401 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-19 14:17:08,401 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-19 14:17:08,401 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-19 14:17:08,402 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-19 14:17:08,402 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-19 14:17:08,402 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-19 14:17:08,402 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-19 14:17:08,403 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-19 14:17:08,403 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 14:17:08,432 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-19 14:17:08,456 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-19 14:17:08,510 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 14:17:08,570 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 14:17:08,623 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 14:17:08,677 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 14:17:08,732 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 14:17:08,763 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-19 14:17:09,118 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 14:17:09,595 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 14:17:09,976 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 14:17:10,340 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 14:17:10,696 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 14:17:11,972 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-19 14:17:11,979 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-19 14:17:11,980 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-19 14:17:11,980 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-19 14:17:11,981 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-19 14:17:11,982 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 1
2025-09-19 14:17:11,982 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.5
2025-09-19 14:17:11,983 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-09-19 14:17:11,983 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.025
2025-09-19 14:17:11,984 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.05
2025-09-19 14:17:11,984 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.05
2025-09-19 14:17:11,985 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-19 14:17:11,986 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 2
2025-09-19 14:17:11,986 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-09-19 14:17:11,987 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-19 14:17:11,987 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-19 14:17:11,988 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-19 14:17:11,988 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-19 14:17:11,991 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 14:17:12,010 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 14:17:15,216 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 14:17:15,230 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 14:17:17,775 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 14:17:17,792 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 14:17:20,660 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 14:17:20,679 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 14:17:23,750 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 14:17:23,767 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 14:17:26,453 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-19 14:17:34,663 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-19_14-17-34.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
│ ETH/USDT │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
│ LTC/USDT │     54 │        -0.14 │         -54.434 │        -5.44 │      4:18:00 │   15     0    39  27.8 │
│ BNB/USDT │     50 │        -0.17 │         -81.110 │        -8.11 │      3:16:00 │   18     0    32  36.0 │
│ XRP/USDT │     32 │        -0.55 │        -149.657 │       -14.97 │      3:04:00 │    4     0    28  12.5 │
│    TOTAL │    136 │        -0.25 │        -285.202 │       -28.52 │      3:38:00 │   37     0    99  27.2 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
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
│     OTHER │     136 │        -0.25 │        -285.202 │       -28.52 │      3:38:00 │   37     0    99  27.2 │
│     TOTAL │     136 │        -0.25 │        -285.202 │       -28.52 │      3:38:00 │   37     0    99  27.2 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │    35 │         1.19 │         377.632 │        37.76 │      4:29:00 │   35     0     0   100 │
│    exit_signal │    17 │        -0.79 │        -106.138 │       -10.61 │     10:14:00 │    2     0    15  11.8 │
│      stop_loss │    84 │        -0.74 │        -556.695 │       -55.67 │      1:57:00 │    0     0    84     0 │
│          TOTAL │   136 │        -0.25 │        -285.202 │       -28.52 │      3:38:00 │   37     0    99  27.2 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │     35 │         1.19 │         377.632 │        37.76 │      4:29:00 │   35     0     0   100 │
│           │    exit_signal │     17 │        -0.79 │        -106.138 │       -10.61 │     10:14:00 │    2     0    15  11.8 │
│           │      stop_loss │     84 │        -0.74 │        -556.695 │       -55.67 │      1:57:00 │    0     0    84     0 │
│     TOTAL │                │    136 │        -0.25 │        -285.202 │       -28.52 │      3:38:00 │   37     0    99  27.2 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 136 / 0.1                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 714.798 USDT                   │
│ Absolute profit               │ -285.202 USDT                  │
│ Total profit %                │ -28.52%                        │
│ CAGR %                        │ -8.69%                         │
│ Sortino                       │ -1.11                          │
│ Sharpe                        │ -0.40                          │
│ Calmar                        │ -1.16                          │
│ SQN                           │ -2.39                          │
│ Profit factor                 │ 0.57                           │
│ Expectancy (Ratio)            │ -2.10 (-0.31)                  │
│ Avg. daily profit             │ -0.212 USDT                    │
│ Avg. stake amount             │ 867.024 USDT                   │
│ Total trade volume            │ 236016.783 USDT                │
│                               │                                │
│ Best Pair                     │ BTC/USDT 0.00%                 │
│ Worst Pair                    │ XRP/USDT -14.97%               │
│ Best trade                    │ LTC/USDT 6.46%                 │
│ Worst trade                   │ LTC/USDT -2.01%                │
│ Best day                      │ 62.043 USDT                    │
│ Worst day                     │ -17.303 USDT                   │
│ Days win/draw/lose            │ 30 / 1204 / 90                 │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 1d 09:45 / 0d 05:30 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 0d 22:00 / 0d 02:56 │
│ Max Consecutive Wins / Loss   │ 4 / 12                         │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 702.12 USDT                    │
│ Max balance                   │ 1076.018 USDT                  │
│ Max % of account underwater   │ 34.75%                         │
│ Absolute drawdown             │ 373.898 USDT (34.75%)          │
│ Drawdown duration             │ 1160 days 06:05:00             │
│ Profit at drawdown start      │ 76.018 USDT                    │
│ Profit at drawdown end        │ -297.88 USDT                   │
│ Drawdown start                │ 2022-03-19 07:30:00            │
│ Drawdown end                  │ 2025-05-22 13:35:00            │
│ Market change                 │ 91.49%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    136 │        -0.25 │        -285.202 │       -28.52 │      3:38:00 │   37     0    99  27.2 │ 373.898 USDT  34.75% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-19T16:17:35.979799",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 8472,
  "total_daily_avg_trades": "136 / 0.1",
  "absolute_profit_usdt": -285.202,
  "total_profit_pct": -28.52,
  "cagr_pct": -8.69,
  "sortino": -1.11,
  "sharpe": -0.4,
  "calmar": -1.16,
  "sqn": -2.39,
  "max_consecutive_wins_loss": "4 / 12",
  "min_balance_usdt": 702.12,
  "max_balance_usdt": 1076.018,
  "market_change_pct": 91.49,
  "win_draw_loss_winpct": "37 0 99 27.2"
}
```
