# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 4066  
**Timestamp:** 2025-09-23 14:56:27

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 4066,
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
2025-09-23 12:51:25,130 - freqtrade - INFO - freqtrade 2025.8
2025-09-23 12:51:25,729 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-23 12:51:30,720 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-23 12:51:30,733 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-23 12:51:30,734 - freqtrade.loggers - INFO - Logfile configured
2025-09-23 12:51:30,736 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-23 12:51:30,739 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-23 12:51:30,742 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-23 12:51:30,743 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-23 12:51:30,743 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20251231 ...
2025-09-23 12:51:31,706 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-23 12:51:31,713 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-23 12:51:31,715 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-23 12:51:31,716 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-23 12:51:31,717 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-23 12:51:31,720 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20251231
2025-09-23 12:51:31,726 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-23 12:51:31,777 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-23 12:51:31,780 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 12:51:31,787 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-23 12:51:31,790 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-23 12:51:31,792 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-23 12:51:31,863 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-23 12:51:35,362 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-23 12:51:35,581 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-23 12:51:35,585 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-23 12:51:35,600 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-23 12:51:35,602 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-23 12:51:35,603 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-23 12:51:35,605 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-23 12:51:35,608 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-23 12:51:35,612 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-23 12:51:35,613 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-23 12:51:35,614 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-23 12:51:35,615 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-23 12:51:35,616 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-23 12:51:35,616 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-23 12:51:35,617 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-23 12:51:35,618 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-23 12:51:35,619 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-23 12:51:35,621 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-23 12:51:35,622 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-23 12:51:35,623 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-23 12:51:35,626 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-23 12:51:35,627 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-23 12:51:35,628 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-23 12:51:35,629 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-23 12:51:35,630 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-23 12:51:35,632 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-23 12:51:35,633 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-23 12:51:35,634 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-23 12:51:35,635 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-23 12:51:35,636 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-23 12:51:35,637 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-23 12:51:35,638 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 12:51:35,693 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-23 12:51:35,747 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-23 12:51:35,850 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:51:36,037 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:51:36,190 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:51:36,303 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-23 12:51:36,304 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:51:36,427 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 12:51:36,493 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 12:51:36,856 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:51:37,920 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:51:39,138 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:51:40,527 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-23 12:51:40,529 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:51:41,928 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 12:51:46,815 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-23 12:51:46,826 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-23 12:51:46,827 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-23 12:51:46,831 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.1
2025-09-23 12:51:46,832 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-23 12:51:46,834 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-23 12:51:46,835 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-23 12:51:46,837 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-09-23 12:51:46,840 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.8
2025-09-23 12:51:46,841 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.25
2025-09-23 12:51:46,843 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.008
2025-09-23 12:51:46,845 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-23 12:51:46,847 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): strong_bullish_upper_wick_threshold = 0.25
2025-09-23 12:51:46,849 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-23 12:51:46,851 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1
2025-09-23 12:51:46,853 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1
2025-09-23 12:51:46,854 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-23 12:51:46,856 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 3
2025-09-23 12:51:46,858 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 1.0
2025-09-23 12:51:46,862 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-23 12:51:46,864 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-23 12:51:46,867 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-23 12:51:46,870 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-23 12:51:46,872 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-23 12:55:01,500 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 12:56:25,433 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-23_12-56-25.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │    120 │         0.18 │         150.297 │        15.03 │     12:51:00 │   47     0    73  39.2 │
│ ETH/USDT │     88 │         0.13 │          10.426 │         1.04 │     13:53:00 │   32     0    56  36.4 │
│ XRP/USDT │     86 │         0.07 │          -9.844 │        -0.98 │     12:37:00 │   27     0    59  31.4 │
│ LTC/USDT │     82 │        -0.47 │         -71.387 │        -7.14 │     12:26:00 │   24     0    58  29.3 │
│ BNB/USDT │    107 │        -0.07 │        -178.642 │       -17.86 │     13:40:00 │   32     0    75  29.9 │
│    TOTAL │    483 │        -0.02 │         -99.151 │        -9.92 │     13:06:00 │  162     0   321  33.5 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                      ENTER TAG STATS                                                      
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │     421 │         0.04 │          80.181 │         8.02 │     13:51:00 │  148     0   273  35.2 │
│         hammer_rebond │       8 │        -0.51 │         -86.553 │        -8.66 │      6:37:00 │    1     0     7  12.5 │
│      engulfing_rebond │      54 │        -0.41 │         -92.779 │        -9.28 │      8:19:00 │   13     0    41  24.1 │
│                 TOTAL │     483 │        -0.02 │         -99.151 │        -9.92 │     13:06:00 │  162     0   321  33.5 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │   102 │         4.69 │        3845.910 │       384.59 │     12:07:00 │  102     0     0   100 │
│    exit_signal │   249 │        -0.81 │       -1491.448 │      -149.14 │     17:37:00 │   60     0   189  24.1 │
│      stop_loss │   132 │        -2.14 │       -2453.613 │      -245.36 │      5:22:00 │    0     0   132     0 │
│          TOTAL │   483 │        -0.02 │         -99.151 │        -9.92 │     13:06:00 │  162     0   321  33.5 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                              MIXED TAG STATS                                                              
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_2R │     91 │          4.6 │        3319.492 │       331.95 │     12:31:00 │   91     0     0   100 │
│      engulfing_rebond │ take_profit_2R │     10 │         5.16 │         486.226 │        48.62 │      8:40:00 │   10     0     0   100 │
│         hammer_rebond │ take_profit_2R │      1 │          8.1 │          40.192 │         4.02 │      9:40:00 │    1     0     0   100 │
│         hammer_rebond │    exit_signal │      3 │        -0.96 │         -22.134 │        -2.21 │      6:40:00 │    0     0     3     0 │
│         hammer_rebond │      stop_loss │      4 │        -2.32 │        -104.612 │       -10.46 │      5:49:00 │    0     0     4     0 │
│      engulfing_rebond │    exit_signal │     20 │        -1.05 │        -141.689 │       -14.17 │     14:18:00 │    3     0    17  15.0 │
│      engulfing_rebond │      stop_loss │     24 │        -2.19 │        -437.316 │       -43.73 │      3:12:00 │    0     0    24     0 │
│ strong_bullish_rebond │    exit_signal │    226 │        -0.79 │       -1327.625 │      -132.76 │     18:03:00 │   57     0   169  25.2 │
│ strong_bullish_rebond │      stop_loss │    104 │        -2.12 │       -1911.685 │      -191.17 │      5:51:00 │    0     0   104     0 │
│                 TOTAL │                │    483 │        -0.02 │         -99.151 │        -9.92 │     13:06:00 │  162     0   321  33.5 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2018-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 483 / 0.17                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 900.849 USDT                   │
│ Absolute profit               │ -99.151 USDT                   │
│ Total profit %                │ -9.92%                         │
│ CAGR %                        │ -1.35%                         │
│ Sortino                       │ -0.08                          │
│ Sharpe                        │ -0.03                          │
│ Calmar                        │ -0.13                          │
│ SQN                           │ -0.19                          │
│ Profit factor                 │ 0.98                           │
│ Expectancy (Ratio)            │ -0.21 (-0.02)                  │
│ Avg. daily profit             │ -0.035 USDT                    │
│ Avg. stake amount             │ 896.34 USDT                    │
│ Total trade volume            │ 867498.627 USDT                │
│                               │                                │
│ Best Pair                     │ BTC/USDT 15.03%                │
│ Worst Pair                    │ BNB/USDT -17.86%               │
│ Best trade                    │ XRP/USDT 23.54%                │
│ Worst trade                   │ XRP/USDT -8.18%                │
│ Best day                      │ 111.196 USDT                   │
│ Worst day                     │ -57.185 USDT                   │
│ Days win/draw/lose            │ 142 / 2395 / 262               │
│ Min/Max/Avg. Duration Winners │ 0d 00:20 / 2d 14:00 / 0d 18:11 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 1d 19:00 / 0d 10:33 │
│ Max Consecutive Wins / Loss   │ 6 / 15                         │
│ Rejected Entry signals        │ 12                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 821.806 USDT                   │
│ Max balance                   │ 1663.932 USDT                  │
│ Max % of account underwater   │ 50.61%                         │
│ Absolute drawdown             │ 842.126 USDT (50.61%)          │
│ Drawdown duration             │ 1331 days 04:30:00             │
│ Profit at drawdown start      │ 663.932 USDT                   │
│ Profit at drawdown end        │ -178.194 USDT                  │
│ Drawdown start                │ 2021-11-08 00:30:00            │
│ Drawdown end                  │ 2025-07-01 05:00:00            │
│ Market change                 │ 2372.94%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    483 │        -0.02 │         -99.151 │        -9.92 │     13:06:00 │  162     0   321  33.5 │ 842.126 USDT  50.61% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-23T14:56:27.054295",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 4066,
  "total_daily_avg_trades": "483 / 0.17",
  "absolute_profit_usdt": -99.151,
  "total_profit_pct": -9.92,
  "cagr_pct": -1.35,
  "sortino": -0.08,
  "sharpe": -0.03,
  "calmar": -0.13,
  "sqn": -0.19,
  "max_consecutive_wins_loss": "6 / 15",
  "min_balance_usdt": 821.806,
  "max_balance_usdt": 1663.932,
  "absolute_drawdown_pct": 50.61,
  "market_change_pct": 2372.94,
  "win_draw_loss_winpct": "162 0 321 33.5"
}
```
