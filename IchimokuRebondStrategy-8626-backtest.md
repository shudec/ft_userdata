# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 8626  
**Timestamp:** 2025-09-25 22:11:10

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 8626,
  "epochs": 100,
  "hyperopt_timerange": "20220101-20231231",
  "backtest_timerange": "20240101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20240101-20251231
```

## Backtesting Output
```
2025-09-25 20:10:11,245 - freqtrade - INFO - freqtrade 2025.7
2025-09-25 20:10:11,613 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-25 20:10:11,614 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-25 20:10:13,111 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-25 20:10:13,114 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-25 20:10:13,114 - freqtrade.loggers - INFO - Logfile configured
2025-09-25 20:10:13,115 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-25 20:10:13,115 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-25 20:10:13,115 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-25 20:10:13,116 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-25 20:10:13,116 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20240101-20251231 ...
2025-09-25 20:10:13,124 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-25 20:10:13,124 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-25 20:10:13,125 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-25 20:10:13,125 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-25 20:10:13,126 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-25 20:10:13,126 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20240101-20251231
2025-09-25 20:10:13,128 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-25 20:10:13,148 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-25 20:10:13,148 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 20:10:13,152 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-25 20:10:13,153 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-25 20:10:13,154 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-25 20:10:13,189 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-25 20:10:15,846 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-25 20:10:15,884 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-25 20:10:15,885 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-25 20:10:15,885 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-25 20:10:15,886 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-25 20:10:15,886 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-25 20:10:15,887 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-25 20:10:15,887 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-25 20:10:15,887 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-25 20:10:15,888 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-25 20:10:15,888 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-25 20:10:15,888 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-25 20:10:15,888 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-25 20:10:15,889 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-25 20:10:15,889 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-25 20:10:15,889 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-25 20:10:15,890 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-25 20:10:15,890 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-25 20:10:15,890 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-25 20:10:15,891 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-25 20:10:15,891 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-25 20:10:15,891 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-25 20:10:15,892 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-25 20:10:15,892 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-25 20:10:15,892 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-25 20:10:15,893 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-25 20:10:15,893 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-25 20:10:15,893 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-25 20:10:15,893 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-25 20:10:15,894 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-25 20:10:15,894 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-25 20:10:15,895 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 20:10:15,899 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-25 20:10:15,931 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-25 20:10:15,962 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-25 20:10:16,001 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-25 20:10:16,042 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-25 20:10:16,088 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-25 20:10:16,132 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-25 20:10:16,161 - freqtrade.optimize.backtesting - INFO - Loading data from 2024-01-01 00:00:00 up to 2025-09-11 17:00:00 (619 days).
2025-09-25 20:10:16,251 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-25 20:10:16,428 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-25 20:10:16,603 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-25 20:10:16,736 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-25 20:10:16,896 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-25 20:10:17,660 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-25 20:10:17,661 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-25 20:10:17,662 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-25 20:10:17,662 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.4
2025-09-25 20:10:17,663 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-25 20:10:17,663 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-25 20:10:17,663 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 3
2025-09-25 20:10:17,664 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 20
2025-09-25 20:10:17,664 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 11
2025-09-25 20:10:17,664 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.614
2025-09-25 20:10:17,665 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.127
2025-09-25 20:10:17,665 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.04
2025-09-25 20:10:17,665 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.003
2025-09-25 20:10:17,665 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-25 20:10:17,666 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-25 20:10:17,666 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.409
2025-09-25 20:10:17,666 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.0
2025-09-25 20:10:17,667 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 3
2025-09-25 20:10:17,667 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1
2025-09-25 20:10:17,667 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-09-25 20:10:17,668 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-25 20:10:17,668 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 4
2025-09-25 20:10:17,668 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-25 20:10:17,669 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-25 20:10:17,669 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-09-25 20:10:17,669 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-25 20:10:17,669 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = atr
2025-09-25 20:10:17,670 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-09-25 20:10:17,670 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-25 20:10:17,670 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-25 20:10:17,671 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-25 20:10:17,671 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-25 20:10:17,672 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 20:10:17,682 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-25 20:10:17,703 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 20:10:17,720 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-25 20:10:20,726 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 20:10:20,735 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-25 20:10:20,759 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 20:10:20,778 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-25 20:10:24,235 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 20:10:24,243 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-25 20:10:24,262 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 20:10:24,279 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-25 20:10:27,262 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 20:10:27,269 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-25 20:10:27,289 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 20:10:27,306 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-25 20:10:30,251 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 20:10:30,257 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-25 20:10:30,276 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 20:10:30,293 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-25 20:10:33,290 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2024-01-01 00:00:00 up to 2025-09-11 17:00:00 (619 days).
2025-09-25 20:11:09,100 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-25_20-11-09.meta.json"
Result for strategy IchimokuRebondStrategy
                                                BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │      6 │         5.11 │         119.699 │        11.97 │  3 days, 19:15:00 │    3     0     3  50.0 │
│ BNB/USDT │      4 │         3.26 │          37.719 │         3.77 │ 11 days, 23:48:00 │    2     0     2  50.0 │
│ LTC/USDT │      3 │         1.95 │          15.547 │         1.55 │   1 day, 12:40:00 │    1     0     2  33.3 │
│ XRP/USDT │      0 │          0.0 │           0.000 │          0.0 │              0:00 │    0     0     0     0 │
│ BTC/USDT │     10 │         -1.1 │         -43.757 │        -4.38 │ 16 days, 20:34:00 │    2     0     8  20.0 │
│    TOTAL │     23 │         1.68 │         129.209 │        12.92 │ 10 days, 14:32:00 │    8     0    15  34.8 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         8.18 │          18.582 │         1.86 │ 31 days, 14:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         8.18 │          18.582 │         1.86 │ 31 days, 14:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                        ENTER TAG STATS                                                         
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│      engulfing_rebond │       6 │         5.07 │         122.732 │        12.27 │ 16 days, 14:02:00 │    3     0     3  50.0 │
│ strong_bullish_rebond │      17 │         0.48 │           6.477 │         0.65 │  8 days, 11:53:00 │    5     0    12  29.4 │
│                 TOTAL │      23 │         1.68 │         129.209 │        12.92 │ 10 days, 14:32:00 │    8     0    15  34.8 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                   EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │     7 │        15.46 │         413.132 │        41.31 │  10 days, 6:09:00 │    7     0     0   100 │
│     force_exit │     1 │         8.18 │          18.582 │         1.86 │ 31 days, 14:00:00 │    1     0     0   100 │
│      stop_loss │    15 │        -5.19 │        -302.505 │       -30.25 │   9 days, 8:53:00 │    0     0    15     0 │
│          TOTAL │    23 │         1.68 │         129.209 │        12.92 │ 10 days, 14:32:00 │    8     0    15  34.8 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                                MIXED TAG STATS                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_3R │      4 │        15.55 │         230.828 │        23.08 │  4 days, 22:55:00 │    4     0     0   100 │
│      engulfing_rebond │ take_profit_3R │      3 │        15.33 │         182.303 │        18.23 │  17 days, 7:47:00 │    3     0     0   100 │
│ strong_bullish_rebond │     force_exit │      1 │         8.18 │          18.582 │         1.86 │ 31 days, 14:00:00 │    1     0     0   100 │
│      engulfing_rebond │      stop_loss │      3 │        -5.19 │         -59.571 │        -5.96 │ 15 days, 20:18:00 │    0     0     3     0 │
│ strong_bullish_rebond │      stop_loss │     12 │        -5.19 │        -242.934 │       -24.29 │  7 days, 18:02:00 │    0     0    12     0 │
│                 TOTAL │                │     23 │         1.68 │         129.209 │        12.92 │ 10 days, 14:32:00 │    8     0    15  34.8 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                          SUMMARY METRICS                           
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                            ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2024-01-01 00:00:00              │
│ Backtesting to                │ 2025-09-11 17:00:00              │
│ Trading Mode                  │ Spot                             │
│ Max open trades               │ 3                                │
│                               │                                  │
│ Total/Daily Avg Trades        │ 23 / 0.04                        │
│ Starting balance              │ 1000 USDT                        │
│ Final balance                 │ 1129.209 USDT                    │
│ Absolute profit               │ 129.209 USDT                     │
│ Total profit %                │ 12.92%                           │
│ CAGR %                        │ 7.43%                            │
│ Sortino                       │ 3.53                             │
│ Sharpe                        │ 0.11                             │
│ Calmar                        │ 2.32                             │
│ SQN                           │ 0.73                             │
│ Profit factor                 │ 1.43                             │
│ Expectancy (Ratio)            │ 5.62 (0.28)                      │
│ Avg. daily profit             │ 0.209 USDT                       │
│ Avg. stake amount             │ 379.306 USDT                     │
│ Total trade volume            │ 17612.461 USDT                   │
│                               │                                  │
│ Best Pair                     │ ETH/USDT 11.97%                  │
│ Worst Pair                    │ BTC/USDT -4.38%                  │
│ Best trade                    │ LTC/USDT 16.24%                  │
│ Worst trade                   │ BTC/USDT -5.19%                  │
│ Best day                      │ 65.481 USDT                      │
│ Worst day                     │ -22.35 USDT                      │
│ Days win/draw/lose            │ 8 / 553 / 15                     │
│ Min/Max/Avg. Duration Winners │ 0d 17:20 / 41d 04:15 / 12d 22:08 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:05 / 45d 15:45 / 9d 08:53  │
│ Max Consecutive Wins / Loss   │ 2 / 8                            │
│ Rejected Entry signals        │ 0                                │
│ Entry/Exit Timeouts           │ 0 / 0                            │
│                               │                                  │
│ Min balance                   │ 878.097 USDT                     │
│ Max balance                   │ 1131.747 USDT                    │
│ Max % of account underwater   │ 17.19%                           │
│ Absolute Drawdown (Account)   │ 17.19%                           │
│ Absolute Drawdown             │ 182.249 USDT                     │
│ Drawdown high                 │ 60.346 USDT                      │
│ Drawdown low                  │ -121.903 USDT                    │
│ Drawdown Start                │ 2024-02-14 09:10:00              │
│ Drawdown End                  │ 2025-01-08 06:30:00              │
│ Market change                 │ 178.91%                          │
└───────────────────────────────┴──────────────────────────────────┘

Backtested 2024-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                    
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     23 │         1.68 │         129.209 │        12.92 │ 10 days, 14:32:00 │    8     0    15  34.8 │ 182.249 USDT  17.19% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-25T22:11:10.137160",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 8626,
  "total_daily_avg_trades": "23 / 0.04",
  "absolute_profit_usdt": 129.209,
  "total_profit_pct": 12.92,
  "cagr_pct": 7.43,
  "sortino": 3.53,
  "sharpe": 0.11,
  "calmar": 2.32,
  "sqn": 0.73,
  "max_consecutive_wins_loss": "2 / 8",
  "min_balance_usdt": 878.097,
  "max_balance_usdt": 1131.747,
  "market_change_pct": 178.91
}
```
