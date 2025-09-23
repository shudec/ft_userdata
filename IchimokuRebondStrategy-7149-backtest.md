# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 7149  
**Timestamp:** 2025-09-23 18:43:34

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 7149,
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
2025-09-23 16:38:40,828 - freqtrade - INFO - freqtrade 2025.8
2025-09-23 16:38:41,134 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-23 16:38:42,514 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-23 16:38:42,520 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-23 16:38:42,520 - freqtrade.loggers - INFO - Logfile configured
2025-09-23 16:38:42,521 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-23 16:38:42,521 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-23 16:38:42,522 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-23 16:38:42,522 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-23 16:38:42,522 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20251231 ...
2025-09-23 16:38:42,918 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-23 16:38:42,920 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-23 16:38:42,921 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-23 16:38:42,921 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-23 16:38:42,921 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-23 16:38:42,922 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20251231
2025-09-23 16:38:42,923 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-23 16:38:42,935 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-23 16:38:42,935 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 16:38:42,938 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-23 16:38:42,939 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-23 16:38:42,939 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-23 16:38:42,960 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-23 16:38:45,571 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-23 16:38:45,673 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-23 16:38:45,675 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-23 16:38:45,680 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-23 16:38:45,680 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-23 16:38:45,681 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-23 16:38:45,681 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-23 16:38:45,682 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-23 16:38:45,682 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-23 16:38:45,683 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-23 16:38:45,683 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-23 16:38:45,684 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-23 16:38:45,684 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-23 16:38:45,685 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-23 16:38:45,686 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-23 16:38:45,686 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-23 16:38:45,687 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-23 16:38:45,687 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-23 16:38:45,688 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-23 16:38:45,689 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-23 16:38:45,689 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-23 16:38:45,690 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-23 16:38:45,690 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-23 16:38:45,690 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-23 16:38:45,691 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-23 16:38:45,691 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-23 16:38:45,691 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-23 16:38:45,692 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-23 16:38:45,692 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-23 16:38:45,693 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-23 16:38:45,693 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-23 16:38:45,693 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 16:38:45,713 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-23 16:38:45,742 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-23 16:38:45,803 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 16:38:45,903 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 16:38:45,982 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 16:38:46,061 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-23 16:38:46,061 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 16:38:46,146 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 16:38:46,190 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 16:38:46,524 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 16:38:47,359 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 16:38:47,974 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 16:38:48,589 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-23 16:38:48,590 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 16:38:49,146 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 16:38:51,747 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-23 16:38:51,751 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-23 16:38:51,752 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-23 16:38:51,752 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-23 16:38:51,753 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-23 16:38:51,753 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-23 16:38:51,753 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-23 16:38:51,754 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-23 16:38:51,754 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-23 16:38:51,754 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-23 16:38:51,755 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-23 16:38:51,755 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-23 16:38:51,755 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-09-23 16:38:51,756 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-09-23 16:38:51,756 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-23 16:38:51,756 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-23 16:38:51,757 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-23 16:38:51,757 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-23 16:38:51,758 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-23 16:38:51,758 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 1
2025-09-23 16:38:51,759 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-23 16:38:51,760 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-23 16:38:51,760 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-23 16:38:51,761 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower
2025-09-23 16:38:51,761 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-23 16:38:51,762 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-23 16:38:51,765 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:38:51,779 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 16:38:51,795 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:38:51,818 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-23 16:39:06,920 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:39:06,936 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 16:39:06,952 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:39:06,976 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-23 16:39:22,380 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:39:22,400 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 16:39:22,428 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:39:22,459 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-15 00:00:00
2025-09-23 16:39:37,186 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:39:37,204 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-23 16:39:37,205 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 16:39:37,221 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:39:37,248 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data starts at 2018-05-04 08:00:00
2025-09-23 16:39:37,249 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-23 16:39:50,688 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:39:50,707 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 16:39:50,728 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:39:50,755 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-23 16:40:05,705 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 16:43:32,398 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-23_16-43-32.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │    228 │         0.51 │         353.351 │        35.34 │     15:19:00 │   75     0   153  32.9 │
│ XRP/USDT │    175 │         0.56 │         289.397 │        28.94 │     13:46:00 │   61     0   114  34.9 │
│ BTC/USDT │    282 │         0.29 │         169.199 │        16.92 │     16:24:00 │   86     0   196  30.5 │
│ LTC/USDT │    168 │         -0.0 │         -36.090 │        -3.61 │     15:00:00 │   47     0   121  28.0 │
│ BNB/USDT │    262 │          0.0 │         -43.031 │         -4.3 │     15:09:00 │   74     0   188  28.2 │
│    TOTAL │   1115 │         0.26 │         732.826 │        73.28 │     15:16:00 │  343     0   772  30.8 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                           LEFT OPEN TRADES REPORT                                           
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         0.05 │           0.165 │         0.02 │      5:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         0.05 │           0.165 │         0.02 │      5:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                      ENTER TAG STATS                                                      
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │     816 │         0.24 │         478.637 │        47.86 │     15:55:00 │  253     0   563  31.0 │
│         hammer_rebond │     194 │         0.35 │         170.647 │        17.06 │     12:36:00 │   53     0   141  27.3 │
│      engulfing_rebond │     105 │         0.32 │          83.542 │         8.35 │     15:05:00 │   37     0    68  35.2 │
│                 TOTAL │    1115 │         0.26 │         732.826 │        73.28 │     15:16:00 │  343     0   772  30.8 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │    83 │        10.41 │        2498.502 │       249.85 │ 1 day, 1:23:00 │   83     0     0   100 │
│     force_exit │     1 │         0.05 │           0.165 │         0.02 │        5:00:00 │    1     0     0   100 │
│      stop_loss │     2 │       -10.18 │         -43.839 │        -4.38 │        7:45:00 │    0     0     2     0 │
│    exit_signal │  1029 │        -0.53 │       -1722.002 │       -172.2 │       14:28:00 │  259     0   770  25.2 │
│          TOTAL │  1115 │         0.26 │         732.826 │        73.28 │       15:16:00 │  343     0   772  30.8 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                               MIXED TAG STATS                                                               
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_1R │     57 │        10.37 │        1707.085 │       170.71 │ 1 day, 1:04:00 │   57     0     0   100 │
│         hammer_rebond │ take_profit_1R │     17 │        10.49 │         517.263 │        51.73 │ 1 day, 3:02:00 │   17     0     0   100 │
│      engulfing_rebond │ take_profit_1R │      9 │        10.53 │         274.154 │        27.42 │ 1 day, 0:17:00 │    9     0     0   100 │
│ strong_bullish_rebond │     force_exit │      1 │         0.05 │           0.165 │         0.02 │        5:00:00 │    1     0     0   100 │
│ strong_bullish_rebond │      stop_loss │      2 │       -10.18 │         -43.839 │        -4.38 │        7:45:00 │    0     0     2     0 │
│      engulfing_rebond │    exit_signal │     96 │        -0.64 │        -190.612 │       -19.06 │       14:14:00 │   28     0    68  29.2 │
│         hammer_rebond │    exit_signal │    177 │        -0.63 │        -346.616 │       -34.66 │       11:13:00 │   36     0   141  20.3 │
│ strong_bullish_rebond │    exit_signal │    756 │         -0.5 │       -1184.774 │      -118.48 │       15:15:00 │  195     0   561  25.8 │
│                 TOTAL │                │   1115 │         0.26 │         732.826 │        73.28 │       15:16:00 │  343     0   772  30.8 │
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
│ Total/Daily Avg Trades        │ 1115 / 0.4                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1732.826 USDT                  │
│ Absolute profit               │ 732.826 USDT                   │
│ Total profit %                │ 73.28%                         │
│ CAGR %                        │ 7.40%                          │
│ Sortino                       │ 1.51                           │
│ Sharpe                        │ 0.48                           │
│ Calmar                        │ 2.62                           │
│ SQN                           │ 2.11                           │
│ Profit factor                 │ 1.21                           │
│ Expectancy (Ratio)            │ 0.66 (0.15)                    │
│ Avg. daily profit             │ 0.261 USDT                     │
│ Avg. stake amount             │ 315.456 USDT                   │
│ Total trade volume            │ 705608.736 USDT                │
│                               │                                │
│ Best Pair                     │ ETH/USDT 35.34%                │
│ Worst Pair                    │ BNB/USDT -4.30%                │
│ Best trade                    │ XRP/USDT 13.21%                │
│ Worst trade                   │ BNB/USDT -10.18%               │
│ Best day                      │ 83.618 USDT                    │
│ Worst day                     │ -31.299 USDT                   │
│ Days win/draw/lose            │ 234 / 2028 / 498               │
│ Min/Max/Avg. Duration Winners │ 0d 01:10 / 3d 05:35 / 1d 04:16 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 1d 22:00 / 0d 09:29 │
│ Max Consecutive Wins / Loss   │ 6 / 21                         │
│ Rejected Entry signals        │ 384                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 978.853 USDT                   │
│ Max balance                   │ 1959.446 USDT                  │
│ Max % of account underwater   │ 19.03%                         │
│ Absolute drawdown             │ 372.959 USDT (19.03%)          │
│ Drawdown duration             │ 899 days 16:00:00              │
│ Profit at drawdown start      │ 959.446 USDT                   │
│ Profit at drawdown end        │ 586.487 USDT                   │
│ Drawdown start                │ 2023-01-21 23:00:00            │
│ Drawdown end                  │ 2025-07-09 15:00:00            │
│ Market change                 │ 2372.94%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │   1115 │         0.26 │         732.826 │        73.28 │     15:16:00 │  343     0   772  30.8 │ 372.959 USDT  19.03% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-23T18:43:34.224934",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 7149,
  "total_daily_avg_trades": "1115 / 0.4",
  "absolute_profit_usdt": 732.826,
  "total_profit_pct": 73.28,
  "cagr_pct": 7.4,
  "sortino": 1.51,
  "sharpe": 0.48,
  "calmar": 2.62,
  "sqn": 2.11,
  "max_consecutive_wins_loss": "6 / 21",
  "min_balance_usdt": 978.853,
  "max_balance_usdt": 1959.446,
  "absolute_drawdown_pct": 19.03,
  "market_change_pct": 2372.94,
  "win_draw_loss_winpct": "343 0 772 30.8"
}
```
