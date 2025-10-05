# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 9989  
**Timestamp:** 2025-10-02 21:55:51

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
  "random_state": 9989,
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
2025-10-02 19:44:18,915 - freqtrade - INFO - freqtrade 2025.7
2025-10-02 19:44:19,311 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-10-02 19:44:19,312 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-02 19:44:21,343 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-02 19:44:21,347 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-02 19:44:21,348 - freqtrade.loggers - INFO - Logfile configured
2025-10-02 19:44:21,348 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-02 19:44:21,349 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-10-02 19:44:21,349 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-02 19:44:21,350 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-02 19:44:21,350 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-10-02 19:44:21,361 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-02 19:44:21,362 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-02 19:44:21,362 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-02 19:44:21,363 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-02 19:44:21,363 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-02 19:44:21,364 - freqtrade.configuration.configuration - INFO - Using pairs ['ADA/USDT', 'SOL/USDT', 'DOGE/USDT', 'TRX/USDT']
2025-10-02 19:44:21,365 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-10-02 19:44:21,366 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-02 19:44:21,389 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-02 19:44:21,390 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-02 19:44:21,394 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-02 19:44:21,395 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-02 19:44:21,396 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-10-02 19:44:21,435 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-02 19:44:23,913 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-02 19:44:23,973 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-10-02 19:44:23,974 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-10-02 19:44:23,975 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-10-02 19:44:23,976 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-02 19:44:23,976 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-02 19:44:23,977 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-02 19:44:23,978 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-02 19:44:23,978 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-02 19:44:23,979 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-10-02 19:44:23,979 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-10-02 19:44:23,980 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-02 19:44:23,980 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-02 19:44:23,981 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-02 19:44:23,981 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-02 19:44:23,982 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-02 19:44:23,982 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-10-02 19:44:23,983 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-02 19:44:23,983 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-02 19:44:23,983 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-02 19:44:23,984 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-10-02 19:44:23,984 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-02 19:44:23,985 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-10-02 19:44:23,985 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-02 19:44:23,986 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-02 19:44:23,986 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-02 19:44:23,987 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-02 19:44:23,987 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-02 19:44:23,987 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-02 19:44:23,988 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-02 19:44:23,988 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-02 19:44:23,989 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-02 19:44:23,994 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-02 19:44:24,033 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-02 19:44:24,075 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-02 19:44:24,129 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-02 19:44:24,178 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-02 19:44:24,222 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-02 19:44:24,253 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-10-02 17:00:00 (1370 days).
2025-10-02 19:44:24,330 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-02 19:44:24,603 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-02 19:44:24,856 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-02 19:44:25,155 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-02 19:44:26,609 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-02 19:44:26,610 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-02 19:44:26,610 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-10-02 19:44:26,611 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.4
2025-10-02 19:44:26,612 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-10-02 19:44:26,612 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-10-02 19:44:26,612 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-10-02 19:44:26,613 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_strength_threshold = 0.02
2025-10-02 19:44:26,613 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 20
2025-10-02 19:44:26,613 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-10-02 19:44:26,614 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 1
2025-10-02 19:44:26,614 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-10-02 19:44:26,615 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.02
2025-10-02 19:44:26,615 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.003
2025-10-02 19:44:26,616 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_engulfing_signal_strength_threshold_max = 0.132
2025-10-02 19:44:26,616 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_engulfing_signal_strength_threshold_min = 0.071
2025-10-02 19:44:26,616 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_hammer_signal_strength_threshold_max = 0.431
2025-10-02 19:44:26,617 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_hammer_signal_strength_threshold_min = 0.254
2025-10-02 19:44:26,617 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): ml_strong_bullish_signal_strength_threshold_max = 0.5
2025-10-02 19:44:26,617 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): ml_strong_bullish_signal_strength_threshold_min = 0.5
2025-10-02 19:44:26,618 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-10-02 19:44:26,618 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-10-02 19:44:26,619 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_size_threshold = 2
2025-10-02 19:44:26,619 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_strength_threshold = 0.02
2025-10-02 19:44:26,619 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.409
2025-10-02 19:44:26,620 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.003
2025-10-02 19:44:26,620 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_engulfing_entry = False
2025-10-02 19:44:26,621 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_hammer_entry = False
2025-10-02 19:44:26,621 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_strong_bullish_entry = True
2025-10-02 19:44:26,622 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0
2025-10-02 19:44:26,622 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 0.5
2025-10-02 19:44:26,623 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-10-02 19:44:26,623 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-10-02 19:44:26,624 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 6
2025-10-02 19:44:26,624 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-10-02 19:44:26,624 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-10-02 19:44:26,625 - freqtrade.strategy.hyper - INFO - Strategy Parameter: trailing_custom_stop = False
2025-10-02 19:44:26,625 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-10-02 19:44:26,626 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-10-02 19:44:26,626 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-10-02 19:44:26,627 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = False
2025-10-02 19:44:26,627 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = False
2025-10-02 19:44:26,628 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-10-02 19:44:26,628 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-10-02 19:44:26,629 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-02 19:44:26,632 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:44:26,642 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-02 19:44:26,671 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:44:26,689 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-02 19:44:38,830 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:44:38,838 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-02 19:44:38,864 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:44:38,883 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-02 19:44:49,996 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:44:50,003 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-02 19:44:50,032 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:44:50,056 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-02 19:45:00,743 - freqtrade.data.dataprovider - INFO - Loading data for TRX/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:45:00,751 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-02 19:45:00,774 - freqtrade.data.dataprovider - INFO - Loading data for TRX/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:45:00,791 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-02 19:45:11,889 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-10-02 17:00:00 (1370 days).
2025-10-02 19:55:50,174 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-02_19-55-50.meta.json"
Result for strategy IchimokuRebondStrategy
                                                BACKTESTING REPORT                                                
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  SOL/USDT │    195 │         0.24 │          99.325 │         9.93 │ 3 days, 17:53:00 │   69     0   126  35.4 │
│  ADA/USDT │    126 │         0.33 │          46.270 │         4.63 │  7 days, 0:47:00 │   45     0    81  35.7 │
│  TRX/USDT │     48 │        -0.98 │         -77.653 │        -7.77 │  5 days, 9:46:00 │   15     0    33  31.3 │
│ DOGE/USDT │    165 │         0.47 │        -103.390 │       -10.34 │ 3 days, 19:27:00 │   55     0   110  33.3 │
│     TOTAL │    534 │         0.22 │         -35.449 │        -3.54 │ 4 days, 16:34:00 │  184     0   350  34.5 │
└───────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                              LEFT OPEN TRADES REPORT                                              
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ DOGE/USDT │      1 │         5.41 │          17.059 │         1.71 │    1 day, 8:00:00 │    1     0     0   100 │
│  ADA/USDT │      1 │        19.27 │          10.632 │         1.06 │ 241 days, 9:00:00 │    1     0     0   100 │
│     TOTAL │      2 │        12.34 │          27.691 │         2.77 │ 121 days, 8:30:00 │    2     0     0   100 │
└───────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                        ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │     534 │         0.22 │         -35.449 │        -3.54 │ 4 days, 16:34:00 │  184     0   350  34.5 │
│                 TOTAL │     534 │         0.22 │         -35.449 │        -3.54 │ 4 days, 16:34:00 │  184     0   350  34.5 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                   EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │   182 │        13.47 │        4948.747 │       494.87 │  5 days, 17:09:00 │  182     0     0   100 │
│     force_exit │     2 │        12.34 │          27.691 │         2.77 │ 121 days, 8:30:00 │    2     0     0   100 │
│      stop_loss │   350 │        -6.73 │       -5011.887 │      -501.19 │  3 days, 11:47:00 │    0     0   350     0 │
│          TOTAL │   534 │         0.22 │         -35.449 │        -3.54 │  4 days, 16:34:00 │  184     0   350  34.5 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                                MIXED TAG STATS                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_2R │    182 │        13.47 │        4948.747 │       494.87 │  5 days, 17:09:00 │  182     0     0   100 │
│ strong_bullish_rebond │     force_exit │      2 │        12.34 │          27.691 │         2.77 │ 121 days, 8:30:00 │    2     0     0   100 │
│ strong_bullish_rebond │      stop_loss │    350 │        -6.73 │       -5011.887 │      -501.19 │  3 days, 11:47:00 │    0     0   350     0 │
│                 TOTAL │                │    534 │         0.22 │         -35.449 │        -3.54 │  4 days, 16:34:00 │  184     0   350  34.5 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                          SUMMARY METRICS                           
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                            ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00              │
│ Backtesting to                │ 2025-10-02 17:00:00              │
│ Trading Mode                  │ Spot                             │
│ Max open trades               │ 3                                │
│                               │                                  │
│ Total/Daily Avg Trades        │ 534 / 0.39                       │
│ Starting balance              │ 1000 USDT                        │
│ Final balance                 │ 964.551 USDT                     │
│ Absolute profit               │ -35.449 USDT                     │
│ Total profit %                │ -3.54%                           │
│ CAGR %                        │ -0.96%                           │
│ Sortino                       │ -0.13                            │
│ Sharpe                        │ -0.02                            │
│ Calmar                        │ -0.09                            │
│ SQN                           │ -0.07                            │
│ Profit factor                 │ 0.99                             │
│ Expectancy (Ratio)            │ -0.07 (-0.00)                    │
│ Avg. daily profit             │ -0.026 USDT                      │
│ Avg. stake amount             │ 237.577 USDT                     │
│ Total trade volume            │ 254204.304 USDT                  │
│                               │                                  │
│ Best Pair                     │ SOL/USDT 9.93%                   │
│ Worst Pair                    │ DOGE/USDT -10.34%                │
│ Best trade                    │ DOGE/USDT 41.62%                 │
│ Worst trade                   │ SOL/USDT -23.49%                 │
│ Best day                      │ 89.441 USDT                      │
│ Worst day                     │ -68.38 USDT                      │
│ Days win/draw/lose            │ 158 / 960 / 246                  │
│ Min/Max/Avg. Duration Winners │ 0d 01:15 / 241d 09:00 / 6d 23:19 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:40 / 58d 10:40 / 3d 11:47  │
│ Max Consecutive Wins / Loss   │ 9 / 15                           │
│ Rejected Entry signals        │ 919                              │
│ Entry/Exit Timeouts           │ 0 / 0                            │
│                               │                                  │
│ Min balance                   │ 429.92 USDT                      │
│ Max balance                   │ 1147.096 USDT                    │
│ Max % of account underwater   │ 57.01%                           │
│ Absolute Drawdown (Account)   │ 57.01%                           │
│ Absolute Drawdown             │ 570.08 USDT                      │
│ Drawdown high                 │ -20.563 USDT                     │
│ Drawdown low                  │ -570.08 USDT                     │
│ Drawdown Start                │ 2022-01-08 17:40:00              │
│ Drawdown End                  │ 2022-12-29 00:15:00              │
│ Market change                 │ 99.71%                           │
└───────────────────────────────┴──────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-10-02 17:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃            Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    534 │         0.22 │         -35.449 │        -3.54 │ 4 days, 16:34:00 │  184     0   350  34.5 │ 570.08 USDT  57.01% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┴─────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-02T21:55:51.514861",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 9989,
  "total_daily_avg_trades": "534 / 0.39",
  "absolute_profit_usdt": -35.449,
  "total_profit_pct": -3.54,
  "cagr_pct": -0.96,
  "sortino": -0.13,
  "sharpe": -0.02,
  "calmar": -0.09,
  "sqn": -0.07,
  "max_consecutive_wins_loss": "9 / 15",
  "min_balance_usdt": 429.92,
  "max_balance_usdt": 1147.096,
  "market_change_pct": 99.71
}
```
