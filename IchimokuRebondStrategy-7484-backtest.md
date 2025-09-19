# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 7484  
**Timestamp:** 2025-09-18 11:19:10

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 7484,
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
2025-09-18 09:18:36,951 - freqtrade - INFO - freqtrade 2025.8
2025-09-18 09:18:37,900 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-18 09:18:40,723 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-18 09:18:40,730 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-18 09:18:40,731 - freqtrade.loggers - INFO - Logfile configured
2025-09-18 09:18:40,731 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-18 09:18:40,732 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-18 09:18:40,732 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-18 09:18:40,733 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-18 09:18:40,733 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-18 09:18:41,012 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-18 09:18:41,014 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-18 09:18:41,015 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-18 09:18:41,015 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-18 09:18:41,015 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-18 09:18:41,016 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-18 09:18:41,017 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-18 09:18:41,027 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-18 09:18:41,028 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 09:18:41,030 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-18 09:18:41,031 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-18 09:18:41,031 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-18 09:18:41,051 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-18 09:18:43,263 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-18 09:18:43,366 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-18 09:18:43,368 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-18 09:18:43,373 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-18 09:18:43,373 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-18 09:18:43,374 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-18 09:18:43,374 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-18 09:18:43,375 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-18 09:18:43,375 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-18 09:18:43,375 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-18 09:18:43,376 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-18 09:18:43,376 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-18 09:18:43,376 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-18 09:18:43,377 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-18 09:18:43,377 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-18 09:18:43,377 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-18 09:18:43,378 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-18 09:18:43,379 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-18 09:18:43,379 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-18 09:18:43,380 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-18 09:18:43,381 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-18 09:18:43,381 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-18 09:18:43,382 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-18 09:18:43,382 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-18 09:18:43,383 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-18 09:18:43,383 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-18 09:18:43,383 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-18 09:18:43,384 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-18 09:18:43,384 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-18 09:18:43,384 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-18 09:18:43,385 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-18 09:18:43,385 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 09:18:43,408 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-18 09:18:43,433 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-18 09:18:43,601 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-18 09:18:43,678 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-18 09:18:43,732 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-18 09:18:43,787 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-18 09:18:43,839 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-18 09:18:43,861 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-18 09:18:44,159 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-18 09:18:44,681 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-18 09:18:45,111 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-18 09:18:45,518 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-18 09:18:45,931 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-18 09:18:47,302 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-18 09:18:47,308 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-18 09:18:47,309 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-18 09:18:47,309 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-18 09:18:47,310 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.491
2025-09-18 09:18:47,310 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.909
2025-09-18 09:18:47,311 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.009
2025-09-18 09:18:47,311 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 2
2025-09-18 09:18:47,312 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 4
2025-09-18 09:18:47,312 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.991
2025-09-18 09:18:47,312 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-18 09:18:47,313 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-18 09:18:47,313 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-18 09:18:47,314 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-18 09:18:47,317 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 09:18:47,345 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-18 09:18:50,439 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 09:18:50,453 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-18 09:18:53,030 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 09:18:53,045 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-18 09:18:56,080 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 09:18:56,097 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-18 09:18:59,217 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 09:18:59,237 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-18 09:19:01,955 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-18 09:19:09,625 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-18_09-19-09.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │      3 │         2.28 │          44.094 │         4.41 │ 1 day, 22:40:00 │    2     0     1  66.7 │
│ LTC/USDT │      1 │         3.16 │          30.237 │         3.02 │ 2 days, 3:50:00 │    1     0     0   100 │
│ ETH/USDT │      0 │          0.0 │           0.000 │          0.0 │            0:00 │    0     0     0     0 │
│ BNB/USDT │      3 │         -0.7 │         -31.318 │        -3.13 │  1 day, 6:53:00 │    1     0     2  33.3 │
│ XRP/USDT │      6 │         -2.0 │         -77.697 │        -7.77 │ 1 day, 13:49:00 │    1     0     5  16.7 │
│    TOTAL │     13 │        -0.32 │         -34.684 │        -3.47 │ 1 day, 15:20:00 │    5     0     8  38.5 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 ENTER TAG STATS                                                  
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │      13 │        -0.32 │         -34.684 │        -3.47 │ 1 day, 15:20:00 │    5     0     8  38.5 │
│     TOTAL │      13 │        -0.32 │         -34.684 │        -3.47 │ 1 day, 15:20:00 │    5     0     8  38.5 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                   EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │     5 │         4.13 │         140.437 │        14.04 │ 2 days, 8:56:00 │    5     0     0   100 │
│        stop_loss │     8 │         -3.1 │        -175.121 │       -17.51 │  1 day, 4:21:00 │    0     0     8     0 │
│            TOTAL │    13 │        -0.32 │         -34.684 │        -3.47 │ 1 day, 15:20:00 │    5     0     8  38.5 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                          MIXED TAG STATS                                                           
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1.5R │      5 │         4.13 │         140.437 │        14.04 │ 2 days, 8:56:00 │    5     0     0   100 │
│           │        stop_loss │      8 │         -3.1 │        -175.121 │       -17.51 │  1 day, 4:21:00 │    0     0     8     0 │
│     TOTAL │                  │     13 │        -0.32 │         -34.684 │        -3.47 │ 1 day, 15:20:00 │    5     0     8  38.5 │
└───────────┴──────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 13 / 0.01                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 965.316 USDT                   │
│ Absolute profit               │ -34.684 USDT                   │
│ Total profit %                │ -3.47%                         │
│ CAGR %                        │ -0.95%                         │
│ Sortino                       │ -0.53                          │
│ Sharpe                        │ -0.02                          │
│ Calmar                        │ -0.38                          │
│ SQN                           │ -0.37                          │
│ Profit factor                 │ 0.80                           │
│ Expectancy (Ratio)            │ -2.67 (-0.12)                  │
│ Avg. daily profit             │ -0.026 USDT                    │
│ Avg. stake amount             │ 742.545 USDT                   │
│ Total trade volume            │ 19310.056 USDT                 │
│                               │                                │
│ Best Pair                     │ BTC/USDT 4.41%                 │
│ Worst Pair                    │ XRP/USDT -7.77%                │
│ Best trade                    │ BTC/USDT 5.42%                 │
│ Worst trade                   │ XRP/USDT -5.08%                │
│ Best day                      │ 33.614 USDT                    │
│ Worst day                     │ -23.599 USDT                   │
│ Days win/draw/lose            │ 5 / 1078 / 8                   │
│ Min/Max/Avg. Duration Winners │ 0d 09:35 / 4d 09:10 / 2d 08:56 │
│ Min/Max/Avg. Duration Losers  │ 0d 03:55 / 4d 03:55 / 1d 04:21 │
│ Max Consecutive Wins / Loss   │ 4 / 6                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 965.316 USDT                   │
│ Max balance                   │ 1108.611 USDT                  │
│ Max % of account underwater   │ 12.93%                         │
│ Absolute drawdown             │ 143.296 USDT (12.93%)          │
│ Drawdown duration             │ 979 days 23:00:00              │
│ Profit at drawdown start      │ 108.611 USDT                   │
│ Profit at drawdown end        │ -34.684 USDT                   │
│ Drawdown start                │ 2022-07-07 14:55:00            │
│ Drawdown end                  │ 2025-03-13 13:55:00            │
│ Market change                 │ 91.49%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     13 │        -0.32 │         -34.684 │        -3.47 │ 1 day, 15:20:00 │    5     0     8  38.5 │ 143.296 USDT  12.93% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-18T11:19:10.885021",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 7484,
  "total_daily_avg_trades": "13 / 0.01",
  "absolute_profit_usdt": -34.684,
  "total_profit_pct": -3.47,
  "cagr_pct": -0.95,
  "sortino": -0.53,
  "sharpe": -0.02,
  "calmar": -0.38,
  "sqn": -0.37,
  "max_consecutive_wins_loss": "4 / 6",
  "min_balance_usdt": 965.316,
  "max_balance_usdt": 1108.611,
  "market_change_pct": 91.49,
  "win_draw_loss_winpct": "0 0 0 0"
}
```
