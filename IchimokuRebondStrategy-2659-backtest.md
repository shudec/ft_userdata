# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 2659  
**Timestamp:** 2025-09-30 22:31:49

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 2659,
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
2025-09-30 20:30:53,475 - freqtrade - INFO - freqtrade 2025.7
2025-09-30 20:30:53,849 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-30 20:30:53,849 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-30 20:30:55,345 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-30 20:30:55,348 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-30 20:30:55,349 - freqtrade.loggers - INFO - Logfile configured
2025-09-30 20:30:55,349 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-30 20:30:55,349 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-30 20:30:55,350 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-30 20:30:55,350 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-30 20:30:55,350 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20241231 ...
2025-09-30 20:30:55,359 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-30 20:30:55,360 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-30 20:30:55,361 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-30 20:30:55,361 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-09-30 20:30:55,362 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-30 20:30:55,362 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-30 20:30:55,363 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20241231
2025-09-30 20:30:55,364 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-30 20:30:55,385 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-30 20:30:55,386 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-30 20:30:55,390 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-30 20:30:55,391 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-30 20:30:55,391 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-30 20:30:55,424 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-30 20:30:58,133 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-30 20:30:58,188 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-30 20:30:58,189 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-30 20:30:58,191 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-30 20:30:58,191 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-30 20:30:58,192 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-30 20:30:58,193 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-30 20:30:58,193 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-30 20:30:58,194 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-30 20:30:58,194 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-30 20:30:58,195 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-30 20:30:58,195 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-30 20:30:58,196 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-30 20:30:58,196 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-30 20:30:58,197 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-30 20:30:58,198 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-30 20:30:58,198 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-30 20:30:58,199 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-30 20:30:58,199 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-30 20:30:58,200 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-30 20:30:58,201 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-30 20:30:58,201 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-30 20:30:58,202 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-30 20:30:58,202 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-30 20:30:58,203 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-30 20:30:58,203 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-30 20:30:58,204 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-30 20:30:58,205 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-30 20:30:58,205 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-30 20:30:58,206 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-30 20:30:58,206 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-30 20:30:58,207 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-30 20:30:58,214 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-30 20:30:58,254 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-30 20:30:58,487 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2024-12-31 00:00:00 (1095 days).
2025-09-30 20:31:00,424 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-30 20:31:00,425 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-30 20:31:00,426 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.4
2025-09-30 20:31:00,426 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-30 20:31:00,427 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-30 20:31:00,427 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-30 20:31:00,427 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_strength_threshold = 0.02
2025-09-30 20:31:00,428 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 5
2025-09-30 20:31:00,428 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-09-30 20:31:00,428 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 1
2025-09-30 20:31:00,429 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-09-30 20:31:00,429 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.02
2025-09-30 20:31:00,429 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.003
2025-09-30 20:31:00,429 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_signal_strength_threshold_max = 0.119
2025-09-30 20:31:00,430 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_signal_strength_threshold_min = 0.098
2025-09-30 20:31:00,430 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-30 20:31:00,430 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-30 20:31:00,431 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_size_threshold = 2
2025-09-30 20:31:00,431 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_strength_threshold = 0.02
2025-09-30 20:31:00,431 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.409
2025-09-30 20:31:00,432 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.003
2025-09-30 20:31:00,432 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_engulfing_entry = False
2025-09-30 20:31:00,432 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_hammer_entry = True
2025-09-30 20:31:00,433 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_strong_bullish_entry = False
2025-09-30 20:31:00,433 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0
2025-09-30 20:31:00,433 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 0.5
2025-09-30 20:31:00,434 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-09-30 20:31:00,434 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-30 20:31:00,434 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 6
2025-09-30 20:31:00,435 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-30 20:31:00,435 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-30 20:31:00,435 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-09-30 20:31:00,436 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-30 20:31:00,436 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-30 20:31:00,436 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = False
2025-09-30 20:31:00,437 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = False
2025-09-30 20:31:00,437 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-30 20:31:00,437 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-30 20:31:00,438 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-30 20:31:00,440 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:31:00,472 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:31:08,050 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:31:08,086 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:31:15,622 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:31:15,673 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:31:23,302 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:31:23,331 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:31:31,014 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:31:31,049 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 20:31:38,731 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2024-12-31 00:00:00 (1095 days).
2025-09-30 20:31:48,591 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-30_20-31-48.meta.json"
Result for strategy IchimokuRebondStrategy
                                              BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ LTC/USDT │     31 │         0.38 │          43.769 │         4.38 │        7:18:00 │   16     0    15  51.6 │
│ ETH/USDT │     13 │          0.5 │          31.750 │         3.18 │        4:10:00 │    8     0     5  61.5 │
│ XRP/USDT │     13 │         1.31 │          16.302 │         1.63 │ 1 day, 7:51:00 │    7     0     6  53.8 │
│ BTC/USDT │     13 │        -0.13 │         -10.907 │        -1.09 │       11:00:00 │    6     0     7  46.2 │
│ BNB/USDT │     16 │        -0.39 │         -21.846 │        -2.18 │       14:42:00 │    8     0     8  50.0 │
│    TOTAL │     86 │         0.32 │          59.068 │         5.91 │       12:28:00 │   45     0    41  52.3 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                  ENTER TAG STATS                                                  
┏━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ hammer_rebond │      86 │         0.32 │          59.068 │         5.91 │     12:28:00 │   45     0    41  52.3 │
│         TOTAL │      86 │         0.32 │          59.068 │         5.91 │     12:28:00 │   45     0    41  52.3 │
└───────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │    45 │         2.41 │         443.348 │        44.33 │     16:09:00 │   45     0     0   100 │
│      stop_loss │    41 │        -1.98 │        -384.280 │       -38.43 │      8:26:00 │    0     0    41     0 │
│          TOTAL │    86 │         0.32 │          59.068 │         5.91 │     12:28:00 │   45     0    41  52.3 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                          MIXED TAG STATS                                                          
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ hammer_rebond │ take_profit_1R │     45 │         2.41 │         443.348 │        44.33 │     16:09:00 │   45     0     0   100 │
│ hammer_rebond │      stop_loss │     41 │        -1.98 │        -384.280 │       -38.43 │      8:26:00 │    0     0    41     0 │
│         TOTAL │                │     86 │         0.32 │          59.068 │         5.91 │     12:28:00 │   45     0    41  52.3 │
└───────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00             │
│ Backtesting to                │ 2024-12-31 00:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 86 / 0.08                       │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 1059.068 USDT                   │
│ Absolute profit               │ 59.068 USDT                     │
│ Total profit %                │ 5.91%                           │
│ CAGR %                        │ 1.93%                           │
│ Sortino                       │ 0.16                            │
│ Sharpe                        │ 0.09                            │
│ Calmar                        │ 1.15                            │
│ SQN                           │ 0.53                            │
│ Profit factor                 │ 1.15                            │
│ Expectancy (Ratio)            │ 0.69 (0.07)                     │
│ Avg. daily profit             │ 0.054 USDT                      │
│ Avg. stake amount             │ 439.824 USDT                    │
│ Total trade volume            │ 75860.381 USDT                  │
│                               │                                 │
│ Best Pair                     │ LTC/USDT 4.38%                  │
│ Worst Pair                    │ BNB/USDT -2.18%                 │
│ Best trade                    │ XRP/USDT 9.62%                  │
│ Worst trade                   │ BNB/USDT -6.58%                 │
│ Best day                      │ 23.755 USDT                     │
│ Worst day                     │ -44.317 USDT                    │
│ Days win/draw/lose            │ 39 / 1011 / 28                  │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 11d 10:50 / 0d 16:09 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 6d 21:55 / 0d 08:26  │
│ Max Consecutive Wins / Loss   │ 7 / 4                           │
│ Rejected Entry signals        │ 0                               │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 956.174 USDT                    │
│ Max balance                   │ 1087.509 USDT                   │
│ Max % of account underwater   │ 8.96%                           │
│ Absolute Drawdown (Account)   │ 8.96%                           │
│ Absolute Drawdown             │ 94.154 USDT                     │
│ Drawdown high                 │ 50.328 USDT                     │
│ Drawdown low                  │ -43.826 USDT                    │
│ Drawdown Start                │ 2022-02-15 14:10:00             │
│ Drawdown End                  │ 2022-11-12 05:15:00             │
│ Market change                 │ 46.34%                          │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2024-12-31 00:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     86 │         0.32 │          59.068 │         5.91 │     12:28:00 │   45     0    41  52.3 │ 94.154 USDT  8.96% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-30T22:31:49.660683",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 2659,
  "total_daily_avg_trades": "86 / 0.08",
  "absolute_profit_usdt": 59.068,
  "total_profit_pct": 5.91,
  "cagr_pct": 1.93,
  "sortino": 0.16,
  "sharpe": 0.09,
  "calmar": 1.15,
  "sqn": 0.53,
  "max_consecutive_wins_loss": "7 / 4",
  "min_balance_usdt": 956.174,
  "max_balance_usdt": 1087.509,
  "market_change_pct": 46.34,
  "win_draw_loss_winpct": "45 0 41 52.3"
}
```
