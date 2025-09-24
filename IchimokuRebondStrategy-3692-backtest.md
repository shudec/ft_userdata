# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 3692  
**Timestamp:** 2025-09-24 10:50:32

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 3692,
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
2025-09-24 08:38:11,052 - freqtrade - INFO - freqtrade 2025.8
2025-09-24 08:38:11,433 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-24 08:38:13,207 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-24 08:38:13,213 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-24 08:38:13,214 - freqtrade.loggers - INFO - Logfile configured
2025-09-24 08:38:13,214 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-24 08:38:13,215 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-24 08:38:13,216 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-24 08:38:13,216 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-24 08:38:13,217 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20200101-20251231 ...
2025-09-24 08:38:13,714 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-24 08:38:13,716 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-24 08:38:13,716 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-24 08:38:13,717 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-24 08:38:13,717 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-24 08:38:13,718 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20200101-20251231
2025-09-24 08:38:13,719 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-24 08:38:13,733 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-24 08:38:13,734 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 08:38:13,737 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-24 08:38:13,739 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-24 08:38:13,740 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-24 08:38:13,765 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-24 08:38:16,253 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-24 08:38:16,373 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-24 08:38:16,375 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-24 08:38:16,379 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-24 08:38:16,380 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-24 08:38:16,380 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-24 08:38:16,381 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-24 08:38:16,381 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-24 08:38:16,382 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-24 08:38:16,382 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-24 08:38:16,382 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-24 08:38:16,383 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-24 08:38:16,383 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-24 08:38:16,383 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-24 08:38:16,384 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-24 08:38:16,384 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-24 08:38:16,384 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-24 08:38:16,385 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-24 08:38:16,385 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-24 08:38:16,386 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-24 08:38:16,386 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-24 08:38:16,387 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-24 08:38:16,388 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-24 08:38:16,388 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-24 08:38:16,389 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-24 08:38:16,389 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-24 08:38:16,390 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-24 08:38:16,390 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-24 08:38:16,390 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-24 08:38:16,391 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-24 08:38:16,391 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-24 08:38:16,392 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 08:38:16,417 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-24 08:38:16,449 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-24 08:38:16,505 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 08:38:16,587 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 08:38:16,652 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 08:38:16,715 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 08:38:16,784 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 08:38:16,819 - freqtrade.optimize.backtesting - INFO - Loading data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 08:38:17,080 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 08:38:17,603 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 08:38:18,174 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 08:38:18,821 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 08:38:19,413 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 08:38:21,731 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-24 08:38:21,737 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-24 08:38:21,738 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-24 08:38:21,739 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-24 08:38:21,740 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-24 08:38:21,740 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-24 08:38:21,741 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-24 08:38:21,741 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-24 08:38:21,741 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-24 08:38:21,742 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-24 08:38:21,742 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-24 08:38:21,743 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-24 08:38:21,743 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-09-24 08:38:21,743 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-09-24 08:38:21,744 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-24 08:38:21,744 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-24 08:38:21,745 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-24 08:38:21,745 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-24 08:38:21,746 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-24 08:38:21,746 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 8
2025-09-24 08:38:21,747 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-24 08:38:21,748 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-24 08:38:21,748 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-24 08:38:21,748 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-24 08:38:21,749 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-24 08:38:21,749 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-24 08:38:21,753 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:38:21,774 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 08:38:21,796 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:38:21,825 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 08:38:38,650 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:38:38,668 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 08:38:38,694 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:38:38,726 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 08:38:55,838 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:38:55,855 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 08:38:55,871 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:38:55,897 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-15 00:00:00
2025-09-24 08:39:12,458 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:39:12,475 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 08:39:12,493 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:39:12,517 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 08:39:28,832 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:39:28,849 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 08:39:28,865 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:39:28,891 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 08:39:45,507 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 08:50:30,341 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-24_08-50-30.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │    151 │         0.67 │         330.256 │        33.03 │  1 day, 7:00:00 │   62     0    89  41.1 │
│ BNB/USDT │    203 │          0.6 │         211.626 │        21.16 │ 1 day, 13:54:00 │   90     0   113  44.3 │
│ BTC/USDT │    252 │         0.22 │         197.051 │        19.71 │ 1 day, 10:22:00 │  129     0   123  51.2 │
│ ETH/USDT │    203 │         0.23 │         121.398 │        12.14 │ 1 day, 12:47:00 │  103     0   100  50.7 │
│ LTC/USDT │    146 │        -0.37 │        -232.352 │       -23.24 │  1 day, 8:30:00 │   61     0    85  41.8 │
│    TOTAL │    955 │         0.28 │         627.979 │         62.8 │ 1 day, 10:49:00 │  445     0   510  46.6 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                            LEFT OPEN TRADES REPORT                                            
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         0.07 │           0.581 │         0.06 │ 1 day, 1:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         0.07 │           0.581 │         0.06 │ 1 day, 1:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                       ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │     765 │         0.23 │         360.363 │        36.04 │  1 day, 9:49:00 │  362     0   403  47.3 │
│      engulfing_rebond │      91 │         0.59 │         169.995 │         17.0 │  1 day, 9:30:00 │   43     0    48  47.3 │
│         hammer_rebond │      99 │         0.44 │          97.621 │         9.76 │ 1 day, 19:49:00 │   40     0    59  40.4 │
│                 TOTAL │     955 │         0.28 │         627.979 │         62.8 │ 1 day, 10:49:00 │  445     0   510  46.6 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                       EXIT REASON STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃               Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ sell_ichimoku_futur_cloud │   346 │         4.16 │        6336.416 │       633.64 │        22:21:00 │  346     0     0   100 │
│            take_profit_3R │     6 │        21.84 │         443.366 │        44.34 │ 3 days, 3:13:00 │    6     0     0   100 │
│                force_exit │     1 │         0.07 │           0.581 │         0.06 │  1 day, 1:00:00 │    1     0     0   100 │
│                 stop_loss │    46 │         -5.7 │       -1295.845 │      -129.58 │        19:57:00 │    0     0    46     0 │
│               exit_signal │   556 │        -1.87 │       -4856.540 │      -485.65 │ 1 day, 19:23:00 │   92     0   464  16.5 │
│                     TOTAL │   955 │         0.28 │         627.979 │         62.8 │ 1 day, 10:49:00 │  445     0   510  46.6 │
└───────────────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                                     MIXED TAG STATS                                                                      
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃               Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ sell_ichimoku_futur_cloud │    291 │         3.96 │        5087.271 │       508.73 │         22:15:00 │  291     0     0   100 │
│      engulfing_rebond │ sell_ichimoku_futur_cloud │     35 │         4.83 │         705.927 │        70.59 │         22:36:00 │   35     0     0   100 │
│         hammer_rebond │ sell_ichimoku_futur_cloud │     20 │         5.98 │         543.218 │        54.32 │         23:22:00 │   20     0     0   100 │
│ strong_bullish_rebond │            take_profit_3R │      4 │        19.43 │         283.915 │        28.39 │ 2 days, 14:16:00 │    4     0     0   100 │
│         hammer_rebond │            take_profit_3R │      2 │        26.67 │         159.451 │        15.95 │  4 days, 5:08:00 │    2     0     0   100 │
│ strong_bullish_rebond │                force_exit │      1 │         0.07 │           0.581 │         0.06 │   1 day, 1:00:00 │    1     0     0   100 │
│      engulfing_rebond │                 stop_loss │      5 │        -6.43 │        -140.040 │        -14.0 │         12:16:00 │    0     0     5     0 │
│         hammer_rebond │                 stop_loss │      7 │        -4.95 │        -191.827 │       -19.18 │         22:20:00 │    0     0     7     0 │
│      engulfing_rebond │               exit_signal │     51 │        -1.64 │        -395.892 │       -39.59 │  1 day, 19:04:00 │    8     0    43  15.7 │
│         hammer_rebond │               exit_signal │     70 │        -1.35 │        -413.222 │       -41.32 │  2 days, 2:10:00 │   18     0    52  25.7 │
│ strong_bullish_rebond │                 stop_loss │     34 │        -5.75 │        -963.978 │        -96.4 │         20:36:00 │    0     0    34     0 │
│ strong_bullish_rebond │               exit_signal │    435 │        -1.98 │       -4047.426 │      -404.74 │  1 day, 18:20:00 │   66     0   369  15.2 │
│                 TOTAL │                           │    955 │         0.28 │         627.979 │         62.8 │  1 day, 10:49:00 │  445     0   510  46.6 │
└───────────────────────┴───────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2020-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 955 / 0.46                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1627.979 USDT                  │
│ Absolute profit               │ 627.979 USDT                   │
│ Total profit %                │ 62.80%                         │
│ CAGR %                        │ 8.93%                          │
│ Sortino                       │ 0.67                           │
│ Sharpe                        │ 0.29                           │
│ Calmar                        │ 1.78                           │
│ SQN                           │ 1.01                           │
│ Profit factor                 │ 1.09                           │
│ Expectancy (Ratio)            │ 0.66 (0.05)                    │
│ Avg. daily profit             │ 0.302 USDT                     │
│ Avg. stake amount             │ 501.103 USDT                   │
│ Total trade volume            │ 959651.491 USDT                │
│                               │                                │
│ Best Pair                     │ XRP/USDT 33.03%                │
│ Worst Pair                    │ LTC/USDT -23.24%               │
│ Best trade                    │ XRP/USDT 37.80%                │
│ Worst trade                   │ XRP/USDT -12.68%               │
│ Best day                      │ 171.507 USDT                   │
│ Worst day                     │ -88.069 USDT                   │
│ Days win/draw/lose            │ 274 / 1426 / 340               │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 6d 16:00 / 1d 12:35 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:30 / 4d 10:00 / 1d 09:16 │
│ Max Consecutive Wins / Loss   │ 13 / 17                        │
│ Rejected Entry signals        │ 1417                           │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 890.685 USDT                   │
│ Max balance                   │ 2074.115 USDT                  │
│ Max % of account underwater   │ 32.37%                         │
│ Absolute drawdown             │ 671.421 USDT (32.37%)          │
│ Drawdown duration             │ 699 days 18:40:00              │
│ Profit at drawdown start      │ 1074.115 USDT                  │
│ Profit at drawdown end        │ 402.694 USDT                   │
│ Drawdown start                │ 2021-11-08 15:20:00            │
│ Drawdown end                  │ 2023-10-09 10:00:00            │
│ Market change                 │ 2537.81%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2020-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    955 │         0.28 │         627.979 │         62.8 │ 1 day, 10:49:00 │  445     0   510  46.6 │ 671.421 USDT  32.37% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-24T10:50:32.098054",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 3692,
  "total_daily_avg_trades": "955 / 0.46",
  "absolute_profit_usdt": 627.979,
  "total_profit_pct": 62.8,
  "cagr_pct": 8.93,
  "sortino": 0.67,
  "sharpe": 0.29,
  "calmar": 1.78,
  "sqn": 1.01,
  "max_consecutive_wins_loss": "13 / 17",
  "min_balance_usdt": 890.685,
  "max_balance_usdt": 2074.115,
  "absolute_drawdown_pct": 32.37,
  "market_change_pct": 2537.81
}
```
