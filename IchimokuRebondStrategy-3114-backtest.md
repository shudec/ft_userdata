# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 3114  
**Timestamp:** 2025-09-24 09:47:16

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 3114,
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
2025-09-24 07:41:57,751 - freqtrade - INFO - freqtrade 2025.8
2025-09-24 07:41:58,405 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-24 07:42:01,110 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-24 07:42:01,117 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-24 07:42:01,117 - freqtrade.loggers - INFO - Logfile configured
2025-09-24 07:42:01,118 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-24 07:42:01,118 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-24 07:42:01,119 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-24 07:42:01,119 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-24 07:42:01,120 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20200101-20251231 ...
2025-09-24 07:42:01,575 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-24 07:42:01,578 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-24 07:42:01,578 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-24 07:42:01,579 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-24 07:42:01,579 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-24 07:42:01,580 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20200101-20251231
2025-09-24 07:42:01,581 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-24 07:42:01,593 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-24 07:42:01,594 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 07:42:01,597 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-24 07:42:01,598 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-24 07:42:01,598 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-24 07:42:01,623 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-24 07:42:04,061 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-24 07:42:04,200 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-24 07:42:04,202 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-24 07:42:04,207 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-24 07:42:04,207 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-24 07:42:04,208 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-24 07:42:04,209 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-24 07:42:04,209 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-24 07:42:04,210 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-24 07:42:04,210 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-24 07:42:04,211 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-24 07:42:04,212 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-24 07:42:04,212 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-24 07:42:04,213 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-24 07:42:04,213 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-24 07:42:04,214 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-24 07:42:04,214 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-24 07:42:04,215 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-24 07:42:04,216 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-24 07:42:04,216 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-24 07:42:04,217 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-24 07:42:04,217 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-24 07:42:04,218 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-24 07:42:04,218 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-24 07:42:04,219 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-24 07:42:04,219 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-24 07:42:04,220 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-24 07:42:04,220 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-24 07:42:04,220 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-24 07:42:04,221 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-24 07:42:04,221 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-24 07:42:04,222 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 07:42:04,250 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-24 07:42:04,277 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-24 07:42:04,353 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 07:42:04,451 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 07:42:04,522 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 07:42:04,596 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 07:42:04,683 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 07:42:04,720 - freqtrade.optimize.backtesting - INFO - Loading data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 07:42:05,026 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 07:42:05,603 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 07:42:06,139 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 07:42:06,766 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 07:42:07,374 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 07:42:09,556 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-24 07:42:09,563 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-24 07:42:09,564 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-24 07:42:09,564 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-24 07:42:09,565 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-24 07:42:09,565 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-24 07:42:09,566 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-24 07:42:09,566 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-24 07:42:09,567 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-24 07:42:09,568 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-24 07:42:09,568 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-24 07:42:09,569 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-24 07:42:09,569 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-09-24 07:42:09,569 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-09-24 07:42:09,570 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-24 07:42:09,570 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-24 07:42:09,571 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-24 07:42:09,572 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-24 07:42:09,572 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-24 07:42:09,573 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 8
2025-09-24 07:42:09,573 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-24 07:42:09,573 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-24 07:42:09,574 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-24 07:42:09,574 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-24 07:42:09,575 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-24 07:42:09,575 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-24 07:42:09,578 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:42:09,598 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 07:42:09,615 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:42:09,644 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 07:42:27,605 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:42:27,627 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 07:42:27,647 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:42:27,675 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 07:42:44,537 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:42:44,556 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 07:42:44,577 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:42:44,611 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-15 00:00:00
2025-09-24 07:43:01,481 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:43:01,504 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 07:43:01,522 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:43:01,561 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 07:43:18,839 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:43:18,865 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 07:43:18,894 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:43:18,927 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 07:43:35,662 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 07:47:15,113 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-24_07-47-15.meta.json"
Result for strategy IchimokuRebondStrategy
                                              BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │    218 │          0.1 │          83.899 │         8.39 │ 1 day, 0:10:00 │  110     0   108  50.5 │
│ BNB/USDT │    202 │        -0.03 │         -51.846 │        -5.18 │       19:21:00 │  104     0    98  51.5 │
│ ETH/USDT │    190 │        -0.08 │         -53.506 │        -5.35 │       20:33:00 │   96     0    94  50.5 │
│ XRP/USDT │    133 │        -0.28 │         -75.954 │         -7.6 │       19:53:00 │   63     0    70  47.4 │
│ LTC/USDT │    137 │        -0.17 │         -82.649 │        -8.26 │       23:44:00 │   66     0    71  48.2 │
│    TOTAL │    880 │        -0.07 │        -180.056 │       -18.01 │       21:34:00 │  439     0   441  49.9 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                            LEFT OPEN TRADES REPORT                                            
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         0.07 │           0.292 │         0.03 │ 1 day, 1:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         0.07 │           0.292 │         0.03 │ 1 day, 1:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                       ENTER TAG STATS                                                       
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│         hammer_rebond │     146 │         0.19 │         112.485 │        11.25 │ 1 day, 4:26:00 │   71     0    75  48.6 │
│      engulfing_rebond │      91 │         0.03 │          45.697 │         4.57 │       19:03:00 │   51     0    40  56.0 │
│ strong_bullish_rebond │     643 │        -0.14 │        -338.238 │       -33.82 │       20:22:00 │  317     0   326  49.3 │
│                 TOTAL │     880 │        -0.07 │        -180.056 │       -18.01 │       21:34:00 │  439     0   441  49.9 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │    82 │         5.49 │        1535.023 │        153.5 │ 1 day, 4:19:00 │   82     0     0   100 │
│     force_exit │     1 │         0.07 │           0.292 │         0.03 │ 1 day, 1:00:00 │    1     0     0   100 │
│      stop_loss │    37 │        -5.26 │        -702.218 │       -70.22 │       13:20:00 │    0     0    37     0 │
│    exit_signal │   760 │        -0.41 │       -1013.153 │      -101.32 │       21:14:00 │  356     0   404  46.8 │
│          TOTAL │   880 │        -0.07 │        -180.056 │       -18.01 │       21:34:00 │  439     0   441  49.9 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                               MIXED TAG STATS                                                               
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_1R │     55 │         4.98 │        1015.875 │       101.59 │ 1 day, 2:29:00 │   55     0     0   100 │
│         hammer_rebond │ take_profit_1R │     19 │         6.75 │         368.888 │        36.89 │ 1 day, 9:13:00 │   19     0     0   100 │
│      engulfing_rebond │ take_profit_1R │      8 │         5.92 │         150.261 │        15.03 │ 1 day, 5:20:00 │    8     0     0   100 │
│ strong_bullish_rebond │     force_exit │      1 │         0.07 │           0.292 │         0.03 │ 1 day, 1:00:00 │    1     0     0   100 │
│      engulfing_rebond │      stop_loss │      3 │        -5.76 │         -51.346 │        -5.13 │        2:17:00 │    0     0     3     0 │
│      engulfing_rebond │    exit_signal │     80 │        -0.34 │         -53.218 │        -5.32 │       18:39:00 │   43     0    37  53.8 │
│         hammer_rebond │    exit_signal │    119 │        -0.42 │         -89.473 │        -8.95 │ 1 day, 4:44:00 │   52     0    67  43.7 │
│         hammer_rebond │      stop_loss │      8 │        -6.35 │        -166.930 │       -16.69 │       12:31:00 │    0     0     8     0 │
│ strong_bullish_rebond │      stop_loss │     26 │        -4.86 │        -483.942 │       -48.39 │       14:52:00 │    0     0    26     0 │
│ strong_bullish_rebond │    exit_signal │    561 │        -0.42 │        -870.463 │       -87.05 │       20:01:00 │  261     0   300  46.5 │
│                 TOTAL │                │    880 │        -0.07 │        -180.056 │       -18.01 │       21:34:00 │  439     0   441  49.9 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2020-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 880 / 0.42                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 819.944 USDT                   │
│ Absolute profit               │ -180.056 USDT                  │
│ Total profit %                │ -18.01%                        │
│ CAGR %                        │ -3.43%                         │
│ Sortino                       │ -0.29                          │
│ Sharpe                        │ -0.16                          │
│ Calmar                        │ -0.38                          │
│ SQN                           │ -0.59                          │
│ Profit factor                 │ 0.95                           │
│ Expectancy (Ratio)            │ -0.20 (-0.02)                  │
│ Avg. daily profit             │ -0.087 USDT                    │
│ Avg. stake amount             │ 344.387 USDT                   │
│ Total trade volume            │ 607155.019 USDT                │
│                               │                                │
│ Best Pair                     │ BTC/USDT 8.39%                 │
│ Worst Pair                    │ LTC/USDT -8.26%                │
│ Best trade                    │ XRP/USDT 13.21%                │
│ Worst trade                   │ XRP/USDT -12.68%               │
│ Best day                      │ 55.442 USDT                    │
│ Worst day                     │ -52.533 USDT                   │
│ Days win/draw/lose            │ 292 / 1435 / 315               │
│ Min/Max/Avg. Duration Winners │ 0d 00:50 / 5d 01:00 / 0d 18:35 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:30 / 3d 11:00 / 1d 00:32 │
│ Max Consecutive Wins / Loss   │ 11 / 12                        │
│ Rejected Entry signals        │ 372                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 746.793 USDT                   │
│ Max balance                   │ 1317.536 USDT                  │
│ Max % of account underwater   │ 43.32%                         │
│ Absolute drawdown             │ 570.743 USDT (43.32%)          │
│ Drawdown duration             │ 1526 days 22:30:00             │
│ Profit at drawdown start      │ 317.536 USDT                   │
│ Profit at drawdown end        │ -253.207 USDT                  │
│ Drawdown start                │ 2021-05-03 16:30:00            │
│ Drawdown end                  │ 2025-07-08 15:00:00            │
│ Market change                 │ 2537.81%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2020-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    880 │        -0.07 │        -180.056 │       -18.01 │     21:34:00 │  439     0   441  49.9 │ 570.743 USDT  43.32% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-24T09:47:16.699518",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 3114,
  "total_daily_avg_trades": "880 / 0.42",
  "absolute_profit_usdt": -180.056,
  "total_profit_pct": -18.01,
  "cagr_pct": -3.43,
  "sortino": -0.29,
  "sharpe": -0.16,
  "calmar": -0.38,
  "sqn": -0.59,
  "max_consecutive_wins_loss": "11 / 12",
  "min_balance_usdt": 746.793,
  "max_balance_usdt": 1317.536,
  "absolute_drawdown_pct": 43.32,
  "market_change_pct": 2537.81,
  "win_draw_loss_winpct": "439 0 441 49.9"
}
```
