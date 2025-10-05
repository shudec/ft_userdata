# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 611  
**Timestamp:** 2025-10-02 21:00:29

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "pairs": [
    "ADA/USDT",
    "SOL/USDT",
    "DOGE/USDT",
    "TRX/USDT"
  ],
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 611,
  "epochs": 100,
  "hyperopt_timerange": "20220101-20231231",
  "backtest_timerange": "20220101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs ADA/USDT SOL/USDT DOGE/USDT TRX/USDT --timerange 20220101-20251231 --export trades
```

## Backtesting Output
```
2025-10-02 18:57:18,673 - freqtrade - INFO - freqtrade 2025.7
2025-10-02 18:57:19,055 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-10-02 18:57:19,056 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-02 18:57:20,638 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-02 18:57:20,641 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-02 18:57:20,642 - freqtrade.loggers - INFO - Logfile configured
2025-10-02 18:57:20,642 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-02 18:57:20,643 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-10-02 18:57:20,644 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-02 18:57:20,644 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-02 18:57:20,645 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-10-02 18:57:20,655 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-02 18:57:20,656 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-02 18:57:20,657 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-02 18:57:20,657 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-02 18:57:20,658 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-02 18:57:20,658 - freqtrade.configuration.configuration - INFO - Using pairs ['ADA/USDT', 'SOL/USDT', 'DOGE/USDT', 'TRX/USDT']
2025-10-02 18:57:20,659 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-10-02 18:57:20,661 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-02 18:57:20,682 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-02 18:57:20,683 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-02 18:57:20,687 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-02 18:57:20,688 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-02 18:57:20,689 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-10-02 18:57:20,726 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-02 18:57:23,296 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-02 18:57:23,338 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-10-02 18:57:23,339 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-10-02 18:57:23,340 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-10-02 18:57:23,340 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-02 18:57:23,341 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-02 18:57:23,341 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-02 18:57:23,342 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-02 18:57:23,342 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-02 18:57:23,342 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-10-02 18:57:23,343 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-10-02 18:57:23,343 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-02 18:57:23,343 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-02 18:57:23,344 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-02 18:57:23,344 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-02 18:57:23,344 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-02 18:57:23,345 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-10-02 18:57:23,345 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-02 18:57:23,346 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-02 18:57:23,346 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-02 18:57:23,346 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-10-02 18:57:23,347 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-02 18:57:23,347 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-10-02 18:57:23,347 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-02 18:57:23,348 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-02 18:57:23,348 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-02 18:57:23,348 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-02 18:57:23,349 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-02 18:57:23,349 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-02 18:57:23,349 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-02 18:57:23,350 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-02 18:57:23,351 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-02 18:57:23,358 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-02 18:57:23,392 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-02 18:57:23,433 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-02 18:57:23,491 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-02 18:57:23,534 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-02 18:57:23,578 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-02 18:57:23,603 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-10-02 17:00:00 (1370 days).
2025-10-02 18:57:23,671 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-02 18:57:23,873 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-02 18:57:24,115 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-02 18:57:24,326 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-02 18:57:25,505 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-02 18:57:25,508 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-02 18:57:25,509 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-10-02 18:57:25,509 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.4
2025-10-02 18:57:25,510 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-10-02 18:57:25,510 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-10-02 18:57:25,510 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-10-02 18:57:25,511 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_strength_threshold = 0.02
2025-10-02 18:57:25,511 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 20
2025-10-02 18:57:25,511 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-10-02 18:57:25,512 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 1
2025-10-02 18:57:25,512 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-10-02 18:57:25,513 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.02
2025-10-02 18:57:25,513 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.003
2025-10-02 18:57:25,513 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_engulfing_signal_strength_threshold_max = 0.132
2025-10-02 18:57:25,514 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_engulfing_signal_strength_threshold_min = 0.071
2025-10-02 18:57:25,514 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_hammer_signal_strength_threshold_max = 0.431
2025-10-02 18:57:25,514 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_hammer_signal_strength_threshold_min = 0.254
2025-10-02 18:57:25,515 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-10-02 18:57:25,515 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-10-02 18:57:25,515 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_size_threshold = 2
2025-10-02 18:57:25,516 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_strength_threshold = 0.02
2025-10-02 18:57:25,516 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.409
2025-10-02 18:57:25,517 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.003
2025-10-02 18:57:25,517 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_engulfing_entry = True
2025-10-02 18:57:25,517 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_hammer_entry = False
2025-10-02 18:57:25,518 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_strong_bullish_entry = False
2025-10-02 18:57:25,518 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0
2025-10-02 18:57:25,519 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 0.5
2025-10-02 18:57:25,519 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-10-02 18:57:25,520 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-10-02 18:57:25,520 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 6
2025-10-02 18:57:25,521 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-10-02 18:57:25,521 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-10-02 18:57:25,521 - freqtrade.strategy.hyper - INFO - Strategy Parameter: trailing_custom_stop = False
2025-10-02 18:57:25,522 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-10-02 18:57:25,522 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-10-02 18:57:25,523 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-10-02 18:57:25,523 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-10-02 18:57:25,523 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = False
2025-10-02 18:57:25,524 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-10-02 18:57:25,524 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-10-02 18:57:25,525 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-02 18:57:25,528 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 18:57:25,537 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-02 18:57:25,564 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 18:57:25,581 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-02 18:57:36,113 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 18:57:36,120 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-02 18:57:36,144 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 18:57:36,163 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-02 18:57:49,674 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 18:57:49,683 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-02 18:57:49,707 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 18:57:49,724 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-02 18:58:00,985 - freqtrade.data.dataprovider - INFO - Loading data for TRX/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 18:58:00,993 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-02 18:58:01,017 - freqtrade.data.dataprovider - INFO - Loading data for TRX/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 18:58:01,040 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-02 18:58:14,297 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-10-02 17:00:00 (1370 days).
2025-10-02 19:00:27,930 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-02_19-00-27.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                               
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  TRX/USDT │     30 │        -0.25 │         -16.586 │        -1.66 │ 1 day, 9:42:00 │   10     0    20  33.3 │
│ DOGE/USDT │    133 │        -0.04 │         -29.679 │        -2.97 │ 1 day, 1:15:00 │   41     0    92  30.8 │
│  SOL/USDT │    189 │        -0.14 │        -116.025 │        -11.6 │       20:11:00 │   55     0   134  29.1 │
│  ADA/USDT │    145 │        -0.12 │        -162.700 │       -16.27 │       22:38:00 │   45     0   100  31.0 │
│     TOTAL │    497 │        -0.11 │        -324.989 │        -32.5 │       23:05:00 │  151     0   346  30.4 │
└───────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
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
│ engulfing_rebond │     497 │        -0.11 │        -324.989 │        -32.5 │     23:05:00 │  151     0   346  30.4 │
│            TOTAL │     497 │        -0.11 │        -324.989 │        -32.5 │     23:05:00 │  151     0   346  30.4 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        EXIT REASON STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                 Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│              take_profit_2R │    95 │         8.68 │        3371.133 │       337.11 │ 1 day, 6:06:00 │   95     0     0   100 │
│ ichimoku_cloud_crossed_exit │   262 │        -1.27 │       -1323.194 │      -132.32 │ 1 day, 1:49:00 │   56     0   206  21.4 │
│                   stop_loss │   140 │        -3.92 │       -2372.929 │      -237.29 │       13:10:00 │    0     0   140     0 │
│                       TOTAL │   497 │        -0.11 │        -324.989 │        -32.5 │       23:05:00 │  151     0   346  30.4 │
└─────────────────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                                   MIXED TAG STATS                                                                   
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃                 Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │              take_profit_2R │     95 │         8.68 │        3371.133 │       337.11 │ 1 day, 6:06:00 │   95     0     0   100 │
│ engulfing_rebond │ ichimoku_cloud_crossed_exit │    262 │        -1.27 │       -1323.194 │      -132.32 │ 1 day, 1:49:00 │   56     0   206  21.4 │
│ engulfing_rebond │                   stop_loss │    140 │        -3.92 │       -2372.929 │      -237.29 │       13:10:00 │    0     0   140     0 │
│            TOTAL │                             │    497 │        -0.11 │        -324.989 │        -32.5 │       23:05:00 │  151     0   346  30.4 │
└──────────────────┴─────────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2025-10-02 17:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 497 / 0.36                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 675.011 USDT                   │
│ Absolute profit               │ -324.989 USDT                  │
│ Total profit %                │ -32.50%                        │
│ CAGR %                        │ -9.94%                         │
│ Sortino                       │ -0.70                          │
│ Sharpe                        │ -0.23                          │
│ Calmar                        │ -0.99                          │
│ SQN                           │ -0.75                          │
│ Profit factor                 │ 0.92                           │
│ Expectancy (Ratio)            │ -0.65 (-0.06)                  │
│ Avg. daily profit             │ -0.237 USDT                    │
│ Avg. stake amount             │ 422.495 USDT                   │
│ Total trade volume            │ 420474.76 USDT                 │
│                               │                                │
│ Best Pair                     │ TRX/USDT -1.66%                │
│ Worst Pair                    │ ADA/USDT -16.27%               │
│ Best trade                    │ SOL/USDT 14.65%                │
│ Worst trade                   │ SOL/USDT -9.29%                │
│ Best day                      │ 72.76 USDT                     │
│ Worst day                     │ -58.604 USDT                   │
│ Days win/draw/lose            │ 129 / 968 / 263                │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 5d 05:10 / 1d 09:55 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 3d 17:00 / 0d 18:21 │
│ Max Consecutive Wins / Loss   │ 5 / 19                         │
│ Rejected Entry signals        │ 12                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 675.011 USDT                   │
│ Max balance                   │ 1245.835 USDT                  │
│ Max % of account underwater   │ 45.82%                         │
│ Absolute Drawdown (Account)   │ 45.82%                         │
│ Absolute Drawdown             │ 570.825 USDT                   │
│ Drawdown high                 │ 245.835 USDT                   │
│ Drawdown low                  │ -324.989 USDT                  │
│ Drawdown Start                │ 2025-01-17 09:10:00            │
│ Drawdown End                  │ 2025-09-30 10:00:00            │
│ Market change                 │ 99.71%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-10-02 17:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    497 │        -0.11 │        -324.989 │        -32.5 │     23:05:00 │  151     0   346  30.4 │ 570.825 USDT  45.82% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-02T21:00:29.358240",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 611,
  "total_daily_avg_trades": "497 / 0.36",
  "absolute_profit_usdt": -324.989,
  "total_profit_pct": -32.5,
  "cagr_pct": -9.94,
  "sortino": -0.7,
  "sharpe": -0.23,
  "calmar": -0.99,
  "sqn": -0.75,
  "max_consecutive_wins_loss": "5 / 19",
  "min_balance_usdt": 675.011,
  "max_balance_usdt": 1245.835,
  "market_change_pct": 99.71,
  "win_draw_loss_winpct": "151 0 346 30.4"
}
```
