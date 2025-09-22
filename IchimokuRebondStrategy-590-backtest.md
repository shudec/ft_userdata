# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 590  
**Timestamp:** 2025-09-22 18:08:56

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 590,
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
2025-09-22 16:06:12,149 - freqtrade - INFO - freqtrade 2025.8
2025-09-22 16:06:12,484 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-22 16:06:13,798 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-22 16:06:13,805 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-22 16:06:13,806 - freqtrade.loggers - INFO - Logfile configured
2025-09-22 16:06:13,806 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-22 16:06:13,807 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-22 16:06:13,807 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-22 16:06:13,808 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-22 16:06:13,808 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20251231 ...
2025-09-22 16:06:14,057 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-22 16:06:14,059 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-22 16:06:14,060 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-22 16:06:14,060 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-22 16:06:14,061 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-22 16:06:14,061 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20251231
2025-09-22 16:06:14,062 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-22 16:06:14,072 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-22 16:06:14,072 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-22 16:06:14,074 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-22 16:06:14,075 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-22 16:06:14,076 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-22 16:06:14,098 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-22 16:06:16,367 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-22 16:06:16,481 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-22 16:06:16,484 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-22 16:06:16,491 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-22 16:06:16,492 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-22 16:06:16,492 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-22 16:06:16,493 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-22 16:06:16,493 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-22 16:06:16,494 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.142, '480': 0.12, '1080': 0.08, '1440': 0}
2025-09-22 16:06:16,494 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-22 16:06:16,495 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-22 16:06:16,495 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-22 16:06:16,496 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-22 16:06:16,496 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-22 16:06:16,497 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-22 16:06:16,497 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-22 16:06:16,498 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-22 16:06:16,498 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-22 16:06:16,500 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-22 16:06:16,501 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-22 16:06:16,501 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-22 16:06:16,502 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-22 16:06:16,503 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-22 16:06:16,503 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-22 16:06:16,504 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-22 16:06:16,504 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-22 16:06:16,505 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-22 16:06:16,505 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-22 16:06:16,506 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-22 16:06:16,506 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-22 16:06:16,507 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-22 16:06:16,507 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-22 16:06:16,531 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-22 16:06:16,560 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-22 16:06:16,621 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 16:06:16,730 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 16:06:16,803 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 16:06:16,875 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-22 16:06:16,876 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 16:06:16,950 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-22 16:06:16,993 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-22 16:06:17,313 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 16:06:18,105 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 16:06:18,756 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 16:06:19,400 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-22 16:06:19,402 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 16:06:20,040 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-22 16:06:22,609 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-22 16:06:22,614 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-22 16:06:22,614 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-22 16:06:22,615 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.193
2025-09-22 16:06:22,615 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-22 16:06:22,616 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = True
2025-09-22 16:06:22,616 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-22 16:06:22,616 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 0
2025-09-22 16:06:22,617 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.652
2025-09-22 16:06:22,617 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.956
2025-09-22 16:06:22,618 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.001
2025-09-22 16:06:22,618 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-22 16:06:22,619 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-22 16:06:22,619 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-22 16:06:22,620 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 9
2025-09-22 16:06:22,620 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.99
2025-09-22 16:06:22,620 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-22 16:06:22,621 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-22 16:06:22,621 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-22 16:06:22,622 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-22 16:06:22,626 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 16:06:22,641 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 16:06:35,694 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 16:06:35,713 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 16:06:49,381 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 16:06:49,398 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 16:07:02,632 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 16:07:02,649 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-22 16:07:02,649 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 16:07:15,958 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-22 16:07:15,974 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-22 16:07:29,098 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-22 16:08:55,386 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-22_16-08-55.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │    101 │         0.56 │         121.197 │        12.12 │     12:07:00 │   35     0    66  34.7 │
│ BTC/USDT │    161 │         0.19 │          62.085 │         6.21 │     14:12:00 │   55     1   105  34.2 │
│ BNB/USDT │    140 │         0.08 │          12.930 │         1.29 │     12:39:00 │   41     1    98  29.3 │
│ LTC/USDT │    107 │         -0.1 │         -23.202 │        -2.32 │     12:39:00 │   31     2    74  29.0 │
│ ETH/USDT │    118 │        -0.35 │         -77.350 │        -7.73 │     13:26:00 │   37     0    81  31.4 │
│    TOTAL │    627 │         0.07 │          95.661 │         9.57 │     13:06:00 │  199     4   424  31.7 │
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
│    hammer_rebond │     192 │         0.25 │          89.387 │         8.94 │     12:07:00 │   63     1   128  32.8 │
│ engulfing_rebond │     435 │         -0.0 │           6.275 │         0.63 │     13:33:00 │  136     3   296  31.3 │
│            TOTAL │     627 │         0.07 │          95.661 │         9.57 │     13:06:00 │  199     4   424  31.7 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│            roi │   135 │         3.41 │         905.791 │        90.58 │     23:29:00 │  131     4     0   100 │
│ take_profit_1R │    17 │        10.56 │         368.786 │        36.88 │     10:43:00 │   17     0     0   100 │
│    exit_signal │   475 │        -1.25 │       -1178.916 │      -117.89 │     10:15:00 │   51     0   424  10.7 │
│          TOTAL │   627 │         0.07 │          95.661 │         9.57 │     13:06:00 │  199     4   424  31.7 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                           MIXED TAG STATS                                                            
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │            roi │    101 │         3.25 │         645.371 │        64.54 │     23:31:00 │   98     3     0   100 │
│    hammer_rebond │            roi │     34 │         3.89 │         260.420 │        26.04 │     23:21:00 │   33     1     0   100 │
│ engulfing_rebond │ take_profit_1R │     10 │        10.57 │         224.655 │        22.47 │     10:04:00 │   10     0     0   100 │
│    hammer_rebond │ take_profit_1R │      7 │        10.56 │         144.131 │        14.41 │     11:39:00 │    7     0     0   100 │
│    hammer_rebond │    exit_signal │    151 │        -1.05 │        -315.164 │       -31.52 │      9:36:00 │   23     0   128  15.2 │
│ engulfing_rebond │    exit_signal │    324 │        -1.34 │        -863.752 │       -86.38 │     10:33:00 │   28     0   296   8.6 │
│            TOTAL │                │    627 │         0.07 │          95.661 │         9.57 │     13:06:00 │  199     4   424  31.7 │
└──────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2018-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 627 / 0.22                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1095.661 USDT                  │
│ Absolute profit               │ 95.661 USDT                    │
│ Total profit %                │ 9.57%                          │
│ CAGR %                        │ 1.19%                          │
│ Sortino                       │ 0.28                           │
│ Sharpe                        │ 0.11                           │
│ Calmar                        │ 0.38                           │
│ SQN                           │ 0.62                           │
│ Profit factor                 │ 1.08                           │
│ Expectancy (Ratio)            │ 0.15 (0.05)                    │
│ Avg. daily profit             │ 0.034 USDT                     │
│ Avg. stake amount             │ 198.067 USDT                   │
│ Total trade volume            │ 248969.231 USDT                │
│                               │                                │
│ Best Pair                     │ XRP/USDT 12.12%                │
│ Worst Pair                    │ ETH/USDT -7.73%                │
│ Best trade                    │ XRP/USDT 11.99%                │
│ Worst trade                   │ LTC/USDT -7.75%                │
│ Best day                      │ 40.07 USDT                     │
│ Worst day                     │ -17.136 USDT                   │
│ Days win/draw/lose            │ 157 / 2293 / 331               │
│ Min/Max/Avg. Duration Winners │ 0d 02:30 / 1d 00:00 / 0d 20:31 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 1d 01:00 / 0d 09:31 │
│ Max Consecutive Wins / Loss   │ 6 / 19                         │
│ Rejected Entry signals        │ 40                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 986.239 USDT                   │
│ Max balance                   │ 1194.223 USDT                  │
│ Max % of account underwater   │ 17.07%                         │
│ Absolute drawdown             │ 203.809 USDT (17.07%)          │
│ Drawdown duration             │ 1533 days 11:45:00             │
│ Profit at drawdown start      │ 194.223 USDT                   │
│ Profit at drawdown end        │ -9.585 USDT                    │
│ Drawdown start                │ 2020-04-29 16:15:00            │
│ Drawdown end                  │ 2024-07-11 04:00:00            │
│ Market change                 │ 2372.94%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    627 │         0.07 │          95.661 │         9.57 │     13:06:00 │  199     4   424  31.7 │ 203.809 USDT  17.07% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-22T18:08:56.783275",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 590,
  "total_daily_avg_trades": "627 / 0.22",
  "absolute_profit_usdt": 95.661,
  "total_profit_pct": 9.57,
  "cagr_pct": 1.19,
  "sortino": 0.28,
  "sharpe": 0.11,
  "calmar": 0.38,
  "sqn": 0.62,
  "max_consecutive_wins_loss": "6 / 19",
  "min_balance_usdt": 986.239,
  "max_balance_usdt": 1194.223,
  "absolute_drawdown_pct": 17.07,
  "market_change_pct": 2372.94,
  "win_draw_loss_winpct": "199 4 424 31.7"
}
```
