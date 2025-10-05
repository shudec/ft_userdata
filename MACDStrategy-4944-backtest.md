# Freqtrade Backtest Log

**Strategy:** MACDStrategy  
**Random State:** 4944  
**Timestamp:** 2025-10-05 21:33:29

## Configuration
```json
{
  "strategy": "MACDStrategy",
  "timeframe": "1h",
  "pairs": [
    "ADA/USDT",
    "SOL/USDT",
    "DOGE/USDT",
    "TRX/USDT"
  ],
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 4944,
  "epochs": 100,
  "hyperopt_timerange": "20220101-20231231",
  "backtest_timerange": "20220101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy MACDStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs ADA/USDT SOL/USDT DOGE/USDT TRX/USDT --timerange 20220101-20251231 --export trades
```

## Backtesting Output
```
2025-10-05 19:32:04,904 - freqtrade - INFO - freqtrade 2025.7
2025-10-05 19:32:05,283 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-10-05 19:32:05,283 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-05 19:32:06,806 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-05 19:32:06,809 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-05 19:32:06,809 - freqtrade.loggers - INFO - Logfile configured
2025-10-05 19:32:06,810 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-05 19:32:06,810 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-10-05 19:32:06,811 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-05 19:32:06,811 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-05 19:32:06,811 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-10-05 19:32:06,821 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-05 19:32:06,822 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-05 19:32:06,822 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-05 19:32:06,823 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-05 19:32:06,823 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-05 19:32:06,823 - freqtrade.configuration.configuration - INFO - Using pairs ['ADA/USDT', 'SOL/USDT', 'DOGE/USDT', 'TRX/USDT']
2025-10-05 19:32:06,824 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-10-05 19:32:06,825 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-05 19:32:06,845 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-05 19:32:06,846 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-05 19:32:06,850 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-05 19:32:06,851 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-05 19:32:06,851 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-10-05 19:32:06,886 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-05 19:32:09,238 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-05 19:32:09,293 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy MACDStrategy from '/freqtrade/user_data/strategies/MACD_strategy.py'...
2025-10-05 19:32:09,293 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/MACD_strategy.json
2025-10-05 19:32:09,294 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-10-05 19:32:09,295 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-05 19:32:09,295 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-05 19:32:09,296 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-05 19:32:09,296 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-05 19:32:09,297 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-05 19:32:09,297 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-10-05 19:32:09,298 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-10-05 19:32:09,298 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-05 19:32:09,298 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-05 19:32:09,299 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-05 19:32:09,299 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-05 19:32:09,300 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-05 19:32:09,300 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'market', 'stoploss_on_exchange': False}
2025-10-05 19:32:09,300 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-05 19:32:09,301 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-05 19:32:09,301 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-05 19:32:09,302 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 200
2025-10-05 19:32:09,302 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-05 19:32:09,302 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-10-05 19:32:09,303 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-05 19:32:09,303 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-05 19:32:09,304 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-05 19:32:09,304 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-05 19:32:09,304 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-05 19:32:09,305 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-05 19:32:09,305 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-05 19:32:09,305 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-05 19:32:09,306 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-05 19:32:09,311 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-05 19:32:09,340 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-05 19:32:09,342 - freqtrade.data.history.history_utils - INFO - Using indicator startup period: 200 ...
2025-10-05 19:32:09,372 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-05 19:32:09,425 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-05 19:32:09,473 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-05 19:32:09,521 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-05 19:32:09,552 - freqtrade.optimize.backtesting - INFO - Loading data from 2021-12-23 16:00:00 up to 2025-10-02 17:00:00 (1379 days).
2025-10-05 19:32:09,628 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-05 19:32:09,836 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-05 19:32:10,057 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-05 19:32:10,302 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-05 19:32:11,428 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-05 19:32:11,430 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-05 19:32:11,431 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy MACDStrategy
2025-10-05 19:32:11,432 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 5
2025-10-05 19:32:11,432 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-10-05 19:32:11,433 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-10-05 19:32:11,433 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1
2025-10-05 19:32:11,433 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1.5
2025-10-05 19:32:11,434 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 4.5
2025-10-05 19:32:11,434 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-10-05 19:32:11,435 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-10-05 19:32:11,435 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-10-05 19:32:11,435 - freqtrade.strategy.hyper - INFO - Strategy Parameter: trailing_custom_stop = True
2025-10-05 19:32:11,436 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-10-05 19:32:11,436 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-10-05 19:32:11,437 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower and atr
2025-10-05 19:32:11,437 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-10-05 19:32:11,437 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-05 19:32:11,440 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-05 19:32:11,450 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-05 19:32:11,470 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-05 19:32:11,487 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-05 19:32:11,522 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-05 19:32:11,532 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-05 19:32:11,552 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-05 19:32:11,570 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-05 19:32:11,604 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-05 19:32:11,615 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-05 19:32:11,635 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-05 19:32:11,654 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-05 19:32:11,690 - freqtrade.data.dataprovider - INFO - Loading data for TRX/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-05 19:32:11,702 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-05 19:32:11,721 - freqtrade.data.dataprovider - INFO - Loading data for TRX/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-05 19:32:11,740 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-05 19:32:11,788 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-10-02 17:00:00 (1370 days).
2025-10-05 19:33:28,676 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-05_19-33-28.meta.json"
Result for strategy MACDStrategy
                                              BACKTESTING REPORT                                              
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  SOL/USDT │    202 │         0.17 │          48.015 │          4.8 │     12:47:00 │   67     0   135  33.2 │
│  ADA/USDT │    192 │         0.14 │          40.662 │         4.07 │     11:26:00 │   58     0   134  30.2 │
│ DOGE/USDT │    207 │        -0.28 │        -110.640 │       -11.06 │     11:23:00 │   56     0   151  27.1 │
│  TRX/USDT │    252 │         -0.3 │        -139.397 │       -13.94 │     12:46:00 │   68     0   184  27.0 │
│     TOTAL │    853 │        -0.09 │        -161.360 │       -16.14 │     12:08:00 │  249     0   604  29.2 │
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
│     OTHER │     853 │        -0.09 │        -161.360 │       -16.14 │     12:08:00 │  249     0   604  29.2 │
│     TOTAL │     853 │        -0.09 │        -161.360 │       -16.14 │     12:08:00 │  249     0   604  29.2 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │     8 │        21.66 │         304.977 │         30.5 │ 1 day, 0:36:00 │    8     0     0   100 │
│      stop_loss │     2 │       -10.17 │         -37.836 │        -3.78 │        6:02:00 │    0     0     2     0 │
│    exit_signal │   843 │        -0.27 │        -428.501 │       -42.85 │       12:02:00 │  241     0   602  28.6 │
│          TOTAL │   853 │        -0.09 │        -161.360 │       -16.14 │       12:08:00 │  249     0   604  29.2 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │      8 │        21.66 │         304.977 │         30.5 │ 1 day, 0:36:00 │    8     0     0   100 │
│           │      stop_loss │      2 │       -10.17 │         -37.836 │        -3.78 │        6:02:00 │    0     0     2     0 │
│           │    exit_signal │    843 │        -0.27 │        -428.501 │       -42.85 │       12:02:00 │  241     0   602  28.6 │
│     TOTAL │                │    853 │        -0.09 │        -161.360 │       -16.14 │       12:08:00 │  249     0   604  29.2 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2025-10-02 17:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 853 / 0.62                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 838.64 USDT                    │
│ Absolute profit               │ -161.36 USDT                   │
│ Total profit %                │ -16.14%                        │
│ CAGR %                        │ -4.58%                         │
│ Sortino                       │ -0.91                          │
│ Sharpe                        │ -0.36                          │
│ Calmar                        │ -1.23                          │
│ SQN                           │ -0.88                          │
│ Profit factor                 │ 0.91                           │
│ Expectancy (Ratio)            │ -0.19 (-0.06)                  │
│ Avg. daily profit             │ -0.118 USDT                    │
│ Avg. stake amount             │ 180.452 USDT                   │
│ Total trade volume            │ 308306.481 USDT                │
│                               │                                │
│ Best Pair                     │ SOL/USDT 4.80%                 │
│ Worst Pair                    │ TRX/USDT -13.94%               │
│ Best trade                    │ SOL/USDT 23.25%                │
│ Worst trade                   │ SOL/USDT -10.18%               │
│ Best day                      │ 40.063 USDT                    │
│ Worst day                     │ -39.468 USDT                   │
│ Days win/draw/lose            │ 166 / 842 / 336                │
│ Min/Max/Avg. Duration Winners │ 0d 08:25 / 2d 14:00 / 0d 23:06 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:55 / 1d 13:00 / 0d 07:37 │
│ Max Consecutive Wins / Loss   │ 8 / 13                         │
│ Rejected Entry signals        │ 264                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 823.409 USDT                   │
│ Max balance                   │ 1006.926 USDT                  │
│ Max % of account underwater   │ 18.23%                         │
│ Absolute Drawdown (Account)   │ 18.23%                         │
│ Absolute Drawdown             │ 183.517 USDT                   │
│ Drawdown high                 │ 6.926 USDT                     │
│ Drawdown low                  │ -176.591 USDT                  │
│ Drawdown Start                │ 2022-04-26 11:00:00            │
│ Drawdown End                  │ 2025-01-20 18:00:00            │
│ Market change                 │ 99.71%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-10-02 17:00:00 | Max open trades : 3
                                                            STRATEGY SUMMARY                                                            
┏━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃     Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ MACDStrategy │    853 │        -0.09 │        -161.360 │       -16.14 │     12:08:00 │  249     0   604  29.2 │ 183.517 USDT  18.23% │
└──────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-05T21:33:29.933655",
  "strategy": "MACDStrategy",
  "random_state": 4944,
  "total_daily_avg_trades": "853 / 0.62",
  "absolute_profit_usdt": -161.36,
  "total_profit_pct": -16.14,
  "cagr_pct": -4.58,
  "sortino": -0.91,
  "sharpe": -0.36,
  "calmar": -1.23,
  "sqn": -0.88,
  "max_consecutive_wins_loss": "8 / 13",
  "min_balance_usdt": 823.409,
  "max_balance_usdt": 1006.926,
  "market_change_pct": 99.71,
  "win_draw_loss_winpct": "249 0 604 29.2"
}
```
