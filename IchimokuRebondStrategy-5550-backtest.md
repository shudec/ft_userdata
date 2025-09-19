# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 5550  
**Timestamp:** 2025-09-19 11:48:39

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 5550,
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
2025-09-19 09:45:59,565 - freqtrade - INFO - freqtrade 2025.8
2025-09-19 09:46:00,043 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-19 09:46:02,155 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-19 09:46:02,164 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-19 09:46:02,164 - freqtrade.loggers - INFO - Logfile configured
2025-09-19 09:46:02,165 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-19 09:46:02,166 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-19 09:46:02,166 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-19 09:46:02,167 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-19 09:46:02,167 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-19 09:46:02,552 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-19 09:46:02,554 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-19 09:46:02,555 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-19 09:46:02,555 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-19 09:46:02,556 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-19 09:46:02,556 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-19 09:46:02,557 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-19 09:46:02,571 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-19 09:46:02,572 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 09:46:02,575 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-19 09:46:02,575 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-19 09:46:02,576 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-19 09:46:02,600 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-19 09:46:07,719 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-19 09:46:07,902 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-19 09:46:07,907 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-19 09:46:07,914 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-19 09:46:07,915 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-19 09:46:07,916 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-19 09:46:07,917 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-19 09:46:07,918 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-19 09:46:07,919 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-19 09:46:07,920 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-19 09:46:07,921 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-19 09:46:07,922 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-19 09:46:07,923 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-19 09:46:07,924 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-19 09:46:07,925 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-19 09:46:07,926 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-19 09:46:07,927 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-19 09:46:07,928 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-19 09:46:07,928 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-19 09:46:07,929 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-19 09:46:07,930 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-19 09:46:07,931 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-19 09:46:07,932 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-19 09:46:07,933 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-19 09:46:07,934 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-19 09:46:07,935 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-19 09:46:07,937 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-19 09:46:07,938 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-19 09:46:07,941 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-19 09:46:07,942 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-19 09:46:07,943 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-19 09:46:07,944 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 09:46:07,979 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-19 09:46:08,019 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-19 09:46:08,099 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 09:46:08,188 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 09:46:08,287 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 09:46:08,385 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 09:46:08,475 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 09:46:08,536 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-19 09:46:10,280 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 09:46:11,356 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 09:46:12,436 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 09:46:13,178 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 09:46:13,747 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 09:46:16,095 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-19 09:46:16,101 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-19 09:46:16,103 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-19 09:46:16,105 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-19 09:46:16,106 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-19 09:46:16,106 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 3
2025-09-19 09:46:16,107 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.962
2025-09-19 09:46:16,108 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.064
2025-09-19 09:46:16,109 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.035
2025-09-19 09:46:16,110 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.019
2025-09-19 09:46:16,112 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 9
2025-09-19 09:46:16,113 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 0
2025-09-19 09:46:16,114 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-09-19 09:46:16,115 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-19 09:46:16,117 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-19 09:46:16,120 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-19 09:46:16,121 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-19 09:46:16,127 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 09:46:16,167 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 09:46:22,975 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 09:46:22,995 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 09:46:26,782 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 09:46:26,816 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 09:46:29,869 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 09:46:29,888 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 09:46:32,487 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 09:46:32,512 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 09:46:35,704 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-19 09:48:37,854 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-19_09-48-37.meta.json"
Result for strategy IchimokuRebondStrategy
                                                BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │      3 │         6.44 │          22.942 │         2.29 │  98 days, 1:47:00 │    2     0     1  66.7 │
│ XRP/USDT │      2 │        19.84 │          16.819 │         1.68 │ 59 days, 23:08:00 │    1     0     1  50.0 │
│ LTC/USDT │      0 │          0.0 │           0.000 │          0.0 │              0:00 │    0     0     0     0 │
│ ETH/USDT │      3 │        -5.56 │          -3.127 │        -0.31 │ 40 days, 20:55:00 │    1     0     2  33.3 │
│ BNB/USDT │      1 │        -8.68 │         -20.243 │        -2.02 │          11:15:00 │    0     0     1     0 │
│    TOTAL │      9 │         3.74 │          16.391 │         1.64 │ 59 days, 16:37:00 │    4     0     5  44.4 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                              LEFT OPEN TRADES REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃       Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │      1 │        10.11 │           5.162 │         0.52 │ 268 days, 23:00:00 │    1     0     0   100 │
│    TOTAL │      1 │        10.11 │           5.162 │         0.52 │ 268 days, 23:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────────┴────────────────────────┘
                                                  ENTER TAG STATS                                                   
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │       9 │         3.74 │          16.391 │         1.64 │ 59 days, 16:37:00 │    4     0     5  44.4 │
│     TOTAL │       9 │         3.74 │          16.391 │         1.64 │ 59 days, 16:37:00 │    4     0     5  44.4 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                   EXIT REASON STATS                                                    
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃       Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │     3 │        32.42 │         107.467 │        10.75 │  32 days, 19:32:00 │    3     0     0   100 │
│     force_exit │     1 │        10.11 │           5.162 │         0.52 │ 268 days, 23:00:00 │    1     0     0   100 │
│    exit_signal │     1 │       -30.79 │         -16.844 │        -1.68 │   65 days, 3:00:00 │    0     0     1     0 │
│      stop_loss │     4 │       -10.74 │         -79.394 │        -7.94 │   26 days, 4:15:00 │    0     0     4     0 │
│          TOTAL │     9 │         3.74 │          16.391 │         1.64 │  59 days, 16:37:00 │    4     0     5  44.4 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────────┴────────────────────────┘
                                                           MIXED TAG STATS                                                           
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃       Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │      3 │        32.42 │         107.467 │        10.75 │  32 days, 19:32:00 │    3     0     0   100 │
│           │     force_exit │      1 │        10.11 │           5.162 │         0.52 │ 268 days, 23:00:00 │    1     0     0   100 │
│           │    exit_signal │      1 │       -30.79 │         -16.844 │        -1.68 │   65 days, 3:00:00 │    0     0     1     0 │
│           │      stop_loss │      4 │       -10.74 │         -79.394 │        -7.94 │   26 days, 4:15:00 │    0     0     4     0 │
│     TOTAL │                │      9 │         3.74 │          16.391 │         1.64 │  59 days, 16:37:00 │    4     0     5  44.4 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────────┴────────────────────────┘
                           SUMMARY METRICS                           
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                             ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00               │
│ Backtesting to                │ 2025-09-10 08:00:00               │
│ Trading Mode                  │ Spot                              │
│ Max open trades               │ 3                                 │
│                               │                                   │
│ Total/Daily Avg Trades        │ 9 / 0.01                          │
│ Starting balance              │ 1000 USDT                         │
│ Final balance                 │ 1016.391 USDT                     │
│ Absolute profit               │ 16.391 USDT                       │
│ Total profit %                │ 1.64%                             │
│ CAGR %                        │ 0.44%                             │
│ Sortino                       │ 0.19                              │
│ Sharpe                        │ 0.01                              │
│ Calmar                        │ 0.39                              │
│ SQN                           │ 0.20                              │
│ Profit factor                 │ 1.17                              │
│ Expectancy (Ratio)            │ 1.82 (0.09)                       │
│ Avg. daily profit             │ 0.012 USDT                        │
│ Avg. stake amount             │ 170.685 USDT                      │
│ Total trade volume            │ 3094.897 USDT                     │
│                               │                                   │
│ Best Pair                     │ BTC/USDT 2.29%                    │
│ Worst Pair                    │ BNB/USDT -2.02%                   │
│ Best trade                    │ XRP/USDT 55.88%                   │
│ Worst trade                   │ ETH/USDT -30.79%                  │
│ Best day                      │ 37.712 USDT                       │
│ Worst day                     │ -20.243 USDT                      │
│ Days win/draw/lose            │ 4 / 1172 / 5                      │
│ Min/Max/Avg. Duration Winners │ 3d 03:20 / 268d 23:00 / 91d 20:24 │
│ Min/Max/Avg. Duration Losers  │ 0d 11:15 / 65d 03:00 / 33d 23:12  │
│ Max Consecutive Wins / Loss   │ 3 / 3                             │
│ Rejected Entry signals        │ 0                                 │
│ Entry/Exit Timeouts           │ 0 / 0                             │
│                               │                                   │
│ Min balance                   │ 940.21 USDT                       │
│ Max balance                   │ 1016.391 USDT                     │
│ Max % of account underwater   │ 5.98%                             │
│ Absolute drawdown             │ 59.79 USDT (5.98%)                │
│ Drawdown duration             │ 352 days 07:45:00                 │
│ Profit at drawdown start      │ -20.243 USDT                      │
│ Profit at drawdown end        │ -59.79 USDT                       │
│ Drawdown start                │ 2022-06-18 08:15:00               │
│ Drawdown end                  │ 2023-06-05 16:00:00               │
│ Market change                 │ 91.49%                            │
└───────────────────────────────┴───────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                  
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃          Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │      9 │         3.74 │          16.391 │         1.64 │ 59 days, 16:37:00 │    4     0     5  44.4 │ 59.79 USDT  5.98% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┴───────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-19T11:48:39.351293",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 5550,
  "total_daily_avg_trades": "9 / 0.01",
  "absolute_profit_usdt": 16.391,
  "total_profit_pct": 1.64,
  "cagr_pct": 0.44,
  "sortino": 0.19,
  "sharpe": 0.01,
  "calmar": 0.39,
  "sqn": 0.2,
  "max_consecutive_wins_loss": "3 / 3",
  "min_balance_usdt": 940.21,
  "max_balance_usdt": 1016.391,
  "market_change_pct": 91.49
}
```
