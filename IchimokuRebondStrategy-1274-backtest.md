# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 1274  
**Timestamp:** 2025-09-25 20:36:04

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 1274,
  "epochs": 100,
  "hyperopt_timerange": "20220101-20231231",
  "backtest_timerange": "20220101-20231231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20231231
```

## Backtesting Output
```
2025-09-25 18:33:13,523 - freqtrade - INFO - freqtrade 2025.7
2025-09-25 18:33:13,858 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-25 18:33:13,859 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-25 18:33:15,592 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-25 18:33:15,595 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-25 18:33:15,596 - freqtrade.loggers - INFO - Logfile configured
2025-09-25 18:33:15,596 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-25 18:33:15,597 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-25 18:33:15,597 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-25 18:33:15,598 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-25 18:33:15,598 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20231231 ...
2025-09-25 18:33:15,606 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-25 18:33:15,608 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-25 18:33:15,608 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-25 18:33:15,609 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-25 18:33:15,609 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-25 18:33:15,610 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20231231
2025-09-25 18:33:15,611 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-25 18:33:15,635 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-25 18:33:15,637 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 18:33:15,641 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-25 18:33:15,643 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-25 18:33:15,643 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-25 18:33:15,678 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-25 18:33:18,209 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-25 18:33:18,254 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-25 18:33:18,255 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-25 18:33:18,256 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-25 18:33:18,257 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-25 18:33:18,257 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-25 18:33:18,257 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-25 18:33:18,258 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-25 18:33:18,258 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-25 18:33:18,259 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-25 18:33:18,259 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-25 18:33:18,260 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-25 18:33:18,260 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-25 18:33:18,260 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-25 18:33:18,261 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-25 18:33:18,261 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-25 18:33:18,262 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-25 18:33:18,262 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-25 18:33:18,263 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-25 18:33:18,263 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-25 18:33:18,263 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-25 18:33:18,264 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-25 18:33:18,264 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-25 18:33:18,265 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-25 18:33:18,265 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-25 18:33:18,265 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-25 18:33:18,266 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-25 18:33:18,266 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-25 18:33:18,267 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-25 18:33:18,267 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-25 18:33:18,267 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-25 18:33:18,268 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 18:33:18,273 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-25 18:33:18,307 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-25 18:33:18,546 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2023-12-31 00:00:00 (729 days).
2025-09-25 18:33:20,172 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-25 18:33:20,176 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-25 18:33:20,177 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.25
2025-09-25 18:33:20,177 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-25 18:33:20,177 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-25 18:33:20,178 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-25 18:33:20,178 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 5
2025-09-25 18:33:20,179 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 1
2025-09-25 18:33:20,179 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 1
2025-09-25 18:33:20,179 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-09-25 18:33:20,180 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.001
2025-09-25 18:33:20,180 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.01
2025-09-25 18:33:20,181 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-25 18:33:20,181 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-25 18:33:20,181 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.5
2025-09-25 18:33:20,182 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.01
2025-09-25 18:33:20,182 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.25
2025-09-25 18:33:20,182 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1.5
2025-09-25 18:33:20,183 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5.5
2025-09-25 18:33:20,183 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-25 18:33:20,184 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 8
2025-09-25 18:33:20,184 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.99
2025-09-25 18:33:20,184 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-25 18:33:20,185 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-09-25 18:33:20,185 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-25 18:33:20,186 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-25 18:33:20,186 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-09-25 18:33:20,186 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-25 18:33:20,187 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-25 18:33:20,187 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-25 18:33:20,187 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-25 18:33:20,190 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 18:33:20,224 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 18:33:26,263 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 18:33:26,302 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 18:33:33,814 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 18:33:33,848 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 18:33:39,550 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 18:33:39,579 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 18:33:44,779 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 18:33:44,806 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 18:33:50,065 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2023-12-31 00:00:00 (729 days).
2025-09-25 18:36:03,320 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-25_18-36-03.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │     76 │         0.07 │          50.653 │         5.07 │ 2 days, 0:51:00 │   25     0    51  32.9 │
│ ETH/USDT │     75 │        -0.13 │         -37.198 │        -3.72 │ 2 days, 4:00:00 │   29     0    46  38.7 │
│ XRP/USDT │     60 │         0.26 │         -49.749 │        -4.97 │ 1 day, 18:53:00 │   19     0    41  31.7 │
│ LTC/USDT │     74 │        -0.08 │         -57.329 │        -5.73 │ 1 day, 20:52:00 │   23     0    51  31.1 │
│ BNB/USDT │     64 │        -0.15 │        -140.516 │       -14.05 │ 1 day, 17:58:00 │   16     0    48  25.0 │
│    TOTAL │    349 │        -0.01 │        -234.139 │       -23.41 │ 1 day, 22:24:00 │  112     0   237  32.1 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                       ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│      engulfing_rebond │      51 │          0.0 │          16.192 │         1.62 │ 1 day, 19:37:00 │   16     0    35  31.4 │
│         hammer_rebond │      48 │        -0.18 │         -42.988 │         -4.3 │ 1 day, 17:47:00 │   15     0    33  31.3 │
│ strong_bullish_rebond │     250 │         0.02 │        -207.342 │       -20.73 │ 1 day, 23:50:00 │   81     0   169  32.4 │
│                 TOTAL │     349 │        -0.01 │        -234.139 │       -23.41 │ 1 day, 22:24:00 │  112     0   237  32.1 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                         EXIT REASON STATS                                                         
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                 Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│              take_profit_2R │    38 │        10.57 │        1090.477 │       109.05 │ 2 days, 23:51:00 │   38     0     0   100 │
│                   stop_loss │    27 │        -4.69 │        -377.866 │       -37.79 │         14:38:00 │    0     0    27     0 │
│ ichimoku_cloud_crossed_exit │   284 │        -0.98 │        -946.749 │       -94.67 │  1 day, 22:00:00 │   74     0   210  26.1 │
│                       TOTAL │   349 │        -0.01 │        -234.139 │       -23.41 │  1 day, 22:24:00 │  112     0   237  32.1 │
└─────────────────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                                      MIXED TAG STATS                                                                       
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃                 Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │              take_profit_2R │     26 │        11.09 │         731.001 │         73.1 │  3 days, 5:01:00 │   26     0     0   100 │
│      engulfing_rebond │              take_profit_2R │      7 │         9.48 │         211.518 │        21.15 │ 2 days, 10:34:00 │    7     0     0   100 │
│         hammer_rebond │              take_profit_2R │      5 │         9.41 │         147.958 │         14.8 │ 2 days, 15:35:00 │    5     0     0   100 │
│         hammer_rebond │                   stop_loss │      4 │        -4.42 │         -55.261 │        -5.53 │         20:30:00 │    0     0     4     0 │
│      engulfing_rebond │                   stop_loss │      6 │        -5.47 │         -95.348 │        -9.53 │         15:18:00 │    0     0     6     0 │
│      engulfing_rebond │ ichimoku_cloud_crossed_exit │     38 │        -0.88 │         -99.978 │        -10.0 │  1 day, 21:21:00 │    9     0    29  23.7 │
│         hammer_rebond │ ichimoku_cloud_crossed_exit │     39 │        -0.97 │        -135.685 │       -13.57 │  1 day, 17:11:00 │   10     0    29  25.6 │
│ strong_bullish_rebond │                   stop_loss │     17 │        -4.48 │        -227.257 │       -22.73 │         13:02:00 │    0     0    17     0 │
│ strong_bullish_rebond │ ichimoku_cloud_crossed_exit │    207 │         -1.0 │        -711.086 │       -71.11 │  1 day, 23:02:00 │   55     0   152  26.6 │
│                 TOTAL │                             │    349 │        -0.01 │        -234.139 │       -23.41 │  1 day, 22:24:00 │  112     0   237  32.1 │
└───────────────────────┴─────────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2023-12-31 00:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 349 / 0.48                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 765.861 USDT                   │
│ Absolute profit               │ -234.139 USDT                  │
│ Total profit %                │ -23.41%                        │
│ CAGR %                        │ -12.50%                        │
│ Sortino                       │ -1.30                          │
│ Sharpe                        │ -0.48                          │
│ Calmar                        │ -1.74                          │
│ SQN                           │ -0.98                          │
│ Profit factor                 │ 0.87                           │
│ Expectancy (Ratio)            │ -0.67 (-0.09)                  │
│ Avg. daily profit             │ -0.321 USDT                    │
│ Avg. stake amount             │ 301.622 USDT                   │
│ Total trade volume            │ 210719.314 USDT                │
│                               │                                │
│ Best Pair                     │ BTC/USDT 5.07%                 │
│ Worst Pair                    │ BNB/USDT -14.05%               │
│ Best trade                    │ XRP/USDT 31.02%                │
│ Worst trade                   │ XRP/USDT -9.00%                │
│ Best day                      │ 67.523 USDT                    │
│ Worst day                     │ -44.292 USDT                   │
│ Days win/draw/lose            │ 71 / 468 / 149                 │
│ Min/Max/Avg. Duration Winners │ 0d 04:10 / 7d 19:35 / 3d 10:15 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 5d 23:00 / 1d 05:27 │
│ Max Consecutive Wins / Loss   │ 7 / 21                         │
│ Rejected Entry signals        │ 3648                           │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 675.411 USDT                   │
│ Max balance                   │ 1042.201 USDT                  │
│ Max % of account underwater   │ 35.19%                         │
│ Absolute Drawdown (Account)   │ 35.19%                         │
│ Absolute Drawdown             │ 366.79 USDT                    │
│ Drawdown high                 │ 42.201 USDT                    │
│ Drawdown low                  │ -324.589 USDT                  │
│ Drawdown Start                │ 2022-02-10 22:00:00            │
│ Drawdown End                  │ 2023-10-09 10:00:00            │
│ Market change                 │ -32.53%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2023-12-31 00:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                  
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃            Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    349 │        -0.01 │        -234.139 │       -23.41 │ 1 day, 22:24:00 │  112     0   237  32.1 │ 366.79 USDT  35.19% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴─────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-25T20:36:04.695773",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 1274,
  "total_daily_avg_trades": "349 / 0.48",
  "absolute_profit_usdt": -234.139,
  "total_profit_pct": -23.41,
  "cagr_pct": -12.5,
  "sortino": -1.3,
  "sharpe": -0.48,
  "calmar": -1.74,
  "sqn": -0.98,
  "max_consecutive_wins_loss": "7 / 21",
  "min_balance_usdt": 675.411,
  "max_balance_usdt": 1042.201,
  "market_change_pct": -32.53,
  "win_draw_loss_winpct": "0 0 0 0"
}
```
