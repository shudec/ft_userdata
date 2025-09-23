# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 6996  
**Timestamp:** 2025-09-23 14:34:59

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 6996,
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
2025-09-23 12:27:45,792 - freqtrade - INFO - freqtrade 2025.8
2025-09-23 12:27:47,117 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-23 12:27:52,113 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-23 12:27:52,126 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-23 12:27:52,128 - freqtrade.loggers - INFO - Logfile configured
2025-09-23 12:27:52,129 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-23 12:27:52,130 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-23 12:27:52,130 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-23 12:27:52,131 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-23 12:27:52,132 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20251231 ...
2025-09-23 12:27:52,804 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-23 12:27:52,810 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-23 12:27:52,811 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-23 12:27:52,812 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-23 12:27:52,812 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-23 12:27:52,813 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20251231
2025-09-23 12:27:52,815 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-23 12:27:52,842 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-23 12:27:52,847 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 12:27:52,856 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-23 12:27:52,859 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-23 12:27:52,862 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-23 12:27:52,929 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-23 12:27:57,309 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-23 12:27:57,585 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-23 12:27:57,592 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-23 12:27:57,601 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-23 12:27:57,603 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-23 12:27:57,606 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-23 12:27:57,611 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-23 12:27:57,613 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-23 12:27:57,614 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-23 12:27:57,615 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-23 12:27:57,616 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-23 12:27:57,617 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-23 12:27:57,618 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-23 12:27:57,618 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-23 12:27:57,619 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-23 12:27:57,620 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-23 12:27:57,622 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-23 12:27:57,624 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-23 12:27:57,629 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-23 12:27:57,630 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-23 12:27:57,632 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-23 12:27:57,633 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-23 12:27:57,634 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-23 12:27:57,635 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-23 12:27:57,637 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-23 12:27:57,638 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-23 12:27:57,639 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-23 12:27:57,640 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-23 12:27:57,642 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-23 12:27:57,644 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-23 12:27:57,646 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-23 12:27:57,648 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 12:27:57,750 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-23 12:27:57,853 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-23 12:27:58,034 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:27:58,328 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:27:58,535 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:27:58,735 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-23 12:27:58,738 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:27:59,065 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:27:59,261 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 12:28:00,013 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:28:02,139 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:28:03,880 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:28:05,685 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-23 12:28:05,688 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:28:07,237 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:28:13,703 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-23 12:28:13,714 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-23 12:28:13,715 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-23 12:28:13,716 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.1
2025-09-23 12:28:13,717 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-23 12:28:13,719 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-23 12:28:13,722 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-23 12:28:13,724 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-09-23 12:28:13,727 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.8
2025-09-23 12:28:13,729 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.25
2025-09-23 12:28:13,731 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.008
2025-09-23 12:28:13,733 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-23 12:28:13,736 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-23 12:28:13,738 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-23 12:28:13,742 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1
2025-09-23 12:28:13,745 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-23 12:28:13,748 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 3
2025-09-23 12:28:13,749 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 1.0
2025-09-23 12:28:13,753 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-23 12:28:13,755 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-23 12:28:13,758 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-23 12:28:13,760 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-23 12:28:13,762 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-23 12:32:57,074 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 12:34:54,892 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-23_12-34-54.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │     34 │         0.72 │         125.722 │        12.57 │     15:48:00 │   11     0    23  32.4 │
│ ETH/USDT │     33 │        -0.22 │         -50.939 │        -5.09 │     10:54:00 │   11     0    22  33.3 │
│ LTC/USDT │     42 │        -0.08 │         -58.724 │        -5.87 │     15:17:00 │   13     0    29  31.0 │
│ BTC/USDT │     46 │        -0.07 │         -77.480 │        -7.75 │     18:22:00 │   14     0    32  30.4 │
│ BNB/USDT │     47 │        -0.25 │        -202.057 │       -20.21 │     13:32:00 │   10     0    37  21.3 │
│    TOTAL │    202 │         -0.0 │        -263.477 │       -26.35 │     14:57:00 │   59     0   143  29.2 │
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
│ engulfing_rebond │     171 │         0.07 │        -119.680 │       -11.97 │     16:21:00 │   52     0   119  30.4 │
│    hammer_rebond │      31 │        -0.42 │        -143.797 │       -14.38 │      7:12:00 │    7     0    24  22.6 │
│            TOTAL │     202 │         -0.0 │        -263.477 │       -26.35 │     14:57:00 │   59     0   143  29.2 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │    59 │         4.36 │        1889.334 │       188.93 │ 1 day, 3:16:00 │   59     0     0   100 │
│      stop_loss │   143 │         -1.8 │       -2152.811 │      -215.28 │        9:52:00 │    0     0   143     0 │
│          TOTAL │   202 │         -0.0 │        -263.477 │       -26.35 │       14:57:00 │   59     0   143  29.2 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                            MIXED TAG STATS                                                             
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │ take_profit_2R │     52 │         4.34 │        1631.770 │       163.18 │ 1 day, 5:58:00 │   52     0     0   100 │
│    hammer_rebond │ take_profit_2R │      7 │          4.5 │         257.564 │        25.76 │        7:12:00 │    7     0     0   100 │
│    hammer_rebond │      stop_loss │     24 │        -1.85 │        -401.361 │       -40.14 │        7:12:00 │    0     0    24     0 │
│ engulfing_rebond │      stop_loss │    119 │        -1.79 │       -1751.450 │      -175.15 │       10:24:00 │    0     0   119     0 │
│            TOTAL │                │    202 │         -0.0 │        -263.477 │       -26.35 │       14:57:00 │   59     0   143  29.2 │
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
│ Total/Daily Avg Trades        │ 202 / 0.07                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 736.523 USDT                   │
│ Absolute profit               │ -263.477 USDT                  │
│ Total profit %                │ -26.35%                        │
│ CAGR %                        │ -3.90%                         │
│ Sortino                       │ -0.29                          │
│ Sharpe                        │ -0.08                          │
│ Calmar                        │ -0.44                          │
│ SQN                           │ -0.80                          │
│ Profit factor                 │ 0.88                           │
│ Expectancy (Ratio)            │ -1.30 (-0.09)                  │
│ Avg. daily profit             │ -0.094 USDT                    │
│ Avg. stake amount             │ 879.038 USDT                   │
│ Total trade volume            │ 355578.222 USDT                │
│                               │                                │
│ Best Pair                     │ XRP/USDT 12.57%                │
│ Worst Pair                    │ BNB/USDT -20.21%               │
│ Best trade                    │ BNB/USDT 13.11%                │
│ Worst trade                   │ LTC/USDT -6.89%                │
│ Best day                      │ 74.845 USDT                    │
│ Worst day                     │ -37.724 USDT                   │
│ Days win/draw/lose            │ 58 / 2589 / 131                │
│ Min/Max/Avg. Duration Winners │ 0d 00:20 / 7d 23:10 / 1d 03:16 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 2d 17:50 / 0d 09:52 │
│ Max Consecutive Wins / Loss   │ 4 / 9                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 708.797 USDT                   │
│ Max balance                   │ 1204.394 USDT                  │
│ Max % of account underwater   │ 41.15%                         │
│ Absolute drawdown             │ 495.598 USDT (41.15%)          │
│ Drawdown duration             │ 1936 days 00:05:00             │
│ Profit at drawdown start      │ 204.394 USDT                   │
│ Profit at drawdown end        │ -291.203 USDT                  │
│ Drawdown start                │ 2020-02-09 04:00:00            │
│ Drawdown end                  │ 2025-05-29 04:05:00            │
│ Market change                 │ 2372.94%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    202 │        -0.00 │        -263.477 │       -26.35 │     14:57:00 │   59     0   143  29.2 │ 495.598 USDT  41.15% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-23T14:34:59.652969",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 6996,
  "total_daily_avg_trades": "202 / 0.07",
  "absolute_profit_usdt": -263.477,
  "total_profit_pct": -26.35,
  "cagr_pct": -3.9,
  "sortino": -0.29,
  "sharpe": -0.08,
  "calmar": -0.44,
  "sqn": -0.8,
  "max_consecutive_wins_loss": "4 / 9",
  "min_balance_usdt": 708.797,
  "max_balance_usdt": 1204.394,
  "absolute_drawdown_pct": 41.15,
  "market_change_pct": 2372.94,
  "win_draw_loss_winpct": "59 0 143 29.2"
}
```
