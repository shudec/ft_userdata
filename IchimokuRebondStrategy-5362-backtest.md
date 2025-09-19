# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 5362  
**Timestamp:** 2025-09-19 16:05:05

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 5362,
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
2025-09-19 13:54:03,180 - freqtrade - INFO - freqtrade 2025.8
2025-09-19 13:54:03,541 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-19 13:54:05,146 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-19 13:54:05,153 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-19 13:54:05,154 - freqtrade.loggers - INFO - Logfile configured
2025-09-19 13:54:05,155 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-19 13:54:05,155 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-19 13:54:05,156 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-19 13:54:05,156 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-19 13:54:05,157 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-19 13:54:05,521 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-19 13:54:05,524 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-19 13:54:05,524 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-19 13:54:05,525 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-19 13:54:05,525 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-19 13:54:05,525 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-19 13:54:05,526 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-19 13:54:05,540 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-19 13:54:05,541 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 13:54:05,544 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-19 13:54:05,545 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-19 13:54:05,545 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-19 13:54:05,567 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-19 13:54:08,528 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-19 13:54:08,657 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-19 13:54:08,659 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-19 13:54:08,665 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-19 13:54:08,666 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-19 13:54:08,666 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-19 13:54:08,666 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-19 13:54:08,667 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-19 13:54:08,667 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-19 13:54:08,668 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-19 13:54:08,669 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-19 13:54:08,670 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-19 13:54:08,670 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-19 13:54:08,670 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-19 13:54:08,671 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-19 13:54:08,671 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-19 13:54:08,671 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-19 13:54:08,672 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-19 13:54:08,673 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-19 13:54:08,673 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-19 13:54:08,673 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-19 13:54:08,674 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-19 13:54:08,674 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-19 13:54:08,675 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-19 13:54:08,676 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-19 13:54:08,677 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-19 13:54:08,678 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-19 13:54:08,679 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-19 13:54:08,679 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-19 13:54:08,680 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-19 13:54:08,681 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-19 13:54:08,682 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 13:54:08,720 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-19 13:54:08,764 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-19 13:54:08,888 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 13:54:09,010 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 13:54:09,080 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 13:54:09,154 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 13:54:09,222 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 13:54:09,250 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-19 13:54:09,569 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 13:54:10,100 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 13:54:10,586 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 13:54:11,088 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 13:54:11,495 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 13:54:13,045 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-19 13:54:13,051 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-19 13:54:13,052 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-19 13:54:13,053 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-19 13:54:13,054 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-19 13:54:13,054 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 1
2025-09-19 13:54:13,055 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.5
2025-09-19 13:54:13,056 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-09-19 13:54:13,057 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.025
2025-09-19 13:54:13,058 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.05
2025-09-19 13:54:13,059 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.05
2025-09-19 13:54:13,059 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-19 13:54:13,060 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 2
2025-09-19 13:54:13,060 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.995
2025-09-19 13:54:13,061 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-19 13:54:13,061 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-19 13:54:13,062 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-19 13:54:13,062 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-19 13:54:13,066 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 13:54:13,092 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 13:54:16,894 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 13:54:16,912 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 13:54:20,442 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 13:54:20,461 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 13:54:24,390 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 13:54:24,406 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 13:54:27,579 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 13:54:27,597 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 13:54:30,789 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-19 14:05:03,643 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-19_14-05-03.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ LTC/USDT │    647 │        -0.26 │         -99.333 │        -9.93 │      6:23:00 │  178     0   469  27.5 │
│ ETH/USDT │    620 │        -0.18 │        -140.196 │       -14.02 │      6:42:00 │  194     0   426  31.3 │
│ BTC/USDT │    641 │         -0.2 │        -202.112 │       -20.21 │      7:39:00 │  169     0   472  26.4 │
│ BNB/USDT │    529 │        -0.35 │        -266.942 │       -26.69 │      6:02:00 │  128     0   401  24.2 │
│ XRP/USDT │    546 │        -0.34 │        -285.857 │       -28.59 │      5:35:00 │  138     0   408  25.3 │
│    TOTAL │   2983 │        -0.26 │        -994.440 │       -99.44 │      6:31:00 │  807     0  2176  27.1 │
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
│     OTHER │    2983 │        -0.26 │        -994.440 │       -99.44 │      6:31:00 │  807     0  2176  27.1 │
│     TOTAL │    2983 │        -0.26 │        -994.440 │       -99.44 │      6:31:00 │  807     0  2176  27.1 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │   649 │         2.49 │        1967.237 │       196.72 │      7:06:00 │  649     0     0   100 │
│      exit_signal │  1401 │        -0.74 │       -1160.020 │       -116.0 │      8:33:00 │  158     0  1243  11.3 │
│        stop_loss │   933 │        -1.46 │       -1801.656 │      -180.17 │      3:03:00 │    0     0   933     0 │
│            TOTAL │  2983 │        -0.26 │        -994.440 │       -99.44 │      6:31:00 │  807     0  2176  27.1 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1.5R │    649 │         2.49 │        1967.237 │       196.72 │      7:06:00 │  649     0     0   100 │
│           │      exit_signal │   1401 │        -0.74 │       -1160.020 │       -116.0 │      8:33:00 │  158     0  1243  11.3 │
│           │        stop_loss │    933 │        -1.46 │       -1801.656 │      -180.17 │      3:03:00 │    0     0   933     0 │
│     TOTAL │                  │   2983 │        -0.26 │        -994.440 │       -99.44 │      6:31:00 │  807     0  2176  27.1 │
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
│ Total/Daily Avg Trades        │ 2983 / 2.21                    │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 5.56 USDT                      │
│ Absolute profit               │ -994.44 USDT                   │
│ Total profit %                │ -99.44%                        │
│ CAGR %                        │ -75.49%                        │
│ Sortino                       │ -5.92                          │
│ Sharpe                        │ -4.02                          │
│ Calmar                        │ -1.42                          │
│ SQN                           │ -5.19                          │
│ Profit factor                 │ 0.68                           │
│ Expectancy (Ratio)            │ -0.33 (-0.24)                  │
│ Avg. daily profit             │ -0.738 USDT                    │
│ Avg. stake amount             │ 122.16 USDT                    │
│ Total trade volume            │ 729270.639 USDT                │
│                               │                                │
│ Best Pair                     │ LTC/USDT -9.93%                │
│ Worst Pair                    │ XRP/USDT -28.59%               │
│ Best trade                    │ LTC/USDT 18.90%                │
│ Worst trade                   │ XRP/USDT -7.80%                │
│ Best day                      │ 34.054 USDT                    │
│ Worst day                     │ -42.7 USDT                     │
│ Days win/draw/lose            │ 231 / 212 / 508                │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 2d 00:10 / 0d 10:12 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 1d 21:40 / 0d 05:09 │
│ Max Consecutive Wins / Loss   │ 8 / 23                         │
│ Rejected Entry signals        │ 27507                          │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 5.56 USDT                      │
│ Max balance                   │ 984.223 USDT                   │
│ Max % of account underwater   │ 99.44%                         │
│ Absolute drawdown             │ 994.44 USDT (99.44%)           │
│ Drawdown duration             │ 949 days 16:15:00              │
│ Profit at drawdown start      │ -15.777 USDT                   │
│ Profit at drawdown end        │ -994.44 USDT                   │
│ Drawdown start                │ 2022-01-04 19:00:00            │
│ Drawdown end                  │ 2024-08-11 11:15:00            │
│ Market change                 │ 91.49%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃            Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │   2983 │        -0.26 │        -994.440 │       -99.44 │      6:31:00 │  807     0  2176  27.1 │ 994.44 USDT  99.44% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴─────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-19T16:05:05.365609",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 5362,
  "total_daily_avg_trades": "2983 / 2.21",
  "absolute_profit_usdt": -994.44,
  "total_profit_pct": -99.44,
  "cagr_pct": -75.49,
  "sortino": -5.92,
  "sharpe": -4.02,
  "calmar": -1.42,
  "sqn": -5.19,
  "max_consecutive_wins_loss": "8 / 23",
  "min_balance_usdt": 5.56,
  "max_balance_usdt": 984.223,
  "market_change_pct": 91.49,
  "win_draw_loss_winpct": "807 0 2176 27.1"
}
```
