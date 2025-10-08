# Freqtrade Backtest Log

**Strategy:** KeltnerChannelStrategy  
**Random State:** 6161  
**Timestamp:** 2025-10-08 22:10:23

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
  "random_state": 6161,
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
2025-10-08 20:06:23,389 - freqtrade - INFO - freqtrade 2025.7
2025-10-08 20:06:23,806 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-10-08 20:06:23,807 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-08 20:06:25,241 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-08 20:06:25,244 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-08 20:06:25,244 - freqtrade.loggers - INFO - Logfile configured
2025-10-08 20:06:25,245 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-08 20:06:25,245 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 15m ...
2025-10-08 20:06:25,245 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-08 20:06:25,246 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-08 20:06:25,246 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20250101-20251231 ...
2025-10-08 20:06:25,254 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-08 20:06:25,254 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-08 20:06:25,255 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-08 20:06:25,255 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-08 20:06:25,255 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-08 20:06:25,256 - freqtrade.configuration.configuration - INFO - Using pairs ['ADA/USDT', 'SOL/USDT', 'DOGE/USDT', 'BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-10-08 20:06:25,256 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20250101-20251231
2025-10-08 20:06:25,257 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-08 20:06:25,276 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-08 20:06:25,277 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-08 20:06:25,281 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-08 20:06:25,281 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-08 20:06:25,282 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-10-08 20:06:25,315 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-08 20:06:27,818 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-08 20:06:27,871 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy KeltnerChannelStrategy from '/freqtrade/user_data/strategies/KeltnerChannelStrategy.py'...
2025-10-08 20:06:27,871 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/KeltnerChannelStrategy.json
2025-10-08 20:06:27,873 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 15m.
2025-10-08 20:06:27,873 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-08 20:06:27,874 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-08 20:06:27,874 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-08 20:06:27,875 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-08 20:06:27,875 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-08 20:06:27,876 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 15m
2025-10-08 20:06:27,876 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-10-08 20:06:27,877 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-08 20:06:27,877 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-08 20:06:27,878 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-08 20:06:27,878 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-08 20:06:27,878 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-08 20:06:27,879 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'market', 'stoploss_on_exchange': False}
2025-10-08 20:06:27,879 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-08 20:06:27,880 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-08 20:06:27,880 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-08 20:06:27,880 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 200
2025-10-08 20:06:27,881 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-08 20:06:27,881 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: False
2025-10-08 20:06:27,882 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-08 20:06:27,882 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-08 20:06:27,882 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-08 20:06:27,883 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-08 20:06:27,883 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-08 20:06:27,884 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-08 20:06:27,884 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-08 20:06:27,885 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-08 20:06:27,885 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-08 20:06:27,890 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-08 20:06:27,946 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-08 20:06:27,948 - freqtrade.data.history.history_utils - INFO - Using indicator startup period: 200 ...
2025-10-08 20:06:27,952 - freqtrade.data.history.datahandlers.idatahandler - WARNING - No history for ADA/USDT, spot, 15m found. Use `freqtrade download-data` to download the data
2025-10-08 20:06:27,954 - freqtrade.data.history.datahandlers.idatahandler - WARNING - No history for SOL/USDT, spot, 15m found. Use `freqtrade download-data` to download the data
2025-10-08 20:06:27,955 - freqtrade.data.history.datahandlers.idatahandler - WARNING - No history for DOGE/USDT, spot, 15m found. Use `freqtrade download-data` to download the data
2025-10-08 20:06:28,005 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 15m, data ends at 2025-09-11 18:15:00
2025-10-08 20:06:28,070 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 15m, data ends at 2025-09-11 18:15:00
2025-10-08 20:06:28,128 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 15m, data ends at 2025-09-11 18:15:00
2025-10-08 20:06:28,182 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 15m, data ends at 2025-09-11 18:15:00
2025-10-08 20:06:28,239 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 15m, data ends at 2025-09-11 18:15:00
2025-10-08 20:06:28,266 - freqtrade.optimize.backtesting - INFO - Loading data from 2024-12-29 22:00:00 up to 2025-09-11 18:15:00 (255 days).
2025-10-08 20:06:28,331 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-08 20:06:28,428 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-08 20:06:28,523 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-08 20:06:28,634 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-08 20:06:28,762 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-08 20:06:28,871 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-08 20:06:28,979 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-08 20:06:29,090 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-08 20:06:30,040 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-08 20:06:30,041 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-08 20:06:30,041 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy KeltnerChannelStrategy
2025-10-08 20:06:30,042 - freqtrade.strategy.hyper - INFO - Strategy Parameter: adx_entry_param = 30
2025-10-08 20:06:30,042 - freqtrade.strategy.hyper - INFO - Strategy Parameter: chop_entry_param = 50
2025-10-08 20:06:30,042 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 5
2025-10-08 20:06:30,043 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-10-08 20:06:30,043 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-10-08 20:06:30,043 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-10-08 20:06:30,044 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1.5
2025-10-08 20:06:30,044 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 4.5
2025-10-08 20:06:30,044 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-10-08 20:06:30,045 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-10-08 20:06:30,045 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-10-08 20:06:30,045 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-10-08 20:06:30,045 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-10-08 20:06:30,046 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = candle_close_atr
2025-10-08 20:06:30,046 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-10-08 20:06:30,046 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-08 20:06:30,048 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-08 20:06:30,058 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-08 20:06:30,077 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-08 20:06:30,095 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-08 20:06:30,627 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-08 20:06:30,634 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-08 20:06:30,652 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-08 20:06:30,673 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-08 20:06:31,217 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-08 20:06:31,225 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-08 20:06:31,240 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-08 20:06:31,259 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-08 20:06:31,760 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-08 20:06:31,767 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-08 20:06:31,784 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-08 20:06:31,800 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-08 20:06:32,330 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2024-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-08 20:06:32,338 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-08 20:06:32,356 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2024-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-08 20:06:32,373 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-08 20:06:32,892 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2025-01-01 00:00:00 up to 2025-09-11 18:15:00 (253 days).
2025-10-08 20:10:22,506 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-08_20-10-22.meta.json"
Result for strategy KeltnerChannelStrategy
                                                BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │     15 │         2.45 │          93.139 │         9.31 │  12 days, 7:39:00 │    1     0    14   6.7 │
│ BTC/USDT │     26 │         0.07 │          22.681 │         2.27 │   6 days, 3:46:00 │    1     0    25   3.8 │
│ ETH/USDT │     16 │        -1.13 │         -56.250 │        -5.62 │   3 days, 9:09:00 │    0     0    16     0 │
│ XRP/USDT │     16 │         1.22 │         -95.863 │        -9.59 │ 11 days, 22:02:00 │    1     0    15   6.2 │
│ LTC/USDT │     20 │        -1.46 │        -100.581 │       -10.06 │    1 day, 1:38:00 │    0     0    20     0 │
│    TOTAL │     93 │         0.12 │        -136.874 │       -13.69 │  6 days, 13:41:00 │    3     0    90   3.2 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                              LEFT OPEN TRADES REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃       Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │        49.61 │         145.284 │        14.53 │  128 days, 3:45:00 │    1     0     0   100 │
│ BTC/USDT │      1 │        32.37 │         100.583 │        10.06 │ 143 days, 17:45:00 │    1     0     0   100 │
│ XRP/USDT │      1 │        46.48 │           2.487 │         0.25 │  152 days, 9:50:00 │    1     0     0   100 │
│    TOTAL │      3 │        42.82 │         248.354 │        24.84 │ 141 days, 10:27:00 │    3     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────────┴────────────────────────┘
                                                  ENTER TAG STATS                                                  
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │      93 │         0.12 │        -136.874 │       -13.69 │ 6 days, 13:41:00 │    3     0    90   3.2 │
│     TOTAL │      93 │         0.12 │        -136.874 │       -13.69 │ 6 days, 13:41:00 │    3     0    90   3.2 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃       Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  force_exit │     3 │        42.82 │         248.354 │        24.84 │ 141 days, 10:27:00 │    3     0     0   100 │
│   stop_loss │    90 │        -1.31 │        -385.228 │       -38.52 │    2 days, 1:48:00 │    0     0    90     0 │
│       TOTAL │    93 │         0.12 │        -136.874 │       -13.69 │   6 days, 13:41:00 │    3     0    90   3.2 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                          
┏━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃       Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │  force_exit │      3 │        42.82 │         248.354 │        24.84 │ 141 days, 10:27:00 │    3     0     0   100 │
│           │   stop_loss │     90 │        -1.31 │        -385.228 │       -38.52 │    2 days, 1:48:00 │    0     0    90     0 │
│     TOTAL │             │     93 │         0.12 │        -136.874 │       -13.69 │   6 days, 13:41:00 │    3     0    90   3.2 │
└───────────┴─────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────────┴────────────────────────┘
                            SUMMARY METRICS                             
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                                ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2025-01-01 00:00:00                  │
│ Backtesting to                │ 2025-09-11 18:15:00                  │
│ Trading Mode                  │ Spot                                 │
│ Max open trades               │ 3                                    │
│                               │                                      │
│ Total/Daily Avg Trades        │ 93 / 0.37                            │
│ Starting balance              │ 1000 USDT                            │
│ Final balance                 │ 863.126 USDT                         │
│ Absolute profit               │ -136.874 USDT                        │
│ Total profit %                │ -13.69%                              │
│ CAGR %                        │ -19.13%                              │
│ Sortino                       │ -3.75                                │
│ Sharpe                        │ -0.55                                │
│ Calmar                        │ -2.68                                │
│ SQN                           │ -0.75                                │
│ Profit factor                 │ 0.64                                 │
│ Expectancy (Ratio)            │ -1.47 (-0.34)                        │
│ Avg. daily profit             │ -0.541 USDT                          │
│ Avg. stake amount             │ 352.937 USDT                         │
│ Total trade volume            │ 65640.482 USDT                       │
│                               │                                      │
│ Best Pair                     │ BNB/USDT 9.31%                       │
│ Worst Pair                    │ LTC/USDT -10.06%                     │
│ Best trade                    │ BNB/USDT 49.61%                      │
│ Worst trade                   │ BTC/USDT -10.18%                     │
│ Best day                      │ 248.354 USDT                         │
│ Worst day                     │ -35.258 USDT                         │
│ Days win/draw/lose            │ 1 / 198 / 55                         │
│ Min/Max/Avg. Duration Winners │ 128d 03:45 / 152d 09:50 / 141d 10:27 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 32d 12:15 / 2d 01:48      │
│ Max Consecutive Wins / Loss   │ 3 / 90                               │
│ Rejected Entry signals        │ 2181                                 │
│ Entry/Exit Timeouts           │ 0 / 0                                │
│                               │                                      │
│ Min balance                   │ 614.772 USDT                         │
│ Max balance                   │ 996.411 USDT                         │
│ Max % of account underwater   │ 38.52%                               │
│ Absolute Drawdown (Account)   │ 38.52%                               │
│ Absolute Drawdown             │ 385.228 USDT                         │
│ Drawdown high                 │ -3.589 USDT                          │
│ Drawdown low                  │ -385.228 USDT                        │
│ Drawdown Start                │ 2025-01-01 01:05:00                  │
│ Drawdown End                  │ 2025-05-05 20:30:00                  │
│ Market change                 │ 27.05%                               │
└───────────────────────────────┴──────────────────────────────────────┘

Backtested 2025-01-01 00:00:00 -> 2025-09-11 18:15:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ KeltnerChannelStrategy │     93 │         0.12 │        -136.874 │       -13.69 │ 6 days, 13:41:00 │    3     0    90   3.2 │ 385.228 USDT  38.52% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-08T22:10:23.709290",
  "strategy": "KeltnerChannelStrategy",
  "random_state": 6161,
  "total_daily_avg_trades": "93 / 0.37",
  "absolute_profit_usdt": -136.874,
  "total_profit_pct": -13.69,
  "cagr_pct": -19.13,
  "sortino": -3.75,
  "sharpe": -0.55,
  "calmar": -2.68,
  "sqn": -0.75,
  "max_consecutive_wins_loss": "3 / 90",
  "min_balance_usdt": 614.772,
  "max_balance_usdt": 996.411,
  "market_change_pct": 27.05
}
```
