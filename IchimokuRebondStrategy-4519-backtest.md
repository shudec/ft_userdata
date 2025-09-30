# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 4519  
**Timestamp:** 2025-09-30 22:38:33

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 4519,
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
2025-09-30 20:36:58,881 - freqtrade - INFO - freqtrade 2025.7
2025-09-30 20:36:59,324 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-30 20:36:59,324 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-30 20:37:01,440 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-30 20:37:01,443 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-30 20:37:01,443 - freqtrade.loggers - INFO - Logfile configured
2025-09-30 20:37:01,444 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-30 20:37:01,444 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-30 20:37:01,445 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-30 20:37:01,445 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-30 20:37:01,445 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20241231 ...
2025-09-30 20:37:01,462 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-30 20:37:01,463 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-30 20:37:01,463 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-30 20:37:01,464 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-09-30 20:37:01,464 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-30 20:37:01,465 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-30 20:37:01,465 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20241231
2025-09-30 20:37:01,467 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-30 20:37:01,486 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-30 20:37:01,487 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-30 20:37:01,490 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-30 20:37:01,491 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-30 20:37:01,491 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-30 20:37:01,523 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-30 20:37:04,197 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-30 20:37:04,251 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-30 20:37:04,251 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-30 20:37:04,252 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-30 20:37:04,253 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-30 20:37:04,254 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-30 20:37:04,254 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-30 20:37:04,255 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-30 20:37:04,255 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-30 20:37:04,255 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-30 20:37:04,256 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-30 20:37:04,256 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-30 20:37:04,257 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-30 20:37:04,257 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-30 20:37:04,257 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-30 20:37:04,258 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-30 20:37:04,258 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-30 20:37:04,259 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-30 20:37:04,259 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-30 20:37:04,260 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-30 20:37:04,260 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-30 20:37:04,260 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-30 20:37:04,261 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-30 20:37:04,261 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-30 20:37:04,262 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-30 20:37:04,262 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-30 20:37:04,263 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-30 20:37:04,263 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-30 20:37:04,263 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-30 20:37:04,264 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-30 20:37:04,264 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-30 20:37:04,265 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-30 20:37:04,271 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-30 20:37:04,308 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-30 20:37:04,523 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2024-12-31 00:00:00 (1095 days).
2025-09-30 20:37:06,401 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-30 20:37:06,406 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-30 20:37:06,407 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.4
2025-09-30 20:37:06,407 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-30 20:37:06,408 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-30 20:37:06,408 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-30 20:37:06,409 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_strength_threshold = 0.02
2025-09-30 20:37:06,409 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 5
2025-09-30 20:37:06,409 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-09-30 20:37:06,410 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 1
2025-09-30 20:37:06,410 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-09-30 20:37:06,411 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.02
2025-09-30 20:37:06,411 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.003
2025-09-30 20:37:06,411 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_signal_strength_threshold_max = 0.814
2025-09-30 20:37:06,412 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_signal_strength_threshold_min = 0.119
2025-09-30 20:37:06,412 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-30 20:37:06,413 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-30 20:37:06,413 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_size_threshold = 2
2025-09-30 20:37:06,413 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_strength_threshold = 0.02
2025-09-30 20:37:06,414 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.409
2025-09-30 20:37:06,414 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.003
2025-09-30 20:37:06,415 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_engulfing_entry = False
2025-09-30 20:37:06,415 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_hammer_entry = True
2025-09-30 20:37:06,416 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_strong_bullish_entry = False
2025-09-30 20:37:06,416 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1
2025-09-30 20:37:06,417 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 0.5
2025-09-30 20:37:06,417 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-09-30 20:37:06,418 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-30 20:37:06,418 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 6
2025-09-30 20:37:06,419 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-30 20:37:06,419 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-30 20:37:06,420 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-09-30 20:37:06,420 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-30 20:37:06,421 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-30 20:37:06,421 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = False
2025-09-30 20:37:06,422 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = False
2025-09-30 20:37:06,422 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-30 20:37:06,423 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-30 20:37:06,423 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-30 20:37:06,426 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:37:06,469 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:37:14,229 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:37:14,264 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:37:22,094 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:37:22,128 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:37:29,979 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:37:30,018 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:37:37,765 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:37:37,800 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:37:45,651 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2024-12-31 00:00:00 (1095 days).
2025-09-30 20:38:32,556 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-30_20-38-32.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │     42 │         1.04 │         120.642 │        12.06 │          9:45:00 │   25     0    17  59.5 │
│ LTC/USDT │     43 │          1.3 │          72.089 │         7.21 │  1 day, 13:28:00 │   25     0    18  58.1 │
│ BTC/USDT │     39 │        -0.11 │          13.052 │         1.31 │   1 day, 8:31:00 │   18     0    21  46.2 │
│ XRP/USDT │     36 │        -1.19 │          -2.952 │         -0.3 │ 2 days, 16:06:00 │   18     0    18  50.0 │
│ BNB/USDT │     20 │         0.05 │          -4.840 │        -0.48 │  1 day, 17:26:00 │   10     0    10  50.0 │
│    TOTAL │    180 │          0.3 │         197.992 │         19.8 │  1 day, 11:42:00 │   96     0    84  53.3 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │      1 │       -11.98 │         -14.213 │        -1.42 │ 20 days, 1:00:00 │    0     0     1     0 │
│    TOTAL │      1 │       -11.98 │         -14.213 │        -1.42 │ 20 days, 1:00:00 │    0     0     1     0 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                   ENTER TAG STATS                                                    
┏━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ hammer_rebond │     180 │          0.3 │         197.992 │         19.8 │ 1 day, 11:42:00 │   96     0    84  53.3 │
│         TOTAL │     180 │          0.3 │         197.992 │         19.8 │ 1 day, 11:42:00 │   96     0    84  53.3 │
└───────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │    96 │         4.71 │        1347.151 │       134.72 │  1 day, 12:31:00 │   96     0     0   100 │
│     force_exit │     1 │       -11.98 │         -14.213 │        -1.42 │ 20 days, 1:00:00 │    0     0     1     0 │
│      stop_loss │    83 │        -4.66 │       -1134.946 │      -113.49 │   1 day, 5:23:00 │    0     0    83     0 │
│          TOTAL │   180 │          0.3 │         197.992 │         19.8 │  1 day, 11:42:00 │   96     0    84  53.3 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                            MIXED TAG STATS                                                            
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ hammer_rebond │ take_profit_1R │     96 │         4.71 │        1347.151 │       134.72 │  1 day, 12:31:00 │   96     0     0   100 │
│ hammer_rebond │     force_exit │      1 │       -11.98 │         -14.213 │        -1.42 │ 20 days, 1:00:00 │    0     0     1     0 │
│ hammer_rebond │      stop_loss │     83 │        -4.66 │       -1134.946 │      -113.49 │   1 day, 5:23:00 │    0     0    83     0 │
│         TOTAL │                │    180 │          0.3 │         197.992 │         19.8 │  1 day, 11:42:00 │   96     0    84  53.3 │
└───────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00             │
│ Backtesting to                │ 2024-12-31 00:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 180 / 0.16                      │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 1197.992 USDT                   │
│ Absolute profit               │ 197.992 USDT                    │
│ Total profit %                │ 19.80%                          │
│ CAGR %                        │ 6.21%                           │
│ Sortino                       │ 0.44                            │
│ Sharpe                        │ 0.22                            │
│ Calmar                        │ 2.06                            │
│ SQN                           │ 0.92                            │
│ Profit factor                 │ 1.17                            │
│ Expectancy (Ratio)            │ 1.10 (0.08)                     │
│ Avg. daily profit             │ 0.181 USDT                      │
│ Avg. stake amount             │ 362.782 USDT                    │
│ Total trade volume            │ 131061.548 USDT                 │
│                               │                                 │
│ Best Pair                     │ ETH/USDT 12.06%                 │
│ Worst Pair                    │ BNB/USDT -0.48%                 │
│ Best trade                    │ XRP/USDT 19.55%                 │
│ Worst trade                   │ XRP/USDT -43.10%                │
│ Best day                      │ 53.67 USDT                      │
│ Worst day                     │ -42.642 USDT                    │
│ Days win/draw/lose            │ 60 / 974 / 56                   │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 23d 21:05 / 1d 12:31 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 34d 23:40 / 1d 10:46 │
│ Max Consecutive Wins / Loss   │ 12 / 8                          │
│ Rejected Entry signals        │ 88                              │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 832.033 USDT                    │
│ Max balance                   │ 1307.584 USDT                   │
│ Max % of account underwater   │ 16.80%                          │
│ Absolute Drawdown (Account)   │ 16.80%                          │
│ Absolute Drawdown             │ 167.967 USDT                    │
│ Drawdown high                 │ -15.838 USDT                    │
│ Drawdown low                  │ -167.967 USDT                   │
│ Drawdown Start                │ 2022-01-07 15:50:00             │
│ Drawdown End                  │ 2022-06-15 09:20:00             │
│ Market change                 │ 46.34%                          │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2024-12-31 00:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    180 │         0.30 │         197.992 │         19.8 │ 1 day, 11:42:00 │   96     0    84  53.3 │ 167.967 USDT  16.80% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-30T22:38:33.703543",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 4519,
  "total_daily_avg_trades": "180 / 0.16",
  "absolute_profit_usdt": 197.992,
  "total_profit_pct": 19.8,
  "cagr_pct": 6.21,
  "sortino": 0.44,
  "sharpe": 0.22,
  "calmar": 2.06,
  "sqn": 0.92,
  "max_consecutive_wins_loss": "12 / 8",
  "min_balance_usdt": 832.033,
  "max_balance_usdt": 1307.584,
  "market_change_pct": 46.34
}
```
