# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 3671  
**Timestamp:** 2025-09-22 18:19:25

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 3671,
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
2025-09-22 16:16:06,707 - freqtrade - INFO - freqtrade 2025.8
2025-09-22 16:16:07,021 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-22 16:16:08,587 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-22 16:16:08,592 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-22 16:16:08,593 - freqtrade.loggers - INFO - Logfile configured
2025-09-22 16:16:08,593 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-22 16:16:08,594 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-22 16:16:08,595 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-22 16:16:08,595 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-22 16:16:08,596 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20251231 ...
2025-09-22 16:16:08,953 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-22 16:16:08,955 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-22 16:16:08,956 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-22 16:16:08,956 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-22 16:16:08,957 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-22 16:16:08,957 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20251231
2025-09-22 16:16:08,959 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-22 16:16:08,973 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-22 16:16:08,974 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-22 16:16:08,978 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-22 16:16:08,979 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-22 16:16:08,980 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-22 16:16:09,006 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-22 16:16:11,689 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-22 16:16:11,814 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-22 16:16:11,817 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-22 16:16:11,823 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-22 16:16:11,824 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-22 16:16:11,824 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-22 16:16:11,825 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-22 16:16:11,826 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-22 16:16:11,827 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-22 16:16:11,828 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-22 16:16:11,828 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-22 16:16:11,829 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-22 16:16:11,830 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-22 16:16:11,831 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-22 16:16:11,831 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-22 16:16:11,832 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-22 16:16:11,833 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-22 16:16:11,834 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-22 16:16:11,834 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-22 16:16:11,835 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-22 16:16:11,835 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-22 16:16:11,836 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-22 16:16:11,837 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-22 16:16:11,837 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-22 16:16:11,838 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-22 16:16:11,839 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-22 16:16:11,840 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-22 16:16:11,840 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-22 16:16:11,841 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-22 16:16:11,842 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-22 16:16:11,843 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-22 16:16:11,845 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-22 16:16:11,873 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-22 16:16:11,905 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-22 16:16:11,966 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 16:16:12,069 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 16:16:12,152 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 16:16:12,255 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-22 16:16:12,256 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 16:16:12,363 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 16:16:12,432 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-22 16:16:12,748 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 16:16:13,431 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 16:16:14,011 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 16:16:14,687 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-22 16:16:14,688 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 16:16:15,382 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 16:16:18,424 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-22 16:16:18,430 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-22 16:16:18,430 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-22 16:16:18,431 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.193
2025-09-22 16:16:18,432 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-22 16:16:18,432 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = True
2025-09-22 16:16:18,433 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-22 16:16:18,433 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 0
2025-09-22 16:16:18,433 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.652
2025-09-22 16:16:18,434 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.956
2025-09-22 16:16:18,435 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.001
2025-09-22 16:16:18,435 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-22 16:16:18,436 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-22 16:16:18,437 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-22 16:16:18,437 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 9
2025-09-22 16:16:18,438 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-22 16:16:18,439 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-22 16:16:18,440 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-22 16:16:18,440 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-22 16:16:18,440 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-22 16:16:18,445 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 16:16:18,465 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 16:16:32,531 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 16:16:32,545 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 16:16:46,626 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 16:16:46,643 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 16:17:02,172 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 16:17:02,186 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-22 16:17:02,187 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 16:17:18,344 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 16:17:18,360 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 16:17:33,903 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-22 16:19:24,527 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-22_16-19-24.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │    155 │         0.43 │         138.967 │         13.9 │     17:43:00 │   50     0   105  32.3 │
│ XRP/USDT │    100 │         0.37 │          85.787 │         8.58 │     13:41:00 │   32     0    68  32.0 │
│ BNB/USDT │    139 │         0.04 │           4.565 │         0.46 │     14:42:00 │   39     0   100  28.1 │
│ LTC/USDT │    105 │        -0.07 │          -6.148 │        -0.61 │     14:35:00 │   30     0    75  28.6 │
│ ETH/USDT │    116 │        -0.24 │         -58.324 │        -5.83 │     15:13:00 │   33     0    83  28.4 │
│    TOTAL │    615 │         0.12 │         164.847 │        16.48 │     15:23:00 │  184     0   431  29.9 │
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
│    hammer_rebond │     189 │         0.48 │         182.871 │        18.29 │     14:08:00 │   61     0   128  32.3 │
│ engulfing_rebond │     426 │        -0.04 │         -18.025 │         -1.8 │     15:55:00 │  123     0   303  28.9 │
│            TOTAL │     615 │         0.12 │         164.847 │        16.48 │     15:23:00 │  184     0   431  29.9 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │    41 │        10.49 │         923.926 │        92.39 │     23:59:00 │   41     0     0   100 │
│    exit_signal │   574 │        -0.62 │        -759.079 │       -75.91 │     14:46:00 │  143     0   431  24.9 │
│          TOTAL │   615 │         0.12 │         164.847 │        16.48 │     15:23:00 │  184     0   431  29.9 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                            MIXED TAG STATS                                                             
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │ take_profit_1R │     24 │        10.44 │         544.023 │         54.4 │ 1 day, 0:07:00 │   24     0     0   100 │
│    hammer_rebond │ take_profit_1R │     17 │        10.56 │         379.903 │        37.99 │       23:48:00 │   17     0     0   100 │
│    hammer_rebond │    exit_signal │    172 │        -0.52 │        -197.031 │        -19.7 │       13:11:00 │   44     0   128  25.6 │
│ engulfing_rebond │    exit_signal │    402 │        -0.66 │        -562.048 │        -56.2 │       15:26:00 │   99     0   303  24.6 │
│            TOTAL │                │    615 │         0.12 │         164.847 │        16.48 │       15:23:00 │  184     0   431  29.9 │
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
│ Total/Daily Avg Trades        │ 615 / 0.22                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1164.847 USDT                  │
│ Absolute profit               │ 164.847 USDT                   │
│ Total profit %                │ 16.48%                         │
│ CAGR %                        │ 2.00%                          │
│ Sortino                       │ 0.45                           │
│ Sharpe                        │ 0.16                           │
│ Calmar                        │ 0.75                           │
│ SQN                           │ 0.92                           │
│ Profit factor                 │ 1.13                           │
│ Expectancy (Ratio)            │ 0.27 (0.09)                    │
│ Avg. daily profit             │ 0.059 USDT                     │
│ Avg. stake amount             │ 210.21 USDT                    │
│ Total trade volume            │ 259241.316 USDT                │
│                               │                                │
│ Best Pair                     │ BTC/USDT 13.90%                │
│ Worst Pair                    │ ETH/USDT -5.83%                │
│ Best trade                    │ LTC/USDT 12.02%                │
│ Worst trade                   │ LTC/USDT -7.75%                │
│ Best day                      │ 39.782 USDT                    │
│ Worst day                     │ -18.457 USDT                   │
│ Days win/draw/lose            │ 147 / 2293 / 341               │
│ Min/Max/Avg. Duration Winners │ 0d 02:40 / 3d 02:00 / 1d 03:27 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 1d 16:00 / 0d 10:13 │
│ Max Consecutive Wins / Loss   │ 6 / 19                         │
│ Rejected Entry signals        │ 60                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 986.239 USDT                   │
│ Max balance                   │ 1254.609 USDT                  │
│ Max % of account underwater   │ 15.00%                         │
│ Absolute drawdown             │ 188.167 USDT (15.00%)          │
│ Drawdown duration             │ 1463 days 03:35:00             │
│ Profit at drawdown start      │ 254.609 USDT                   │
│ Profit at drawdown end        │ 66.442 USDT                    │
│ Drawdown start                │ 2020-07-09 00:25:00            │
│ Drawdown end                  │ 2024-07-11 04:00:00            │
│ Market change                 │ 2372.94%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    615 │         0.12 │         164.847 │        16.48 │     15:23:00 │  184     0   431  29.9 │ 188.167 USDT  15.00% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-22T18:19:25.860428",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 3671,
  "total_daily_avg_trades": "615 / 0.22",
  "absolute_profit_usdt": 164.847,
  "total_profit_pct": 16.48,
  "cagr_pct": 2.0,
  "sortino": 0.45,
  "sharpe": 0.16,
  "calmar": 0.75,
  "sqn": 0.92,
  "max_consecutive_wins_loss": "6 / 19",
  "min_balance_usdt": 986.239,
  "max_balance_usdt": 1254.609,
  "absolute_drawdown_pct": 15.0,
  "market_change_pct": 2372.94,
  "win_draw_loss_winpct": "184 0 431 29.9"
}
```
