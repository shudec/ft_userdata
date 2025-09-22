# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 8027  
**Timestamp:** 2025-09-22 17:16:12

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 8027,
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
2025-09-22 15:12:37,196 - freqtrade - INFO - freqtrade 2025.8
2025-09-22 15:12:37,587 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-22 15:12:39,201 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-22 15:12:39,208 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-22 15:12:39,208 - freqtrade.loggers - INFO - Logfile configured
2025-09-22 15:12:39,208 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-22 15:12:39,209 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-22 15:12:39,209 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-22 15:12:39,210 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-22 15:12:39,210 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20251231 ...
2025-09-22 15:12:39,654 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-22 15:12:39,656 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-22 15:12:39,657 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-22 15:12:39,658 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-22 15:12:39,658 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-22 15:12:39,659 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20251231
2025-09-22 15:12:39,660 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-22 15:12:39,674 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-22 15:12:39,675 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-22 15:12:39,678 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-22 15:12:39,679 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-22 15:12:39,679 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-22 15:12:39,704 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-22 15:12:41,960 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-22 15:12:42,043 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-22 15:12:42,045 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-22 15:12:42,048 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-22 15:12:42,048 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-22 15:12:42,049 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-22 15:12:42,049 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-22 15:12:42,049 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-22 15:12:42,050 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-22 15:12:42,050 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-22 15:12:42,050 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-22 15:12:42,051 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-22 15:12:42,051 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-22 15:12:42,052 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-22 15:12:42,052 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-22 15:12:42,052 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-22 15:12:42,053 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-22 15:12:42,053 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-22 15:12:42,054 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-22 15:12:42,054 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-22 15:12:42,054 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-22 15:12:42,055 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-22 15:12:42,055 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-22 15:12:42,056 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-22 15:12:42,056 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-22 15:12:42,056 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-22 15:12:42,057 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-22 15:12:42,057 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-22 15:12:42,058 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-22 15:12:42,058 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-22 15:12:42,059 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-22 15:12:42,059 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-22 15:12:42,077 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-22 15:12:42,099 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-22 15:12:42,147 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 15:12:42,224 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 15:12:42,285 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 15:12:42,350 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-22 15:12:42,350 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 15:12:42,422 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 15:12:42,466 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-22 15:12:42,755 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 15:12:43,556 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 15:12:44,216 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 15:12:44,824 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-22 15:12:44,825 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 15:12:45,351 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 15:12:47,872 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-22 15:12:47,877 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-22 15:12:47,878 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-22 15:12:47,879 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.193
2025-09-22 15:12:47,880 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-22 15:12:47,881 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-22 15:12:47,881 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-22 15:12:47,882 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 0
2025-09-22 15:12:47,883 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.652
2025-09-22 15:12:47,883 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.956
2025-09-22 15:12:47,884 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.001
2025-09-22 15:12:47,884 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-22 15:12:47,885 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-22 15:12:47,886 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-22 15:12:47,886 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 9
2025-09-22 15:12:47,887 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.99
2025-09-22 15:12:47,887 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-22 15:12:47,888 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-22 15:12:47,888 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-22 15:12:47,888 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-22 15:12:47,892 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 15:12:47,914 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 15:13:03,382 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 15:13:03,396 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 15:13:19,065 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 15:13:19,079 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 15:13:32,686 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 15:13:32,708 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-22 15:13:32,708 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 15:13:46,111 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 15:13:46,127 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 15:13:59,983 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-22 15:16:11,094 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-22_15-16-11.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │    151 │         0.13 │          52.863 │         5.29 │     11:44:00 │   39     0   112  25.8 │
│ BTC/USDT │    225 │         0.09 │          52.062 │         5.21 │     15:49:00 │   63     0   162  28.0 │
│ ETH/USDT │    183 │         0.01 │          -2.416 │        -0.24 │     14:48:00 │   54     0   129  29.5 │
│ LTC/USDT │    160 │        -0.06 │          -9.370 │        -0.94 │     13:31:00 │   49     0   111  30.6 │
│ BNB/USDT │    186 │        -0.06 │         -38.098 │        -3.81 │     14:11:00 │   47     0   139  25.3 │
│    TOTAL │    905 │         0.02 │          55.041 │          5.5 │     14:11:00 │  252     0   653  27.8 │
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
│    hammer_rebond │     501 │         0.14 │         134.024 │         13.4 │     13:03:00 │  134     0   367  26.7 │
│ engulfing_rebond │     404 │        -0.12 │         -78.983 │         -7.9 │     15:35:00 │  118     0   286  29.2 │
│            TOTAL │     905 │         0.02 │          55.041 │          5.5 │     14:11:00 │  252     0   653  27.8 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │    52 │        10.41 │        1132.752 │       113.28 │ 1 day, 0:21:00 │   52     0     0   100 │
│    exit_signal │   853 │        -0.61 │       -1077.711 │      -107.77 │       13:34:00 │  200     0   653  23.4 │
│          TOTAL │   905 │         0.02 │          55.041 │          5.5 │       14:11:00 │  252     0   653  27.8 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                            MIXED TAG STATS                                                             
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│    hammer_rebond │ take_profit_1R │     31 │        10.42 │         673.537 │        67.35 │ 1 day, 0:17:00 │   31     0     0   100 │
│ engulfing_rebond │ take_profit_1R │     21 │         10.4 │         459.215 │        45.92 │ 1 day, 0:27:00 │   21     0     0   100 │
│ engulfing_rebond │    exit_signal │    383 │         -0.7 │        -538.198 │       -53.82 │       15:06:00 │   97     0   286  25.3 │
│    hammer_rebond │    exit_signal │    470 │        -0.54 │        -539.513 │       -53.95 │       12:19:00 │  103     0   367  21.9 │
│            TOTAL │                │    905 │         0.02 │          55.041 │          5.5 │       14:11:00 │  252     0   653  27.8 │
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
│ Total/Daily Avg Trades        │ 905 / 0.32                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1055.041 USDT                  │
│ Absolute profit               │ 55.041 USDT                    │
│ Total profit %                │ 5.50%                          │
│ CAGR %                        │ 0.70%                          │
│ Sortino                       │ 0.16                           │
│ Sharpe                        │ 0.06                           │
│ Calmar                        │ 0.16                           │
│ SQN                           │ 0.28                           │
│ Profit factor                 │ 1.03                           │
│ Expectancy (Ratio)            │ 0.06 (0.02)                    │
│ Avg. daily profit             │ 0.02 USDT                      │
│ Avg. stake amount             │ 204.008 USDT                   │
│ Total trade volume            │ 370049.349 USDT                │
│                               │                                │
│ Best Pair                     │ XRP/USDT 5.29%                 │
│ Worst Pair                    │ BNB/USDT -3.81%                │
│ Best trade                    │ ETH/USDT 11.62%                │
│ Worst trade                   │ LTC/USDT -7.75%                │
│ Best day                      │ 62.078 USDT                    │
│ Worst day                     │ -20.326 USDT                   │
│ Days win/draw/lose            │ 194 / 2116 / 479               │
│ Min/Max/Avg. Duration Winners │ 0d 00:15 / 3d 05:35 / 1d 02:44 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 1d 22:00 / 0d 09:21 │
│ Max Consecutive Wins / Loss   │ 7 / 29                         │
│ Rejected Entry signals        │ 180                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 970.845 USDT                   │
│ Max balance                   │ 1301.724 USDT                  │
│ Max % of account underwater   │ 23.93%                         │
│ Absolute drawdown             │ 311.523 USDT (23.93%)          │
│ Drawdown duration             │ 2204 days 09:45:00             │
│ Profit at drawdown start      │ 301.724 USDT                   │
│ Profit at drawdown end        │ -9.799 USDT                    │
│ Drawdown start                │ 2019-06-26 05:15:00            │
│ Drawdown end                  │ 2025-07-08 15:00:00            │
│ Market change                 │ 2372.94%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    905 │         0.02 │          55.041 │          5.5 │     14:11:00 │  252     0   653  27.8 │ 311.523 USDT  23.93% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-22T17:16:12.398512",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 8027,
  "total_daily_avg_trades": "905 / 0.32",
  "absolute_profit_usdt": 55.041,
  "total_profit_pct": 5.5,
  "cagr_pct": 0.7,
  "sortino": 0.16,
  "sharpe": 0.06,
  "calmar": 0.16,
  "sqn": 0.28,
  "max_consecutive_wins_loss": "7 / 29",
  "min_balance_usdt": 970.845,
  "max_balance_usdt": 1301.724,
  "market_change_pct": 2372.94,
  "win_draw_loss_winpct": "252 0 653 27.8"
}
```
