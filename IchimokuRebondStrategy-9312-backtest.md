# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 9312  
**Timestamp:** 2025-09-24 10:19:58

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 9312,
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
2025-09-24 08:13:20,877 - freqtrade - INFO - freqtrade 2025.8
2025-09-24 08:13:21,322 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-24 08:13:23,477 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-24 08:13:23,487 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-24 08:13:23,488 - freqtrade.loggers - INFO - Logfile configured
2025-09-24 08:13:23,488 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-24 08:13:23,489 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-24 08:13:23,490 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-24 08:13:23,491 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-24 08:13:23,492 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20200101-20251231 ...
2025-09-24 08:13:24,026 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-24 08:13:24,029 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-24 08:13:24,031 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-24 08:13:24,032 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-24 08:13:24,034 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-24 08:13:24,036 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20200101-20251231
2025-09-24 08:13:24,038 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-24 08:13:24,058 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-24 08:13:24,059 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 08:13:24,064 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-24 08:13:24,066 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-24 08:13:24,066 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-24 08:13:24,100 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-24 08:13:28,168 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-24 08:13:28,312 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-24 08:13:28,314 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-24 08:13:28,320 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-24 08:13:28,321 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-24 08:13:28,321 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-24 08:13:28,322 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-24 08:13:28,323 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-24 08:13:28,324 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-24 08:13:28,325 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-24 08:13:28,326 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-24 08:13:28,327 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-24 08:13:28,327 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-24 08:13:28,328 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-24 08:13:28,329 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-24 08:13:28,330 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-24 08:13:28,331 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-24 08:13:28,331 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-24 08:13:28,332 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-24 08:13:28,333 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-24 08:13:28,334 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-24 08:13:28,335 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-24 08:13:28,335 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-24 08:13:28,336 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-24 08:13:28,337 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-24 08:13:28,337 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-24 08:13:28,338 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-24 08:13:28,339 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-24 08:13:28,339 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-24 08:13:28,340 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-24 08:13:28,341 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-24 08:13:28,342 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 08:13:28,367 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-24 08:13:28,398 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-24 08:13:28,458 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 08:13:28,546 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 08:13:28,628 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 08:13:28,703 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 08:13:28,784 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 08:13:28,830 - freqtrade.optimize.backtesting - INFO - Loading data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 08:13:29,215 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 08:13:29,900 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 08:13:30,582 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 08:13:31,254 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 08:13:31,972 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 08:13:34,793 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-24 08:13:34,798 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-24 08:13:34,799 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-24 08:13:34,800 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-24 08:13:34,801 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-24 08:13:34,802 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-24 08:13:34,803 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-24 08:13:34,804 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-24 08:13:34,805 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-24 08:13:34,805 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-24 08:13:34,806 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-24 08:13:34,807 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-24 08:13:34,807 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-09-24 08:13:34,808 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-09-24 08:13:34,809 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-24 08:13:34,810 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-24 08:13:34,810 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-24 08:13:34,811 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-24 08:13:34,812 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-24 08:13:34,812 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 8
2025-09-24 08:13:34,813 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-24 08:13:34,814 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-24 08:13:34,815 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-24 08:13:34,817 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-24 08:13:34,818 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-24 08:13:34,819 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-24 08:13:34,823 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:13:34,852 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 08:13:34,879 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:13:34,911 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 08:13:58,005 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:13:58,035 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 08:13:58,068 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:13:58,103 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 08:14:16,978 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:14:16,993 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 08:14:17,012 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:14:17,040 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-15 00:00:00
2025-09-24 08:14:36,580 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:14:36,601 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 08:14:36,627 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:14:36,659 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 08:14:56,050 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:14:56,071 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 08:14:56,090 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:14:56,115 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 08:15:14,083 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 08:19:56,812 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-24_08-19-56.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │    143 │        -0.12 │          32.458 │         3.25 │     16:06:00 │   80     0    63  55.9 │
│ BTC/USDT │    234 │        -0.01 │          -9.800 │        -0.98 │     19:39:00 │  137     0    97  58.5 │
│ BNB/USDT │    214 │         -0.0 │         -56.441 │        -5.64 │     16:45:00 │  121     0    93  56.5 │
│ ETH/USDT │    200 │         -0.2 │        -114.170 │       -11.42 │     17:43:00 │  113     0    87  56.5 │
│ LTC/USDT │    145 │        -0.37 │        -170.158 │       -17.02 │     20:52:00 │   74     0    71  51.0 │
│    TOTAL │    936 │        -0.12 │        -318.112 │       -31.81 │     18:13:00 │  525     0   411  56.1 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                            LEFT OPEN TRADES REPORT                                            
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         0.07 │           0.243 │         0.02 │ 1 day, 1:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         0.07 │           0.243 │         0.02 │ 1 day, 1:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                       ENTER TAG STATS                                                       
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│      engulfing_rebond │      96 │          0.0 │          18.668 │         1.87 │       15:37:00 │   61     0    35  63.5 │
│         hammer_rebond │     149 │        -0.15 │         -10.944 │        -1.09 │ 1 day, 1:21:00 │   75     0    74  50.3 │
│ strong_bullish_rebond │     691 │        -0.13 │        -325.836 │       -32.58 │       17:03:00 │  389     0   302  56.3 │
│                 TOTAL │     936 │        -0.12 │        -318.112 │       -31.81 │       18:13:00 │  525     0   411  56.1 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                       EXIT REASON STATS                                                       
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃               Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ sell_ichimoku_futur_cloud │   376 │         2.07 │        2430.740 │       243.07 │       13:47:00 │  376     0     0   100 │
│                force_exit │     1 │         0.07 │           0.243 │         0.02 │ 1 day, 1:00:00 │    1     0     0   100 │
│                 stop_loss │    35 │        -5.44 │        -628.962 │        -62.9 │       12:39:00 │    0     0    35     0 │
│               exit_signal │   524 │        -1.34 │       -2120.133 │      -212.01 │       21:46:00 │  148     0   376  28.2 │
│                     TOTAL │   936 │        -0.12 │        -318.112 │       -31.81 │       18:13:00 │  525     0   411  56.1 │
└───────────────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                                    MIXED TAG STATS                                                                     
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃               Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ sell_ichimoku_futur_cloud │    282 │         1.94 │        1691.060 │       169.11 │       12:43:00 │  282     0     0   100 │
│         hammer_rebond │ sell_ichimoku_futur_cloud │     52 │         2.96 │         499.743 │        49.97 │       19:50:00 │   52     0     0   100 │
│      engulfing_rebond │ sell_ichimoku_futur_cloud │     42 │         1.82 │         239.938 │        23.99 │       13:21:00 │   42     0     0   100 │
│ strong_bullish_rebond │                force_exit │      1 │         0.07 │           0.243 │         0.02 │ 1 day, 1:00:00 │    1     0     0   100 │
│      engulfing_rebond │                 stop_loss │      3 │        -5.76 │         -46.941 │        -4.69 │        2:17:00 │    0     0     3     0 │
│         hammer_rebond │                 stop_loss │      8 │        -6.35 │        -156.409 │       -15.64 │       12:31:00 │    0     0     8     0 │
│      engulfing_rebond │               exit_signal │     51 │        -1.16 │        -174.329 │       -17.43 │       18:17:00 │   19     0    32  37.3 │
│         hammer_rebond │               exit_signal │     89 │        -1.41 │        -354.277 │       -35.43 │ 1 day, 5:44:00 │   23     0    66  25.8 │
│ strong_bullish_rebond │                 stop_loss │     24 │         -5.1 │        -425.611 │       -42.56 │       13:59:00 │    0     0    24     0 │
│ strong_bullish_rebond │               exit_signal │    384 │        -1.35 │       -1591.527 │      -159.15 │       20:24:00 │  106     0   278  27.6 │
│                 TOTAL │                           │    936 │        -0.12 │        -318.112 │       -31.81 │       18:13:00 │  525     0   411  56.1 │
└───────────────────────┴───────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2020-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 936 / 0.45                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 681.888 USDT                   │
│ Absolute profit               │ -318.112 USDT                  │
│ Total profit %                │ -31.81%                        │
│ CAGR %                        │ -6.50%                         │
│ Sortino                       │ -0.55                          │
│ Sharpe                        │ -0.34                          │
│ Calmar                        │ -0.57                          │
│ SQN                           │ -1.22                          │
│ Profit factor                 │ 0.91                           │
│ Expectancy (Ratio)            │ -0.34 (-0.04)                  │
│ Avg. daily profit             │ -0.153 USDT                    │
│ Avg. stake amount             │ 321.931 USDT                   │
│ Total trade volume            │ 603542.312 USDT                │
│                               │                                │
│ Best Pair                     │ XRP/USDT 3.25%                 │
│ Worst Pair                    │ LTC/USDT -17.02%               │
│ Best trade                    │ BNB/USDT 12.19%                │
│ Worst trade                   │ XRP/USDT -12.68%               │
│ Best day                      │ 43.581 USDT                    │
│ Worst day                     │ -50.961 USDT                   │
│ Days win/draw/lose            │ 330 / 1416 / 296               │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 4d 17:00 / 0d 14:07 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:30 / 3d 02:00 / 0d 23:28 │
│ Max Consecutive Wins / Loss   │ 10 / 6                         │
│ Rejected Entry signals        │ 263                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 618.146 USDT                   │
│ Max balance                   │ 1261.473 USDT                  │
│ Max % of account underwater   │ 51.00%                         │
│ Absolute drawdown             │ 643.327 USDT (51.00%)          │
│ Drawdown duration             │ 1520 days 05:00:00             │
│ Profit at drawdown start      │ 261.473 USDT                   │
│ Profit at drawdown end        │ -381.854 USDT                  │
│ Drawdown start                │ 2021-05-10 10:00:00            │
│ Drawdown end                  │ 2025-07-08 15:00:00            │
│ Market change                 │ 2537.81%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2020-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    936 │        -0.12 │        -318.112 │       -31.81 │     18:13:00 │  525     0   411  56.1 │ 643.327 USDT  51.00% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-24T10:19:58.282626",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 9312,
  "total_daily_avg_trades": "936 / 0.45",
  "absolute_profit_usdt": -318.112,
  "total_profit_pct": -31.81,
  "cagr_pct": -6.5,
  "sortino": -0.55,
  "sharpe": -0.34,
  "calmar": -0.57,
  "sqn": -1.22,
  "max_consecutive_wins_loss": "10 / 6",
  "min_balance_usdt": 618.146,
  "max_balance_usdt": 1261.473,
  "absolute_drawdown_pct": 51.0,
  "market_change_pct": 2537.81,
  "win_draw_loss_winpct": "525 0 411 56.1"
}
```
