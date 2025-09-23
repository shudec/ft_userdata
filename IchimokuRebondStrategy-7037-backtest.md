# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 7037  
**Timestamp:** 2025-09-23 22:27:56

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 7037,
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
2025-09-23 20:21:06,152 - freqtrade - INFO - freqtrade 2025.7
2025-09-23 20:21:06,486 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-23 20:21:06,486 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-23 20:21:07,971 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-23 20:21:07,973 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-23 20:21:07,974 - freqtrade.loggers - INFO - Logfile configured
2025-09-23 20:21:07,974 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-23 20:21:07,975 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-23 20:21:07,975 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-23 20:21:07,975 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-23 20:21:07,976 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20200101-20251231 ...
2025-09-23 20:21:07,984 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-23 20:21:07,984 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-23 20:21:07,985 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-23 20:21:07,985 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-23 20:21:07,986 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-23 20:21:07,986 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20200101-20251231
2025-09-23 20:21:07,987 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-23 20:21:08,005 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-23 20:21:08,006 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 20:21:08,010 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-23 20:21:08,011 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-23 20:21:08,011 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-23 20:21:08,044 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-23 20:21:10,464 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-23 20:21:10,503 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-23 20:21:10,503 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-23 20:21:10,504 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-23 20:21:10,505 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-23 20:21:10,505 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-23 20:21:10,505 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-23 20:21:10,506 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-23 20:21:10,506 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-23 20:21:10,506 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-23 20:21:10,507 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-23 20:21:10,507 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-23 20:21:10,507 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-23 20:21:10,508 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-23 20:21:10,508 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-23 20:21:10,508 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-23 20:21:10,509 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-23 20:21:10,509 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-23 20:21:10,510 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-23 20:21:10,510 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-23 20:21:10,510 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-23 20:21:10,511 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-23 20:21:10,511 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-23 20:21:10,511 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-23 20:21:10,512 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-23 20:21:10,512 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-23 20:21:10,512 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-23 20:21:10,512 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-23 20:21:10,513 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-23 20:21:10,513 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-23 20:21:10,513 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-23 20:21:10,514 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 20:21:10,519 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-23 20:21:10,551 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-23 20:21:10,583 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 20:21:10,646 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 20:21:10,727 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 20:21:10,783 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 20:21:10,833 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 20:21:10,867 - freqtrade.optimize.backtesting - INFO - Loading data from 2020-01-01 00:00:00 up to 2025-09-11 17:00:00 (2080 days).
2025-09-23 20:21:10,941 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 20:21:11,301 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 20:21:11,589 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 20:21:11,910 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 20:21:12,209 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 20:21:14,235 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-23 20:21:14,236 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-23 20:21:14,237 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-23 20:21:14,237 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-23 20:21:14,238 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-23 20:21:14,238 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-23 20:21:14,238 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-23 20:21:14,239 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-23 20:21:14,239 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-23 20:21:14,239 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-23 20:21:14,240 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-23 20:21:14,240 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-23 20:21:14,240 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-09-23 20:21:14,241 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-09-23 20:21:14,241 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-23 20:21:14,241 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-23 20:21:14,242 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-23 20:21:14,242 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-23 20:21:14,243 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-23 20:21:14,243 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 8
2025-09-23 20:21:14,243 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-23 20:21:14,244 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-23 20:21:14,244 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-23 20:21:14,244 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-23 20:21:14,245 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-23 20:21:14,245 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-23 20:21:14,248 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:21:14,259 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 20:21:14,282 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:21:14,300 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 20:21:28,993 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:21:29,001 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 20:21:29,022 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:21:29,039 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 20:21:43,905 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:21:43,913 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 20:21:43,932 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:21:43,950 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 20:21:58,746 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:21:58,754 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 20:21:58,775 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:21:58,792 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 20:22:13,432 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:22:13,440 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 20:22:13,460 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:22:13,478 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 20:22:28,318 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2020-01-01 00:00:00 up to 2025-09-11 17:00:00 (2080 days).
2025-09-23 20:27:55,215 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-23_20-27-55.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │    195 │         0.74 │         552.789 │        55.28 │ 1 day, 15:51:00 │   85     0   110  43.6 │
│ BTC/USDT │    220 │         0.31 │         281.085 │        28.11 │ 1 day, 18:25:00 │   90     0   130  40.9 │
│ BNB/USDT │    189 │         0.57 │         214.346 │        21.43 │ 1 day, 14:30:00 │   72     0   117  38.1 │
│ XRP/USDT │    136 │         0.26 │         198.403 │        19.84 │ 1 day, 10:46:00 │   44     0    92  32.4 │
│ LTC/USDT │    135 │          0.1 │         -36.330 │        -3.63 │ 1 day, 12:19:00 │   48     0    87  35.6 │
│    TOTAL │    875 │         0.42 │        1210.292 │       121.03 │ 1 day, 14:52:00 │  339     0   536  38.7 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         1.33 │          14.764 │         1.48 │ 2 days, 10:00:00 │    1     0     0   100 │
│ BTC/USDT │      1 │        -0.12 │          -0.491 │        -0.05 │         13:00:00 │    0     0     1     0 │
│ LTC/USDT │      1 │        -3.08 │         -21.348 │        -2.13 │         17:00:00 │    0     0     1     0 │
│    TOTAL │      3 │        -0.62 │          -7.075 │        -0.71 │   1 day, 5:20:00 │    1     0     2  33.3 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                       ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │     690 │         0.42 │         892.027 │         89.2 │ 1 day, 14:54:00 │  268     0   422  38.8 │
│         hammer_rebond │      97 │         0.54 │         168.885 │        16.89 │ 1 day, 13:13:00 │   38     0    59  39.2 │
│      engulfing_rebond │      88 │         0.32 │         149.381 │        14.94 │ 1 day, 16:25:00 │   33     0    55  37.5 │
│                 TOTAL │     875 │         0.42 │        1210.292 │       121.03 │ 1 day, 14:52:00 │  339     0   536  38.7 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │   278 │         6.46 │        9624.946 │       962.49 │ 1 day, 12:48:00 │  278     0     0   100 │
│     force_exit │     3 │        -0.62 │          -7.075 │        -0.71 │  1 day, 5:20:00 │    1     0     2  33.3 │
│      stop_loss │    40 │        -5.76 │       -1374.049 │       -137.4 │        17:34:00 │    0     0    40     0 │
│    exit_signal │   554 │        -2.16 │       -7033.529 │      -703.35 │ 1 day, 17:30:00 │   60     0   494  10.8 │
│          TOTAL │   875 │         0.42 │        1210.292 │       121.03 │ 1 day, 14:52:00 │  339     0   536  38.7 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                               MIXED TAG STATS                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_1R │    220 │         6.45 │        7622.566 │       762.26 │ 1 day, 13:08:00 │  220     0     0   100 │
│         hammer_rebond │ take_profit_1R │     31 │         6.56 │        1069.553 │       106.96 │  1 day, 8:09:00 │   31     0     0   100 │
│      engulfing_rebond │ take_profit_1R │     27 │         6.42 │         932.827 │        93.28 │ 1 day, 15:22:00 │   27     0     0   100 │
│      engulfing_rebond │     force_exit │      1 │        -0.12 │          -0.491 │        -0.05 │        13:00:00 │    0     0     1     0 │
│ strong_bullish_rebond │     force_exit │      2 │        -0.88 │          -6.585 │        -0.66 │ 1 day, 13:30:00 │    1     0     1  50.0 │
│      engulfing_rebond │      stop_loss │      2 │        -7.88 │         -73.386 │        -7.34 │  1 day, 9:28:00 │    0     0     2     0 │
│         hammer_rebond │      stop_loss │      6 │        -6.32 │        -201.518 │       -20.15 │        12:08:00 │    0     0     6     0 │
│         hammer_rebond │    exit_signal │     60 │        -1.89 │        -699.150 │       -69.91 │ 1 day, 18:21:00 │    7     0    53  11.7 │
│      engulfing_rebond │    exit_signal │     58 │        -2.23 │        -709.569 │       -70.96 │ 1 day, 17:36:00 │    6     0    52  10.3 │
│ strong_bullish_rebond │      stop_loss │     32 │        -5.53 │       -1099.145 │      -109.91 │        17:36:00 │    0     0    32     0 │
│ strong_bullish_rebond │    exit_signal │    436 │        -2.18 │       -5624.810 │      -562.48 │ 1 day, 17:22:00 │   47     0   389  10.8 │
│                 TOTAL │                │    875 │         0.42 │        1210.292 │       121.03 │ 1 day, 14:52:00 │  339     0   536  38.7 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2020-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-11 17:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 875 / 0.42                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 2210.292 USDT                  │
│ Absolute profit               │ 1210.292 USDT                  │
│ Total profit %                │ 121.03%                        │
│ CAGR %                        │ 14.93%                         │
│ Sortino                       │ 1.03                           │
│ Sharpe                        │ 0.43                           │
│ Calmar                        │ 4.04                           │
│ SQN                           │ 1.58                           │
│ Profit factor                 │ 1.14                           │
│ Expectancy (Ratio)            │ 1.38 (0.08)                    │
│ Avg. daily profit             │ 0.582 USDT                     │
│ Avg. stake amount             │ 633.423 USDT                   │
│ Total trade volume            │ 1111922.842 USDT               │
│                               │                                │
│ Best Pair                     │ ETH/USDT 55.28%                │
│ Worst Pair                    │ LTC/USDT -3.63%                │
│ Best trade                    │ XRP/USDT 20.23%                │
│ Worst trade                   │ LTC/USDT -11.67%               │
│ Best day                      │ 164.522 USDT                   │
│ Worst day                     │ -107.295 USDT                  │
│ Days win/draw/lose            │ 235 / 1460 / 346               │
│ Min/Max/Avg. Duration Winners │ 0d 00:50 / 6d 21:00 / 1d 22:05 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 4d 07:00 / 1d 10:18 │
│ Max Consecutive Wins / Loss   │ 10 / 16                        │
│ Rejected Entry signals        │ 1561                           │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 857.025 USDT                   │
│ Max balance                   │ 2584.674 USDT                  │
│ Max % of account underwater   │ 27.49%                         │
│ Absolute Drawdown (Account)   │ 27.49%                         │
│ Absolute Drawdown             │ 674.388 USDT                   │
│ Drawdown high                 │ 1453.211 USDT                  │
│ Drawdown low                  │ 778.823 USDT                   │
│ Drawdown Start                │ 2023-01-14 06:50:00            │
│ Drawdown End                  │ 2023-09-27 15:00:00            │
│ Market change                 │ 2586.51%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2020-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    875 │         0.42 │        1210.292 │       121.03 │ 1 day, 14:52:00 │  339     0   536  38.7 │ 674.388 USDT  27.49% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-23T22:27:56.558478",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 7037,
  "total_daily_avg_trades": "875 / 0.42",
  "absolute_profit_usdt": 1210.292,
  "total_profit_pct": 121.03,
  "cagr_pct": 14.93,
  "sortino": 1.03,
  "sharpe": 0.43,
  "calmar": 4.04,
  "sqn": 1.58,
  "max_consecutive_wins_loss": "10 / 16",
  "min_balance_usdt": 857.025,
  "max_balance_usdt": 2584.674,
  "market_change_pct": 2586.51
}
```
