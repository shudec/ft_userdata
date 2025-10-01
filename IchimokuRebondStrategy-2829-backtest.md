# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 2829  
**Timestamp:** 2025-10-01 21:28:38

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 2829,
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
2025-10-01 19:26:39,082 - freqtrade - INFO - freqtrade 2025.7
2025-10-01 19:26:39,489 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-10-01 19:26:39,490 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-01 19:26:41,045 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-01 19:26:41,048 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-01 19:26:41,048 - freqtrade.loggers - INFO - Logfile configured
2025-10-01 19:26:41,049 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-01 19:26:41,049 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-10-01 19:26:41,049 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-01 19:26:41,050 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-01 19:26:41,050 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-10-01 19:26:41,058 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-01 19:26:41,059 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-01 19:26:41,059 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-01 19:26:41,059 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-01 19:26:41,060 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-01 19:26:41,060 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-10-01 19:26:41,061 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-10-01 19:26:41,062 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-01 19:26:41,081 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-01 19:26:41,082 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-01 19:26:41,086 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-01 19:26:41,087 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-01 19:26:41,088 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-10-01 19:26:41,121 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-01 19:26:43,871 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-01 19:26:43,919 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-10-01 19:26:43,919 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-10-01 19:26:43,920 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-10-01 19:26:43,921 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-01 19:26:43,921 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-01 19:26:43,922 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-01 19:26:43,922 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-01 19:26:43,923 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-01 19:26:43,923 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-10-01 19:26:43,924 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-10-01 19:26:43,924 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-01 19:26:43,924 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-01 19:26:43,925 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-01 19:26:43,925 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-01 19:26:43,925 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-01 19:26:43,926 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-10-01 19:26:43,926 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-01 19:26:43,927 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-01 19:26:43,927 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-01 19:26:43,927 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-10-01 19:26:43,928 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-01 19:26:43,928 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-10-01 19:26:43,929 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-01 19:26:43,929 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-01 19:26:43,929 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-01 19:26:43,930 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-01 19:26:43,930 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-01 19:26:43,931 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-01 19:26:43,931 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-01 19:26:43,931 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-01 19:26:43,932 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-01 19:26:43,938 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-01 19:26:43,972 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-01 19:26:44,009 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-10-01 19:26:44,063 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-10-01 19:26:44,110 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-10-01 19:26:44,152 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-10-01 19:26:44,197 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-10-01 19:26:44,226 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-10-01 19:26:44,296 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-01 19:26:44,546 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-01 19:26:44,843 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-01 19:26:45,078 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-01 19:26:45,283 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-01 19:26:46,575 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-01 19:26:46,576 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-01 19:26:46,576 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-10-01 19:26:46,577 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.4
2025-10-01 19:26:46,577 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-10-01 19:26:46,577 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-10-01 19:26:46,578 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-10-01 19:26:46,578 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_strength_threshold = 0.02
2025-10-01 19:26:46,578 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 20
2025-10-01 19:26:46,579 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-10-01 19:26:46,579 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 1
2025-10-01 19:26:46,579 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-10-01 19:26:46,579 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.02
2025-10-01 19:26:46,580 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.003
2025-10-01 19:26:46,580 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_engulfing_signal_strength_threshold_max = 0.132
2025-10-01 19:26:46,580 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_engulfing_signal_strength_threshold_min = 0.071
2025-10-01 19:26:46,581 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_hammer_signal_strength_threshold_max = 0.431
2025-10-01 19:26:46,581 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_hammer_signal_strength_threshold_min = 0.254
2025-10-01 19:26:46,581 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-10-01 19:26:46,582 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-10-01 19:26:46,582 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_size_threshold = 2
2025-10-01 19:26:46,582 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_strength_threshold = 0.02
2025-10-01 19:26:46,582 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.409
2025-10-01 19:26:46,583 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.003
2025-10-01 19:26:46,583 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_engulfing_entry = True
2025-10-01 19:26:46,583 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_hammer_entry = False
2025-10-01 19:26:46,584 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_strong_bullish_entry = False
2025-10-01 19:26:46,584 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0
2025-10-01 19:26:46,584 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 0.5
2025-10-01 19:26:46,585 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-10-01 19:26:46,585 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-10-01 19:26:46,586 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 6
2025-10-01 19:26:46,586 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-10-01 19:26:46,586 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-10-01 19:26:46,587 - freqtrade.strategy.hyper - INFO - Strategy Parameter: trailing_custom_stop = False
2025-10-01 19:26:46,587 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = False
2025-10-01 19:26:46,588 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-10-01 19:26:46,588 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-10-01 19:26:46,589 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-10-01 19:26:46,589 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = False
2025-10-01 19:26:46,590 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-10-01 19:26:46,590 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-10-01 19:26:46,590 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-01 19:26:46,593 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 19:26:46,601 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-01 19:26:46,627 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 19:26:46,644 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-01 19:26:55,952 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 19:26:55,960 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-01 19:26:55,984 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 19:26:56,001 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-01 19:27:05,240 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 19:27:05,247 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-01 19:27:05,271 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 19:27:05,289 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-01 19:27:14,626 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 19:27:14,633 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-01 19:27:14,656 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 19:27:14,673 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-01 19:27:24,074 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 19:27:24,081 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-01 19:27:24,104 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 19:27:24,122 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-01 19:27:33,621 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-10-01 19:28:36,817 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-01_19-28-36.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │     11 │         1.58 │         104.914 │        10.49 │ 2 days, 7:11:00 │    3     0     8  27.3 │
│ BNB/USDT │     10 │          0.4 │          43.332 │         4.33 │ 1 day, 19:34:00 │    2     0     8  20.0 │
│ XRP/USDT │     98 │         0.17 │          -0.710 │        -0.07 │ 1 day, 13:57:00 │   30     0    68  30.6 │
│ LTC/USDT │     38 │         -0.2 │         -57.685 │        -5.77 │ 1 day, 19:50:00 │   10     0    28  26.3 │
│ ETH/USDT │     48 │        -0.34 │         -79.551 │        -7.96 │ 1 day, 18:58:00 │   14     0    34  29.2 │
│    TOTAL │    205 │         0.07 │          10.301 │         1.03 │ 1 day, 17:25:00 │   59     0   146  28.8 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                     ENTER TAG STATS                                                     
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │     205 │         0.07 │          10.301 │         1.03 │ 1 day, 17:25:00 │   59     0   146  28.8 │
│            TOTAL │     205 │         0.07 │          10.301 │         1.03 │ 1 day, 17:25:00 │   59     0   146  28.8 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                        EXIT REASON STATS                                                         
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                 Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ichimoku_cloud_crossed_exit │   141 │         1.65 │        1118.219 │       111.82 │ 2 days, 5:40:00 │   59     0    82  41.8 │
│                   stop_loss │    64 │        -3.41 │       -1107.918 │      -110.79 │        14:25:00 │    0     0    64     0 │
│                       TOTAL │   205 │         0.07 │          10.301 │         1.03 │ 1 day, 17:25:00 │   59     0   146  28.8 │
└─────────────────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                                   MIXED TAG STATS                                                                    
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃                 Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │ ichimoku_cloud_crossed_exit │    141 │         1.65 │        1118.219 │       111.82 │ 2 days, 5:40:00 │   59     0    82  41.8 │
│ engulfing_rebond │                   stop_loss │     64 │        -3.41 │       -1107.918 │      -110.79 │        14:25:00 │    0     0    64     0 │
│            TOTAL │                             │    205 │         0.07 │          10.301 │         1.03 │ 1 day, 17:25:00 │   59     0   146  28.8 │
└──────────────────┴─────────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00             │
│ Backtesting to                │ 2025-09-11 17:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 205 / 0.15                      │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 1010.301 USDT                   │
│ Absolute profit               │ 10.301 USDT                     │
│ Total profit %                │ 1.03%                           │
│ CAGR %                        │ 0.28%                           │
│ Sortino                       │ 0.02                            │
│ Sharpe                        │ 0.01                            │
│ Calmar                        │ 0.04                            │
│ SQN                           │ 0.03                            │
│ Profit factor                 │ 1.01                            │
│ Expectancy (Ratio)            │ 0.05 (0.00)                     │
│ Avg. daily profit             │ 0.008 USDT                      │
│ Avg. stake amount             │ 505.544 USDT                    │
│ Total trade volume            │ 207698.282 USDT                 │
│                               │                                 │
│ Best Pair                     │ BTC/USDT 10.49%                 │
│ Worst Pair                    │ ETH/USDT -7.96%                 │
│ Best trade                    │ XRP/USDT 45.76%                 │
│ Worst trade                   │ XRP/USDT -8.15%                 │
│ Best day                      │ 163.208 USDT                    │
│ Worst day                     │ -44.254 USDT                    │
│ Days win/draw/lose            │ 55 / 1153 / 126                 │
│ Min/Max/Avg. Duration Winners │ 0d 08:00 / 14d 15:00 / 3d 23:55 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:40 / 3d 11:00 / 0d 19:24  │
│ Max Consecutive Wins / Loss   │ 4 / 16                          │
│ Rejected Entry signals        │ 0                               │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 846.039 USDT                    │
│ Max balance                   │ 1368.529 USDT                   │
│ Max % of account underwater   │ 38.18%                          │
│ Absolute Drawdown (Account)   │ 38.18%                          │
│ Absolute Drawdown             │ 522.49 USDT                     │
│ Drawdown high                 │ 368.529 USDT                    │
│ Drawdown low                  │ -153.961 USDT                   │
│ Drawdown Start                │ 2023-06-25 19:00:00             │
│ Drawdown End                  │ 2025-07-22 04:55:00             │
│ Market change                 │ 94.84%                          │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                  
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃            Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    205 │         0.07 │          10.301 │         1.03 │ 1 day, 17:25:00 │   59     0   146  28.8 │ 522.49 USDT  38.18% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴─────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-01T21:28:38.005159",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 2829,
  "total_daily_avg_trades": "205 / 0.15",
  "absolute_profit_usdt": 10.301,
  "total_profit_pct": 1.03,
  "cagr_pct": 0.28,
  "sortino": 0.02,
  "sharpe": 0.01,
  "calmar": 0.04,
  "sqn": 0.03,
  "max_consecutive_wins_loss": "4 / 16",
  "min_balance_usdt": 846.039,
  "max_balance_usdt": 1368.529,
  "market_change_pct": 94.84,
  "win_draw_loss_winpct": "0 0 0 0"
}
```
