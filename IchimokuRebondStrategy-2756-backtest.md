# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 2756  
**Timestamp:** 2025-09-23 17:29:06

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 2756,
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
2025-09-23 15:21:37,181 - freqtrade - INFO - freqtrade 2025.8
2025-09-23 15:21:37,932 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-23 15:21:40,835 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-23 15:21:40,844 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-23 15:21:40,845 - freqtrade.loggers - INFO - Logfile configured
2025-09-23 15:21:40,846 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-23 15:21:40,847 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-23 15:21:40,847 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-23 15:21:40,848 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-23 15:21:40,849 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20251231 ...
2025-09-23 15:21:41,333 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-23 15:21:41,335 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-23 15:21:41,336 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-23 15:21:41,337 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-23 15:21:41,337 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-23 15:21:41,338 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20251231
2025-09-23 15:21:41,340 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-23 15:21:41,352 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-23 15:21:41,352 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 15:21:41,355 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-23 15:21:41,356 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-23 15:21:41,357 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-23 15:21:41,379 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-23 15:21:43,716 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-23 15:21:43,819 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-23 15:21:43,821 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-23 15:21:43,825 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-23 15:21:43,825 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-23 15:21:43,826 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-23 15:21:43,826 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-23 15:21:43,826 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-23 15:21:43,827 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-23 15:21:43,827 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-23 15:21:43,828 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-23 15:21:43,828 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-23 15:21:43,828 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-23 15:21:43,829 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-23 15:21:43,829 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-23 15:21:43,830 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-23 15:21:43,830 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-23 15:21:43,831 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-23 15:21:43,831 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-23 15:21:43,832 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-23 15:21:43,832 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-23 15:21:43,833 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-23 15:21:43,833 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-23 15:21:43,834 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-23 15:21:43,834 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-23 15:21:43,834 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-23 15:21:43,835 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-23 15:21:43,835 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-23 15:21:43,835 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-23 15:21:43,836 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-23 15:21:43,836 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-23 15:21:43,836 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 15:21:43,860 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-23 15:21:43,884 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-23 15:21:43,953 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 15:21:44,041 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 15:21:44,107 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 15:21:44,166 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-23 15:21:44,167 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 15:21:44,227 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 15:21:44,261 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 15:21:44,512 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 15:21:45,397 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 15:21:46,077 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 15:21:46,774 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-23 15:21:46,775 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 15:21:47,403 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 15:21:50,204 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-23 15:21:50,221 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-23 15:21:50,222 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-23 15:21:50,223 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-23 15:21:50,223 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-23 15:21:50,224 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-23 15:21:50,224 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-23 15:21:50,224 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-23 15:21:50,225 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-23 15:21:50,225 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-23 15:21:50,225 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-23 15:21:50,226 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-23 15:21:50,226 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-23 15:21:50,226 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-23 15:21:50,227 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-23 15:21:50,227 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-23 15:21:50,227 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-23 15:21:50,228 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 1
2025-09-23 15:21:50,228 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-23 15:21:50,228 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-23 15:21:50,229 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-23 15:21:50,229 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower
2025-09-23 15:21:50,229 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-23 15:21:50,230 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-23 15:23:08,936 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 15:29:04,521 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-23_15-29-04.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │    363 │         0.48 │         468.218 │        46.82 │     13:52:00 │  119     0   244  32.8 │
│ ETH/USDT │    445 │         0.34 │         427.989 │         42.8 │     16:35:00 │  148     0   297  33.3 │
│ BNB/USDT │    431 │          0.2 │         240.084 │        24.01 │     16:02:00 │  136     0   295  31.6 │
│ BTC/USDT │    511 │         0.14 │         169.667 │        16.97 │     17:02:00 │  158     0   353  30.9 │
│ LTC/USDT │    357 │        -0.32 │        -369.090 │       -36.91 │     15:20:00 │  105     0   252  29.4 │
│    TOTAL │   2107 │         0.17 │         936.867 │        93.69 │     15:54:00 │  666     0  1441  31.6 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                           LEFT OPEN TRADES REPORT                                           
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         0.05 │           0.185 │         0.02 │      5:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         0.05 │           0.185 │         0.02 │      5:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                      ENTER TAG STATS                                                      
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │    1613 │         0.18 │         679.290 │        67.93 │     16:30:00 │  527     0  1086  32.7 │
│         hammer_rebond │     277 │         0.17 │         131.206 │        13.12 │     12:36:00 │   73     0   204  26.4 │
│      engulfing_rebond │     217 │         0.14 │         126.371 │        12.64 │     15:35:00 │   66     0   151  30.4 │
│                 TOTAL │    2107 │         0.17 │         936.867 │        93.69 │     15:54:00 │  666     0  1441  31.6 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │   153 │        10.45 │        4643.443 │       464.34 │     22:40:00 │  153     0     0   100 │
│     force_exit │     1 │         0.05 │           0.185 │         0.02 │      5:00:00 │    1     0     0   100 │
│      stop_loss │     6 │       -10.18 │        -167.120 │       -16.71 │      4:28:00 │    0     0     6     0 │
│    exit_signal │  1947 │         -0.6 │       -3539.641 │      -353.96 │     15:24:00 │  512     0  1435  26.3 │
│          TOTAL │  2107 │         0.17 │         936.867 │        93.69 │     15:54:00 │  666     0  1441  31.6 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                               MIXED TAG STATS                                                               
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_1R │    116 │        10.42 │        3490.936 │       349.09 │       22:31:00 │  116     0     0   100 │
│         hammer_rebond │ take_profit_1R │     22 │        10.53 │         673.812 │        67.38 │ 1 day, 1:22:00 │   22     0     0   100 │
│      engulfing_rebond │ take_profit_1R │     15 │        10.52 │         478.696 │        47.87 │       19:49:00 │   15     0     0   100 │
│ strong_bullish_rebond │     force_exit │      1 │         0.05 │           0.185 │         0.02 │        5:00:00 │    1     0     0   100 │
│ strong_bullish_rebond │      stop_loss │      6 │       -10.18 │        -167.120 │       -16.71 │        4:28:00 │    0     0     6     0 │
│      engulfing_rebond │    exit_signal │    202 │        -0.63 │        -352.325 │       -35.23 │       15:16:00 │   51     0   151  25.2 │
│         hammer_rebond │    exit_signal │    255 │        -0.72 │        -542.605 │       -54.26 │       11:29:00 │   51     0   204  20.0 │
│ strong_bullish_rebond │    exit_signal │   1490 │        -0.58 │       -2644.711 │      -264.47 │       16:06:00 │  410     0  1080  27.5 │
│                 TOTAL │                │   2107 │         0.17 │         936.867 │        93.69 │       15:54:00 │  666     0  1441  31.6 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2018-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 2107 / 0.75                    │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1936.867 USDT                  │
│ Absolute profit               │ 936.867 USDT                   │
│ Total profit %                │ 93.69%                         │
│ CAGR %                        │ 8.97%                          │
│ Sortino                       │ 1.57                           │
│ Sharpe                        │ 0.60                           │
│ Calmar                        │ 3.25                           │
│ SQN                           │ 1.92                           │
│ Profit factor                 │ 1.14                           │
│ Expectancy (Ratio)            │ 0.44 (0.09)                    │
│ Avg. daily profit             │ 0.334 USDT                     │
│ Avg. stake amount             │ 306.026 USDT                   │
│ Total trade volume            │ 1293113.121 USDT               │
│                               │                                │
│ Best Pair                     │ XRP/USDT 46.82%                │
│ Worst Pair                    │ LTC/USDT -36.91%               │
│ Best trade                    │ XRP/USDT 13.21%                │
│ Worst trade                   │ ETH/USDT -10.18%               │
│ Best day                      │ 106.469 USDT                   │
│ Worst day                     │ -49.073 USDT                   │
│ Days win/draw/lose            │ 395 / 1639 / 769               │
│ Min/Max/Avg. Duration Winners │ 0d 00:15 / 3d 05:35 / 1d 04:04 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 1d 22:00 / 0d 10:16 │
│ Max Consecutive Wins / Loss   │ 7 / 30                         │
│ Rejected Entry signals        │ 2647                           │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 1018.218 USDT                  │
│ Max balance                   │ 2210.227 USDT                  │
│ Max % of account underwater   │ 19.63%                         │
│ Absolute drawdown             │ 433.887 USDT (19.63%)          │
│ Drawdown duration             │ 1079 days 07:00:00             │
│ Profit at drawdown start      │ 1210.227 USDT                  │
│ Profit at drawdown end        │ 776.34 USDT                    │
│ Drawdown start                │ 2021-11-14 09:00:00            │
│ Drawdown end                  │ 2024-10-28 16:00:00            │
│ Market change                 │ 2372.94%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │   2107 │         0.17 │         936.867 │        93.69 │     15:54:00 │  666     0  1441  31.6 │ 433.887 USDT  19.63% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-23T17:29:06.577093",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 2756,
  "total_daily_avg_trades": "2107 / 0.75",
  "absolute_profit_usdt": 936.867,
  "total_profit_pct": 93.69,
  "cagr_pct": 8.97,
  "sortino": 1.57,
  "sharpe": 0.6,
  "calmar": 3.25,
  "sqn": 1.92,
  "max_consecutive_wins_loss": "7 / 30",
  "min_balance_usdt": 1018.218,
  "max_balance_usdt": 2210.227,
  "absolute_drawdown_pct": 19.63,
  "market_change_pct": 2372.94,
  "win_draw_loss_winpct": "666 0 1441 31.6"
}
```
