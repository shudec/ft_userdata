# Freqtrade Backtest Log

**Strategy:** SimpleStrategy  
**Random State:** 8061  
**Timestamp:** 2025-10-07 18:12:32

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
  "random_state": 8061,
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
2025-10-07 16:07:26,315 - freqtrade - INFO - freqtrade 2025.8
2025-10-07 16:07:26,816 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-07 16:07:29,043 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-07 16:07:29,050 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-07 16:07:29,051 - freqtrade.loggers - INFO - Logfile configured
2025-10-07 16:07:29,052 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-07 16:07:29,054 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 15m ...
2025-10-07 16:07:29,055 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-07 16:07:29,056 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-07 16:07:29,057 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20250101-20251231 ...
2025-10-07 16:07:29,366 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-07 16:07:29,369 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-07 16:07:29,370 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-07 16:07:29,371 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-07 16:07:29,371 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-07 16:07:29,372 - freqtrade.configuration.configuration - INFO - Using pairs ['ADA/USDT', 'SOL/USDT', 'DOGE/USDT', 'BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-10-07 16:07:29,373 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20250101-20251231
2025-10-07 16:07:29,374 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-07 16:07:29,393 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-07 16:07:29,394 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-07 16:07:29,398 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-07 16:07:29,399 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-07 16:07:29,400 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-10-07 16:07:29,429 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-07 16:07:32,559 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-07 16:07:32,767 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy SimpleStrategy from '/freqtrade/user_data/strategies/SimpleStrategy.py'...
2025-10-07 16:07:32,769 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2025-10-07 16:07:32,770 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 15m.
2025-10-07 16:07:32,771 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-07 16:07:32,772 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-07 16:07:32,773 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-07 16:07:32,774 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-07 16:07:32,775 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-07 16:07:32,776 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 15m
2025-10-07 16:07:32,776 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-10-07 16:07:32,777 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-07 16:07:32,778 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-07 16:07:32,778 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-07 16:07:32,779 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-07 16:07:32,780 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-07 16:07:32,780 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'market', 'stoploss_on_exchange': False}
2025-10-07 16:07:32,781 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-07 16:07:32,782 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-07 16:07:32,783 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-07 16:07:32,783 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 200
2025-10-07 16:07:32,784 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-07 16:07:32,785 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-10-07 16:07:32,785 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-07 16:07:32,786 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-07 16:07:32,788 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-07 16:07:32,789 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-07 16:07:32,790 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-07 16:07:32,791 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-07 16:07:32,791 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-07 16:07:32,792 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-07 16:07:32,793 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-07 16:07:32,815 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-07 16:07:32,854 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-07 16:07:32,964 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:07:33,050 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:07:33,142 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:07:33,258 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:07:33,368 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:07:33,476 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:07:33,574 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:07:33,674 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:07:33,693 - freqtrade.optimize.backtesting - INFO - Loading data from 2024-12-29 22:00:00 up to 2025-10-07 14:45:00 (281 days).
2025-10-07 16:07:33,897 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:07:34,099 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:07:34,337 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:07:34,674 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:07:35,007 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:07:35,327 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:07:35,647 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:07:35,988 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:07:38,404 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-07 16:07:38,411 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-07 16:07:38,412 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy SimpleStrategy
2025-10-07 16:07:38,413 - freqtrade.strategy.hyper - INFO - No params for buy found, using default values.
2025-10-07 16:07:38,414 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_adx_threshold = 5
2025-10-07 16:07:38,415 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-10-07 16:07:38,415 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-10-07 16:07:38,416 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): volume_factor = 0.5
2025-10-07 16:07:38,417 - freqtrade.strategy.hyper - INFO - No params for sell found, using default values.
2025-10-07 16:07:38,417 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): atr_stoploss_multiplier = 1.5
2025-10-07 16:07:38,418 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): custom_sell_atr_factor = 4.5
2025-10-07 16:07:38,419 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): lookback_period_for_stoploss = 5
2025-10-07 16:07:38,420 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): stoploss_margin = 0.999
2025-10-07 16:07:38,420 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): take_profit_multiplier = 2
2025-10-07 16:07:38,421 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): trailing_custom_stop = True
2025-10-07 16:07:38,422 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_sell = True
2025-10-07 16:07:38,423 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_stoploss_param = True
2025-10-07 16:07:38,423 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_stoploss_type = lower
2025-10-07 16:07:38,424 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_sell_signal_param = True
2025-10-07 16:07:38,424 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-07 16:07:38,428 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:07:38,456 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:07:38,480 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:07:38,520 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:07:38,597 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:07:38,621 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:07:38,650 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:07:38,690 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:07:38,768 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:07:38,838 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:07:38,889 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:07:38,938 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:07:39,000 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:07:39,032 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:07:39,068 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:07:39,122 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:07:39,221 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:07:39,255 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:07:39,304 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:07:39,348 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:07:39,440 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:07:39,523 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:07:39,605 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:07:39,685 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:07:39,756 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:07:39,788 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:07:39,836 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:07:39,885 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:07:39,937 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:07:39,963 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:07:39,991 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:07:40,035 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:07:40,187 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2025-01-01 00:00:00 up to 2025-10-07 14:45:00 (279 days).
2025-10-07 16:12:30,668 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-07_16-12-30.meta.json"
Result for strategy SimpleStrategy
                                              BACKTESTING REPORT                                              
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  BNB/USDT │    386 │        -0.11 │         -44.910 │        -4.49 │      2:12:00 │   83     0   303  21.5 │
│  XRP/USDT │    316 │        -0.09 │         -74.018 │         -7.4 │      1:50:00 │   71     0   245  22.5 │
│ DOGE/USDT │    428 │        -0.16 │         -88.812 │        -8.88 │      1:45:00 │   95     0   333  22.2 │
│  ETH/USDT │    369 │        -0.13 │         -97.078 │        -9.71 │      1:46:00 │   71     0   298  19.2 │
│  SOL/USDT │    411 │        -0.19 │        -142.142 │       -14.21 │      1:58:00 │   83     0   328  20.2 │
│  BTC/USDT │    462 │        -0.19 │        -143.851 │       -14.39 │      2:01:00 │   74     0   388  16.0 │
│  LTC/USDT │    450 │        -0.21 │        -158.576 │       -15.86 │      1:43:00 │   88     0   362  19.6 │
│  ADA/USDT │    566 │        -0.21 │        -190.444 │       -19.04 │      1:52:00 │  119     0   447  21.0 │
│     TOTAL │   3388 │        -0.17 │        -939.831 │       -93.98 │      1:53:00 │  684     0  2704  20.2 │
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
│     OTHER │    3388 │        -0.17 │        -939.831 │       -93.98 │      1:53:00 │  684     0  2704  20.2 │
│     TOTAL │    3388 │        -0.17 │        -939.831 │       -93.98 │      1:53:00 │  684     0  2704  20.2 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │   328 │         2.22 │        1222.469 │       122.25 │      3:13:00 │  328     0     0   100 │
│      stop_loss │   182 │        -1.06 │        -342.233 │       -34.22 │      0:40:00 │    0     0   182     0 │
│    exit_signal │  2878 │        -0.38 │       -1820.067 │      -182.01 │      1:49:00 │  356     0  2522  12.4 │
│          TOTAL │  3388 │        -0.17 │        -939.831 │       -93.98 │      1:53:00 │  684     0  2704  20.2 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │    328 │         2.22 │        1222.469 │       122.25 │      3:13:00 │  328     0     0   100 │
│           │      stop_loss │    182 │        -1.06 │        -342.233 │       -34.22 │      0:40:00 │    0     0   182     0 │
│           │    exit_signal │   2878 │        -0.38 │       -1820.067 │      -182.01 │      1:49:00 │  356     0  2522  12.4 │
│     TOTAL │                │   3388 │        -0.17 │        -939.831 │       -93.98 │      1:53:00 │  684     0  2704  20.2 │
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
│ Total/Daily Avg Trades        │ 3388 / 12.14                   │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 60.169 USDT                    │
│ Absolute profit               │ -939.831 USDT                  │
│ Total profit %                │ -93.98%                        │
│ CAGR %                        │ -97.47%                        │
│ Sortino                       │ -54.52                         │
│ Sharpe                        │ -29.66                         │
│ Calmar                        │ -6.85                          │
│ SQN                           │ -7.44                          │
│ Profit factor                 │ 0.63                           │
│ Expectancy (Ratio)            │ -0.28 (-0.30)                  │
│ Avg. daily profit             │ -3.369 USDT                    │
│ Avg. stake amount             │ 155.725 USDT                   │
│ Total trade volume            │ 1056362.636 USDT               │
│                               │                                │
│ Best Pair                     │ BNB/USDT -4.49%                │
│ Worst Pair                    │ ADA/USDT -19.04%               │
│ Best trade                    │ ETH/USDT 8.72%                 │
│ Worst trade                   │ DOGE/USDT -4.13%               │
│ Best day                      │ 31.974 USDT                    │
│ Worst day                     │ -83.028 USDT                   │
│ Days win/draw/lose            │ 80 / 0 / 200                   │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 0d 16:00 / 0d 04:19 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 0d 11:30 / 0d 01:16 │
│ Max Consecutive Wins / Loss   │ 6 / 36                         │
│ Rejected Entry signals        │ 312                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 60.169 USDT                    │
│ Max balance                   │ 1006.093 USDT                  │
│ Max % of account underwater   │ 94.02%                         │
│ Absolute drawdown             │ 945.925 USDT (94.02%)          │
│ Drawdown duration             │ 278 days 03:40:00              │
│ Profit at drawdown start      │ 6.093 USDT                     │
│ Profit at drawdown end        │ -939.831 USDT                  │
│ Drawdown start                │ 2025-01-02 10:00:00            │
│ Drawdown end                  │ 2025-10-07 13:40:00            │
│ Market change                 │ 25.01%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2025-01-01 00:00:00 -> 2025-10-07 14:45:00 | Max open trades : 3
                                                             STRATEGY SUMMARY                                                             
┏━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃       Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ SimpleStrategy │   3388 │        -0.17 │        -939.831 │       -93.98 │      1:53:00 │  684     0  2704  20.2 │ 945.925 USDT  94.02% │
└────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-07T18:12:32.753697",
  "strategy": "SimpleStrategy",
  "random_state": 8061,
  "total_daily_avg_trades": "3388 / 12.14",
  "absolute_profit_usdt": -939.831,
  "total_profit_pct": -93.98,
  "cagr_pct": -97.47,
  "sortino": -54.52,
  "sharpe": -29.66,
  "calmar": -6.85,
  "sqn": -7.44,
  "max_consecutive_wins_loss": "6 / 36",
  "min_balance_usdt": 60.169,
  "max_balance_usdt": 1006.093,
  "absolute_drawdown_pct": 94.02,
  "market_change_pct": 25.01,
  "win_draw_loss_winpct": "684 0 2704 20.2"
}
```
