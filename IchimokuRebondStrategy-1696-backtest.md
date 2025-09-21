# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 1696  
**Timestamp:** 2025-09-19 22:19:20

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 1696,
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
2025-09-19 20:18:43,622 - freqtrade - INFO - freqtrade 2025.7
2025-09-19 20:18:44,010 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-19 20:18:44,010 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-19 20:18:45,683 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-19 20:18:45,685 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-19 20:18:45,686 - freqtrade.loggers - INFO - Logfile configured
2025-09-19 20:18:45,686 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-19 20:18:45,687 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-19 20:18:45,687 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-19 20:18:45,687 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-19 20:18:45,688 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-19 20:18:45,696 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-19 20:18:45,697 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-19 20:18:45,697 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-19 20:18:45,698 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-19 20:18:45,698 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-19 20:18:45,699 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-19 20:18:45,700 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-19 20:18:45,720 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-19 20:18:45,721 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 20:18:45,725 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-19 20:18:45,726 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-19 20:18:45,727 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-19 20:18:45,761 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-19 20:18:48,248 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-19 20:18:48,299 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-19 20:18:48,300 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-19 20:18:48,301 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-19 20:18:48,302 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-19 20:18:48,302 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-19 20:18:48,303 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-19 20:18:48,303 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-19 20:18:48,304 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-19 20:18:48,304 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-19 20:18:48,305 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-19 20:18:48,305 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-19 20:18:48,305 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-19 20:18:48,306 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-19 20:18:48,306 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-19 20:18:48,307 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-19 20:18:48,307 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-19 20:18:48,308 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-19 20:18:48,308 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-19 20:18:48,309 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-19 20:18:48,309 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-19 20:18:48,309 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-19 20:18:48,310 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-19 20:18:48,310 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-19 20:18:48,311 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-19 20:18:48,311 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-19 20:18:48,311 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-19 20:18:48,312 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-19 20:18:48,312 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-19 20:18:48,313 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-19 20:18:48,313 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-19 20:18:48,314 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 20:18:48,321 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-19 20:18:48,357 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-19 20:18:48,395 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-19 20:18:48,449 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-19 20:18:48,499 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-19 20:18:48,549 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-19 20:18:48,596 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-19 20:18:48,621 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-19 20:18:48,707 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-19 20:18:48,967 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-19 20:18:49,198 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-19 20:18:49,421 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-19 20:18:49,683 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-19 20:18:51,089 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-19 20:18:51,090 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-19 20:18:51,090 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-19 20:18:51,091 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-19 20:18:51,091 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-19 20:18:51,091 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 4
2025-09-19 20:18:51,092 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.55
2025-09-19 20:18:51,092 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.9
2025-09-19 20:18:51,092 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.03
2025-09-19 20:18:51,092 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-19 20:18:51,093 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.001
2025-09-19 20:18:51,093 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-19 20:18:51,093 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 8
2025-09-19 20:18:51,094 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.994
2025-09-19 20:18:51,094 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-19 20:18:51,094 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-19 20:18:51,095 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-19 20:18:51,095 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-19 20:18:51,097 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 20:18:51,107 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-19 20:18:53,748 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 20:18:53,758 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-19 20:18:56,360 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 20:18:56,371 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-19 20:18:59,068 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 20:18:59,078 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-19 20:19:01,725 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 20:19:01,736 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-19 20:19:04,462 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-19 20:19:19,073 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-19_20-19-19.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │      7 │         1.96 │         107.502 │        10.75 │  1 day, 2:18:00 │    3     0     4  42.9 │
│ BTC/USDT │     11 │        -0.19 │         -20.684 │        -2.07 │ 1 day, 18:48:00 │    3     0     8  27.3 │
│ ETH/USDT │     11 │        -0.37 │         -32.245 │        -3.22 │ 1 day, 10:24:00 │    3     0     8  27.3 │
│ LTC/USDT │      4 │         -2.5 │         -67.949 │        -6.79 │  1 day, 9:36:00 │    0     0     4     0 │
│ BNB/USDT │     10 │        -1.12 │         -91.924 │        -9.19 │        20:29:00 │    1     0     9  10.0 │
│    TOTAL │     43 │        -0.32 │        -105.299 │       -10.53 │  1 day, 7:55:00 │   10     0    33  23.3 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 ENTER TAG STATS                                                 
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │      43 │        -0.32 │        -105.299 │       -10.53 │ 1 day, 7:55:00 │   10     0    33  23.3 │
│     TOTAL │      43 │        -0.32 │        -105.299 │       -10.53 │ 1 day, 7:55:00 │   10     0    33  23.3 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │    10 │          4.2 │         367.786 │        36.78 │ 1 day, 9:04:00 │   10     0     0   100 │
│      stop_loss │    33 │        -1.69 │        -473.086 │       -47.31 │ 1 day, 7:34:00 │    0     0    33     0 │
│          TOTAL │    43 │        -0.32 │        -105.299 │       -10.53 │ 1 day, 7:55:00 │   10     0    33  23.3 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_3R │     10 │          4.2 │         367.786 │        36.78 │ 1 day, 9:04:00 │   10     0     0   100 │
│           │      stop_loss │     33 │        -1.69 │        -473.086 │       -47.31 │ 1 day, 7:34:00 │    0     0    33     0 │
│     TOTAL │                │     43 │        -0.32 │        -105.299 │       -10.53 │ 1 day, 7:55:00 │   10     0    33  23.3 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-11 17:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 43 / 0.03                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 894.701 USDT                   │
│ Absolute profit               │ -105.299 USDT                  │
│ Total profit %                │ -10.53%                        │
│ CAGR %                        │ -2.97%                         │
│ Sortino                       │ -0.34                          │
│ Sharpe                        │ -0.07                          │
│ Calmar                        │ -0.80                          │
│ SQN                           │ -0.69                          │
│ Profit factor                 │ 0.78                           │
│ Expectancy (Ratio)            │ -2.45 (-0.17)                  │
│ Avg. daily profit             │ -0.078 USDT                    │
│ Avg. stake amount             │ 885.721 USDT                   │
│ Total trade volume            │ 76218.973 USDT                 │
│                               │                                │
│ Best Pair                     │ XRP/USDT 10.75%                │
│ Worst Pair                    │ BNB/USDT -9.19%                │
│ Best trade                    │ XRP/USDT 7.16%                 │
│ Worst trade                   │ LTC/USDT -4.84%                │
│ Best day                      │ 56.816 USDT                    │
│ Worst day                     │ -21.579 USDT                   │
│ Days win/draw/lose            │ 10 / 1220 / 33                 │
│ Min/Max/Avg. Duration Winners │ 0d 12:15 / 3d 08:35 / 1d 09:04 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:05 / 7d 14:05 / 1d 07:34 │
│ Max Consecutive Wins / Loss   │ 2 / 12                         │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 860.55 USDT                    │
│ Max balance                   │ 1056.816 USDT                  │
│ Max % of account underwater   │ 18.57%                         │
│ Absolute Drawdown (Account)   │ 18.57%                         │
│ Absolute Drawdown             │ 196.266 USDT                   │
│ Drawdown high                 │ 56.816 USDT                    │
│ Drawdown low                  │ -139.45 USDT                   │
│ Drawdown Start                │ 2022-03-22 04:35:00            │
│ Drawdown End                  │ 2023-09-06 17:05:00            │
│ Market change                 │ 94.84%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                  
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     43 │        -0.32 │        -105.299 │       -10.53 │ 1 day, 7:55:00 │   10     0    33  23.3 │ 196.266 USDT  18.57% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-19T22:19:20.255524",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 1696,
  "total_daily_avg_trades": "43 / 0.03",
  "absolute_profit_usdt": -105.299,
  "total_profit_pct": -10.53,
  "cagr_pct": -2.97,
  "sortino": -0.34,
  "sharpe": -0.07,
  "calmar": -0.8,
  "sqn": -0.69,
  "max_consecutive_wins_loss": "2 / 12",
  "min_balance_usdt": 860.55,
  "max_balance_usdt": 1056.816,
  "absolute_drawdown_pct": 18.57,
  "market_change_pct": 94.84,
  "win_draw_loss_winpct": "0 0 0 0"
}
```
