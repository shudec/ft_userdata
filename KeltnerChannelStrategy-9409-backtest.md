# Freqtrade Backtest Log

**Strategy:** KeltnerChannelStrategy  
**Random State:** 9409  
**Timestamp:** 2025-10-09 18:51:48

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
  "random_state": 9409,
  "epochs": 100,
  "hyperopt_timerange": "20220101-20231231",
  "backtest_timerange": "20220101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy KeltnerChannelStrategy --timeframe 15m --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs ADA/USDT SOL/USDT DOGE/USDT BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231 --export trades
```

## Backtesting Output
```
2025-10-09 16:22:15,011 - freqtrade - INFO - freqtrade 2025.8
2025-10-09 16:22:15,952 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-09 16:22:19,251 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-09 16:22:19,259 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-09 16:22:19,260 - freqtrade.loggers - INFO - Logfile configured
2025-10-09 16:22:19,260 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-09 16:22:19,261 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 15m ...
2025-10-09 16:22:19,262 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-09 16:22:19,262 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-09 16:22:19,263 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-10-09 16:22:19,528 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-09 16:22:19,530 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-09 16:22:19,531 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-09 16:22:19,531 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-09 16:22:19,532 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-09 16:22:19,533 - freqtrade.configuration.configuration - INFO - Using pairs ['ADA/USDT', 'SOL/USDT', 'DOGE/USDT', 'BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-10-09 16:22:19,533 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-10-09 16:22:19,536 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-09 16:22:19,550 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-09 16:22:19,551 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-09 16:22:19,553 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-09 16:22:19,555 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-09 16:22:19,555 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-10-09 16:22:19,583 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-09 16:22:22,499 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-09 16:22:22,696 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy KeltnerChannelStrategy from '/freqtrade/user_data/strategies/KeltnerChannelStrategy.py'...
2025-10-09 16:22:22,698 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/KeltnerChannelStrategy.json
2025-10-09 16:22:22,704 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 15m.
2025-10-09 16:22:22,704 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-09 16:22:22,705 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-09 16:22:22,705 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-09 16:22:22,706 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-09 16:22:22,707 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-09 16:22:22,707 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 15m
2025-10-09 16:22:22,708 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-10-09 16:22:22,708 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-09 16:22:22,709 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-09 16:22:22,709 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-09 16:22:22,710 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-09 16:22:22,712 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-09 16:22:22,713 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'market', 'stoploss_on_exchange': False}
2025-10-09 16:22:22,714 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-09 16:22:22,714 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-09 16:22:22,715 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-09 16:22:22,716 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 200
2025-10-09 16:22:22,716 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-09 16:22:22,717 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-10-09 16:22:22,717 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-09 16:22:22,718 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-09 16:22:22,719 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-09 16:22:22,719 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-09 16:22:22,720 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-09 16:22:22,721 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-09 16:22:22,721 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-09 16:22:22,722 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-09 16:22:22,723 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-09 16:22:22,759 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-09 16:22:22,800 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-09 16:22:22,962 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 16:22:23,155 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 16:22:23,340 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 16:22:23,536 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 16:22:23,708 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 16:22:23,881 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 16:22:24,026 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 16:22:24,216 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 16:22:24,291 - freqtrade.optimize.backtesting - INFO - Loading data from 2021-12-29 22:00:00 up to 2025-10-07 14:45:00 (1377 days).
2025-10-09 16:22:24,622 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 16:22:25,056 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 16:22:25,735 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 16:22:26,625 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 16:22:27,240 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 16:22:27,871 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 16:22:28,413 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 16:22:28,943 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 16:22:39,717 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-09 16:22:39,735 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-09 16:22:39,735 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy KeltnerChannelStrategy
2025-10-09 16:22:39,736 - freqtrade.strategy.hyper - INFO - Strategy Parameter: adx_entry_param = 25
2025-10-09 16:22:39,737 - freqtrade.strategy.hyper - INFO - Strategy Parameter: chop_entry_param = 40
2025-10-09 16:22:39,737 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 5
2025-10-09 16:22:39,738 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-10-09 16:22:39,738 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-10-09 16:22:39,739 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-10-09 16:22:39,740 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 2.5
2025-10-09 16:22:39,740 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 4.5
2025-10-09 16:22:39,741 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-10-09 16:22:39,741 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-10-09 16:22:39,742 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-10-09 16:22:39,742 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-10-09 16:22:39,743 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-10-09 16:22:39,744 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = candle_close_atr
2025-10-09 16:22:39,744 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-10-09 16:22:39,745 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-09 16:22:39,754 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 16:22:39,785 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 16:22:39,834 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 16:22:39,871 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 16:22:43,290 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 16:22:43,308 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 16:22:43,339 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 16:22:43,379 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 16:22:46,604 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 16:22:46,626 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 16:22:46,650 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 16:22:46,687 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 16:22:49,884 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 16:22:49,913 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 16:22:49,941 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 16:22:49,975 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 16:22:53,270 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 16:22:53,306 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 16:22:53,339 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 16:22:53,372 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 16:22:56,441 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 16:22:56,479 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 16:22:56,514 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 16:22:56,553 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 16:22:59,844 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 16:22:59,875 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 16:22:59,903 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 16:22:59,937 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 16:23:03,233 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 16:23:03,262 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 16:23:03,285 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 16:23:03,318 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 16:23:06,463 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-10-07 14:45:00 (1375 days).
2025-10-09 16:51:42,846 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-09_16-51-42.meta.json"
Result for strategy KeltnerChannelStrategy
                                              BACKTESTING REPORT                                              
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  BNB/USDT │    353 │        -0.05 │           5.340 │         0.53 │      9:58:00 │  117     0   236  33.1 │
│  BTC/USDT │    451 │        -0.16 │         -10.594 │        -1.06 │     10:13:00 │  140     0   311  31.0 │
│  XRP/USDT │    369 │        -0.25 │        -102.017 │        -10.2 │      9:17:00 │  106     0   263  28.7 │
│ DOGE/USDT │    520 │        -0.33 │        -120.663 │       -12.07 │      9:05:00 │  143     0   377  27.5 │
│  ETH/USDT │    415 │        -0.27 │        -136.213 │       -13.62 │     10:03:00 │  114     0   301  27.5 │
│  LTC/USDT │    333 │        -0.41 │        -142.854 │       -14.29 │     11:08:00 │   92     0   241  27.6 │
│  ADA/USDT │    528 │        -0.17 │        -233.696 │       -23.37 │      9:42:00 │  153     0   375  29.0 │
│  SOL/USDT │    483 │        -0.14 │        -235.286 │       -23.53 │     10:22:00 │  150     0   333  31.1 │
│     TOTAL │   3452 │        -0.22 │        -975.983 │        -97.6 │      9:56:00 │ 1015     0  2437  29.4 │
└───────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                           LEFT OPEN TRADES REPORT                                           
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         0.22 │           0.026 │          0.0 │      4:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         0.22 │           0.026 │          0.0 │      4:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                ENTER TAG STATS                                                
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │    3452 │        -0.22 │        -975.983 │        -97.6 │      9:56:00 │ 1015     0  2437  29.4 │
│     TOTAL │    3452 │        -0.22 │        -975.983 │        -97.6 │      9:56:00 │ 1015     0  2437  29.4 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │  1014 │         3.65 │        4128.570 │       412.86 │     13:44:00 │ 1014     0     0   100 │
│     force_exit │     1 │         0.22 │           0.026 │          0.0 │      4:00:00 │    1     0     0   100 │
│      stop_loss │  2437 │        -1.83 │       -5104.579 │      -510.46 │      8:21:00 │    0     0  2437     0 │
│          TOTAL │  3452 │        -0.22 │        -975.983 │        -97.6 │      9:56:00 │ 1015     0  2437  29.4 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │   1014 │         3.65 │        4128.570 │       412.86 │     13:44:00 │ 1014     0     0   100 │
│           │     force_exit │      1 │         0.22 │           0.026 │          0.0 │      4:00:00 │    1     0     0   100 │
│           │      stop_loss │   2437 │        -1.83 │       -5104.579 │      -510.46 │      8:21:00 │    0     0  2437     0 │
│     TOTAL │                │   3452 │        -0.22 │        -975.983 │        -97.6 │      9:56:00 │ 1015     0  2437  29.4 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00             │
│ Backtesting to                │ 2025-10-07 14:45:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 3452 / 2.51                     │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 24.017 USDT                     │
│ Absolute profit               │ -975.983 USDT                   │
│ Total profit %                │ -97.60%                         │
│ CAGR %                        │ -62.84%                         │
│ Sortino                       │ -4.45                           │
│ Sharpe                        │ -2.66                           │
│ Calmar                        │ -1.39                           │
│ SQN                           │ -3.26                           │
│ Profit factor                 │ 0.81                            │
│ Expectancy (Ratio)            │ -0.28 (-0.13)                   │
│ Avg. daily profit             │ -0.71 USDT                      │
│ Avg. stake amount             │ 105.671 USDT                    │
│ Total trade volume            │ 730035.99 USDT                  │
│                               │                                 │
│ Best Pair                     │ BNB/USDT 0.53%                  │
│ Worst Pair                    │ SOL/USDT -23.53%                │
│ Best trade                    │ SOL/USDT 23.03%                 │
│ Worst trade                   │ ADA/USDT -13.36%                │
│ Best day                      │ 86.79 USDT                      │
│ Worst day                     │ -39.523 USDT                    │
│ Days win/draw/lose            │ 408 / 182 / 785                 │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 14d 01:20 / 0d 13:43 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 6d 19:20 / 0d 08:21  │
│ Max Consecutive Wins / Loss   │ 11 / 25                         │
│ Rejected Entry signals        │ 6924                            │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 23.154 USDT                     │
│ Max balance                   │ 992.852 USDT                    │
│ Max % of account underwater   │ 97.68%                          │
│ Absolute drawdown             │ 976.846 USDT (97.68%)           │
│ Drawdown duration             │ 1366 days 23:55:00              │
│ Profit at drawdown start      │ -7.148 USDT                     │
│ Profit at drawdown end        │ -976.846 USDT                   │
│ Drawdown start                │ 2022-01-02 01:50:00             │
│ Drawdown end                  │ 2025-09-30 01:45:00             │
│ Market change                 │ 76.94%                          │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-10-07 14:45:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ KeltnerChannelStrategy │   3452 │        -0.22 │        -975.983 │        -97.6 │      9:56:00 │ 1015     0  2437  29.4 │ 976.846 USDT  97.68% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-09T18:51:48.352133",
  "strategy": "KeltnerChannelStrategy",
  "random_state": 9409,
  "total_daily_avg_trades": "3452 / 2.51",
  "absolute_profit_usdt": -975.983,
  "total_profit_pct": -97.6,
  "cagr_pct": -62.84,
  "sortino": -4.45,
  "sharpe": -2.66,
  "calmar": -1.39,
  "sqn": -3.26,
  "max_consecutive_wins_loss": "11 / 25",
  "min_balance_usdt": 23.154,
  "max_balance_usdt": 992.852,
  "absolute_drawdown_pct": 97.68,
  "market_change_pct": 76.94,
  "win_draw_loss_winpct": "1015 0 2437 29.4"
}
```
