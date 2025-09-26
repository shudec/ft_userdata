# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 262  
**Timestamp:** 2025-09-25 19:10:26

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 262,
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
2025-09-25 17:08:03,476 - freqtrade - INFO - freqtrade 2025.8
2025-09-25 17:08:04,087 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-25 17:08:06,928 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-25 17:08:06,934 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-25 17:08:06,934 - freqtrade.loggers - INFO - Logfile configured
2025-09-25 17:08:06,935 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-25 17:08:06,935 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-25 17:08:06,935 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-25 17:08:06,936 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-25 17:08:06,936 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20231231 ...
2025-09-25 17:08:07,456 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-25 17:08:07,458 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-25 17:08:07,459 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-25 17:08:07,459 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-25 17:08:07,459 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-25 17:08:07,460 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20231231
2025-09-25 17:08:07,461 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-25 17:08:07,472 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-25 17:08:07,472 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 17:08:07,475 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-25 17:08:07,475 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-25 17:08:07,475 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-25 17:08:07,495 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-25 17:08:09,810 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-25 17:08:09,918 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-25 17:08:09,920 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-25 17:08:09,925 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-25 17:08:09,925 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-25 17:08:09,926 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-25 17:08:09,926 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-25 17:08:09,926 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-25 17:08:09,927 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-25 17:08:09,927 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-25 17:08:09,928 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-25 17:08:09,928 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-25 17:08:09,928 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-25 17:08:09,929 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-25 17:08:09,929 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-25 17:08:09,929 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-25 17:08:09,930 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-25 17:08:09,930 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-25 17:08:09,930 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-25 17:08:09,930 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-25 17:08:09,931 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-25 17:08:09,931 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-25 17:08:09,931 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-25 17:08:09,932 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-25 17:08:09,932 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-25 17:08:09,932 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-25 17:08:09,933 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-25 17:08:09,933 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-25 17:08:09,933 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-25 17:08:09,934 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-25 17:08:09,934 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-25 17:08:09,935 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 17:08:09,960 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-25 17:08:09,984 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-25 17:08:10,260 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2023-12-31 00:00:00 (729 days).
2025-09-25 17:08:13,008 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-25 17:08:13,031 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-25 17:08:13,032 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-25 17:08:13,033 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-25 17:08:13,034 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-25 17:08:13,035 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-25 17:08:13,035 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 10
2025-09-25 17:08:13,036 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-25 17:08:13,037 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-25 17:08:13,037 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-25 17:08:13,038 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-25 17:08:13,038 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.007
2025-09-25 17:08:13,038 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-25 17:08:13,039 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-25 17:08:13,039 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-25 17:08:13,040 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.007
2025-09-25 17:08:13,040 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.25
2025-09-25 17:08:13,041 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 0.5
2025-09-25 17:08:13,041 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 6
2025-09-25 17:08:13,041 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.998
2025-09-25 17:08:13,042 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 2
2025-09-25 17:08:13,043 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.99
2025-09-25 17:08:13,044 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-25 17:08:13,045 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = False
2025-09-25 17:08:13,046 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-25 17:08:13,046 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-25 17:08:13,047 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-09-25 17:08:13,047 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-25 17:08:13,048 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-25 17:08:13,048 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-25 17:08:13,049 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-25 17:08:13,051 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 17:08:13,091 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 17:08:19,445 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 17:08:19,478 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 17:08:26,276 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 17:08:26,326 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 17:08:32,997 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 17:08:33,041 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 17:08:39,217 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 17:08:39,245 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2022-01-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 17:08:44,885 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2023-12-31 00:00:00 (729 days).
2025-09-25 17:10:25,288 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-25_17-10-25.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │     57 │         0.49 │         146.605 │        14.66 │  2 days, 7:06:00 │   17     0    40  29.8 │
│ ETH/USDT │     58 │         0.41 │         106.990 │         10.7 │ 2 days, 11:30:00 │   22     0    36  37.9 │
│ XRP/USDT │     45 │        -0.23 │         -14.251 │        -1.43 │  1 day, 20:52:00 │   11     0    34  24.4 │
│ BNB/USDT │     49 │        -0.01 │         -27.981 │         -2.8 │  2 days, 1:40:00 │   14     0    35  28.6 │
│ LTC/USDT │     58 │        -0.17 │        -129.223 │       -12.92 │  2 days, 1:45:00 │   17     0    41  29.3 │
│    TOTAL │    267 │         0.11 │          82.141 │         8.21 │  2 days, 4:10:00 │   81     0   186  30.3 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
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
│ strong_bullish_rebond │     207 │         0.33 │         204.712 │        20.47 │ 2 days, 8:09:00 │   65     0   142  31.4 │
│      engulfing_rebond │      23 │        -0.55 │         -30.206 │        -3.02 │ 1 day, 19:55:00 │    7     0    16  30.4 │
│         hammer_rebond │      37 │        -0.67 │         -92.366 │        -9.24 │ 1 day, 11:04:00 │    9     0    28  24.3 │
│                 TOTAL │     267 │         0.11 │          82.141 │         8.21 │ 2 days, 4:10:00 │   81     0   186  30.3 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                         EXIT REASON STATS                                                         
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                 Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ichimoku_cloud_crossed_exit │   190 │         1.36 │        1005.514 │       100.55 │ 2 days, 18:19:00 │   81     0   109  42.6 │
│                   stop_loss │    77 │        -2.95 │        -923.373 │       -92.34 │         17:16:00 │    0     0    77     0 │
│                       TOTAL │   267 │         0.11 │          82.141 │         8.21 │  2 days, 4:10:00 │   81     0   186  30.3 │
└─────────────────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                                      MIXED TAG STATS                                                                       
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃                 Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ ichimoku_cloud_crossed_exit │    155 │         1.47 │         848.553 │        84.86 │ 2 days, 20:46:00 │   65     0    90  41.9 │
│         hammer_rebond │ ichimoku_cloud_crossed_exit │     18 │         1.13 │         115.722 │        11.57 │  2 days, 8:37:00 │    9     0     9  50.0 │
│      engulfing_rebond │ ichimoku_cloud_crossed_exit │     17 │         0.53 │          41.239 │         4.12 │  2 days, 6:11:00 │    7     0    10  41.2 │
│      engulfing_rebond │                   stop_loss │      6 │        -3.61 │         -71.445 │        -7.14 │         14:50:00 │    0     0     6     0 │
│         hammer_rebond │                   stop_loss │     19 │        -2.38 │        -208.088 │       -20.81 │         14:39:00 │    0     0    19     0 │
│ strong_bullish_rebond │                   stop_loss │     52 │        -3.08 │        -643.840 │       -64.38 │         18:30:00 │    0     0    52     0 │
│                 TOTAL │                             │    267 │         0.11 │          82.141 │         8.21 │  2 days, 4:10:00 │   81     0   186  30.3 │
└───────────────────────┴─────────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00             │
│ Backtesting to                │ 2023-12-31 00:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 267 / 0.37                      │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 1082.141 USDT                   │
│ Absolute profit               │ 82.141 USDT                     │
│ Total profit %                │ 8.21%                           │
│ CAGR %                        │ 4.03%                           │
│ Sortino                       │ 0.39                            │
│ Sharpe                        │ 0.10                            │
│ Calmar                        │ 0.69                            │
│ SQN                           │ 0.24                            │
│ Profit factor                 │ 1.05                            │
│ Expectancy (Ratio)            │ 0.31 (0.03)                     │
│ Avg. daily profit             │ 0.113 USDT                      │
│ Avg. stake amount             │ 415.176 USDT                    │
│ Total trade volume            │ 222230.28 USDT                  │
│                               │                                 │
│ Best Pair                     │ BTC/USDT 14.66%                 │
│ Worst Pair                    │ LTC/USDT -12.92%                │
│ Best trade                    │ BTC/USDT 23.84%                 │
│ Worst trade                   │ LTC/USDT -7.04%                 │
│ Best day                      │ 230.45 USDT                     │
│ Worst day                     │ -45.637 USDT                    │
│ Days win/draw/lose            │ 59 / 506 / 123                  │
│ Min/Max/Avg. Duration Winners │ 1d 09:00 / 14d 12:00 / 4d 14:46 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:15 / 4d 15:00 / 1d 02:39  │
│ Max Consecutive Wins / Loss   │ 5 / 20                          │
│ Rejected Entry signals        │ 1524                            │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 850.913 USDT                    │
│ Max balance                   │ 1239.683 USDT                   │
│ Max % of account underwater   │ 31.36%                          │
│ Absolute drawdown             │ 388.77 USDT (31.36%)            │
│ Drawdown duration             │ 266 days 22:45:00               │
│ Profit at drawdown start      │ 239.683 USDT                    │
│ Profit at drawdown end        │ -149.087 USDT                   │
│ Drawdown start                │ 2023-01-23 15:00:00             │
│ Drawdown end                  │ 2023-10-17 13:45:00             │
│ Market change                 │ -32.53%                         │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2023-12-31 00:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                  
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃            Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    267 │         0.11 │          82.141 │         8.21 │ 2 days, 4:10:00 │   81     0   186  30.3 │ 388.77 USDT  31.36% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴─────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-25T19:10:26.461163",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 262,
  "total_daily_avg_trades": "267 / 0.37",
  "absolute_profit_usdt": 82.141,
  "total_profit_pct": 8.21,
  "cagr_pct": 4.03,
  "sortino": 0.39,
  "sharpe": 0.1,
  "calmar": 0.69,
  "sqn": 0.24,
  "max_consecutive_wins_loss": "5 / 20",
  "min_balance_usdt": 850.913,
  "max_balance_usdt": 1239.683,
  "absolute_drawdown_pct": 31.36,
  "market_change_pct": -32.53,
  "win_draw_loss_winpct": "0 0 0 0"
}
```
