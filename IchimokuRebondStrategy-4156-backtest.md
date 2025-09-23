# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 4156  
**Timestamp:** 2025-09-23 14:24:49

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 4156,
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
2025-09-23 12:17:28,331 - freqtrade - INFO - freqtrade 2025.8
2025-09-23 12:17:30,355 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-23 12:17:38,477 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-23 12:17:38,496 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-23 12:17:38,497 - freqtrade.loggers - INFO - Logfile configured
2025-09-23 12:17:38,497 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-23 12:17:38,499 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-23 12:17:38,500 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-23 12:17:38,501 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-23 12:17:38,502 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20251231 ...
2025-09-23 12:17:39,460 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-23 12:17:39,467 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-23 12:17:39,470 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-23 12:17:39,472 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-23 12:17:39,474 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-23 12:17:39,476 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20251231
2025-09-23 12:17:39,480 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-23 12:17:39,537 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-23 12:17:39,542 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 12:17:39,553 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-23 12:17:39,554 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-23 12:17:39,555 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-23 12:17:39,608 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-23 12:17:43,465 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-23 12:17:43,713 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-23 12:17:43,717 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-23 12:17:43,728 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-23 12:17:43,729 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-23 12:17:43,729 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-23 12:17:43,730 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-23 12:17:43,730 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-23 12:17:43,732 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-23 12:17:43,732 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-23 12:17:43,733 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-23 12:17:43,733 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-23 12:17:43,734 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-23 12:17:43,734 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-23 12:17:43,735 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-23 12:17:43,735 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-23 12:17:43,736 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-23 12:17:43,737 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-23 12:17:43,738 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-23 12:17:43,739 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-23 12:17:43,740 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-23 12:17:43,742 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-23 12:17:43,744 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-23 12:17:43,745 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-23 12:17:43,746 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-23 12:17:43,747 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-23 12:17:43,748 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-23 12:17:43,749 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-23 12:17:43,750 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-23 12:17:43,750 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-23 12:17:43,751 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-23 12:17:43,751 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 12:17:43,796 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-23 12:17:43,853 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-23 12:17:44,001 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:17:44,289 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:17:44,513 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:17:44,662 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-23 12:17:44,664 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:17:44,816 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:17:44,925 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 12:17:45,676 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:17:47,392 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:17:48,798 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:17:50,288 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-23 12:17:50,289 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:17:51,697 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:17:57,982 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-23 12:17:57,996 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-23 12:17:57,997 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-23 12:17:57,998 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.1
2025-09-23 12:17:58,000 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-23 12:17:58,002 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = True
2025-09-23 12:17:58,004 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-23 12:17:58,005 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-09-23 12:17:58,007 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.811
2025-09-23 12:17:58,008 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.28
2025-09-23 12:17:58,009 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.008
2025-09-23 12:17:58,010 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-23 12:17:58,011 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-23 12:17:58,012 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-23 12:17:58,013 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1
2025-09-23 12:17:58,014 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-23 12:17:58,014 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 3
2025-09-23 12:17:58,015 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 1.0
2025-09-23 12:17:58,016 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-23 12:17:58,017 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-23 12:17:58,020 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-23 12:17:58,023 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-23 12:17:58,025 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-23 12:22:41,830 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 12:24:44,728 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-23_12-24-44.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │     32 │         0.77 │         114.304 │        11.43 │     15:54:00 │   11     0    21  34.4 │
│ BTC/USDT │     41 │         0.05 │         -27.361 │        -2.74 │     19:57:00 │   14     0    27  34.1 │
│ LTC/USDT │     37 │        -0.05 │         -38.337 │        -3.83 │     14:41:00 │   11     0    26  29.7 │
│ ETH/USDT │     27 │        -0.42 │        -102.398 │       -10.24 │     10:58:00 │    8     0    19  29.6 │
│ BNB/USDT │     45 │        -0.25 │        -186.663 │       -18.67 │     14:21:00 │    9     0    36  20.0 │
│    TOTAL │    182 │         0.01 │        -240.456 │       -24.05 │     15:27:00 │   53     0   129  29.1 │
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
│    hammer_rebond │      31 │        -0.05 │         -56.741 │        -5.67 │      7:57:00 │    9     0    22  29.0 │
│ engulfing_rebond │     151 │         0.03 │        -183.715 │       -18.37 │     16:59:00 │   44     0   107  29.1 │
│            TOTAL │     182 │         0.01 │        -240.456 │       -24.05 │     15:27:00 │   53     0   129  29.1 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │    53 │         4.57 │        1764.888 │       176.49 │ 1 day, 3:30:00 │   53     0     0   100 │
│      stop_loss │   129 │        -1.86 │       -2005.344 │      -200.53 │       10:30:00 │    0     0   129     0 │
│          TOTAL │   182 │         0.01 │        -240.456 │       -24.05 │       15:27:00 │   53     0   129  29.1 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                            MIXED TAG STATS                                                             
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │ take_profit_2R │     44 │         4.63 │        1450.626 │       145.06 │ 1 day, 7:40:00 │   44     0     0   100 │
│    hammer_rebond │ take_profit_2R │      9 │          4.3 │         314.262 │        31.43 │        7:07:00 │    9     0     0   100 │
│    hammer_rebond │      stop_loss │     22 │        -1.84 │        -371.003 │        -37.1 │        8:18:00 │    0     0    22     0 │
│ engulfing_rebond │      stop_loss │    107 │        -1.86 │       -1634.341 │      -163.43 │       10:57:00 │    0     0   107     0 │
│            TOTAL │                │    182 │         0.01 │        -240.456 │       -24.05 │       15:27:00 │   53     0   129  29.1 │
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
│ Total/Daily Avg Trades        │ 182 / 0.06                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 759.544 USDT                   │
│ Absolute profit               │ -240.456 USDT                  │
│ Total profit %                │ -24.05%                        │
│ CAGR %                        │ -3.51%                         │
│ Sortino                       │ -0.25                          │
│ Sharpe                        │ -0.07                          │
│ Calmar                        │ -0.37                          │
│ SQN                           │ -0.75                          │
│ Profit factor                 │ 0.88                           │
│ Expectancy (Ratio)            │ -1.32 (-0.08)                  │
│ Avg. daily profit             │ -0.086 USDT                    │
│ Avg. stake amount             │ 877.06 USDT                    │
│ Total trade volume            │ 319647.871 USDT                │
│                               │                                │
│ Best Pair                     │ XRP/USDT 11.43%                │
│ Worst Pair                    │ BNB/USDT -18.67%               │
│ Best trade                    │ BNB/USDT 13.11%                │
│ Worst trade                   │ LTC/USDT -6.89%                │
│ Best day                      │ 80.614 USDT                    │
│ Worst day                     │ -40.63 USDT                    │
│ Days win/draw/lose            │ 52 / 2607 / 119                │
│ Min/Max/Avg. Duration Winners │ 0d 00:20 / 7d 23:10 / 1d 03:30 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 2d 17:50 / 0d 10:30 │
│ Max Consecutive Wins / Loss   │ 3 / 9                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 724.503 USDT                   │
│ Max balance                   │ 1301.805 USDT                  │
│ Max % of account underwater   │ 44.35%                         │
│ Absolute drawdown             │ 577.302 USDT (44.35%)          │
│ Drawdown duration             │ 1936 days 00:05:00             │
│ Profit at drawdown start      │ 301.805 USDT                   │
│ Profit at drawdown end        │ -275.497 USDT                  │
│ Drawdown start                │ 2020-02-09 04:00:00            │
│ Drawdown end                  │ 2025-05-29 04:05:00            │
│ Market change                 │ 2372.94%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    182 │         0.01 │        -240.456 │       -24.05 │     15:27:00 │   53     0   129  29.1 │ 577.302 USDT  44.35% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-23T14:24:49.465421",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 4156,
  "total_daily_avg_trades": "182 / 0.06",
  "absolute_profit_usdt": -240.456,
  "total_profit_pct": -24.05,
  "cagr_pct": -3.51,
  "sortino": -0.25,
  "sharpe": -0.07,
  "calmar": -0.37,
  "sqn": -0.75,
  "max_consecutive_wins_loss": "3 / 9",
  "min_balance_usdt": 724.503,
  "max_balance_usdt": 1301.805,
  "absolute_drawdown_pct": 44.35,
  "market_change_pct": 2372.94,
  "win_draw_loss_winpct": "53 0 129 29.1"
}
```
