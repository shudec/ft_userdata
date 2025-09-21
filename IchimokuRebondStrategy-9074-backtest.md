# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 9074  
**Timestamp:** 2025-09-19 22:07:04

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy",
  "random_state": 9074,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231
```

## Backtesting Output
```
2025-09-19 20:06:36,618 - freqtrade - INFO - freqtrade 2025.7
2025-09-19 20:06:37,021 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-19 20:06:37,022 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-19 20:06:38,640 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-19 20:06:38,643 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-19 20:06:38,643 - freqtrade.loggers - INFO - Logfile configured
2025-09-19 20:06:38,643 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-19 20:06:38,644 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-19 20:06:38,644 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-19 20:06:38,645 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-19 20:06:38,645 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-19 20:06:38,653 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-19 20:06:38,653 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-19 20:06:38,654 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-19 20:06:38,654 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-19 20:06:38,655 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-19 20:06:38,655 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-19 20:06:38,657 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-19 20:06:38,678 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-19 20:06:38,679 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 20:06:38,684 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-19 20:06:38,685 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-19 20:06:38,685 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-19 20:06:38,721 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-19 20:06:41,222 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-19 20:06:41,259 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-19 20:06:41,260 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-19 20:06:41,261 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-19 20:06:41,261 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-19 20:06:41,262 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-19 20:06:41,262 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-19 20:06:41,263 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-19 20:06:41,263 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-19 20:06:41,264 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-19 20:06:41,264 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-19 20:06:41,264 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-19 20:06:41,265 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-19 20:06:41,265 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-19 20:06:41,265 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-19 20:06:41,266 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-19 20:06:41,266 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-19 20:06:41,267 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-19 20:06:41,267 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-19 20:06:41,267 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-19 20:06:41,268 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-19 20:06:41,268 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-19 20:06:41,268 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-19 20:06:41,269 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-19 20:06:41,269 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-19 20:06:41,269 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-19 20:06:41,270 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-19 20:06:41,270 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-19 20:06:41,271 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-19 20:06:41,271 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-19 20:06:41,271 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-19 20:06:41,272 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 20:06:41,277 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-19 20:06:41,311 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-19 20:06:41,345 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-19 20:06:41,397 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-19 20:06:41,448 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-19 20:06:41,502 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-19 20:06:41,553 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-19 20:06:41,583 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-19 20:06:41,667 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-19 20:06:41,904 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-19 20:06:42,185 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-19 20:06:42,404 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-19 20:06:42,643 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-19 20:06:44,077 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-19 20:06:44,078 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-19 20:06:44,078 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-19 20:06:44,079 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-19 20:06:44,079 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-19 20:06:44,080 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 11
2025-09-19 20:06:44,080 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.568
2025-09-19 20:06:44,080 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.885
2025-09-19 20:06:44,081 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.029
2025-09-19 20:06:44,081 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.0
2025-09-19 20:06:44,081 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.001
2025-09-19 20:06:44,082 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-19 20:06:44,082 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 2
2025-09-19 20:06:44,082 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-09-19 20:06:44,083 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-19 20:06:44,083 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-19 20:06:44,083 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-19 20:06:44,084 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-19 20:06:44,085 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 20:06:44,094 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-19 20:06:46,752 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 20:06:46,759 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-19 20:06:49,405 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 20:06:49,413 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-19 20:06:52,084 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 20:06:52,091 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-19 20:06:54,695 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 20:06:54,702 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-19 20:06:57,393 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-19 20:07:03,572 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-19_20-07-03.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │      7 │          0.9 │          63.047 │          6.3 │      6:55:00 │    4     0     3  57.1 │
│ LTC/USDT │      4 │          1.4 │          40.070 │         4.01 │      8:48:00 │    1     0     3  25.0 │
│ BNB/USDT │      8 │        -0.01 │          -1.189 │        -0.12 │      4:17:00 │    2     0     6  25.0 │
│ BTC/USDT │      8 │        -0.27 │         -21.229 │        -2.12 │      8:54:00 │    2     0     6  25.0 │
│ ETH/USDT │      9 │        -0.33 │         -31.553 │        -3.16 │      1:53:00 │    1     0     8  11.1 │
│    TOTAL │     36 │         0.19 │          49.146 │         4.91 │      5:43:00 │   10     0    26  27.8 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
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
│     OTHER │      36 │         0.19 │          49.146 │         4.91 │      5:43:00 │   10     0    26  27.8 │
│     TOTAL │      36 │         0.19 │          49.146 │         4.91 │      5:43:00 │   10     0    26  27.8 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │     8 │          2.7 │         204.654 │        20.47 │      7:23:00 │    8     0     0   100 │
│    exit_signal │     6 │        -0.28 │         -16.905 │        -1.69 │     16:10:00 │    2     0     4  33.3 │
│      stop_loss │    22 │         -0.6 │        -138.603 │       -13.86 │      2:16:00 │    0     0    22     0 │
│          TOTAL │    36 │         0.19 │          49.146 │         4.91 │      5:43:00 │   10     0    26  27.8 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_3R │      8 │          2.7 │         204.654 │        20.47 │      7:23:00 │    8     0     0   100 │
│           │    exit_signal │      6 │        -0.28 │         -16.905 │        -1.69 │     16:10:00 │    2     0     4  33.3 │
│           │      stop_loss │     22 │         -0.6 │        -138.603 │       -13.86 │      2:16:00 │    0     0    22     0 │
│     TOTAL │                │     36 │         0.19 │          49.146 │         4.91 │      5:43:00 │   10     0    26  27.8 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-11 17:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 36 / 0.03                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1049.146 USDT                  │
│ Absolute profit               │ 49.146 USDT                    │
│ Total profit %                │ 4.91%                          │
│ CAGR %                        │ 1.31%                          │
│ Sortino                       │ 0.26                           │
│ Sharpe                        │ 0.04                           │
│ Calmar                        │ 1.12                           │
│ SQN                           │ 0.51                           │
│ Profit factor                 │ 1.31                           │
│ Expectancy (Ratio)            │ 1.37 (0.22)                    │
│ Avg. daily profit             │ 0.036 USDT                     │
│ Avg. stake amount             │ 1035.988 USDT                  │
│ Total trade volume            │ 74789.704 USDT                 │
│                               │                                │
│ Best Pair                     │ XRP/USDT 6.30%                 │
│ Worst Pair                    │ ETH/USDT -3.16%                │
│ Best trade                    │ LTC/USDT 8.27%                 │
│ Worst trade                   │ LTC/USDT -1.34%                │
│ Best day                      │ 67.965 USDT                    │
│ Worst day                     │ -21.238 USDT                   │
│ Days win/draw/lose            │ 10 / 1229 / 25                 │
│ Min/Max/Avg. Duration Winners │ 0d 01:25 / 1d 02:40 / 0d 10:48 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:05 / 0d 20:00 / 0d 03:46 │
│ Max Consecutive Wins / Loss   │ 2 / 11                         │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 1023.595 USDT                  │
│ Max balance                   │ 1091.56 USDT                   │
│ Max % of account underwater   │ 6.19%                          │
│ Absolute Drawdown (Account)   │ 6.19%                          │
│ Absolute Drawdown             │ 67.548 USDT                    │
│ Drawdown high                 │ 91.56 USDT                     │
│ Drawdown low                  │ 24.012 USDT                    │
│ Drawdown Start                │ 2022-11-05 16:40:00            │
│ Drawdown End                  │ 2023-09-06 04:50:00            │
│ Market change                 │ 94.84%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     36 │         0.19 │          49.146 │         4.91 │      5:43:00 │   10     0    26  27.8 │ 67.548 USDT  6.19% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-19T22:07:04.704095",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 9074,
  "total_daily_avg_trades": "36 / 0.03",
  "absolute_profit_usdt": 49.146,
  "total_profit_pct": 4.91,
  "cagr_pct": 1.31,
  "sortino": 0.26,
  "sharpe": 0.04,
  "calmar": 1.12,
  "sqn": 0.51,
  "max_consecutive_wins_loss": "2 / 11",
  "min_balance_usdt": 1023.595,
  "max_balance_usdt": 1091.56,
  "absolute_drawdown_pct": 6.19,
  "market_change_pct": 94.84,
  "win_draw_loss_winpct": "10 0 26 27.8"
}
```
