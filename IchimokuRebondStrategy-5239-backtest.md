# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 5239  
**Timestamp:** 2025-09-19 14:32:58

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 5239,
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
2025-09-19 12:32:22,905 - freqtrade - INFO - freqtrade 2025.8
2025-09-19 12:32:23,523 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-19 12:32:26,464 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-19 12:32:26,472 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-19 12:32:26,473 - freqtrade.loggers - INFO - Logfile configured
2025-09-19 12:32:26,474 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-19 12:32:26,475 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-19 12:32:26,475 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-19 12:32:26,476 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-19 12:32:26,477 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-19 12:32:26,900 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-19 12:32:26,903 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-19 12:32:26,903 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-19 12:32:26,904 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-19 12:32:26,904 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-19 12:32:26,905 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-19 12:32:26,907 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-19 12:32:26,919 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-19 12:32:26,920 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 12:32:26,922 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-19 12:32:26,923 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-19 12:32:26,924 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-19 12:32:26,946 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-19 12:32:31,273 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-19 12:32:31,361 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-19 12:32:31,364 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-19 12:32:31,370 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-19 12:32:31,370 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-19 12:32:31,371 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-19 12:32:31,371 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-19 12:32:31,372 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-19 12:32:31,372 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-19 12:32:31,372 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-19 12:32:31,373 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-19 12:32:31,373 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-19 12:32:31,374 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-19 12:32:31,374 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-19 12:32:31,375 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-19 12:32:31,375 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-19 12:32:31,375 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-19 12:32:31,376 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-19 12:32:31,376 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-19 12:32:31,376 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-19 12:32:31,377 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-19 12:32:31,377 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-19 12:32:31,378 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-19 12:32:31,378 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-19 12:32:31,379 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-19 12:32:31,379 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-19 12:32:31,379 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-19 12:32:31,380 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-19 12:32:31,380 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-19 12:32:31,381 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-19 12:32:31,382 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-19 12:32:31,382 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 12:32:31,412 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-19 12:32:31,454 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-19 12:32:31,567 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 12:32:31,663 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 12:32:31,752 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 12:32:31,827 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 12:32:31,895 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 12:32:31,928 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-19 12:32:32,199 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 12:32:32,629 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 12:32:32,992 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 12:32:33,386 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 12:32:33,980 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 12:32:35,764 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-19 12:32:35,772 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-19 12:32:35,773 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-19 12:32:35,774 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-19 12:32:35,774 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2
2025-09-19 12:32:35,775 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 3
2025-09-19 12:32:35,776 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.858
2025-09-19 12:32:35,776 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.261
2025-09-19 12:32:35,777 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.025
2025-09-19 12:32:35,777 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.017
2025-09-19 12:32:35,778 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-19 12:32:35,779 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 10
2025-09-19 12:32:35,779 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 1.0
2025-09-19 12:32:35,780 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-19 12:32:35,781 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-19 12:32:35,781 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-19 12:32:35,782 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-19 12:32:35,786 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 12:32:35,805 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 12:32:39,117 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 12:32:39,132 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 12:32:41,992 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 12:32:42,012 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 12:32:45,041 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 12:32:45,060 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 12:32:48,110 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 12:32:48,124 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 12:32:51,020 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-19 12:32:57,422 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-19_12-32-57.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │      2 │         0.51 │           9.723 │         0.97 │         6:38:00 │    1     0     1  50.0 │
│ BNB/USDT │      2 │         0.26 │           4.866 │         0.49 │ 1 day, 11:18:00 │    1     0     1  50.0 │
│ LTC/USDT │      0 │          0.0 │           0.000 │          0.0 │            0:00 │    0     0     0     0 │
│ XRP/USDT │      1 │        -1.07 │         -10.624 │        -1.06 │         5:05:00 │    0     0     1     0 │
│ BTC/USDT │      6 │        -0.81 │         -30.203 │        -3.02 │        20:32:00 │    2     0     4  33.3 │
│    TOTAL │     11 │         -0.4 │         -26.238 │        -2.62 │        19:17:00 │    4     0     7  36.4 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
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
│     OTHER │      11 │         -0.4 │         -26.238 │        -2.62 │     19:17:00 │    4     0     7  36.4 │
│     TOTAL │      11 │         -0.4 │         -26.238 │        -2.62 │     19:17:00 │    4     0     7  36.4 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │     4 │         1.87 │          71.818 │         7.18 │     12:46:00 │    4     0     0   100 │
│        stop_loss │     7 │         -1.7 │         -98.056 │        -9.81 │     23:01:00 │    0     0     7     0 │
│            TOTAL │    11 │         -0.4 │         -26.238 │        -2.62 │     19:17:00 │    4     0     7  36.4 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1.5R │      4 │         1.87 │          71.818 │         7.18 │     12:46:00 │    4     0     0   100 │
│           │        stop_loss │      7 │         -1.7 │         -98.056 │        -9.81 │     23:01:00 │    0     0     7     0 │
│     TOTAL │                  │     11 │         -0.4 │         -26.238 │        -2.62 │     19:17:00 │    4     0     7  36.4 │
└───────────┴──────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 11 / 0.01                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 973.762 USDT                   │
│ Absolute profit               │ -26.238 USDT                   │
│ Total profit %                │ -2.62%                         │
│ CAGR %                        │ -0.72%                         │
│ Sortino                       │ -0.06                          │
│ Sharpe                        │ -0.02                          │
│ Calmar                        │ -0.84                          │
│ SQN                           │ -0.46                          │
│ Profit factor                 │ 0.73                           │
│ Expectancy (Ratio)            │ -2.39 (-0.17)                  │
│ Avg. daily profit             │ -0.019 USDT                    │
│ Avg. stake amount             │ 916.927 USDT                   │
│ Total trade volume            │ 20186.494 USDT                 │
│                               │                                │
│ Best Pair                     │ ETH/USDT 0.97%                 │
│ Worst Pair                    │ BTC/USDT -3.02%                │
│ Best trade                    │ BNB/USDT 2.42%                 │
│ Worst trade                   │ BTC/USDT -3.28%                │
│ Best day                      │ 23.315 USDT                    │
│ Worst day                     │ -21.066 USDT                   │
│ Days win/draw/lose            │ 4 / 1079 / 7                   │
│ Min/Max/Avg. Duration Winners │ 0d 05:45 / 0d 20:20 / 0d 12:46 │
│ Min/Max/Avg. Duration Losers  │ 0d 02:35 / 2d 10:30 / 0d 23:01 │
│ Max Consecutive Wins / Loss   │ 2 / 3                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 956.06 USDT                    │
│ Max balance                   │ 1000.383 USDT                  │
│ Max % of account underwater   │ 4.43%                          │
│ Absolute drawdown             │ 44.323 USDT (4.43%)            │
│ Drawdown duration             │ 166 days 18:15:00              │
│ Profit at drawdown start      │ 0.383 USDT                     │
│ Profit at drawdown end        │ -43.94 USDT                    │
│ Drawdown start                │ 2024-04-08 07:40:00            │
│ Drawdown end                  │ 2024-09-22 01:55:00            │
│ Market change                 │ 91.49%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     11 │        -0.40 │         -26.238 │        -2.62 │     19:17:00 │    4     0     7  36.4 │ 44.323 USDT  4.43% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-19T14:32:58.716570",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 5239,
  "total_daily_avg_trades": "11 / 0.01",
  "absolute_profit_usdt": -26.238,
  "total_profit_pct": -2.62,
  "cagr_pct": -0.72,
  "sortino": -0.06,
  "sharpe": -0.02,
  "calmar": -0.84,
  "sqn": -0.46,
  "max_consecutive_wins_loss": "2 / 3",
  "min_balance_usdt": 956.06,
  "max_balance_usdt": 1000.383,
  "market_change_pct": 91.49,
  "win_draw_loss_winpct": "4 0 7 36.4"
}
```
