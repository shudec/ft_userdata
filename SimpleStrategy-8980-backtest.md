# Freqtrade Backtest Log

**Strategy:** SimpleStrategy  
**Random State:** 8980  
**Timestamp:** 2025-10-08 22:05:19

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
  "random_state": 8980,
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
2025-10-08 20:02:18,046 - freqtrade - INFO - freqtrade 2025.7
2025-10-08 20:02:18,381 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-10-08 20:02:18,382 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-08 20:02:19,923 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-08 20:02:19,926 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-08 20:02:19,926 - freqtrade.loggers - INFO - Logfile configured
2025-10-08 20:02:19,927 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-08 20:02:19,927 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 15m ...
2025-10-08 20:02:19,928 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-08 20:02:19,928 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-08 20:02:19,928 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20250101-20251231 ...
2025-10-08 20:02:19,936 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-08 20:02:19,937 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-08 20:02:19,937 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-08 20:02:19,937 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-08 20:02:19,938 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-08 20:02:19,938 - freqtrade.configuration.configuration - INFO - Using pairs ['ADA/USDT', 'SOL/USDT', 'DOGE/USDT', 'BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-10-08 20:02:19,939 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20250101-20251231
2025-10-08 20:02:19,940 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-08 20:02:19,959 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-08 20:02:19,960 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-08 20:02:19,963 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-08 20:02:19,964 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-08 20:02:19,965 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-10-08 20:02:19,997 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-08 20:02:22,569 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-08 20:02:22,631 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy SimpleStrategy from '/freqtrade/user_data/strategies/SimpleStrategy.py'...
2025-10-08 20:02:22,632 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/SimpleStrategy.json
2025-10-08 20:02:22,633 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 15m.
2025-10-08 20:02:22,633 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-08 20:02:22,634 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-08 20:02:22,634 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-08 20:02:22,634 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-08 20:02:22,635 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-08 20:02:22,635 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 15m
2025-10-08 20:02:22,635 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-10-08 20:02:22,636 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-08 20:02:22,636 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-08 20:02:22,636 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-08 20:02:22,637 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-08 20:02:22,637 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-08 20:02:22,638 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'market', 'stoploss_on_exchange': False}
2025-10-08 20:02:22,638 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-08 20:02:22,638 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-08 20:02:22,639 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-08 20:02:22,639 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 200
2025-10-08 20:02:22,640 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-08 20:02:22,640 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-10-08 20:02:22,641 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-08 20:02:22,641 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-08 20:02:22,641 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-08 20:02:22,642 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-08 20:02:22,642 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-08 20:02:22,643 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-08 20:02:22,643 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-08 20:02:22,643 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-08 20:02:22,644 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-08 20:02:22,649 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-08 20:02:22,694 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-08 20:02:22,696 - freqtrade.data.history.history_utils - INFO - Using indicator startup period: 200 ...
2025-10-08 20:02:22,702 - freqtrade.data.history.datahandlers.idatahandler - WARNING - No history for ADA/USDT, spot, 15m found. Use `freqtrade download-data` to download the data
2025-10-08 20:02:22,703 - freqtrade.data.history.datahandlers.idatahandler - WARNING - No history for SOL/USDT, spot, 15m found. Use `freqtrade download-data` to download the data
2025-10-08 20:02:22,705 - freqtrade.data.history.datahandlers.idatahandler - WARNING - No history for DOGE/USDT, spot, 15m found. Use `freqtrade download-data` to download the data
2025-10-08 20:02:22,761 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 15m, data ends at 2025-09-11 18:15:00
2025-10-08 20:02:22,828 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 15m, data ends at 2025-09-11 18:15:00
2025-10-08 20:02:22,892 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 15m, data ends at 2025-09-11 18:15:00
2025-10-08 20:02:22,949 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 15m, data ends at 2025-09-11 18:15:00
2025-10-08 20:02:23,012 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 15m, data ends at 2025-09-11 18:15:00
2025-10-08 20:02:23,036 - freqtrade.optimize.backtesting - INFO - Loading data from 2024-12-29 22:00:00 up to 2025-09-11 18:15:00 (255 days).
2025-10-08 20:02:23,112 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-08 20:02:23,217 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-08 20:02:23,340 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-08 20:02:23,471 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-08 20:02:23,593 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-08 20:02:23,713 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-08 20:02:23,825 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-08 20:02:23,933 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-08 20:02:24,889 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-08 20:02:24,890 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-08 20:02:24,891 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy SimpleStrategy
2025-10-08 20:02:24,891 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 5
2025-10-08 20:02:24,892 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-10-08 20:02:24,892 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-10-08 20:02:24,892 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1
2025-10-08 20:02:24,893 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1.5
2025-10-08 20:02:24,893 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 4.5
2025-10-08 20:02:24,893 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-10-08 20:02:24,894 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-10-08 20:02:24,894 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-10-08 20:02:24,894 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-10-08 20:02:24,895 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-10-08 20:02:24,895 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower
2025-10-08 20:02:24,895 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-10-08 20:02:24,895 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-08 20:02:24,897 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-08 20:02:24,907 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-08 20:02:24,925 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-08 20:02:24,944 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-08 20:02:26,861 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-08 20:02:26,868 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-08 20:02:26,883 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-08 20:02:26,900 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-08 20:02:28,822 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-08 20:02:28,829 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-08 20:02:28,844 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-08 20:02:28,861 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-08 20:02:30,825 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-08 20:02:30,833 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-08 20:02:30,849 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-08 20:02:30,865 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-08 20:02:32,791 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-08 20:02:32,798 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-08 20:02:32,814 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-08 20:02:32,831 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-08 20:02:34,741 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2025-01-01 00:00:00 up to 2025-09-11 18:15:00 (253 days).
2025-10-08 20:05:18,664 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-08_20-05-18.meta.json"
Result for strategy SimpleStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │    139 │         0.07 │          46.694 │         4.67 │     17:59:00 │   48     0    91  34.5 │
│ ETH/USDT │    155 │        -0.01 │         -24.257 │        -2.43 │     11:41:00 │   48     0   107  31.0 │
│ BNB/USDT │    163 │        -0.25 │         -83.243 │        -8.32 │     10:05:00 │   46     0   117  28.2 │
│ LTC/USDT │    171 │        -0.42 │        -186.957 │        -18.7 │     12:29:00 │   46     0   125  26.9 │
│ XRP/USDT │    148 │        -0.25 │        -200.098 │       -20.01 │     11:19:00 │   43     0   105  29.1 │
│    TOTAL │    776 │        -0.18 │        -447.861 │       -44.79 │     12:35:00 │  231     0   545  29.8 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                           LEFT OPEN TRADES REPORT                                           
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │      1 │         0.34 │           0.932 │         0.09 │     21:45:00 │    1     0     0   100 │
│ ETH/USDT │      1 │        -0.33 │          -0.895 │        -0.09 │      1:00:00 │    0     0     1     0 │
│    TOTAL │      2 │          0.0 │           0.037 │          0.0 │     11:22:00 │    1     0     1  50.0 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                ENTER TAG STATS                                                
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │     776 │        -0.18 │        -447.861 │       -44.79 │     12:35:00 │  231     0   545  29.8 │
│     TOTAL │     776 │        -0.18 │        -447.861 │       -44.79 │     12:35:00 │  231     0   545  29.8 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │   230 │         2.99 │        2124.162 │       212.42 │     19:31:00 │  230     0     0   100 │
│     force_exit │     2 │          0.0 │           0.037 │          0.0 │     11:22:00 │    1     0     1  50.0 │
│      stop_loss │   544 │        -1.53 │       -2572.060 │      -257.21 │      9:39:00 │    0     0   544     0 │
│          TOTAL │   776 │        -0.18 │        -447.861 │       -44.79 │     12:35:00 │  231     0   545  29.8 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │    230 │         2.99 │        2124.162 │       212.42 │     19:31:00 │  230     0     0   100 │
│           │     force_exit │      2 │          0.0 │           0.037 │          0.0 │     11:22:00 │    1     0     1  50.0 │
│           │      stop_loss │    544 │        -1.53 │       -2572.060 │      -257.21 │      9:39:00 │    0     0   544     0 │
│     TOTAL │                │    776 │        -0.18 │        -447.861 │       -44.79 │     12:35:00 │  231     0   545  29.8 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2025-01-01 00:00:00             │
│ Backtesting to                │ 2025-09-11 18:15:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 776 / 3.07                      │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 552.139 USDT                    │
│ Absolute profit               │ -447.861 USDT                   │
│ Total profit %                │ -44.79%                         │
│ CAGR %                        │ -57.55%                         │
│ Sortino                       │ -9.24                           │
│ Sharpe                        │ -4.12                           │
│ Calmar                        │ -6.84                           │
│ SQN                           │ -1.96                           │
│ Profit factor                 │ 0.83                            │
│ Expectancy (Ratio)            │ -0.58 (-0.12)                   │
│ Avg. daily profit             │ -1.77 USDT                      │
│ Avg. stake amount             │ 299.546 USDT                    │
│ Total trade volume            │ 465376.656 USDT                 │
│                               │                                 │
│ Best Pair                     │ BTC/USDT 4.67%                  │
│ Worst Pair                    │ XRP/USDT -20.01%                │
│ Best trade                    │ XRP/USDT 15.83%                 │
│ Worst trade                   │ LTC/USDT -7.50%                 │
│ Best day                      │ 63.354 USDT                     │
│ Worst day                     │ -57.47 USDT                     │
│ Days win/draw/lose            │ 79 / 35 / 140                   │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 13d 15:20 / 0d 19:32 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 7d 15:45 / 0d 09:38  │
│ Max Consecutive Wins / Loss   │ 8 / 16                          │
│ Rejected Entry signals        │ 2283                            │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 531.245 USDT                    │
│ Max balance                   │ 1051.39 USDT                    │
│ Max % of account underwater   │ 49.47%                          │
│ Absolute Drawdown (Account)   │ 49.47%                          │
│ Absolute Drawdown             │ 520.145 USDT                    │
│ Drawdown high                 │ 51.39 USDT                      │
│ Drawdown low                  │ -468.755 USDT                   │
│ Drawdown Start                │ 2025-01-15 22:55:00             │
│ Drawdown End                  │ 2025-08-07 03:10:00             │
│ Market change                 │ 27.05%                          │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2025-01-01 00:00:00 -> 2025-09-11 18:15:00 | Max open trades : 3
                                                             STRATEGY SUMMARY                                                             
┏━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃       Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ SimpleStrategy │    776 │        -0.18 │        -447.861 │       -44.79 │     12:35:00 │  231     0   545  29.8 │ 520.145 USDT  49.47% │
└────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-08T22:05:19.878166",
  "strategy": "SimpleStrategy",
  "random_state": 8980,
  "total_daily_avg_trades": "776 / 3.07",
  "absolute_profit_usdt": -447.861,
  "total_profit_pct": -44.79,
  "cagr_pct": -57.55,
  "sortino": -9.24,
  "sharpe": -4.12,
  "calmar": -6.84,
  "sqn": -1.96,
  "max_consecutive_wins_loss": "8 / 16",
  "min_balance_usdt": 531.245,
  "max_balance_usdt": 1051.39,
  "market_change_pct": 27.05,
  "win_draw_loss_winpct": "231 0 545 29.8"
}
```
