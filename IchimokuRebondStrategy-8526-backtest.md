# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 8526  
**Timestamp:** 2025-09-29 17:28:39

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 8526,
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
2025-09-29 15:22:06,030 - freqtrade - INFO - freqtrade 2025.8
2025-09-29 15:22:06,730 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-29 15:22:09,429 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-29 15:22:09,436 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-29 15:22:09,436 - freqtrade.loggers - INFO - Logfile configured
2025-09-29 15:22:09,437 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-29 15:22:09,437 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-29 15:22:09,438 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-29 15:22:09,438 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-29 15:22:09,439 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-29 15:22:10,134 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-29 15:22:10,137 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-29 15:22:10,137 - freqtrade.configuration.configuration - INFO - Storing backtest results to backtest-result.csv ...
2025-09-29 15:22:10,137 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-29 15:22:10,138 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-09-29 15:22:10,138 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-29 15:22:10,139 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-29 15:22:10,139 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-29 15:22:10,141 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-29 15:22:10,156 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-29 15:22:10,157 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-29 15:22:10,160 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-29 15:22:10,160 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-29 15:22:10,161 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-29 15:22:10,185 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-29 15:22:12,542 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-29 15:22:12,678 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-29 15:22:12,680 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-29 15:22:12,687 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-29 15:22:12,687 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-29 15:22:12,688 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-29 15:22:12,688 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-29 15:22:12,688 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-29 15:22:12,689 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-29 15:22:12,690 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-29 15:22:12,690 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-29 15:22:12,691 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-29 15:22:12,691 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-29 15:22:12,691 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-29 15:22:12,692 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-29 15:22:12,692 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-29 15:22:12,692 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-29 15:22:12,693 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-29 15:22:12,693 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-29 15:22:12,693 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-29 15:22:12,694 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-29 15:22:12,694 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-29 15:22:12,694 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-29 15:22:12,695 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-29 15:22:12,695 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-29 15:22:12,696 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-29 15:22:12,697 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-29 15:22:12,697 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-29 15:22:12,697 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-29 15:22:12,698 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-29 15:22:12,698 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-29 15:22:12,698 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-29 15:22:12,723 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-29 15:22:12,748 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-29 15:22:12,904 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-29 15:22:13,003 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-29 15:22:13,070 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-29 15:22:13,129 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-29 15:22:13,185 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-29 15:22:13,207 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-29 15:22:13,467 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-29 15:22:13,862 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-29 15:22:14,224 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-29 15:22:14,598 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-29 15:22:14,954 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-29 15:22:16,128 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-29 15:22:16,134 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-29 15:22:16,135 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-29 15:22:16,135 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.4
2025-09-29 15:22:16,136 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-29 15:22:16,136 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-29 15:22:16,137 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-29 15:22:16,137 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_strength_threshold = 0.02
2025-09-29 15:22:16,137 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 5
2025-09-29 15:22:16,138 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-09-29 15:22:16,138 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 1
2025-09-29 15:22:16,138 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-09-29 15:22:16,139 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.02
2025-09-29 15:22:16,139 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.003
2025-09-29 15:22:16,139 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-29 15:22:16,140 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-29 15:22:16,140 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_size_threshold = 2
2025-09-29 15:22:16,140 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_strength_threshold = 0.02
2025-09-29 15:22:16,141 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.409
2025-09-29 15:22:16,141 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.003
2025-09-29 15:22:16,142 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_engulfing_entry = False
2025-09-29 15:22:16,143 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_hammer_entry = True
2025-09-29 15:22:16,143 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_strong_bullish_entry = False
2025-09-29 15:22:16,144 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 2.5
2025-09-29 15:22:16,144 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 0.5
2025-09-29 15:22:16,145 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-09-29 15:22:16,145 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-29 15:22:16,146 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 6
2025-09-29 15:22:16,146 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-29 15:22:16,146 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-29 15:22:16,147 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-09-29 15:22:16,147 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-29 15:22:16,147 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-29 15:22:16,148 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-09-29 15:22:16,148 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-29 15:22:16,148 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-29 15:22:16,149 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-29 15:22:16,149 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-29 15:22:16,151 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 15:22:16,166 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-29 15:22:16,192 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 15:22:16,214 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-29 15:22:26,033 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 15:22:26,050 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-29 15:22:26,067 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 15:22:26,089 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-29 15:22:35,745 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 15:22:35,762 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-29 15:22:35,780 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 15:22:35,803 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-15 00:00:00
2025-09-29 15:22:45,584 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 15:22:45,615 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-29 15:22:45,633 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 15:22:45,657 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-29 15:22:55,389 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 15:22:55,406 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-29 15:22:55,426 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-29 15:22:55,450 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-29 15:23:05,439 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-29 15:28:38,377 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-29_15-28-38.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │    140 │         0.34 │         140.600 │        14.06 │  1 day, 19:13:00 │   56     0    84  40.0 │
│ BNB/USDT │     65 │          0.8 │           9.314 │         0.93 │ 2 days, 18:18:00 │   26     0    39  40.0 │
│ BTC/USDT │     77 │        -0.15 │        -102.983 │        -10.3 │ 3 days, 12:42:00 │   29     0    48  37.7 │
│ XRP/USDT │    188 │        -0.14 │        -141.400 │       -14.14 │  2 days, 4:58:00 │   75     0   113  39.9 │
│ LTC/USDT │    187 │         0.13 │        -226.778 │       -22.68 │ 2 days, 11:31:00 │   68     0   119  36.4 │
│    TOTAL │    657 │         0.13 │        -321.248 │       -32.12 │  2 days, 9:48:00 │  254     0   403  38.7 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ LTC/USDT │      1 │        -0.53 │          -0.635 │        -0.06 │ 52 days, 9:00:00 │    0     0     1     0 │
│    TOTAL │      1 │        -0.53 │          -0.635 │        -0.06 │ 52 days, 9:00:00 │    0     0     1     0 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                   ENTER TAG STATS                                                    
┏━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ hammer_rebond │     657 │         0.13 │        -321.248 │       -32.12 │ 2 days, 9:48:00 │  254     0   403  38.7 │
│         TOTAL │     657 │         0.13 │        -321.248 │       -32.12 │ 2 days, 9:48:00 │  254     0   403  38.7 │
└───────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                   EXIT REASON STATS                                                    
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │   254 │         6.47 │        4226.807 │       422.68 │ 2 days, 23:53:00 │  254     0     0   100 │
│       force_exit │     1 │        -0.53 │          -0.635 │        -0.06 │ 52 days, 9:00:00 │    0     0     1     0 │
│        stop_loss │   402 │        -3.88 │       -4547.419 │      -454.74 │  1 day, 21:54:00 │    0     0   402     0 │
│            TOTAL │   657 │         0.13 │        -321.248 │       -32.12 │  2 days, 9:48:00 │  254     0   403  38.7 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                             MIXED TAG STATS                                                             
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ hammer_rebond │ take_profit_1.5R │    254 │         6.47 │        4226.807 │       422.68 │ 2 days, 23:53:00 │  254     0     0   100 │
│ hammer_rebond │       force_exit │      1 │        -0.53 │          -0.635 │        -0.06 │ 52 days, 9:00:00 │    0     0     1     0 │
│ hammer_rebond │        stop_loss │    402 │        -3.88 │       -4547.419 │      -454.74 │  1 day, 21:54:00 │    0     0   402     0 │
│         TOTAL │                  │    657 │         0.13 │        -321.248 │       -32.12 │  2 days, 9:48:00 │  254     0   403  38.7 │
└───────────────┴──────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00             │
│ Backtesting to                │ 2025-09-10 08:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 657 / 0.49                      │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 678.752 USDT                    │
│ Absolute profit               │ -321.248 USDT                   │
│ Total profit %                │ -32.12%                         │
│ CAGR %                        │ -9.96%                          │
│ Sortino                       │ -0.97                           │
│ Sharpe                        │ -0.31                           │
│ Calmar                        │ -1.15                           │
│ SQN                           │ -0.84                           │
│ Profit factor                 │ 0.93                            │
│ Expectancy (Ratio)            │ -0.49 (-0.04)                   │
│ Avg. daily profit             │ -0.238 USDT                     │
│ Avg. stake amount             │ 309.058 USDT                    │
│ Total trade volume            │ 406592.993 USDT                 │
│                               │                                 │
│ Best Pair                     │ ETH/USDT 14.06%                 │
│ Worst Pair                    │ LTC/USDT -22.68%                │
│ Best trade                    │ XRP/USDT 26.28%                 │
│ Worst trade                   │ XRP/USDT -30.89%                │
│ Best day                      │ 70.048 USDT                     │
│ Worst day                     │ -72.1 USDT                      │
│ Days win/draw/lose            │ 187 / 914 / 242                 │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 56d 03:00 / 2d 23:53 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 63d 02:25 / 2d 00:55 │
│ Max Consecutive Wins / Loss   │ 8 / 15                          │
│ Rejected Entry signals        │ 1337                            │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 605.853 USDT                    │
│ Max balance                   │ 1002.181 USDT                   │
│ Max % of account underwater   │ 39.55%                          │
│ Absolute drawdown             │ 396.328 USDT (39.55%)           │
│ Drawdown duration             │ 620 days 15:55:00               │
│ Profit at drawdown start      │ 2.181 USDT                      │
│ Profit at drawdown end        │ -394.147 USDT                   │
│ Drawdown start                │ 2022-03-24 15:45:00             │
│ Drawdown end                  │ 2023-12-05 07:40:00             │
│ Market change                 │ 91.49%                          │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    657 │         0.13 │        -321.248 │       -32.12 │ 2 days, 9:48:00 │  254     0   403  38.7 │ 396.328 USDT  39.55% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-29T17:28:39.664319",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 8526,
  "total_daily_avg_trades": "657 / 0.49",
  "absolute_profit_usdt": -321.248,
  "total_profit_pct": -32.12,
  "cagr_pct": -9.96,
  "sortino": -0.97,
  "sharpe": -0.31,
  "calmar": -1.15,
  "sqn": -0.84,
  "max_consecutive_wins_loss": "8 / 15",
  "min_balance_usdt": 605.853,
  "max_balance_usdt": 1002.181,
  "absolute_drawdown_pct": 39.55,
  "market_change_pct": 91.49
}
```
