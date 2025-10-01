# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 1250  
**Timestamp:** 2025-10-01 20:46:44

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 1250,
  "epochs": 100,
  "hyperopt_timerange": "20220101-20231231",
  "backtest_timerange": "20220101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231 --export trades
```

## Backtesting Output
```
2025-10-01 18:44:50,529 - freqtrade - INFO - freqtrade 2025.7
2025-10-01 18:44:50,954 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-10-01 18:44:50,955 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-01 18:44:52,827 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-01 18:44:52,830 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-01 18:44:52,831 - freqtrade.loggers - INFO - Logfile configured
2025-10-01 18:44:52,831 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-01 18:44:52,832 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-10-01 18:44:52,832 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-01 18:44:52,833 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-01 18:44:52,833 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-10-01 18:44:52,842 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-01 18:44:52,843 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-01 18:44:52,844 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-01 18:44:52,845 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-01 18:44:52,845 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-01 18:44:52,846 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-10-01 18:44:52,847 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-10-01 18:44:52,849 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-01 18:44:52,873 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-01 18:44:52,874 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-01 18:44:52,879 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-01 18:44:52,881 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-01 18:44:52,881 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-10-01 18:44:52,916 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-01 18:44:55,729 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-01 18:44:55,806 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-10-01 18:44:55,806 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-10-01 18:44:55,808 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-10-01 18:44:55,808 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-01 18:44:55,809 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-01 18:44:55,810 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-01 18:44:55,810 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-01 18:44:55,811 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-01 18:44:55,811 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-10-01 18:44:55,812 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-10-01 18:44:55,812 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-01 18:44:55,813 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-01 18:44:55,813 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-01 18:44:55,814 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-01 18:44:55,815 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-01 18:44:55,815 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-10-01 18:44:55,816 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-01 18:44:55,816 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-01 18:44:55,817 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-01 18:44:55,818 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-10-01 18:44:55,818 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-01 18:44:55,819 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-10-01 18:44:55,819 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-01 18:44:55,820 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-01 18:44:55,820 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-01 18:44:55,821 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-01 18:44:55,821 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-01 18:44:55,822 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-01 18:44:55,822 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-01 18:44:55,823 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-01 18:44:55,823 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-01 18:44:55,830 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-01 18:44:55,872 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-01 18:44:55,930 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-10-01 18:44:56,021 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-10-01 18:44:56,080 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-10-01 18:44:56,148 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-10-01 18:44:56,203 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-10-01 18:44:56,237 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-10-01 18:44:56,323 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-01 18:44:56,558 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-01 18:44:56,771 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-01 18:44:56,988 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-01 18:44:57,211 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-01 18:44:58,555 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-01 18:44:58,557 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-01 18:44:58,558 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-10-01 18:44:58,559 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.4
2025-10-01 18:44:58,559 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-10-01 18:44:58,559 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-10-01 18:44:58,560 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-10-01 18:44:58,560 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_strength_threshold = 0.02
2025-10-01 18:44:58,560 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 20
2025-10-01 18:44:58,561 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-10-01 18:44:58,561 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 1
2025-10-01 18:44:58,561 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-10-01 18:44:58,562 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.02
2025-10-01 18:44:58,562 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.003
2025-10-01 18:44:58,562 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_engulfing_signal_strength_threshold_max = 0.132
2025-10-01 18:44:58,563 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_engulfing_signal_strength_threshold_min = 0.071
2025-10-01 18:44:58,563 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_hammer_signal_strength_threshold_max = 0.431
2025-10-01 18:44:58,563 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_hammer_signal_strength_threshold_min = 0.254
2025-10-01 18:44:58,564 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-10-01 18:44:58,564 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-10-01 18:44:58,564 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_size_threshold = 2
2025-10-01 18:44:58,565 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_strength_threshold = 0.02
2025-10-01 18:44:58,565 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.409
2025-10-01 18:44:58,565 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.003
2025-10-01 18:44:58,566 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_engulfing_entry = True
2025-10-01 18:44:58,566 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_hammer_entry = False
2025-10-01 18:44:58,566 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_strong_bullish_entry = False
2025-10-01 18:44:58,567 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0
2025-10-01 18:44:58,567 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 0.5
2025-10-01 18:44:58,568 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-10-01 18:44:58,568 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-10-01 18:44:58,568 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 6
2025-10-01 18:44:58,569 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-10-01 18:44:58,569 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-10-01 18:44:58,570 - freqtrade.strategy.hyper - INFO - Strategy Parameter: trailing_custom_stop = False
2025-10-01 18:44:58,570 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-10-01 18:44:58,570 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-10-01 18:44:58,571 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-10-01 18:44:58,571 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = False
2025-10-01 18:44:58,572 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = False
2025-10-01 18:44:58,572 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-10-01 18:44:58,573 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-10-01 18:44:58,573 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-01 18:44:58,576 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 18:44:58,588 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-01 18:44:58,617 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 18:44:58,638 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-01 18:45:07,980 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 18:45:07,989 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-01 18:45:08,015 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 18:45:08,033 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-01 18:45:17,350 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 18:45:17,380 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-01 18:45:17,403 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 18:45:17,422 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-01 18:45:26,793 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 18:45:26,802 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-01 18:45:26,828 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 18:45:26,847 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-01 18:45:36,302 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 18:45:36,312 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-01 18:45:36,336 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 18:45:36,356 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-01 18:45:45,862 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-10-01 18:46:42,940 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-01_18-46-42.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │     50 │         0.32 │          60.800 │         6.08 │ 1 day, 11:09:00 │   22     0    28  44.0 │
│ BNB/USDT │     10 │         0.92 │          50.415 │         5.04 │        17:02:00 │    4     0     6  40.0 │
│ BTC/USDT │     11 │        -0.51 │         -31.504 │        -3.15 │        23:54:00 │    4     0     7  36.4 │
│ LTC/USDT │     39 │        -0.11 │         -32.006 │         -3.2 │        21:20:00 │   13     0    26  33.3 │
│ XRP/USDT │    107 │        -0.16 │        -169.374 │       -16.94 │  1 day, 6:24:00 │   36     0    71  33.6 │
│    TOTAL │    217 │        -0.01 │        -121.669 │       -12.17 │  1 day, 4:55:00 │   79     0   138  36.4 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                    ENTER TAG STATS                                                     
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │     217 │        -0.01 │        -121.669 │       -12.17 │ 1 day, 4:55:00 │   79     0   138  36.4 │
│            TOTAL │     217 │        -0.01 │        -121.669 │       -12.17 │ 1 day, 4:55:00 │   79     0   138  36.4 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                    EXIT REASON STATS                                                     
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     take_profit_2R │    31 │         7.85 │        1108.393 │       110.84 │ 2 days, 10:16:00 │   31     0     0   100 │
│          stop_loss │     1 │         -4.2 │         -21.490 │        -2.15 │          1:35:00 │    0     0     1     0 │
│ trailing_stop_loss │   185 │         -1.3 │       -1208.572 │      -120.86 │   1 day, 0:09:00 │   48     0   137  25.9 │
│              TOTAL │   217 │        -0.01 │        -121.669 │       -12.17 │   1 day, 4:55:00 │   79     0   138  36.4 │
└────────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                               MIXED TAG STATS                                                                
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃        Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │     take_profit_2R │     31 │         7.85 │        1108.393 │       110.84 │ 2 days, 10:16:00 │   31     0     0   100 │
│ engulfing_rebond │          stop_loss │      1 │         -4.2 │         -21.490 │        -2.15 │          1:35:00 │    0     0     1     0 │
│ engulfing_rebond │ trailing_stop_loss │    185 │         -1.3 │       -1208.572 │      -120.86 │   1 day, 0:09:00 │   48     0   137  25.9 │
│            TOTAL │                    │    217 │        -0.01 │        -121.669 │       -12.17 │   1 day, 4:55:00 │   79     0   138  36.4 │
└──────────────────┴────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00             │
│ Backtesting to                │ 2025-09-11 17:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 217 / 0.16                      │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 878.331 USDT                    │
│ Absolute profit               │ -121.669 USDT                   │
│ Total profit %                │ -12.17%                         │
│ CAGR %                        │ -3.45%                          │
│ Sortino                       │ -0.34                           │
│ Sharpe                        │ -0.10                           │
│ Calmar                        │ -0.58                           │
│ SQN                           │ -0.47                           │
│ Profit factor                 │ 0.92                            │
│ Expectancy (Ratio)            │ -0.56 (-0.05)                   │
│ Avg. daily profit             │ -0.09 USDT                      │
│ Avg. stake amount             │ 501.01 USDT                     │
│ Total trade volume            │ 217751.805 USDT                 │
│                               │                                 │
│ Best Pair                     │ ETH/USDT 6.08%                  │
│ Worst Pair                    │ XRP/USDT -16.94%                │
│ Best trade                    │ XRP/USDT 21.68%                 │
│ Worst trade                   │ XRP/USDT -7.12%                 │
│ Best day                      │ 70.376 USDT                     │
│ Worst day                     │ -36.861 USDT                    │
│ Days win/draw/lose            │ 71 / 1141 / 120                 │
│ Min/Max/Avg. Duration Winners │ 0d 03:30 / 20d 12:25 / 2d 01:15 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 9d 20:00 / 0d 17:17  │
│ Max Consecutive Wins / Loss   │ 5 / 9                           │
│ Rejected Entry signals        │ 0                               │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 871.237 USDT                    │
│ Max balance                   │ 1243.722 USDT                   │
│ Max % of account underwater   │ 29.95%                          │
│ Absolute Drawdown (Account)   │ 29.95%                          │
│ Absolute Drawdown             │ 372.485 USDT                    │
│ Drawdown high                 │ 243.722 USDT                    │
│ Drawdown low                  │ -128.763 USDT                   │
│ Drawdown Start                │ 2023-04-26 12:25:00             │
│ Drawdown End                  │ 2025-08-22 14:00:00             │
│ Market change                 │ 94.84%                          │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                  
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    217 │        -0.01 │        -121.669 │       -12.17 │ 1 day, 4:55:00 │   79     0   138  36.4 │ 372.485 USDT  29.95% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-01T20:46:44.125716",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 1250,
  "total_daily_avg_trades": "217 / 0.16",
  "absolute_profit_usdt": -121.669,
  "total_profit_pct": -12.17,
  "cagr_pct": -3.45,
  "sortino": -0.34,
  "sharpe": -0.1,
  "calmar": -0.58,
  "sqn": -0.47,
  "max_consecutive_wins_loss": "5 / 9",
  "min_balance_usdt": 871.237,
  "max_balance_usdt": 1243.722,
  "market_change_pct": 94.84,
  "win_draw_loss_winpct": "0 0 0 0"
}
```
