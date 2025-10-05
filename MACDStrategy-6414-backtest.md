# Freqtrade Backtest Log

**Strategy:** MACDStrategy  
**Random State:** 6414  
**Timestamp:** 2025-10-05 22:14:35

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
  "random_state": 6414,
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
2025-10-05 20:08:29,194 - freqtrade - INFO - freqtrade 2025.7
2025-10-05 20:08:29,528 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-10-05 20:08:29,528 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-05 20:08:31,001 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-05 20:08:31,004 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-05 20:08:31,004 - freqtrade.loggers - INFO - Logfile configured
2025-10-05 20:08:31,004 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-05 20:08:31,005 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-10-05 20:08:31,005 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-05 20:08:31,006 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-05 20:08:31,006 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-10-05 20:08:31,014 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-05 20:08:31,015 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-05 20:08:31,016 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-05 20:08:31,016 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-05 20:08:31,016 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-05 20:08:31,017 - freqtrade.configuration.configuration - INFO - Using pairs ['ADA/USDT', 'SOL/USDT', 'DOGE/USDT', 'TRX/USDT']
2025-10-05 20:08:31,017 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-10-05 20:08:31,019 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-05 20:08:31,039 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-05 20:08:31,040 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-05 20:08:31,043 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-05 20:08:31,044 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-05 20:08:31,045 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-10-05 20:08:31,079 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-05 20:08:33,750 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-05 20:08:33,808 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy MACDStrategy from '/freqtrade/user_data/strategies/MACD_strategy.py'...
2025-10-05 20:08:33,809 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/MACD_strategy.json
2025-10-05 20:08:33,810 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-10-05 20:08:33,810 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-05 20:08:33,811 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-05 20:08:33,811 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-05 20:08:33,812 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-05 20:08:33,812 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-05 20:08:33,812 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-10-05 20:08:33,813 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-10-05 20:08:33,813 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-05 20:08:33,813 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-05 20:08:33,814 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-05 20:08:33,814 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-05 20:08:33,814 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-05 20:08:33,815 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'market', 'stoploss_on_exchange': False}
2025-10-05 20:08:33,815 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-05 20:08:33,816 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-05 20:08:33,816 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-05 20:08:33,816 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 200
2025-10-05 20:08:33,817 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-05 20:08:33,817 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-10-05 20:08:33,817 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-05 20:08:33,818 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-05 20:08:33,818 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-05 20:08:33,819 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-05 20:08:33,819 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-05 20:08:33,819 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-05 20:08:33,820 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-05 20:08:33,820 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-05 20:08:33,821 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-05 20:08:33,827 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-05 20:08:33,856 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-05 20:08:33,858 - freqtrade.data.history.history_utils - INFO - Using indicator startup period: 200 ...
2025-10-05 20:08:33,889 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-05 20:08:33,940 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-05 20:08:33,986 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-05 20:08:34,042 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-05 20:08:34,079 - freqtrade.optimize.backtesting - INFO - Loading data from 2021-12-23 16:00:00 up to 2025-10-02 17:00:00 (1379 days).
2025-10-05 20:08:34,153 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-05 20:08:34,419 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-05 20:08:34,726 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-05 20:08:35,013 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-05 20:08:36,387 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-05 20:08:36,388 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-05 20:08:36,388 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy MACDStrategy
2025-10-05 20:08:36,389 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 5
2025-10-05 20:08:36,389 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-10-05 20:08:36,390 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-10-05 20:08:36,390 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1
2025-10-05 20:08:36,391 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1.5
2025-10-05 20:08:36,391 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 4.5
2025-10-05 20:08:36,391 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-10-05 20:08:36,392 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-10-05 20:08:36,392 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-10-05 20:08:36,392 - freqtrade.strategy.hyper - INFO - Strategy Parameter: trailing_custom_stop = True
2025-10-05 20:08:36,393 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-10-05 20:08:36,393 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-10-05 20:08:36,393 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-10-05 20:08:36,394 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-10-05 20:08:36,394 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-05 20:08:36,396 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-05 20:08:36,406 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-05 20:08:36,430 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-05 20:08:36,449 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-05 20:08:36,484 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-05 20:08:36,494 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-05 20:08:36,517 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-05 20:08:36,535 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-05 20:08:36,577 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-05 20:08:36,591 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-05 20:08:36,619 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-05 20:08:36,640 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-05 20:08:36,684 - freqtrade.data.dataprovider - INFO - Loading data for TRX/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-05 20:08:36,696 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-05 20:08:36,721 - freqtrade.data.dataprovider - INFO - Loading data for TRX/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-05 20:08:36,749 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-05 20:08:36,820 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-10-02 17:00:00 (1370 days).
2025-10-05 20:14:33,839 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-05_20-14-33.meta.json"
Result for strategy MACDStrategy
                                                BACKTESTING REPORT                                                
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  SOL/USDT │    115 │         0.78 │           5.091 │         0.51 │ 3 days, 10:58:00 │   41     0    74  35.7 │
│  ADA/USDT │    121 │        -0.57 │        -101.842 │       -10.18 │ 2 days, 17:47:00 │   37     0    84  30.6 │
│  TRX/USDT │    123 │        -0.38 │        -173.716 │       -17.37 │ 3 days, 19:10:00 │   36     0    87  29.3 │
│ DOGE/USDT │    110 │        -1.08 │        -213.014 │        -21.3 │  3 days, 1:49:00 │   28     0    82  25.5 │
│     TOTAL │    469 │        -0.31 │        -483.482 │       -48.35 │  3 days, 6:32:00 │  142     0   327  30.3 │
└───────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                            LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ADA/USDT │      1 │         6.99 │          15.226 │         1.52 │ 1 day, 21:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         6.99 │          15.226 │         1.52 │ 1 day, 21:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                 ENTER TAG STATS                                                  
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │     469 │        -0.31 │        -483.482 │       -48.35 │ 3 days, 6:32:00 │  142     0   327  30.3 │
│     TOTAL │     469 │        -0.31 │        -483.482 │       -48.35 │ 3 days, 6:32:00 │  142     0   327  30.3 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │   141 │         9.65 │        2783.524 │       278.35 │ 4 days, 17:16:00 │  141     0     0   100 │
│     force_exit │     1 │         6.99 │          15.226 │         1.52 │  1 day, 21:00:00 │    1     0     0   100 │
│      stop_loss │   327 │        -4.63 │       -3282.233 │      -328.22 │ 2 days, 15:40:00 │    0     0   327     0 │
│          TOTAL │   469 │        -0.31 │        -483.482 │       -48.35 │  3 days, 6:32:00 │  142     0   327  30.3 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                          MIXED TAG STATS                                                          
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │    141 │         9.65 │        2783.524 │       278.35 │ 4 days, 17:16:00 │  141     0     0   100 │
│           │     force_exit │      1 │         6.99 │          15.226 │         1.52 │  1 day, 21:00:00 │    1     0     0   100 │
│           │      stop_loss │    327 │        -4.63 │       -3282.233 │      -328.22 │ 2 days, 15:40:00 │    0     0   327     0 │
│     TOTAL │                │    469 │        -0.31 │        -483.482 │       -48.35 │  3 days, 6:32:00 │  142     0   327  30.3 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00             │
│ Backtesting to                │ 2025-10-02 17:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 469 / 0.34                      │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 516.518 USDT                    │
│ Absolute profit               │ -483.482 USDT                   │
│ Total profit %                │ -48.35%                         │
│ CAGR %                        │ -16.14%                         │
│ Sortino                       │ -1.34                           │
│ Sharpe                        │ -0.44                           │
│ Calmar                        │ -1.11                           │
│ SQN                           │ -1.46                           │
│ Profit factor                 │ 0.85                            │
│ Expectancy (Ratio)            │ -1.03 (-0.10)                   │
│ Avg. daily profit             │ -0.353 USDT                     │
│ Avg. stake amount             │ 241.449 USDT                    │
│ Total trade volume            │ 226447.98 USDT                  │
│                               │                                 │
│ Best Pair                     │ SOL/USDT 0.51%                  │
│ Worst Pair                    │ DOGE/USDT -21.30%               │
│ Best trade                    │ SOL/USDT 41.21%                 │
│ Worst trade                   │ DOGE/USDT -15.21%               │
│ Best day                      │ 74.591 USDT                     │
│ Worst day                     │ -53.504 USDT                    │
│ Days win/draw/lose            │ 121 / 1009 / 225                │
│ Min/Max/Avg. Duration Winners │ 0d 02:35 / 82d 06:35 / 4d 16:47 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:05 / 33d 07:35 / 2d 15:40 │
│ Max Consecutive Wins / Loss   │ 7 / 21                          │
│ Rejected Entry signals        │ 839                             │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 416.242 USDT                    │
│ Max balance                   │ 1065.101 USDT                   │
│ Max % of account underwater   │ 60.92%                          │
│ Absolute Drawdown (Account)   │ 60.92%                          │
│ Absolute Drawdown             │ 648.858 USDT                    │
│ Drawdown high                 │ 65.101 USDT                     │
│ Drawdown low                  │ -583.758 USDT                   │
│ Drawdown Start                │ 2022-04-05 13:20:00             │
│ Drawdown End                  │ 2025-07-01 14:25:00             │
│ Market change                 │ 99.71%                          │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-10-02 17:00:00 | Max open trades : 3
                                                             STRATEGY SUMMARY                                                              
┏━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃     Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ MACDStrategy │    469 │        -0.31 │        -483.482 │       -48.35 │ 3 days, 6:32:00 │  142     0   327  30.3 │ 648.858 USDT  60.92% │
└──────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-05T22:14:35.027996",
  "strategy": "MACDStrategy",
  "random_state": 6414,
  "total_daily_avg_trades": "469 / 0.34",
  "absolute_profit_usdt": -483.482,
  "total_profit_pct": -48.35,
  "cagr_pct": -16.14,
  "sortino": -1.34,
  "sharpe": -0.44,
  "calmar": -1.11,
  "sqn": -1.46,
  "max_consecutive_wins_loss": "7 / 21",
  "min_balance_usdt": 416.242,
  "max_balance_usdt": 1065.101,
  "market_change_pct": 99.71
}
```
