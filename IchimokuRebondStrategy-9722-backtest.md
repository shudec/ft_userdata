# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 9722  
**Timestamp:** 2025-09-25 15:42:36

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 9722,
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
2025-09-25 13:29:08,845 - freqtrade - INFO - freqtrade 2025.8
2025-09-25 13:29:09,149 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-25 13:29:10,709 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-25 13:29:10,715 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-25 13:29:10,715 - freqtrade.loggers - INFO - Logfile configured
2025-09-25 13:29:10,716 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-25 13:29:10,716 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-25 13:29:10,717 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-25 13:29:10,718 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-25 13:29:10,718 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20231231 ...
2025-09-25 13:29:11,235 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-25 13:29:11,238 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-25 13:29:11,239 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-25 13:29:11,240 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-25 13:29:11,240 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-25 13:29:11,241 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20231231
2025-09-25 13:29:11,243 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-25 13:29:11,265 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-25 13:29:11,267 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 13:29:11,272 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-25 13:29:11,273 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-25 13:29:11,274 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-25 13:29:11,306 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-25 13:29:13,719 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-25 13:29:13,803 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-25 13:29:13,805 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-25 13:29:13,810 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-25 13:29:13,810 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-25 13:29:13,810 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-25 13:29:13,811 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-25 13:29:13,811 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-25 13:29:13,811 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-25 13:29:13,812 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-25 13:29:13,812 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-25 13:29:13,812 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-25 13:29:13,813 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-25 13:29:13,813 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-25 13:29:13,813 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-25 13:29:13,813 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-25 13:29:13,814 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-25 13:29:13,814 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-25 13:29:13,814 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-25 13:29:13,815 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-25 13:29:13,815 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-25 13:29:13,815 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-25 13:29:13,815 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-25 13:29:13,816 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-25 13:29:13,816 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-25 13:29:13,816 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-25 13:29:13,817 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-25 13:29:13,817 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-25 13:29:13,818 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-25 13:29:13,818 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-25 13:29:13,818 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-25 13:29:13,819 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 13:29:13,833 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-25 13:29:13,855 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-25 13:29:13,904 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-25 13:29:13,973 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-25 13:29:13,983 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-25 13:29:14,030 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-25 13:29:14,084 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-25 13:29:14,138 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-25 13:29:14,150 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-25 13:29:14,168 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2023-12-31 00:00:00 (2326 days).
2025-09-25 13:29:14,415 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data starts at 2017-08-17 04:00:00
2025-09-25 13:29:14,921 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data starts at 2017-08-17 04:00:00
2025-09-25 13:29:15,068 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 5m, spot between two candles of 48.50% detected.
2025-09-25 13:29:15,429 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data starts at 2017-12-13 03:30:00
2025-09-25 13:29:15,889 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-25 13:29:16,328 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data starts at 2017-11-06 03:50:00
2025-09-25 13:29:16,463 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 5m, spot between two candles of 23.53% detected.
2025-09-25 13:29:18,216 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-25 13:29:18,236 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-25 13:29:18,237 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-25 13:29:18,238 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-25 13:29:18,238 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-25 13:29:18,239 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-25 13:29:18,240 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 5
2025-09-25 13:29:18,240 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-25 13:29:18,241 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-25 13:29:18,241 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-25 13:29:18,242 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-25 13:29:18,242 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.007
2025-09-25 13:29:18,243 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-25 13:29:18,244 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-25 13:29:18,244 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-25 13:29:18,245 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.007
2025-09-25 13:29:18,246 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.25
2025-09-25 13:29:18,247 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 0.5
2025-09-25 13:29:18,247 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 6
2025-09-25 13:29:18,248 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.998
2025-09-25 13:29:18,249 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 2
2025-09-25 13:29:18,250 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.99
2025-09-25 13:29:18,250 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-25 13:29:18,251 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = False
2025-09-25 13:29:18,251 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-25 13:29:18,252 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-25 13:29:18,252 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-09-25 13:29:18,253 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-25 13:29:18,253 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-25 13:29:18,254 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-25 13:29:18,254 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-25 13:29:18,258 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 13:29:18,277 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-25 13:29:18,300 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 13:29:18,325 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data starts at 2017-08-17 04:00:00
2025-09-25 13:29:34,694 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 13:29:34,709 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-25 13:29:34,730 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 13:29:34,749 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data starts at 2017-08-17 04:00:00
2025-09-25 13:29:34,753 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 4h, spot between two candles of 48.50% detected.
2025-09-25 13:29:52,200 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 13:29:52,217 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-25 13:29:52,238 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 13:29:52,267 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data starts at 2017-12-13 00:00:00
2025-09-25 13:30:09,436 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 13:30:09,450 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-25 13:30:09,468 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 13:30:09,490 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data starts at 2018-05-04 08:00:00
2025-09-25 13:30:24,569 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 13:30:24,587 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-25 13:30:24,612 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 13:30:24,639 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data starts at 2017-11-06 00:00:00
2025-09-25 13:30:24,643 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 4h, spot between two candles of 23.53% detected.
2025-09-25 13:30:41,491 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2017-08-17 04:00:00 up to 2023-12-31 00:00:00 (2326 days).
2025-09-25 13:42:35,276 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-25_13-42-35.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │    282 │         1.42 │       27051.601 │      2705.16 │  2 days, 8:36:00 │   97     0   185  34.4 │
│ BNB/USDT │    267 │         2.07 │       26504.998 │       2650.5 │  2 days, 6:03:00 │   85     0   182  31.8 │
│ BTC/USDT │    301 │         0.98 │        9132.528 │       913.25 │ 2 days, 10:16:00 │   94     0   207  31.2 │
│ XRP/USDT │    200 │         0.75 │        6905.322 │       690.53 │  1 day, 18:42:00 │   52     0   148  26.0 │
│ LTC/USDT │    233 │         0.12 │       -5402.750 │      -540.27 │  1 day, 22:52:00 │   73     0   160  31.3 │
│    TOTAL │   1283 │         1.11 │       64191.699 │      6419.17 │  2 days, 4:32:00 │  401     0   882  31.3 │
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
│ strong_bullish_rebond │     980 │         1.08 │       44892.134 │      4489.21 │ 2 days, 7:11:00 │  320     0   660  32.7 │
│         hammer_rebond │     184 │         1.23 │       20783.937 │      2078.39 │ 1 day, 15:20:00 │   40     0   144  21.7 │
│      engulfing_rebond │     119 │         1.15 │       -1484.372 │      -148.44 │ 2 days, 3:06:00 │   41     0    78  34.5 │
│                 TOTAL │    1283 │         1.11 │       64191.699 │      6419.17 │ 2 days, 4:32:00 │  401     0   882  31.3 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                         EXIT REASON STATS                                                         
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                 Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ichimoku_cloud_crossed_exit │   879 │         3.26 │      226963.550 │     22696.35 │ 2 days, 20:26:00 │  401     0   478  45.6 │
│                   stop_loss │   404 │        -3.57 │     -162771.850 │    -16277.19 │         17:55:00 │    0     0   404     0 │
│                       TOTAL │  1283 │         1.11 │       64191.699 │      6419.17 │  2 days, 4:32:00 │  401     0   882  31.3 │
└─────────────────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                                      MIXED TAG STATS                                                                       
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃                 Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ ichimoku_cloud_crossed_exit │    726 │         2.86 │      160031.125 │     16003.11 │ 2 days, 19:48:00 │  320     0   406  44.1 │
│         hammer_rebond │ ichimoku_cloud_crossed_exit │     69 │         7.61 │       54191.405 │      5419.14 │  3 days, 8:25:00 │   40     0    29  58.0 │
│      engulfing_rebond │ ichimoku_cloud_crossed_exit │     84 │         3.17 │       12741.020 │       1274.1 │ 2 days, 16:06:00 │   41     0    43  48.8 │
│      engulfing_rebond │                   stop_loss │     35 │        -3.69 │      -14225.392 │     -1422.54 │         19:56:00 │    0     0    35     0 │
│         hammer_rebond │                   stop_loss │    115 │        -2.59 │      -33407.468 │     -3340.75 │         14:40:00 │    0     0   115     0 │
│ strong_bullish_rebond │                   stop_loss │    254 │         -4.0 │     -115138.991 │     -11513.9 │         19:06:00 │    0     0   254     0 │
│                 TOTAL │                             │   1283 │         1.11 │       64191.699 │      6419.17 │  2 days, 4:32:00 │  401     0   882  31.3 │
└───────────────────────┴─────────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2017-08-17 04:00:00             │
│ Backtesting to                │ 2023-12-31 00:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 1283 / 0.55                     │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 65191.699 USDT                  │
│ Absolute profit               │ 64191.699 USDT                  │
│ Total profit %                │ 6419.17%                        │
│ CAGR %                        │ 92.61%                          │
│ Sortino                       │ 1.46                            │
│ Sharpe                        │ 0.47                            │
│ Calmar                        │ 103.24                          │
│ SQN                           │ 1.60                            │
│ Profit factor                 │ 1.23                            │
│ Expectancy (Ratio)            │ 50.03 (0.16)                    │
│ Avg. daily profit             │ 27.597 USDT                     │
│ Avg. stake amount             │ 12618.326 USDT                  │
│ Total trade volume            │ 32507765.921 USDT               │
│                               │                                 │
│ Best Pair                     │ ETH/USDT 2705.16%               │
│ Worst Pair                    │ LTC/USDT -540.27%               │
│ Best trade                    │ BNB/USDT 166.24%                │
│ Worst trade                   │ BNB/USDT -20.56%                │
│ Best day                      │ 15597.001 USDT                  │
│ Worst day                     │ -3511.013 USDT                  │
│ Days win/draw/lose            │ 282 / 1491 / 548                │
│ Min/Max/Avg. Duration Winners │ 1d 04:00 / 16d 07:00 / 4d 12:06 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:05 / 4d 17:00 / 1d 03:16  │
│ Max Consecutive Wins / Loss   │ 8 / 19                          │
│ Rejected Entry signals        │ 10507                           │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 984.906 USDT                    │
│ Max balance                   │ 87124.867 USDT                  │
│ Max % of account underwater   │ 51.07%                          │
│ Absolute drawdown             │ 44495.991 USDT (51.07%)         │
│ Drawdown duration             │ 347 days 18:15:00               │
│ Profit at drawdown start      │ 86124.867 USDT                  │
│ Profit at drawdown end        │ 41628.877 USDT                  │
│ Drawdown start                │ 2021-11-10 20:00:00             │
│ Drawdown end                  │ 2022-10-24 14:15:00             │
│ Market change                 │ 4006.86%                        │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2017-08-17 04:00:00 -> 2023-12-31 00:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                    
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃               Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │   1283 │         1.11 │       64191.699 │      6419.17 │ 2 days, 4:32:00 │  401     0   882  31.3 │ 44495.991 USDT  51.07% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴────────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-25T15:42:36.811817",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 9722,
  "total_daily_avg_trades": "1283 / 0.55",
  "absolute_profit_usdt": 64191.699,
  "total_profit_pct": 6419.17,
  "cagr_pct": 92.61,
  "sortino": 1.46,
  "sharpe": 0.47,
  "calmar": 103.24,
  "sqn": 1.6,
  "max_consecutive_wins_loss": "8 / 19",
  "min_balance_usdt": 984.906,
  "max_balance_usdt": 87124.867,
  "absolute_drawdown_pct": 51.07,
  "market_change_pct": 4006.86,
  "win_draw_loss_winpct": "0 0 0 0"
}
```
