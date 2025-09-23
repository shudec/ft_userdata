# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 2245  
**Timestamp:** 2025-09-23 09:58:45

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 2245,
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
2025-09-23 07:54:35,642 - freqtrade - INFO - freqtrade 2025.8
2025-09-23 07:54:36,017 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-23 07:54:37,802 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-23 07:54:37,808 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-23 07:54:37,809 - freqtrade.loggers - INFO - Logfile configured
2025-09-23 07:54:37,809 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-23 07:54:37,810 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-23 07:54:37,810 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-23 07:54:37,811 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-23 07:54:37,811 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20251231 ...
2025-09-23 07:54:38,172 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-23 07:54:38,174 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-23 07:54:38,175 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-23 07:54:38,175 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-23 07:54:38,176 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-23 07:54:38,176 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20251231
2025-09-23 07:54:38,177 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-23 07:54:38,188 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-23 07:54:38,189 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 07:54:38,191 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-23 07:54:38,192 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-23 07:54:38,192 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-23 07:54:38,213 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-23 07:54:40,402 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-23 07:54:40,492 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-23 07:54:40,494 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-23 07:54:40,499 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-23 07:54:40,499 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-23 07:54:40,500 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-23 07:54:40,501 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-23 07:54:40,501 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-23 07:54:40,502 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-23 07:54:40,502 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-23 07:54:40,503 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-23 07:54:40,503 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-23 07:54:40,504 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-23 07:54:40,504 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-23 07:54:40,504 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-23 07:54:40,505 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-23 07:54:40,505 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-23 07:54:40,506 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-23 07:54:40,506 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-23 07:54:40,506 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-23 07:54:40,507 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-23 07:54:40,507 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-23 07:54:40,507 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-23 07:54:40,508 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-23 07:54:40,508 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-23 07:54:40,508 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-23 07:54:40,509 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-23 07:54:40,509 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-23 07:54:40,509 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-23 07:54:40,510 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-23 07:54:40,510 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-23 07:54:40,511 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 07:54:40,527 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-23 07:54:40,553 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-23 07:54:40,607 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:54:40,685 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:54:40,764 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:54:40,853 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-23 07:54:40,854 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:54:40,942 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:54:40,986 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 07:54:41,248 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:54:41,886 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:54:42,600 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:54:43,327 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-23 07:54:43,328 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:54:44,080 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:54:47,497 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-23 07:54:47,503 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-23 07:54:47,504 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-23 07:54:47,505 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.5
2025-09-23 07:54:47,506 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-23 07:54:47,507 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = True
2025-09-23 07:54:47,508 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2
2025-09-23 07:54:47,508 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 17
2025-09-23 07:54:47,509 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.557
2025-09-23 07:54:47,509 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.695
2025-09-23 07:54:47,510 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.007
2025-09-23 07:54:47,510 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-23 07:54:47,511 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-23 07:54:47,512 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 2
2025-09-23 07:54:47,513 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-23 07:54:47,513 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 3
2025-09-23 07:54:47,514 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 1.0
2025-09-23 07:54:47,514 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-23 07:54:47,515 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-23 07:54:47,515 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower
2025-09-23 07:54:47,516 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-23 07:54:47,517 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-23 07:54:47,522 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:54:47,545 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:55:09,094 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:55:09,113 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:55:33,746 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:55:33,763 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:55:54,561 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:55:54,577 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-23 07:55:54,578 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:56:14,478 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:56:14,496 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:56:36,345 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 07:58:43,371 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-23_07-58-43.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │    171 │        -0.08 │         -56.885 │        -5.69 │     12:30:00 │   54     0   117  31.6 │
│ XRP/USDT │    106 │         0.21 │         -88.265 │        -8.83 │     11:05:00 │   36     0    70  34.0 │
│ LTC/USDT │    104 │        -0.23 │        -117.505 │       -11.75 │     12:39:00 │   28     0    76  26.9 │
│ BNB/USDT │    122 │        -0.22 │        -209.881 │       -20.99 │     14:51:00 │   36     0    86  29.5 │
│ ETH/USDT │    116 │        -0.32 │        -248.492 │       -24.85 │      8:55:00 │   35     0    81  30.2 │
│    TOTAL │    619 │        -0.13 │        -721.028 │        -72.1 │     12:05:00 │  189     0   430  30.5 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                           LEFT OPEN TRADES REPORT                                           
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         0.04 │           0.108 │         0.01 │      2:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         0.04 │           0.108 │         0.01 │      2:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                   ENTER TAG STATS                                                    
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│    hammer_rebond │      63 │         0.33 │          37.983 │          3.8 │     11:32:00 │   21     0    42  33.3 │
│ engulfing_rebond │     556 │        -0.18 │        -759.012 │        -75.9 │     12:08:00 │  168     0   388  30.2 │
│            TOTAL │     619 │        -0.13 │        -721.028 │        -72.1 │     12:05:00 │  189     0   430  30.5 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │   188 │          3.3 │        3086.173 │       308.62 │     16:03:00 │  188     0     0   100 │
│     force_exit │     1 │         0.04 │           0.108 │         0.01 │      2:00:00 │    1     0     0   100 │
│      stop_loss │   430 │        -1.63 │       -3807.310 │      -380.73 │     10:22:00 │    0     0   430     0 │
│          TOTAL │   619 │        -0.13 │        -721.028 │        -72.1 │     12:05:00 │  189     0   430  30.5 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                           MIXED TAG STATS                                                            
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │ take_profit_2R │    167 │         3.18 │        2679.337 │       267.93 │     16:48:00 │  167     0     0   100 │
│    hammer_rebond │ take_profit_2R │     21 │         4.28 │         406.836 │        40.68 │     10:06:00 │   21     0     0   100 │
│ engulfing_rebond │     force_exit │      1 │         0.04 │           0.108 │         0.01 │      2:00:00 │    1     0     0   100 │
│    hammer_rebond │      stop_loss │     42 │        -1.65 │        -368.853 │       -36.89 │     12:14:00 │    0     0    42     0 │
│ engulfing_rebond │      stop_loss │    388 │        -1.63 │       -3438.457 │      -343.85 │     10:09:00 │    0     0   388     0 │
│            TOTAL │                │    619 │        -0.13 │        -721.028 │        -72.1 │     12:05:00 │  189     0   430  30.5 │
└──────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2018-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 619 / 0.22                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 278.972 USDT                   │
│ Absolute profit               │ -721.028 USDT                  │
│ Total profit %                │ -72.10%                        │
│ CAGR %                        │ -15.29%                        │
│ Sortino                       │ -0.81                          │
│ Sharpe                        │ -0.34                          │
│ Calmar                        │ -0.63                          │
│ SQN                           │ -2.02                          │
│ Profit factor                 │ 0.81                           │
│ Expectancy (Ratio)            │ -1.16 (-0.13)                  │
│ Avg. daily profit             │ -0.257 USDT                    │
│ Avg. stake amount             │ 566.173 USDT                   │
│ Total trade volume            │ 701602.928 USDT                │
│                               │                                │
│ Best Pair                     │ BTC/USDT -5.69%                │
│ Worst Pair                    │ ETH/USDT -24.85%               │
│ Best trade                    │ LTC/USDT 20.60%                │
│ Worst trade                   │ BNB/USDT -10.18%               │
│ Best day                      │ 76.709 USDT                    │
│ Worst day                     │ -29.742 USDT                   │
│ Days win/draw/lose            │ 158 / 2258 / 366               │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 7d 23:10 / 0d 15:59 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 9d 03:50 / 0d 10:22 │
│ Max Consecutive Wins / Loss   │ 3 / 19                         │
│ Rejected Entry signals        │ 12                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 260.563 USDT                   │
│ Max balance                   │ 1166.766 USDT                  │
│ Max % of account underwater   │ 77.67%                         │
│ Absolute drawdown             │ 906.203 USDT (77.67%)          │
│ Drawdown duration             │ 2108 days 08:35:00             │
│ Profit at drawdown start      │ 166.766 USDT                   │
│ Profit at drawdown end        │ -739.437 USDT                  │
│ Drawdown start                │ 2019-09-03 11:25:00            │
│ Drawdown end                  │ 2025-06-11 20:00:00            │
│ Market change                 │ 2372.94%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    619 │        -0.13 │        -721.028 │        -72.1 │     12:05:00 │  189     0   430  30.5 │ 906.203 USDT  77.67% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-23T09:58:45.102746",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 2245,
  "total_daily_avg_trades": "619 / 0.22",
  "absolute_profit_usdt": -721.028,
  "total_profit_pct": -72.1,
  "cagr_pct": -15.29,
  "sortino": -0.81,
  "sharpe": -0.34,
  "calmar": -0.63,
  "sqn": -2.02,
  "max_consecutive_wins_loss": "3 / 19",
  "min_balance_usdt": 260.563,
  "max_balance_usdt": 1166.766,
  "absolute_drawdown_pct": 77.67,
  "market_change_pct": 2372.94,
  "win_draw_loss_winpct": "189 0 430 30.5"
}
```
