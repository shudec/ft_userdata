# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 6375  
**Timestamp:** 2025-09-25 10:53:36

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 6375,
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
2025-09-25 08:26:40,002 - freqtrade - INFO - freqtrade 2025.8
2025-09-25 08:26:40,788 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-25 08:26:44,390 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-25 08:26:44,399 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-25 08:26:44,399 - freqtrade.loggers - INFO - Logfile configured
2025-09-25 08:26:44,400 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-25 08:26:44,401 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-25 08:26:44,401 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-25 08:26:44,401 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-25 08:26:44,402 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20231231 ...
2025-09-25 08:26:45,050 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-25 08:26:45,053 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-25 08:26:45,053 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-25 08:26:45,054 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-25 08:26:45,055 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-25 08:26:45,055 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20231231
2025-09-25 08:26:45,057 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-25 08:26:45,074 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-25 08:26:45,075 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 08:26:45,079 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-25 08:26:45,080 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-25 08:26:45,081 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-25 08:26:45,113 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-25 08:26:47,602 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-25 08:26:47,710 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-25 08:26:47,712 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-25 08:26:47,717 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-25 08:26:47,718 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-25 08:26:47,719 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-25 08:26:47,719 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-25 08:26:47,720 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-25 08:26:47,720 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-25 08:26:47,721 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-25 08:26:47,721 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-25 08:26:47,722 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-25 08:26:47,722 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-25 08:26:47,723 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-25 08:26:47,723 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-25 08:26:47,724 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-25 08:26:47,724 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-25 08:26:47,725 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-25 08:26:47,725 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-25 08:26:47,726 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-25 08:26:47,726 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-25 08:26:47,727 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-25 08:26:47,727 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-25 08:26:47,728 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-25 08:26:47,728 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-25 08:26:47,729 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-25 08:26:47,729 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-25 08:26:47,729 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-25 08:26:47,730 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-25 08:26:47,730 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-25 08:26:47,730 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-25 08:26:47,731 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 08:26:47,757 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-25 08:26:47,787 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-25 08:26:47,851 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-25 08:26:47,974 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-25 08:26:47,985 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-25 08:26:48,047 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-25 08:26:48,115 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-25 08:26:48,183 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-25 08:26:48,198 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-25 08:26:48,223 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2023-12-31 00:00:00 (2326 days).
2025-09-25 08:26:48,548 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data starts at 2017-08-17 04:00:00
2025-09-25 08:26:49,200 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data starts at 2017-08-17 04:00:00
2025-09-25 08:26:49,398 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 5m, spot between two candles of 48.50% detected.
2025-09-25 08:26:49,914 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data starts at 2017-12-13 03:30:00
2025-09-25 08:26:50,523 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-25 08:26:51,159 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data starts at 2017-11-06 03:50:00
2025-09-25 08:26:51,421 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 5m, spot between two candles of 23.53% detected.
2025-09-25 08:26:53,698 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-25 08:26:53,717 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-25 08:26:53,718 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-25 08:26:53,719 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-25 08:26:53,719 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-25 08:26:53,719 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-25 08:26:53,720 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 10
2025-09-25 08:26:53,720 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-25 08:26:53,721 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-25 08:26:53,721 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-25 08:26:53,721 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-25 08:26:53,722 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.007
2025-09-25 08:26:53,722 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-25 08:26:53,722 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-25 08:26:53,723 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-25 08:26:53,723 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.007
2025-09-25 08:26:53,724 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.25
2025-09-25 08:26:53,725 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1.5
2025-09-25 08:26:53,725 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-09-25 08:26:53,725 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.998
2025-09-25 08:26:53,726 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 1
2025-09-25 08:26:53,726 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.996
2025-09-25 08:26:53,727 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-25 08:26:53,727 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = False
2025-09-25 08:26:53,727 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-25 08:26:53,728 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = none
2025-09-25 08:26:53,728 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = False
2025-09-25 08:26:53,729 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-25 08:26:53,730 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-25 08:26:53,730 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-25 08:26:53,731 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-25 08:26:53,734 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 08:26:53,755 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-25 08:26:53,783 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 08:26:53,810 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data starts at 2017-08-17 04:00:00
2025-09-25 08:27:05,959 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 08:27:05,976 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-25 08:27:05,995 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 08:27:06,020 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data starts at 2017-08-17 04:00:00
2025-09-25 08:27:06,026 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 4h, spot between two candles of 48.50% detected.
2025-09-25 08:27:18,222 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 08:27:18,241 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-25 08:27:18,262 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 08:27:18,292 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data starts at 2017-12-13 00:00:00
2025-09-25 08:27:30,443 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 08:27:30,460 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-25 08:27:30,476 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 08:27:30,507 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data starts at 2018-05-04 08:00:00
2025-09-25 08:27:40,928 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 08:27:40,943 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-25 08:27:40,958 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 08:27:40,981 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data starts at 2017-11-06 00:00:00
2025-09-25 08:27:40,985 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 4h, spot between two candles of 23.53% detected.
2025-09-25 08:27:52,873 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2017-08-17 04:00:00 up to 2023-12-31 00:00:00 (2326 days).
2025-09-25 08:53:35,035 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-25_08-53-34.meta.json"
Result for strategy IchimokuRebondStrategy
                                                BACKTESTING REPORT                                                 
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃       Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      4 │      2747.56 │       14811.077 │      1481.11 │  552 days, 3:48:00 │    1     0     3  25.0 │
│ ETH/USDT │     11 │       121.09 │        2539.849 │       253.98 │  188 days, 7:35:00 │    1     0    10   9.1 │
│ BTC/USDT │      7 │        67.04 │         951.334 │        95.13 │ 256 days, 14:25:00 │    1     0     6  14.3 │
│ XRP/USDT │      4 │        -5.19 │         -62.061 │        -6.21 │  19 days, 15:14:00 │    0     0     4     0 │
│ LTC/USDT │      8 │        -5.19 │        -115.613 │       -11.56 │  51 days, 20:07:00 │    0     0     8     0 │
│    TOTAL │     34 │       374.39 │       18124.587 │      1812.46 │  193 days, 5:20:00 │    3     0    31   8.8 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────────┴────────────────────────┘
                                              LEFT OPEN TRADES REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃        Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │     11006.43 │       14835.450 │      1483.54 │ 2207 days, 11:55:00 │    1     0     0   100 │
│ ETH/USDT │      1 │      1383.88 │        2701.761 │       270.18 │ 1363 days, 14:00:00 │    1     0     0   100 │
│ BTC/USDT │      1 │       500.41 │        1043.824 │       104.38 │  1353 days, 7:00:00 │    1     0     0   100 │
│    TOTAL │      3 │       4296.9 │       18581.035 │       1858.1 │ 1641 days, 10:58:00 │    3     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────────┴────────────────────────┘
                                                         ENTER TAG STATS                                                         
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃       Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │      28 │       437.67 │       17140.261 │      1714.03 │ 185 days, 17:56:00 │    2     0    26   7.1 │
│         hammer_rebond │       5 │        95.93 │         996.717 │        99.67 │  273 days, 5:21:00 │    1     0     4  20.0 │
│      engulfing_rebond │       1 │        -5.19 │         -12.391 │        -1.24 │   2 days, 12:35:00 │    0     0     1     0 │
│                 TOTAL │      34 │       374.39 │       18124.587 │      1812.46 │  193 days, 5:20:00 │    3     0    31   8.8 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴────────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃        Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  force_exit │     3 │       4296.9 │       18581.035 │       1858.1 │ 1641 days, 10:58:00 │    3     0     0   100 │
│   stop_loss │    31 │        -5.21 │        -456.448 │       -45.64 │    53 days, 1:41:00 │    0     0    31     0 │
│       TOTAL │    34 │       374.39 │       18124.587 │      1812.46 │   193 days, 5:20:00 │    3     0    31   8.8 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────────┴────────────────────────┘
                                                                MIXED TAG STATS                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃        Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │  force_exit │      2 │      6195.15 │       17537.211 │      1753.72 │ 1785 days, 12:58:00 │    2     0     0   100 │
│         hammer_rebond │  force_exit │      1 │       500.41 │        1043.824 │       104.38 │  1353 days, 7:00:00 │    1     0     0   100 │
│      engulfing_rebond │   stop_loss │      1 │        -5.19 │         -12.391 │        -1.24 │    2 days, 12:35:00 │    0     0     1     0 │
│         hammer_rebond │   stop_loss │      4 │        -5.19 │         -47.108 │        -4.71 │     3 days, 4:56:00 │    0     0     4     0 │
│ strong_bullish_rebond │   stop_loss │     26 │        -5.21 │        -396.950 │       -39.69 │   62 days, 16:28:00 │    0     0    26     0 │
│                 TOTAL │             │     34 │       374.39 │       18124.587 │      1812.46 │   193 days, 5:20:00 │    3     0    31   8.8 │
└───────────────────────┴─────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────────┴────────────────────────┘
                              SUMMARY METRICS                              
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                                   ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2017-08-17 04:00:00                     │
│ Backtesting to                │ 2023-12-31 00:00:00                     │
│ Trading Mode                  │ Spot                                    │
│ Max open trades               │ 3                                       │
│                               │                                         │
│ Total/Daily Avg Trades        │ 34 / 0.01                               │
│ Starting balance              │ 1000 USDT                               │
│ Final balance                 │ 19124.587 USDT                          │
│ Absolute profit               │ 18124.587 USDT                          │
│ Total profit %                │ 1812.46%                                │
│ CAGR %                        │ 58.89%                                  │
│ Sortino                       │ 43.03                                   │
│ Sharpe                        │ 0.06                                    │
│ Calmar                        │ 32.61                                   │
│ SQN                           │ 1.21                                    │
│ Profit factor                 │ 40.71                                   │
│ Expectancy (Ratio)            │ 533.08 (36.20)                          │
│ Avg. daily profit             │ 7.792 USDT                              │
│ Avg. stake amount             │ 273.704 USDT                            │
│ Total trade volume            │ 36810.002 USDT                          │
│                               │                                         │
│ Best Pair                     │ BNB/USDT 1481.11%                       │
│ Worst Pair                    │ LTC/USDT -11.56%                        │
│ Best trade                    │ BNB/USDT 11006.43%                      │
│ Worst trade                   │ BNB/USDT -5.80%                         │
│ Best day                      │ 18581.035 USDT                          │
│ Worst day                     │ -31.192 USDT                            │
│ Days win/draw/lose            │ 1 / 2252 / 26                           │
│ Min/Max/Avg. Duration Winners │ 1353d 07:00 / 2207d 11:55 / 1641d 10:58 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 414d 15:20 / 53d 01:41       │
│ Max Consecutive Wins / Loss   │ 3 / 31                                  │
│ Rejected Entry signals        │ 17400                                   │
│ Entry/Exit Timeouts           │ 0 / 0                                   │
│                               │                                         │
│ Min balance                   │ 543.552 USDT                            │
│ Max balance                   │ 19124.587 USDT                          │
│ Max % of account underwater   │ 45.64%                                  │
│ Absolute drawdown             │ 456.448 USDT (45.64%)                   │
│ Drawdown duration             │ 923 days 19:50:00                       │
│ Profit at drawdown start      │ -20.571 USDT                            │
│ Profit at drawdown end        │ -456.448 USDT                           │
│ Drawdown start                │ 2017-10-05 04:30:00                     │
│ Drawdown end                  │ 2020-04-16 00:20:00                     │
│ Market change                 │ 4006.86%                                │
└───────────────────────────────┴─────────────────────────────────────────┘

Backtested 2017-08-17 04:00:00 -> 2023-12-31 00:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                    
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     34 │       374.39 │       18124.587 │      1812.46 │ 193 days, 5:20:00 │    3     0    31   8.8 │ 456.448 USDT  45.64% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-25T10:53:36.782966",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 6375,
  "total_daily_avg_trades": "34 / 0.01",
  "absolute_profit_usdt": 18124.587,
  "total_profit_pct": 1812.46,
  "cagr_pct": 58.89,
  "sortino": 43.03,
  "sharpe": 0.06,
  "calmar": 32.61,
  "sqn": 1.21,
  "max_consecutive_wins_loss": "3 / 31",
  "min_balance_usdt": 543.552,
  "max_balance_usdt": 19124.587,
  "absolute_drawdown_pct": 45.64,
  "market_change_pct": 4006.86
}
```
