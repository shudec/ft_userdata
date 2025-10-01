# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 4570  
**Timestamp:** 2025-10-01 22:14:46

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 4570,
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
2025-10-01 20:11:59,931 - freqtrade - INFO - freqtrade 2025.7
2025-10-01 20:12:00,329 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-10-01 20:12:00,330 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-01 20:12:01,896 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-01 20:12:01,899 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-01 20:12:01,899 - freqtrade.loggers - INFO - Logfile configured
2025-10-01 20:12:01,900 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-01 20:12:01,900 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-10-01 20:12:01,900 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-01 20:12:01,901 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-01 20:12:01,901 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-10-01 20:12:01,909 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-01 20:12:01,910 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-01 20:12:01,911 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-01 20:12:01,911 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-01 20:12:01,912 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-01 20:12:01,912 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-10-01 20:12:01,912 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-10-01 20:12:01,914 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-01 20:12:01,932 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-01 20:12:01,933 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-01 20:12:01,936 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-01 20:12:01,937 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-01 20:12:01,938 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-10-01 20:12:01,975 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-01 20:12:04,906 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-01 20:12:04,951 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-10-01 20:12:04,952 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-10-01 20:12:04,953 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-10-01 20:12:04,953 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-01 20:12:04,954 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-01 20:12:04,954 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-01 20:12:04,954 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-01 20:12:04,955 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-01 20:12:04,955 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-10-01 20:12:04,956 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-10-01 20:12:04,956 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-01 20:12:04,956 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-01 20:12:04,957 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-01 20:12:04,957 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-01 20:12:04,958 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-01 20:12:04,958 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-10-01 20:12:04,959 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-01 20:12:04,959 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-01 20:12:04,959 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-01 20:12:04,960 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-10-01 20:12:04,960 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-01 20:12:04,961 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-10-01 20:12:04,961 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-01 20:12:04,961 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-01 20:12:04,962 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-01 20:12:04,962 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-01 20:12:04,963 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-01 20:12:04,963 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-01 20:12:04,964 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-01 20:12:04,964 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-01 20:12:04,965 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-01 20:12:04,970 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-01 20:12:05,005 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-01 20:12:05,039 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-10-01 20:12:05,094 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-10-01 20:12:05,150 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-10-01 20:12:05,200 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-10-01 20:12:05,253 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-10-01 20:12:05,287 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-10-01 20:12:05,365 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-01 20:12:05,600 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-01 20:12:05,822 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-01 20:12:06,047 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-01 20:12:06,264 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-01 20:12:07,645 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-01 20:12:07,646 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-01 20:12:07,647 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-10-01 20:12:07,648 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.4
2025-10-01 20:12:07,648 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-10-01 20:12:07,649 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-10-01 20:12:07,649 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-10-01 20:12:07,650 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_strength_threshold = 0.02
2025-10-01 20:12:07,650 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 20
2025-10-01 20:12:07,651 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-10-01 20:12:07,651 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 1
2025-10-01 20:12:07,652 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-10-01 20:12:07,652 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.02
2025-10-01 20:12:07,653 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.003
2025-10-01 20:12:07,654 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_engulfing_signal_strength_threshold_max = 0.132
2025-10-01 20:12:07,654 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_engulfing_signal_strength_threshold_min = 0.071
2025-10-01 20:12:07,655 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_hammer_signal_strength_threshold_max = 0.431
2025-10-01 20:12:07,656 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_hammer_signal_strength_threshold_min = 0.254
2025-10-01 20:12:07,656 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-10-01 20:12:07,657 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-10-01 20:12:07,658 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_size_threshold = 2
2025-10-01 20:12:07,659 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_strength_threshold = 0.02
2025-10-01 20:12:07,659 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.409
2025-10-01 20:12:07,660 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.003
2025-10-01 20:12:07,660 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_engulfing_entry = True
2025-10-01 20:12:07,661 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_hammer_entry = False
2025-10-01 20:12:07,661 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_strong_bullish_entry = False
2025-10-01 20:12:07,662 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0
2025-10-01 20:12:07,662 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 0.5
2025-10-01 20:12:07,663 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-10-01 20:12:07,663 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-10-01 20:12:07,664 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 6
2025-10-01 20:12:07,664 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-10-01 20:12:07,665 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-10-01 20:12:07,665 - freqtrade.strategy.hyper - INFO - Strategy Parameter: trailing_custom_stop = False
2025-10-01 20:12:07,666 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-10-01 20:12:07,666 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-10-01 20:12:07,667 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-10-01 20:12:07,667 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = False
2025-10-01 20:12:07,668 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = False
2025-10-01 20:12:07,668 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-10-01 20:12:07,669 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-10-01 20:12:07,669 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-01 20:12:07,674 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 20:12:07,684 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-01 20:12:07,709 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 20:12:07,726 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-01 20:12:17,733 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 20:12:17,740 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-01 20:12:17,763 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 20:12:17,780 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-01 20:12:27,638 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 20:12:27,648 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-01 20:12:27,680 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 20:12:27,698 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-01 20:12:38,249 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 20:12:38,256 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-01 20:12:38,278 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 20:12:38,296 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-01 20:12:48,477 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 20:12:48,485 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-01 20:12:48,508 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 20:12:48,525 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-01 20:12:58,707 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-10-01 20:14:45,743 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-01_20-14-45.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │     89 │         0.55 │         180.652 │        18.07 │  3 days, 4:11:00 │   33     0    56  37.1 │
│ BNB/USDT │     10 │         0.52 │          37.522 │         3.75 │  1 day, 14:40:00 │    4     0     6  40.0 │
│ BTC/USDT │     11 │         0.26 │          17.341 │         1.73 │  1 day, 15:14:00 │    4     0     7  36.4 │
│ ETH/USDT │     45 │         0.15 │          11.372 │         1.14 │ 2 days, 11:14:00 │   15     0    30  33.3 │
│ LTC/USDT │     37 │         0.01 │         -29.701 │        -2.97 │  1 day, 19:02:00 │   12     0    25  32.4 │
│    TOTAL │    192 │         0.33 │         217.186 │        21.72 │ 2 days, 13:45:00 │   68     0   124  35.4 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                     ENTER TAG STATS                                                      
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │     192 │         0.33 │         217.186 │        21.72 │ 2 days, 13:45:00 │   68     0   124  35.4 │
│            TOTAL │     192 │         0.33 │         217.186 │        21.72 │ 2 days, 13:45:00 │   68     0   124  35.4 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │    68 │         7.67 │        2678.208 │       267.82 │  3 days, 3:11:00 │   68     0     0   100 │
│      stop_loss │   124 │        -3.69 │       -2461.022 │       -246.1 │  2 days, 6:23:00 │    0     0   124     0 │
│          TOTAL │   192 │         0.33 │         217.186 │        21.72 │ 2 days, 13:45:00 │   68     0   124  35.4 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                             MIXED TAG STATS                                                              
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │ take_profit_2R │     68 │         7.67 │        2678.208 │       267.82 │  3 days, 3:11:00 │   68     0     0   100 │
│ engulfing_rebond │      stop_loss │    124 │        -3.69 │       -2461.022 │       -246.1 │  2 days, 6:23:00 │    0     0   124     0 │
│            TOTAL │                │    192 │         0.33 │         217.186 │        21.72 │ 2 days, 13:45:00 │   68     0   124  35.4 │
└──────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00             │
│ Backtesting to                │ 2025-09-11 17:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 192 / 0.14                      │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 1217.186 USDT                   │
│ Absolute profit               │ 217.186 USDT                    │
│ Total profit %                │ 21.72%                          │
│ CAGR %                        │ 5.46%                           │
│ Sortino                       │ 0.64                            │
│ Sharpe                        │ 0.11                            │
│ Calmar                        │ 1.30                            │
│ SQN                           │ 0.54                            │
│ Profit factor                 │ 1.09                            │
│ Expectancy (Ratio)            │ 1.13 (0.06)                     │
│ Avg. daily profit             │ 0.161 USDT                      │
│ Avg. stake amount             │ 551.773 USDT                    │
│ Total trade volume            │ 212522.776 USDT                 │
│                               │                                 │
│ Best Pair                     │ XRP/USDT 18.07%                 │
│ Worst Pair                    │ LTC/USDT -2.97%                 │
│ Best trade                    │ XRP/USDT 21.68%                 │
│ Worst trade                   │ XRP/USDT -8.19%                 │
│ Best day                      │ 76.156 USDT                     │
│ Worst day                     │ -53.4 USDT                      │
│ Days win/draw/lose            │ 67 / 1150 / 107                 │
│ Min/Max/Avg. Duration Winners │ 0d 00:15 / 20d 12:25 / 3d 03:11 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:40 / 49d 11:05 / 2d 06:23 │
│ Max Consecutive Wins / Loss   │ 5 / 10                          │
│ Rejected Entry signals        │ 0                               │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 916.947 USDT                    │
│ Max balance                   │ 1508.082 USDT                   │
│ Max % of account underwater   │ 23.57%                          │
│ Absolute Drawdown (Account)   │ 23.57%                          │
│ Absolute Drawdown             │ 355.458 USDT                    │
│ Drawdown high                 │ 508.082 USDT                    │
│ Drawdown low                  │ 152.623 USDT                    │
│ Drawdown Start                │ 2023-07-19 03:05:00             │
│ Drawdown End                  │ 2025-02-18 16:25:00             │
│ Market change                 │ 94.84%                          │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    192 │         0.33 │         217.186 │        21.72 │ 2 days, 13:45:00 │   68     0   124  35.4 │ 355.458 USDT  23.57% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-01T22:14:46.894821",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 4570,
  "total_daily_avg_trades": "192 / 0.14",
  "absolute_profit_usdt": 217.186,
  "total_profit_pct": 21.72,
  "cagr_pct": 5.46,
  "sortino": 0.64,
  "sharpe": 0.11,
  "calmar": 1.3,
  "sqn": 0.54,
  "max_consecutive_wins_loss": "5 / 10",
  "min_balance_usdt": 916.947,
  "max_balance_usdt": 1508.082,
  "market_change_pct": 94.84,
  "win_draw_loss_winpct": "0 0 0 0"
}
```
