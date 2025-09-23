# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 7934  
**Timestamp:** 2025-09-23 09:53:04

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 7934,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20180101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20180101-20251231
```

## Backtesting Output
```
2025-09-23 07:47:34,601 - freqtrade - INFO - freqtrade 2025.8
2025-09-23 07:47:35,153 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-23 07:47:37,872 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-23 07:47:37,879 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-23 07:47:37,880 - freqtrade.loggers - INFO - Logfile configured
2025-09-23 07:47:37,880 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-23 07:47:37,881 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-23 07:47:37,881 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-23 07:47:37,882 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-23 07:47:37,882 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20251231 ...
2025-09-23 07:47:38,241 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-23 07:47:38,243 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-23 07:47:38,243 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-23 07:47:38,244 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-23 07:47:38,244 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-23 07:47:38,245 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20251231
2025-09-23 07:47:38,246 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-23 07:47:38,258 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-23 07:47:38,259 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 07:47:38,261 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-23 07:47:38,262 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-23 07:47:38,262 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-23 07:47:38,283 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-23 07:47:40,956 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-23 07:47:41,096 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-23 07:47:41,098 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-23 07:47:41,103 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-23 07:47:41,104 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-23 07:47:41,104 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-23 07:47:41,105 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-23 07:47:41,105 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-23 07:47:41,106 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-23 07:47:41,107 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-23 07:47:41,107 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-23 07:47:41,108 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-23 07:47:41,109 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-23 07:47:41,109 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-23 07:47:41,110 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-23 07:47:41,110 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-23 07:47:41,110 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-23 07:47:41,111 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-23 07:47:41,111 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-23 07:47:41,112 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-23 07:47:41,113 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-23 07:47:41,113 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-23 07:47:41,114 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-23 07:47:41,114 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-23 07:47:41,114 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-23 07:47:41,115 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-23 07:47:41,116 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-23 07:47:41,117 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-23 07:47:41,117 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-23 07:47:41,118 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-23 07:47:41,119 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-23 07:47:41,120 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 07:47:41,147 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-23 07:47:41,175 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-23 07:47:41,293 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:47:41,454 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:47:41,562 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:47:41,678 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-23 07:47:41,680 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:47:41,786 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:47:41,846 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 07:47:42,225 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:47:43,143 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:47:43,942 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:47:44,822 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-23 07:47:44,823 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:47:45,708 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:47:49,496 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-23 07:47:49,519 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-23 07:47:49,520 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-23 07:47:49,522 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.5
2025-09-23 07:47:49,523 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-23 07:47:49,524 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = True
2025-09-23 07:47:49,527 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2
2025-09-23 07:47:49,529 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 17
2025-09-23 07:47:49,530 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.557
2025-09-23 07:47:49,531 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.695
2025-09-23 07:47:49,532 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.007
2025-09-23 07:47:49,533 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-23 07:47:49,535 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-23 07:47:49,536 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 2
2025-09-23 07:47:49,537 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-23 07:47:49,538 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 9
2025-09-23 07:47:49,539 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-23 07:47:49,541 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-23 07:47:49,543 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-23 07:47:49,544 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower
2025-09-23 07:47:49,547 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-23 07:47:49,549 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-23 07:47:49,557 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:47:49,600 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:48:13,725 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:48:13,741 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:48:35,421 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:48:35,440 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:48:57,549 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:48:57,570 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-23 07:48:57,571 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:49:19,873 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:49:19,890 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:49:41,733 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 07:53:01,797 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-23_07-53-01.meta.json"
Result for strategy IchimokuRebondStrategy
                                              BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ LTC/USDT │     93 │         0.06 │         -50.923 │        -5.09 │       22:27:00 │   36     0    57  38.7 │
│ XRP/USDT │     99 │         0.11 │         -91.535 │        -9.15 │       20:27:00 │   36     0    63  36.4 │
│ ETH/USDT │    114 │        -0.47 │        -131.241 │       -13.12 │ 1 day, 0:24:00 │   42     0    72  36.8 │
│ BTC/USDT │    163 │        -0.15 │        -131.596 │       -13.16 │ 1 day, 2:50:00 │   65     0    98  39.9 │
│ BNB/USDT │    115 │        -0.13 │        -140.260 │       -14.03 │       20:45:00 │   44     0    71  38.3 │
│    TOTAL │    584 │        -0.13 │        -545.555 │       -54.56 │       23:23:00 │  223     0   361  38.2 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                           LEFT OPEN TRADES REPORT                                           
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         0.04 │           0.176 │         0.02 │      2:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         0.04 │           0.176 │         0.02 │      2:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                    ENTER TAG STATS                                                     
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│    hammer_rebond │      55 │         0.21 │          -6.668 │        -0.67 │       14:22:00 │   18     0    37  32.7 │
│ engulfing_rebond │     529 │        -0.17 │        -538.887 │       -53.89 │ 1 day, 0:19:00 │  205     0   324  38.8 │
│            TOTAL │     584 │        -0.13 │        -545.555 │       -54.56 │       23:23:00 │  223     0   361  38.2 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │   222 │         4.01 │        3300.110 │       330.01 │ 1 day, 3:46:00 │  222     0     0   100 │
│       force_exit │     1 │         0.04 │           0.176 │         0.02 │        2:00:00 │    1     0     0   100 │
│        stop_loss │   361 │        -2.67 │       -3845.841 │      -384.58 │       20:45:00 │    0     0   361     0 │
│            TOTAL │   584 │        -0.13 │        -545.555 │       -54.56 │       23:23:00 │  223     0   361  38.2 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                             MIXED TAG STATS                                                              
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │ take_profit_1.5R │    204 │         3.92 │        2931.889 │       293.19 │ 1 day, 4:26:00 │  204     0     0   100 │
│    hammer_rebond │ take_profit_1.5R │     18 │         4.98 │         368.222 │        36.82 │       20:11:00 │   18     0     0   100 │
│ engulfing_rebond │       force_exit │      1 │         0.04 │           0.176 │         0.02 │        2:00:00 │    1     0     0   100 │
│    hammer_rebond │        stop_loss │     37 │        -2.11 │        -374.890 │       -37.49 │       11:31:00 │    0     0    37     0 │
│ engulfing_rebond │        stop_loss │    324 │        -2.74 │       -3470.951 │       -347.1 │       21:48:00 │    0     0   324     0 │
│            TOTAL │                  │    584 │        -0.13 │        -545.555 │       -54.56 │       23:23:00 │  223     0   361  38.2 │
└──────────────────┴──────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2018-01-01 00:00:00             │
│ Backtesting to                │ 2025-09-10 08:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 584 / 0.21                      │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 454.445 USDT                    │
│ Absolute profit               │ -545.555 USDT                   │
│ Total profit %                │ -54.56%                         │
│ CAGR %                        │ -9.74%                          │
│ Sortino                       │ -0.72                           │
│ Sharpe                        │ -0.27                           │
│ Calmar                        │ -0.59                           │
│ SQN                           │ -1.62                           │
│ Profit factor                 │ 0.86                            │
│ Expectancy (Ratio)            │ -0.93 (-0.09)                   │
│ Avg. daily profit             │ -0.194 USDT                     │
│ Avg. stake amount             │ 449.437 USDT                    │
│ Total trade volume            │ 525446.443 USDT                 │
│                               │                                 │
│ Best Pair                     │ LTC/USDT -5.09%                 │
│ Worst Pair                    │ BNB/USDT -14.03%                │
│ Best trade                    │ BNB/USDT 24.24%                 │
│ Worst trade                   │ ETH/USDT -10.36%                │
│ Best day                      │ 53.323 USDT                     │
│ Worst day                     │ -32.851 USDT                    │
│ Days win/draw/lose            │ 194 / 2277 / 311                │
│ Min/Max/Avg. Duration Winners │ 0d 00:25 / 12d 13:05 / 1d 03:39 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 14d 02:35 / 0d 20:45 │
│ Max Consecutive Wins / Loss   │ 7 / 11                          │
│ Rejected Entry signals        │ 36                              │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 374.633 USDT                    │
│ Max balance                   │ 1023.415 USDT                   │
│ Max % of account underwater   │ 63.39%                          │
│ Absolute drawdown             │ 648.782 USDT (63.39%)           │
│ Drawdown duration             │ 2287 days 20:55:00              │
│ Profit at drawdown start      │ 23.415 USDT                     │
│ Profit at drawdown end        │ -625.367 USDT                   │
│ Drawdown start                │ 2018-04-24 16:50:00             │
│ Drawdown end                  │ 2024-07-29 13:45:00             │
│ Market change                 │ 2372.94%                        │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    584 │        -0.13 │        -545.555 │       -54.56 │     23:23:00 │  223     0   361  38.2 │ 648.782 USDT  63.39% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-23T09:53:04.171751",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 7934,
  "total_daily_avg_trades": "584 / 0.21",
  "absolute_profit_usdt": -545.555,
  "total_profit_pct": -54.56,
  "cagr_pct": -9.74,
  "sortino": -0.72,
  "sharpe": -0.27,
  "calmar": -0.59,
  "sqn": -1.62,
  "max_consecutive_wins_loss": "7 / 11",
  "min_balance_usdt": 374.633,
  "max_balance_usdt": 1023.415,
  "absolute_drawdown_pct": 63.39,
  "market_change_pct": 2372.94,
  "win_draw_loss_winpct": "223 0 361 38.2"
}
```
