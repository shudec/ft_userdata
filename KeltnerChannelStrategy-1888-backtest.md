# Freqtrade Backtest Log

**Strategy:** KeltnerChannelStrategy  
**Random State:** 1888  
**Timestamp:** 2025-10-09 11:16:47

## Configuration
```json
{
  "strategy": "KeltnerChannelStrategy",
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
  "random_state": 1888,
  "epochs": 100,
  "hyperopt_timerange": "20220101-20231231",
  "backtest_timerange": "20250101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy KeltnerChannelStrategy --timeframe 15m --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs ADA/USDT SOL/USDT DOGE/USDT BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20250101-20251231 --export trades
```

## Backtesting Output
```
2025-10-09 09:16:08,686 - freqtrade - INFO - freqtrade 2025.8
2025-10-09 09:16:09,371 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-09 09:16:12,659 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-09 09:16:12,671 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-09 09:16:12,672 - freqtrade.loggers - INFO - Logfile configured
2025-10-09 09:16:12,672 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-09 09:16:12,673 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 15m ...
2025-10-09 09:16:12,674 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-09 09:16:12,675 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-09 09:16:12,676 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20250101-20251231 ...
2025-10-09 09:16:12,988 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-09 09:16:12,991 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-09 09:16:12,993 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-09 09:16:12,994 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-09 09:16:12,996 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-09 09:16:12,997 - freqtrade.configuration.configuration - INFO - Using pairs ['ADA/USDT', 'SOL/USDT', 'DOGE/USDT', 'BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-10-09 09:16:12,998 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20250101-20251231
2025-10-09 09:16:13,000 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-09 09:16:13,019 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-09 09:16:13,033 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-09 09:16:13,037 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-09 09:16:13,039 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-09 09:16:13,039 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-10-09 09:16:13,074 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-09 09:16:18,066 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-09 09:16:18,310 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy KeltnerChannelStrategy from '/freqtrade/user_data/strategies/KeltnerChannelStrategy.py'...
2025-10-09 09:16:18,313 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/KeltnerChannelStrategy.json
2025-10-09 09:16:18,320 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 15m.
2025-10-09 09:16:18,321 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-09 09:16:18,322 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-09 09:16:18,322 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-09 09:16:18,323 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-09 09:16:18,324 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-09 09:16:18,324 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 15m
2025-10-09 09:16:18,325 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-10-09 09:16:18,325 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-09 09:16:18,326 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-09 09:16:18,327 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-09 09:16:18,327 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-09 09:16:18,328 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-09 09:16:18,328 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'market', 'stoploss_on_exchange': False}
2025-10-09 09:16:18,329 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-09 09:16:18,330 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-09 09:16:18,330 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-09 09:16:18,331 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 200
2025-10-09 09:16:18,332 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-09 09:16:18,333 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-10-09 09:16:18,354 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-09 09:16:18,355 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-09 09:16:18,355 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-09 09:16:18,356 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-09 09:16:18,356 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-09 09:16:18,357 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-09 09:16:18,358 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-09 09:16:18,358 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-09 09:16:18,359 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-09 09:16:18,387 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-09 09:16:18,453 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-09 09:16:18,664 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 09:16:18,800 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 09:16:18,987 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 09:16:19,252 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 09:16:19,454 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 09:16:19,689 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 09:16:19,903 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 09:16:20,127 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 09:16:20,186 - freqtrade.optimize.backtesting - INFO - Loading data from 2024-12-29 22:00:00 up to 2025-10-07 14:45:00 (281 days).
2025-10-09 09:16:20,631 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 09:16:21,089 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 09:16:21,565 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 09:16:22,062 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 09:16:22,586 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 09:16:23,022 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 09:16:23,578 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 09:16:24,106 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 09:16:27,026 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-09 09:16:27,033 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-09 09:16:27,034 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy KeltnerChannelStrategy
2025-10-09 09:16:27,035 - freqtrade.strategy.hyper - INFO - Strategy Parameter: adx_entry_param = 30
2025-10-09 09:16:27,035 - freqtrade.strategy.hyper - INFO - Strategy Parameter: chop_entry_param = 20
2025-10-09 09:16:27,036 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 5
2025-10-09 09:16:27,036 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-10-09 09:16:27,037 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-10-09 09:16:27,037 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-10-09 09:16:27,039 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 2.5
2025-10-09 09:16:27,039 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 4.5
2025-10-09 09:16:27,040 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-10-09 09:16:27,041 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-10-09 09:16:27,042 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-10-09 09:16:27,042 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-10-09 09:16:27,042 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-10-09 09:16:27,043 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = candle_close_atr
2025-10-09 09:16:27,043 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-10-09 09:16:27,044 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-09 09:16:27,047 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 09:16:27,070 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 09:16:27,099 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 09:16:27,137 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 09:16:27,961 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 09:16:27,992 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 09:16:28,018 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 09:16:28,060 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 09:16:28,703 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 09:16:28,734 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 09:16:28,762 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 09:16:28,800 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 09:16:29,501 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 09:16:29,521 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 09:16:29,537 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 09:16:29,568 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 09:16:30,277 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 09:16:30,302 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 09:16:30,321 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 09:16:30,366 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 09:16:31,095 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 09:16:31,120 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 09:16:31,146 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 09:16:31,183 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 09:16:31,852 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 09:16:31,882 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 09:16:31,901 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 09:16:31,933 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 09:16:32,604 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 09:16:32,627 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 09:16:32,644 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 09:16:32,679 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 09:16:33,387 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2025-01-01 00:00:00 up to 2025-10-07 14:45:00 (279 days).
2025-10-09 09:16:45,860 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-09_09-16-45.meta.json"
Result for strategy KeltnerChannelStrategy
                                               BACKTESTING REPORT                                               
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  LTC/USDT │      4 │          2.1 │          37.227 │         3.72 │       13:11:00 │    3     0     1  75.0 │
│  ADA/USDT │      7 │         0.46 │          22.454 │         2.25 │        4:58:00 │    2     0     5  28.6 │
│  ETH/USDT │      2 │         0.54 │           5.027 │          0.5 │       17:50:00 │    1     0     1  50.0 │
│  BTC/USDT │      9 │        -0.03 │          -1.546 │        -0.15 │        5:17:00 │    4     0     5  44.4 │
│  SOL/USDT │      1 │        -1.11 │          -4.987 │         -0.5 │ 1 day, 2:35:00 │    0     0     1     0 │
│  BNB/USDT │      6 │         -0.7 │         -19.431 │        -1.94 │        9:34:00 │    1     0     5  16.7 │
│ DOGE/USDT │      4 │        -2.15 │         -40.851 │        -4.09 │        3:11:00 │    0     0     4     0 │
│  XRP/USDT │      6 │        -1.05 │         -43.528 │        -4.35 │       22:12:00 │    2     0     4  33.3 │
│     TOTAL │     39 │         -0.2 │         -45.634 │        -4.56 │       10:17:00 │   13     0    26  33.3 │
└───────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
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
│     OTHER │      39 │         -0.2 │         -45.634 │        -4.56 │     10:17:00 │   13     0    26  33.3 │
│     TOTAL │      39 │         -0.2 │         -45.634 │        -4.56 │     10:17:00 │   13     0    26  33.3 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │    13 │         3.76 │         178.240 │        17.82 │      8:05:00 │   13     0     0   100 │
│      stop_loss │    26 │        -2.18 │        -223.874 │       -22.39 │     11:22:00 │    0     0    26     0 │
│          TOTAL │    39 │         -0.2 │         -45.634 │        -4.56 │     10:17:00 │   13     0    26  33.3 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │     13 │         3.76 │         178.240 │        17.82 │      8:05:00 │   13     0     0   100 │
│           │      stop_loss │     26 │        -2.18 │        -223.874 │       -22.39 │     11:22:00 │    0     0    26     0 │
│     TOTAL │                │     39 │         -0.2 │         -45.634 │        -4.56 │     10:17:00 │   13     0    26  33.3 │
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
│ Total/Daily Avg Trades        │ 39 / 0.14                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 954.366 USDT                   │
│ Absolute profit               │ -45.634 USDT                   │
│ Total profit %                │ -4.56%                         │
│ CAGR %                        │ -5.93%                         │
│ Sortino                       │ -0.55                          │
│ Sharpe                        │ -0.23                          │
│ Calmar                        │ -2.66                          │
│ SQN                           │ -0.52                          │
│ Profit factor                 │ 0.80                           │
│ Expectancy (Ratio)            │ -1.17 (-0.14)                  │
│ Avg. daily profit             │ -0.164 USDT                    │
│ Avg. stake amount             │ 433.22 USDT                    │
│ Total trade volume            │ 33813.089 USDT                 │
│                               │                                │
│ Best Pair                     │ LTC/USDT 3.72%                 │
│ Worst Pair                    │ XRP/USDT -4.35%                │
│ Best trade                    │ ADA/USDT 14.66%                │
│ Worst trade                   │ ADA/USDT -9.64%                │
│ Best day                      │ 38.212 USDT                    │
│ Worst day                     │ -20.45 USDT                    │
│ Days win/draw/lose            │ 11 / 227 / 21                  │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 1d 04:10 / 0d 08:05 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 2d 23:00 / 0d 11:22 │
│ Max Consecutive Wins / Loss   │ 2 / 5                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 896.693 USDT                   │
│ Max balance                   │ 1015.805 USDT                  │
│ Max % of account underwater   │ 11.73%                         │
│ Absolute drawdown             │ 119.112 USDT (11.73%)          │
│ Drawdown duration             │ 127 days 00:45:00              │
│ Profit at drawdown start      │ 15.805 USDT                    │
│ Profit at drawdown end        │ -103.307 USDT                  │
│ Drawdown start                │ 2025-03-02 15:35:00            │
│ Drawdown end                  │ 2025-07-07 16:20:00            │
│ Market change                 │ 25.01%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2025-01-01 00:00:00 -> 2025-10-07 14:45:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ KeltnerChannelStrategy │     39 │        -0.20 │         -45.634 │        -4.56 │     10:17:00 │   13     0    26  33.3 │ 119.112 USDT  11.73% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-09T11:16:47.731400",
  "strategy": "KeltnerChannelStrategy",
  "random_state": 1888,
  "total_daily_avg_trades": "39 / 0.14",
  "absolute_profit_usdt": -45.634,
  "total_profit_pct": -4.56,
  "cagr_pct": -5.93,
  "sortino": -0.55,
  "sharpe": -0.23,
  "calmar": -2.66,
  "sqn": -0.52,
  "max_consecutive_wins_loss": "2 / 5",
  "min_balance_usdt": 896.693,
  "max_balance_usdt": 1015.805,
  "absolute_drawdown_pct": 11.73,
  "market_change_pct": 25.01,
  "win_draw_loss_winpct": "13 0 26 33.3"
}
```
