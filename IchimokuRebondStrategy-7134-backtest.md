# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 7134  
**Timestamp:** 2025-09-30 22:41:17

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 7134,
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
2025-09-30 20:39:19,653 - freqtrade - INFO - freqtrade 2025.7
2025-09-30 20:39:20,001 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-30 20:39:20,002 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-30 20:39:21,454 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-30 20:39:21,456 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-30 20:39:21,457 - freqtrade.loggers - INFO - Logfile configured
2025-09-30 20:39:21,457 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-30 20:39:21,458 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-30 20:39:21,458 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-30 20:39:21,458 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-30 20:39:21,458 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-30 20:39:21,466 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-30 20:39:21,467 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-30 20:39:21,467 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-30 20:39:21,468 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-09-30 20:39:21,468 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-30 20:39:21,468 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-30 20:39:21,469 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-30 20:39:21,470 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-30 20:39:21,489 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-30 20:39:21,490 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-30 20:39:21,493 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-30 20:39:21,494 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-30 20:39:21,495 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-30 20:39:21,527 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-30 20:39:24,158 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-30 20:39:24,199 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-30 20:39:24,200 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-30 20:39:24,200 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-30 20:39:24,201 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-30 20:39:24,201 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-30 20:39:24,202 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-30 20:39:24,202 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-30 20:39:24,202 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-30 20:39:24,203 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-30 20:39:24,203 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-30 20:39:24,203 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-30 20:39:24,204 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-30 20:39:24,204 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-30 20:39:24,204 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-30 20:39:24,205 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-30 20:39:24,205 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-30 20:39:24,205 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-30 20:39:24,206 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-30 20:39:24,206 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-30 20:39:24,206 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-30 20:39:24,207 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-30 20:39:24,208 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-30 20:39:24,208 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-30 20:39:24,209 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-30 20:39:24,209 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-30 20:39:24,210 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-30 20:39:24,210 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-30 20:39:24,211 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-30 20:39:24,211 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-30 20:39:24,212 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-30 20:39:24,212 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-30 20:39:24,217 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-30 20:39:24,250 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-30 20:39:24,281 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-30 20:39:24,330 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-30 20:39:24,384 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-30 20:39:24,436 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-30 20:39:24,484 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-30 20:39:24,511 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-30 20:39:24,582 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-30 20:39:24,812 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-30 20:39:25,038 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-30 20:39:25,284 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-30 20:39:25,498 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-30 20:39:26,759 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-30 20:39:26,760 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-30 20:39:26,761 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-30 20:39:26,761 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.4
2025-09-30 20:39:26,762 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-30 20:39:26,762 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-30 20:39:26,762 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-30 20:39:26,763 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_strength_threshold = 0.02
2025-09-30 20:39:26,763 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 5
2025-09-30 20:39:26,763 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-09-30 20:39:26,764 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 1
2025-09-30 20:39:26,764 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-09-30 20:39:26,764 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.02
2025-09-30 20:39:26,765 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.003
2025-09-30 20:39:26,765 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_signal_strength_threshold_max = 0.814
2025-09-30 20:39:26,765 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_signal_strength_threshold_min = 0.119
2025-09-30 20:39:26,766 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-30 20:39:26,766 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-30 20:39:26,766 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_size_threshold = 2
2025-09-30 20:39:26,767 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_strength_threshold = 0.02
2025-09-30 20:39:26,767 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.409
2025-09-30 20:39:26,767 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.003
2025-09-30 20:39:26,767 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_engulfing_entry = False
2025-09-30 20:39:26,768 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_hammer_entry = True
2025-09-30 20:39:26,768 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_strong_bullish_entry = False
2025-09-30 20:39:26,768 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1
2025-09-30 20:39:26,769 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 0.5
2025-09-30 20:39:26,769 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-09-30 20:39:26,770 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-30 20:39:26,770 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 6
2025-09-30 20:39:26,770 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-30 20:39:26,771 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-30 20:39:26,771 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-09-30 20:39:26,771 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-30 20:39:26,772 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-30 20:39:26,772 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = False
2025-09-30 20:39:26,772 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = False
2025-09-30 20:39:26,773 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-30 20:39:26,773 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-30 20:39:26,773 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-30 20:39:26,776 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-30 20:39:26,786 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-30 20:39:26,810 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-30 20:39:26,827 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-30 20:39:36,303 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-30 20:39:36,311 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-30 20:39:36,335 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-30 20:39:36,352 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-30 20:39:45,751 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-30 20:39:45,759 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-30 20:39:45,782 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-30 20:39:45,799 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-30 20:39:55,526 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-30 20:39:55,534 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-30 20:39:55,559 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-30 20:39:55,576 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-30 20:40:05,088 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-30 20:40:05,096 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-30 20:40:05,119 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-30 20:40:05,137 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-30 20:40:14,569 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-30 20:41:16,353 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-30_20-41-16.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ LTC/USDT │     63 │         1.87 │         172.893 │        17.29 │  1 day, 14:16:00 │   36     0    27  57.1 │
│ ETH/USDT │     50 │         0.77 │         134.891 │        13.49 │          9:19:00 │   29     0    21  58.0 │
│ BTC/USDT │     43 │         0.05 │          43.147 │         4.31 │   1 day, 7:09:00 │   21     0    22  48.8 │
│ XRP/USDT │     41 │        -0.43 │           6.821 │         0.68 │ 2 days, 18:04:00 │   20     0    21  48.8 │
│ BNB/USDT │     24 │         0.24 │         -30.554 │        -3.06 │  2 days, 1:01:00 │   12     0    12  50.0 │
│    TOTAL │    221 │         0.66 │         327.197 │        32.72 │  1 day, 12:39:00 │  118     0   103  53.4 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                   ENTER TAG STATS                                                    
┏━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ hammer_rebond │     221 │         0.66 │         327.197 │        32.72 │ 1 day, 12:39:00 │  118     0   103  53.4 │
│         TOTAL │     221 │         0.66 │         327.197 │        32.72 │ 1 day, 12:39:00 │  118     0   103  53.4 │
└───────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │   118 │         5.15 │        1800.732 │       180.07 │ 1 day, 21:54:00 │  118     0     0   100 │
│      stop_loss │   103 │        -4.48 │       -1473.535 │      -147.35 │  1 day, 2:04:00 │    0     0   103     0 │
│          TOTAL │   221 │         0.66 │         327.197 │        32.72 │ 1 day, 12:39:00 │  118     0   103  53.4 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                           MIXED TAG STATS                                                            
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ hammer_rebond │ take_profit_1R │    118 │         5.15 │        1800.732 │       180.07 │ 1 day, 21:54:00 │  118     0     0   100 │
│ hammer_rebond │      stop_loss │    103 │        -4.48 │       -1473.535 │      -147.35 │  1 day, 2:04:00 │    0     0   103     0 │
│         TOTAL │                │    221 │         0.66 │         327.197 │        32.72 │ 1 day, 12:39:00 │  118     0   103  53.4 │
└───────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00             │
│ Backtesting to                │ 2025-09-11 17:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 221 / 0.16                      │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 1327.197 USDT                   │
│ Absolute profit               │ 327.197 USDT                    │
│ Total profit %                │ 32.72%                          │
│ CAGR %                        │ 7.96%                           │
│ Sortino                       │ 0.58                            │
│ Sharpe                        │ 0.27                            │
│ Calmar                        │ 3.07                            │
│ SQN                           │ 1.29                            │
│ Profit factor                 │ 1.22                            │
│ Expectancy (Ratio)            │ 1.48 (0.10)                     │
│ Avg. daily profit             │ 0.243 USDT                      │
│ Avg. stake amount             │ 382.722 USDT                    │
│ Total trade volume            │ 169829.68 USDT                  │
│                               │                                 │
│ Best Pair                     │ LTC/USDT 17.29%                 │
│ Worst Pair                    │ BNB/USDT -3.06%                 │
│ Best trade                    │ XRP/USDT 21.56%                 │
│ Worst trade                   │ XRP/USDT -43.10%                │
│ Best day                      │ 53.67 USDT                      │
│ Worst day                     │ -65.358 USDT                    │
│ Days win/draw/lose            │ 74 / 1171 / 62                  │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 35d 03:50 / 1d 21:54 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 34d 23:40 / 1d 02:04 │
│ Max Consecutive Wins / Loss   │ 11 / 8                          │
│ Rejected Entry signals        │ 112                             │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 849.245 USDT                    │
│ Max balance                   │ 1333.524 USDT                   │
│ Max % of account underwater   │ 15.08%                          │
│ Absolute Drawdown (Account)   │ 15.08%                          │
│ Absolute Drawdown             │ 150.755 USDT                    │
│ Drawdown high                 │ -15.838 USDT                    │
│ Drawdown low                  │ -150.755 USDT                   │
│ Drawdown Start                │ 2022-01-07 15:50:00             │
│ Drawdown End                  │ 2022-06-15 09:20:00             │
│ Market change                 │ 94.84%                          │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    221 │         0.66 │         327.197 │        32.72 │ 1 day, 12:39:00 │  118     0   103  53.4 │ 150.755 USDT  15.08% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-30T22:41:17.529031",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 7134,
  "total_daily_avg_trades": "221 / 0.16",
  "absolute_profit_usdt": 327.197,
  "total_profit_pct": 32.72,
  "cagr_pct": 7.96,
  "sortino": 0.58,
  "sharpe": 0.27,
  "calmar": 3.07,
  "sqn": 1.29,
  "max_consecutive_wins_loss": "11 / 8",
  "min_balance_usdt": 849.245,
  "max_balance_usdt": 1333.524,
  "market_change_pct": 94.84,
  "win_draw_loss_winpct": "0 0 0 0"
}
```
