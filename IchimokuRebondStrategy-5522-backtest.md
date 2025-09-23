# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 5522  
**Timestamp:** 2025-09-23 14:42:21

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 5522,
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
2025-09-23 12:36:24,522 - freqtrade - INFO - freqtrade 2025.8
2025-09-23 12:36:25,328 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-23 12:36:30,278 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-23 12:36:30,292 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-23 12:36:30,293 - freqtrade.loggers - INFO - Logfile configured
2025-09-23 12:36:30,294 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-23 12:36:30,296 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-23 12:36:30,297 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-23 12:36:30,298 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-23 12:36:30,299 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20251231 ...
2025-09-23 12:36:31,072 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-23 12:36:31,077 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-23 12:36:31,077 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-23 12:36:31,078 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-23 12:36:31,078 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-23 12:36:31,079 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20251231
2025-09-23 12:36:31,082 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-23 12:36:31,109 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-23 12:36:31,110 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 12:36:31,115 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-23 12:36:31,116 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-23 12:36:31,117 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-23 12:36:31,178 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-23 12:36:34,693 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-23 12:36:34,889 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-23 12:36:34,892 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-23 12:36:34,903 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-23 12:36:34,905 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-23 12:36:34,906 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-23 12:36:34,907 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-23 12:36:34,908 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-23 12:36:34,909 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-23 12:36:34,910 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-23 12:36:34,910 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-23 12:36:34,911 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-23 12:36:34,912 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-23 12:36:34,912 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-23 12:36:34,913 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-23 12:36:34,913 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-23 12:36:34,914 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-23 12:36:34,915 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-23 12:36:34,916 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-23 12:36:34,917 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-23 12:36:34,918 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-23 12:36:34,919 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-23 12:36:34,921 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-23 12:36:34,922 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-23 12:36:34,924 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-23 12:36:34,925 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-23 12:36:34,926 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-23 12:36:34,927 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-23 12:36:34,928 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-23 12:36:34,928 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-23 12:36:34,929 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-23 12:36:34,931 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 12:36:34,966 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-23 12:36:35,051 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-23 12:36:35,178 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:36:35,459 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:36:35,642 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:36:35,865 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-23 12:36:35,867 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:36:36,092 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:36:36,245 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 12:36:36,966 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:36:39,480 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:36:41,631 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:36:43,501 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-23 12:36:43,503 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:36:45,373 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:36:52,573 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-23 12:36:52,583 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-23 12:36:52,585 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-23 12:36:52,587 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.1
2025-09-23 12:36:52,588 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-23 12:36:52,589 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-23 12:36:52,589 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-23 12:36:52,591 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-09-23 12:36:52,591 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.8
2025-09-23 12:36:52,592 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.25
2025-09-23 12:36:52,593 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.008
2025-09-23 12:36:52,593 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-23 12:36:52,594 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-23 12:36:52,595 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1
2025-09-23 12:36:52,596 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1
2025-09-23 12:36:52,598 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-23 12:36:52,598 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 3
2025-09-23 12:36:52,600 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 1.0
2025-09-23 12:36:52,601 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-23 12:36:52,602 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-23 12:36:52,603 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-23 12:36:52,604 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-23 12:36:52,604 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-23 12:41:32,091 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 12:42:16,522 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-23_12-42-16.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │     10 │         1.92 │          75.660 │         7.57 │     16:06:00 │    4     0     6  40.0 │
│ BTC/USDT │     11 │         0.38 │          -8.792 │        -0.88 │     21:15:00 │    4     0     7  36.4 │
│ ETH/USDT │     14 │         -0.2 │         -34.425 │        -3.44 │      9:24:00 │    5     0     9  35.7 │
│ BNB/USDT │     21 │         0.01 │         -70.338 │        -7.03 │     11:32:00 │    4     0    17  19.0 │
│ LTC/USDT │     20 │        -0.35 │         -70.509 │        -7.05 │     16:18:00 │    5     0    15  25.0 │
│    TOTAL │     76 │         0.18 │        -108.405 │       -10.84 │     14:24:00 │   22     0    54  28.9 │
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
│ engulfing_rebond │      63 │         0.25 │         -51.021 │         -5.1 │     15:55:00 │   19     0    44  30.2 │
│    hammer_rebond │      13 │        -0.15 │         -57.384 │        -5.74 │      7:05:00 │    3     0    10  23.1 │
│            TOTAL │      76 │         0.18 │        -108.405 │       -10.84 │     14:24:00 │   22     0    54  28.9 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │    22 │         5.62 │         744.219 │        74.42 │ 1 day, 2:12:00 │   22     0     0   100 │
│      stop_loss │    54 │        -2.03 │        -852.624 │       -85.26 │        9:36:00 │    0     0    54     0 │
│          TOTAL │    76 │         0.18 │        -108.405 │       -10.84 │       14:24:00 │   22     0    54  28.9 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                            MIXED TAG STATS                                                             
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │ take_profit_2R │     19 │         5.59 │         628.602 │        62.86 │ 1 day, 5:29:00 │   19     0     0   100 │
│    hammer_rebond │ take_profit_2R │      3 │         5.84 │         115.617 │        11.56 │        5:22:00 │    3     0     0   100 │
│    hammer_rebond │      stop_loss │     10 │        -1.95 │        -173.001 │        -17.3 │        7:36:00 │    0     0    10     0 │
│ engulfing_rebond │      stop_loss │     44 │        -2.05 │        -679.623 │       -67.96 │       10:03:00 │    0     0    44     0 │
│            TOTAL │                │     76 │         0.18 │        -108.405 │       -10.84 │       14:24:00 │   22     0    54  28.9 │
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
│ Total/Daily Avg Trades        │ 76 / 0.03                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 891.595 USDT                   │
│ Absolute profit               │ -108.405 USDT                  │
│ Total profit %                │ -10.84%                        │
│ CAGR %                        │ -1.48%                         │
│ Sortino                       │ -0.12                          │
│ Sharpe                        │ -0.03                          │
│ Calmar                        │ -0.39                          │
│ SQN                           │ -0.52                          │
│ Profit factor                 │ 0.87                           │
│ Expectancy (Ratio)            │ -1.43 (-0.09)                  │
│ Avg. daily profit             │ -0.039 USDT                    │
│ Avg. stake amount             │ 817.553 USDT                   │
│ Total trade volume            │ 124408.193 USDT                │
│                               │                                │
│ Best Pair                     │ XRP/USDT 7.57%                 │
│ Worst Pair                    │ LTC/USDT -7.05%                │
│ Best trade                    │ BNB/USDT 13.11%                │
│ Worst trade                   │ LTC/USDT -6.89%                │
│ Best day                      │ 51.532 USDT                    │
│ Worst day                     │ -28.048 USDT                   │
│ Days win/draw/lose            │ 22 / 2621 / 50                 │
│ Min/Max/Avg. Duration Winners │ 0d 00:20 / 3d 22:00 / 1d 02:12 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 2d 00:00 / 0d 09:36 │
│ Max Consecutive Wins / Loss   │ 3 / 7                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 883.227 USDT                   │
│ Max balance                   │ 1089.265 USDT                  │
│ Max % of account underwater   │ 18.92%                         │
│ Absolute drawdown             │ 206.038 USDT (18.92%)          │
│ Drawdown duration             │ 1626 days 00:40:00             │
│ Profit at drawdown start      │ 89.265 USDT                    │
│ Profit at drawdown end        │ -116.773 USDT                  │
│ Drawdown start                │ 2020-02-09 04:00:00            │
│ Drawdown end                  │ 2024-07-23 04:40:00            │
│ Market change                 │ 2372.94%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     76 │         0.18 │        -108.405 │       -10.84 │     14:24:00 │   22     0    54  28.9 │ 206.038 USDT  18.92% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-23T14:42:20.738558",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 5522,
  "total_daily_avg_trades": "76 / 0.03",
  "absolute_profit_usdt": -108.405,
  "total_profit_pct": -10.84,
  "cagr_pct": -1.48,
  "sortino": -0.12,
  "sharpe": -0.03,
  "calmar": -0.39,
  "sqn": -0.52,
  "max_consecutive_wins_loss": "3 / 7",
  "min_balance_usdt": 883.227,
  "max_balance_usdt": 1089.265,
  "absolute_drawdown_pct": 18.92,
  "market_change_pct": 2372.94,
  "win_draw_loss_winpct": "22 0 54 28.9"
}
```
