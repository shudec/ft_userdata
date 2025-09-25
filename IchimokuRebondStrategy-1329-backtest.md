# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 1329  
**Timestamp:** 2025-09-25 20:56:43

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 1329,
  "epochs": 100,
  "hyperopt_timerange": "20220101-20231231",
  "backtest_timerange": "20220101-20231231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20231231
```

## Backtesting Output
```
2025-09-25 18:55:23,887 - freqtrade - INFO - freqtrade 2025.7
2025-09-25 18:55:24,253 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-25 18:55:24,253 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-25 18:55:25,760 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-25 18:55:25,763 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-25 18:55:25,763 - freqtrade.loggers - INFO - Logfile configured
2025-09-25 18:55:25,764 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-25 18:55:25,764 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-25 18:55:25,765 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-25 18:55:25,765 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-25 18:55:25,765 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20231231 ...
2025-09-25 18:55:25,775 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-25 18:55:25,776 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-25 18:55:25,776 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-25 18:55:25,777 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-25 18:55:25,777 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-25 18:55:25,778 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20231231
2025-09-25 18:55:25,779 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-25 18:55:25,798 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-25 18:55:25,799 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 18:55:25,803 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-25 18:55:25,804 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-25 18:55:25,805 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-25 18:55:25,837 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-25 18:55:28,341 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-25 18:55:28,384 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-25 18:55:28,384 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-25 18:55:28,385 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-25 18:55:28,385 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-25 18:55:28,386 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-25 18:55:28,386 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-25 18:55:28,387 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-25 18:55:28,387 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-25 18:55:28,387 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-25 18:55:28,388 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-25 18:55:28,388 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-25 18:55:28,388 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-25 18:55:28,389 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-25 18:55:28,389 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-25 18:55:28,389 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-25 18:55:28,389 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-25 18:55:28,390 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-25 18:55:28,390 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-25 18:55:28,390 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-25 18:55:28,391 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-25 18:55:28,391 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-25 18:55:28,391 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-25 18:55:28,392 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-25 18:55:28,392 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-25 18:55:28,392 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-25 18:55:28,393 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-25 18:55:28,393 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-25 18:55:28,393 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-25 18:55:28,394 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-25 18:55:28,394 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-25 18:55:28,395 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 18:55:28,399 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-25 18:55:28,431 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-25 18:55:28,604 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2023-12-31 00:00:00 (729 days).
2025-09-25 18:55:30,057 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-25 18:55:30,061 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-25 18:55:30,061 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.25
2025-09-25 18:55:30,062 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-25 18:55:30,062 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-25 18:55:30,062 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-25 18:55:30,063 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 20
2025-09-25 18:55:30,063 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 1
2025-09-25 18:55:30,063 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 1
2025-09-25 18:55:30,064 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-09-25 18:55:30,064 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.001
2025-09-25 18:55:30,065 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-25 18:55:30,065 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-25 18:55:30,065 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-25 18:55:30,066 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.5
2025-09-25 18:55:30,066 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.0
2025-09-25 18:55:30,066 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 2
2025-09-25 18:55:30,067 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1
2025-09-25 18:55:30,067 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-09-25 18:55:30,068 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-25 18:55:30,068 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 4
2025-09-25 18:55:30,069 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-25 18:55:30,070 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-25 18:55:30,070 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-09-25 18:55:30,071 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-25 18:55:30,072 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = atr
2025-09-25 18:55:30,072 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-09-25 18:55:30,073 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-25 18:55:30,073 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-25 18:55:30,074 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-25 18:55:30,074 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-25 18:55:30,076 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 18:55:30,107 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 18:55:33,497 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 18:55:33,523 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 18:55:36,932 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 18:55:36,957 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 18:55:40,378 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 18:55:40,406 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 18:55:43,802 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 18:55:43,828 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 18:55:47,293 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2023-12-31 00:00:00 (729 days).
2025-09-25 18:56:42,557 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-25_18-56-42.meta.json"
Result for strategy IchimokuRebondStrategy
                                                BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      7 │         6.78 │         213.354 │        21.34 │  18 days, 6:44:00 │    4     0     3  57.1 │
│ BTC/USDT │      6 │         6.75 │         156.983 │         15.7 │ 15 days, 22:08:00 │    4     0     2  66.7 │
│ ETH/USDT │     13 │         3.65 │         154.532 │        15.45 │  9 days, 10:12:00 │    6     0     7  46.2 │
│ XRP/USDT │      7 │         1.56 │          67.453 │         6.75 │    1 day, 9:59:00 │    2     0     5  28.6 │
│ LTC/USDT │      5 │        -5.19 │        -122.402 │       -12.24 │  4 days, 13:28:00 │    0     0     5     0 │
│    TOTAL │     38 │         3.17 │         469.919 │        46.99 │  9 days, 23:12:00 │   16     0    22  42.1 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │      1 │         4.98 │          27.244 │         2.72 │ 27 days, 1:00:00 │    1     0     0   100 │
│ ETH/USDT │      1 │         3.72 │          10.193 │         1.02 │ 27 days, 1:00:00 │    1     0     0   100 │
│    TOTAL │      2 │         4.35 │          37.437 │         3.74 │ 27 days, 1:00:00 │    2     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                        ENTER TAG STATS                                                         
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │      35 │         3.29 │         441.831 │        44.18 │  8 days, 12:52:00 │   15     0    20  42.9 │
│      engulfing_rebond │       3 │         1.78 │          28.088 │         2.81 │ 26 days, 15:43:00 │    1     0     2  33.3 │
│                 TOTAL │      38 │         3.17 │         469.919 │        46.99 │  9 days, 23:12:00 │   16     0    22  42.1 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                   EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │    14 │        16.12 │         916.514 │        91.65 │ 11 days, 22:14:00 │   14     0     0   100 │
│     force_exit │     2 │         4.35 │          37.437 │         3.74 │  27 days, 1:00:00 │    2     0     0   100 │
│      stop_loss │    22 │        -5.18 │        -484.033 │        -48.4 │   7 days, 4:01:00 │    0     0    22     0 │
│          TOTAL │    38 │         3.17 │         469.919 │        46.99 │  9 days, 23:12:00 │   16     0    22  42.1 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                                MIXED TAG STATS                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_3R │     13 │        16.15 │         844.825 │        84.48 │ 11 days, 12:33:00 │   13     0     0   100 │
│      engulfing_rebond │ take_profit_3R │      1 │         15.7 │          71.690 │         7.17 │  17 days, 4:05:00 │    1     0     0   100 │
│ strong_bullish_rebond │     force_exit │      2 │         4.35 │          37.437 │         3.74 │  27 days, 1:00:00 │    2     0     0   100 │
│      engulfing_rebond │      stop_loss │      2 │        -5.17 │         -43.602 │        -4.36 │  31 days, 9:32:00 │    0     0     2     0 │
│ strong_bullish_rebond │      stop_loss │     20 │        -5.18 │        -440.431 │       -44.04 │  4 days, 17:52:00 │    0     0    20     0 │
│                 TOTAL │                │     38 │         3.17 │         469.919 │        46.99 │  9 days, 23:12:00 │   16     0    22  42.1 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                          SUMMARY METRICS                           
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                            ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00              │
│ Backtesting to                │ 2023-12-31 00:00:00              │
│ Trading Mode                  │ Spot                             │
│ Max open trades               │ 3                                │
│                               │                                  │
│ Total/Daily Avg Trades        │ 38 / 0.05                        │
│ Starting balance              │ 1000 USDT                        │
│ Final balance                 │ 1469.919 USDT                    │
│ Absolute profit               │ 469.919 USDT                     │
│ Total profit %                │ 46.99%                           │
│ CAGR %                        │ 21.27%                           │
│ Sortino                       │ 3.16                             │
│ Sharpe                        │ 0.29                             │
│ Calmar                        │ 11.14                            │
│ SQN                           │ 1.76                             │
│ Profit factor                 │ 1.97                             │
│ Expectancy (Ratio)            │ 12.37 (0.56)                     │
│ Avg. daily profit             │ 0.645 USDT                       │
│ Avg. stake amount             │ 416.264 USDT                     │
│ Total trade volume            │ 32170.226 USDT                   │
│                               │                                  │
│ Best Pair                     │ BNB/USDT 21.34%                  │
│ Worst Pair                    │ LTC/USDT -12.24%                 │
│ Best trade                    │ XRP/USDT 21.53%                  │
│ Worst trade                   │ LTC/USDT -5.19%                  │
│ Best day                      │ 145.637 USDT                     │
│ Worst day                     │ -47.464 USDT                     │
│ Days win/draw/lose            │ 13 / 652 / 19                    │
│ Min/Max/Avg. Duration Winners │ 0d 00:25 / 27d 19:45 / 13d 19:35 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:30 / 61d 14:00 / 7d 04:01  │
│ Max Consecutive Wins / Loss   │ 4 / 5                            │
│ Rejected Entry signals        │ 0                                │
│ Entry/Exit Timeouts           │ 0 / 0                            │
│                               │                                  │
│ Min balance                   │ 953.104 USDT                     │
│ Max balance                   │ 1469.919 USDT                    │
│ Max % of account underwater   │ 11.06%                           │
│ Absolute Drawdown (Account)   │ 11.06%                           │
│ Absolute Drawdown             │ 134.784 USDT                     │
│ Drawdown high                 │ 218.707 USDT                     │
│ Drawdown low                  │ 83.923 USDT                      │
│ Drawdown Start                │ 2023-01-14 01:15:00              │
│ Drawdown End                  │ 2023-07-07 00:00:00              │
│ Market change                 │ -32.53%                          │
└───────────────────────────────┴──────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2023-12-31 00:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     38 │         3.17 │         469.919 │        46.99 │ 9 days, 23:12:00 │   16     0    22  42.1 │ 134.784 USDT  11.06% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-25T20:56:43.719842",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 1329,
  "total_daily_avg_trades": "38 / 0.05",
  "absolute_profit_usdt": 469.919,
  "total_profit_pct": 46.99,
  "cagr_pct": 21.27,
  "sortino": 3.16,
  "sharpe": 0.29,
  "calmar": 11.14,
  "sqn": 1.76,
  "max_consecutive_wins_loss": "4 / 5",
  "min_balance_usdt": 953.104,
  "max_balance_usdt": 1469.919,
  "market_change_pct": -32.53
}
```
