# Freqtrade Backtest Log

**Strategy:** KeltnerChannelStrategy  
**Random State:** 8564  
**Timestamp:** 2025-10-09 17:47:43

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
  "random_state": 8564,
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
2025-10-09 15:45:34,251 - freqtrade - INFO - freqtrade 2025.8
2025-10-09 15:45:34,679 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-09 15:45:36,629 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-09 15:45:36,638 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-09 15:45:36,639 - freqtrade.loggers - INFO - Logfile configured
2025-10-09 15:45:36,640 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-09 15:45:36,640 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 15m ...
2025-10-09 15:45:36,641 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-09 15:45:36,642 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-09 15:45:36,643 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-10-09 15:45:36,893 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-09 15:45:36,896 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-09 15:45:36,897 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-09 15:45:36,897 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-09 15:45:36,898 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-09 15:45:36,899 - freqtrade.configuration.configuration - INFO - Using pairs ['ADA/USDT', 'SOL/USDT', 'DOGE/USDT', 'BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-10-09 15:45:36,899 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-10-09 15:45:36,901 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-09 15:45:36,915 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-09 15:45:36,916 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-09 15:45:36,920 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-09 15:45:36,921 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-09 15:45:36,922 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-10-09 15:45:36,948 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-09 15:45:41,694 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-09 15:45:41,893 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy KeltnerChannelStrategy from '/freqtrade/user_data/strategies/KeltnerChannelStrategy.py'...
2025-10-09 15:45:41,895 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/KeltnerChannelStrategy.json
2025-10-09 15:45:41,900 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 15m.
2025-10-09 15:45:41,900 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-09 15:45:41,901 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-09 15:45:41,901 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-09 15:45:41,902 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-09 15:45:41,903 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-09 15:45:41,904 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 15m
2025-10-09 15:45:41,905 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-10-09 15:45:41,905 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-09 15:45:41,906 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-09 15:45:41,907 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-09 15:45:41,907 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-09 15:45:41,908 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-09 15:45:41,909 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'market', 'stoploss_on_exchange': False}
2025-10-09 15:45:41,909 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-09 15:45:41,910 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-09 15:45:41,911 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-09 15:45:41,911 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 200
2025-10-09 15:45:41,912 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-09 15:45:41,913 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-10-09 15:45:41,913 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-09 15:45:41,914 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-09 15:45:41,915 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-09 15:45:41,915 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-09 15:45:41,916 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-09 15:45:41,917 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-09 15:45:41,917 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-09 15:45:41,918 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-09 15:45:41,919 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-09 15:45:41,944 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-09 15:45:41,990 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-09 15:45:42,183 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 15:45:42,392 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 15:45:42,557 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 15:45:42,772 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 15:45:42,965 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 15:45:43,143 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 15:45:43,318 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 15:45:43,502 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 15m, data ends at 2025-10-07 14:45:00
2025-10-09 15:45:43,583 - freqtrade.optimize.backtesting - INFO - Loading data from 2021-12-29 22:00:00 up to 2025-10-07 14:45:00 (1377 days).
2025-10-09 15:45:43,877 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 15:45:44,345 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 15:45:44,877 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 15:45:45,513 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 15:45:46,092 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 15:45:46,711 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 15:45:47,253 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 15:45:47,866 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-10-07 15:00:00
2025-10-09 15:45:58,495 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-09 15:45:58,508 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-09 15:45:58,508 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy KeltnerChannelStrategy
2025-10-09 15:45:58,510 - freqtrade.strategy.hyper - INFO - Strategy Parameter: adx_entry_param = 30
2025-10-09 15:45:58,511 - freqtrade.strategy.hyper - INFO - Strategy Parameter: chop_entry_param = 20
2025-10-09 15:45:58,512 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 5
2025-10-09 15:45:58,513 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-10-09 15:45:58,513 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-10-09 15:45:58,514 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-10-09 15:45:58,515 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 2.5
2025-10-09 15:45:58,515 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 4.5
2025-10-09 15:45:58,516 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-10-09 15:45:58,517 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-10-09 15:45:58,517 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-10-09 15:45:58,519 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-10-09 15:45:58,522 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-10-09 15:45:58,524 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = candle_close_atr
2025-10-09 15:45:58,525 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-10-09 15:45:58,526 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-09 15:45:58,537 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 15:45:58,582 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 15:45:58,660 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 15:45:58,711 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 15:46:02,346 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 15:46:02,363 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 15:46:02,401 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 15:46:02,429 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 15:46:05,410 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 15:46:05,438 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 15:46:05,464 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 15:46:05,497 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 15:46:08,460 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 15:46:08,485 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 15:46:08,509 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 15:46:08,555 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 15:46:11,560 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 15:46:11,591 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 15:46:11,617 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 15:46:11,648 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 15:46:14,469 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 15:46:14,496 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 15:46:14,517 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 15:46:14,555 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 15:46:17,539 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 15:46:17,557 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 15:46:17,583 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 15:46:17,616 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 15:46:20,674 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-09 15:46:20,699 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-10-06 00:00:00
2025-10-09 15:46:20,720 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-09 15:46:20,750 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-10-07 08:00:00
2025-10-09 15:46:23,838 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-10-07 14:45:00 (1375 days).
2025-10-09 15:47:39,994 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-09_15-47-39.meta.json"
Result for strategy KeltnerChannelStrategy
                                              BACKTESTING REPORT                                              
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  BTC/USDT │     34 │         0.55 │          93.612 │         9.36 │      5:08:00 │   17     0    17  50.0 │
│  BNB/USDT │     23 │          0.5 │          52.378 │         5.24 │     15:37:00 │   11     0    12  47.8 │
│  ADA/USDT │     24 │         0.23 │          38.395 │         3.84 │      8:25:00 │    9     0    15  37.5 │
│  SOL/USDT │     14 │         0.07 │          15.576 │         1.56 │     15:34:00 │    5     0     9  35.7 │
│ DOGE/USDT │     22 │        -0.16 │         -17.365 │        -1.74 │      4:30:00 │    5     0    17  22.7 │
│  LTC/USDT │     17 │        -0.23 │         -23.078 │        -2.31 │     15:01:00 │    6     0    11  35.3 │
│  ETH/USDT │     22 │        -0.26 │         -31.836 │        -3.18 │     14:25:00 │    6     0    16  27.3 │
│  XRP/USDT │     36 │        -1.14 │        -163.565 │       -16.36 │     11:15:00 │    9     0    27  25.0 │
│     TOTAL │    192 │        -0.09 │         -35.884 │        -3.59 │     10:34:00 │   68     0   124  35.4 │
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
│     OTHER │     192 │        -0.09 │         -35.884 │        -3.59 │     10:34:00 │   68     0   124  35.4 │
│     TOTAL │     192 │        -0.09 │         -35.884 │        -3.59 │     10:34:00 │   68     0   124  35.4 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │    68 │          3.9 │        1179.119 │       117.91 │     11:46:00 │   68     0     0   100 │
│      stop_loss │   124 │        -2.28 │       -1215.004 │       -121.5 │      9:55:00 │    0     0   124     0 │
│          TOTAL │   192 │        -0.09 │         -35.884 │        -3.59 │     10:34:00 │   68     0   124  35.4 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │     68 │          3.9 │        1179.119 │       117.91 │     11:46:00 │   68     0     0   100 │
│           │      stop_loss │    124 │        -2.28 │       -1215.004 │       -121.5 │      9:55:00 │    0     0   124     0 │
│     TOTAL │                │    192 │        -0.09 │         -35.884 │        -3.59 │     10:34:00 │   68     0   124  35.4 │
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
│ Total/Daily Avg Trades        │ 192 / 0.14                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 964.116 USDT                   │
│ Absolute profit               │ -35.884 USDT                   │
│ Total profit %                │ -3.59%                         │
│ CAGR %                        │ -0.97%                         │
│ Sortino                       │ -0.09                          │
│ Sharpe                        │ -0.03                          │
│ Calmar                        │ -0.23                          │
│ SQN                           │ -0.17                          │
│ Profit factor                 │ 0.97                           │
│ Expectancy (Ratio)            │ -0.19 (-0.02)                  │
│ Avg. daily profit             │ -0.026 USDT                    │
│ Avg. stake amount             │ 451.823 USDT                   │
│ Total trade volume            │ 173811.582 USDT                │
│                               │                                │
│ Best Pair                     │ BTC/USDT 9.36%                 │
│ Worst Pair                    │ XRP/USDT -16.36%               │
│ Best trade                    │ ADA/USDT 14.66%                │
│ Worst trade                   │ XRP/USDT -11.54%               │
│ Best day                      │ 45.412 USDT                    │
│ Worst day                     │ -37.064 USDT                   │
│ Days win/draw/lose            │ 54 / 1210 / 96                 │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 3d 11:30 / 0d 11:46 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 3d 22:05 / 0d 09:55 │
│ Max Consecutive Wins / Loss   │ 4 / 9                          │
│ Rejected Entry signals        │ 15                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 869.688 USDT                   │
│ Max balance                   │ 1104.423 USDT                  │
│ Max % of account underwater   │ 21.25%                         │
│ Absolute drawdown             │ 234.735 USDT (21.25%)          │
│ Drawdown duration             │ 848 days 16:10:00              │
│ Profit at drawdown start      │ 104.423 USDT                   │
│ Profit at drawdown end        │ -130.312 USDT                  │
│ Drawdown start                │ 2022-04-25 17:05:00            │
│ Drawdown end                  │ 2024-08-21 09:15:00            │
│ Market change                 │ 76.94%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-10-07 14:45:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ KeltnerChannelStrategy │    192 │        -0.09 │         -35.884 │        -3.59 │     10:34:00 │   68     0   124  35.4 │ 234.735 USDT  21.25% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-09T17:47:42.980117",
  "strategy": "KeltnerChannelStrategy",
  "random_state": 8564,
  "total_daily_avg_trades": "192 / 0.14",
  "absolute_profit_usdt": -35.884,
  "total_profit_pct": -3.59,
  "cagr_pct": -0.97,
  "sortino": -0.09,
  "sharpe": -0.03,
  "calmar": -0.23,
  "sqn": -0.17,
  "max_consecutive_wins_loss": "4 / 9",
  "min_balance_usdt": 869.688,
  "max_balance_usdt": 1104.423,
  "absolute_drawdown_pct": 21.25,
  "market_change_pct": 76.94,
  "win_draw_loss_winpct": "68 0 124 35.4"
}
```
