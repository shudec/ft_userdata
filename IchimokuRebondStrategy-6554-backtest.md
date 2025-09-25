# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 6554  
**Timestamp:** 2025-09-25 09:42:38

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 6554,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20231231",
  "backtest_timerange": "20170801-20231231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20231231
```

## Backtesting Output
```
2025-09-25 07:33:17,083 - freqtrade - INFO - freqtrade 2025.8
2025-09-25 07:33:17,907 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-25 07:33:20,852 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-25 07:33:20,861 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-25 07:33:20,862 - freqtrade.loggers - INFO - Logfile configured
2025-09-25 07:33:20,862 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-25 07:33:20,863 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-25 07:33:20,864 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-25 07:33:20,864 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-25 07:33:20,865 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20231231 ...
2025-09-25 07:33:21,447 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-25 07:33:21,450 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-25 07:33:21,451 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-25 07:33:21,452 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-25 07:33:21,452 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-25 07:33:21,453 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20231231
2025-09-25 07:33:21,454 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-25 07:33:21,468 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-25 07:33:21,469 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 07:33:21,472 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-25 07:33:21,473 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-25 07:33:21,473 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-25 07:33:21,500 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-25 07:33:25,055 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-25 07:33:25,239 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-25 07:33:25,242 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-25 07:33:25,250 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-25 07:33:25,251 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-25 07:33:25,251 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-25 07:33:25,252 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-25 07:33:25,253 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-25 07:33:25,254 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-25 07:33:25,255 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-25 07:33:25,255 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-25 07:33:25,256 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-25 07:33:25,257 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-25 07:33:25,257 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-25 07:33:25,259 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-25 07:33:25,260 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-25 07:33:25,261 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-25 07:33:25,263 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-25 07:33:25,264 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-25 07:33:25,264 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-25 07:33:25,265 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-25 07:33:25,265 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-25 07:33:25,267 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-25 07:33:25,267 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-25 07:33:25,268 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-25 07:33:25,269 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-25 07:33:25,270 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-25 07:33:25,271 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-25 07:33:25,272 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-25 07:33:25,273 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-25 07:33:25,273 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-25 07:33:25,274 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 07:33:25,320 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-25 07:33:25,356 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-25 07:33:25,540 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-25 07:33:25,734 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-25 07:33:25,752 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-25 07:33:25,833 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-25 07:33:25,924 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-25 07:33:26,010 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-25 07:33:26,028 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-25 07:33:26,060 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2023-12-31 00:00:00 (2326 days).
2025-09-25 07:33:26,700 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data starts at 2017-08-17 04:00:00
2025-09-25 07:33:27,562 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data starts at 2017-08-17 04:00:00
2025-09-25 07:33:27,746 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 5m, spot between two candles of 48.50% detected.
2025-09-25 07:33:28,186 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data starts at 2017-12-13 03:30:00
2025-09-25 07:33:28,735 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-25 07:33:29,262 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data starts at 2017-11-06 03:50:00
2025-09-25 07:33:29,434 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 5m, spot between two candles of 23.53% detected.
2025-09-25 07:33:31,419 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-25 07:33:31,447 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-25 07:33:31,448 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-25 07:33:31,448 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-25 07:33:31,448 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-25 07:33:31,449 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-25 07:33:31,449 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 10
2025-09-25 07:33:31,450 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-25 07:33:31,450 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-25 07:33:31,451 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-25 07:33:31,452 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-25 07:33:31,452 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.007
2025-09-25 07:33:31,453 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-25 07:33:31,454 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-25 07:33:31,454 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-25 07:33:31,455 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.007
2025-09-25 07:33:31,455 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.25
2025-09-25 07:33:31,456 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1.5
2025-09-25 07:33:31,456 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-09-25 07:33:31,457 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.998
2025-09-25 07:33:31,457 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 1
2025-09-25 07:33:31,458 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.996
2025-09-25 07:33:31,458 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-25 07:33:31,459 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-25 07:33:31,459 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = none
2025-09-25 07:33:31,459 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-09-25 07:33:31,460 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-25 07:33:31,460 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-25 07:33:31,461 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-25 07:33:31,461 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-25 07:33:31,464 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 07:33:31,483 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-25 07:33:31,508 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 07:33:31,536 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data starts at 2017-08-17 04:00:00
2025-09-25 07:33:42,956 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 07:33:42,986 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-25 07:33:43,017 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 07:33:43,041 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data starts at 2017-08-17 04:00:00
2025-09-25 07:33:43,046 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 4h, spot between two candles of 48.50% detected.
2025-09-25 07:33:55,882 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 07:33:55,900 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-25 07:33:55,917 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 07:33:55,942 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data starts at 2017-12-13 00:00:00
2025-09-25 07:34:06,422 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 07:34:06,436 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-25 07:34:06,451 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 07:34:06,474 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data starts at 2018-05-04 08:00:00
2025-09-25 07:34:16,135 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 07:34:16,150 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-25 07:34:16,167 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 07:34:16,191 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data starts at 2017-11-06 00:00:00
2025-09-25 07:34:16,195 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 4h, spot between two candles of 23.53% detected.
2025-09-25 07:34:27,168 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2017-08-17 04:00:00 up to 2023-12-31 00:00:00 (2326 days).
2025-09-25 07:42:36,434 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-25_07-42-36.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │    266 │          1.0 │        6867.859 │       686.79 │ 1 day, 23:14:00 │   96     0   170  36.1 │
│ BTC/USDT │    261 │         1.18 │        3976.517 │       397.65 │ 2 days, 7:44:00 │   92     0   169  35.2 │
│ BNB/USDT │    245 │         1.15 │        3255.867 │       325.59 │ 1 day, 21:31:00 │   88     0   157  35.9 │
│ XRP/USDT │    161 │         0.28 │        2952.895 │       295.29 │ 1 day, 10:10:00 │   47     0   114  29.2 │
│ LTC/USDT │    187 │         0.14 │        -300.067 │       -30.01 │ 1 day, 18:21:00 │   61     0   126  32.6 │
│    TOTAL │   1120 │         0.83 │       16753.071 │      1675.31 │ 1 day, 22:09:00 │  384     0   736  34.3 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
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
│ strong_bullish_rebond │     856 │         0.73 │        7888.401 │       788.84 │ 1 day, 23:19:00 │  291     0   565  34.0 │
│      engulfing_rebond │      84 │         2.68 │        7209.571 │       720.96 │ 1 day, 23:59:00 │   37     0    47  44.0 │
│         hammer_rebond │     180 │         0.45 │        1655.100 │       165.51 │ 1 day, 15:42:00 │   56     0   124  31.1 │
│                 TOTAL │    1120 │         0.83 │       16753.071 │      1675.31 │ 1 day, 22:09:00 │  384     0   736  34.3 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                         EXIT REASON STATS                                                         
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                 Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│              take_profit_3R │   157 │        15.67 │       59579.757 │      5957.98 │ 2 days, 15:12:00 │  157     0     0   100 │
│ ichimoku_cloud_crossed_exit │   722 │        -0.39 │      -13078.188 │     -1307.82 │  2 days, 4:06:00 │  227     0   495  31.4 │
│                   stop_loss │   241 │        -5.19 │      -29748.498 │     -2974.85 │         17:13:00 │    0     0   241     0 │
│                       TOTAL │  1120 │         0.83 │       16753.071 │      1675.31 │  1 day, 22:09:00 │  384     0   736  34.3 │
└─────────────────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                                      MIXED TAG STATS                                                                       
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃                 Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │              take_profit_3R │    113 │        15.68 │       41395.849 │      4139.58 │ 2 days, 19:32:00 │  113     0     0   100 │
│         hammer_rebond │              take_profit_3R │     25 │        15.63 │       10039.064 │      1003.91 │  2 days, 0:46:00 │   25     0     0   100 │
│      engulfing_rebond │              take_profit_3R │     19 │        15.69 │        8144.844 │       814.48 │  2 days, 8:24:00 │   19     0     0   100 │
│      engulfing_rebond │ ichimoku_cloud_crossed_exit │     55 │        -0.38 │          30.772 │         3.08 │  2 days, 3:21:00 │   18     0    37  32.7 │
│      engulfing_rebond │                   stop_loss │     10 │        -5.19 │        -966.046 │        -96.6 │         13:30:00 │    0     0    10     0 │
│         hammer_rebond │ ichimoku_cloud_crossed_exit │    112 │        -0.77 │       -3826.588 │      -382.66 │  1 day, 22:23:00 │   31     0    81  27.7 │
│         hammer_rebond │                   stop_loss │     43 │        -5.19 │       -4557.376 │      -455.74 │         17:03:00 │    0     0    43     0 │
│ strong_bullish_rebond │ ichimoku_cloud_crossed_exit │    555 │        -0.31 │       -9282.373 │      -928.24 │  2 days, 5:19:00 │  178     0   377  32.1 │
│ strong_bullish_rebond │                   stop_loss │    188 │        -5.19 │      -24225.076 │     -2422.51 │         17:27:00 │    0     0   188     0 │
│                 TOTAL │                             │   1120 │         0.83 │       16753.071 │      1675.31 │  1 day, 22:09:00 │  384     0   736  34.3 │
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
│ Total/Daily Avg Trades        │ 1120 / 0.48                    │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 17753.071 USDT                 │
│ Absolute profit               │ 16753.071 USDT                 │
│ Total profit %                │ 1675.31%                       │
│ CAGR %                        │ 57.05%                         │
│ Sortino                       │ 1.46                           │
│ Sharpe                        │ 0.60                           │
│ Calmar                        │ 41.78                          │
│ SQN                           │ 2.17                           │
│ Profit factor                 │ 1.26                           │
│ Expectancy (Ratio)            │ 14.96 (0.17)                   │
│ Avg. daily profit             │ 7.203 USDT                     │
│ Avg. stake amount             │ 2964.357 USDT                  │
│ Total trade volume            │ 6670240.278 USDT               │
│                               │                                │
│ Best Pair                     │ ETH/USDT 686.79%               │
│ Worst Pair                    │ LTC/USDT -30.01%               │
│ Best trade                    │ XRP/USDT 21.53%                │
│ Worst trade                   │ BNB/USDT -5.80%                │
│ Best day                      │ 2315.454 USDT                  │
│ Worst day                     │ -895.872 USDT                  │
│ Days win/draw/lose            │ 272 / 1569 / 438               │
│ Min/Max/Avg. Duration Winners │ 0d 00:25 / 9d 17:40 / 3d 07:30 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 5d 09:00 / 1d 04:45 │
│ Max Consecutive Wins / Loss   │ 7 / 17                         │
│ Rejected Entry signals        │ 9066                           │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 993.739 USDT                   │
│ Max balance                   │ 19817.986 USDT                 │
│ Max % of account underwater   │ 37.10%                         │
│ Absolute drawdown             │ 6527.232 USDT (32.94%)         │
│ Drawdown duration             │ 241 days 23:00:00              │
│ Profit at drawdown start      │ 18817.986 USDT                 │
│ Profit at drawdown end        │ 12290.755 USDT                 │
│ Drawdown start                │ 2021-11-10 20:00:00            │
│ Drawdown end                  │ 2022-07-10 19:00:00            │
│ Market change                 │ 4006.86%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2017-08-17 04:00:00 -> 2023-12-31 00:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃              Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │   1120 │         0.83 │       16753.071 │      1675.31 │ 1 day, 22:09:00 │  384     0   736  34.3 │ 6527.232 USDT  32.94% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴───────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-25T09:42:38.476620",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 6554,
  "total_daily_avg_trades": "1120 / 0.48",
  "absolute_profit_usdt": 16753.071,
  "total_profit_pct": 1675.31,
  "cagr_pct": 57.05,
  "sortino": 1.46,
  "sharpe": 0.6,
  "calmar": 41.78,
  "sqn": 2.17,
  "max_consecutive_wins_loss": "7 / 17",
  "min_balance_usdt": 993.739,
  "max_balance_usdt": 19817.986,
  "absolute_drawdown_pct": 32.94,
  "market_change_pct": 4006.86,
  "win_draw_loss_winpct": "0 0 0 0"
}
```
