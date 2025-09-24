# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 663  
**Timestamp:** 2025-09-24 08:58:45

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 663,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20200101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20200101-20251231
```

## Backtesting Output
```
2025-09-24 06:54:19,215 - freqtrade - INFO - freqtrade 2025.8
2025-09-24 06:54:19,594 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-24 06:54:21,264 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-24 06:54:21,272 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-24 06:54:21,273 - freqtrade.loggers - INFO - Logfile configured
2025-09-24 06:54:21,273 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-24 06:54:21,274 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-24 06:54:21,275 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-24 06:54:21,276 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-24 06:54:21,276 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20200101-20251231 ...
2025-09-24 06:54:21,650 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-24 06:54:21,653 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-24 06:54:21,653 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-24 06:54:21,653 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-24 06:54:21,654 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-24 06:54:21,654 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20200101-20251231
2025-09-24 06:54:21,655 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-24 06:54:21,667 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-24 06:54:21,667 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 06:54:21,670 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-24 06:54:21,671 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-24 06:54:21,671 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-24 06:54:21,692 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-24 06:54:26,029 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-24 06:54:26,131 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-24 06:54:26,133 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-24 06:54:26,138 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-24 06:54:26,139 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-24 06:54:26,139 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-24 06:54:26,140 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-24 06:54:26,140 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-24 06:54:26,141 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-24 06:54:26,141 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-24 06:54:26,141 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-24 06:54:26,142 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-24 06:54:26,142 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-24 06:54:26,143 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-24 06:54:26,143 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-24 06:54:26,143 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-24 06:54:26,144 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-24 06:54:26,144 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-24 06:54:26,144 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-24 06:54:26,145 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-24 06:54:26,146 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-24 06:54:26,146 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-24 06:54:26,146 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-24 06:54:26,147 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-24 06:54:26,148 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-24 06:54:26,148 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-24 06:54:26,148 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-24 06:54:26,149 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-24 06:54:26,149 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-24 06:54:26,150 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-24 06:54:26,150 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-24 06:54:26,151 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 06:54:26,169 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-24 06:54:26,194 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-24 06:54:26,254 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 06:54:26,327 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 06:54:26,405 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 06:54:26,476 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 06:54:26,545 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 06:54:26,586 - freqtrade.optimize.backtesting - INFO - Loading data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 06:54:27,021 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 06:54:27,576 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 06:54:28,088 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 06:54:28,588 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 06:54:29,168 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 06:54:31,086 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-24 06:54:31,091 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-24 06:54:31,091 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-24 06:54:31,092 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-24 06:54:31,092 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-24 06:54:31,093 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-24 06:54:31,093 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-24 06:54:31,094 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-24 06:54:31,095 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-24 06:54:31,095 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-24 06:54:31,096 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-24 06:54:31,096 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-24 06:54:31,097 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-09-24 06:54:31,098 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-09-24 06:54:31,099 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-24 06:54:31,100 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-24 06:54:31,101 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-24 06:54:31,102 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-24 06:54:31,103 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-24 06:54:31,104 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 8
2025-09-24 06:54:31,105 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-24 06:54:31,107 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-24 06:54:31,107 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-24 06:54:31,108 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-24 06:54:31,109 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-24 06:54:31,110 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-24 06:54:31,114 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 06:54:31,134 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 06:54:31,158 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 06:54:31,189 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 06:54:46,050 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 06:54:46,070 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 06:54:46,094 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 06:54:46,130 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 06:55:01,359 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 06:55:01,376 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 06:55:01,391 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 06:55:01,413 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-15 00:00:00
2025-09-24 06:55:15,899 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 06:55:15,913 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 06:55:15,926 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 06:55:15,948 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 06:55:29,660 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 06:55:29,678 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 06:55:29,697 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 06:55:29,723 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 06:55:43,626 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 06:58:44,251 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-24_06-58-44.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │    195 │         0.29 │          31.729 │         3.17 │      9:06:00 │   78     0   117  40.0 │
│ BTC/USDT │    318 │        -0.06 │         -52.683 │        -5.27 │     17:00:00 │  129     0   189  40.6 │
│ ETH/USDT │    289 │        -0.08 │         -94.705 │        -9.47 │      9:14:00 │  105     0   184  36.3 │
│ LTC/USDT │    195 │        -0.24 │        -131.075 │       -13.11 │      9:41:00 │   62     0   133  31.8 │
│ BNB/USDT │    268 │        -0.14 │        -135.269 │       -13.53 │     14:55:00 │  107     0   161  39.9 │
│    TOTAL │   1265 │        -0.06 │        -382.004 │        -38.2 │     12:27:00 │  481     0   784  38.0 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         2.37 │           7.176 │         0.72 │ 6 days, 17:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         2.37 │           7.176 │         0.72 │ 6 days, 17:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                      ENTER TAG STATS                                                      
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│      engulfing_rebond │     136 │        -0.18 │         -42.106 │        -4.21 │     10:55:00 │   46     0    90  33.8 │
│         hammer_rebond │     137 │        -0.33 │        -127.928 │       -12.79 │     16:42:00 │   55     0    82  40.1 │
│ strong_bullish_rebond │     992 │         -0.0 │        -211.970 │        -21.2 │     12:04:00 │  380     0   612  38.3 │
│                 TOTAL │    1265 │        -0.06 │        -382.004 │        -38.2 │     12:27:00 │  481     0   784  38.0 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │   104 │         5.87 │        1406.496 │       140.65 │         22:20:00 │  104     0     0   100 │
│     force_exit │     1 │         2.37 │           7.176 │         0.72 │ 6 days, 17:00:00 │    1     0     0   100 │
│    exit_signal │  1057 │        -0.25 │        -448.147 │       -44.81 │          9:03:00 │  376     0   681  35.6 │
│      stop_loss │   103 │        -4.06 │       -1347.530 │      -134.75 │  1 day, 11:47:00 │    0     0   103     0 │
│          TOTAL │  1265 │        -0.06 │        -382.004 │        -38.2 │         12:27:00 │  481     0   784  38.0 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                                MIXED TAG STATS                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_1R │     85 │         6.03 │        1136.297 │       113.63 │         21:50:00 │   85     0     0   100 │
│         hammer_rebond │ take_profit_1R │     10 │         5.99 │         162.823 │        16.28 │         20:08:00 │   10     0     0   100 │
│      engulfing_rebond │ take_profit_1R │      9 │         4.22 │         107.376 │        10.74 │   1 day, 5:22:00 │    9     0     0   100 │
│         hammer_rebond │    exit_signal │    105 │        -0.05 │          19.737 │         1.97 │         13:19:00 │   45     0    60  42.9 │
│ strong_bullish_rebond │     force_exit │      1 │         2.37 │           7.176 │         0.72 │ 6 days, 17:00:00 │    1     0     0   100 │
│      engulfing_rebond │    exit_signal │    118 │        -0.21 │         -29.483 │        -2.95 │          8:31:00 │   37     0    81  31.4 │
│      engulfing_rebond │      stop_loss │      9 │        -4.21 │        -119.998 │        -12.0 │         23:56:00 │    0     0     9     0 │
│         hammer_rebond │      stop_loss │     22 │         -4.5 │        -310.488 │       -31.05 │   1 day, 7:17:00 │    0     0    22     0 │
│ strong_bullish_rebond │    exit_signal │    834 │        -0.28 │        -438.400 │       -43.84 │          8:36:00 │  294     0   540  35.3 │
│ strong_bullish_rebond │      stop_loss │     72 │        -3.91 │        -917.043 │        -91.7 │  1 day, 14:38:00 │    0     0    72     0 │
│                 TOTAL │                │   1265 │        -0.06 │        -382.004 │        -38.2 │         12:27:00 │  481     0   784  38.0 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2020-01-01 00:00:00             │
│ Backtesting to                │ 2025-09-10 08:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 1265 / 0.61                     │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 617.996 USDT                    │
│ Absolute profit               │ -382.004 USDT                   │
│ Total profit %                │ -38.20%                         │
│ CAGR %                        │ -8.10%                          │
│ Sortino                       │ -0.84                           │
│ Sharpe                        │ -0.56                           │
│ Calmar                        │ -0.76                           │
│ SQN                           │ -1.70                           │
│ Profit factor                 │ 0.87                            │
│ Expectancy (Ratio)            │ -0.30 (-0.08)                   │
│ Avg. daily profit             │ -0.184 USDT                     │
│ Avg. stake amount             │ 257.429 USDT                    │
│ Total trade volume            │ 652215.641 USDT                 │
│                               │                                 │
│ Best Pair                     │ XRP/USDT 3.17%                  │
│ Worst Pair                    │ BNB/USDT -13.53%                │
│ Best trade                    │ XRP/USDT 20.23%                 │
│ Worst trade                   │ ETH/USDT -9.25%                 │
│ Best day                      │ 42.619 USDT                     │
│ Worst day                     │ -48.117 USDT                    │
│ Days win/draw/lose            │ 290 / 1320 / 434                │
│ Min/Max/Avg. Duration Winners │ 0d 00:50 / 9d 22:00 / 0d 17:25  │
│ Min/Max/Avg. Duration Losers  │ 0d 00:30 / 10d 00:05 / 0d 09:24 │
│ Max Consecutive Wins / Loss   │ 10 / 13                         │
│ Rejected Entry signals        │ 384                             │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 544.335 USDT                    │
│ Max balance                   │ 1013.635 USDT                   │
│ Max % of account underwater   │ 46.30%                          │
│ Absolute drawdown             │ 469.301 USDT (46.30%)           │
│ Drawdown duration             │ 1974 days 10:00:00              │
│ Profit at drawdown start      │ 13.635 USDT                     │
│ Profit at drawdown end        │ -455.665 USDT                   │
│ Drawdown start                │ 2020-02-09 13:00:00             │
│ Drawdown end                  │ 2025-07-06 23:00:00             │
│ Market change                 │ 2537.81%                        │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2020-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │   1265 │        -0.06 │        -382.004 │        -38.2 │     12:27:00 │  481     0   784  38.0 │ 469.301 USDT  46.30% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-24T08:58:45.826389",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 663,
  "total_daily_avg_trades": "1265 / 0.61",
  "absolute_profit_usdt": -382.004,
  "total_profit_pct": -38.2,
  "cagr_pct": -8.1,
  "sortino": -0.84,
  "sharpe": -0.56,
  "calmar": -0.76,
  "sqn": -1.7,
  "max_consecutive_wins_loss": "10 / 13",
  "min_balance_usdt": 544.335,
  "max_balance_usdt": 1013.635,
  "absolute_drawdown_pct": 46.3,
  "market_change_pct": 2537.81,
  "win_draw_loss_winpct": "481 0 784 38.0"
}
```
