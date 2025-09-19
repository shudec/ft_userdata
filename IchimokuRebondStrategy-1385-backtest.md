# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 1385  
**Timestamp:** 2025-09-18 11:35:44

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 1385,
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
2025-09-18 09:34:15,322 - freqtrade - INFO - freqtrade 2025.8
2025-09-18 09:34:16,013 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-18 09:34:18,473 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-18 09:34:18,479 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-18 09:34:18,480 - freqtrade.loggers - INFO - Logfile configured
2025-09-18 09:34:18,480 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-18 09:34:18,481 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-18 09:34:18,481 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-18 09:34:18,481 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-18 09:34:18,482 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-18 09:34:18,805 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-18 09:34:18,807 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-18 09:34:18,807 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-18 09:34:18,808 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-18 09:34:18,808 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-18 09:34:18,809 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-18 09:34:18,810 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-18 09:34:18,821 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-18 09:34:18,822 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 09:34:18,824 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-18 09:34:18,825 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-18 09:34:18,826 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-18 09:34:18,847 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-18 09:34:22,896 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-18 09:34:23,024 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-18 09:34:23,026 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-18 09:34:23,030 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-18 09:34:23,031 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-18 09:34:23,031 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-18 09:34:23,032 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-18 09:34:23,032 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-18 09:34:23,033 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-18 09:34:23,033 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-18 09:34:23,034 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-18 09:34:23,034 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-18 09:34:23,034 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-18 09:34:23,035 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-18 09:34:23,035 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-18 09:34:23,035 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-18 09:34:23,036 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-18 09:34:23,036 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-18 09:34:23,036 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-18 09:34:23,037 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-18 09:34:23,037 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-18 09:34:23,038 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-18 09:34:23,038 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-18 09:34:23,039 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-18 09:34:23,039 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-18 09:34:23,040 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-18 09:34:23,040 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-18 09:34:23,041 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-18 09:34:23,041 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-18 09:34:23,041 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-18 09:34:23,042 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-18 09:34:23,042 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 09:34:23,074 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-18 09:34:23,100 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-18 09:34:23,206 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-18 09:34:23,291 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-18 09:34:23,348 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-18 09:34:23,404 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-18 09:34:23,457 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-18 09:34:23,484 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-18 09:34:23,789 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-18 09:34:24,264 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-18 09:34:24,667 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-18 09:34:25,070 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-18 09:34:25,456 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-18 09:34:26,725 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-18 09:34:26,740 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-18 09:34:26,741 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-18 09:34:26,741 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-18 09:34:26,742 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.923
2025-09-18 09:34:26,742 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.716
2025-09-18 09:34:26,743 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.01
2025-09-18 09:34:26,743 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 3
2025-09-18 09:34:26,743 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 0
2025-09-18 09:34:26,744 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-18 09:34:26,744 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-18 09:34:26,744 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-18 09:34:26,745 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-18 09:34:26,745 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-18 09:34:26,747 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 09:34:26,762 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-18 09:34:28,795 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 09:34:28,812 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-18 09:34:30,808 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 09:34:30,825 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-18 09:34:33,402 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 09:34:33,419 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-18 09:34:35,964 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 09:34:35,982 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-18 09:34:38,317 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-18 09:35:43,446 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-18_09-35-43.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │      7 │          4.4 │          26.998 │          2.7 │  9 days, 5:25:00 │    2     0     5  28.6 │
│ BTC/USDT │      6 │         3.31 │           5.451 │         0.55 │ 14 days, 0:55:00 │    4     0     2  66.7 │
│ BNB/USDT │      7 │        -2.96 │         -20.074 │        -2.01 │ 8 days, 11:00:00 │    1     0     6  14.3 │
│ XRP/USDT │     13 │        -1.63 │         -26.503 │        -2.65 │ 4 days, 22:06:00 │    3     0    10  23.1 │
│ LTC/USDT │     10 │        -5.09 │         -46.049 │         -4.6 │ 5 days, 10:36:00 │    2     0     8  20.0 │
│    TOTAL │     43 │        -0.98 │         -60.177 │        -6.02 │ 7 days, 14:11:00 │   12     0    31  27.9 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                  ENTER TAG STATS                                                  
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │      43 │        -0.98 │         -60.177 │        -6.02 │ 7 days, 14:11:00 │   12     0    31  27.9 │
│     TOTAL │      43 │        -0.98 │         -60.177 │        -6.02 │ 7 days, 14:11:00 │   12     0    31  27.9 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                   EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │     2 │        25.99 │          75.098 │         7.51 │ 14 days, 21:05:00 │    2     0     0   100 │
│      stop_loss │     2 │        -5.53 │         -41.208 │        -4.12 │   4 days, 0:48:00 │    0     0     2     0 │
│    exit_signal │    39 │        -2.13 │         -94.066 │        -9.41 │   7 days, 9:35:00 │   10     0    29  25.6 │
│          TOTAL │    43 │        -0.98 │         -60.177 │        -6.02 │  7 days, 14:11:00 │   12     0    31  27.9 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                          MIXED TAG STATS                                                           
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │      2 │        25.99 │          75.098 │         7.51 │ 14 days, 21:05:00 │    2     0     0   100 │
│           │      stop_loss │      2 │        -5.53 │         -41.208 │        -4.12 │   4 days, 0:48:00 │    0     0     2     0 │
│           │    exit_signal │     39 │        -2.13 │         -94.066 │        -9.41 │   7 days, 9:35:00 │   10     0    29  25.6 │
│     TOTAL │                │     43 │        -0.98 │         -60.177 │        -6.02 │  7 days, 14:11:00 │   12     0    31  27.9 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                          SUMMARY METRICS                           
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                            ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00              │
│ Backtesting to                │ 2025-09-10 08:00:00              │
│ Trading Mode                  │ Spot                             │
│ Max open trades               │ 3                                │
│                               │                                  │
│ Total/Daily Avg Trades        │ 43 / 0.03                        │
│ Starting balance              │ 1000 USDT                        │
│ Final balance                 │ 939.823 USDT                     │
│ Absolute profit               │ -60.177 USDT                     │
│ Total profit %                │ -6.02%                           │
│ CAGR %                        │ -1.67%                           │
│ Sortino                       │ -0.16                            │
│ Sharpe                        │ -0.08                            │
│ Calmar                        │ -0.64                            │
│ SQN                           │ -0.82                            │
│ Profit factor                 │ 0.67                             │
│ Expectancy (Ratio)            │ -1.40 (-0.24)                    │
│ Avg. daily profit             │ -0.045 USDT                      │
│ Avg. stake amount             │ 112.454 USDT                     │
│ Total trade volume            │ 9630.137 USDT                    │
│                               │                                  │
│ Best Pair                     │ ETH/USDT 2.70%                   │
│ Worst Pair                    │ LTC/USDT -4.60%                  │
│ Best trade                    │ ETH/USDT 30.95%                  │
│ Worst trade                   │ BNB/USDT -19.23%                 │
│ Best day                      │ 39.347 USDT                      │
│ Worst day                     │ -21.015 USDT                     │
│ Days win/draw/lose            │ 11 / 1230 / 30                   │
│ Min/Max/Avg. Duration Winners │ 2d 06:00 / 25d 16:55 / 10d 21:36 │
│ Min/Max/Avg. Duration Losers  │ 0d 05:00 / 49d 04:00 / 6d 07:26  │
│ Max Consecutive Wins / Loss   │ 3 / 8                            │
│ Rejected Entry signals        │ 0                                │
│ Entry/Exit Timeouts           │ 0 / 0                            │
│                               │                                  │
│ Min balance                   │ 897.769 USDT                     │
│ Max balance                   │ 1035.095 USDT                    │
│ Max % of account underwater   │ 13.27%                           │
│ Absolute drawdown             │ 137.326 USDT (13.27%)            │
│ Drawdown duration             │ 986 days 20:00:00                │
│ Profit at drawdown start      │ 35.095 USDT                      │
│ Profit at drawdown end        │ -102.231 USDT                    │
│ Drawdown start                │ 2022-07-21 03:00:00              │
│ Drawdown end                  │ 2025-04-02 23:00:00              │
│ Market change                 │ 91.49%                           │
└───────────────────────────────┴──────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     43 │        -0.98 │         -60.177 │        -6.02 │ 7 days, 14:11:00 │   12     0    31  27.9 │ 137.326 USDT  13.27% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-18T11:35:44.885127",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 1385,
  "total_daily_avg_trades": "43 / 0.03",
  "absolute_profit_usdt": -60.177,
  "total_profit_pct": -6.02,
  "cagr_pct": -1.67,
  "sortino": -0.16,
  "sharpe": -0.08,
  "calmar": -0.64,
  "sqn": -0.82,
  "max_consecutive_wins_loss": "3 / 8",
  "min_balance_usdt": 897.769,
  "max_balance_usdt": 1035.095,
  "market_change_pct": 91.49,
  "win_draw_loss_winpct": "0 0 0 0"
}
```
