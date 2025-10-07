# Freqtrade Backtest Log

**Strategy:** SimpleStrategy  
**Random State:** 7347  
**Timestamp:** 2025-10-07 17:37:41

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
  "random_state": 7347,
  "epochs": 100,
  "hyperopt_timerange": "20220101-20231231",
  "backtest_timerange": "20220101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy SimpleStrategy --timeframe 15m --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs ADA/USDT SOL/USDT DOGE/USDT BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231 --export trades
```

## Backtesting Output
```
2025-10-07 15:11:25,946 - freqtrade - INFO - freqtrade 2025.8
2025-10-07 15:11:26,981 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-07 15:11:30,503 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-07 15:11:30,510 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-07 15:11:30,511 - freqtrade.loggers - INFO - Logfile configured
2025-10-07 15:11:30,512 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-07 15:11:30,513 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 15m ...
2025-10-07 15:11:30,514 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-07 15:11:30,515 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-07 15:11:30,516 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-10-07 15:11:30,839 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-07 15:11:30,841 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-07 15:11:30,842 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-07 15:11:30,842 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-07 15:11:30,843 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-07 15:11:30,843 - freqtrade.configuration.configuration - INFO - Using pairs ['ADA/USDT', 'SOL/USDT', 'DOGE/USDT', 'BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-10-07 15:11:30,844 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-10-07 15:11:30,847 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-07 15:11:30,860 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-07 15:11:30,861 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-07 15:11:30,866 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-07 15:11:30,867 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-07 15:11:30,868 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-10-07 15:11:30,899 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-07 15:11:33,749 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-07 15:11:33,969 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy SimpleStrategy from '/freqtrade/user_data/strategies/SimpleStrategy.py'...
2025-10-07 15:11:33,972 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2025-10-07 15:11:33,974 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 15m.
2025-10-07 15:11:33,974 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-07 15:11:33,975 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-07 15:11:33,975 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-07 15:11:33,976 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-07 15:11:33,977 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-07 15:11:33,977 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 15m
2025-10-07 15:11:33,978 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-10-07 15:11:33,978 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-07 15:11:33,979 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-07 15:11:33,980 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-07 15:11:33,981 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-07 15:11:33,981 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-07 15:11:33,982 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'market', 'stoploss_on_exchange': False}
2025-10-07 15:11:33,983 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-07 15:11:33,984 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-07 15:11:33,984 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-07 15:11:33,985 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 200
2025-10-07 15:11:33,986 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-07 15:11:33,986 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-10-07 15:11:33,987 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-07 15:11:33,988 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-07 15:11:33,988 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-07 15:11:33,989 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-07 15:11:33,989 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-07 15:11:33,990 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-07 15:11:33,991 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-07 15:11:33,991 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-07 15:11:33,992 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-07 15:11:34,058 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-07 15:11:34,103 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-07 15:11:34,315 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 15:11:34,560 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 15:11:34,735 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 15:11:34,944 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 15:11:35,193 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 15:11:35,372 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 15:11:35,547 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 15:11:35,729 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-07 15:11:35,848 - freqtrade.optimize.backtesting - INFO - Loading data from 2021-12-29 22:00:00 up to 2025-10-07 14:45:00 (1377 days).
2025-10-07 15:11:36,130 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 15:11:36,575 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 15:11:37,097 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 15:11:37,664 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 15:11:38,290 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 15:11:38,851 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 15:11:39,290 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 15:11:39,813 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-07 15:11:50,160 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-07 15:11:50,184 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-07 15:11:50,186 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy SimpleStrategy
2025-10-07 15:11:50,187 - freqtrade.strategy.hyper - INFO - No params for buy found, using default values.
2025-10-07 15:11:50,188 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_adx_threshold = 5
2025-10-07 15:11:50,189 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-10-07 15:11:50,189 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-10-07 15:11:50,190 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): volume_factor = 0.5
2025-10-07 15:11:50,190 - freqtrade.strategy.hyper - INFO - No params for sell found, using default values.
2025-10-07 15:11:50,191 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): atr_stoploss_multiplier = 1.5
2025-10-07 15:11:50,192 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): custom_sell_atr_factor = 4.5
2025-10-07 15:11:50,192 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): lookback_period_for_stoploss = 5
2025-10-07 15:11:50,194 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): stoploss_margin = 0.999
2025-10-07 15:11:50,194 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): take_profit_multiplier = 2
2025-10-07 15:11:50,195 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): trailing_custom_stop = True
2025-10-07 15:11:50,195 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_sell = True
2025-10-07 15:11:50,196 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_stoploss_param = True
2025-10-07 15:11:50,196 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_stoploss_type = lower
2025-10-07 15:11:50,197 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_sell_signal_param = True
2025-10-07 15:11:50,198 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-07 15:11:50,208 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 15:11:50,234 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 15:11:50,294 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 15:11:50,323 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 15:11:50,586 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 15:11:50,610 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 15:11:50,646 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 15:11:50,673 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 15:11:50,795 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 15:11:50,814 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 15:11:50,837 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 15:11:50,866 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 15:11:51,003 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 15:11:51,022 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 15:11:51,047 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 15:11:51,078 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 15:11:51,232 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 15:11:51,255 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 15:11:51,279 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 15:11:51,309 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 15:11:51,423 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 15:11:51,458 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 15:11:51,530 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 15:11:51,594 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 15:11:51,750 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 15:11:51,776 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 15:11:51,805 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 15:11:51,843 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 15:11:51,950 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-07 15:11:51,974 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-07 15:11:51,998 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-07 15:11:52,027 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-07 15:11:52,448 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-10-07 14:45:00 (1375 days).
2025-10-07 15:37:37,854 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-07_15-37-37.meta.json"
Result for strategy SimpleStrategy
                                              BACKTESTING REPORT                                              
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  SOL/USDT │    527 │        -0.25 │         -22.769 │        -2.28 │      4:45:00 │  181     0   346  34.3 │
│  BNB/USDT │    374 │        -0.26 │         -43.272 │        -4.33 │      4:17:00 │  106     0   268  28.3 │
│  ETH/USDT │    386 │        -0.22 │        -110.665 │       -11.07 │      4:14:00 │  114     0   272  29.5 │
│  BTC/USDT │    453 │        -0.21 │        -112.332 │       -11.23 │      4:32:00 │  122     0   331  26.9 │
│  XRP/USDT │    521 │        -0.27 │        -114.043 │        -11.4 │      4:09:00 │  153     0   368  29.4 │
│  LTC/USDT │    477 │        -0.29 │        -149.032 │        -14.9 │      4:07:00 │  158     0   319  33.1 │
│  ADA/USDT │    624 │        -0.24 │        -203.963 │        -20.4 │      4:22:00 │  195     0   429  31.3 │
│ DOGE/USDT │   1836 │        -0.23 │        -241.842 │       -24.18 │      4:36:00 │  611     0  1225  33.3 │
│     TOTAL │   5198 │        -0.24 │        -997.918 │       -99.79 │      4:26:00 │ 1640     0  3558  31.6 │
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
│     OTHER │    5198 │        -0.24 │        -997.918 │       -99.79 │      4:26:00 │ 1640     0  3558  31.6 │
│     TOTAL │    5198 │        -0.24 │        -997.918 │       -99.79 │      4:26:00 │ 1640     0  3558  31.6 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │   680 │         2.64 │        2027.679 │       202.77 │      4:41:00 │  680     0     0   100 │
│    exit_signal │  2510 │        -0.05 │        -174.083 │       -17.41 │      5:39:00 │  960     0  1550  38.2 │
│      stop_loss │  2008 │        -1.46 │       -2851.513 │      -285.15 │      2:51:00 │    0     0  2008     0 │
│          TOTAL │  5198 │        -0.24 │        -997.918 │       -99.79 │      4:26:00 │ 1640     0  3558  31.6 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │    680 │         2.64 │        2027.679 │       202.77 │      4:41:00 │  680     0     0   100 │
│           │    exit_signal │   2510 │        -0.05 │        -174.083 │       -17.41 │      5:39:00 │  960     0  1550  38.2 │
│           │      stop_loss │   2008 │        -1.46 │       -2851.513 │      -285.15 │      2:51:00 │    0     0  2008     0 │
│     TOTAL │                │   5198 │        -0.24 │        -997.918 │       -99.79 │      4:26:00 │ 1640     0  3558  31.6 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2025-10-07 14:45:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 5198 / 3.78                    │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 2.082 USDT                     │
│ Absolute profit               │ -997.918 USDT                  │
│ Total profit %                │ -99.79%                        │
│ CAGR %                        │ -80.58%                        │
│ Sortino                       │ -6.46                          │
│ Sharpe                        │ -4.44                          │
│ Calmar                        │ -1.39                          │
│ SQN                           │ -4.43                          │
│ Profit factor                 │ 0.74                           │
│ Expectancy (Ratio)            │ -0.19 (-0.18)                  │
│ Avg. daily profit             │ -0.726 USDT                    │
│ Avg. stake amount             │ 94.794 USDT                    │
│ Total trade volume            │ 986447.972 USDT                │
│                               │                                │
│ Best Pair                     │ SOL/USDT -2.28%                │
│ Worst Pair                    │ DOGE/USDT -24.18%              │
│ Best trade                    │ SOL/USDT 20.30%                │
│ Worst trade                   │ SOL/USDT -13.51%               │
│ Best day                      │ 75.71 USDT                     │
│ Worst day                     │ -75.943 USDT                   │
│ Days win/draw/lose            │ 492 / 82 / 802                 │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 1d 15:30 / 0d 06:26 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 1d 12:00 / 0d 03:31 │
│ Max Consecutive Wins / Loss   │ 8 / 24                         │
│ Rejected Entry signals        │ 841                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 2.079 USDT                     │
│ Max balance                   │ 1061.041 USDT                  │
│ Max % of account underwater   │ 99.80%                         │
│ Absolute drawdown             │ 1058.962 USDT (99.80%)         │
│ Drawdown duration             │ 1360 days 02:15:00             │
│ Profit at drawdown start      │ 61.041 USDT                    │
│ Profit at drawdown end        │ -997.921 USDT                  │
│ Drawdown start                │ 2022-01-14 21:55:00            │
│ Drawdown end                  │ 2025-10-06 00:10:00            │
│ Market change                 │ 76.94%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-10-07 14:45:00 | Max open trades : 3
                                                             STRATEGY SUMMARY                                                              
┏━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃       Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃              Drawdown ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ SimpleStrategy │   5198 │        -0.24 │        -997.918 │       -99.79 │      4:26:00 │ 1640     0  3558  31.6 │ 1058.962 USDT  99.80% │
└────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴───────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-07T17:37:41.653062",
  "strategy": "SimpleStrategy",
  "random_state": 7347,
  "total_daily_avg_trades": "5198 / 3.78",
  "absolute_profit_usdt": -997.918,
  "total_profit_pct": -99.79,
  "cagr_pct": -80.58,
  "sortino": -6.46,
  "sharpe": -4.44,
  "calmar": -1.39,
  "sqn": -4.43,
  "max_consecutive_wins_loss": "8 / 24",
  "min_balance_usdt": 2.079,
  "max_balance_usdt": 1061.041,
  "absolute_drawdown_pct": 99.8,
  "market_change_pct": 76.94,
  "win_draw_loss_winpct": "1640 0 3558 31.6"
}
```
