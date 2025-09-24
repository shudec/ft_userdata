# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 4313  
**Timestamp:** 2025-09-24 13:04:27

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 4313,
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
2025-09-24 10:58:20,368 - freqtrade - INFO - freqtrade 2025.8
2025-09-24 10:58:20,973 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-24 10:58:23,753 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-24 10:58:23,760 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-24 10:58:23,761 - freqtrade.loggers - INFO - Logfile configured
2025-09-24 10:58:23,761 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-24 10:58:23,762 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-24 10:58:23,763 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-24 10:58:23,763 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-24 10:58:23,764 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20200101-20251231 ...
2025-09-24 10:58:24,332 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-24 10:58:24,335 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-24 10:58:24,335 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-24 10:58:24,336 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-24 10:58:24,336 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-24 10:58:24,337 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20200101-20251231
2025-09-24 10:58:24,339 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-24 10:58:24,355 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-24 10:58:24,356 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 10:58:24,359 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-24 10:58:24,360 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-24 10:58:24,360 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-24 10:58:24,386 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-24 10:58:27,109 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-24 10:58:27,215 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-24 10:58:27,217 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-24 10:58:27,223 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-24 10:58:27,223 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-24 10:58:27,224 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-24 10:58:27,224 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-24 10:58:27,224 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-24 10:58:27,225 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-24 10:58:27,225 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-24 10:58:27,226 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-24 10:58:27,226 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-24 10:58:27,226 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-24 10:58:27,227 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-24 10:58:27,227 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-24 10:58:27,227 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-24 10:58:27,228 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-24 10:58:27,228 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-24 10:58:27,228 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-24 10:58:27,229 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-24 10:58:27,229 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-24 10:58:27,229 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-24 10:58:27,230 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-24 10:58:27,230 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-24 10:58:27,231 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-24 10:58:27,231 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-24 10:58:27,232 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-24 10:58:27,232 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-24 10:58:27,232 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-24 10:58:27,232 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-24 10:58:27,233 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-24 10:58:27,233 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 10:58:27,257 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-24 10:58:27,281 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-24 10:58:27,338 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 10:58:27,412 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 10:58:27,473 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 10:58:27,538 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 10:58:27,606 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 10:58:27,643 - freqtrade.optimize.backtesting - INFO - Loading data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 10:58:27,989 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 10:58:28,455 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 10:58:28,923 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 10:58:29,439 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 10:58:29,941 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 10:58:31,832 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-24 10:58:31,838 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-24 10:58:31,839 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-24 10:58:31,840 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-24 10:58:31,840 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-24 10:58:31,841 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-24 10:58:31,841 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-24 10:58:31,842 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-24 10:58:31,843 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-24 10:58:31,843 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-24 10:58:31,844 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-24 10:58:31,844 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-24 10:58:31,845 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-09-24 10:58:31,845 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-09-24 10:58:31,846 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-24 10:58:31,847 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-24 10:58:31,847 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-24 10:58:31,848 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-24 10:58:31,849 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): custom_sell_atr_factor = 4.5
2025-09-24 10:58:31,850 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-24 10:58:31,851 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 8
2025-09-24 10:58:31,851 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-24 10:58:31,851 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-24 10:58:31,852 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-24 10:58:31,853 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-24 10:58:31,853 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-24 10:58:31,853 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-24 10:58:31,856 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 10:58:31,876 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 10:58:31,894 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 10:58:31,919 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 10:58:47,614 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 10:58:47,630 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 10:58:47,647 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 10:58:47,671 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 10:59:03,524 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 10:59:03,541 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 10:59:03,563 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 10:59:03,590 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-15 00:00:00
2025-09-24 10:59:19,920 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 10:59:19,944 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 10:59:19,967 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 10:59:20,002 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 10:59:37,213 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 10:59:37,233 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 10:59:37,272 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 10:59:37,316 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 10:59:53,152 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 11:04:25,615 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-24_11-04-25.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │    128 │         0.95 │         741.377 │        74.14 │ 2 days, 7:56:00 │   54     0    74  42.2 │
│ ETH/USDT │    104 │         0.65 │         452.660 │        45.27 │ 2 days, 2:32:00 │   37     0    67  35.6 │
│ BNB/USDT │    125 │         1.24 │         372.687 │        37.27 │ 2 days, 6:05:00 │   42     0    83  33.6 │
│ LTC/USDT │     96 │         -0.1 │         -34.458 │        -3.45 │ 1 day, 20:47:00 │   30     0    66  31.3 │
│ XRP/USDT │     87 │        -0.83 │        -532.658 │       -53.27 │ 1 day, 13:54:00 │   19     0    68  21.8 │
│    TOTAL │    540 │         0.49 │         999.608 │        99.96 │ 2 days, 1:35:00 │  182     0   358  33.7 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                            LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         3.08 │          30.060 │         3.01 │ 4 days, 6:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         3.08 │          30.060 │         3.01 │ 4 days, 6:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                       ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │     429 │          0.3 │         653.493 │        65.35 │ 2 days, 1:34:00 │  143     0   286  33.3 │
│      engulfing_rebond │      61 │         1.77 │         335.346 │        33.53 │ 2 days, 2:53:00 │   21     0    40  34.4 │
│         hammer_rebond │      50 │         0.54 │          10.769 │         1.08 │ 2 days, 0:03:00 │   18     0    32  36.0 │
│                 TOTAL │     540 │         0.49 │         999.608 │        99.96 │ 2 days, 1:35:00 │  182     0   358  33.7 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │    42 │         17.1 │        3795.703 │       379.57 │ 3 days, 6:50:00 │   42     0     0   100 │
│     force_exit │     1 │         3.08 │          30.060 │         3.01 │ 4 days, 6:00:00 │    1     0     0   100 │
│      stop_loss │    21 │        -5.59 │        -635.059 │       -63.51 │        23:35:00 │    0     0    21     0 │
│    exit_signal │   476 │        -0.72 │       -2191.095 │      -219.11 │ 2 days, 0:02:00 │  139     0   337  29.2 │
│          TOTAL │   540 │         0.49 │         999.608 │        99.96 │ 2 days, 1:35:00 │  182     0   358  33.7 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                                MIXED TAG STATS                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_3R │     33 │        16.19 │        3008.386 │       300.84 │  3 days, 7:11:00 │   33     0     0   100 │
│      engulfing_rebond │ take_profit_3R │      7 │        18.84 │         614.367 │        61.44 │  3 days, 1:10:00 │    7     0     0   100 │
│         hammer_rebond │ take_profit_3R │      2 │        25.99 │         172.950 │        17.29 │ 3 days, 20:48:00 │    2     0     0   100 │
│ strong_bullish_rebond │     force_exit │      1 │         3.08 │          30.060 │         3.01 │  4 days, 6:00:00 │    1     0     0   100 │
│         hammer_rebond │    exit_signal │     45 │        -0.26 │         -79.795 │        -7.98 │  1 day, 23:37:00 │   16     0    29  35.6 │
│         hammer_rebond │      stop_loss │      3 │        -4.39 │         -82.386 │        -8.24 │   1 day, 0:32:00 │    0     0     3     0 │
│      engulfing_rebond │      stop_loss │      3 │        -6.75 │        -110.432 │       -11.04 │         16:55:00 │    0     0     3     0 │
│      engulfing_rebond │    exit_signal │     51 │        -0.07 │        -168.589 │       -16.86 │  2 days, 1:49:00 │   14     0    37  27.5 │
│ strong_bullish_rebond │      stop_loss │     15 │        -5.59 │        -442.241 │       -44.22 │   1 day, 0:44:00 │    0     0    15     0 │
│ strong_bullish_rebond │    exit_signal │    380 │        -0.86 │       -1942.711 │      -194.27 │  1 day, 23:50:00 │  109     0   271  28.7 │
│                 TOTAL │                │    540 │         0.49 │         999.608 │        99.96 │  2 days, 1:35:00 │  182     0   358  33.7 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2020-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 540 / 0.26                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1999.608 USDT                  │
│ Absolute profit               │ 999.608 USDT                   │
│ Total profit %                │ 99.96%                         │
│ CAGR %                        │ 12.94%                         │
│ Sortino                       │ 0.93                           │
│ Sharpe                        │ 0.27                           │
│ Calmar                        │ 2.47                           │
│ SQN                           │ 1.28                           │
│ Profit factor                 │ 1.18                           │
│ Expectancy (Ratio)            │ 1.85 (0.12)                    │
│ Avg. daily profit             │ 0.481 USDT                     │
│ Avg. stake amount             │ 684.516 USDT                   │
│ Total trade volume            │ 741758.435 USDT                │
│                               │                                │
│ Best Pair                     │ BTC/USDT 74.14%                │
│ Worst Pair                    │ XRP/USDT -53.27%               │
│ Best trade                    │ BNB/USDT 38.12%                │
│ Worst trade                   │ LTC/USDT -14.45%               │
│ Best day                      │ 162.411 USDT                   │
│ Worst day                     │ -78.556 USDT                   │
│ Days win/draw/lose            │ 144 / 1640 / 256               │
│ Min/Max/Avg. Duration Winners │ 0d 06:05 / 8d 18:00 / 3d 14:55 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:30 / 4d 03:00 / 1d 06:35 │
│ Max Consecutive Wins / Loss   │ 7 / 18                         │
│ Rejected Entry signals        │ 480                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 937.071 USDT                   │
│ Max balance                   │ 2780.868 USDT                  │
│ Max % of account underwater   │ 37.22%                         │
│ Absolute drawdown             │ 1035.089 USDT (37.22%)         │
│ Drawdown duration             │ 862 days 18:00:00              │
│ Profit at drawdown start      │ 1780.868 USDT                  │
│ Profit at drawdown end        │ 745.779 USDT                   │
│ Drawdown start                │ 2023-01-24 23:00:00            │
│ Drawdown end                  │ 2025-06-05 17:00:00            │
│ Market change                 │ 2537.81%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2020-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃              Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    540 │         0.49 │         999.608 │        99.96 │ 2 days, 1:35:00 │  182     0   358  33.7 │ 1035.089 USDT  37.22% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴───────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-24T13:04:27.277912",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 4313,
  "total_daily_avg_trades": "540 / 0.26",
  "absolute_profit_usdt": 999.608,
  "total_profit_pct": 99.96,
  "cagr_pct": 12.94,
  "sortino": 0.93,
  "sharpe": 0.27,
  "calmar": 2.47,
  "sqn": 1.28,
  "max_consecutive_wins_loss": "7 / 18",
  "min_balance_usdt": 937.071,
  "max_balance_usdt": 2780.868,
  "absolute_drawdown_pct": 37.22,
  "market_change_pct": 2537.81
}
```
