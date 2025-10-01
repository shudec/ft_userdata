# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 1208  
**Timestamp:** 2025-10-01 21:50:29

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 1208,
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
2025-10-01 19:39:01,399 - freqtrade - INFO - freqtrade 2025.7
2025-10-01 19:39:01,766 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-10-01 19:39:01,766 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-01 19:39:03,273 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-01 19:39:03,275 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-01 19:39:03,276 - freqtrade.loggers - INFO - Logfile configured
2025-10-01 19:39:03,276 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-01 19:39:03,277 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-10-01 19:39:03,277 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-01 19:39:03,277 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-01 19:39:03,278 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-10-01 19:39:03,285 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-01 19:39:03,286 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-01 19:39:03,286 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-01 19:39:03,287 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-01 19:39:03,287 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-01 19:39:03,288 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-10-01 19:39:03,288 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-10-01 19:39:03,289 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-01 19:39:03,310 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-01 19:39:03,311 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-01 19:39:03,314 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-01 19:39:03,315 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-01 19:39:03,316 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-10-01 19:39:03,348 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-01 19:39:05,951 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-01 19:39:05,991 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-10-01 19:39:05,992 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-10-01 19:39:05,992 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-10-01 19:39:05,993 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-01 19:39:05,993 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-01 19:39:05,994 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-01 19:39:05,994 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-01 19:39:05,994 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-01 19:39:05,995 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-10-01 19:39:05,995 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-10-01 19:39:05,995 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-01 19:39:05,996 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-01 19:39:05,996 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-01 19:39:05,996 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-01 19:39:05,997 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-01 19:39:05,997 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-10-01 19:39:05,997 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-01 19:39:05,998 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-01 19:39:05,998 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-01 19:39:05,998 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-10-01 19:39:05,999 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-01 19:39:05,999 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-10-01 19:39:06,000 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-01 19:39:06,000 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-01 19:39:06,000 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-01 19:39:06,001 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-01 19:39:06,001 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-01 19:39:06,002 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-01 19:39:06,002 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-01 19:39:06,002 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-01 19:39:06,003 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-01 19:39:06,008 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-01 19:39:06,041 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-01 19:39:06,074 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-10-01 19:39:06,126 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-10-01 19:39:06,175 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-10-01 19:39:06,217 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-10-01 19:39:06,262 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-10-01 19:39:06,290 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-10-01 19:39:06,361 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-01 19:39:06,567 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-01 19:39:06,785 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-01 19:39:07,036 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-01 19:39:07,251 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-10-01 19:39:08,537 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-01 19:39:08,538 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-01 19:39:08,538 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-10-01 19:39:08,539 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.4
2025-10-01 19:39:08,539 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-10-01 19:39:08,539 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-10-01 19:39:08,540 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-10-01 19:39:08,540 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_strength_threshold = 0.02
2025-10-01 19:39:08,540 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 20
2025-10-01 19:39:08,541 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-10-01 19:39:08,541 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 1
2025-10-01 19:39:08,541 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-10-01 19:39:08,542 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.02
2025-10-01 19:39:08,542 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.003
2025-10-01 19:39:08,542 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_engulfing_signal_strength_threshold_max = 0.132
2025-10-01 19:39:08,543 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_engulfing_signal_strength_threshold_min = 0.071
2025-10-01 19:39:08,543 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_hammer_signal_strength_threshold_max = 0.431
2025-10-01 19:39:08,543 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_hammer_signal_strength_threshold_min = 0.254
2025-10-01 19:39:08,543 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-10-01 19:39:08,544 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-10-01 19:39:08,544 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_size_threshold = 2
2025-10-01 19:39:08,544 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_strength_threshold = 0.02
2025-10-01 19:39:08,545 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.409
2025-10-01 19:39:08,545 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.003
2025-10-01 19:39:08,545 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_engulfing_entry = True
2025-10-01 19:39:08,546 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_hammer_entry = False
2025-10-01 19:39:08,546 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_strong_bullish_entry = False
2025-10-01 19:39:08,546 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0
2025-10-01 19:39:08,547 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 0.5
2025-10-01 19:39:08,547 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-10-01 19:39:08,548 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-10-01 19:39:08,548 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 6
2025-10-01 19:39:08,548 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-10-01 19:39:08,549 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-10-01 19:39:08,549 - freqtrade.strategy.hyper - INFO - Strategy Parameter: trailing_custom_stop = False
2025-10-01 19:39:08,549 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = False
2025-10-01 19:39:08,550 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-10-01 19:39:08,550 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-10-01 19:39:08,551 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = False
2025-10-01 19:39:08,551 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = False
2025-10-01 19:39:08,551 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-10-01 19:39:08,552 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-10-01 19:39:08,552 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-01 19:39:08,555 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 19:39:08,564 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-01 19:39:08,589 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 19:39:08,606 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-01 19:39:18,144 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 19:39:18,152 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-01 19:39:18,173 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 19:39:18,191 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-01 19:39:27,569 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 19:39:27,576 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-01 19:39:27,599 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 19:39:27,616 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-01 19:39:37,087 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 19:39:37,094 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-01 19:39:37,119 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 19:39:37,137 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-01 19:39:46,549 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 19:39:46,557 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-10-01 19:39:46,581 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-01 19:39:46,598 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-10-01 19:39:56,048 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-10-01 19:50:28,523 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-01_19-50-28.meta.json"
Result for strategy IchimokuRebondStrategy
                                                BACKTESTING REPORT                                                 
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃       Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │      5 │       118.02 │        1901.967 │        190.2 │ 204 days, 10:09:00 │    1     0     4  20.0 │
│ XRP/USDT │      6 │       137.22 │        1817.698 │       181.77 │ 216 days, 19:25:00 │    1     0     5  16.7 │
│ ETH/USDT │     14 │        15.85 │          87.668 │         8.77 │  74 days, 13:29:00 │    1     0    13   7.1 │
│ BNB/USDT │      3 │        -2.93 │         -35.125 │        -3.51 │   5 days, 15:48:00 │    0     0     3     0 │
│ LTC/USDT │      6 │        -3.64 │         -53.447 │        -5.34 │   4 days, 12:12:00 │    0     0     6     0 │
│    TOTAL │     34 │         47.2 │        3718.760 │       371.88 │  100 days, 7:40:00 │    3     0    31   8.8 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────────┴────────────────────────┘
                                              LEFT OPEN TRADES REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃        Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │      1 │       600.52 │        1915.823 │       191.58 │  1018 days, 0:00:00 │    1     0     0   100 │
│ XRP/USDT │      1 │       846.87 │        1911.173 │       191.12 │  1180 days, 6:00:00 │    1     0     0   100 │
│ ETH/USDT │      1 │       264.89 │         247.664 │        24.77 │  996 days, 12:00:00 │    1     0     0   100 │
│    TOTAL │      3 │       570.76 │        4074.660 │       407.47 │ 1064 days, 22:00:00 │    3     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────────┴────────────────────────┘
                                                      ENTER TAG STATS                                                      
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │      34 │         47.2 │        3718.760 │       371.88 │ 100 days, 7:40:00 │    3     0    31   8.8 │
│            TOTAL │      34 │         47.2 │        3718.760 │       371.88 │ 100 days, 7:40:00 │    3     0    31   8.8 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃        Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  force_exit │     3 │       570.76 │        4074.660 │       407.47 │ 1064 days, 22:00:00 │    3     0     0   100 │
│   stop_loss │    31 │        -3.47 │        -355.900 │       -35.59 │    6 days, 23:19:00 │    0     0    31     0 │
│       TOTAL │    34 │         47.2 │        3718.760 │       371.88 │   100 days, 7:40:00 │    3     0    31   8.8 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────────┴────────────────────────┘
                                                             MIXED TAG STATS                                                              
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃        Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │  force_exit │      3 │       570.76 │        4074.660 │       407.47 │ 1064 days, 22:00:00 │    3     0     0   100 │
│ engulfing_rebond │   stop_loss │     31 │        -3.47 │        -355.900 │       -35.59 │    6 days, 23:19:00 │    0     0    31     0 │
│            TOTAL │             │     34 │         47.2 │        3718.760 │       371.88 │   100 days, 7:40:00 │    3     0    31   8.8 │
└──────────────────┴─────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────────┴────────────────────────┘
                             SUMMARY METRICS                              
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                                  ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00                    │
│ Backtesting to                │ 2025-09-11 17:00:00                    │
│ Trading Mode                  │ Spot                                   │
│ Max open trades               │ 3                                      │
│                               │                                        │
│ Total/Daily Avg Trades        │ 34 / 0.03                              │
│ Starting balance              │ 1000 USDT                              │
│ Final balance                 │ 4718.76 USDT                           │
│ Absolute profit               │ 3718.76 USDT                           │
│ Total profit %                │ 371.88%                                │
│ CAGR %                        │ 52.17%                                 │
│ Sortino                       │ 9.31                                   │
│ Sharpe                        │ 0.12                                   │
│ Calmar                        │ 14.80                                  │
│ SQN                           │ 1.39                                   │
│ Profit factor                 │ 11.45                                  │
│ Expectancy (Ratio)            │ 109.38 (9.53)                          │
│ Avg. daily profit             │ 2.757 USDT                             │
│ Avg. stake amount             │ 314.915 USDT                           │
│ Total trade volume            │ 25183.323 USDT                         │
│                               │                                        │
│ Best Pair                     │ BTC/USDT 190.20%                       │
│ Worst Pair                    │ LTC/USDT -5.34%                        │
│ Best trade                    │ XRP/USDT 846.87%                       │
│ Worst trade                   │ XRP/USDT -6.17%                        │
│ Best day                      │ 4074.66 USDT                           │
│ Worst day                     │ -23.117 USDT                           │
│ Days win/draw/lose            │ 1 / 1302 / 27                          │
│ Min/Max/Avg. Duration Winners │ 996d 12:00 / 1180d 06:00 / 1064d 22:00 │
│ Min/Max/Avg. Duration Losers  │ 0d 02:05 / 104d 17:20 / 6d 23:19       │
│ Max Consecutive Wins / Loss   │ 3 / 31                                 │
│ Rejected Entry signals        │ 504                                    │
│ Entry/Exit Timeouts           │ 0 / 0                                  │
│                               │                                        │
│ Min balance                   │ 644.1 USDT                             │
│ Max balance                   │ 4718.76 USDT                           │
│ Max % of account underwater   │ 35.59%                                 │
│ Absolute Drawdown (Account)   │ 35.59%                                 │
│ Absolute Drawdown             │ 355.9 USDT                             │
│ Drawdown high                 │ -20.441 USDT                           │
│ Drawdown low                  │ -355.9 USDT                            │
│ Drawdown Start                │ 2022-01-21 03:30:00                    │
│ Drawdown End                  │ 2022-11-20 11:15:00                    │
│ Market change                 │ 94.84%                                 │
└───────────────────────────────┴────────────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     34 │        47.20 │        3718.760 │       371.88 │ 100 days, 7:40:00 │    3     0    31   8.8 │ 355.9 USDT  35.59% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┴────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-01T21:50:29.674236",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 1208,
  "total_daily_avg_trades": "34 / 0.03",
  "absolute_profit_usdt": 3718.76,
  "total_profit_pct": 371.88,
  "cagr_pct": 52.17,
  "sortino": 9.31,
  "sharpe": 0.12,
  "calmar": 14.8,
  "sqn": 1.39,
  "max_consecutive_wins_loss": "3 / 31",
  "min_balance_usdt": 644.1,
  "max_balance_usdt": 4718.76,
  "market_change_pct": 94.84
}
```
