# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 539  
**Timestamp:** 2025-09-30 18:46:38

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 539,
  "epochs": 100,
  "hyperopt_timerange": "20220101-20231231",
  "backtest_timerange": "20220101-20241231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20241231 --export trades
```

## Backtesting Output
```
2025-09-30 16:43:51,427 - freqtrade - INFO - freqtrade 2025.8
2025-09-30 16:43:51,891 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-30 16:43:53,693 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-30 16:43:53,702 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-30 16:43:53,703 - freqtrade.loggers - INFO - Logfile configured
2025-09-30 16:43:53,703 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-30 16:43:53,704 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-30 16:43:53,705 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-30 16:43:53,706 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-30 16:43:53,707 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20241231 ...
2025-09-30 16:43:54,479 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-30 16:43:54,481 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-30 16:43:54,482 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-30 16:43:54,482 - freqtrade.configuration.configuration - INFO - Parameter --export detected: trades ...
2025-09-30 16:43:54,483 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-30 16:43:54,483 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-30 16:43:54,484 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20241231
2025-09-30 16:43:54,486 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-30 16:43:54,499 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-30 16:43:54,501 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-30 16:43:54,505 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-30 16:43:54,506 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-30 16:43:54,507 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-30 16:43:54,542 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-30 16:43:57,333 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-30 16:43:57,470 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-30 16:43:57,473 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-30 16:43:57,478 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-30 16:43:57,479 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-30 16:43:57,480 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-30 16:43:57,481 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-30 16:43:57,482 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-30 16:43:57,483 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-30 16:43:57,484 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-30 16:43:57,484 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-30 16:43:57,485 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-30 16:43:57,485 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-30 16:43:57,487 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-30 16:43:57,488 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-30 16:43:57,488 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-30 16:43:57,489 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-30 16:43:57,490 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-30 16:43:57,491 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-30 16:43:57,491 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-30 16:43:57,492 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-30 16:43:57,492 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-30 16:43:57,493 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-30 16:43:57,493 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-30 16:43:57,494 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-30 16:43:57,495 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-30 16:43:57,495 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-30 16:43:57,496 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-30 16:43:57,496 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-30 16:43:57,497 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-30 16:43:57,498 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-30 16:43:57,498 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-30 16:43:57,521 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-30 16:43:57,556 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-30 16:43:57,955 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2024-12-31 00:00:00 (1095 days).
2025-09-30 16:44:02,012 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-30 16:44:02,033 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-30 16:44:02,034 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.4
2025-09-30 16:44:02,034 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-30 16:44:02,035 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-30 16:44:02,035 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-30 16:44:02,036 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_strength_threshold = 0.02
2025-09-30 16:44:02,036 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 5
2025-09-30 16:44:02,037 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 2
2025-09-30 16:44:02,038 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 1
2025-09-30 16:44:02,038 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-09-30 16:44:02,039 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.02
2025-09-30 16:44:02,039 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.003
2025-09-30 16:44:02,040 - freqtrade.strategy.hyper - INFO - Strategy Parameter: ml_signal_strength_threshold = 0.119
2025-09-30 16:44:02,040 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-30 16:44:02,040 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-30 16:44:02,041 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_size_threshold = 2
2025-09-30 16:44:02,042 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_strength_threshold = 0.02
2025-09-30 16:44:02,042 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.409
2025-09-30 16:44:02,043 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.003
2025-09-30 16:44:02,043 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_engulfing_entry = False
2025-09-30 16:44:02,044 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_hammer_entry = True
2025-09-30 16:44:02,044 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_strong_bullish_entry = False
2025-09-30 16:44:02,045 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-30 16:44:02,045 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 0.5
2025-09-30 16:44:02,046 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-09-30 16:44:02,046 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-30 16:44:02,047 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 6
2025-09-30 16:44:02,047 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-30 16:44:02,048 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-30 16:44:02,048 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-09-30 16:44:02,049 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-30 16:44:02,049 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-30 16:44:02,049 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-09-30 16:44:02,050 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-30 16:44:02,050 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-30 16:44:02,050 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-30 16:44:02,051 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-30 16:44:02,054 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 16:44:02,116 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 16:44:13,615 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 16:44:13,688 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 16:44:25,626 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 16:44:25,680 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 16:44:41,502 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 16:44:41,570 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 16:44:58,144 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 16:44:58,211 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2022-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-30 16:45:11,799 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2024-12-31 00:00:00 (1095 days).
2025-09-30 16:46:37,100 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-30_16-46-37.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │     42 │         1.04 │         120.235 │        12.02 │          9:45:00 │   25     0    17  59.5 │
│ LTC/USDT │     43 │         1.28 │          69.352 │         6.94 │  1 day, 13:28:00 │   25     0    18  58.1 │
│ BTC/USDT │     39 │        -0.11 │          13.006 │          1.3 │   1 day, 8:31:00 │   18     0    21  46.2 │
│ XRP/USDT │     36 │        -1.19 │          -2.965 │         -0.3 │ 2 days, 16:06:00 │   18     0    18  50.0 │
│ BNB/USDT │     20 │         0.04 │          -5.269 │        -0.53 │  1 day, 17:26:00 │   10     0    10  50.0 │
│    TOTAL │    180 │         0.29 │         194.359 │        19.44 │  1 day, 11:42:00 │   96     0    84  53.3 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │      1 │       -11.98 │         -14.158 │        -1.42 │ 20 days, 1:00:00 │    0     0     1     0 │
│    TOTAL │      1 │       -11.98 │         -14.158 │        -1.42 │ 20 days, 1:00:00 │    0     0     1     0 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                   ENTER TAG STATS                                                    
┏━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ hammer_rebond │     180 │         0.29 │         194.359 │        19.44 │ 1 day, 11:42:00 │   96     0    84  53.3 │
│         TOTAL │     180 │         0.29 │         194.359 │        19.44 │ 1 day, 11:42:00 │   96     0    84  53.3 │
└───────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │    96 │         4.71 │        1343.698 │       134.37 │  1 day, 12:31:00 │   96     0     0   100 │
│     force_exit │     1 │       -11.98 │         -14.158 │        -1.42 │ 20 days, 1:00:00 │    0     0     1     0 │
│      stop_loss │    83 │        -4.67 │       -1135.182 │      -113.52 │   1 day, 5:23:00 │    0     0    83     0 │
│          TOTAL │   180 │         0.29 │         194.359 │        19.44 │  1 day, 11:42:00 │   96     0    84  53.3 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                            MIXED TAG STATS                                                            
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ hammer_rebond │ take_profit_1R │     96 │         4.71 │        1343.698 │       134.37 │  1 day, 12:31:00 │   96     0     0   100 │
│ hammer_rebond │     force_exit │      1 │       -11.98 │         -14.158 │        -1.42 │ 20 days, 1:00:00 │    0     0     1     0 │
│ hammer_rebond │      stop_loss │     83 │        -4.67 │       -1135.182 │      -113.52 │   1 day, 5:23:00 │    0     0    83     0 │
│         TOTAL │                │    180 │         0.29 │         194.359 │        19.44 │  1 day, 11:42:00 │   96     0    84  53.3 │
└───────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00             │
│ Backtesting to                │ 2024-12-31 00:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 180 / 0.16                      │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 1194.359 USDT                   │
│ Absolute profit               │ 194.359 USDT                    │
│ Total profit %                │ 19.44%                          │
│ CAGR %                        │ 6.10%                           │
│ Sortino                       │ 0.43                            │
│ Sharpe                        │ 0.21                            │
│ Calmar                        │ 1.99                            │
│ SQN                           │ 0.90                            │
│ Profit factor                 │ 1.17                            │
│ Expectancy (Ratio)            │ 1.08 (0.08)                     │
│ Avg. daily profit             │ 0.177 USDT                      │
│ Avg. stake amount             │ 361.926 USDT                    │
│ Total trade volume            │ 130748.815 USDT                 │
│                               │                                 │
│ Best Pair                     │ ETH/USDT 12.02%                 │
│ Worst Pair                    │ BNB/USDT -0.53%                 │
│ Best trade                    │ XRP/USDT 19.55%                 │
│ Worst trade                   │ XRP/USDT -43.10%                │
│ Best day                      │ 53.527 USDT                     │
│ Worst day                     │ -42.578 USDT                    │
│ Days win/draw/lose            │ 60 / 974 / 56                   │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 23d 21:05 / 1d 12:31 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 34d 23:40 / 1d 10:46 │
│ Max Consecutive Wins / Loss   │ 12 / 8                          │
│ Rejected Entry signals        │ 88                              │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 829.923 USDT                    │
│ Max balance                   │ 1303.586 USDT                   │
│ Max % of account underwater   │ 17.01%                          │
│ Absolute drawdown             │ 170.077 USDT (17.01%)           │
│ Drawdown duration             │ 158 days 17:30:00               │
│ Profit at drawdown start      │ -15.84 USDT                     │
│ Profit at drawdown end        │ -170.077 USDT                   │
│ Drawdown start                │ 2022-01-07 15:50:00             │
│ Drawdown end                  │ 2022-06-15 09:20:00             │
│ Market change                 │ 46.34%                          │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2024-12-31 00:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    180 │         0.29 │         194.359 │        19.44 │ 1 day, 11:42:00 │   96     0    84  53.3 │ 170.077 USDT  17.01% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-30T18:46:38.631453",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 539,
  "total_daily_avg_trades": "180 / 0.16",
  "absolute_profit_usdt": 194.359,
  "total_profit_pct": 19.44,
  "cagr_pct": 6.1,
  "sortino": 0.43,
  "sharpe": 0.21,
  "calmar": 1.99,
  "sqn": 0.9,
  "max_consecutive_wins_loss": "12 / 8",
  "min_balance_usdt": 829.923,
  "max_balance_usdt": 1303.586,
  "absolute_drawdown_pct": 17.01,
  "market_change_pct": 46.34
}
```
