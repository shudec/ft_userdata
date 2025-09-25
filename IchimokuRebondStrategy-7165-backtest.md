# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 7165  
**Timestamp:** 2025-09-25 22:22:24

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 7165,
  "epochs": 100,
  "hyperopt_timerange": "20220101-20231231",
  "backtest_timerange": "20220101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231
```

## Backtesting Output
```
2025-09-25 20:20:13,177 - freqtrade - INFO - freqtrade 2025.7
2025-09-25 20:20:13,614 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-25 20:20:13,614 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-25 20:20:15,495 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-25 20:20:15,498 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-25 20:20:15,499 - freqtrade.loggers - INFO - Logfile configured
2025-09-25 20:20:15,499 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-25 20:20:15,500 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-25 20:20:15,500 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-25 20:20:15,500 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-25 20:20:15,501 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-25 20:20:15,511 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-25 20:20:15,511 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-25 20:20:15,512 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-25 20:20:15,512 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-25 20:20:15,513 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-25 20:20:15,513 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-25 20:20:15,514 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-25 20:20:15,532 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-25 20:20:15,533 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 20:20:15,537 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-25 20:20:15,538 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-25 20:20:15,538 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-25 20:20:15,570 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-25 20:20:17,958 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-25 20:20:17,998 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-25 20:20:17,999 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-25 20:20:18,000 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-25 20:20:18,000 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-25 20:20:18,001 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-25 20:20:18,001 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-25 20:20:18,002 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-25 20:20:18,002 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-25 20:20:18,002 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-25 20:20:18,003 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-25 20:20:18,003 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-25 20:20:18,003 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-25 20:20:18,004 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-25 20:20:18,004 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-25 20:20:18,004 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-25 20:20:18,005 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-25 20:20:18,005 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-25 20:20:18,005 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-25 20:20:18,006 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-25 20:20:18,006 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-25 20:20:18,006 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-25 20:20:18,007 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-25 20:20:18,007 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-25 20:20:18,007 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-25 20:20:18,008 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-25 20:20:18,008 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-25 20:20:18,009 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-25 20:20:18,009 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-25 20:20:18,009 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-25 20:20:18,010 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-25 20:20:18,010 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 20:20:18,015 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-25 20:20:18,048 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-25 20:20:18,080 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-25 20:20:18,133 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-25 20:20:18,181 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-25 20:20:18,221 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-25 20:20:18,268 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-25 20:20:18,302 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-25 20:20:18,381 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-25 20:20:18,606 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-25 20:20:18,824 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-25 20:20:19,043 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-25 20:20:19,267 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-25 20:20:20,592 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-25 20:20:20,593 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-25 20:20:20,593 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-25 20:20:20,594 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.4
2025-09-25 20:20:20,594 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-25 20:20:20,595 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-25 20:20:20,595 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-25 20:20:20,595 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 20
2025-09-25 20:20:20,595 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 11
2025-09-25 20:20:20,596 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.614
2025-09-25 20:20:20,596 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.127
2025-09-25 20:20:20,596 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.04
2025-09-25 20:20:20,597 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.003
2025-09-25 20:20:20,597 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-25 20:20:20,597 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-25 20:20:20,598 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.409
2025-09-25 20:20:20,598 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.0
2025-09-25 20:20:20,598 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 3
2025-09-25 20:20:20,598 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1
2025-09-25 20:20:20,599 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-09-25 20:20:20,599 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-25 20:20:20,600 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 4
2025-09-25 20:20:20,600 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-25 20:20:20,601 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-25 20:20:20,601 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-09-25 20:20:20,602 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-25 20:20:20,602 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = atr
2025-09-25 20:20:20,603 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-09-25 20:20:20,603 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-25 20:20:20,604 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-25 20:20:20,604 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-25 20:20:20,605 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-25 20:20:20,607 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 20:20:20,617 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-25 20:20:20,640 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 20:20:20,658 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-25 20:20:27,106 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 20:20:27,114 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-25 20:20:27,137 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 20:20:27,154 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-25 20:20:33,574 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 20:20:33,582 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-25 20:20:33,604 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 20:20:33,622 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-25 20:20:40,047 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 20:20:40,054 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-25 20:20:40,075 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 20:20:40,093 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-25 20:20:46,461 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 20:20:46,469 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-25 20:20:46,489 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 20:20:46,508 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-25 20:20:52,963 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-25 20:22:22,978 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-25_20-22-22.meta.json"
Result for strategy IchimokuRebondStrategy
                                                BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │     15 │         5.97 │         481.800 │        48.18 │  7 days, 14:56:00 │    8     0     7  53.3 │
│ BNB/USDT │      8 │         6.77 │         252.040 │         25.2 │ 11 days, 23:50:00 │    5     0     3  62.5 │
│ BTC/USDT │     16 │         2.52 │         128.658 │        12.87 │ 18 days, 12:15:00 │    6     0    10  37.5 │
│ XRP/USDT │      2 │         8.17 │          80.643 │         8.06 │          14:45:00 │    1     0     1  50.0 │
│ LTC/USDT │      9 │        -2.81 │        -112.127 │       -11.21 │   3 days, 7:32:00 │    1     0     8  11.1 │
│    TOTAL │     50 │          3.5 │         831.014 │         83.1 │ 10 days, 18:00:00 │   21     0    29  42.0 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         8.18 │          30.204 │         3.02 │ 31 days, 14:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         8.18 │          30.204 │         3.02 │ 31 days, 14:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                        ENTER TAG STATS                                                         
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │      41 │         3.41 │         588.935 │        58.89 │  9 days, 20:50:00 │   17     0    24  41.5 │
│      engulfing_rebond │       9 │         3.89 │         242.080 │        24.21 │ 14 days, 18:26:00 │    4     0     5  44.4 │
│                 TOTAL │      50 │          3.5 │         831.014 │         83.1 │ 10 days, 18:00:00 │   21     0    29  42.0 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                   EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │    20 │        15.86 │        1620.404 │       162.04 │ 13 days, 18:07:00 │   20     0     0   100 │
│     force_exit │     1 │         8.18 │          30.204 │         3.02 │ 31 days, 14:00:00 │    1     0     0   100 │
│      stop_loss │    29 │        -5.19 │        -819.593 │       -81.96 │  7 days, 23:02:00 │    0     0    29     0 │
│          TOTAL │    50 │          3.5 │         831.014 │         83.1 │ 10 days, 18:00:00 │   21     0    29  42.0 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                                MIXED TAG STATS                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_3R │     16 │        16.02 │        1239.777 │       123.98 │ 12 days, 20:12:00 │   16     0     0   100 │
│      engulfing_rebond │ take_profit_3R │      4 │        15.25 │         380.626 │        38.06 │  17 days, 9:45:00 │    4     0     0   100 │
│ strong_bullish_rebond │     force_exit │      1 │         8.18 │          30.204 │         3.02 │ 31 days, 14:00:00 │    1     0     0   100 │
│      engulfing_rebond │      stop_loss │      5 │        -5.19 │        -138.546 │       -13.85 │ 12 days, 15:47:00 │    0     0     5     0 │
│ strong_bullish_rebond │      stop_loss │     24 │        -5.19 │        -681.047 │        -68.1 │  6 days, 23:32:00 │    0     0    24     0 │
│                 TOTAL │                │     50 │          3.5 │         831.014 │         83.1 │ 10 days, 18:00:00 │   21     0    29  42.0 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                          SUMMARY METRICS                           
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                            ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00              │
│ Backtesting to                │ 2025-09-11 17:00:00              │
│ Trading Mode                  │ Spot                             │
│ Max open trades               │ 3                                │
│                               │                                  │
│ Total/Daily Avg Trades        │ 50 / 0.04                        │
│ Starting balance              │ 1000 USDT                        │
│ Final balance                 │ 1831.014 USDT                    │
│ Absolute profit               │ 831.014 USDT                     │
│ Total profit %                │ 83.10%                           │
│ CAGR %                        │ 17.78%                           │
│ Sortino                       │ 2.21                             │
│ Sharpe                        │ 0.22                             │
│ Calmar                        │ 6.85                             │
│ SQN                           │ 2.14                             │
│ Profit factor                 │ 2.01                             │
│ Expectancy (Ratio)            │ 16.62 (0.59)                     │
│ Avg. daily profit             │ 0.616 USDT                       │
│ Avg. stake amount             │ 527.823 USDT                     │
│ Total trade volume            │ 53720.605 USDT                   │
│                               │                                  │
│ Best Pair                     │ ETH/USDT 48.18%                  │
│ Worst Pair                    │ LTC/USDT -11.21%                 │
│ Best trade                    │ XRP/USDT 21.53%                  │
│ Worst trade                   │ LTC/USDT -5.19%                  │
│ Best day                      │ 106.197 USDT                     │
│ Worst day                     │ -42.35 USDT                      │
│ Days win/draw/lose            │ 21 / 1201 / 28                   │
│ Min/Max/Avg. Duration Winners │ 0d 00:25 / 41d 04:15 / 14d 14:29 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:30 / 45d 15:45 / 7d 23:02  │
│ Max Consecutive Wins / Loss   │ 3 / 8                            │
│ Rejected Entry signals        │ 0                                │
│ Entry/Exit Timeouts           │ 0 / 0                            │
│                               │                                  │
│ Min balance                   │ 979.443 USDT                     │
│ Max balance                   │ 1835.002 USDT                    │
│ Max % of account underwater   │ 17.19%                           │
│ Absolute Drawdown (Account)   │ 17.19%                           │
│ Absolute Drawdown             │ 295.563 USDT                     │
│ Drawdown high                 │ 719.293 USDT                     │
│ Drawdown low                  │ 423.73 USDT                      │
│ Drawdown Start                │ 2024-02-14 09:10:00              │
│ Drawdown End                  │ 2025-01-08 06:30:00              │
│ Market change                 │ 94.84%                           │
└───────────────────────────────┴──────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                    
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     50 │         3.50 │         831.014 │         83.1 │ 10 days, 18:00:00 │   21     0    29  42.0 │ 295.563 USDT  17.19% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-25T22:22:24.091092",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 7165,
  "total_daily_avg_trades": "50 / 0.04",
  "absolute_profit_usdt": 831.014,
  "total_profit_pct": 83.1,
  "cagr_pct": 17.78,
  "sortino": 2.21,
  "sharpe": 0.22,
  "calmar": 6.85,
  "sqn": 2.14,
  "max_consecutive_wins_loss": "3 / 8",
  "min_balance_usdt": 979.443,
  "max_balance_usdt": 1835.002,
  "market_change_pct": 94.84
}
```
