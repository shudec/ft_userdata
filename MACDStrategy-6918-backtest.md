# Freqtrade Backtest Log

**Strategy:** MACDStrategy  
**Random State:** 6918  
**Timestamp:** 2025-10-05 22:01:42

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
  "random_state": 6918,
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
2025-10-05 20:00:22,544 - freqtrade - INFO - freqtrade 2025.7
2025-10-05 20:00:22,881 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-10-05 20:00:22,882 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-05 20:00:24,473 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-05 20:00:24,477 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-05 20:00:24,477 - freqtrade.loggers - INFO - Logfile configured
2025-10-05 20:00:24,478 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-05 20:00:24,478 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-10-05 20:00:24,479 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-05 20:00:24,479 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-05 20:00:24,479 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-10-05 20:00:24,490 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-05 20:00:24,491 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-05 20:00:24,491 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-05 20:00:24,492 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-05 20:00:24,492 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-05 20:00:24,492 - freqtrade.configuration.configuration - INFO - Using pairs ['ADA/USDT', 'SOL/USDT', 'DOGE/USDT', 'TRX/USDT']
2025-10-05 20:00:24,493 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-10-05 20:00:24,494 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-05 20:00:24,514 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-05 20:00:24,515 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-05 20:00:24,519 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-05 20:00:24,520 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-05 20:00:24,521 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-10-05 20:00:24,557 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-05 20:00:27,099 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-05 20:00:27,152 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy MACDStrategy from '/freqtrade/user_data/strategies/MACD_strategy.py'...
2025-10-05 20:00:27,152 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/MACD_strategy.json
2025-10-05 20:00:27,153 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-10-05 20:00:27,154 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-05 20:00:27,155 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-05 20:00:27,155 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-05 20:00:27,156 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-05 20:00:27,156 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-05 20:00:27,157 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-10-05 20:00:27,157 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-10-05 20:00:27,157 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-05 20:00:27,158 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-05 20:00:27,158 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-05 20:00:27,159 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-05 20:00:27,159 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-05 20:00:27,160 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'market', 'stoploss_on_exchange': False}
2025-10-05 20:00:27,160 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-05 20:00:27,161 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-05 20:00:27,161 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-05 20:00:27,162 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 200
2025-10-05 20:00:27,162 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-05 20:00:27,163 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-10-05 20:00:27,163 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-05 20:00:27,163 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-05 20:00:27,164 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-05 20:00:27,164 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-05 20:00:27,165 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-05 20:00:27,165 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-05 20:00:27,166 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-05 20:00:27,166 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-05 20:00:27,167 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-05 20:00:27,172 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-05 20:00:27,202 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-05 20:00:27,204 - freqtrade.data.history.history_utils - INFO - Using indicator startup period: 200 ...
2025-10-05 20:00:27,235 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-05 20:00:27,289 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-05 20:00:27,336 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-05 20:00:27,410 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-05 20:00:27,453 - freqtrade.optimize.backtesting - INFO - Loading data from 2021-12-23 16:00:00 up to 2025-10-02 17:00:00 (1379 days).
2025-10-05 20:00:27,536 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-05 20:00:27,826 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-05 20:00:28,109 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-05 20:00:28,398 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-05 20:00:29,766 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-05 20:00:29,767 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-05 20:00:29,768 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy MACDStrategy
2025-10-05 20:00:29,768 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 5
2025-10-05 20:00:29,769 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-10-05 20:00:29,769 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-10-05 20:00:29,769 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1
2025-10-05 20:00:29,770 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1.5
2025-10-05 20:00:29,770 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 4.5
2025-10-05 20:00:29,771 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-10-05 20:00:29,771 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-10-05 20:00:29,771 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-10-05 20:00:29,771 - freqtrade.strategy.hyper - INFO - Strategy Parameter: trailing_custom_stop = True
2025-10-05 20:00:29,772 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-10-05 20:00:29,772 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-10-05 20:00:29,772 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower and atr
2025-10-05 20:00:29,773 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-10-05 20:00:29,773 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-05 20:00:29,775 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-05 20:00:29,784 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-05 20:00:29,802 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-05 20:00:29,818 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-05 20:00:29,853 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-05 20:00:29,862 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-05 20:00:29,881 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-05 20:00:29,899 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-05 20:00:29,934 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-05 20:00:29,944 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-05 20:00:29,963 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-05 20:00:29,981 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-05 20:00:30,015 - freqtrade.data.dataprovider - INFO - Loading data for TRX/USDT 1d from 2021-06-15 00:00:00 to 2025-12-31 00:00:00
2025-10-05 20:00:30,024 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-05 20:00:30,043 - freqtrade.data.dataprovider - INFO - Loading data for TRX/USDT 4h from 2021-11-28 16:00:00 to 2025-12-31 00:00:00
2025-10-05 20:00:30,061 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-05 20:00:30,109 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-10-02 17:00:00 (1370 days).
2025-10-05 20:01:41,248 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-05_20-01-41.meta.json"
Result for strategy MACDStrategy
                                              BACKTESTING REPORT                                              
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  TRX/USDT │    241 │         0.01 │           5.339 │         0.53 │     15:47:00 │  239     0     2  99.2 │
│  ADA/USDT │    203 │        -0.16 │         -58.681 │        -5.87 │      7:51:00 │  196     0     7  96.6 │
│ DOGE/USDT │    232 │        -0.26 │        -104.148 │       -10.41 │      5:48:00 │  221     0    11  95.3 │
│  SOL/USDT │    211 │        -0.29 │        -107.308 │       -10.73 │      5:39:00 │  201     0    10  95.3 │
│     TOTAL │    887 │        -0.17 │        -264.797 │       -26.48 │      8:57:00 │  857     0    30  96.6 │
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
│     OTHER │     887 │        -0.17 │        -264.797 │       -26.48 │      8:57:00 │  857     0    30  96.6 │
│     TOTAL │     887 │        -0.17 │        -264.797 │       -26.48 │      8:57:00 │  857     0    30  96.6 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │   857 │         0.18 │         248.467 │        24.85 │         7:25:00 │  857     0     0   100 │
│      stop_loss │    30 │       -10.17 │        -513.264 │       -51.33 │ 2 days, 4:53:00 │    0     0    30     0 │
│          TOTAL │   887 │        -0.17 │        -264.797 │       -26.48 │         8:57:00 │  857     0    30  96.6 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                          
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │    857 │         0.18 │         248.467 │        24.85 │         7:25:00 │  857     0     0   100 │
│           │      stop_loss │     30 │       -10.17 │        -513.264 │       -51.33 │ 2 days, 4:53:00 │    0     0    30     0 │
│     TOTAL │                │    887 │        -0.17 │        -264.797 │       -26.48 │         8:57:00 │  857     0    30  96.6 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00             │
│ Backtesting to                │ 2025-10-02 17:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 887 / 0.65                      │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 735.203 USDT                    │
│ Absolute profit               │ -264.797 USDT                   │
│ Total profit %                │ -26.48%                         │
│ CAGR %                        │ -7.87%                          │
│ Sortino                       │ -2.48                           │
│ Sharpe                        │ -1.14                           │
│ Calmar                        │ -1.33                           │
│ SQN                           │ -2.75                           │
│ Profit factor                 │ 0.48                            │
│ Expectancy (Ratio)            │ -0.30 (-0.02)                   │
│ Avg. daily profit             │ -0.193 USDT                     │
│ Avg. stake amount             │ 160.938 USDT                    │
│ Total trade volume            │ 285811.033 USDT                 │
│                               │                                 │
│ Best Pair                     │ TRX/USDT 0.53%                  │
│ Worst Pair                    │ SOL/USDT -10.73%                │
│ Best trade                    │ ADA/USDT 8.85%                  │
│ Worst trade                   │ DOGE/USDT -10.18%               │
│ Best day                      │ 13.32 USDT                      │
│ Worst day                     │ -46.647 USDT                    │
│ Days win/draw/lose            │ 478 / 851 / 27                  │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 12d 12:35 / 0d 07:25 │
│ Min/Max/Avg. Duration Losers  │ 0d 04:30 / 6d 04:00 / 2d 04:53  │
│ Max Consecutive Wins / Loss   │ 104 / 3                         │
│ Rejected Entry signals        │ 19                              │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 724.391 USDT                    │
│ Max balance                   │ 1001.973 USDT                   │
│ Max % of account underwater   │ 27.70%                          │
│ Absolute Drawdown (Account)   │ 27.70%                          │
│ Absolute Drawdown             │ 277.581 USDT                    │
│ Drawdown high                 │ 1.973 USDT                      │
│ Drawdown low                  │ -275.609 USDT                   │
│ Drawdown Start                │ 2022-01-19 01:05:00             │
│ Drawdown End                  │ 2025-06-13 02:40:00             │
│ Market change                 │ 99.71%                          │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-10-02 17:00:00 | Max open trades : 3
                                                            STRATEGY SUMMARY                                                            
┏━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃     Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ MACDStrategy │    887 │        -0.17 │        -264.797 │       -26.48 │      8:57:00 │  857     0    30  96.6 │ 277.581 USDT  27.70% │
└──────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-05T22:01:42.488726",
  "strategy": "MACDStrategy",
  "random_state": 6918,
  "total_daily_avg_trades": "887 / 0.65",
  "absolute_profit_usdt": -264.797,
  "total_profit_pct": -26.48,
  "cagr_pct": -7.87,
  "sortino": -2.48,
  "sharpe": -1.14,
  "calmar": -1.33,
  "sqn": -2.75,
  "max_consecutive_wins_loss": "104 / 3",
  "min_balance_usdt": 724.391,
  "max_balance_usdt": 1001.973,
  "market_change_pct": 99.71,
  "win_draw_loss_winpct": "857 0 30 96.6"
}
```
