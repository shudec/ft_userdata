# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 4829  
**Timestamp:** 2025-09-23 21:59:16

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 4829,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20250101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20250101-20251231
```

## Backtesting Output
```
2025-09-23 19:58:41,285 - freqtrade - INFO - freqtrade 2025.7
2025-09-23 19:58:41,658 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-23 19:58:41,659 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-23 19:58:43,150 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-23 19:58:43,153 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-23 19:58:43,153 - freqtrade.loggers - INFO - Logfile configured
2025-09-23 19:58:43,153 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-23 19:58:43,154 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-23 19:58:43,154 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-23 19:58:43,154 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-23 19:58:43,155 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20250101-20251231 ...
2025-09-23 19:58:43,162 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-23 19:58:43,163 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-23 19:58:43,163 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-23 19:58:43,164 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-23 19:58:43,164 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-23 19:58:43,165 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20250101-20251231
2025-09-23 19:58:43,166 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-23 19:58:43,185 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-23 19:58:43,186 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 19:58:43,190 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-23 19:58:43,191 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-23 19:58:43,191 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-23 19:58:43,225 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-23 19:58:45,714 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-23 19:58:45,754 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-23 19:58:45,755 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-23 19:58:45,756 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-23 19:58:45,756 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-23 19:58:45,757 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-23 19:58:45,757 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-23 19:58:45,757 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-23 19:58:45,758 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-23 19:58:45,758 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-23 19:58:45,758 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-23 19:58:45,759 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-23 19:58:45,759 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-23 19:58:45,759 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-23 19:58:45,760 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-23 19:58:45,760 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-23 19:58:45,760 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-23 19:58:45,761 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-23 19:58:45,761 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-23 19:58:45,762 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-23 19:58:45,762 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-23 19:58:45,762 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-23 19:58:45,763 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-23 19:58:45,763 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-23 19:58:45,763 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-23 19:58:45,764 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-23 19:58:45,764 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-23 19:58:45,764 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-23 19:58:45,765 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-23 19:58:45,765 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-23 19:58:45,766 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-23 19:58:45,766 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 19:58:45,771 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-23 19:58:45,802 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-23 19:58:45,833 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 19:58:45,877 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 19:58:45,911 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 19:58:45,945 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 19:58:45,978 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 19:58:45,996 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 00:00:00 up to 2025-09-11 17:00:00 (253 days).
2025-09-23 19:58:46,086 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 19:58:46,196 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 19:58:46,290 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 19:58:46,393 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 19:58:46,492 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 19:58:46,822 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-23 19:58:46,824 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-23 19:58:46,824 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-23 19:58:46,825 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-23 19:58:46,825 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-23 19:58:46,826 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-23 19:58:46,826 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-23 19:58:46,827 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-23 19:58:46,827 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-23 19:58:46,827 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-23 19:58:46,828 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-23 19:58:46,828 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-23 19:58:46,829 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-09-23 19:58:46,829 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-09-23 19:58:46,829 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-23 19:58:46,830 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-23 19:58:46,830 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-23 19:58:46,831 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-23 19:58:46,831 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-23 19:58:46,832 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 1
2025-09-23 19:58:46,832 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-23 19:58:46,832 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-23 19:58:46,833 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-23 19:58:46,833 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower
2025-09-23 19:58:46,834 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-23 19:58:46,834 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-23 19:58:46,836 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2025-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 19:58:46,846 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 19:58:46,866 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2025-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 19:58:46,884 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 19:58:48,119 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2025-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 19:58:48,126 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 19:58:48,139 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2025-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 19:58:48,156 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 19:58:49,387 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2025-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 19:58:49,393 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 19:58:49,407 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2025-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 19:58:49,424 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 19:58:50,628 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2025-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 19:58:50,635 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 19:58:50,647 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2025-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 19:58:50,665 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 19:58:51,899 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2025-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 19:58:51,906 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 19:58:51,919 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2025-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 19:58:51,936 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 19:58:53,154 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2025-01-01 00:00:00 up to 2025-09-11 17:00:00 (253 days).
2025-09-23 19:59:15,078 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-23_19-59-15.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │     16 │         1.12 │          36.169 │         3.62 │  1 day, 19:15:00 │    7     0     9  43.8 │
│ LTC/USDT │     12 │         1.39 │          30.745 │         3.07 │   1 day, 6:38:00 │    4     0     8  33.3 │
│ BTC/USDT │     20 │         0.62 │          21.952 │          2.2 │ 2 days, 12:29:00 │    8     0    12  40.0 │
│ BNB/USDT │     22 │        -0.02 │          -2.064 │        -0.21 │  1 day, 20:22:00 │    6     0    16  27.3 │
│ XRP/USDT │     15 │        -1.86 │         -55.667 │        -5.57 │  1 day, 20:27:00 │    2     0    13  13.3 │
│    TOTAL │     85 │         0.22 │          31.135 │         3.11 │  1 day, 22:02:00 │   27     0    58  31.8 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         4.38 │           8.965 │          0.9 │ 5 days, 15:00:00 │    1     0     0   100 │
│ BTC/USDT │      1 │        -0.12 │          -0.252 │        -0.03 │         13:00:00 │    0     0     1     0 │
│ LTC/USDT │      1 │        -3.08 │          -6.287 │        -0.63 │         17:00:00 │    0     0     1     0 │
│    TOTAL │      3 │         0.39 │           2.426 │         0.24 │  2 days, 7:00:00 │    1     0     2  33.3 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                       ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│      engulfing_rebond │       6 │         0.92 │          11.428 │         1.14 │  1 day, 7:08:00 │    2     0     4  33.3 │
│         hammer_rebond │       4 │         1.23 │          10.937 │         1.09 │  1 day, 6:16:00 │    1     0     3  25.0 │
│ strong_bullish_rebond │      75 │         0.11 │           8.770 │         0.88 │ 2 days, 0:04:00 │   24     0    51  32.0 │
│                 TOTAL │      85 │         0.22 │          31.135 │         3.11 │ 1 day, 22:02:00 │   27     0    58  31.8 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │    11 │         10.3 │         217.689 │        21.77 │ 2 days, 3:56:00 │   11     0     0   100 │
│     force_exit │     3 │         0.39 │           2.426 │         0.24 │ 2 days, 7:00:00 │    1     0     2  33.3 │
│    exit_signal │    71 │        -1.35 │        -188.981 │        -18.9 │ 1 day, 20:44:00 │   15     0    56  21.1 │
│          TOTAL │    85 │         0.22 │          31.135 │         3.11 │ 1 day, 22:02:00 │   27     0    58  31.8 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                               MIXED TAG STATS                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_1R │      9 │        10.35 │         176.545 │        17.65 │ 2 days, 7:30:00 │    9     0     0   100 │
│         hammer_rebond │ take_profit_1R │      1 │        10.13 │          21.001 │          2.1 │ 1 day, 16:05:00 │    1     0     0   100 │
│      engulfing_rebond │ take_profit_1R │      1 │        10.04 │          20.142 │         2.01 │  1 day, 7:45:00 │    1     0     0   100 │
│ strong_bullish_rebond │     force_exit │      2 │         0.65 │           2.678 │         0.27 │ 3 days, 4:00:00 │    1     0     1  50.0 │
│      engulfing_rebond │     force_exit │      1 │        -0.12 │          -0.252 │        -0.03 │        13:00:00 │    0     0     1     0 │
│      engulfing_rebond │    exit_signal │      4 │        -1.11 │          -8.463 │        -0.85 │ 1 day, 11:30:00 │    1     0     3  25.0 │
│         hammer_rebond │    exit_signal │      3 │        -1.74 │         -10.065 │        -1.01 │  1 day, 3:00:00 │    0     0     3     0 │
│ strong_bullish_rebond │    exit_signal │     64 │        -1.35 │        -170.453 │       -17.05 │ 1 day, 22:08:00 │   14     0    50  21.9 │
│                 TOTAL │                │     85 │         0.22 │          31.135 │         3.11 │ 1 day, 22:02:00 │   27     0    58  31.8 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2025-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-11 17:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 85 / 0.34                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1031.135 USDT                  │
│ Absolute profit               │ 31.135 USDT                    │
│ Total profit %                │ 3.11%                          │
│ CAGR %                        │ 4.52%                          │
│ Sortino                       │ 0.82                           │
│ Sharpe                        │ 0.27                           │
│ Calmar                        │ 3.55                           │
│ SQN                           │ 0.38                           │
│ Profit factor                 │ 1.12                           │
│ Expectancy (Ratio)            │ 0.37 (0.08)                    │
│ Avg. daily profit             │ 0.123 USDT                     │
│ Avg. stake amount             │ 194.325 USDT                   │
│ Total trade volume            │ 33132.596 USDT                 │
│                               │                                │
│ Best Pair                     │ ETH/USDT 3.62%                 │
│ Worst Pair                    │ XRP/USDT -5.57%                │
│ Best trade                    │ BNB/USDT 10.97%                │
│ Worst trade                   │ XRP/USDT -7.73%                │
│ Best day                      │ 38.542 USDT                    │
│ Worst day                     │ -21.586 USDT                   │
│ Days win/draw/lose            │ 20 / 154 / 38                  │
│ Min/Max/Avg. Duration Winners │ 1d 00:45 / 5d 19:00 / 3d 08:39 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 4d 07:00 / 1d 05:55 │
│ Max Consecutive Wins / Loss   │ 5 / 9                          │
│ Rejected Entry signals        │ 324                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 933.863 USDT                   │
│ Max balance                   │ 1068.343 USDT                  │
│ Max % of account underwater   │ 6.61%                          │
│ Absolute Drawdown (Account)   │ 6.61%                          │
│ Absolute Drawdown             │ 66.137 USDT                    │
│ Drawdown high                 │ -7.56 USDT                     │
│ Drawdown low                  │ -66.137 USDT                   │
│ Drawdown Start                │ 2025-02-12 07:00:00            │
│ Drawdown End                  │ 2025-05-04 03:00:00            │
│ Market change                 │ 26.37%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2025-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                  
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     85 │         0.22 │          31.135 │         3.11 │ 1 day, 22:02:00 │   27     0    58  31.8 │ 66.137 USDT  6.61% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-23T21:59:16.126222",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 4829,
  "total_daily_avg_trades": "85 / 0.34",
  "absolute_profit_usdt": 31.135,
  "total_profit_pct": 3.11,
  "cagr_pct": 4.52,
  "sortino": 0.82,
  "sharpe": 0.27,
  "calmar": 3.55,
  "sqn": 0.38,
  "max_consecutive_wins_loss": "5 / 9",
  "min_balance_usdt": 933.863,
  "max_balance_usdt": 1068.343,
  "market_change_pct": 26.37
}
```
