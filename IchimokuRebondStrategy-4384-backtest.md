# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 4384  
**Timestamp:** 2025-09-23 21:31:17

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 4384,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20180101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20180101-20251231
```

## Backtesting Output
```
2025-09-23 19:22:26,247 - freqtrade - INFO - freqtrade 2025.7
2025-09-23 19:22:26,624 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-23 19:22:26,625 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-23 19:22:28,479 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-23 19:22:28,482 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-23 19:22:28,482 - freqtrade.loggers - INFO - Logfile configured
2025-09-23 19:22:28,483 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-23 19:22:28,483 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-23 19:22:28,483 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-23 19:22:28,484 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-23 19:22:28,484 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20251231 ...
2025-09-23 19:22:28,492 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-23 19:22:28,493 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-23 19:22:28,493 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-23 19:22:28,494 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-23 19:22:28,494 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-23 19:22:28,495 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20251231
2025-09-23 19:22:28,496 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-23 19:22:28,515 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-23 19:22:28,516 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 19:22:28,520 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-23 19:22:28,521 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-23 19:22:28,522 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-23 19:22:28,556 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-23 19:22:31,239 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-23 19:22:31,292 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-23 19:22:31,293 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-23 19:22:31,295 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-23 19:22:31,295 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-23 19:22:31,296 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-23 19:22:31,296 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-23 19:22:31,297 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-23 19:22:31,297 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-23 19:22:31,298 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-23 19:22:31,299 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-23 19:22:31,299 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-23 19:22:31,299 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-23 19:22:31,300 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-23 19:22:31,300 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-23 19:22:31,301 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-23 19:22:31,301 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-23 19:22:31,302 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-23 19:22:31,302 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-23 19:22:31,303 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-23 19:22:31,303 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-23 19:22:31,304 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-23 19:22:31,304 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-23 19:22:31,305 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-23 19:22:31,306 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-23 19:22:31,306 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-23 19:22:31,307 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-23 19:22:31,307 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-23 19:22:31,308 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-23 19:22:31,308 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-23 19:22:31,308 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-23 19:22:31,309 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 19:22:31,315 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-23 19:22:31,352 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-23 19:22:31,385 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 19:22:31,456 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 19:22:31,513 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 19:22:31,567 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-23 19:22:31,568 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 19:22:31,623 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 19:22:31,660 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2025-09-11 17:00:00 (2810 days).
2025-09-23 19:22:31,734 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 19:22:32,246 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 19:22:32,663 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 19:22:33,088 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-23 19:22:33,089 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 19:22:33,529 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 19:22:36,458 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-23 19:22:36,460 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-23 19:22:36,461 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-23 19:22:36,462 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-23 19:22:36,462 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-23 19:22:36,463 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-23 19:22:36,463 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-23 19:22:36,464 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-23 19:22:36,464 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-23 19:22:36,465 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-23 19:22:36,465 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-23 19:22:36,466 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-23 19:22:36,467 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-09-23 19:22:36,467 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-09-23 19:22:36,467 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-23 19:22:36,468 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-23 19:22:36,468 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-23 19:22:36,469 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-23 19:22:36,469 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-23 19:22:36,470 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 1
2025-09-23 19:22:36,470 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-23 19:22:36,471 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-23 19:22:36,471 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-23 19:22:36,472 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower
2025-09-23 19:22:36,472 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-23 19:22:36,473 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-23 19:22:36,477 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 19:22:36,487 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 19:22:36,513 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 19:22:36,534 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 19:22:52,075 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 19:22:52,082 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 19:22:52,106 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 19:22:52,124 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 19:23:05,588 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 19:23:05,598 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 19:23:05,619 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 19:23:05,638 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 19:23:19,049 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 19:23:19,057 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-23 19:23:19,058 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 19:23:19,078 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 19:23:19,096 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data starts at 2018-05-04 08:00:00
2025-09-23 19:23:19,097 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 19:23:35,549 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 19:23:35,559 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 19:23:35,585 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 19:23:35,606 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 19:23:56,024 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2025-09-11 17:00:00 (2810 days).
2025-09-23 19:31:15,849 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-23_19-31-15.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │    212 │         1.12 │         934.537 │        93.45 │ 2 days, 0:07:00 │   89     0   123  42.0 │
│ BTC/USDT │    244 │         0.82 │         681.231 │        68.12 │ 2 days, 8:03:00 │  101     0   143  41.4 │
│ BNB/USDT │    218 │          0.8 │         523.976 │         52.4 │ 1 day, 22:19:00 │   80     0   138  36.7 │
│ XRP/USDT │    168 │         0.09 │          73.661 │         7.37 │ 1 day, 11:06:00 │   46     0   122  27.4 │
│ LTC/USDT │    158 │         0.11 │          34.143 │         3.41 │ 1 day, 18:26:00 │   58     0   100  36.7 │
│    TOTAL │   1000 │         0.64 │        2247.547 │       224.75 │ 1 day, 22:34:00 │  374     0   626  37.4 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         4.38 │          28.245 │         2.82 │ 5 days, 15:00:00 │    1     0     0   100 │
│ BTC/USDT │      1 │        -0.12 │          -0.792 │        -0.08 │         13:00:00 │    0     0     1     0 │
│ LTC/USDT │      1 │        -3.08 │         -19.801 │        -1.98 │         17:00:00 │    0     0     1     0 │
│    TOTAL │      3 │         0.39 │           7.652 │         0.77 │  2 days, 7:00:00 │    1     0     2  33.3 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                       ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │     777 │         0.61 │        1540.136 │       154.01 │ 1 day, 22:53:00 │  292     0   485  37.6 │
│      engulfing_rebond │      94 │         0.79 │         404.014 │         40.4 │ 1 day, 23:41:00 │   33     0    61  35.1 │
│         hammer_rebond │     129 │         0.71 │         303.398 │        30.34 │ 1 day, 19:53:00 │   49     0    80  38.0 │
│                 TOTAL │    1000 │         0.64 │        2247.547 │       224.75 │ 1 day, 22:34:00 │  374     0   626  37.4 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │   200 │        10.45 │        8473.958 │        847.4 │ 2 days, 2:17:00 │  200     0     0   100 │
│     force_exit │     3 │         0.39 │           7.652 │         0.77 │ 2 days, 7:00:00 │    1     0     2  33.3 │
│      stop_loss │    21 │       -10.18 │        -734.631 │       -73.46 │        15:50:00 │    0     0    21     0 │
│    exit_signal │   776 │        -1.59 │       -5499.433 │      -549.94 │ 1 day, 22:25:00 │  173     0   603  22.3 │
│          TOTAL │  1000 │         0.64 │        2247.547 │       224.75 │ 1 day, 22:34:00 │  374     0   626  37.4 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                               MIXED TAG STATS                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_1R │    153 │        10.43 │        6446.025 │        644.6 │ 2 days, 2:59:00 │  153     0     0   100 │
│         hammer_rebond │ take_profit_1R │     26 │        10.62 │        1017.853 │       101.79 │ 1 day, 19:41:00 │   26     0     0   100 │
│      engulfing_rebond │ take_profit_1R │     21 │        10.38 │        1010.081 │       101.01 │ 2 days, 5:22:00 │   21     0     0   100 │
│ strong_bullish_rebond │     force_exit │      2 │         0.65 │           8.444 │         0.84 │ 3 days, 4:00:00 │    1     0     1  50.0 │
│      engulfing_rebond │     force_exit │      1 │        -0.12 │          -0.792 │        -0.08 │        13:00:00 │    0     0     1     0 │
│      engulfing_rebond │      stop_loss │      1 │       -10.18 │         -70.260 │        -7.03 │        19:25:00 │    0     0     1     0 │
│         hammer_rebond │      stop_loss │      5 │       -10.18 │        -221.280 │       -22.13 │        12:01:00 │    0     0     5     0 │
│ strong_bullish_rebond │      stop_loss │     15 │       -10.18 │        -443.090 │       -44.31 │        16:52:00 │    0     0    15     0 │
│         hammer_rebond │    exit_signal │     98 │        -1.37 │        -493.175 │       -49.32 │ 1 day, 21:34:00 │   23     0    75  23.5 │
│      engulfing_rebond │    exit_signal │     71 │        -1.88 │        -535.015 │        -53.5 │ 1 day, 22:53:00 │   12     0    59  16.9 │
│ strong_bullish_rebond │    exit_signal │    607 │        -1.59 │       -4471.242 │      -447.12 │ 1 day, 22:30:00 │  138     0   469  22.7 │
│                 TOTAL │                │   1000 │         0.64 │        2247.547 │       224.75 │ 1 day, 22:34:00 │  374     0   626  37.4 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2018-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-11 17:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 1000 / 0.36                    │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 3247.547 USDT                  │
│ Absolute profit               │ 2247.547 USDT                  │
│ Total profit %                │ 224.75%                        │
│ CAGR %                        │ 16.53%                         │
│ Sortino                       │ 1.52                           │
│ Sharpe                        │ 0.63                           │
│ Calmar                        │ 9.65                           │
│ SQN                           │ 2.91                           │
│ Profit factor                 │ 1.29                           │
│ Expectancy (Ratio)            │ 2.25 (0.18)                    │
│ Avg. daily profit             │ 0.8 USDT                       │
│ Avg. stake amount             │ 452.942 USDT                   │
│ Total trade volume            │ 909949.141 USDT                │
│                               │                                │
│ Best Pair                     │ ETH/USDT 93.45%                │
│ Worst Pair                    │ LTC/USDT 3.41%                 │
│ Best trade                    │ XRP/USDT 13.21%                │
│ Worst trade                   │ BNB/USDT -10.18%               │
│ Best day                      │ 182.597 USDT                   │
│ Worst day                     │ -86.798 USDT                   │
│ Days win/draw/lose            │ 267 / 2077 / 416               │
│ Min/Max/Avg. Duration Winners │ 0d 00:20 / 7d 19:35 / 2d 18:54 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 4d 07:00 / 1d 10:26 │
│ Max Consecutive Wins / Loss   │ 9 / 15                         │
│ Rejected Entry signals        │ 2499                           │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 934.497 USDT                   │
│ Max balance                   │ 3494.108 USDT                  │
│ Max % of account underwater   │ 16.69%                         │
│ Absolute Drawdown (Account)   │ 15.84%                         │
│ Absolute Drawdown             │ 553.313 USDT                   │
│ Drawdown high                 │ 2494.108 USDT                  │
│ Drawdown low                  │ 1940.795 USDT                  │
│ Drawdown Start                │ 2024-12-01 19:50:00            │
│ Drawdown End                  │ 2025-05-04 03:00:00            │
│ Market change                 │ 2415.18%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │   1000 │         0.64 │        2247.547 │       224.75 │ 1 day, 22:34:00 │  374     0   626  37.4 │ 553.313 USDT  15.84% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-23T21:31:17.291282",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 4384,
  "total_daily_avg_trades": "1000 / 0.36",
  "absolute_profit_usdt": 2247.547,
  "total_profit_pct": 224.75,
  "cagr_pct": 16.53,
  "sortino": 1.52,
  "sharpe": 0.63,
  "calmar": 9.65,
  "sqn": 2.91,
  "max_consecutive_wins_loss": "9 / 15",
  "min_balance_usdt": 934.497,
  "max_balance_usdt": 3494.108,
  "market_change_pct": 2415.18
}
```
