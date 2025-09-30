# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 4194  
**Timestamp:** 2025-09-30 22:08:00

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 4194,
  "epochs": 100,
  "hyperopt_timerange": "20220101-20231231",
  "backtest_timerange": "20220101-20241231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20241231 --export trades
```

## Backtesting Output
```
2025-09-30 20:00:14,575 - freqtrade - INFO - freqtrade 2025.7
2025-09-30 20:00:14,910 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-30 20:00:14,911 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-30 20:00:16,435 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-30 20:00:16,439 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-30 20:00:16,439 - freqtrade.loggers - INFO - Logfile configured
2025-09-30 20:00:16,440 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-30 20:00:16,440 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-30 20:00:16,441 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-30 20:00:16,441 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-30 20:00:16,441 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20241231 ...
2025-09-30 20:00:16,449 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-30 20:00:16,450 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-30 20:00:16,451 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-30 20:00:16,452 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-09-30 20:00:16,452 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-30 20:00:16,452 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-30 20:00:16,453 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20241231
2025-09-30 20:00:16,454 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-30 20:00:16,475 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-30 20:00:16,476 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-30 20:00:16,480 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-30 20:00:16,481 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-30 20:00:16,481 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-30 20:00:16,518 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-30 20:00:19,199 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-30 20:00:19,250 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-30 20:00:19,250 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-30 20:00:19,251 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-30 20:00:19,252 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-30 20:00:19,252 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-30 20:00:19,252 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-30 20:00:19,253 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-30 20:00:19,253 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-30 20:00:19,254 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-30 20:00:19,254 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-30 20:00:19,254 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-30 20:00:19,255 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-30 20:00:19,255 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-30 20:00:19,255 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-30 20:00:19,256 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-30 20:00:19,256 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-30 20:00:19,256 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-30 20:00:19,257 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-30 20:00:19,257 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-30 20:00:19,257 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-30 20:00:19,258 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-30 20:00:19,258 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-30 20:00:19,258 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-30 20:00:19,259 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-30 20:00:19,259 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-30 20:00:19,259 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-30 20:00:19,260 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-30 20:00:19,260 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-30 20:00:19,260 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-30 20:00:19,261 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-30 20:00:19,261 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-30 20:00:19,266 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-30 20:00:19,301 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-30 20:00:19,518 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2024-12-31 00:00:00 (1095 days).
2025-09-30 20:00:21,379 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-30 20:00:21,383 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-30 20:00:21,383 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.4
2025-09-30 20:00:21,384 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-30 20:00:21,384 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-30 20:00:21,385 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-30 20:00:21,385 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_strength_threshold = 0.02
2025-09-30 20:00:21,386 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 5
2025-09-30 20:00:21,386 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-09-30 20:00:21,386 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 1
2025-09-30 20:00:21,387 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-09-30 20:00:21,387 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.02
2025-09-30 20:00:21,388 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.003
2025-09-30 20:00:21,388 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_signal_strength_threshold_max = 0.371
2025-09-30 20:00:21,388 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_signal_strength_threshold_min = 0.076
2025-09-30 20:00:21,389 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-30 20:00:21,389 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-30 20:00:21,389 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_size_threshold = 2
2025-09-30 20:00:21,390 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_strength_threshold = 0.02
2025-09-30 20:00:21,390 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.409
2025-09-30 20:00:21,391 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.003
2025-09-30 20:00:21,391 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_engulfing_entry = False
2025-09-30 20:00:21,391 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_hammer_entry = True
2025-09-30 20:00:21,392 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_strong_bullish_entry = False
2025-09-30 20:00:21,392 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1.5
2025-09-30 20:00:21,393 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 0.5
2025-09-30 20:00:21,394 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-09-30 20:00:21,394 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-30 20:00:21,395 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 6
2025-09-30 20:00:21,396 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-30 20:00:21,396 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-30 20:00:21,397 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = False
2025-09-30 20:00:21,397 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-30 20:00:21,398 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-30 20:00:21,398 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = False
2025-09-30 20:00:21,399 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = False
2025-09-30 20:00:21,399 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-30 20:00:21,399 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-30 20:00:21,400 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-30 20:00:21,403 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:00:21,442 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:00:29,030 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:00:29,085 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:00:36,690 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:00:36,742 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:00:44,355 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:00:44,406 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:00:51,950 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:00:52,001 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:00:59,662 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2024-12-31 00:00:00 (1095 days).
2025-09-30 20:07:59,148 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-30_20-07-59.meta.json"
Result for strategy IchimokuRebondStrategy
                                                BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │     11 │        17.14 │         249.320 │        24.93 │ 85 days, 12:00:00 │    1     0    10   9.1 │
│ LTC/USDT │     10 │        10.19 │         147.848 │        14.78 │  95 days, 2:21:00 │    1     0     9  10.0 │
│ BNB/USDT │     12 │        -1.39 │         -37.171 │        -3.72 │ 25 days, 19:14:00 │    1     0    11   8.3 │
│ BTC/USDT │     23 │        -3.32 │        -148.781 │       -14.88 │ 12 days, 17:30:00 │    0     0    23     0 │
│ XRP/USDT │     28 │        -2.93 │        -160.765 │       -16.08 │   8 days, 6:26:00 │    0     0    28     0 │
│    TOTAL │     84 │         1.38 │          50.451 │         5.05 │ 32 days, 10:41:00 │    3     0    81   3.6 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                              LEFT OPEN TRADES REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃       Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │      1 │       222.07 │         359.859 │        35.99 │ 901 days, 10:00:00 │    1     0     0   100 │
│ LTC/USDT │      1 │       123.93 │         196.029 │         19.6 │  931 days, 6:00:00 │    1     0     0   100 │
│ BNB/USDT │      1 │         29.5 │          38.681 │         3.87 │   90 days, 3:00:00 │    1     0     0   100 │
│    TOTAL │      3 │       125.17 │         594.569 │        59.46 │ 640 days, 22:20:00 │    3     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────────┴────────────────────────┘
                                                    ENTER TAG STATS                                                     
┏━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ hammer_rebond │      84 │         1.38 │          50.451 │         5.05 │ 32 days, 10:41:00 │    3     0    81   3.6 │
│         TOTAL │      84 │         1.38 │          50.451 │         5.05 │ 32 days, 10:41:00 │    3     0    81   3.6 │
└───────────────┴─────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃       Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  force_exit │     3 │       125.17 │         594.569 │        59.46 │ 640 days, 22:20:00 │    3     0     0   100 │
│   stop_loss │    81 │        -3.21 │        -544.119 │       -54.41 │   9 days, 21:48:00 │    0     0    81     0 │
│       TOTAL │    84 │         1.38 │          50.451 │         5.05 │  32 days, 10:41:00 │    3     0    81   3.6 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────────┴────────────────────────┘
                                                           MIXED TAG STATS                                                            
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃       Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ hammer_rebond │  force_exit │      3 │       125.17 │         594.569 │        59.46 │ 640 days, 22:20:00 │    3     0     0   100 │
│ hammer_rebond │   stop_loss │     81 │        -3.21 │        -544.119 │       -54.41 │   9 days, 21:48:00 │    0     0    81     0 │
│         TOTAL │             │     84 │         1.38 │          50.451 │         5.05 │  32 days, 10:41:00 │    3     0    81   3.6 │
└───────────────┴─────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────────┴────────────────────────┘
                            SUMMARY METRICS                            
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                               ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00                 │
│ Backtesting to                │ 2024-12-31 00:00:00                 │
│ Trading Mode                  │ Spot                                │
│ Max open trades               │ 3                                   │
│                               │                                     │
│ Total/Daily Avg Trades        │ 84 / 0.08                           │
│ Starting balance              │ 1000 USDT                           │
│ Final balance                 │ 1050.451 USDT                       │
│ Absolute profit               │ 50.451 USDT                         │
│ Total profit %                │ 5.05%                               │
│ CAGR %                        │ 1.65%                               │
│ Sortino                       │ 0.16                                │
│ Sharpe                        │ 0.02                                │
│ Calmar                        │ 0.16                                │
│ SQN                           │ 0.12                                │
│ Profit factor                 │ 1.09                                │
│ Expectancy (Ratio)            │ 0.60 (0.09)                         │
│ Avg. daily profit             │ 0.046 USDT                          │
│ Avg. stake amount             │ 257.711 USDT                        │
│ Total trade volume            │ 43432.663 USDT                      │
│                               │                                     │
│ Best Pair                     │ ETH/USDT 24.93%                     │
│ Worst Pair                    │ XRP/USDT -16.08%                    │
│ Best trade                    │ ETH/USDT 222.07%                    │
│ Worst trade                   │ BNB/USDT -13.27%                    │
│ Best day                      │ 594.569 USDT                        │
│ Worst day                     │ -44.21 USDT                         │
│ Days win/draw/lose            │ 1 / 1037 / 52                       │
│ Min/Max/Avg. Duration Winners │ 90d 03:00 / 931d 06:00 / 640d 22:20 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 74d 07:30 / 9d 21:48     │
│ Max Consecutive Wins / Loss   │ 3 / 81                              │
│ Rejected Entry signals        │ 1573                                │
│ Entry/Exit Timeouts           │ 0 / 0                               │
│                               │                                     │
│ Min balance                   │ 455.881 USDT                        │
│ Max balance                   │ 1050.451 USDT                       │
│ Max % of account underwater   │ 54.41%                              │
│ Absolute Drawdown (Account)   │ 54.41%                              │
│ Absolute Drawdown             │ 544.119 USDT                        │
│ Drawdown high                 │ -1.54 USDT                          │
│ Drawdown low                  │ -544.119 USDT                       │
│ Drawdown Start                │ 2022-01-07 05:00:00                 │
│ Drawdown End                  │ 2024-10-01 20:05:00                 │
│ Market change                 │ 46.34%                              │
└───────────────────────────────┴─────────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2024-12-31 00:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                    
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     84 │         1.38 │          50.451 │         5.05 │ 32 days, 10:41:00 │    3     0    81   3.6 │ 544.119 USDT  54.41% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-30T22:08:00.235473",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 4194,
  "total_daily_avg_trades": "84 / 0.08",
  "absolute_profit_usdt": 50.451,
  "total_profit_pct": 5.05,
  "cagr_pct": 1.65,
  "sortino": 0.16,
  "sharpe": 0.02,
  "calmar": 0.16,
  "sqn": 0.12,
  "max_consecutive_wins_loss": "3 / 81",
  "min_balance_usdt": 455.881,
  "max_balance_usdt": 1050.451,
  "market_change_pct": 46.34
}
```
