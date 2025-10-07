# Freqtrade Backtest Log

**Strategy:** SimpleStrategy  
**Random State:** 7002  
**Timestamp:** 2025-10-07 18:05:59

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
  "random_state": 7002,
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
2025-10-07 16:03:10,606 - freqtrade - INFO - freqtrade 2025.8
2025-10-07 16:03:11,065 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-07 16:03:12,883 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-07 16:03:12,890 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-07 16:03:12,891 - freqtrade.loggers - INFO - Logfile configured
2025-10-07 16:03:12,892 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-07 16:03:12,893 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 15m ...
2025-10-07 16:03:12,893 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-07 16:03:12,894 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-07 16:03:12,894 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20250101-20251231 ...
2025-10-07 16:03:13,177 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-07 16:03:13,179 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-07 16:03:13,180 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-07 16:03:13,180 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-07 16:03:13,181 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-07 16:03:13,181 - freqtrade.configuration.configuration - INFO - Using pairs ['ADA/USDT', 'SOL/USDT', 'DOGE/USDT', 'BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-10-07 16:03:13,182 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20250101-20251231
2025-10-07 16:03:13,183 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-07 16:03:13,202 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-07 16:03:13,203 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-07 16:03:13,206 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-07 16:03:13,207 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-07 16:03:13,208 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-10-07 16:03:13,235 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-07 16:03:16,149 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-07 16:03:16,369 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy SimpleStrategy from '/freqtrade/user_data/strategies/SimpleStrategy.py'...
2025-10-07 16:03:16,371 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2025-10-07 16:03:16,372 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 15m.
2025-10-07 16:03:16,372 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-07 16:03:16,373 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-07 16:03:16,373 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-07 16:03:16,374 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-07 16:03:16,374 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-07 16:03:16,375 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 15m
2025-10-07 16:03:16,375 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-10-07 16:03:16,376 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-07 16:03:16,377 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-07 16:03:16,377 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-07 16:03:16,378 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-07 16:03:16,378 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-07 16:03:16,380 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'market', 'stoploss_on_exchange': False}
2025-10-07 16:03:16,380 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-07 16:03:16,382 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-07 16:03:16,383 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-07 16:03:16,384 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 200
2025-10-07 16:03:16,384 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-07 16:03:16,385 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-10-07 16:03:16,386 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-07 16:03:16,386 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-07 16:03:16,387 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-07 16:03:16,387 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-07 16:03:16,388 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-07 16:03:16,388 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-07 16:03:16,389 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-07 16:03:16,389 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-07 16:03:16,389 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-07 16:03:16,413 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-07 16:03:16,460 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-07 16:03:16,577 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:03:16,676 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:03:16,785 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:03:16,926 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:03:17,035 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:03:17,135 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:03:17,228 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:03:17,326 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 16:03:17,348 - freqtrade.optimize.backtesting - INFO - Loading data from 2024-12-29 22:00:00 up to 2025-10-07 14:45:00 (281 days).
2025-10-07 16:03:17,605 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:03:17,850 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:03:18,104 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:03:18,481 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:03:18,866 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:03:19,229 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:03:19,548 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:03:19,876 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 16:03:22,056 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-07 16:03:22,062 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-07 16:03:22,063 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy SimpleStrategy
2025-10-07 16:03:22,064 - freqtrade.strategy.hyper - INFO - No params for buy found, using default values.
2025-10-07 16:03:22,065 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_adx_threshold = 5
2025-10-07 16:03:22,067 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-10-07 16:03:22,068 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-10-07 16:03:22,069 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): volume_factor = 0.5
2025-10-07 16:03:22,070 - freqtrade.strategy.hyper - INFO - No params for sell found, using default values.
2025-10-07 16:03:22,070 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): atr_stoploss_multiplier = 1.5
2025-10-07 16:03:22,071 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): custom_sell_atr_factor = 4.5
2025-10-07 16:03:22,072 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): lookback_period_for_stoploss = 5
2025-10-07 16:03:22,072 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): stoploss_margin = 0.999
2025-10-07 16:03:22,073 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): take_profit_multiplier = 2
2025-10-07 16:03:22,073 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): trailing_custom_stop = True
2025-10-07 16:03:22,074 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_sell = True
2025-10-07 16:03:22,075 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_stoploss_param = True
2025-10-07 16:03:22,075 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_stoploss_type = lower
2025-10-07 16:03:22,076 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_sell_signal_param = True
2025-10-07 16:03:22,077 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-07 16:03:22,081 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:03:22,106 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:03:22,148 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:03:22,187 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:03:22,272 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:03:22,302 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:03:22,331 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:03:22,369 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:03:22,436 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:03:22,462 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:03:22,483 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:03:22,520 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:03:22,568 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:03:22,596 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:03:22,620 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:03:22,662 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:03:22,724 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:03:22,746 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:03:22,774 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:03:22,815 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:03:22,866 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:03:22,889 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:03:22,914 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:03:22,952 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:03:23,007 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:03:23,036 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:03:23,068 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:03:23,106 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:03:23,154 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 16:03:23,179 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 16:03:23,200 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 16:03:23,232 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 16:03:23,354 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2025-01-01 00:00:00 up to 2025-10-07 14:45:00 (279 days).
2025-10-07 16:05:57,588 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-07_16-05-57.meta.json"
Result for strategy SimpleStrategy
                                              BACKTESTING REPORT                                              
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  BNB/USDT │    486 │         -0.2 │        -101.779 │       -10.18 │      0:40:00 │   95     0   391  19.5 │
│  ETH/USDT │    479 │        -0.17 │        -108.100 │       -10.81 │      0:38:00 │  124     0   355  25.9 │
│ DOGE/USDT │    520 │        -0.19 │        -116.200 │       -11.62 │      0:39:00 │  144     0   376  27.7 │
│  XRP/USDT │    429 │        -0.22 │        -116.741 │       -11.67 │      0:37:00 │   94     0   335  21.9 │
│  SOL/USDT │    545 │        -0.16 │        -122.016 │        -12.2 │      0:39:00 │  157     0   388  28.8 │
│  ADA/USDT │    698 │        -0.21 │        -131.804 │       -13.18 │      0:41:00 │  187     0   511  26.8 │
│  LTC/USDT │    578 │         -0.2 │        -138.548 │       -13.85 │      0:39:00 │  154     0   424  26.6 │
│  BTC/USDT │    593 │        -0.21 │        -149.009 │        -14.9 │      0:40:00 │  106     0   487  17.9 │
│     TOTAL │   4328 │         -0.2 │        -984.196 │       -98.42 │      0:39:00 │ 1061     0  3267  24.5 │
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
│     OTHER │    4328 │         -0.2 │        -984.196 │       -98.42 │      0:39:00 │ 1061     0  3267  24.5 │
│     TOTAL │    4328 │         -0.2 │        -984.196 │       -98.42 │      0:39:00 │ 1061     0  3267  24.5 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │    72 │         1.97 │         205.031 │         20.5 │      0:50:00 │   72     0     0   100 │
│      stop_loss │   133 │        -1.02 │        -197.653 │       -19.77 │      0:15:00 │    0     0   133     0 │
│    exit_signal │  4123 │        -0.21 │        -991.574 │       -99.16 │      0:40:00 │  989     0  3134  24.0 │
│          TOTAL │  4328 │         -0.2 │        -984.196 │       -98.42 │      0:39:00 │ 1061     0  3267  24.5 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │     72 │         1.97 │         205.031 │         20.5 │      0:50:00 │   72     0     0   100 │
│           │      stop_loss │    133 │        -1.02 │        -197.653 │       -19.77 │      0:15:00 │    0     0   133     0 │
│           │    exit_signal │   4123 │        -0.21 │        -991.574 │       -99.16 │      0:40:00 │  989     0  3134  24.0 │
│     TOTAL │                │   4328 │         -0.2 │        -984.196 │       -98.42 │      0:39:00 │ 1061     0  3267  24.5 │
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
│ Total/Daily Avg Trades        │ 4328 / 15.51                   │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 15.804 USDT                    │
│ Absolute profit               │ -984.196 USDT                  │
│ Total profit %                │ -98.42%                        │
│ CAGR %                        │ -99.56%                        │
│ Sortino                       │ -74.34                         │
│ Sharpe                        │ -54.32                         │
│ Calmar                        │ -6.85                          │
│ SQN                           │ -12.06                         │
│ Profit factor                 │ 0.44                           │
│ Expectancy (Ratio)            │ -0.23 (-0.42)                  │
│ Avg. daily profit             │ -3.528 USDT                    │
│ Avg. stake amount             │ 112.615 USDT                   │
│ Total trade volume            │ 975760 USDT                    │
│                               │                                │
│ Best Pair                     │ BNB/USDT -10.18%               │
│ Worst Pair                    │ BTC/USDT -14.90%               │
│ Best trade                    │ ETH/USDT 6.62%                 │
│ Worst trade                   │ DOGE/USDT -4.13%               │
│ Best day                      │ 24.024 USDT                    │
│ Worst day                     │ -77.664 USDT                   │
│ Days win/draw/lose            │ 38 / 0 / 242                   │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 0d 02:15 / 0d 00:58 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 0d 02:00 / 0d 00:33 │
│ Max Consecutive Wins / Loss   │ 8 / 36                         │
│ Rejected Entry signals        │ 157                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 15.804 USDT                    │
│ Max balance                   │ 1005.505 USDT                  │
│ Max % of account underwater   │ 98.43%                         │
│ Absolute drawdown             │ 989.701 USDT (98.43%)          │
│ Drawdown duration             │ 279 days 12:10:00              │
│ Profit at drawdown start      │ 5.505 USDT                     │
│ Profit at drawdown end        │ -984.196 USDT                  │
│ Drawdown start                │ 2025-01-01 01:30:00            │
│ Drawdown end                  │ 2025-10-07 13:40:00            │
│ Market change                 │ 25.01%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2025-01-01 00:00:00 -> 2025-10-07 14:45:00 | Max open trades : 3
                                                             STRATEGY SUMMARY                                                             
┏━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃       Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ SimpleStrategy │   4328 │        -0.20 │        -984.196 │       -98.42 │      0:39:00 │ 1061     0  3267  24.5 │ 989.701 USDT  98.43% │
└────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-07T18:05:59.769255",
  "strategy": "SimpleStrategy",
  "random_state": 7002,
  "total_daily_avg_trades": "4328 / 15.51",
  "absolute_profit_usdt": -984.196,
  "total_profit_pct": -98.42,
  "cagr_pct": -99.56,
  "sortino": -74.34,
  "sharpe": -54.32,
  "calmar": -6.85,
  "sqn": -12.06,
  "max_consecutive_wins_loss": "8 / 36",
  "min_balance_usdt": 15.804,
  "max_balance_usdt": 1005.505,
  "absolute_drawdown_pct": 98.43,
  "market_change_pct": 25.01,
  "win_draw_loss_winpct": "1061 0 3267 24.5"
}
```
