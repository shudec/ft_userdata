# Freqtrade Backtest Log

**Strategy:** MACDStrategy  
**Random State:** 6234  
**Timestamp:** 2025-10-05 21:54:18

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
  "random_state": 6234,
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
2025-10-05 19:53:52,760 - freqtrade - INFO - freqtrade 2025.7
2025-10-05 19:53:53,179 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-10-05 19:53:53,180 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-05 19:53:54,775 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-05 19:53:54,777 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-05 19:53:54,778 - freqtrade.loggers - INFO - Logfile configured
2025-10-05 19:53:54,778 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-05 19:53:54,779 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-10-05 19:53:54,779 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-05 19:53:54,779 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-05 19:53:54,780 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-10-05 19:53:54,787 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-05 19:53:54,789 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-05 19:53:54,789 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-05 19:53:54,790 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-05 19:53:54,791 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-05 19:53:54,791 - freqtrade.configuration.configuration - INFO - Using pairs ['ADA/USDT', 'SOL/USDT', 'DOGE/USDT', 'TRX/USDT']
2025-10-05 19:53:54,792 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-10-05 19:53:54,794 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-05 19:53:54,814 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-05 19:53:54,815 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-05 19:53:54,818 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-05 19:53:54,819 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-05 19:53:54,819 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-10-05 19:53:54,852 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-05 19:53:57,396 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-05 19:53:57,451 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy MACDStrategy from '/freqtrade/user_data/strategies/MACD_strategy.py'...
2025-10-05 19:53:57,452 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/MACD_strategy.json
2025-10-05 19:53:57,453 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-10-05 19:53:57,454 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-05 19:53:57,454 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-05 19:53:57,455 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-05 19:53:57,456 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-05 19:53:57,456 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-05 19:53:57,457 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-10-05 19:53:57,457 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-10-05 19:53:57,458 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-05 19:53:57,459 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-05 19:53:57,460 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-05 19:53:57,460 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-05 19:53:57,461 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-05 19:53:57,462 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'market', 'stoploss_on_exchange': False}
2025-10-05 19:53:57,462 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-05 19:53:57,463 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-05 19:53:57,463 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-05 19:53:57,464 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 200
2025-10-05 19:53:57,464 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-05 19:53:57,465 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-10-05 19:53:57,465 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-05 19:53:57,465 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-05 19:53:57,466 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-05 19:53:57,466 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-05 19:53:57,467 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-05 19:53:57,467 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-05 19:53:57,468 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-05 19:53:57,468 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-05 19:53:57,468 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-05 19:53:57,474 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-05 19:53:57,505 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-05 19:53:57,506 - freqtrade.data.history.history_utils - INFO - Using indicator startup period: 200 ...
2025-10-05 19:53:57,538 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-05 19:53:57,587 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-05 19:53:57,631 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-05 19:53:57,675 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-05 19:53:57,704 - freqtrade.optimize.backtesting - INFO - Loading data from 2021-12-23 16:00:00 up to 2025-10-02 17:00:00 (1379 days).
2025-10-05 19:53:57,772 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-05 19:53:57,997 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-05 19:53:58,246 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-05 19:53:58,468 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-05 19:53:59,606 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-05 19:53:59,607 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-05 19:53:59,607 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy MACDStrategy
2025-10-05 19:53:59,608 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 5
2025-10-05 19:53:59,608 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-10-05 19:53:59,609 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-10-05 19:53:59,609 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1
2025-10-05 19:53:59,609 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1.5
2025-10-05 19:53:59,610 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 4.5
2025-10-05 19:53:59,610 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-10-05 19:53:59,610 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-10-05 19:53:59,611 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-10-05 19:53:59,611 - freqtrade.strategy.hyper - INFO - Strategy Parameter: trailing_custom_stop = True
2025-10-05 19:53:59,611 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-10-05 19:53:59,612 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-10-05 19:53:59,612 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower and atr
2025-10-05 19:53:59,612 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-10-05 19:53:59,612 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-05 19:53:59,614 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-05 19:53:59,622 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-05 19:53:59,641 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-05 19:53:59,658 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-05 19:53:59,692 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-05 19:53:59,701 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-05 19:53:59,719 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-05 19:53:59,737 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-05 19:53:59,772 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-05 19:53:59,782 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-05 19:53:59,800 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-05 19:53:59,818 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-05 19:53:59,852 - freqtrade.data.dataprovider - INFO - Loading data for TRX/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-05 19:53:59,862 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-05 19:53:59,880 - freqtrade.data.dataprovider - INFO - Loading data for TRX/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-05 19:53:59,898 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-05 19:53:59,950 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-10-02 17:00:00 (1370 days).
2025-10-05 19:54:17,722 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-05_19-54-17.meta.json"
Result for strategy MACDStrategy
                                              BACKTESTING REPORT                                              
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ DOGE/USDT │    213 │         -0.1 │         -40.877 │        -4.09 │      1:02:00 │  172     0    41  80.8 │
│  SOL/USDT │    206 │        -0.12 │         -42.415 │        -4.24 │      1:17:00 │  179     0    27  86.9 │
│  ADA/USDT │    195 │        -0.12 │         -44.832 │        -4.48 │      1:22:00 │  159     0    36  81.5 │
│  TRX/USDT │    261 │        -0.18 │         -82.298 │        -8.23 │      2:26:00 │  194     0    67  74.3 │
│     TOTAL │    875 │        -0.14 │        -210.423 │       -21.04 │      1:35:00 │  704     0   171  80.5 │
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
│     OTHER │     875 │        -0.14 │        -210.423 │       -21.04 │      1:35:00 │  704     0   171  80.5 │
│     TOTAL │     875 │        -0.14 │        -210.423 │       -21.04 │      1:35:00 │  704     0   171  80.5 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │   704 │         0.19 │         227.130 │        22.71 │      1:09:00 │  704     0     0   100 │
│    exit_signal │   171 │        -1.46 │        -437.553 │       -43.76 │      3:23:00 │    0     0   171     0 │
│          TOTAL │   875 │        -0.14 │        -210.423 │       -21.04 │      1:35:00 │  704     0   171  80.5 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │    704 │         0.19 │         227.130 │        22.71 │      1:09:00 │  704     0     0   100 │
│           │    exit_signal │    171 │        -1.46 │        -437.553 │       -43.76 │      3:23:00 │    0     0   171     0 │
│     TOTAL │                │    875 │        -0.14 │        -210.423 │       -21.04 │      1:35:00 │  704     0   171  80.5 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2025-10-02 17:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 875 / 0.64                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 789.577 USDT                   │
│ Absolute profit               │ -210.423 USDT                  │
│ Total profit %                │ -21.04%                        │
│ CAGR %                        │ -6.10%                         │
│ Sortino                       │ -1.70                          │
│ Sharpe                        │ -1.88                          │
│ Calmar                        │ -1.36                          │
│ SQN                           │ -4.56                          │
│ Profit factor                 │ 0.52                           │
│ Expectancy (Ratio)            │ -0.24 (-0.09)                  │
│ Avg. daily profit             │ -0.154 USDT                    │
│ Avg. stake amount             │ 173.432 USDT                   │
│ Total trade volume            │ 303903.449 USDT                │
│                               │                                │
│ Best Pair                     │ DOGE/USDT -4.09%               │
│ Worst Pair                    │ TRX/USDT -8.23%                │
│ Best trade                    │ ADA/USDT 8.85%                 │
│ Worst trade                   │ SOL/USDT -5.73%                │
│ Best day                      │ 14.177 USDT                    │
│ Worst day                     │ -15.167 USDT                   │
│ Days win/draw/lose            │ 333 / 880 / 130                │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 0d 17:35 / 0d 01:09 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 1d 00:00 / 0d 03:23 │
│ Max Consecutive Wins / Loss   │ 24 / 3                         │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 784.629 USDT                   │
│ Max balance                   │ 1000.76 USDT                   │
│ Max % of account underwater   │ 21.60%                         │
│ Absolute Drawdown (Account)   │ 21.60%                         │
│ Absolute Drawdown             │ 216.131 USDT                   │
│ Drawdown high                 │ 0.76 USDT                      │
│ Drawdown low                  │ -215.371 USDT                  │
│ Drawdown Start                │ 2022-01-14 20:45:00            │
│ Drawdown End                  │ 2025-08-15 14:00:00            │
│ Market change                 │ 99.71%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-10-02 17:00:00 | Max open trades : 3
                                                            STRATEGY SUMMARY                                                            
┏━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃     Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ MACDStrategy │    875 │        -0.14 │        -210.423 │       -21.04 │      1:35:00 │  704     0   171  80.5 │ 216.131 USDT  21.60% │
└──────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-05T21:54:18.921602",
  "strategy": "MACDStrategy",
  "random_state": 6234,
  "total_daily_avg_trades": "875 / 0.64",
  "absolute_profit_usdt": -210.423,
  "total_profit_pct": -21.04,
  "cagr_pct": -6.1,
  "sortino": -1.7,
  "sharpe": -1.88,
  "calmar": -1.36,
  "sqn": -4.56,
  "max_consecutive_wins_loss": "24 / 3",
  "min_balance_usdt": 784.629,
  "max_balance_usdt": 1000.76,
  "market_change_pct": 99.71,
  "win_draw_loss_winpct": "704 0 171 80.5"
}
```
