# Freqtrade Backtest Log

**Strategy:** SimpleStrategy  
**Random State:** 9816  
**Timestamp:** 2025-10-07 18:01:24

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
  "random_state": 9816,
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
2025-10-07 15:59:23,993 - freqtrade - INFO - freqtrade 2025.8
2025-10-07 15:59:24,792 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-07 15:59:27,706 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-07 15:59:27,715 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-07 15:59:27,715 - freqtrade.loggers - INFO - Logfile configured
2025-10-07 15:59:27,716 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-07 15:59:27,716 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 15m ...
2025-10-07 15:59:27,717 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-07 15:59:27,718 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-07 15:59:27,718 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20250101-20251231 ...
2025-10-07 15:59:28,049 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-07 15:59:28,052 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-07 15:59:28,053 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-07 15:59:28,053 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-07 15:59:28,054 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-07 15:59:28,054 - freqtrade.configuration.configuration - INFO - Using pairs ['ADA/USDT', 'SOL/USDT', 'DOGE/USDT', 'BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-10-07 15:59:28,055 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20250101-20251231
2025-10-07 15:59:28,056 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-07 15:59:28,071 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-07 15:59:28,072 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-07 15:59:28,074 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-07 15:59:28,075 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-07 15:59:28,076 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-10-07 15:59:28,101 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-07 15:59:31,671 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-07 15:59:32,022 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy SimpleStrategy from '/freqtrade/user_data/strategies/SimpleStrategy.py'...
2025-10-07 15:59:32,025 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2025-10-07 15:59:32,028 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 15m.
2025-10-07 15:59:32,029 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-07 15:59:32,030 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-07 15:59:32,031 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-07 15:59:32,032 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-07 15:59:32,033 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-07 15:59:32,034 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 15m
2025-10-07 15:59:32,035 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-10-07 15:59:32,036 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-07 15:59:32,037 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-07 15:59:32,037 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-07 15:59:32,039 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-07 15:59:32,040 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-07 15:59:32,040 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'market', 'stoploss_on_exchange': False}
2025-10-07 15:59:32,041 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-07 15:59:32,042 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-07 15:59:32,043 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-07 15:59:32,044 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 200
2025-10-07 15:59:32,045 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-07 15:59:32,046 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-10-07 15:59:32,046 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-07 15:59:32,047 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-07 15:59:32,048 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-07 15:59:32,050 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-07 15:59:32,051 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-07 15:59:32,051 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-07 15:59:32,052 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-07 15:59:32,053 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-07 15:59:32,053 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-07 15:59:32,096 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-07 15:59:32,163 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-07 15:59:32,378 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 15:59:32,545 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 15:59:32,711 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 15:59:32,937 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 15:59:33,095 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 15:59:33,242 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 15:59:33,443 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 15:59:33,678 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 15:59:33,721 - freqtrade.optimize.backtesting - INFO - Loading data from 2024-12-29 22:00:00 up to 2025-10-07 14:45:00 (281 days).
2025-10-07 15:59:34,361 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 15:59:34,760 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 15:59:35,261 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 15:59:35,748 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 15:59:36,180 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 15:59:36,557 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 15:59:36,936 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 15:59:37,274 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 15:59:39,184 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-07 15:59:39,190 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-07 15:59:39,191 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy SimpleStrategy
2025-10-07 15:59:39,191 - freqtrade.strategy.hyper - INFO - No params for buy found, using default values.
2025-10-07 15:59:39,193 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_adx_threshold = 5
2025-10-07 15:59:39,193 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-10-07 15:59:39,194 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-10-07 15:59:39,194 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): volume_factor = 0.5
2025-10-07 15:59:39,195 - freqtrade.strategy.hyper - INFO - No params for sell found, using default values.
2025-10-07 15:59:39,196 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): atr_stoploss_multiplier = 1.5
2025-10-07 15:59:39,197 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): custom_sell_atr_factor = 4.5
2025-10-07 15:59:39,197 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): lookback_period_for_stoploss = 5
2025-10-07 15:59:39,198 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): stoploss_margin = 0.999
2025-10-07 15:59:39,199 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): take_profit_multiplier = 2
2025-10-07 15:59:39,200 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): trailing_custom_stop = True
2025-10-07 15:59:39,201 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_sell = True
2025-10-07 15:59:39,202 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_stoploss_param = True
2025-10-07 15:59:39,202 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_stoploss_type = lower
2025-10-07 15:59:39,203 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_sell_signal_param = True
2025-10-07 15:59:39,204 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-07 15:59:39,206 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 15:59:39,225 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 15:59:39,256 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 15:59:39,286 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 15:59:39,352 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 15:59:39,371 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 15:59:39,387 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 15:59:39,413 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 15:59:39,456 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 15:59:39,477 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 15:59:39,495 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 15:59:39,525 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 15:59:39,562 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 15:59:39,584 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 15:59:39,602 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 15:59:39,636 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 15:59:39,686 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 15:59:39,708 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 15:59:39,726 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 15:59:39,764 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 15:59:39,808 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 15:59:39,828 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 15:59:39,846 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 15:59:39,879 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 15:59:39,912 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 15:59:39,935 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 15:59:39,953 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 15:59:39,984 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 15:59:40,030 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 15:59:40,051 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 15:59:40,066 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 15:59:40,097 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 15:59:40,203 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2025-01-01 00:00:00 up to 2025-10-07 14:45:00 (279 days).
2025-10-07 16:01:22,327 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-07_16-01-22.meta.json"
Result for strategy SimpleStrategy
                                              BACKTESTING REPORT                                              
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  ETH/USDT │    333 │        -0.18 │         -78.540 │        -7.85 │      0:37:00 │   81     0   252  24.3 │
│  XRP/USDT │    346 │        -0.23 │         -95.573 │        -9.56 │      0:36:00 │   72     0   274  20.8 │
│  BNB/USDT │    354 │        -0.21 │        -102.055 │       -10.21 │      0:38:00 │   64     0   290  18.1 │
│  ADA/USDT │    526 │        -0.22 │        -110.734 │       -11.07 │      0:38:00 │  147     0   379  27.9 │
│  BTC/USDT │    428 │         -0.2 │        -117.536 │       -11.75 │      0:38:00 │   73     0   355  17.1 │
│  LTC/USDT │    429 │        -0.21 │        -128.062 │       -12.81 │      0:38:00 │  109     0   320  25.4 │
│ DOGE/USDT │    421 │        -0.22 │        -156.933 │       -15.69 │      0:37:00 │  111     0   310  26.4 │
│  SOL/USDT │    462 │        -0.22 │        -178.526 │       -17.85 │      0:36:00 │  117     0   345  25.3 │
│     TOTAL │   3299 │        -0.21 │        -967.959 │        -96.8 │      0:37:00 │  774     0  2525  23.5 │
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
│     OTHER │    3299 │        -0.21 │        -967.959 │        -96.8 │      0:37:00 │  774     0  2525  23.5 │
│     TOTAL │    3299 │        -0.21 │        -967.959 │        -96.8 │      0:37:00 │  774     0  2525  23.5 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │    44 │         1.94 │         175.445 │        17.54 │      0:50:00 │   44     0     0   100 │
│      stop_loss │    81 │        -1.03 │        -146.358 │       -14.64 │      0:14:00 │    0     0    81     0 │
│    exit_signal │  3174 │        -0.22 │        -997.046 │        -99.7 │      0:38:00 │  730     0  2444  23.0 │
│          TOTAL │  3299 │        -0.21 │        -967.959 │        -96.8 │      0:37:00 │  774     0  2525  23.5 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │     44 │         1.94 │         175.445 │        17.54 │      0:50:00 │   44     0     0   100 │
│           │      stop_loss │     81 │        -1.03 │        -146.358 │       -14.64 │      0:14:00 │    0     0    81     0 │
│           │    exit_signal │   3174 │        -0.22 │        -997.046 │        -99.7 │      0:38:00 │  730     0  2444  23.0 │
│     TOTAL │                │   3299 │        -0.21 │        -967.959 │        -96.8 │      0:37:00 │  774     0  2525  23.5 │
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
│ Total/Daily Avg Trades        │ 3299 / 11.82                   │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 32.041 USDT                    │
│ Absolute profit               │ -967.959 USDT                  │
│ Total profit %                │ -96.80%                        │
│ CAGR %                        │ -98.89%                        │
│ Sortino                       │ -65.38                         │
│ Sharpe                        │ -46.49                         │
│ Calmar                        │ -6.85                          │
│ SQN                           │ -11.82                         │
│ Profit factor                 │ 0.42                           │
│ Expectancy (Ratio)            │ -0.29 (-0.44)                  │
│ Avg. daily profit             │ -3.469 USDT                    │
│ Avg. stake amount             │ 139.683 USDT                   │
│ Total trade volume            │ 922502.231 USDT                │
│                               │                                │
│ Best Pair                     │ ETH/USDT -7.85%                │
│ Worst Pair                    │ SOL/USDT -17.85%               │
│ Best trade                    │ ETH/USDT 4.13%                 │
│ Worst trade                   │ DOGE/USDT -4.13%               │
│ Best day                      │ 34.385 USDT                    │
│ Worst day                     │ -44.011 USDT                   │
│ Days win/draw/lose            │ 47 / 0 / 233                   │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 0d 02:15 / 0d 00:56 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 0d 02:00 / 0d 00:32 │
│ Max Consecutive Wins / Loss   │ 6 / 28                         │
│ Rejected Entry signals        │ 190                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 32.041 USDT                    │
│ Max balance                   │ 1003.981 USDT                  │
│ Max % of account underwater   │ 96.81%                         │
│ Absolute drawdown             │ 971.94 USDT (96.81%)           │
│ Drawdown duration             │ 279 days 12:25:00              │
│ Profit at drawdown start      │ 3.981 USDT                     │
│ Profit at drawdown end        │ -967.959 USDT                  │
│ Drawdown start                │ 2025-01-01 01:15:00            │
│ Drawdown end                  │ 2025-10-07 13:40:00            │
│ Market change                 │ 25.01%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2025-01-01 00:00:00 -> 2025-10-07 14:45:00 | Max open trades : 3
                                                            STRATEGY SUMMARY                                                             
┏━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃       Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃            Drawdown ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
│ SimpleStrategy │   3299 │        -0.21 │        -967.959 │        -96.8 │      0:37:00 │  774     0  2525  23.5 │ 971.94 USDT  96.81% │
└────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴─────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-07T18:01:24.270701",
  "strategy": "SimpleStrategy",
  "random_state": 9816,
  "total_daily_avg_trades": "3299 / 11.82",
  "absolute_profit_usdt": -967.959,
  "total_profit_pct": -96.8,
  "cagr_pct": -98.89,
  "sortino": -65.38,
  "sharpe": -46.49,
  "calmar": -6.85,
  "sqn": -11.82,
  "max_consecutive_wins_loss": "6 / 28",
  "min_balance_usdt": 32.041,
  "max_balance_usdt": 1003.981,
  "absolute_drawdown_pct": 96.81,
  "market_change_pct": 25.01,
  "win_draw_loss_winpct": "774 0 2525 23.5"
}
```
