# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 2036  
**Timestamp:** 2025-10-02 21:12:37

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
  "random_state": 2036,
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
2025-10-02 19:11:45,228 - freqtrade - INFO - freqtrade 2025.7
2025-10-02 19:11:45,628 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-10-02 19:11:45,629 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-10-02 19:11:47,215 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-10-02 19:11:47,219 - freqtrade.loggers - INFO - Enabling colorized output.
2025-10-02 19:11:47,220 - freqtrade.loggers - INFO - Logfile configured
2025-10-02 19:11:47,220 - freqtrade.loggers - INFO - Verbosity set to 0
2025-10-02 19:11:47,221 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-10-02 19:11:47,221 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-10-02 19:11:47,222 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-10-02 19:11:47,222 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-10-02 19:11:47,233 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-10-02 19:11:47,235 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-10-02 19:11:47,236 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-10-02 19:11:47,236 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-10-02 19:11:47,237 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-10-02 19:11:47,238 - freqtrade.configuration.configuration - INFO - Using pairs ['ADA/USDT', 'SOL/USDT', 'DOGE/USDT', 'TRX/USDT']
2025-10-02 19:11:47,239 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-10-02 19:11:47,241 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-10-02 19:11:47,270 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-10-02 19:11:47,271 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-02 19:11:47,277 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-10-02 19:11:47,278 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-10-02 19:11:47,279 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-10-02 19:11:47,318 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-10-02 19:11:50,160 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-10-02 19:11:50,202 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-10-02 19:11:50,203 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-10-02 19:11:50,204 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-10-02 19:11:50,204 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-10-02 19:11:50,205 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-10-02 19:11:50,205 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-10-02 19:11:50,206 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-10-02 19:11:50,206 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-10-02 19:11:50,206 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-10-02 19:11:50,207 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-10-02 19:11:50,207 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-10-02 19:11:50,207 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-10-02 19:11:50,208 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-10-02 19:11:50,208 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-10-02 19:11:50,208 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-10-02 19:11:50,209 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-10-02 19:11:50,210 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-10-02 19:11:50,210 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-10-02 19:11:50,210 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-10-02 19:11:50,211 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-10-02 19:11:50,211 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-10-02 19:11:50,212 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-10-02 19:11:50,212 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-10-02 19:11:50,212 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-10-02 19:11:50,213 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-10-02 19:11:50,213 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-10-02 19:11:50,213 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-10-02 19:11:50,214 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-10-02 19:11:50,214 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-10-02 19:11:50,215 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-10-02 19:11:50,215 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-10-02 19:11:50,220 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-10-02 19:11:50,248 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-10-02 19:11:50,280 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-02 19:11:50,328 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-02 19:11:50,381 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-02 19:11:50,426 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 1h, data ends at 2025-10-02 17:00:00
2025-10-02 19:11:50,465 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-10-02 17:00:00 (1370 days).
2025-10-02 19:11:50,547 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-02 19:11:50,774 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-02 19:11:51,013 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-02 19:11:51,242 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 5m, data ends at 2025-10-02 18:50:00
2025-10-02 19:11:52,415 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-10-02 19:11:52,416 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-10-02 19:11:52,416 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-10-02 19:11:52,417 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.4
2025-10-02 19:11:52,417 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-10-02 19:11:52,417 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-10-02 19:11:52,418 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-10-02 19:11:52,418 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_strength_threshold = 0.02
2025-10-02 19:11:52,418 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 20
2025-10-02 19:11:52,419 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-10-02 19:11:52,419 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 1
2025-10-02 19:11:52,419 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-10-02 19:11:52,420 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.02
2025-10-02 19:11:52,420 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.003
2025-10-02 19:11:52,420 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_engulfing_signal_strength_threshold_max = 0.132
2025-10-02 19:11:52,421 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_engulfing_signal_strength_threshold_min = 0.071
2025-10-02 19:11:52,421 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_hammer_signal_strength_threshold_max = 0.431
2025-10-02 19:11:52,421 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_hammer_signal_strength_threshold_min = 0.254
2025-10-02 19:11:52,421 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): ml_strong_bullish_signal_strength_threshold_max = 0.5
2025-10-02 19:11:52,422 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): ml_strong_bullish_signal_strength_threshold_min = 0.5
2025-10-02 19:11:52,422 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-10-02 19:11:52,422 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-10-02 19:11:52,423 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_size_threshold = 2
2025-10-02 19:11:52,423 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_strength_threshold = 0.02
2025-10-02 19:11:52,423 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.409
2025-10-02 19:11:52,424 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.003
2025-10-02 19:11:52,424 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_engulfing_entry = False
2025-10-02 19:11:52,424 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_hammer_entry = False
2025-10-02 19:11:52,425 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_strong_bullish_entry = True
2025-10-02 19:11:52,425 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0
2025-10-02 19:11:52,425 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 0.5
2025-10-02 19:11:52,426 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-10-02 19:11:52,426 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-10-02 19:11:52,427 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 6
2025-10-02 19:11:52,427 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-10-02 19:11:52,427 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-10-02 19:11:52,428 - freqtrade.strategy.hyper - INFO - Strategy Parameter: trailing_custom_stop = False
2025-10-02 19:11:52,428 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = False
2025-10-02 19:11:52,429 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-10-02 19:11:52,429 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-10-02 19:11:52,429 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = False
2025-10-02 19:11:52,430 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = False
2025-10-02 19:11:52,430 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-10-02 19:11:52,430 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-10-02 19:11:52,431 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-10-02 19:11:52,433 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:11:52,443 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-02 19:11:52,476 - freqtrade.data.dataprovider - INFO - Loading data for ADA/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:11:52,496 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ADA/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-02 19:12:02,872 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:12:02,878 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-02 19:12:02,903 - freqtrade.data.dataprovider - INFO - Loading data for SOL/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:12:02,920 - freqtrade.data.history.datahandlers.idatahandler - WARNING - SOL/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-02 19:12:13,434 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:12:13,442 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-02 19:12:13,468 - freqtrade.data.dataprovider - INFO - Loading data for DOGE/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:12:13,485 - freqtrade.data.history.datahandlers.idatahandler - WARNING - DOGE/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-02 19:12:23,805 - freqtrade.data.dataprovider - INFO - Loading data for TRX/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:12:23,813 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 1d, data ends at 2025-10-01 00:00:00
2025-10-02 19:12:23,841 - freqtrade.data.dataprovider - INFO - Loading data for TRX/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-10-02 19:12:23,859 - freqtrade.data.history.datahandlers.idatahandler - WARNING - TRX/USDT, spot, 4h, data ends at 2025-10-02 12:00:00
2025-10-02 19:12:34,467 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-10-02 17:00:00 (1370 days).
2025-10-02 19:12:36,064 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-10-02_19-12-36.meta.json"
Result for strategy IchimokuRebondStrategy
                                              BACKTESTING REPORT                                              
┏━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  ADA/USDT │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
│  SOL/USDT │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
│ DOGE/USDT │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
│  TRX/USDT │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
│     TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                ENTER TAG STATS                                                
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     TOTAL │       0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                               EXIT REASON STATS                                               
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│       TOTAL │     0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                      MIXED TAG STATS                                                       
┏━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     TOTAL │             │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────────┴─────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
No trades made. Your starting balance was 1000 USDT, and your stake was unlimited.

Backtested 2022-01-01 00:00:00 -> 2025-10-02 17:00:00 | Max open trades : 3
                                                             STRATEGY SUMMARY                                                              
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃      Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │      0 │         0.00 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │ 0 USDT  0.00% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴───────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-10-02T21:12:37.091069",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 2036,
  "win_draw_loss_winpct": "0 0 0 0"
}
```
