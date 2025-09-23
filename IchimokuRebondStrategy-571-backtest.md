# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 571  
**Timestamp:** 2025-09-23 09:12:42

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 571,
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
2025-09-23 07:07:15,217 - freqtrade - INFO - freqtrade 2025.8
2025-09-23 07:07:15,679 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-23 07:07:17,521 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-23 07:07:17,535 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-23 07:07:17,536 - freqtrade.loggers - INFO - Logfile configured
2025-09-23 07:07:17,536 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-23 07:07:17,537 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-23 07:07:17,537 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-23 07:07:17,538 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-23 07:07:17,538 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20251231 ...
2025-09-23 07:07:17,986 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-23 07:07:17,989 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-23 07:07:17,989 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-23 07:07:17,990 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-23 07:07:17,990 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-23 07:07:17,991 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20251231
2025-09-23 07:07:17,992 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-23 07:07:18,006 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-23 07:07:18,007 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 07:07:18,010 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-23 07:07:18,012 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-23 07:07:18,012 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-23 07:07:18,039 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-23 07:07:20,873 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-23 07:07:21,009 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-23 07:07:21,011 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-23 07:07:21,016 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-23 07:07:21,017 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-23 07:07:21,017 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-23 07:07:21,018 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-23 07:07:21,018 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-23 07:07:21,019 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-23 07:07:21,020 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-23 07:07:21,020 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-23 07:07:21,020 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-23 07:07:21,021 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-23 07:07:21,021 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-23 07:07:21,021 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-23 07:07:21,022 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-23 07:07:21,022 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-23 07:07:21,022 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-23 07:07:21,023 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-23 07:07:21,023 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-23 07:07:21,023 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-23 07:07:21,024 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-23 07:07:21,024 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-23 07:07:21,025 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-23 07:07:21,026 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-23 07:07:21,026 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-23 07:07:21,027 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-23 07:07:21,027 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-23 07:07:21,027 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-23 07:07:21,028 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-23 07:07:21,028 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-23 07:07:21,029 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 07:07:21,054 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-23 07:07:21,085 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-23 07:07:21,172 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:07:21,273 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:07:21,365 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:07:21,449 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-23 07:07:21,450 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:07:21,533 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:07:21,582 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 07:07:21,998 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:07:22,751 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:07:23,423 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:07:24,068 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-23 07:07:24,069 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:07:24,724 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:07:27,272 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-23 07:07:27,279 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-23 07:07:27,279 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-23 07:07:27,280 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.498
2025-09-23 07:07:27,281 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-23 07:07:27,282 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-23 07:07:27,282 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2
2025-09-23 07:07:27,283 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 17
2025-09-23 07:07:27,283 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.557
2025-09-23 07:07:27,284 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.695
2025-09-23 07:07:27,284 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.007
2025-09-23 07:07:27,285 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-23 07:07:27,285 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-23 07:07:27,286 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss = True
2025-09-23 07:07:27,287 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 2
2025-09-23 07:07:27,288 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-23 07:07:27,288 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 9
2025-09-23 07:07:27,289 - freqtrade.strategy.hyper - INFO - Strategy Parameter: previous_low_stoploss = False
2025-09-23 07:07:27,289 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-23 07:07:27,290 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-23 07:07:27,290 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-23 07:07:27,291 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-23 07:07:27,291 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-23 07:07:27,295 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:07:27,318 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:07:50,809 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:07:50,828 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:08:13,911 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:08:13,934 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:08:39,733 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:08:39,751 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-23 07:08:39,752 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:09:01,332 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:09:01,351 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:09:24,339 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 07:12:40,985 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-23_07-12-40.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │    145 │        -0.23 │          44.983 │          4.5 │     16:30:00 │   53     0    92  36.6 │
│ BTC/USDT │    204 │        -0.17 │         -93.624 │        -9.36 │     18:11:00 │   76     0   128  37.3 │
│ XRP/USDT │    116 │        -0.07 │        -116.723 │       -11.67 │     13:33:00 │   44     0    72  37.9 │
│ BNB/USDT │    148 │        -0.09 │        -135.143 │       -13.51 │     18:23:00 │   54     0    94  36.5 │
│ LTC/USDT │    126 │        -0.41 │        -321.780 │       -32.18 │     16:23:00 │   42     0    84  33.3 │
│    TOTAL │    739 │        -0.19 │        -622.287 │       -62.23 │     16:51:00 │  269     0   470  36.4 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                           LEFT OPEN TRADES REPORT                                           
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         0.04 │           0.146 │         0.01 │      2:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         0.04 │           0.146 │         0.01 │      2:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                   ENTER TAG STATS                                                    
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│    hammer_rebond │     133 │        -0.15 │          46.392 │         4.64 │     23:18:00 │   51     0    82  38.3 │
│ engulfing_rebond │     606 │         -0.2 │        -668.679 │       -66.87 │     15:27:00 │  218     0   388  36.0 │
│            TOTAL │     739 │        -0.19 │        -622.287 │       -62.23 │     16:51:00 │  269     0   470  36.4 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │   268 │         3.32 │        4708.264 │       470.83 │     18:26:00 │  268     0     0   100 │
│       force_exit │     1 │         0.04 │           0.146 │         0.01 │      2:00:00 │    1     0     0   100 │
│        stop_loss │   470 │        -2.19 │       -5330.697 │      -533.07 │     16:00:00 │    0     0   470     0 │
│            TOTAL │   739 │        -0.19 │        -622.287 │       -62.23 │     16:51:00 │  269     0   470  36.4 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                             MIXED TAG STATS                                                              
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │ take_profit_1.5R │    217 │         3.12 │        3309.568 │       330.96 │       15:50:00 │  217     0     0   100 │
│    hammer_rebond │ take_profit_1.5R │     51 │         4.16 │        1398.696 │       139.87 │ 1 day, 5:27:00 │   51     0     0   100 │
│ engulfing_rebond │       force_exit │      1 │         0.04 │           0.146 │         0.01 │        2:00:00 │    1     0     0   100 │
│    hammer_rebond │        stop_loss │     82 │        -2.84 │       -1352.304 │      -135.23 │       19:28:00 │    0     0    82     0 │
│ engulfing_rebond │        stop_loss │    388 │        -2.05 │       -3978.393 │      -397.84 │       15:16:00 │    0     0   388     0 │
│            TOTAL │                  │    739 │        -0.19 │        -622.287 │       -62.23 │       16:51:00 │  269     0   470  36.4 │
└──────────────────┴──────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2018-01-01 00:00:00             │
│ Backtesting to                │ 2025-09-10 08:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 739 / 0.26                      │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 377.713 USDT                    │
│ Absolute profit               │ -622.287 USDT                   │
│ Total profit %                │ -62.23%                         │
│ CAGR %                        │ -11.88%                         │
│ Sortino                       │ -0.56                           │
│ Sharpe                        │ -0.25                           │
│ Calmar                        │ -0.59                           │
│ SQN                           │ -1.37                           │
│ Profit factor                 │ 0.88                            │
│ Expectancy (Ratio)            │ -0.84 (-0.07)                   │
│ Avg. daily profit             │ -0.222 USDT                     │
│ Avg. stake amount             │ 547.005 USDT                    │
│ Total trade volume            │ 809468.496 USDT                 │
│                               │                                 │
│ Best Pair                     │ ETH/USDT 4.50%                  │
│ Worst Pair                    │ LTC/USDT -32.18%                │
│ Best trade                    │ ETH/USDT 12.52%                 │
│ Worst trade                   │ XRP/USDT -9.00%                 │
│ Best day                      │ 75.028 USDT                     │
│ Worst day                     │ -62.695 USDT                    │
│ Days win/draw/lose            │ 236 / 2160 / 394                │
│ Min/Max/Avg. Duration Winners │ 0d 00:10 / 11d 01:35 / 0d 18:22 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 7d 13:30 / 0d 16:00  │
│ Max Consecutive Wins / Loss   │ 8 / 16                          │
│ Rejected Entry signals        │ 12                              │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 365.04 USDT                     │
│ Max balance                   │ 1311.097 USDT                   │
│ Max % of account underwater   │ 72.16%                          │
│ Absolute drawdown             │ 946.057 USDT (72.16%)           │
│ Drawdown duration             │ 2068 days 10:20:00              │
│ Profit at drawdown start      │ 311.097 USDT                    │
│ Profit at drawdown end        │ -634.96 USDT                    │
│ Drawdown start                │ 2019-09-03 11:25:00             │
│ Drawdown end                  │ 2025-05-02 21:45:00             │
│ Market change                 │ 2372.94%                        │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    739 │        -0.19 │        -622.287 │       -62.23 │     16:51:00 │  269     0   470  36.4 │ 946.057 USDT  72.16% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-23T09:12:42.724225",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 571,
  "total_daily_avg_trades": "739 / 0.26",
  "absolute_profit_usdt": -622.287,
  "total_profit_pct": -62.23,
  "cagr_pct": -11.88,
  "sortino": -0.56,
  "sharpe": -0.25,
  "calmar": -0.59,
  "sqn": -1.37,
  "max_consecutive_wins_loss": "8 / 16",
  "min_balance_usdt": 365.04,
  "max_balance_usdt": 1311.097,
  "absolute_drawdown_pct": 72.16,
  "market_change_pct": 2372.94,
  "win_draw_loss_winpct": "269 0 470 36.4"
}
```
