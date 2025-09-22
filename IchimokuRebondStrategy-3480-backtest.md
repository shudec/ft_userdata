# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 3480  
**Timestamp:** 2025-09-22 18:01:02

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 3480,
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
2025-09-22 15:58:09,686 - freqtrade - INFO - freqtrade 2025.8
2025-09-22 15:58:09,995 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-22 15:58:11,598 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-22 15:58:11,606 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-22 15:58:11,606 - freqtrade.loggers - INFO - Logfile configured
2025-09-22 15:58:11,606 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-22 15:58:11,607 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-22 15:58:11,607 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-22 15:58:11,608 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-22 15:58:11,609 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20251231 ...
2025-09-22 15:58:11,904 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-22 15:58:11,907 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-22 15:58:11,907 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-22 15:58:11,908 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-22 15:58:11,908 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-22 15:58:11,908 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20251231
2025-09-22 15:58:11,910 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-22 15:58:11,921 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-22 15:58:11,922 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-22 15:58:11,925 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-22 15:58:11,925 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-22 15:58:11,926 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-22 15:58:11,949 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-22 15:58:15,776 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-22 15:58:15,856 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-22 15:58:15,858 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-22 15:58:15,862 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-22 15:58:15,862 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-22 15:58:15,863 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-22 15:58:15,863 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-22 15:58:15,863 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-22 15:58:15,864 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.142, '452': 0.118, '1139': 0.09, '2547': 0}
2025-09-22 15:58:15,864 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-22 15:58:15,865 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-22 15:58:15,865 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-22 15:58:15,865 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-22 15:58:15,866 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-22 15:58:15,866 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-22 15:58:15,866 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-22 15:58:15,867 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-22 15:58:15,867 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-22 15:58:15,867 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-22 15:58:15,867 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-22 15:58:15,868 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-22 15:58:15,868 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-22 15:58:15,868 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-22 15:58:15,868 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-22 15:58:15,869 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-22 15:58:15,869 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-22 15:58:15,870 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-22 15:58:15,870 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-22 15:58:15,871 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-22 15:58:15,871 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-22 15:58:15,872 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-22 15:58:15,873 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-22 15:58:15,889 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-22 15:58:15,913 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-22 15:58:15,976 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 15:58:16,080 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 15:58:16,163 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 15:58:16,250 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-22 15:58:16,251 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 15:58:16,331 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 15:58:16,375 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-22 15:58:16,697 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 15:58:17,536 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 15:58:18,135 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 15:58:18,771 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-22 15:58:18,772 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 15:58:19,432 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 15:58:22,075 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-22 15:58:22,081 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-22 15:58:22,081 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-22 15:58:22,082 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.193
2025-09-22 15:58:22,083 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-22 15:58:22,084 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = True
2025-09-22 15:58:22,084 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-22 15:58:22,085 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 0
2025-09-22 15:58:22,086 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.652
2025-09-22 15:58:22,087 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.956
2025-09-22 15:58:22,087 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.001
2025-09-22 15:58:22,088 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-22 15:58:22,088 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-22 15:58:22,089 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-22 15:58:22,090 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 9
2025-09-22 15:58:22,090 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.99
2025-09-22 15:58:22,091 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-22 15:58:22,091 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-22 15:58:22,092 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-22 15:58:22,092 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-22 15:58:22,095 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 15:58:22,114 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 15:58:34,606 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 15:58:34,627 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 15:58:47,621 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 15:58:47,664 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 15:59:00,651 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 15:59:00,670 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-22 15:59:00,671 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 15:59:13,275 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 15:59:13,295 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 15:59:26,283 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-22 16:01:00,488 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-22_16-01-00.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │    157 │         0.38 │         127.523 │        12.75 │     16:40:00 │   50     0   107  31.8 │
│ XRP/USDT │    100 │         0.46 │          98.220 │         9.82 │     13:24:00 │   32     0    68  32.0 │
│ BNB/USDT │    139 │         0.03 │           1.293 │         0.13 │     14:27:00 │   39     0   100  28.1 │
│ LTC/USDT │    105 │        -0.11 │         -20.827 │        -2.08 │     14:22:00 │   30     0    75  28.6 │
│ ETH/USDT │    116 │        -0.26 │         -65.510 │        -6.55 │     14:49:00 │   33     0    83  28.4 │
│    TOTAL │    617 │         0.11 │         140.699 │        14.07 │     14:54:00 │  184     0   433  29.8 │
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
│    hammer_rebond │     189 │         0.39 │         149.107 │        14.91 │     13:45:00 │   61     0   128  32.3 │
│ engulfing_rebond │     428 │        -0.01 │          -8.408 │        -0.84 │     15:24:00 │  123     0   305  28.7 │
│            TOTAL │     617 │         0.11 │         140.699 │        14.07 │     14:54:00 │  184     0   433  29.8 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│            roi │    48 │         7.38 │         739.668 │        73.97 │ 1 day, 9:17:00 │   48     0     0   100 │
│ take_profit_1R │    16 │         10.6 │         366.259 │        36.63 │       11:14:00 │   16     0     0   100 │
│    exit_signal │   553 │        -0.83 │        -965.228 │       -96.52 │       13:24:00 │  120     0   433  21.7 │
│          TOTAL │   617 │         0.11 │         140.699 │        14.07 │       14:54:00 │  184     0   433  29.8 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                            MIXED TAG STATS                                                             
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │            roi │     34 │         7.09 │         497.551 │        49.76 │ 1 day, 9:42:00 │   34     0     0   100 │
│    hammer_rebond │            roi │     14 │          8.1 │         242.117 │        24.21 │ 1 day, 8:15:00 │   14     0     0   100 │
│ engulfing_rebond │ take_profit_1R │      9 │        10.63 │         216.035 │         21.6 │       10:55:00 │    9     0     0   100 │
│    hammer_rebond │ take_profit_1R │      7 │        10.56 │         150.224 │        15.02 │       11:39:00 │    7     0     0   100 │
│    hammer_rebond │    exit_signal │    168 │        -0.68 │        -243.234 │       -24.32 │       12:18:00 │   40     0   128  23.8 │
│ engulfing_rebond │    exit_signal │    385 │        -0.89 │        -721.994 │        -72.2 │       13:53:00 │   80     0   305  20.8 │
│            TOTAL │                │    617 │         0.11 │         140.699 │        14.07 │       14:54:00 │  184     0   433  29.8 │
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
│ Total/Daily Avg Trades        │ 617 / 0.22                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1140.699 USDT                  │
│ Absolute profit               │ 140.699 USDT                   │
│ Total profit %                │ 14.07%                         │
│ CAGR %                        │ 1.73%                          │
│ Sortino                       │ 0.38                           │
│ Sharpe                        │ 0.14                           │
│ Calmar                        │ 0.57                           │
│ SQN                           │ 0.81                           │
│ Profit factor                 │ 1.11                           │
│ Expectancy (Ratio)            │ 0.23 (0.07)                    │
│ Avg. daily profit             │ 0.05 USDT                      │
│ Avg. stake amount             │ 209.735 USDT                   │
│ Total trade volume            │ 259472.432 USDT                │
│                               │                                │
│ Best Pair                     │ BTC/USDT 12.75%                │
│ Worst Pair                    │ ETH/USDT -6.55%                │
│ Best trade                    │ XRP/USDT 11.79%                │
│ Worst trade                   │ LTC/USDT -7.75%                │
│ Best day                      │ 34.433 USDT                    │
│ Worst day                     │ -18.243 USDT                   │
│ Days win/draw/lose            │ 146 / 2296 / 339               │
│ Min/Max/Avg. Duration Winners │ 0d 02:40 / 1d 18:30 / 1d 01:57 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 1d 16:00 / 0d 10:12 │
│ Max Consecutive Wins / Loss   │ 6 / 19                         │
│ Rejected Entry signals        │ 60                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 986.239 USDT                   │
│ Max balance                   │ 1267.18 USDT                   │
│ Max % of account underwater   │ 16.70%                         │
│ Absolute drawdown             │ 211.575 USDT (16.70%)          │
│ Drawdown duration             │ 1463 days 18:25:00             │
│ Profit at drawdown start      │ 267.18 USDT                    │
│ Profit at drawdown end        │ 55.605 USDT                    │
│ Drawdown start                │ 2020-07-08 09:35:00            │
│ Drawdown end                  │ 2024-07-11 04:00:00            │
│ Market change                 │ 2372.94%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    617 │         0.11 │         140.699 │        14.07 │     14:54:00 │  184     0   433  29.8 │ 211.575 USDT  16.70% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-22T18:01:02.230777",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 3480,
  "total_daily_avg_trades": "617 / 0.22",
  "absolute_profit_usdt": 140.699,
  "total_profit_pct": 14.07,
  "cagr_pct": 1.73,
  "sortino": 0.38,
  "sharpe": 0.14,
  "calmar": 0.57,
  "sqn": 0.81,
  "max_consecutive_wins_loss": "6 / 19",
  "min_balance_usdt": 986.239,
  "max_balance_usdt": 1267.18,
  "market_change_pct": 2372.94,
  "win_draw_loss_winpct": "184 0 433 29.8"
}
```
