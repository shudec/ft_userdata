# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 5605  
**Timestamp:** 2025-09-24 10:07:35

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 5605,
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
2025-09-24 08:01:40,992 - freqtrade - INFO - freqtrade 2025.8
2025-09-24 08:01:41,656 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-24 08:01:45,070 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-24 08:01:45,078 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-24 08:01:45,078 - freqtrade.loggers - INFO - Logfile configured
2025-09-24 08:01:45,079 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-24 08:01:45,079 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-24 08:01:45,080 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-24 08:01:45,081 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-24 08:01:45,082 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20200101-20251231 ...
2025-09-24 08:01:45,575 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-24 08:01:45,577 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-24 08:01:45,577 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-24 08:01:45,578 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-24 08:01:45,578 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-24 08:01:45,579 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20200101-20251231
2025-09-24 08:01:45,580 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-24 08:01:45,592 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-24 08:01:45,592 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 08:01:45,595 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-24 08:01:45,596 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-24 08:01:45,596 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-24 08:01:45,616 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-24 08:01:50,082 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-24 08:01:50,210 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-24 08:01:50,213 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-24 08:01:50,218 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-24 08:01:50,218 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-24 08:01:50,219 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-24 08:01:50,219 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-24 08:01:50,220 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-24 08:01:50,220 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-24 08:01:50,221 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-24 08:01:50,221 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-24 08:01:50,222 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-24 08:01:50,222 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-24 08:01:50,223 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-24 08:01:50,223 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-24 08:01:50,224 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-24 08:01:50,224 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-24 08:01:50,225 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-24 08:01:50,225 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-24 08:01:50,226 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-24 08:01:50,226 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-24 08:01:50,227 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-24 08:01:50,227 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-24 08:01:50,227 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-24 08:01:50,228 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-24 08:01:50,228 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-24 08:01:50,229 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-24 08:01:50,229 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-24 08:01:50,229 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-24 08:01:50,230 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-24 08:01:50,230 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-24 08:01:50,231 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 08:01:50,258 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-24 08:01:50,283 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-24 08:01:50,356 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 08:01:50,462 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 08:01:50,538 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 08:01:50,610 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 08:01:50,721 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 08:01:50,770 - freqtrade.optimize.backtesting - INFO - Loading data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 08:01:51,081 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 08:01:51,752 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 08:01:52,388 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 08:01:52,971 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 08:01:53,636 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 08:01:55,469 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-24 08:01:55,483 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-24 08:01:55,484 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-24 08:01:55,485 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-24 08:01:55,486 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-24 08:01:55,486 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-24 08:01:55,487 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-24 08:01:55,488 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-24 08:01:55,489 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-24 08:01:55,491 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-24 08:01:55,492 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-24 08:01:55,492 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-24 08:01:55,493 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-09-24 08:01:55,493 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-09-24 08:01:55,494 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-24 08:01:55,495 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-24 08:01:55,495 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-24 08:01:55,496 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-24 08:01:55,497 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-24 08:01:55,497 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 8
2025-09-24 08:01:55,498 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-24 08:01:55,498 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-24 08:01:55,499 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-24 08:01:55,500 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-24 08:01:55,501 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-24 08:01:55,502 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-24 08:01:55,507 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:01:55,532 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 08:01:55,555 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:01:55,579 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 08:02:12,562 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:02:12,581 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 08:02:12,603 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:02:12,629 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 08:02:29,184 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:02:29,204 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 08:02:29,224 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:02:29,250 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-15 00:00:00
2025-09-24 08:02:46,328 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:02:46,347 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 08:02:46,365 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:02:46,388 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 08:03:04,402 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:03:04,423 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 08:03:04,442 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:03:04,469 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 08:03:25,824 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 08:07:33,502 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-24_08-07-33.meta.json"
Result for strategy IchimokuRebondStrategy
                                              BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │    216 │         0.14 │         101.492 │        10.15 │ 1 day, 0:55:00 │  109     0   107  50.5 │
│ ETH/USDT │    188 │        -0.02 │          -6.622 │        -0.66 │       20:59:00 │   95     0    93  50.5 │
│ LTC/USDT │    135 │        -0.07 │         -28.212 │        -2.82 │ 1 day, 0:48:00 │   64     0    71  47.4 │
│ BNB/USDT │    202 │        -0.02 │         -60.075 │        -6.01 │       19:48:00 │  104     0    98  51.5 │
│ XRP/USDT │    133 │        -0.24 │         -94.506 │        -9.45 │       19:59:00 │   62     0    71  46.6 │
│    TOTAL │    874 │        -0.02 │         -87.922 │        -8.79 │       22:07:00 │  434     0   440  49.7 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                            LEFT OPEN TRADES REPORT                                            
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         0.07 │           0.325 │         0.03 │ 1 day, 1:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         0.07 │           0.325 │         0.03 │ 1 day, 1:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                       ENTER TAG STATS                                                       
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│         hammer_rebond │     146 │         0.19 │         104.128 │        10.41 │ 1 day, 5:17:00 │   71     0    75  48.6 │
│      engulfing_rebond │      91 │         0.04 │          51.963 │          5.2 │       19:12:00 │   51     0    40  56.0 │
│ strong_bullish_rebond │     637 │        -0.08 │        -244.013 │        -24.4 │       20:54:00 │  312     0   325  49.0 │
│                 TOTAL │     874 │        -0.02 │         -87.922 │        -8.79 │       22:07:00 │  434     0   440  49.7 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│    exit_signal │   829 │         0.12 │         414.528 │        41.45 │       22:26:00 │  428     0   401  51.6 │
│ take_profit_3R │     5 │         16.5 │         231.914 │        23.19 │ 1 day, 9:17:00 │    5     0     0   100 │
│     force_exit │     1 │         0.07 │           0.325 │         0.03 │ 1 day, 1:00:00 │    1     0     0   100 │
│      stop_loss │    39 │        -5.26 │        -734.690 │       -73.47 │       13:57:00 │    0     0    39     0 │
│          TOTAL │   874 │        -0.02 │         -87.922 │        -8.79 │       22:07:00 │  434     0   440  49.7 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                               MIXED TAG STATS                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│         hammer_rebond │    exit_signal │    137 │         0.61 │         290.452 │        29.05 │  1 day, 6:14:00 │   71     0    66  51.8 │
│ strong_bullish_rebond │ take_profit_3R │      4 │        18.17 │         183.200 │        18.32 │ 1 day, 16:05:00 │    4     0     0   100 │
│ strong_bullish_rebond │    exit_signal │    605 │         0.01 │          67.574 │         6.76 │        21:02:00 │  307     0   298  50.7 │
│      engulfing_rebond │    exit_signal │     87 │         0.13 │          56.502 │         5.65 │        19:56:00 │   50     0    37  57.5 │
│      engulfing_rebond │ take_profit_3R │      1 │         9.82 │          48.714 │         4.87 │         6:05:00 │    1     0     0   100 │
│ strong_bullish_rebond │     force_exit │      1 │         0.07 │           0.325 │         0.03 │  1 day, 1:00:00 │    1     0     0   100 │
│      engulfing_rebond │      stop_loss │      3 │        -5.76 │         -53.253 │        -5.33 │         2:17:00 │    0     0     3     0 │
│         hammer_rebond │      stop_loss │      9 │        -6.16 │        -186.324 │       -18.63 │        15:01:00 │    0     0     9     0 │
│ strong_bullish_rebond │      stop_loss │     27 │        -4.91 │        -495.112 │       -49.51 │        14:54:00 │    0     0    27     0 │
│                 TOTAL │                │    874 │        -0.02 │         -87.922 │        -8.79 │        22:07:00 │  434     0   440  49.7 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2020-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 874 / 0.42                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 912.078 USDT                   │
│ Absolute profit               │ -87.922 USDT                   │
│ Total profit %                │ -8.79%                         │
│ CAGR %                        │ -1.60%                         │
│ Sortino                       │ -0.15                          │
│ Sharpe                        │ -0.07                          │
│ Calmar                        │ -0.22                          │
│ SQN                           │ -0.27                          │
│ Profit factor                 │ 0.98                           │
│ Expectancy (Ratio)            │ -0.10 (-0.01)                  │
│ Avg. daily profit             │ -0.042 USDT                    │
│ Avg. stake amount             │ 343.669 USDT                   │
│ Total trade volume            │ 601847.772 USDT                │
│                               │                                │
│ Best Pair                     │ BTC/USDT 10.15%                │
│ Worst Pair                    │ XRP/USDT -9.45%                │
│ Best trade                    │ XRP/USDT 29.46%                │
│ Worst trade                   │ XRP/USDT -12.68%               │
│ Best day                      │ 104.941 USDT                   │
│ Worst day                     │ -49.321 USDT                   │
│ Days win/draw/lose            │ 288 / 1437 / 317               │
│ Min/Max/Avg. Duration Winners │ 0d 02:00 / 5d 22:00 / 0d 19:37 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:30 / 3d 11:00 / 1d 00:36 │
│ Max Consecutive Wins / Loss   │ 11 / 12                        │
│ Rejected Entry signals        │ 396                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 780.802 USDT                   │
│ Max balance                   │ 1238.214 USDT                  │
│ Max % of account underwater   │ 36.94%                         │
│ Absolute drawdown             │ 457.412 USDT (36.94%)          │
│ Drawdown duration             │ 888 days 15:00:00              │
│ Profit at drawdown start      │ 238.214 USDT                   │
│ Profit at drawdown end        │ -219.198 USDT                  │
│ Drawdown start                │ 2021-05-03 19:00:00            │
│ Drawdown end                  │ 2023-10-09 10:00:00            │
│ Market change                 │ 2537.81%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2020-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    874 │        -0.02 │         -87.922 │        -8.79 │     22:07:00 │  434     0   440  49.7 │ 457.412 USDT  36.94% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-24T10:07:35.330566",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 5605,
  "total_daily_avg_trades": "874 / 0.42",
  "absolute_profit_usdt": -87.922,
  "total_profit_pct": -8.79,
  "cagr_pct": -1.6,
  "sortino": -0.15,
  "sharpe": -0.07,
  "calmar": -0.22,
  "sqn": -0.27,
  "max_consecutive_wins_loss": "11 / 12",
  "min_balance_usdt": 780.802,
  "max_balance_usdt": 1238.214,
  "absolute_drawdown_pct": 36.94,
  "market_change_pct": 2537.81,
  "win_draw_loss_winpct": "434 0 440 49.7"
}
```
