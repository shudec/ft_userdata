# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 5360  
**Timestamp:** 2025-09-19 14:45:11

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 5360,
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
2025-09-19 12:44:38,544 - freqtrade - INFO - freqtrade 2025.8
2025-09-19 12:44:39,115 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-19 12:44:41,486 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-19 12:44:41,491 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-19 12:44:41,492 - freqtrade.loggers - INFO - Logfile configured
2025-09-19 12:44:41,492 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-19 12:44:41,493 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-19 12:44:41,494 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-19 12:44:41,494 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-19 12:44:41,495 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-19 12:44:41,802 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-19 12:44:41,805 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-19 12:44:41,806 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-19 12:44:41,806 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-19 12:44:41,806 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-19 12:44:41,807 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-19 12:44:41,808 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-19 12:44:41,820 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-19 12:44:41,821 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 12:44:41,823 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-19 12:44:41,824 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-19 12:44:41,824 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-19 12:44:41,844 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-19 12:44:45,807 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-19 12:44:45,919 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-19 12:44:45,921 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-19 12:44:45,926 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-19 12:44:45,926 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-19 12:44:45,926 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-19 12:44:45,927 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-19 12:44:45,927 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-19 12:44:45,928 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-19 12:44:45,928 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-19 12:44:45,929 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-19 12:44:45,929 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-19 12:44:45,930 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-19 12:44:45,930 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-19 12:44:45,931 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-19 12:44:45,931 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-19 12:44:45,932 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-19 12:44:45,932 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-19 12:44:45,933 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-19 12:44:45,934 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-19 12:44:45,935 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-19 12:44:45,935 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-19 12:44:45,936 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-19 12:44:45,937 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-19 12:44:45,937 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-19 12:44:45,938 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-19 12:44:45,938 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-19 12:44:45,939 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-19 12:44:45,939 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-19 12:44:45,940 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-19 12:44:45,940 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-19 12:44:45,941 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 12:44:45,966 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-19 12:44:45,991 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-19 12:44:46,048 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 12:44:46,118 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 12:44:46,175 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 12:44:46,227 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 12:44:46,283 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 12:44:46,310 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-19 12:44:46,572 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 12:44:46,978 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 12:44:47,339 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 12:44:47,737 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 12:44:48,107 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 12:44:49,270 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-19 12:44:49,287 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-19 12:44:49,288 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-19 12:44:49,289 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-19 12:44:49,290 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2
2025-09-19 12:44:49,290 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 3
2025-09-19 12:44:49,291 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.858
2025-09-19 12:44:49,291 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.261
2025-09-19 12:44:49,292 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.025
2025-09-19 12:44:49,292 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.017
2025-09-19 12:44:49,292 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-19 12:44:49,293 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 10
2025-09-19 12:44:49,293 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 1.0
2025-09-19 12:44:49,293 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-19 12:44:49,294 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-19 12:44:49,294 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-19 12:44:49,294 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-19 12:44:49,296 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 12:44:49,310 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 12:44:51,859 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 12:44:51,877 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 12:44:54,886 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 12:44:54,907 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 12:44:58,261 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 12:44:58,277 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 12:45:01,149 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 12:45:01,164 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 12:45:04,762 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-19 12:45:10,074 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-19_12-45-10.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      2 │         0.91 │          17.669 │         1.77 │     20:40:00 │    1     0     1  50.0 │
│ ETH/USDT │      2 │         0.51 │           9.464 │         0.95 │      6:38:00 │    1     0     1  50.0 │
│ LTC/USDT │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
│ XRP/USDT │      1 │        -1.07 │         -10.624 │        -1.06 │      5:05:00 │    0     0     1     0 │
│ BTC/USDT │      6 │        -0.69 │         -27.053 │        -2.71 │      9:32:00 │    1     0     5  16.7 │
│    TOTAL │     11 │        -0.22 │         -10.544 │        -1.05 │     10:38:00 │    3     0     8  27.3 │
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
│     OTHER │      11 │        -0.22 │         -10.544 │        -1.05 │     10:38:00 │    3     0     8  27.3 │
│     TOTAL │      11 │        -0.22 │         -10.544 │        -1.05 │     10:38:00 │    3     0     8  27.3 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │     3 │         2.07 │          59.794 │         5.98 │     15:07:00 │    3     0     0   100 │
│        stop_loss │     3 │        -0.87 │         -25.751 │        -2.58 │      3:32:00 │    0     0     3     0 │
│      exit_signal │     5 │        -1.19 │         -44.587 │        -4.46 │     12:12:00 │    0     0     5     0 │
│            TOTAL │    11 │        -0.22 │         -10.544 │        -1.05 │     10:38:00 │    3     0     8  27.3 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1.5R │      3 │         2.07 │          59.794 │         5.98 │     15:07:00 │    3     0     0   100 │
│           │        stop_loss │      3 │        -0.87 │         -25.751 │        -2.58 │      3:32:00 │    0     0     3     0 │
│           │      exit_signal │      5 │        -1.19 │         -44.587 │        -4.46 │     12:12:00 │    0     0     5     0 │
│     TOTAL │                  │     11 │        -0.22 │         -10.544 │        -1.05 │     10:38:00 │    3     0     8  27.3 │
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
│ Final balance                 │ 989.456 USDT                   │
│ Absolute profit               │ -10.544 USDT                   │
│ Total profit %                │ -1.05%                         │
│ CAGR %                        │ -0.29%                         │
│ Sortino                       │ -0.03                          │
│ Sharpe                        │ -0.01                          │
│ Calmar                        │ -0.40                          │
│ SQN                           │ -0.23                          │
│ Profit factor                 │ 0.85                           │
│ Expectancy (Ratio)            │ -0.96 (-0.11)                  │
│ Avg. daily profit             │ -0.008 USDT                    │
│ Avg. stake amount             │ 918.768 USDT                   │
│ Total trade volume            │ 20242.796 USDT                 │
│                               │                                │
│ Best Pair                     │ BNB/USDT 1.77%                 │
│ Worst Pair                    │ BTC/USDT -2.71%                │
│ Best trade                    │ BNB/USDT 2.42%                 │
│ Worst trade                   │ BTC/USDT -2.80%                │
│ Best day                      │ 23.466 USDT                    │
│ Worst day                     │ -17.781 USDT                   │
│ Days win/draw/lose            │ 3 / 1078 / 8                   │
│ Min/Max/Avg. Duration Winners │ 0d 10:40 / 0d 20:20 / 0d 15:07 │
│ Min/Max/Avg. Duration Losers  │ 0d 02:35 / 0d 21:00 / 0d 08:57 │
│ Max Consecutive Wins / Loss   │ 2 / 3                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 962.529 USDT                   │
│ Max balance                   │ 1002.572 USDT                  │
│ Max % of account underwater   │ 3.75%                          │
│ Absolute drawdown             │ 37.471 USDT (3.75%)            │
│ Drawdown duration             │ 747 days 20:50:00              │
│ Profit at drawdown start      │ -10.624 USDT                   │
│ Profit at drawdown end        │ -37.471 USDT                   │
│ Drawdown start                │ 2022-09-05 05:05:00            │
│ Drawdown end                  │ 2024-09-22 01:55:00            │
│ Market change                 │ 91.49%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     11 │        -0.22 │         -10.544 │        -1.05 │     10:38:00 │    3     0     8  27.3 │ 37.471 USDT  3.75% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-19T14:45:11.253794",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 5360,
  "total_daily_avg_trades": "11 / 0.01",
  "absolute_profit_usdt": -10.544,
  "total_profit_pct": -1.05,
  "cagr_pct": -0.29,
  "sortino": -0.03,
  "sharpe": -0.01,
  "calmar": -0.4,
  "sqn": -0.23,
  "max_consecutive_wins_loss": "2 / 3",
  "min_balance_usdt": 962.529,
  "max_balance_usdt": 1002.572,
  "market_change_pct": 91.49,
  "win_draw_loss_winpct": "3 0 8 27.3"
}
```
