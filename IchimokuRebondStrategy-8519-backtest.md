# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 8519  
**Timestamp:** 2025-09-22 17:22:38

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 8519,
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
2025-09-22 15:19:42,345 - freqtrade - INFO - freqtrade 2025.8
2025-09-22 15:19:42,720 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-22 15:19:44,511 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-22 15:19:44,518 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-22 15:19:44,518 - freqtrade.loggers - INFO - Logfile configured
2025-09-22 15:19:44,519 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-22 15:19:44,520 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-22 15:19:44,521 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-22 15:19:44,521 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-22 15:19:44,522 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20251231 ...
2025-09-22 15:19:44,849 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-22 15:19:44,852 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-22 15:19:44,853 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-22 15:19:44,853 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-22 15:19:44,854 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-22 15:19:44,854 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20251231
2025-09-22 15:19:44,855 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-22 15:19:44,870 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-22 15:19:44,871 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-22 15:19:44,875 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-22 15:19:44,876 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-22 15:19:44,877 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-22 15:19:44,907 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-22 15:19:47,165 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-22 15:19:47,256 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-22 15:19:47,259 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-22 15:19:47,263 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-22 15:19:47,263 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-22 15:19:47,264 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-22 15:19:47,264 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-22 15:19:47,264 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-22 15:19:47,265 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-22 15:19:47,265 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-22 15:19:47,266 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-22 15:19:47,266 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-22 15:19:47,266 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-22 15:19:47,267 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-22 15:19:47,267 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-22 15:19:47,268 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-22 15:19:47,268 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-22 15:19:47,269 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-22 15:19:47,269 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-22 15:19:47,270 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-22 15:19:47,270 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-22 15:19:47,271 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-22 15:19:47,271 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-22 15:19:47,272 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-22 15:19:47,272 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-22 15:19:47,272 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-22 15:19:47,273 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-22 15:19:47,273 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-22 15:19:47,273 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-22 15:19:47,274 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-22 15:19:47,274 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-22 15:19:47,275 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-22 15:19:47,293 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-22 15:19:47,319 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-22 15:19:47,376 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 15:19:47,461 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 15:19:47,531 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 15:19:47,598 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-22 15:19:47,599 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 15:19:47,664 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 15:19:47,701 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-22 15:19:47,949 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 15:19:48,659 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 15:19:49,234 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 15:19:49,843 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-22 15:19:49,844 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 15:19:50,391 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 15:19:53,357 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-22 15:19:53,362 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-22 15:19:53,363 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-22 15:19:53,364 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.193
2025-09-22 15:19:53,364 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-22 15:19:53,365 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-22 15:19:53,366 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-22 15:19:53,367 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 0
2025-09-22 15:19:53,368 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.652
2025-09-22 15:19:53,369 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.956
2025-09-22 15:19:53,370 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.001
2025-09-22 15:19:53,371 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-22 15:19:53,372 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-22 15:19:53,373 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-22 15:19:53,373 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 9
2025-09-22 15:19:53,374 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.99
2025-09-22 15:19:53,375 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-22 15:19:53,375 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-22 15:19:53,376 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-22 15:19:53,376 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-22 15:19:53,381 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 15:19:53,403 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 15:20:08,656 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 15:20:08,670 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 15:20:22,680 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 15:20:22,697 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 15:20:35,825 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 15:20:35,844 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-22 15:20:35,845 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 15:20:48,562 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 15:20:48,579 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 15:21:01,527 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-22 15:22:37,506 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-22_15-22-37.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │    104 │          0.4 │          89.656 │         8.97 │     12:51:00 │   32     0    72  30.8 │
│ BTC/USDT │    167 │         0.15 │          45.656 │         4.57 │     16:27:00 │   48     0   119  28.7 │
│ LTC/USDT │    116 │         0.03 │           8.288 │         0.83 │     14:32:00 │   36     0    80  31.0 │
│ ETH/USDT │    128 │        -0.08 │         -18.659 │        -1.87 │     15:04:00 │   38     0    90  29.7 │
│ BNB/USDT │    142 │        -0.07 │         -32.851 │        -3.29 │     14:41:00 │   39     0   103  27.5 │
│    TOTAL │    657 │         0.08 │          92.089 │         9.21 │     14:53:00 │  193     0   464  29.4 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                   ENTER TAG STATS                                                    
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│    hammer_rebond │     226 │         0.38 │         157.088 │        15.71 │     13:41:00 │   69     0   157  30.5 │
│ engulfing_rebond │     431 │        -0.08 │         -64.999 │         -6.5 │     15:31:00 │  124     0   307  28.8 │
│            TOTAL │     657 │         0.08 │          92.089 │         9.21 │     14:53:00 │  193     0   464  29.4 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │    43 │        10.46 │         928.256 │        92.83 │ 1 day, 0:10:00 │   43     0     0   100 │
│    exit_signal │   614 │        -0.65 │        -836.167 │       -83.62 │       14:14:00 │  150     0   464  24.4 │
│          TOTAL │   657 │         0.08 │          92.089 │         9.21 │       14:53:00 │  193     0   464  29.4 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                            MIXED TAG STATS                                                             
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │ take_profit_1R │     24 │         10.4 │         520.351 │        52.04 │ 1 day, 0:35:00 │   24     0     0   100 │
│    hammer_rebond │ take_profit_1R │     19 │        10.53 │         407.906 │        40.79 │       23:38:00 │   19     0     0   100 │
│    hammer_rebond │    exit_signal │    207 │        -0.56 │        -250.818 │       -25.08 │       12:46:00 │   50     0   157  24.2 │
│ engulfing_rebond │    exit_signal │    407 │         -0.7 │        -585.349 │       -58.53 │       14:59:00 │  100     0   307  24.6 │
│            TOTAL │                │    657 │         0.08 │          92.089 │         9.21 │       14:53:00 │  193     0   464  29.4 │
└──────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2018-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 657 / 0.23                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1092.089 USDT                  │
│ Absolute profit               │ 92.089 USDT                    │
│ Total profit %                │ 9.21%                          │
│ CAGR %                        │ 1.15%                          │
│ Sortino                       │ 0.26                           │
│ Sharpe                        │ 0.09                           │
│ Calmar                        │ 0.34                           │
│ SQN                           │ 0.52                           │
│ Profit factor                 │ 1.07                           │
│ Expectancy (Ratio)            │ 0.14 (0.05)                    │
│ Avg. daily profit             │ 0.033 USDT                     │
│ Avg. stake amount             │ 205.804 USDT                   │
│ Total trade volume            │ 271059.993 USDT                │
│                               │                                │
│ Best Pair                     │ XRP/USDT 8.97%                 │
│ Worst Pair                    │ BNB/USDT -3.29%                │
│ Best trade                    │ LTC/USDT 12.02%                │
│ Worst trade                   │ LTC/USDT -7.75%                │
│ Best day                      │ 58.141 USDT                    │
│ Worst day                     │ -17.802 USDT                   │
│ Days win/draw/lose            │ 152 / 2266 / 363               │
│ Min/Max/Avg. Duration Winners │ 0d 02:40 / 3d 02:00 / 1d 02:50 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 1d 21:00 / 0d 09:55 │
│ Max Consecutive Wins / Loss   │ 7 / 22                         │
│ Rejected Entry signals        │ 60                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 986.017 USDT                   │
│ Max balance                   │ 1247.074 USDT                  │
│ Max % of account underwater   │ 18.28%                         │
│ Absolute drawdown             │ 227.915 USDT (18.28%)          │
│ Drawdown duration             │ 1533 days 11:15:00             │
│ Profit at drawdown start      │ 247.074 USDT                   │
│ Profit at drawdown end        │ 19.16 USDT                     │
│ Drawdown start                │ 2020-04-29 16:45:00            │
│ Drawdown end                  │ 2024-07-11 04:00:00            │
│ Market change                 │ 2372.94%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    657 │         0.08 │          92.089 │         9.21 │     14:53:00 │  193     0   464  29.4 │ 227.915 USDT  18.28% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-22T17:22:38.848208",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 8519,
  "total_daily_avg_trades": "657 / 0.23",
  "absolute_profit_usdt": 92.089,
  "total_profit_pct": 9.21,
  "cagr_pct": 1.15,
  "sortino": 0.26,
  "sharpe": 0.09,
  "calmar": 0.34,
  "sqn": 0.52,
  "max_consecutive_wins_loss": "7 / 22",
  "min_balance_usdt": 986.017,
  "max_balance_usdt": 1247.074,
  "market_change_pct": 2372.94,
  "win_draw_loss_winpct": "193 0 464 29.4"
}
```
