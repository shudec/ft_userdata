# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 5417  
**Timestamp:** 2025-09-25 10:03:49

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 5417,
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
2025-09-25 07:50:00,383 - freqtrade - INFO - freqtrade 2025.8
2025-09-25 07:50:00,771 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-25 07:50:02,324 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-25 07:50:02,330 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-25 07:50:02,330 - freqtrade.loggers - INFO - Logfile configured
2025-09-25 07:50:02,331 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-25 07:50:02,331 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-25 07:50:02,332 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-25 07:50:02,332 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-25 07:50:02,332 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20231231 ...
2025-09-25 07:50:02,814 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-25 07:50:02,817 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-25 07:50:02,818 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-25 07:50:02,818 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-25 07:50:02,819 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-25 07:50:02,819 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20231231
2025-09-25 07:50:02,820 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-25 07:50:02,833 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-25 07:50:02,834 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 07:50:02,836 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-25 07:50:02,837 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-25 07:50:02,837 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-25 07:50:02,863 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-25 07:50:05,258 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-25 07:50:05,354 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-25 07:50:05,357 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-25 07:50:05,362 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-25 07:50:05,363 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-25 07:50:05,363 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-25 07:50:05,363 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-25 07:50:05,364 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-25 07:50:05,364 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-25 07:50:05,365 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-25 07:50:05,365 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-25 07:50:05,365 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-25 07:50:05,366 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-25 07:50:05,366 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-25 07:50:05,367 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-25 07:50:05,367 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-25 07:50:05,368 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-25 07:50:05,368 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-25 07:50:05,369 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-25 07:50:05,370 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-25 07:50:05,370 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-25 07:50:05,371 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-25 07:50:05,372 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-25 07:50:05,372 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-25 07:50:05,373 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-25 07:50:05,374 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-25 07:50:05,375 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-25 07:50:05,376 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-25 07:50:05,377 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-25 07:50:05,377 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-25 07:50:05,378 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-25 07:50:05,378 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 07:50:05,398 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-25 07:50:05,425 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-25 07:50:05,485 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-25 07:50:05,572 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-25 07:50:05,584 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-25 07:50:05,644 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-25 07:50:05,721 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-25 07:50:05,793 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-25 07:50:05,805 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-25 07:50:05,827 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2023-12-31 00:00:00 (2326 days).
2025-09-25 07:50:06,074 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data starts at 2017-08-17 04:00:00
2025-09-25 07:50:06,632 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data starts at 2017-08-17 04:00:00
2025-09-25 07:50:06,796 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 5m, spot between two candles of 48.50% detected.
2025-09-25 07:50:07,213 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data starts at 2017-12-13 03:30:00
2025-09-25 07:50:07,769 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-25 07:50:08,435 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data starts at 2017-11-06 03:50:00
2025-09-25 07:50:08,625 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 5m, spot between two candles of 23.53% detected.
2025-09-25 07:50:11,217 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-25 07:50:11,236 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-25 07:50:11,237 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-25 07:50:11,238 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-25 07:50:11,238 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-25 07:50:11,238 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-25 07:50:11,239 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 10
2025-09-25 07:50:11,239 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-25 07:50:11,239 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-25 07:50:11,240 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-25 07:50:11,241 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-25 07:50:11,242 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.007
2025-09-25 07:50:11,243 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-25 07:50:11,245 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-25 07:50:11,246 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-25 07:50:11,246 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.007
2025-09-25 07:50:11,247 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.25
2025-09-25 07:50:11,247 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1.5
2025-09-25 07:50:11,249 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-09-25 07:50:11,250 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.998
2025-09-25 07:50:11,250 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 1
2025-09-25 07:50:11,251 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.996
2025-09-25 07:50:11,252 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-25 07:50:11,252 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-25 07:50:11,253 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = none
2025-09-25 07:50:11,254 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = False
2025-09-25 07:50:11,254 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-25 07:50:11,255 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-25 07:50:11,255 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-25 07:50:11,256 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-25 07:50:11,260 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 07:50:11,279 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-25 07:50:11,303 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 07:50:11,329 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data starts at 2017-08-17 04:00:00
2025-09-25 07:50:22,819 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 07:50:22,834 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-25 07:50:22,851 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 07:50:22,875 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data starts at 2017-08-17 04:00:00
2025-09-25 07:50:22,880 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 4h, spot between two candles of 48.50% detected.
2025-09-25 07:50:41,676 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 07:50:41,697 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-25 07:50:41,720 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 07:50:41,749 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data starts at 2017-12-13 00:00:00
2025-09-25 07:50:54,578 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 07:50:54,596 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-25 07:50:54,612 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 07:50:54,635 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data starts at 2018-05-04 08:00:00
2025-09-25 07:51:04,566 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 07:51:04,582 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-25 07:51:04,598 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 07:51:04,621 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data starts at 2017-11-06 00:00:00
2025-09-25 07:51:04,625 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 4h, spot between two candles of 23.53% detected.
2025-09-25 07:51:15,461 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2017-08-17 04:00:00 up to 2023-12-31 00:00:00 (2326 days).
2025-09-25 08:03:47,166 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-25_08-03-47.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │    175 │         1.56 │        5489.932 │       548.99 │ 4 days, 13:14:00 │   58     0   117  33.1 │
│ BNB/USDT │    163 │         1.94 │        4709.409 │       470.94 │ 4 days, 13:03:00 │   56     0   107  34.4 │
│ LTC/USDT │    115 │         0.97 │        1587.734 │       158.77 │ 3 days, 18:34:00 │   34     0    81  29.6 │
│ BTC/USDT │    138 │         1.86 │        1508.167 │       150.82 │ 7 days, 15:22:00 │   47     0    91  34.1 │
│ XRP/USDT │    102 │        -0.46 │       -2205.476 │      -220.55 │ 3 days, 10:56:00 │   23     0    79  22.5 │
│    TOTAL │    693 │         1.31 │       11089.766 │      1108.98 │ 4 days, 20:59:00 │  218     0   475  31.5 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │      1 │         1.77 │          35.595 │         3.56 │ 11 days, 22:00:00 │    1     0     0   100 │
│ BTC/USDT │      1 │        -1.32 │         -56.943 │        -5.69 │  12 days, 2:00:00 │    0     0     1     0 │
│ XRP/USDT │      1 │        -3.09 │        -150.098 │       -15.01 │  2 days, 23:00:00 │    0     0     1     0 │
│    TOTAL │      3 │        -0.88 │        -171.446 │       -17.14 │  8 days, 23:40:00 │    1     0     2  33.3 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                        ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│      engulfing_rebond │      58 │         3.56 │        6195.138 │       619.51 │  5 days, 5:42:00 │   25     0    33  43.1 │
│         hammer_rebond │     123 │         2.18 │        3995.205 │       399.52 │  4 days, 5:48:00 │   44     0    79  35.8 │
│ strong_bullish_rebond │     512 │         0.85 │         899.423 │        89.94 │ 4 days, 23:38:00 │  149     0   363  29.1 │
│                 TOTAL │     693 │         1.31 │       11089.766 │      1108.98 │ 4 days, 20:59:00 │  218     0   475  31.5 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │   217 │        15.53 │       77699.219 │      7769.92 │  7 days, 3:04:00 │  217     0     0   100 │
│     force_exit │     3 │        -0.88 │        -171.446 │       -17.14 │ 8 days, 23:40:00 │    1     0     2  33.3 │
│      stop_loss │   473 │        -5.19 │      -66438.007 │      -6643.8 │ 3 days, 19:33:00 │    0     0   473     0 │
│          TOTAL │   693 │         1.31 │       11089.766 │      1108.98 │ 4 days, 20:59:00 │  218     0   475  31.5 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                                MIXED TAG STATS                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_3R │    149 │        15.54 │       52073.729 │      5207.37 │  7 days, 11:54:00 │  149     0     0   100 │
│         hammer_rebond │ take_profit_3R │     44 │         15.4 │       14940.792 │      1494.08 │  6 days, 11:41:00 │   44     0     0   100 │
│      engulfing_rebond │ take_profit_3R │     24 │        15.67 │       10684.698 │      1068.47 │   6 days, 0:24:00 │   24     0     0   100 │
│      engulfing_rebond │     force_exit │      1 │         1.77 │          35.595 │         3.56 │ 11 days, 22:00:00 │    1     0     0   100 │
│ strong_bullish_rebond │     force_exit │      2 │        -2.21 │        -207.041 │        -20.7 │  7 days, 12:30:00 │    0     0     2     0 │
│      engulfing_rebond │      stop_loss │     33 │        -5.19 │       -4525.155 │      -452.52 │  4 days, 11:15:00 │    0     0    33     0 │
│         hammer_rebond │      stop_loss │     79 │        -5.19 │      -10945.587 │     -1094.56 │  2 days, 23:46:00 │    0     0    79     0 │
│ strong_bullish_rebond │      stop_loss │    361 │        -5.19 │      -50967.265 │     -5096.73 │  3 days, 22:26:00 │    0     0   361     0 │
│                 TOTAL │                │    693 │         1.31 │       11089.766 │      1108.98 │  4 days, 20:59:00 │  218     0   475  31.5 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2017-08-17 04:00:00             │
│ Backtesting to                │ 2023-12-31 00:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 693 / 0.3                       │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 12089.766 USDT                  │
│ Absolute profit               │ 11089.766 USDT                  │
│ Total profit %                │ 1108.98%                        │
│ CAGR %                        │ 47.86%                          │
│ Sortino                       │ 0.73                            │
│ Sharpe                        │ 0.29                            │
│ Calmar                        │ 14.71                           │
│ SQN                           │ 1.35                            │
│ Profit factor                 │ 1.17                            │
│ Expectancy (Ratio)            │ 16.00 (0.11)                    │
│ Avg. daily profit             │ 4.768 USDT                      │
│ Avg. stake amount             │ 2582.443 USDT                   │
│ Total trade volume            │ 3597544.281 USDT                │
│                               │                                 │
│ Best Pair                     │ ETH/USDT 548.99%                │
│ Worst Pair                    │ XRP/USDT -220.55%               │
│ Best trade                    │ BNB/USDT 20.05%                 │
│ Worst trade                   │ BNB/USDT -5.80%                 │
│ Best day                      │ 2514.867 USDT                   │
│ Worst day                     │ -1255.158 USDT                  │
│ Days win/draw/lose            │ 174 / 1788 / 317                │
│ Min/Max/Avg. Duration Winners │ 0d 02:30 / 75d 02:55 / 7d 03:35 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 84d 00:00 / 3d 19:55 │
│ Max Consecutive Wins / Loss   │ 8 / 31                          │
│ Rejected Entry signals        │ 11811                           │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 979.429 USDT                    │
│ Max balance                   │ 24658.928 USDT                  │
│ Max % of account underwater   │ 61.90%                          │
│ Absolute drawdown             │ 15264.911 USDT (61.90%)         │
│ Drawdown duration             │ 703 days 04:10:00               │
│ Profit at drawdown start      │ 23658.928 USDT                  │
│ Profit at drawdown end        │ 8394.018 USDT                   │
│ Drawdown start                │ 2021-11-07 02:00:00             │
│ Drawdown end                  │ 2023-10-11 06:10:00             │
│ Market change                 │ 4006.86%                        │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2017-08-17 04:00:00 -> 2023-12-31 00:00:00 | Max open trades : 3
                                                                    STRATEGY SUMMARY                                                                    
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃               Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    693 │         1.31 │       11089.766 │      1108.98 │ 4 days, 20:59:00 │  218     0   475  31.5 │ 15264.911 USDT  61.90% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┴────────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-25T10:03:49.014022",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 5417,
  "total_daily_avg_trades": "693 / 0.3",
  "absolute_profit_usdt": 11089.766,
  "total_profit_pct": 1108.98,
  "cagr_pct": 47.86,
  "sortino": 0.73,
  "sharpe": 0.29,
  "calmar": 14.71,
  "sqn": 1.35,
  "max_consecutive_wins_loss": "8 / 31",
  "min_balance_usdt": 979.429,
  "max_balance_usdt": 24658.928,
  "absolute_drawdown_pct": 61.9,
  "market_change_pct": 4006.86
}
```
