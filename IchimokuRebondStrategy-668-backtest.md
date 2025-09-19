# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 668  
**Timestamp:** 2025-09-19 17:31:33

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 668,
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
2025-09-19 15:23:29,854 - freqtrade - INFO - freqtrade 2025.8
2025-09-19 15:23:30,359 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-19 15:23:32,505 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-19 15:23:32,511 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-19 15:23:32,512 - freqtrade.loggers - INFO - Logfile configured
2025-09-19 15:23:32,513 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-19 15:23:32,514 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-19 15:23:32,514 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-19 15:23:32,515 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-19 15:23:32,515 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-19 15:23:32,891 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-19 15:23:32,894 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-19 15:23:32,894 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-19 15:23:32,894 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-19 15:23:32,895 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-19 15:23:32,895 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-19 15:23:32,897 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-19 15:23:32,909 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-19 15:23:32,909 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 15:23:32,912 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-19 15:23:32,914 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-19 15:23:32,914 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-19 15:23:32,937 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-19 15:23:35,500 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-19 15:23:35,604 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-19 15:23:35,606 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-19 15:23:35,611 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-19 15:23:35,612 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-19 15:23:35,612 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-19 15:23:35,613 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-19 15:23:35,613 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-19 15:23:35,614 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-19 15:23:35,614 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-19 15:23:35,615 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-19 15:23:35,615 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-19 15:23:35,616 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-19 15:23:35,616 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-19 15:23:35,617 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-19 15:23:35,618 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-19 15:23:35,618 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-19 15:23:35,619 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-19 15:23:35,620 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-19 15:23:35,620 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-19 15:23:35,621 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-19 15:23:35,621 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-19 15:23:35,622 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-19 15:23:35,622 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-19 15:23:35,622 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-19 15:23:35,623 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-19 15:23:35,623 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-19 15:23:35,623 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-19 15:23:35,624 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-19 15:23:35,624 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-19 15:23:35,625 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-19 15:23:35,625 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 15:23:35,647 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-19 15:23:35,675 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-19 15:23:35,740 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 15:23:35,814 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 15:23:35,883 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 15:23:35,956 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 15:23:36,031 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 15:23:36,071 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-19 15:23:36,358 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 15:23:36,771 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 15:23:37,180 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 15:23:37,671 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 15:23:38,240 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 15:23:39,930 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-19 15:23:39,939 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-19 15:23:39,940 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-19 15:23:39,942 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-19 15:23:39,943 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-19 15:23:39,944 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 1
2025-09-19 15:23:39,945 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.5
2025-09-19 15:23:39,946 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-09-19 15:23:39,947 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.025
2025-09-19 15:23:39,949 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-19 15:23:39,950 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.001
2025-09-19 15:23:39,951 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-19 15:23:39,952 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 2
2025-09-19 15:23:39,953 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-09-19 15:23:39,954 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-19 15:23:39,955 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-19 15:23:39,955 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-19 15:23:39,956 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-19 15:23:39,960 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 15:23:39,990 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 15:23:43,850 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 15:23:43,871 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 15:23:47,391 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 15:23:47,414 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 15:23:51,575 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 15:23:51,598 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 15:23:55,265 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 15:23:55,286 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 15:23:58,896 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-19 15:31:31,460 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-19_15-31-31.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │    587 │        -0.16 │        -143.246 │       -14.32 │      4:32:00 │  160     0   427  27.3 │
│ BTC/USDT │    675 │        -0.19 │        -173.965 │        -17.4 │      5:11:00 │  157     0   518  23.3 │
│ LTC/USDT │    577 │        -0.25 │        -217.996 │        -21.8 │      4:25:00 │  155     0   422  26.9 │
│ BNB/USDT │    542 │        -0.27 │        -225.383 │       -22.54 │      3:35:00 │  134     0   408  24.7 │
│ XRP/USDT │    519 │        -0.31 │        -233.847 │       -23.38 │      4:12:00 │  125     0   394  24.1 │
│    TOTAL │   2900 │        -0.23 │        -994.437 │       -99.44 │      4:26:00 │  731     0  2169  25.2 │
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
│     OTHER │    2900 │        -0.23 │        -994.437 │       -99.44 │      4:26:00 │  731     0  2169  25.2 │
│     TOTAL │    2900 │        -0.23 │        -994.437 │       -99.44 │      4:26:00 │  731     0  2169  25.2 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │   604 │          1.7 │        1491.963 │        149.2 │      4:35:00 │  604     0     0   100 │
│    exit_signal │   976 │        -0.57 │        -654.670 │       -65.47 │      7:50:00 │  127     0   849  13.0 │
│      stop_loss │  1320 │        -0.86 │       -1831.730 │      -183.17 │      1:51:00 │    0     0  1320     0 │
│          TOTAL │  2900 │        -0.23 │        -994.437 │       -99.44 │      4:26:00 │  731     0  2169  25.2 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │    604 │          1.7 │        1491.963 │        149.2 │      4:35:00 │  604     0     0   100 │
│           │    exit_signal │    976 │        -0.57 │        -654.670 │       -65.47 │      7:50:00 │  127     0   849  13.0 │
│           │      stop_loss │   1320 │        -0.86 │       -1831.730 │      -183.17 │      1:51:00 │    0     0  1320     0 │
│     TOTAL │                │   2900 │        -0.23 │        -994.437 │       -99.44 │      4:26:00 │  731     0  2169  25.2 │
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
│ Total/Daily Avg Trades        │ 2900 / 2.15                    │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 5.563 USDT                     │
│ Absolute profit               │ -994.437 USDT                  │
│ Total profit %                │ -99.44%                        │
│ CAGR %                        │ -75.48%                        │
│ Sortino                       │ -6.36                          │
│ Sharpe                        │ -4.14                          │
│ Calmar                        │ -1.42                          │
│ SQN                           │ -5.43                          │
│ Profit factor                 │ 0.62                           │
│ Expectancy (Ratio)            │ -0.34 (-0.28)                  │
│ Avg. daily profit             │ -0.738 USDT                    │
│ Avg. stake amount             │ 137.829 USDT                   │
│ Total trade volume            │ 800011.849 USDT                │
│                               │                                │
│ Best Pair                     │ ETH/USDT -14.32%               │
│ Worst Pair                    │ XRP/USDT -23.38%               │
│ Best trade                    │ LTC/USDT 14.78%                │
│ Worst trade                   │ XRP/USDT -7.80%                │
│ Best day                      │ 44.762 USDT                    │
│ Worst day                     │ -53.451 USDT                   │
│ Days win/draw/lose            │ 188 / 199 / 421                │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 2d 20:05 / 0d 07:52 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 1d 15:00 / 0d 03:16 │
│ Max Consecutive Wins / Loss   │ 7 / 19                         │
│ Rejected Entry signals        │ 7648                           │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 5.563 USDT                     │
│ Max balance                   │ 991.028 USDT                   │
│ Max % of account underwater   │ 99.44%                         │
│ Absolute drawdown             │ 994.437 USDT (99.44%)          │
│ Drawdown duration             │ 807 days 01:35:00              │
│ Profit at drawdown start      │ -8.972 USDT                    │
│ Profit at drawdown end        │ -994.437 USDT                  │
│ Drawdown start                │ 2022-01-05 00:00:00            │
│ Drawdown end                  │ 2024-03-22 01:35:00            │
│ Market change                 │ 91.49%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │   2900 │        -0.23 │        -994.437 │       -99.44 │      4:26:00 │  731     0  2169  25.2 │ 994.437 USDT  99.44% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-19T17:31:33.232112",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 668,
  "total_daily_avg_trades": "2900 / 2.15",
  "absolute_profit_usdt": -994.437,
  "total_profit_pct": -99.44,
  "cagr_pct": -75.48,
  "sortino": -6.36,
  "sharpe": -4.14,
  "calmar": -1.42,
  "sqn": -5.43,
  "max_consecutive_wins_loss": "7 / 19",
  "min_balance_usdt": 5.563,
  "max_balance_usdt": 991.028,
  "market_change_pct": 91.49,
  "win_draw_loss_winpct": "731 0 2169 25.2"
}
```
