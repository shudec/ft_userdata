# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 6274  
**Timestamp:** 2025-09-24 14:14:00

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 6274,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20170801-20231231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20231231
```

## Backtesting Output
```
2025-09-24 12:05:47,315 - freqtrade - INFO - freqtrade 2025.8
2025-09-24 12:05:47,943 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-24 12:05:51,055 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-24 12:05:51,063 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-24 12:05:51,063 - freqtrade.loggers - INFO - Logfile configured
2025-09-24 12:05:51,064 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-24 12:05:51,065 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-24 12:05:51,065 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-24 12:05:51,066 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-24 12:05:51,067 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20231231 ...
2025-09-24 12:05:51,750 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-24 12:05:51,753 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-24 12:05:51,754 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-24 12:05:51,755 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-24 12:05:51,756 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-24 12:05:51,757 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20231231
2025-09-24 12:05:51,760 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-24 12:05:51,782 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-24 12:05:51,784 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 12:05:51,789 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-24 12:05:51,791 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-24 12:05:51,792 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-24 12:05:51,833 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-24 12:05:54,160 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-24 12:05:54,284 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-24 12:05:54,287 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-24 12:05:54,293 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-24 12:05:54,294 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-24 12:05:54,294 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-24 12:05:54,295 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-24 12:05:54,295 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-24 12:05:54,296 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-24 12:05:54,296 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-24 12:05:54,297 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-24 12:05:54,297 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-24 12:05:54,298 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-24 12:05:54,299 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-24 12:05:54,299 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-24 12:05:54,300 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-24 12:05:54,300 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-24 12:05:54,301 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-24 12:05:54,302 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-24 12:05:54,302 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-24 12:05:54,303 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-24 12:05:54,303 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-24 12:05:54,304 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-24 12:05:54,304 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-24 12:05:54,305 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-24 12:05:54,305 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-24 12:05:54,305 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-24 12:05:54,306 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-24 12:05:54,307 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-24 12:05:54,308 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-24 12:05:54,309 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-24 12:05:54,310 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 12:05:54,340 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-24 12:05:54,366 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-24 12:05:54,435 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-24 12:05:54,531 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-24 12:05:54,543 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-24 12:05:54,614 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-24 12:05:54,710 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-24 12:05:54,794 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-24 12:05:54,808 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-24 12:05:54,833 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2023-12-31 00:00:00 (2326 days).
2025-09-24 12:05:55,125 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data starts at 2017-08-17 04:00:00
2025-09-24 12:05:55,930 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data starts at 2017-08-17 04:00:00
2025-09-24 12:05:56,120 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 5m, spot between two candles of 48.50% detected.
2025-09-24 12:05:56,603 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data starts at 2017-12-13 03:30:00
2025-09-24 12:05:57,363 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-24 12:05:58,166 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data starts at 2017-11-06 03:50:00
2025-09-24 12:05:58,546 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 5m, spot between two candles of 23.53% detected.
2025-09-24 12:06:01,553 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-24 12:06:01,589 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-24 12:06:01,591 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-24 12:06:01,592 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-24 12:06:01,593 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-24 12:06:01,593 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-24 12:06:01,594 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_adx_threshold = 20
2025-09-24 12:06:01,594 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-24 12:06:01,595 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-24 12:06:01,596 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-24 12:06:01,596 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-24 12:06:01,597 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-24 12:06:01,597 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-09-24 12:06:01,598 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-09-24 12:06:01,598 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-24 12:06:01,599 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-24 12:06:01,599 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-24 12:06:01,600 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-24 12:06:01,601 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): custom_sell_atr_factor = 4.5
2025-09-24 12:06:01,601 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-24 12:06:01,602 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 8
2025-09-24 12:06:01,602 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-24 12:06:01,603 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-24 12:06:01,604 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-24 12:06:01,606 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-24 12:06:01,608 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_sell_ichimoku_cloud_signal = True
2025-09-24 12:06:01,609 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_sell_ichimoku_futur_cloud_signal = False
2025-09-24 12:06:01,610 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_sell_kinjun_signal = False
2025-09-24 12:06:01,611 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-24 12:06:01,612 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-24 12:06:01,616 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 12:06:01,647 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-24 12:06:01,684 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 12:06:01,727 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data starts at 2017-08-17 04:00:00
2025-09-24 12:06:23,202 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 12:06:23,220 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-24 12:06:23,238 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 12:06:23,264 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data starts at 2017-08-17 04:00:00
2025-09-24 12:06:23,269 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 4h, spot between two candles of 48.50% detected.
2025-09-24 12:06:42,165 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 12:06:42,183 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-24 12:06:42,200 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 12:06:42,224 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data starts at 2017-12-13 00:00:00
2025-09-24 12:07:02,451 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 12:07:02,477 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-24 12:07:02,505 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 12:07:02,537 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data starts at 2018-05-04 08:00:00
2025-09-24 12:07:19,490 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 12:07:19,510 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-24 12:07:19,530 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-24 12:07:19,572 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data starts at 2017-11-06 00:00:00
2025-09-24 12:07:19,581 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 4h, spot between two candles of 23.53% detected.
2025-09-24 12:07:36,704 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2017-08-17 04:00:00 up to 2023-12-31 00:00:00 (2326 days).
2025-09-24 12:13:58,420 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-24_12-13-58.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │    147 │         1.51 │        1962.158 │       196.22 │ 2 days, 14:21:00 │   62     0    85  42.2 │
│ ETH/USDT │    121 │         1.76 │        1826.888 │       182.69 │ 2 days, 15:02:00 │   54     0    67  44.6 │
│ BNB/USDT │    103 │         1.51 │         700.066 │        70.01 │ 2 days, 10:41:00 │   40     0    63  38.8 │
│ XRP/USDT │     90 │         0.77 │          60.880 │         6.09 │  1 day, 19:13:00 │   19     0    71  21.1 │
│ LTC/USDT │     91 │        -0.44 │        -333.916 │       -33.39 │  2 days, 4:14:00 │   30     0    61  33.0 │
│    TOTAL │    552 │         1.12 │        4216.076 │       421.61 │  2 days, 9:02:00 │  205     0   347  37.1 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                       ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │     406 │         0.98 │        2499.858 │       249.99 │ 2 days, 9:19:00 │  150     0   256  36.9 │
│         hammer_rebond │     101 │         1.21 │         982.009 │         98.2 │ 2 days, 7:39:00 │   38     0    63  37.6 │
│      engulfing_rebond │      45 │          2.2 │         734.209 │        73.42 │ 2 days, 9:32:00 │   17     0    28  37.8 │
│                 TOTAL │     552 │         1.12 │        4216.076 │       421.61 │ 2 days, 9:02:00 │  205     0   347  37.1 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                         EXIT REASON STATS                                                         
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                 Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│              take_profit_3R │    61 │        18.31 │        8562.692 │       856.27 │ 3 days, 16:13:00 │   61     0     0   100 │
│                   stop_loss │    37 │        -6.16 │       -2092.245 │      -209.22 │         14:38:00 │    0     0    37     0 │
│ ichimoku_cloud_crossed_exit │   454 │         -0.6 │       -2254.371 │      -225.44 │  2 days, 8:18:00 │  144     0   310  31.7 │
│                       TOTAL │   552 │         1.12 │        4216.076 │       421.61 │  2 days, 9:02:00 │  205     0   347  37.1 │
└─────────────────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                                      MIXED TAG STATS                                                                       
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃                 Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │              take_profit_3R │     45 │         17.9 │        6073.657 │       607.37 │ 3 days, 16:17:00 │   45     0     0   100 │
│         hammer_rebond │              take_profit_3R │      9 │        19.15 │        1565.337 │       156.53 │ 3 days, 14:44:00 │    9     0     0   100 │
│      engulfing_rebond │              take_profit_3R │      7 │        19.82 │         923.699 │        92.37 │ 3 days, 17:48:00 │    7     0     0   100 │
│      engulfing_rebond │                   stop_loss │      1 │        -3.18 │         -14.891 │        -1.49 │          3:35:00 │    0     0     1     0 │
│      engulfing_rebond │ ichimoku_cloud_crossed_exit │     37 │        -0.99 │        -174.598 │       -17.46 │  2 days, 4:54:00 │   10     0    27  27.0 │
│         hammer_rebond │ ichimoku_cloud_crossed_exit │     84 │         0.17 │        -225.989 │        -22.6 │  2 days, 8:26:00 │   29     0    55  34.5 │
│         hammer_rebond │                   stop_loss │      8 │         -8.1 │        -357.340 │       -35.73 │         12:35:00 │    0     0     8     0 │
│ strong_bullish_rebond │                   stop_loss │     28 │        -5.72 │       -1720.015 │       -172.0 │         15:37:00 │    0     0    28     0 │
│ strong_bullish_rebond │ ichimoku_cloud_crossed_exit │    333 │        -0.75 │       -1853.784 │      -185.38 │  2 days, 8:39:00 │  105     0   228  31.5 │
│                 TOTAL │                             │    552 │         1.12 │        4216.076 │       421.61 │  2 days, 9:02:00 │  205     0   347  37.1 │
└───────────────────────┴─────────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2017-08-17 04:00:00            │
│ Backtesting to                │ 2023-12-31 00:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 552 / 0.24                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 5216.076 USDT                  │
│ Absolute profit               │ 4216.076 USDT                  │
│ Total profit %                │ 421.61%                        │
│ CAGR %                        │ 29.59%                         │
│ Sortino                       │ 1.45                           │
│ Sharpe                        │ 0.52                           │
│ Calmar                        │ 14.93                          │
│ SQN                           │ 2.68                           │
│ Profit factor                 │ 1.44                           │
│ Expectancy (Ratio)            │ 7.64 (0.28)                    │
│ Avg. daily profit             │ 1.813 USDT                     │
│ Avg. stake amount             │ 988.446 USDT                   │
│ Total trade volume            │ 1097653.133 USDT               │
│                               │                                │
│ Best Pair                     │ BTC/USDT 196.22%               │
│ Worst Pair                    │ LTC/USDT -33.39%               │
│ Best trade                    │ XRP/USDT 65.72%                │
│ Worst trade                   │ ETH/USDT -17.44%               │
│ Best day                      │ 303.971 USDT                   │
│ Worst day                     │ -204.046 USDT                  │
│ Days win/draw/lose            │ 158 / 1863 / 255               │
│ Min/Max/Avg. Duration Winners │ 0d 03:55 / 9d 20:25 / 3d 20:12 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 4d 10:00 / 1d 12:15 │
│ Max Consecutive Wins / Loss   │ 8 / 15                         │
│ Rejected Entry signals        │ 1056                           │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 994.956 USDT                   │
│ Max balance                   │ 5540.194 USDT                  │
│ Max % of account underwater   │ 23.20%                         │
│ Absolute drawdown             │ 1285.217 USDT (23.20%)         │
│ Drawdown duration             │ 545 days 01:00:00              │
│ Profit at drawdown start      │ 4540.194 USDT                  │
│ Profit at drawdown end        │ 3254.977 USDT                  │
│ Drawdown start                │ 2022-03-31 14:00:00            │
│ Drawdown end                  │ 2023-09-27 15:00:00            │
│ Market change                 │ 4006.86%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2017-08-17 04:00:00 -> 2023-12-31 00:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃              Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    552 │         1.12 │        4216.076 │       421.61 │ 2 days, 9:02:00 │  205     0   347  37.1 │ 1285.217 USDT  23.20% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴───────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-24T14:14:00.444496",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 6274,
  "total_daily_avg_trades": "552 / 0.24",
  "absolute_profit_usdt": 4216.076,
  "total_profit_pct": 421.61,
  "cagr_pct": 29.59,
  "sortino": 1.45,
  "sharpe": 0.52,
  "calmar": 14.93,
  "sqn": 2.68,
  "max_consecutive_wins_loss": "8 / 15",
  "min_balance_usdt": 994.956,
  "max_balance_usdt": 5540.194,
  "absolute_drawdown_pct": 23.2,
  "market_change_pct": 4006.86,
  "win_draw_loss_winpct": "0 0 0 0"
}
```
