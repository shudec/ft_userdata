# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 8748  
**Timestamp:** 2025-09-23 18:06:30

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 8748,
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
2025-09-23 16:01:05,859 - freqtrade - INFO - freqtrade 2025.8
2025-09-23 16:01:06,409 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-23 16:01:09,427 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-23 16:01:09,439 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-23 16:01:09,440 - freqtrade.loggers - INFO - Logfile configured
2025-09-23 16:01:09,440 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-23 16:01:09,442 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-23 16:01:09,443 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-23 16:01:09,444 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-23 16:01:09,444 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20251231 ...
2025-09-23 16:01:09,955 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-23 16:01:09,959 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-23 16:01:09,960 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-23 16:01:09,961 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-23 16:01:09,962 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-23 16:01:09,963 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20251231
2025-09-23 16:01:09,967 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-23 16:01:09,990 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-23 16:01:09,991 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 16:01:09,997 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-23 16:01:09,999 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-23 16:01:10,001 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-23 16:01:10,040 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-23 16:01:12,505 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-23 16:01:12,624 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-23 16:01:12,627 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-23 16:01:12,631 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-23 16:01:12,631 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-23 16:01:12,631 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-23 16:01:12,632 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-23 16:01:12,632 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-23 16:01:12,633 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-23 16:01:12,633 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-23 16:01:12,634 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-23 16:01:12,634 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-23 16:01:12,635 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-23 16:01:12,635 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-23 16:01:12,636 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-23 16:01:12,636 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-23 16:01:12,637 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-23 16:01:12,637 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-23 16:01:12,638 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-23 16:01:12,638 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-23 16:01:12,639 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-23 16:01:12,639 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-23 16:01:12,640 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-23 16:01:12,640 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-23 16:01:12,640 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-23 16:01:12,641 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-23 16:01:12,641 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-23 16:01:12,641 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-23 16:01:12,642 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-23 16:01:12,642 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-23 16:01:12,642 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-23 16:01:12,643 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 16:01:12,668 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-23 16:01:12,694 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-23 16:01:12,759 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 16:01:12,851 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 16:01:12,926 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 16:01:12,997 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-23 16:01:12,998 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 16:01:13,062 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 16:01:13,098 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 16:01:13,340 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 16:01:13,990 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 16:01:14,597 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 16:01:15,260 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-23 16:01:15,261 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 16:01:15,801 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 16:01:18,620 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-23 16:01:18,628 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-23 16:01:18,628 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-23 16:01:18,629 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-23 16:01:18,630 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-23 16:01:18,630 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-23 16:01:18,631 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-23 16:01:18,631 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-23 16:01:18,632 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-23 16:01:18,632 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-23 16:01:18,633 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-23 16:01:18,633 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-23 16:01:18,634 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-23 16:01:18,635 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-23 16:01:18,635 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-23 16:01:18,636 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-23 16:01:18,637 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-23 16:01:18,637 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 1
2025-09-23 16:01:18,637 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-23 16:01:18,638 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-23 16:01:18,638 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-23 16:01:18,639 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower
2025-09-23 16:01:18,639 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-23 16:01:18,640 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-23 16:01:18,646 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:01:18,673 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 16:01:33,847 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:01:33,870 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 16:01:48,603 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:01:48,626 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 16:02:01,842 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:02:01,860 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-23 16:02:01,860 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 16:02:15,108 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:02:15,142 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 16:02:30,053 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 16:06:28,356 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-23_16-06-28.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │    279 │         0.45 │         355.257 │        35.53 │     17:31:00 │   95     0   184  34.1 │
│ XRP/USDT │    182 │         0.37 │         169.729 │        16.97 │     13:38:00 │   63     0   119  34.6 │
│ BTC/USDT │    331 │         0.18 │         131.272 │        13.13 │     17:14:00 │  104     0   227  31.4 │
│ BNB/USDT │    267 │         0.01 │         -32.820 │        -3.28 │     15:35:00 │   79     0   188  29.6 │
│ LTC/USDT │    135 │        -0.21 │        -109.723 │       -10.97 │     14:15:00 │   36     0    99  26.7 │
│    TOTAL │   1194 │         0.19 │         513.715 │        51.37 │     16:02:00 │  377     0   817  31.6 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                           LEFT OPEN TRADES REPORT                                           
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         0.05 │           0.145 │         0.01 │      5:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         0.05 │           0.145 │         0.01 │      5:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                      ENTER TAG STATS                                                      
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │     918 │         0.19 │         395.269 │        39.53 │     16:38:00 │  298     0   620  32.5 │
│         hammer_rebond │     151 │         0.29 │          90.245 │         9.02 │     13:01:00 │   41     0   110  27.2 │
│      engulfing_rebond │     125 │         0.11 │          28.201 │         2.82 │     15:23:00 │   38     0    87  30.4 │
│                 TOTAL │    1194 │         0.19 │         513.715 │        51.37 │     16:02:00 │  377     0   817  31.6 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │    89 │        10.41 │        2469.591 │       246.96 │ 1 day, 0:43:00 │   89     0     0   100 │
│     force_exit │     1 │         0.05 │           0.145 │         0.01 │        5:00:00 │    1     0     0   100 │
│      stop_loss │     2 │       -10.18 │         -59.665 │        -5.97 │        2:10:00 │    0     0     2     0 │
│    exit_signal │  1102 │        -0.61 │       -1896.355 │      -189.64 │       15:23:00 │  287     0   815  26.0 │
│          TOTAL │  1194 │         0.19 │         513.715 │        51.37 │       16:02:00 │  377     0   817  31.6 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                               MIXED TAG STATS                                                               
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_1R │     67 │        10.41 │        1865.993 │        186.6 │ 1 day, 0:14:00 │   67     0     0   100 │
│         hammer_rebond │ take_profit_1R │     13 │        10.29 │         353.105 │        35.31 │ 1 day, 7:27:00 │   13     0     0   100 │
│      engulfing_rebond │ take_profit_1R │      9 │        10.51 │         250.493 │        25.05 │       18:35:00 │    9     0     0   100 │
│ strong_bullish_rebond │     force_exit │      1 │         0.05 │           0.145 │         0.01 │        5:00:00 │    1     0     0   100 │
│ strong_bullish_rebond │      stop_loss │      2 │       -10.18 │         -59.665 │        -5.97 │        2:10:00 │    0     0     2     0 │
│      engulfing_rebond │    exit_signal │    116 │         -0.7 │        -222.292 │       -22.23 │       15:08:00 │   29     0    87  25.0 │
│         hammer_rebond │    exit_signal │    138 │        -0.65 │        -262.860 │       -26.29 │       11:17:00 │   28     0   110  20.3 │
│ strong_bullish_rebond │    exit_signal │    848 │         -0.6 │       -1411.204 │      -141.12 │       16:04:00 │  230     0   618  27.1 │
│                 TOTAL │                │   1194 │         0.19 │         513.715 │        51.37 │       16:02:00 │  377     0   817  31.6 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2018-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 1194 / 0.43                    │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1513.715 USDT                  │
│ Absolute profit               │ 513.715 USDT                   │
│ Total profit %                │ 51.37%                         │
│ CAGR %                        │ 5.53%                          │
│ Sortino                       │ 0.99                           │
│ Sharpe                        │ 0.36                           │
│ Calmar                        │ 2.56                           │
│ SQN                           │ 1.55                           │
│ Profit factor                 │ 1.15                           │
│ Expectancy (Ratio)            │ 0.43 (0.10)                    │
│ Avg. daily profit             │ 0.183 USDT                     │
│ Avg. stake amount             │ 279.518 USDT                   │
│ Total trade volume            │ 669340.039 USDT                │
│                               │                                │
│ Best Pair                     │ ETH/USDT 35.53%                │
│ Worst Pair                    │ LTC/USDT -10.97%               │
│ Best trade                    │ XRP/USDT 12.32%                │
│ Worst trade                   │ LTC/USDT -10.18%               │
│ Best day                      │ 87.381 USDT                    │
│ Worst day                     │ -36.12 USDT                    │
│ Days win/draw/lose            │ 234 / 1872 / 489               │
│ Min/Max/Avg. Duration Winners │ 0d 00:20 / 3d 05:35 / 1d 04:37 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 1d 22:00 / 0d 10:14 │
│ Max Consecutive Wins / Loss   │ 6 / 17                         │
│ Rejected Entry signals        │ 576                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 997.173 USDT                   │
│ Max balance                   │ 1620.237 USDT                  │
│ Max % of account underwater   │ 13.65%                         │
│ Absolute drawdown             │ 221.152 USDT (13.65%)          │
│ Drawdown duration             │ 244 days 10:00:00              │
│ Profit at drawdown start      │ 620.237 USDT                   │
│ Profit at drawdown end        │ 399.085 USDT                   │
│ Drawdown start                │ 2024-02-28 19:00:00            │
│ Drawdown end                  │ 2024-10-30 05:00:00            │
│ Market change                 │ 2372.94%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │   1194 │         0.19 │         513.715 │        51.37 │     16:02:00 │  377     0   817  31.6 │ 221.152 USDT  13.65% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-23T18:06:30.143247",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 8748,
  "total_daily_avg_trades": "1194 / 0.43",
  "absolute_profit_usdt": 513.715,
  "total_profit_pct": 51.37,
  "cagr_pct": 5.53,
  "sortino": 0.99,
  "sharpe": 0.36,
  "calmar": 2.56,
  "sqn": 1.55,
  "max_consecutive_wins_loss": "6 / 17",
  "min_balance_usdt": 997.173,
  "max_balance_usdt": 1620.237,
  "absolute_drawdown_pct": 13.65,
  "market_change_pct": 2372.94,
  "win_draw_loss_winpct": "377 0 817 31.6"
}
```
