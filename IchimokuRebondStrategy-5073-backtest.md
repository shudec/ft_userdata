# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 5073  
**Timestamp:** 2025-10-02 21:27:50

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
  "random_state": 5073,
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
2025-10-02 19:13:47,943 - freqtrade - INFO - freqtrade 2025.7
2025-10-02 19:13:48,335 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-10-02 19:13:48,335 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-02 19:13:50,095 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-02 19:13:50,098 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-02 19:13:50,098 - freqtrade.loggers - INFO - Logfile configured
2025-10-02 19:13:50,099 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-02 19:13:50,099 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-10-02 19:13:50,100 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-02 19:13:50,100 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-02 19:13:50,100 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-10-02 19:13:50,108 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-02 19:13:50,109 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-02 19:13:50,109 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-02 19:13:50,110 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-02 19:13:50,110 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-02 19:13:50,111 - freqtrade.configuration.configuration - INFO - Using pairs ['ADA/USDT', 'SOL/USDT', 'DOGE/USDT', 'TRX/USDT']
2025-10-02 19:13:50,111 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-10-02 19:13:50,112 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-02 19:13:50,133 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-02 19:13:50,134 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-02 19:13:50,139 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-02 19:13:50,140 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-02 19:13:50,140 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-10-02 19:13:50,175 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-02 19:13:52,631 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-02 19:13:52,676 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-10-02 19:13:52,677 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-10-02 19:13:52,678 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-10-02 19:13:52,678 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-02 19:13:52,679 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-02 19:13:52,679 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-02 19:13:52,680 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-02 19:13:52,680 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-02 19:13:52,680 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-10-02 19:13:52,681 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-10-02 19:13:52,681 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-02 19:13:52,681 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-02 19:13:52,682 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-02 19:13:52,682 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-02 19:13:52,682 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-02 19:13:52,683 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-10-02 19:13:52,683 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-02 19:13:52,683 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-02 19:13:52,684 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-02 19:13:52,684 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-10-02 19:13:52,685 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-02 19:13:52,685 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-10-02 19:13:52,685 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-02 19:13:52,686 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-02 19:13:52,686 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-02 19:13:52,686 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-02 19:13:52,687 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-02 19:13:52,687 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-02 19:13:52,687 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-02 19:13:52,688 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-02 19:13:52,688 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-02 19:13:52,693 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-02 19:13:52,720 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-02 19:13:52,753 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-02 19:13:52,807 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-02 19:13:52,851 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-02 19:13:52,894 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-02 19:13:52,927 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-10-02 17:00:00 (1370 days).
2025-10-02 19:13:53,005 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-02 19:13:53,246 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-02 19:13:53,497 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-02 19:13:53,756 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-02 19:13:54,906 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-02 19:13:54,907 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-02 19:13:54,907 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-10-02 19:13:54,908 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.4
2025-10-02 19:13:54,908 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-10-02 19:13:54,909 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-10-02 19:13:54,909 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-10-02 19:13:54,909 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_strength_threshold = 0.02
2025-10-02 19:13:54,910 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 20
2025-10-02 19:13:54,910 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-10-02 19:13:54,910 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 1
2025-10-02 19:13:54,911 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-10-02 19:13:54,911 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.02
2025-10-02 19:13:54,911 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.003
2025-10-02 19:13:54,911 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_engulfing_signal_strength_threshold_max = 0.132
2025-10-02 19:13:54,912 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_engulfing_signal_strength_threshold_min = 0.071
2025-10-02 19:13:54,912 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_hammer_signal_strength_threshold_max = 0.431
2025-10-02 19:13:54,912 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_hammer_signal_strength_threshold_min = 0.254
2025-10-02 19:13:54,913 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): ml_strong_bullish_signal_strength_threshold_max = 0.5
2025-10-02 19:13:54,913 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): ml_strong_bullish_signal_strength_threshold_min = 0.5
2025-10-02 19:13:54,913 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-10-02 19:13:54,914 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-10-02 19:13:54,914 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_size_threshold = 2
2025-10-02 19:13:54,914 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_strength_threshold = 0.02
2025-10-02 19:13:54,914 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.409
2025-10-02 19:13:54,915 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.003
2025-10-02 19:13:54,915 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_engulfing_entry = False
2025-10-02 19:13:54,915 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_hammer_entry = False
2025-10-02 19:13:54,916 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_strong_bullish_entry = True
2025-10-02 19:13:54,916 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0
2025-10-02 19:13:54,917 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 0.5
2025-10-02 19:13:54,917 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-10-02 19:13:54,917 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-10-02 19:13:54,918 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 6
2025-10-02 19:13:54,918 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-10-02 19:13:54,918 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-10-02 19:13:54,919 - freqtrade.strategy.hyper - INFO - Strategy Parameter: trailing_custom_stop = False
2025-10-02 19:13:54,919 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = False
2025-10-02 19:13:54,920 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-10-02 19:13:54,920 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-10-02 19:13:54,920 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = False
2025-10-02 19:13:54,921 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = False
2025-10-02 19:13:54,921 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-10-02 19:13:54,922 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-10-02 19:13:54,922 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-02 19:13:54,925 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:13:54,934 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-02 19:13:54,964 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:13:54,981 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-02 19:14:05,971 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:14:05,978 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-02 19:14:06,001 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:14:06,020 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-02 19:14:16,683 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:14:16,691 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-02 19:14:16,713 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:14:16,731 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-02 19:14:27,427 - freqtrade.data.dataprovider - INFO - Loading data for TRX/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:14:27,435 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-02 19:14:27,459 - freqtrade.data.dataprovider - INFO - Loading data for TRX/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:14:27,477 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-02 19:14:38,337 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-10-02 17:00:00 (1370 days).
2025-10-02 19:27:49,236 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-02_19-27-49.meta.json"
Result for strategy IchimokuRebondStrategy
                                                 BACKTESTING REPORT                                                 
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃       Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  SOL/USDT │     26 │        74.12 │        2137.117 │       213.71 │   49 days, 9:27:00 │    1     0    25   3.8 │
│  TRX/USDT │      8 │        65.46 │         648.076 │        64.81 │ 152 days, 17:49:00 │    1     0     7  12.5 │
│  ADA/USDT │     20 │         5.58 │         -85.385 │        -8.54 │  65 days, 13:22:00 │    1     0    19   5.0 │
│ DOGE/USDT │     10 │        -8.37 │        -106.974 │        -10.7 │  19 days, 22:22:00 │    0     0    10     0 │
│     TOTAL │     64 │        38.73 │        2592.834 │       259.28 │  62 days, 18:14:00 │    3     0    61   4.7 │
└───────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────────┴────────────────────────┘
                                              LEFT OPEN TRADES REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃        Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ SOL/USDT │      1 │      2139.51 │        2447.908 │       244.79 │  1006 days, 1:00:00 │    1     0     0   100 │
│ TRX/USDT │      1 │       581.19 │         734.966 │         73.5 │ 1052 days, 17:00:00 │    1     0     0   100 │
│ ADA/USDT │      1 │       250.83 │         118.999 │         11.9 │   845 days, 8:00:00 │    1     0     0   100 │
│    TOTAL │      3 │       990.51 │        3301.874 │       330.19 │   968 days, 0:40:00 │    3     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────────┴────────────────────────┘
                                                        ENTER TAG STATS                                                         
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │      64 │        38.73 │        2592.834 │       259.28 │ 62 days, 18:14:00 │    3     0    61   4.7 │
│                 TOTAL │      64 │        38.73 │        2592.834 │       259.28 │ 62 days, 18:14:00 │    3     0    61   4.7 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  force_exit │     3 │       990.51 │        3301.874 │       330.19 │ 968 days, 0:40:00 │    3     0     0   100 │
│   stop_loss │    61 │        -8.08 │        -709.039 │        -70.9 │  18 days, 5:44:00 │    0     0    61     0 │
│       TOTAL │    64 │        38.73 │        2592.834 │       259.28 │ 62 days, 18:14:00 │    3     0    61   4.7 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                               MIXED TAG STATS                                                               
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │  force_exit │      3 │       990.51 │        3301.874 │       330.19 │ 968 days, 0:40:00 │    3     0     0   100 │
│ strong_bullish_rebond │   stop_loss │     61 │        -8.08 │        -709.039 │        -70.9 │  18 days, 5:44:00 │    0     0    61     0 │
│                 TOTAL │             │     64 │        38.73 │        2592.834 │       259.28 │ 62 days, 18:14:00 │    3     0    61   4.7 │
└───────────────────────┴─────────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                             SUMMARY METRICS                             
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                                 ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00                   │
│ Backtesting to                │ 2025-10-02 17:00:00                   │
│ Trading Mode                  │ Spot                                  │
│ Max open trades               │ 3                                     │
│                               │                                       │
│ Total/Daily Avg Trades        │ 64 / 0.05                             │
│ Starting balance              │ 1000 USDT                             │
│ Final balance                 │ 3592.834 USDT                         │
│ Absolute profit               │ 2592.834 USDT                         │
│ Total profit %                │ 259.28%                               │
│ CAGR %                        │ 40.60%                                │
│ Sortino                       │ 8.25                                  │
│ Sharpe                        │ 0.11                                  │
│ Calmar                        │ 5.10                                  │
│ SQN                           │ 1.01                                  │
│ Profit factor                 │ 4.66                                  │
│ Expectancy (Ratio)            │ 40.51 (3.49)                          │
│ Avg. daily profit             │ 1.893 USDT                            │
│ Avg. stake amount             │ 163.042 USDT                          │
│ Total trade volume            │ 23509.218 USDT                        │
│                               │                                       │
│ Best Pair                     │ SOL/USDT 213.71%                      │
│ Worst Pair                    │ DOGE/USDT -10.70%                     │
│ Best trade                    │ SOL/USDT 2139.51%                     │
│ Worst trade                   │ SOL/USDT -23.49%                      │
│ Best day                      │ 3301.874 USDT                         │
│ Worst day                     │ -58.501 USDT                          │
│ Days win/draw/lose            │ 1 / 1318 / 45                         │
│ Min/Max/Avg. Duration Winners │ 845d 08:00 / 1052d 17:00 / 968d 00:40 │
│ Min/Max/Avg. Duration Losers  │ 0d 03:30 / 156d 12:20 / 18d 05:44     │
│ Max Consecutive Wins / Loss   │ 3 / 61                                │
│ Rejected Entry signals        │ 4908                                  │
│ Entry/Exit Timeouts           │ 0 / 0                                 │
│                               │                                       │
│ Min balance                   │ 290.961 USDT                          │
│ Max balance                   │ 3592.834 USDT                         │
│ Max % of account underwater   │ 70.90%                                │
│ Absolute Drawdown (Account)   │ 70.90%                                │
│ Absolute Drawdown             │ 709.039 USDT                          │
│ Drawdown high                 │ -20.563 USDT                          │
│ Drawdown low                  │ -709.039 USDT                         │
│ Drawdown Start                │ 2022-01-08 17:40:00                   │
│ Drawdown End                  │ 2023-06-10 04:20:00                   │
│ Market change                 │ 99.71%                                │
└───────────────────────────────┴───────────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-10-02 17:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                    
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     64 │        38.73 │        2592.834 │       259.28 │ 62 days, 18:14:00 │    3     0    61   4.7 │ 709.039 USDT  70.90% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-02T21:27:50.501046",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 5073,
  "total_daily_avg_trades": "64 / 0.05",
  "absolute_profit_usdt": 2592.834,
  "total_profit_pct": 259.28,
  "cagr_pct": 40.6,
  "sortino": 8.25,
  "sharpe": 0.11,
  "calmar": 5.1,
  "sqn": 1.01,
  "max_consecutive_wins_loss": "3 / 61",
  "min_balance_usdt": 290.961,
  "max_balance_usdt": 3592.834,
  "market_change_pct": 99.71
}
```
