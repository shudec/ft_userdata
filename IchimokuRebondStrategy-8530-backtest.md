# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 8530  
**Timestamp:** 2025-10-02 22:29:15

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "pairs": [
    "ADA/USDT",
    "SOL/USDT",
    "DOGE/USDT",
    "TRX/USDT"
  ],
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 8530,
  "epochs": 100,
  "hyperopt_timerange": "20220101-20231231",
  "backtest_timerange": "20220101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs ADA/USDT SOL/USDT DOGE/USDT TRX/USDT --timerange 20220101-20251231 --export trades
```

## Backtesting Output
```
2025-10-02 20:17:57,030 - freqtrade - INFO - freqtrade 2025.7
2025-10-02 20:17:57,575 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-10-02 20:17:57,576 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-02 20:18:00,083 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-02 20:18:00,087 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-02 20:18:00,088 - freqtrade.loggers - INFO - Logfile configured
2025-10-02 20:18:00,088 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-02 20:18:00,089 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-10-02 20:18:00,090 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-02 20:18:00,090 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-02 20:18:00,091 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-10-02 20:18:00,112 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-02 20:18:00,113 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-02 20:18:00,114 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-02 20:18:00,114 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-02 20:18:00,115 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-02 20:18:00,115 - freqtrade.configuration.configuration - INFO - Using pairs ['ADA/USDT', 'SOL/USDT', 'DOGE/USDT', 'TRX/USDT']
2025-10-02 20:18:00,116 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-10-02 20:18:00,118 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-02 20:18:00,139 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-02 20:18:00,140 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-02 20:18:00,144 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-02 20:18:00,145 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-02 20:18:00,146 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-10-02 20:18:00,184 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-02 20:18:03,101 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-02 20:18:03,169 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-10-02 20:18:03,170 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-10-02 20:18:03,171 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-10-02 20:18:03,172 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-02 20:18:03,173 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-02 20:18:03,173 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-02 20:18:03,174 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-02 20:18:03,174 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-02 20:18:03,175 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-10-02 20:18:03,175 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-10-02 20:18:03,176 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-02 20:18:03,176 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-02 20:18:03,177 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-02 20:18:03,177 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-02 20:18:03,178 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-02 20:18:03,178 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-10-02 20:18:03,179 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-02 20:18:03,180 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-02 20:18:03,180 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-02 20:18:03,181 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-10-02 20:18:03,181 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-02 20:18:03,182 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-10-02 20:18:03,182 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-02 20:18:03,183 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-02 20:18:03,183 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-02 20:18:03,184 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-02 20:18:03,184 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-02 20:18:03,185 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-02 20:18:03,185 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-02 20:18:03,186 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-02 20:18:03,186 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-02 20:18:03,193 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-02 20:18:03,229 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-02 20:18:03,274 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-02 20:18:03,343 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-02 20:18:03,405 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-02 20:18:03,474 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-02 20:18:03,519 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-10-02 17:00:00 (1370 days).
2025-10-02 20:18:03,622 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-02 20:18:04,003 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-02 20:18:04,345 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-02 20:18:04,636 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-02 20:18:06,264 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-02 20:18:06,265 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-02 20:18:06,266 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-10-02 20:18:06,267 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.4
2025-10-02 20:18:06,267 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-10-02 20:18:06,267 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-10-02 20:18:06,268 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-10-02 20:18:06,268 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_strength_threshold = 0.02
2025-10-02 20:18:06,268 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 20
2025-10-02 20:18:06,269 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-10-02 20:18:06,269 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 1
2025-10-02 20:18:06,270 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-10-02 20:18:06,270 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.02
2025-10-02 20:18:06,270 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.003
2025-10-02 20:18:06,271 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_engulfing_signal_strength_threshold_max = 0.189
2025-10-02 20:18:06,271 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_engulfing_signal_strength_threshold_min = 0.757
2025-10-02 20:18:06,271 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_hammer_signal_strength_threshold_max = 0.213
2025-10-02 20:18:06,272 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_hammer_signal_strength_threshold_min = 0.273
2025-10-02 20:18:06,272 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_strong_bullish_signal_strength_threshold_max = 0.39
2025-10-02 20:18:06,273 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_strong_bullish_signal_strength_threshold_min = 0.091
2025-10-02 20:18:06,273 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-10-02 20:18:06,273 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-10-02 20:18:06,274 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_size_threshold = 2
2025-10-02 20:18:06,274 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_strength_threshold = 0.02
2025-10-02 20:18:06,274 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.409
2025-10-02 20:18:06,275 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.003
2025-10-02 20:18:06,275 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_engulfing_entry = False
2025-10-02 20:18:06,276 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_hammer_entry = False
2025-10-02 20:18:06,276 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_strong_bullish_entry = True
2025-10-02 20:18:06,277 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1
2025-10-02 20:18:06,277 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 0.5
2025-10-02 20:18:06,278 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-10-02 20:18:06,279 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-10-02 20:18:06,280 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 6
2025-10-02 20:18:06,281 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-10-02 20:18:06,282 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-10-02 20:18:06,282 - freqtrade.strategy.hyper - INFO - Strategy Parameter: trailing_custom_stop = False
2025-10-02 20:18:06,283 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-10-02 20:18:06,283 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-10-02 20:18:06,284 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-10-02 20:18:06,284 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = False
2025-10-02 20:18:06,284 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = False
2025-10-02 20:18:06,285 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-10-02 20:18:06,285 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-10-02 20:18:06,286 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-02 20:18:06,289 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 20:18:06,301 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-02 20:18:06,337 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 20:18:06,359 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-02 20:18:20,005 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 20:18:20,017 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-02 20:18:20,047 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 20:18:20,068 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-02 20:18:33,308 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 20:18:33,320 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-02 20:18:33,346 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 20:18:33,366 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-02 20:18:47,061 - freqtrade.data.dataprovider - INFO - Loading data for TRX/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 20:18:47,075 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-02 20:18:47,104 - freqtrade.data.dataprovider - INFO - Loading data for TRX/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 20:18:47,125 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-02 20:19:00,644 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-10-02 17:00:00 (1370 days).
2025-10-02 20:29:14,411 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-02_20-29-14.meta.json"
Result for strategy IchimokuRebondStrategy
                                                BACKTESTING REPORT                                                
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  ADA/USDT │    137 │         0.17 │          -4.955 │         -0.5 │  5 days, 3:39:00 │   48     0    89  35.0 │
│  SOL/USDT │    187 │         0.16 │         -31.614 │        -3.16 │ 3 days, 17:16:00 │   63     0   124  33.7 │
│  TRX/USDT │     38 │        -1.39 │        -136.470 │       -13.65 │ 6 days, 13:49:00 │   11     0    27  28.9 │
│ DOGE/USDT │    171 │         0.61 │        -180.667 │       -18.07 │  3 days, 6:04:00 │   56     0   115  32.7 │
│     TOTAL │    533 │          0.2 │        -353.706 │       -35.37 │  4 days, 3:24:00 │  178     0   355  33.4 │
└───────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                            LEFT OPEN TRADES REPORT                                            
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ADA/USDT │      1 │         3.38 │           8.827 │         0.88 │ 1 day, 8:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         3.38 │           8.827 │         0.88 │ 1 day, 8:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                       ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │     533 │          0.2 │        -353.706 │       -35.37 │ 4 days, 3:24:00 │  178     0   355  33.4 │
│                 TOTAL │     533 │          0.2 │        -353.706 │       -35.37 │ 4 days, 3:24:00 │  178     0   355  33.4 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │   177 │        13.94 │        4209.073 │       420.91 │ 5 days, 16:58:00 │  177     0     0   100 │
│     force_exit │     1 │         3.38 │           8.827 │         0.88 │   1 day, 8:00:00 │    1     0     0   100 │
│      stop_loss │   355 │        -6.66 │       -4571.606 │      -457.16 │  3 days, 8:52:00 │    0     0   355     0 │
│          TOTAL │   533 │          0.2 │        -353.706 │       -35.37 │  4 days, 3:24:00 │  178     0   355  33.4 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                                MIXED TAG STATS                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_2R │    177 │        13.94 │        4209.073 │       420.91 │ 5 days, 16:58:00 │  177     0     0   100 │
│ strong_bullish_rebond │     force_exit │      1 │         3.38 │           8.827 │         0.88 │   1 day, 8:00:00 │    1     0     0   100 │
│ strong_bullish_rebond │      stop_loss │    355 │        -6.66 │       -4571.606 │      -457.16 │  3 days, 8:52:00 │    0     0   355     0 │
│                 TOTAL │                │    533 │          0.2 │        -353.706 │       -35.37 │  4 days, 3:24:00 │  178     0   355  33.4 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00             │
│ Backtesting to                │ 2025-10-02 17:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 533 / 0.39                      │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 646.294 USDT                    │
│ Absolute profit               │ -353.706 USDT                   │
│ Total profit %                │ -35.37%                         │
│ CAGR %                        │ -10.98%                         │
│ Sortino                       │ -1.72                           │
│ Sharpe                        │ -0.28                           │
│ Calmar                        │ -0.83                           │
│ SQN                           │ -0.86                           │
│ Profit factor                 │ 0.92                            │
│ Expectancy (Ratio)            │ -0.66 (-0.05)                   │
│ Avg. daily profit             │ -0.258 USDT                     │
│ Avg. stake amount             │ 205.433 USDT                    │
│ Total trade volume            │ 219075.491 USDT                 │
│                               │                                 │
│ Best Pair                     │ ADA/USDT -0.50%                 │
│ Worst Pair                    │ DOGE/USDT -18.07%               │
│ Best trade                    │ DOGE/USDT 41.62%                │
│ Worst trade                   │ DOGE/USDT -15.26%               │
│ Best day                      │ 75.089 USDT                     │
│ Worst day                     │ -58.501 USDT                    │
│ Days win/draw/lose            │ 148 / 966 / 250                 │
│ Min/Max/Avg. Duration Winners │ 0d 03:35 / 93d 07:30 / 5d 16:23 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:30 / 58d 10:40 / 3d 08:52 │
│ Max Consecutive Wins / Loss   │ 9 / 15                          │
│ Rejected Entry signals        │ 547                             │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 405.732 USDT                    │
│ Max balance                   │ 979.437 USDT                    │
│ Max % of account underwater   │ 59.43%                          │
│ Absolute Drawdown (Account)   │ 59.43%                          │
│ Absolute Drawdown             │ 594.268 USDT                    │
│ Drawdown high                 │ -20.563 USDT                    │
│ Drawdown low                  │ -594.268 USDT                   │
│ Drawdown Start                │ 2022-01-08 17:40:00             │
│ Drawdown End                  │ 2022-12-28 05:40:00             │
│ Market change                 │ 99.71%                          │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-10-02 17:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    533 │         0.20 │        -353.706 │       -35.37 │ 4 days, 3:24:00 │  178     0   355  33.4 │ 594.268 USDT  59.43% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-02T22:29:15.840678",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 8530,
  "total_daily_avg_trades": "533 / 0.39",
  "absolute_profit_usdt": -353.706,
  "total_profit_pct": -35.37,
  "cagr_pct": -10.98,
  "sortino": -1.72,
  "sharpe": -0.28,
  "calmar": -0.83,
  "sqn": -0.86,
  "max_consecutive_wins_loss": "9 / 15",
  "min_balance_usdt": 405.732,
  "max_balance_usdt": 979.437,
  "market_change_pct": 99.71
}
```
