# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 9337  
**Timestamp:** 2025-09-29 22:21:03

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 9337,
  "epochs": 100,
  "hyperopt_timerange": "20220101-20231231",
  "backtest_timerange": "20220101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231 --export trades --export-filename backtest-result.csv
```

## Backtesting Output
```
2025-09-29 20:14:40,448 - freqtrade - INFO - freqtrade 2025.7
2025-09-29 20:14:40,782 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-29 20:14:40,783 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-29 20:14:42,310 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-29 20:14:42,312 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-29 20:14:42,313 - freqtrade.loggers - INFO - Logfile configured
2025-09-29 20:14:42,313 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-29 20:14:42,314 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-29 20:14:42,314 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-29 20:14:42,314 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-29 20:14:42,315 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-29 20:14:42,322 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-29 20:14:42,323 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-29 20:14:42,324 - freqtrade.configuration.configuration - INFO - Storing backtest results to backtest-result.csv ...
2025-09-29 20:14:42,325 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-29 20:14:42,325 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-09-29 20:14:42,326 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-29 20:14:42,326 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-29 20:14:42,327 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-29 20:14:42,329 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-29 20:14:42,352 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-29 20:14:42,353 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-29 20:14:42,358 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-29 20:14:42,359 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-29 20:14:42,360 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-29 20:14:42,402 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-29 20:14:44,915 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-29 20:14:44,956 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-29 20:14:44,957 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-29 20:14:44,958 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-29 20:14:44,958 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-29 20:14:44,959 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-29 20:14:44,959 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-29 20:14:44,959 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-29 20:14:44,960 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-29 20:14:44,960 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-29 20:14:44,960 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-29 20:14:44,961 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-29 20:14:44,961 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-29 20:14:44,961 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-29 20:14:44,962 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-29 20:14:44,962 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-29 20:14:44,962 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-29 20:14:44,963 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-29 20:14:44,963 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-29 20:14:44,963 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-29 20:14:44,964 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-29 20:14:44,964 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-29 20:14:44,964 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-29 20:14:44,965 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-29 20:14:44,965 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-29 20:14:44,965 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-29 20:14:44,966 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-29 20:14:44,966 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-29 20:14:44,966 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-29 20:14:44,967 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-29 20:14:44,967 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-29 20:14:44,967 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-29 20:14:44,972 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-29 20:14:45,005 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-29 20:14:45,040 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-29 20:14:45,089 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-29 20:14:45,131 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-29 20:14:45,177 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-29 20:14:45,216 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-29 20:14:45,245 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-29 20:14:45,319 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-29 20:14:45,542 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-29 20:14:45,747 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-29 20:14:45,952 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-29 20:14:46,169 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-29 20:14:47,529 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-29 20:14:47,531 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-29 20:14:47,531 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-29 20:14:47,531 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.4
2025-09-29 20:14:47,532 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-29 20:14:47,532 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-29 20:14:47,532 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-29 20:14:47,533 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_strength_threshold = 0.02
2025-09-29 20:14:47,533 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 5
2025-09-29 20:14:47,533 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-09-29 20:14:47,534 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 1
2025-09-29 20:14:47,534 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-09-29 20:14:47,534 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.02
2025-09-29 20:14:47,534 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.003
2025-09-29 20:14:47,535 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): ml_signal_strength_threshold = 50
2025-09-29 20:14:47,535 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-29 20:14:47,535 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-29 20:14:47,536 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_size_threshold = 2
2025-09-29 20:14:47,536 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_strength_threshold = 0.02
2025-09-29 20:14:47,536 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.409
2025-09-29 20:14:47,537 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.003
2025-09-29 20:14:47,537 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_engulfing_entry = False
2025-09-29 20:14:47,537 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_hammer_entry = True
2025-09-29 20:14:47,537 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_strong_bullish_entry = False
2025-09-29 20:14:47,538 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 2.5
2025-09-29 20:14:47,538 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 0.5
2025-09-29 20:14:47,539 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-09-29 20:14:47,539 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-29 20:14:47,539 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 6
2025-09-29 20:14:47,540 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-29 20:14:47,540 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-29 20:14:47,540 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-09-29 20:14:47,541 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-29 20:14:47,541 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-29 20:14:47,541 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-09-29 20:14:47,542 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-29 20:14:47,542 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-29 20:14:47,542 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-29 20:14:47,543 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-29 20:14:47,545 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 20:14:47,554 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-29 20:14:47,578 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 20:14:47,594 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-29 20:14:57,234 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 20:14:57,243 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-29 20:14:57,268 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 20:14:57,286 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-29 20:15:07,253 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 20:15:07,260 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-29 20:15:07,283 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 20:15:07,302 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-29 20:15:17,350 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 20:15:17,357 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-29 20:15:17,380 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 20:15:17,396 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-29 20:15:27,237 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 20:15:27,245 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-29 20:15:27,269 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 20:15:27,285 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-29 20:15:37,291 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-29 20:21:01,713 - freqtrade.misc - INFO - dumping json to "backtest-result-2025-09-29_20-21-01.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │    140 │         0.34 │         136.610 │        13.66 │  1 day, 19:13:00 │   56     0    84  40.0 │
│ BNB/USDT │     64 │         0.63 │         -19.485 │        -1.95 │ 2 days, 11:57:00 │   25     0    39  39.1 │
│ BTC/USDT │     77 │        -0.15 │         -98.958 │         -9.9 │ 3 days, 12:42:00 │   29     0    48  37.7 │
│ XRP/USDT │    188 │        -0.14 │        -149.621 │       -14.96 │  2 days, 4:58:00 │   75     0   113  39.9 │
│ LTC/USDT │    187 │         0.14 │        -217.949 │       -21.79 │ 2 days, 11:42:00 │   69     0   118  36.9 │
│    TOTAL │    656 │         0.11 │        -349.404 │       -34.94 │  2 days, 9:13:00 │  254     0   402  38.7 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ LTC/USDT │      1 │         0.44 │           0.512 │         0.05 │ 53 days, 18:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         0.44 │           0.512 │         0.05 │ 53 days, 18:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                   ENTER TAG STATS                                                    
┏━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ hammer_rebond │     656 │         0.11 │        -349.404 │       -34.94 │ 2 days, 9:13:00 │  254     0   402  38.7 │
│         TOTAL │     656 │         0.11 │        -349.404 │       -34.94 │ 2 days, 9:13:00 │  254     0   402  38.7 │
└───────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                    EXIT REASON STATS                                                    
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │   253 │         6.47 │        4132.043 │        413.2 │  2 days, 21:03:00 │  253     0     0   100 │
│       force_exit │     1 │         0.44 │           0.512 │         0.05 │ 53 days, 18:00:00 │    1     0     0   100 │
│        stop_loss │   402 │        -3.88 │       -4481.959 │       -448.2 │   1 day, 22:41:00 │    0     0   402     0 │
│            TOTAL │   656 │         0.11 │        -349.404 │       -34.94 │   2 days, 9:13:00 │  254     0   402  38.7 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                             MIXED TAG STATS                                                              
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ hammer_rebond │ take_profit_1.5R │    253 │         6.47 │        4132.043 │        413.2 │  2 days, 21:03:00 │  253     0     0   100 │
│ hammer_rebond │       force_exit │      1 │         0.44 │           0.512 │         0.05 │ 53 days, 18:00:00 │    1     0     0   100 │
│ hammer_rebond │        stop_loss │    402 │        -3.88 │       -4481.959 │       -448.2 │   1 day, 22:41:00 │    0     0   402     0 │
│         TOTAL │                  │    656 │         0.11 │        -349.404 │       -34.94 │   2 days, 9:13:00 │  254     0   402  38.7 │
└───────────────┴──────────────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00             │
│ Backtesting to                │ 2025-09-11 17:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 656 / 0.49                      │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 650.596 USDT                    │
│ Absolute profit               │ -349.404 USDT                   │
│ Total profit %                │ -34.94%                         │
│ CAGR %                        │ -10.98%                         │
│ Sortino                       │ -1.08                           │
│ Sharpe                        │ -0.34                           │
│ Calmar                        │ -1.22                           │
│ SQN                           │ -0.93                           │
│ Profit factor                 │ 0.92                            │
│ Expectancy (Ratio)            │ -0.53 (-0.05)                   │
│ Avg. daily profit             │ -0.259 USDT                     │
│ Avg. stake amount             │ 304.748 USDT                    │
│ Total trade volume            │ 400279.169 USDT                 │
│                               │                                 │
│ Best Pair                     │ ETH/USDT 13.66%                 │
│ Worst Pair                    │ LTC/USDT -21.79%                │
│ Best trade                    │ XRP/USDT 26.28%                 │
│ Worst trade                   │ XRP/USDT -30.89%                │
│ Best day                      │ 70.069 USDT                     │
│ Worst day                     │ -68.951 USDT                    │
│ Days win/draw/lose            │ 187 / 915 / 242                 │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 56d 03:00 / 3d 01:51 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 63d 02:25 / 1d 22:41 │
│ Max Consecutive Wins / Loss   │ 8 / 15                          │
│ Rejected Entry signals        │ 1337                            │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 597.405 USDT                    │
│ Max balance                   │ 1003.499 USDT                   │
│ Max % of account underwater   │ 40.47%                          │
│ Absolute Drawdown (Account)   │ 40.47%                          │
│ Absolute Drawdown             │ 406.094 USDT                    │
│ Drawdown high                 │ 3.499 USDT                      │
│ Drawdown low                  │ -402.595 USDT                   │
│ Drawdown Start                │ 2022-03-24 15:45:00             │
│ Drawdown End                  │ 2024-10-03 08:05:00             │
│ Market change                 │ 94.84%                          │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    656 │         0.11 │        -349.404 │       -34.94 │ 2 days, 9:13:00 │  254     0   402  38.7 │ 406.094 USDT  40.47% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-29T22:21:03.033071",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 9337,
  "total_daily_avg_trades": "656 / 0.49",
  "absolute_profit_usdt": -349.404,
  "total_profit_pct": -34.94,
  "cagr_pct": -10.98,
  "sortino": -1.08,
  "sharpe": -0.34,
  "calmar": -1.22,
  "sqn": -0.93,
  "max_consecutive_wins_loss": "8 / 15",
  "min_balance_usdt": 597.405,
  "max_balance_usdt": 1003.499,
  "market_change_pct": 94.84
}
```
