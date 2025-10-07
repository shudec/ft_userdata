# Freqtrade Backtest Log

**Strategy:** SimpleStrategy  
**Random State:** 6768  
**Timestamp:** 2025-10-07 18:22:20

## Configuration
```json
{
  "strategy": "SimpleStrategy",
  "timeframe": "15m",
  "pairs": [
    "ADA/USDT",
    "SOL/USDT",
    "DOGE/USDT",
    "BTC/USDT",
    "ETH/USDT",
    "LTC/USDT",
    "XRP/USDT",
    "BNB/USDT"
  ],
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 6768,
  "epochs": 100,
  "hyperopt_timerange": "20220101-20231231",
  "backtest_timerange": "20250101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy SimpleStrategy --timeframe 15m --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs ADA/USDT SOL/USDT DOGE/USDT BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20250101-20251231 --export trades
```

## Backtesting Output
```
2025-10-07 16:17:18,923 - freqtrade - INFO - freqtrade 2025.8
2025-10-07 16:17:19,390 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-07 16:17:21,633 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-07 16:17:21,642 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-07 16:17:21,642 - freqtrade.loggers - INFO - Logfile configured
2025-10-07 16:17:21,643 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-07 16:17:21,644 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 15m ...
2025-10-07 16:17:21,644 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-07 16:17:21,645 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-07 16:17:21,645 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20250101-20251231 ...
2025-10-07 16:17:21,949 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-07 16:17:21,952 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-07 16:17:21,953 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-07 16:17:21,954 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-07 16:17:21,954 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-07 16:17:21,955 - freqtrade.configuration.configuration - INFO - Using pairs ['ADA/USDT', 'SOL/USDT', 'DOGE/USDT', 'BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-10-07 16:17:21,956 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20250101-20251231
2025-10-07 16:17:21,958 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-07 16:17:21,973 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-07 16:17:21,974 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-07 16:17:21,979 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-07 16:17:21,980 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-07 16:17:21,981 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-10-07 16:17:22,012 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-07 16:17:24,789 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-07 16:17:25,022 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy SimpleStrategy from '/freqtrade/user_data/strategies/SimpleStrategy.py'...
2025-10-07 16:17:25,024 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2025-10-07 16:17:25,026 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 15m.
2025-10-07 16:17:25,026 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-07 16:17:25,027 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-07 16:17:25,027 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-07 16:17:25,028 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-07 16:17:25,029 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-07 16:17:25,029 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 15m
2025-10-07 16:17:25,030 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-10-07 16:17:25,030 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-07 16:17:25,031 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-07 16:17:25,032 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-07 16:17:25,032 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-07 16:17:25,033 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-07 16:17:25,033 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'market', 'stoploss_on_exchange': False}
2025-10-07 16:17:25,034 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-07 16:17:25,035 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-07 16:17:25,036 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-07 16:17:25,038 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 200
2025-10-07 16:17:25,039 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-07 16:17:25,039 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-10-07 16:17:25,040 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-07 16:17:25,041 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-07 16:17:25,041 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-07 16:17:25,042 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-07 16:17:25,042 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-07 16:17:25,043 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-07 16:17:25,043 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-07 16:17:25,043 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-07 16:17:25,044 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-07 16:17:25,067 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-07 16:17:25,116 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-07 16:17:25,236 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:17:25,323 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:17:25,441 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:17:25,574 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:17:25,690 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:17:25,804 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:17:25,913 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:17:26,039 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:17:26,071 - freqtrade.optimize.backtesting - INFO - Loading data from 2024-12-29 22:00:00 up to 2025-10-07 14:45:00 (281 days).
2025-10-07 16:17:26,356 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:17:26,626 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:17:27,025 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:17:27,573 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:17:28,040 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:17:28,563 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:17:28,933 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:17:29,345 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:17:31,314 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-07 16:17:31,320 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-07 16:17:31,320 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy SimpleStrategy
2025-10-07 16:17:31,321 - freqtrade.strategy.hyper - INFO - No params for buy found, using default values.
2025-10-07 16:17:31,322 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_adx_threshold = 5
2025-10-07 16:17:31,323 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-10-07 16:17:31,324 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-10-07 16:17:31,325 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): volume_factor = 0.5
2025-10-07 16:17:31,326 - freqtrade.strategy.hyper - INFO - No params for sell found, using default values.
2025-10-07 16:17:31,327 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): atr_stoploss_multiplier = 1.5
2025-10-07 16:17:31,328 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): custom_sell_atr_factor = 4.5
2025-10-07 16:17:31,329 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): lookback_period_for_stoploss = 5
2025-10-07 16:17:31,330 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): stoploss_margin = 0.999
2025-10-07 16:17:31,331 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): take_profit_multiplier = 2
2025-10-07 16:17:31,331 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): trailing_custom_stop = True
2025-10-07 16:17:31,332 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_sell = True
2025-10-07 16:17:31,333 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_stoploss_param = True
2025-10-07 16:17:31,334 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_stoploss_type = lower
2025-10-07 16:17:31,335 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_sell_signal_param = True
2025-10-07 16:17:31,336 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-07 16:17:31,339 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:17:31,363 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:17:31,393 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:17:31,426 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:17:31,487 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:17:31,507 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:17:31,530 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:17:31,557 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:17:31,607 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:17:31,632 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:17:31,651 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:17:31,691 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:17:31,732 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:17:31,752 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:17:31,767 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:17:31,800 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:17:31,848 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:17:31,864 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:17:31,879 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:17:31,920 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:17:31,959 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:17:31,979 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:17:31,993 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:17:32,020 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:17:32,051 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:17:32,070 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:17:32,086 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:17:32,113 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:17:32,150 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:17:32,168 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:17:32,185 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:17:32,215 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:17:32,322 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2025-01-01 00:00:00 up to 2025-10-07 14:45:00 (279 days).
2025-10-07 16:22:18,507 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-07_16-22-18.meta.json"
Result for strategy SimpleStrategy
                                              BACKTESTING REPORT                                              
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  BNB/USDT │    361 │        -0.11 │         -43.333 │        -4.33 │      2:24:00 │   75     0   286  20.8 │
│  XRP/USDT │    289 │        -0.08 │         -66.875 │        -6.69 │      2:02:00 │   67     0   222  23.2 │
│ DOGE/USDT │    399 │        -0.17 │         -83.492 │        -8.35 │      2:01:00 │   90     0   309  22.6 │
│  ETH/USDT │    348 │        -0.13 │        -103.564 │       -10.36 │      2:00:00 │   62     0   286  17.8 │
│  LTC/USDT │    418 │         -0.2 │        -135.084 │       -13.51 │      1:55:00 │   80     0   338  19.1 │
│  BTC/USDT │    433 │         -0.2 │        -144.126 │       -14.41 │      2:13:00 │   68     0   365  15.7 │
│  SOL/USDT │    392 │         -0.2 │        -149.757 │       -14.98 │      2:12:00 │   74     0   318  18.9 │
│  ADA/USDT │    519 │        -0.21 │        -202.175 │       -20.22 │      2:09:00 │  101     0   418  19.5 │
│     TOTAL │   3159 │        -0.17 │        -928.406 │       -92.84 │      2:07:00 │  617     0  2542  19.5 │
└───────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                ENTER TAG STATS                                                
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │    3159 │        -0.17 │        -928.406 │       -92.84 │      2:07:00 │  617     0  2542  19.5 │
│     TOTAL │    3159 │        -0.17 │        -928.406 │       -92.84 │      2:07:00 │  617     0  2542  19.5 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │   328 │         2.32 │        1396.414 │       139.64 │      3:38:00 │  328     0     0   100 │
│      stop_loss │   193 │        -1.07 │        -408.231 │       -40.82 │      0:47:00 │    0     0   193     0 │
│    exit_signal │  2638 │        -0.41 │       -1916.589 │      -191.66 │      2:02:00 │  289     0  2349  11.0 │
│          TOTAL │  3159 │        -0.17 │        -928.406 │       -92.84 │      2:07:00 │  617     0  2542  19.5 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │    328 │         2.32 │        1396.414 │       139.64 │      3:38:00 │  328     0     0   100 │
│           │      stop_loss │    193 │        -1.07 │        -408.231 │       -40.82 │      0:47:00 │    0     0   193     0 │
│           │    exit_signal │   2638 │        -0.41 │       -1916.589 │      -191.66 │      2:02:00 │  289     0  2349  11.0 │
│     TOTAL │                │   3159 │        -0.17 │        -928.406 │       -92.84 │      2:07:00 │  617     0  2542  19.5 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2025-01-01 00:00:00            │
│ Backtesting to                │ 2025-10-07 14:45:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 3159 / 11.32                   │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 71.594 USDT                    │
│ Absolute profit               │ -928.406 USDT                  │
│ Total profit %                │ -92.84%                        │
│ CAGR %                        │ -96.82%                        │
│ Sortino                       │ -50.69                         │
│ Sharpe                        │ -25.71                         │
│ Calmar                        │ -6.84                          │
│ SQN                           │ -6.68                          │
│ Profit factor                 │ 0.64                           │
│ Expectancy (Ratio)            │ -0.29 (-0.29)                  │
│ Avg. daily profit             │ -3.328 USDT                    │
│ Avg. stake amount             │ 166.435 USDT                   │
│ Total trade volume            │ 1052709.262 USDT               │
│                               │                                │
│ Best Pair                     │ BNB/USDT -4.33%                │
│ Worst Pair                    │ ADA/USDT -20.22%               │
│ Best trade                    │ ETH/USDT 8.72%                 │
│ Worst trade                   │ DOGE/USDT -4.13%               │
│ Best day                      │ 64.685 USDT                    │
│ Worst day                     │ -88.884 USDT                   │
│ Days win/draw/lose            │ 84 / 0 / 196                   │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 0d 16:00 / 0d 04:55 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 0d 11:30 / 0d 01:26 │
│ Max Consecutive Wins / Loss   │ 5 / 35                         │
│ Rejected Entry signals        │ 394                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 71.594 USDT                    │
│ Max balance                   │ 1006.27 USDT                   │
│ Max % of account underwater   │ 92.89%                         │
│ Absolute drawdown             │ 934.676 USDT (92.89%)          │
│ Drawdown duration             │ 278 days 03:40:00              │
│ Profit at drawdown start      │ 6.27 USDT                      │
│ Profit at drawdown end        │ -928.406 USDT                  │
│ Drawdown start                │ 2025-01-02 10:00:00            │
│ Drawdown end                  │ 2025-10-07 13:40:00            │
│ Market change                 │ 25.01%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2025-01-01 00:00:00 -> 2025-10-07 14:45:00 | Max open trades : 3
                                                             STRATEGY SUMMARY                                                             
┏━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃       Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ SimpleStrategy │   3159 │        -0.17 │        -928.406 │       -92.84 │      2:07:00 │  617     0  2542  19.5 │ 934.676 USDT  92.89% │
└────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-07T18:22:20.440404",
  "strategy": "SimpleStrategy",
  "random_state": 6768,
  "total_daily_avg_trades": "3159 / 11.32",
  "absolute_profit_usdt": -928.406,
  "total_profit_pct": -92.84,
  "cagr_pct": -96.82,
  "sortino": -50.69,
  "sharpe": -25.71,
  "calmar": -6.84,
  "sqn": -6.68,
  "max_consecutive_wins_loss": "5 / 35",
  "min_balance_usdt": 71.594,
  "max_balance_usdt": 1006.27,
  "absolute_drawdown_pct": 92.89,
  "market_change_pct": 25.01,
  "win_draw_loss_winpct": "617 0 2542 19.5"
}
```
