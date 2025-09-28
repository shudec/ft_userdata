# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 5111  
**Timestamp:** 2025-09-27 22:28:38

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 5111,
  "epochs": 100,
  "hyperopt_timerange": "20220101-20231231",
  "backtest_timerange": "20220101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231 --export trades --export-filename backtest-result.csv
```

## Backtesting Output
```
2025-09-27 20:26:34,415 - freqtrade - INFO - freqtrade 2025.7
2025-09-27 20:26:34,748 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-27 20:26:34,748 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-27 20:26:36,187 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-27 20:26:36,190 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-27 20:26:36,190 - freqtrade.loggers - INFO - Logfile configured
2025-09-27 20:26:36,191 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-27 20:26:36,191 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-27 20:26:36,191 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-27 20:26:36,192 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-27 20:26:36,192 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-27 20:26:36,200 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-27 20:26:36,201 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-27 20:26:36,201 - freqtrade.configuration.configuration - INFO - Storing backtest results to backtest-result.csv ...
2025-09-27 20:26:36,202 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-27 20:26:36,202 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-09-27 20:26:36,202 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-27 20:26:36,203 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-27 20:26:36,203 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-27 20:26:36,205 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-27 20:26:36,225 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-27 20:26:36,225 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-27 20:26:36,229 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-27 20:26:36,231 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-27 20:26:36,231 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-27 20:26:36,267 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-27 20:26:38,599 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-27 20:26:38,649 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-27 20:26:38,650 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-27 20:26:38,651 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-27 20:26:38,652 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-27 20:26:38,652 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-27 20:26:38,653 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-27 20:26:38,653 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-27 20:26:38,654 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-27 20:26:38,654 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-27 20:26:38,655 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-27 20:26:38,655 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-27 20:26:38,655 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-27 20:26:38,656 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-27 20:26:38,656 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-27 20:26:38,657 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-27 20:26:38,657 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-27 20:26:38,658 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-27 20:26:38,658 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-27 20:26:38,659 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-27 20:26:38,659 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-27 20:26:38,659 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-27 20:26:38,660 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-27 20:26:38,660 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-27 20:26:38,661 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-27 20:26:38,661 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-27 20:26:38,661 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-27 20:26:38,662 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-27 20:26:38,662 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-27 20:26:38,663 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-27 20:26:38,663 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-27 20:26:38,664 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-27 20:26:38,669 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-27 20:26:38,705 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-27 20:26:38,739 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-27 20:26:38,790 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-27 20:26:38,837 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-27 20:26:38,878 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-27 20:26:38,925 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-27 20:26:38,956 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-27 20:26:39,028 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-27 20:26:39,250 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-27 20:26:39,452 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-27 20:26:39,656 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-27 20:26:39,885 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-27 20:26:41,216 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-27 20:26:41,217 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-27 20:26:41,217 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-27 20:26:41,218 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.4
2025-09-27 20:26:41,218 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-27 20:26:41,218 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-27 20:26:41,219 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-27 20:26:41,219 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_strength_threshold = 0.02
2025-09-27 20:26:41,219 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 5
2025-09-27 20:26:41,219 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-09-27 20:26:41,220 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 1
2025-09-27 20:26:41,220 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-09-27 20:26:41,220 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.02
2025-09-27 20:26:41,221 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.003
2025-09-27 20:26:41,221 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-27 20:26:41,221 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-27 20:26:41,222 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_size_threshold = 2
2025-09-27 20:26:41,222 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_strength_threshold = 0.02
2025-09-27 20:26:41,222 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.409
2025-09-27 20:26:41,222 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.003
2025-09-27 20:26:41,223 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_engulfing_entry = False
2025-09-27 20:26:41,223 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_hammer_entry = True
2025-09-27 20:26:41,223 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_strong_bullish_entry = False
2025-09-27 20:26:41,224 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 2.5
2025-09-27 20:26:41,224 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 0.5
2025-09-27 20:26:41,224 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-09-27 20:26:41,225 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-27 20:26:41,225 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 6
2025-09-27 20:26:41,225 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-27 20:26:41,226 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-27 20:26:41,226 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-09-27 20:26:41,226 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-27 20:26:41,227 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-27 20:26:41,227 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-09-27 20:26:41,227 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-27 20:26:41,228 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-27 20:26:41,228 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-27 20:26:41,229 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-27 20:26:41,231 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-27 20:26:41,241 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-27 20:26:41,264 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-27 20:26:41,281 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-27 20:26:50,812 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-27 20:26:50,819 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-27 20:26:50,840 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-27 20:26:50,858 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-27 20:27:00,421 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-27 20:27:00,428 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-27 20:27:00,450 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-27 20:27:00,467 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-27 20:27:10,049 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-27 20:27:10,057 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-27 20:27:10,079 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-27 20:27:10,096 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-27 20:27:19,550 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-27 20:27:19,557 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-27 20:27:19,579 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-27 20:27:19,596 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-27 20:27:29,230 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-27 20:28:37,115 - freqtrade.misc - INFO - dumping json to "backtest-result-2025-09-27_20-28-37.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │     15 │         0.56 │          21.975 │          2.2 │ 5 days, 17:07:00 │    7     0     8  46.7 │
│ BNB/USDT │     14 │         0.58 │          18.414 │         1.84 │  2 days, 7:36:00 │    6     0     8  42.9 │
│ ETH/USDT │     13 │         0.55 │           9.784 │         0.98 │  1 day, 21:28:00 │    5     0     8  38.5 │
│ XRP/USDT │     39 │         -0.6 │         -76.542 │        -7.65 │ 2 days, 11:22:00 │   15     0    24  38.5 │
│ LTC/USDT │     33 │        -1.05 │        -203.007 │        -20.3 │ 4 days, 11:34:00 │    8     0    25  24.2 │
│    TOTAL │    114 │         -0.3 │        -229.375 │       -22.94 │  3 days, 9:30:00 │   41     0    73  36.0 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ LTC/USDT │      1 │         0.44 │           0.578 │         0.06 │ 53 days, 18:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         0.44 │           0.578 │         0.06 │ 53 days, 18:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                   ENTER TAG STATS                                                    
┏━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ hammer_rebond │     114 │         -0.3 │        -229.375 │       -22.94 │ 3 days, 9:30:00 │   41     0    73  36.0 │
│         TOTAL │     114 │         -0.3 │        -229.375 │       -22.94 │ 3 days, 9:30:00 │   41     0    73  36.0 │
└───────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                    EXIT REASON STATS                                                    
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │    40 │         7.83 │         879.527 │        87.95 │  2 days, 17:33:00 │   40     0     0   100 │
│       force_exit │     1 │         0.44 │           0.578 │         0.06 │ 53 days, 18:00:00 │    1     0     0   100 │
│        stop_loss │    73 │        -4.77 │       -1109.480 │      -110.95 │   3 days, 1:41:00 │    0     0    73     0 │
│            TOTAL │   114 │         -0.3 │        -229.375 │       -22.94 │   3 days, 9:30:00 │   41     0    73  36.0 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                             MIXED TAG STATS                                                              
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ hammer_rebond │ take_profit_1.5R │     40 │         7.83 │         879.527 │        87.95 │  2 days, 17:33:00 │   40     0     0   100 │
│ hammer_rebond │       force_exit │      1 │         0.44 │           0.578 │         0.06 │ 53 days, 18:00:00 │    1     0     0   100 │
│ hammer_rebond │        stop_loss │     73 │        -4.77 │       -1109.480 │      -110.95 │   3 days, 1:41:00 │    0     0    73     0 │
│         TOTAL │                  │    114 │         -0.3 │        -229.375 │       -22.94 │   3 days, 9:30:00 │   41     0    73  36.0 │
└───────────────┴──────────────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00             │
│ Backtesting to                │ 2025-09-11 17:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 114 / 0.08                      │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 770.625 USDT                    │
│ Absolute profit               │ -229.375 USDT                   │
│ Total profit %                │ -22.94%                         │
│ CAGR %                        │ -6.81%                          │
│ Sortino                       │ -0.77                           │
│ Sharpe                        │ -0.17                           │
│ Calmar                        │ -1.15                           │
│ SQN                           │ -1.15                           │
│ Profit factor                 │ 0.79                            │
│ Expectancy (Ratio)            │ -2.01 (-0.13)                   │
│ Avg. daily profit             │ -0.17 USDT                      │
│ Avg. stake amount             │ 352.868 USDT                    │
│ Total trade volume            │ 80385.066 USDT                  │
│                               │                                 │
│ Best Pair                     │ BTC/USDT 2.20%                  │
│ Worst Pair                    │ LTC/USDT -20.30%                │
│ Best trade                    │ LTC/USDT 22.95%                 │
│ Worst trade                   │ XRP/USDT -14.87%                │
│ Best day                      │ 50.219 USDT                     │
│ Worst day                     │ -38.903 USDT                    │
│ Days win/draw/lose            │ 37 / 1232 / 61                  │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 53d 18:00 / 3d 23:25 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 34d 19:50 / 3d 01:41 │
│ Max Consecutive Wins / Loss   │ 6 / 11                          │
│ Rejected Entry signals        │ 24                              │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 748.665 USDT                    │
│ Max balance                   │ 1044.784 USDT                   │
│ Max % of account underwater   │ 28.34%                          │
│ Absolute Drawdown (Account)   │ 28.34%                          │
│ Absolute Drawdown             │ 296.119 USDT                    │
│ Drawdown high                 │ 44.784 USDT                     │
│ Drawdown low                  │ -251.335 USDT                   │
│ Drawdown Start                │ 2022-02-07 22:25:00             │
│ Drawdown End                  │ 2024-11-12 04:25:00             │
│ Market change                 │ 94.84%                          │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    114 │        -0.30 │        -229.375 │       -22.94 │ 3 days, 9:30:00 │   41     0    73  36.0 │ 296.119 USDT  28.34% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-27T22:28:38.170273",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 5111,
  "total_daily_avg_trades": "114 / 0.08",
  "absolute_profit_usdt": -229.375,
  "total_profit_pct": -22.94,
  "cagr_pct": -6.81,
  "sortino": -0.77,
  "sharpe": -0.17,
  "calmar": -1.15,
  "sqn": -1.15,
  "max_consecutive_wins_loss": "6 / 11",
  "min_balance_usdt": 748.665,
  "max_balance_usdt": 1044.784,
  "market_change_pct": 94.84
}
```
