# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 6752  
**Timestamp:** 2025-09-25 20:58:40

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 6752,
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
2025-09-25 18:57:31,880 - freqtrade - INFO - freqtrade 2025.7
2025-09-25 18:57:32,213 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-25 18:57:32,214 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-25 18:57:33,699 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-25 18:57:33,701 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-25 18:57:33,702 - freqtrade.loggers - INFO - Logfile configured
2025-09-25 18:57:33,702 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-25 18:57:33,703 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-25 18:57:33,703 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-25 18:57:33,703 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-25 18:57:33,704 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20240101-20251231 ...
2025-09-25 18:57:33,711 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-25 18:57:33,712 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-25 18:57:33,712 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-25 18:57:33,713 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-25 18:57:33,713 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-25 18:57:33,714 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20240101-20251231
2025-09-25 18:57:33,715 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-25 18:57:33,736 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-25 18:57:33,736 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 18:57:33,740 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-25 18:57:33,741 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-25 18:57:33,741 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-25 18:57:33,773 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-25 18:57:36,292 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-25 18:57:36,346 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-25 18:57:36,347 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-25 18:57:36,349 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-25 18:57:36,349 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-25 18:57:36,350 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-25 18:57:36,351 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-25 18:57:36,352 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-25 18:57:36,352 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-25 18:57:36,353 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-25 18:57:36,353 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-25 18:57:36,354 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-25 18:57:36,354 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-25 18:57:36,355 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-25 18:57:36,355 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-25 18:57:36,356 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-25 18:57:36,356 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-25 18:57:36,357 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-25 18:57:36,357 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-25 18:57:36,358 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-25 18:57:36,358 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-25 18:57:36,359 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-25 18:57:36,359 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-25 18:57:36,360 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-25 18:57:36,360 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-25 18:57:36,361 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-25 18:57:36,361 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-25 18:57:36,361 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-25 18:57:36,362 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-25 18:57:36,362 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-25 18:57:36,363 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-25 18:57:36,364 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 18:57:36,369 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-25 18:57:36,407 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-25 18:57:36,444 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-25 18:57:36,489 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-25 18:57:36,530 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-25 18:57:36,567 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-25 18:57:36,605 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-25 18:57:36,622 - freqtrade.optimize.backtesting - INFO - Loading data from 2024-01-01 00:00:00 up to 2025-09-11 17:00:00 (619 days).
2025-09-25 18:57:36,698 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-25 18:57:36,854 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-25 18:57:37,041 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-25 18:57:37,210 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-25 18:57:37,372 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-25 18:57:38,042 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-25 18:57:38,043 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-25 18:57:38,043 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-25 18:57:38,044 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.25
2025-09-25 18:57:38,044 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-25 18:57:38,044 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-25 18:57:38,045 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-25 18:57:38,045 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 20
2025-09-25 18:57:38,045 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 1
2025-09-25 18:57:38,046 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 1
2025-09-25 18:57:38,046 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-09-25 18:57:38,046 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.001
2025-09-25 18:57:38,047 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-25 18:57:38,047 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-25 18:57:38,047 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-25 18:57:38,048 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.5
2025-09-25 18:57:38,048 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.0
2025-09-25 18:57:38,048 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 2
2025-09-25 18:57:38,049 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1
2025-09-25 18:57:38,049 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-09-25 18:57:38,049 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-25 18:57:38,050 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 4
2025-09-25 18:57:38,050 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-25 18:57:38,050 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-25 18:57:38,051 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-09-25 18:57:38,051 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-25 18:57:38,051 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = atr
2025-09-25 18:57:38,052 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-09-25 18:57:38,052 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-25 18:57:38,052 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-25 18:57:38,053 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-25 18:57:38,053 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-25 18:57:38,055 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 18:57:38,063 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-25 18:57:38,085 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 18:57:38,103 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-25 18:57:41,303 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 18:57:41,311 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-25 18:57:41,329 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 18:57:41,347 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-25 18:57:44,772 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 18:57:44,779 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-25 18:57:44,797 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 18:57:44,815 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-25 18:57:48,011 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 18:57:48,019 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-25 18:57:48,038 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 18:57:48,055 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-25 18:57:51,020 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 18:57:51,028 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-25 18:57:51,048 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 18:57:51,065 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-25 18:57:54,036 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2024-01-01 00:00:00 up to 2025-09-11 17:00:00 (619 days).
2025-09-25 18:58:39,805 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-25_18-58-39.meta.json"
Result for strategy IchimokuRebondStrategy
                                                BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │     10 │         3.96 │         155.883 │        15.59 │  18 days, 7:46:00 │    5     0     5  50.0 │
│ BNB/USDT │      5 │         5.75 │         106.466 │        10.65 │  19 days, 9:14:00 │    3     0     2  60.0 │
│ ETH/USDT │      6 │         5.08 │         103.865 │        10.39 │   6 days, 5:00:00 │    3     0     3  50.0 │
│ LTC/USDT │      4 │         0.17 │          -1.184 │        -0.12 │    1 day, 9:50:00 │    1     0     3  25.0 │
│ XRP/USDT │      1 │        -5.19 │         -23.021 │         -2.3 │   1 day, 10:45:00 │    0     0     1     0 │
│    TOTAL │     26 │         3.63 │         342.009 │         34.2 │ 12 days, 11:32:00 │   12     0    14  46.2 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         8.18 │          22.433 │         2.24 │ 31 days, 14:00:00 │    1     0     0   100 │
│ BTC/USDT │      1 │         4.62 │          20.930 │         2.09 │ 66 days, 19:00:00 │    1     0     0   100 │
│    TOTAL │      2 │          6.4 │          43.363 │         4.34 │  49 days, 4:30:00 │    2     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                        ENTER TAG STATS                                                         
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │      17 │         3.45 │         172.642 │        17.26 │  14 days, 4:00:00 │    8     0     9  47.1 │
│      engulfing_rebond │       9 │         3.96 │         169.367 │        16.94 │   9 days, 7:06:00 │    4     0     5  44.4 │
│                 TOTAL │      26 │         3.63 │         342.009 │         34.2 │ 12 days, 11:32:00 │   12     0    14  46.2 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                   EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │    10 │        15.41 │         597.948 │        59.79 │  15 days, 2:05:00 │   10     0     0   100 │
│     force_exit │     2 │          6.4 │          43.363 │         4.34 │  49 days, 4:30:00 │    2     0     0   100 │
│      stop_loss │    14 │        -5.19 │        -299.303 │       -29.93 │   5 days, 9:01:00 │    0     0    14     0 │
│          TOTAL │    26 │         3.63 │         342.009 │         34.2 │ 12 days, 11:32:00 │   12     0    14  46.2 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                                MIXED TAG STATS                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_3R │      6 │        15.42 │         325.772 │        32.58 │ 13 days, 16:33:00 │    6     0     0   100 │
│      engulfing_rebond │ take_profit_3R │      4 │         15.4 │         272.176 │        27.22 │  17 days, 4:22:00 │    4     0     0   100 │
│ strong_bullish_rebond │     force_exit │      2 │          6.4 │          43.363 │         4.34 │  49 days, 4:30:00 │    2     0     0   100 │
│      engulfing_rebond │      stop_loss │      5 │        -5.19 │        -102.809 │       -10.28 │  2 days, 23:41:00 │    0     0     5     0 │
│ strong_bullish_rebond │      stop_loss │      9 │        -5.19 │        -196.493 │       -19.65 │  6 days, 16:52:00 │    0     0     9     0 │
│                 TOTAL │                │     26 │         3.63 │         342.009 │         34.2 │ 12 days, 11:32:00 │   12     0    14  46.2 │
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
│ Total/Daily Avg Trades        │ 26 / 0.04                        │
│ Starting balance              │ 1000 USDT                        │
│ Final balance                 │ 1342.009 USDT                    │
│ Absolute profit               │ 342.009 USDT                     │
│ Total profit %                │ 34.20%                           │
│ CAGR %                        │ 18.94%                           │
│ Sortino                       │ 2.16                             │
│ Sharpe                        │ 0.27                             │
│ Calmar                        │ 9.11                             │
│ SQN                           │ 1.66                             │
│ Profit factor                 │ 2.14                             │
│ Expectancy (Ratio)            │ 13.15 (0.62)                     │
│ Avg. daily profit             │ 0.553 USDT                       │
│ Avg. stake amount             │ 398.435 USDT                     │
│ Total trade volume            │ 21102.782 USDT                   │
│                               │                                  │
│ Best Pair                     │ BTC/USDT 15.59%                  │
│ Worst Pair                    │ XRP/USDT -2.30%                  │
│ Best trade                    │ LTC/USDT 16.24%                  │
│ Worst trade                   │ ETH/USDT -5.19%                  │
│ Best day                      │ 124.361 USDT                     │
│ Worst day                     │ -25.652 USDT                     │
│ Days win/draw/lose            │ 10 / 540 / 14                    │
│ Min/Max/Avg. Duration Winners │ 3d 00:20 / 66d 19:00 / 20d 18:29 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:05 / 32d 20:45 / 5d 09:01  │
│ Max Consecutive Wins / Loss   │ 3 / 7                            │
│ Rejected Entry signals        │ 0                                │
│ Entry/Exit Timeouts           │ 0 / 0                            │
│                               │                                  │
│ Min balance                   │ 994.27 USDT                      │
│ Max balance                   │ 1342.009 USDT                    │
│ Max % of account underwater   │ 11.59%                           │
│ Absolute Drawdown (Account)   │ 11.59%                           │
│ Absolute Drawdown             │ 130.332 USDT                     │
│ Drawdown high                 │ 124.602 USDT                     │
│ Drawdown low                  │ -5.73 USDT                       │
│ Drawdown Start                │ 2024-03-04 17:30:00              │
│ Drawdown End                  │ 2024-10-23 16:20:00              │
│ Market change                 │ 178.91%                          │
└───────────────────────────────┴──────────────────────────────────┘

Backtested 2024-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                    
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     26 │         3.63 │         342.009 │         34.2 │ 12 days, 11:32:00 │   12     0    14  46.2 │ 130.332 USDT  11.59% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-25T20:58:40.872619",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 6752,
  "total_daily_avg_trades": "26 / 0.04",
  "absolute_profit_usdt": 342.009,
  "total_profit_pct": 34.2,
  "cagr_pct": 18.94,
  "sortino": 2.16,
  "sharpe": 0.27,
  "calmar": 9.11,
  "sqn": 1.66,
  "max_consecutive_wins_loss": "3 / 7",
  "min_balance_usdt": 994.27,
  "max_balance_usdt": 1342.009,
  "market_change_pct": 178.91
}
```
