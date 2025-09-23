# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 9523  
**Timestamp:** 2025-09-23 22:17:36

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 9523,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20200101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20200101-20251231
```

## Backtesting Output
```
2025-09-23 20:11:41,617 - freqtrade - INFO - freqtrade 2025.7
2025-09-23 20:11:41,951 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-23 20:11:41,951 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-23 20:11:43,471 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-23 20:11:43,474 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-23 20:11:43,474 - freqtrade.loggers - INFO - Logfile configured
2025-09-23 20:11:43,474 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-23 20:11:43,475 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-23 20:11:43,475 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-23 20:11:43,475 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-23 20:11:43,476 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20200101-20251231 ...
2025-09-23 20:11:43,484 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-23 20:11:43,485 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-23 20:11:43,485 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-23 20:11:43,486 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-23 20:11:43,486 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-23 20:11:43,486 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20200101-20251231
2025-09-23 20:11:43,488 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-23 20:11:43,506 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-23 20:11:43,507 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 20:11:43,511 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-23 20:11:43,512 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-23 20:11:43,512 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-23 20:11:43,546 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-23 20:11:45,875 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-23 20:11:45,913 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-23 20:11:45,914 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-23 20:11:45,915 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-23 20:11:45,915 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-23 20:11:45,916 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-23 20:11:45,916 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-23 20:11:45,917 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-23 20:11:45,917 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-23 20:11:45,917 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-23 20:11:45,918 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-23 20:11:45,918 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-23 20:11:45,919 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-23 20:11:45,919 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-23 20:11:45,919 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-23 20:11:45,920 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-23 20:11:45,920 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-23 20:11:45,920 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-23 20:11:45,921 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-23 20:11:45,921 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-23 20:11:45,922 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-23 20:11:45,922 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-23 20:11:45,922 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-23 20:11:45,923 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-23 20:11:45,923 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-23 20:11:45,924 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-23 20:11:45,924 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-23 20:11:45,924 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-23 20:11:45,925 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-23 20:11:45,925 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-23 20:11:45,926 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-23 20:11:45,926 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 20:11:45,931 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-23 20:11:45,962 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-23 20:11:45,997 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 20:11:46,054 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 20:11:46,106 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 20:11:46,156 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 20:11:46,206 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-23 20:11:46,245 - freqtrade.optimize.backtesting - INFO - Loading data from 2020-01-01 00:00:00 up to 2025-09-11 17:00:00 (2080 days).
2025-09-23 20:11:46,317 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 20:11:46,612 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 20:11:46,899 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 20:11:47,190 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 20:11:47,528 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-23 20:11:49,581 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-23 20:11:49,582 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-23 20:11:49,582 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-23 20:11:49,583 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-23 20:11:49,583 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-23 20:11:49,583 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-23 20:11:49,584 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-23 20:11:49,584 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-23 20:11:49,584 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-23 20:11:49,585 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-23 20:11:49,585 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-23 20:11:49,585 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-23 20:11:49,585 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-09-23 20:11:49,586 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-09-23 20:11:49,586 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-23 20:11:49,586 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-23 20:11:49,587 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-23 20:11:49,587 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-23 20:11:49,587 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-23 20:11:49,588 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 1
2025-09-23 20:11:49,588 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-23 20:11:49,588 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-23 20:11:49,589 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-23 20:11:49,589 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower
2025-09-23 20:11:49,589 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-23 20:11:49,590 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-23 20:11:49,592 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:11:49,601 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 20:11:49,622 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:11:49,639 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 20:11:59,305 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:11:59,313 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 20:11:59,332 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:11:59,349 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 20:12:09,089 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:12:09,096 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 20:12:09,115 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:12:09,132 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 20:12:18,784 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:12:18,791 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 20:12:18,810 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:12:18,827 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 20:12:28,374 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:12:28,383 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-23 20:12:28,403 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 20:12:28,421 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-11 12:00:00
2025-09-23 20:12:38,210 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2020-01-01 00:00:00 up to 2025-09-11 17:00:00 (2080 days).
2025-09-23 20:17:35,062 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-23_20-17-35.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │    166 │         1.22 │         559.000 │         55.9 │ 2 days, 3:01:00 │   74     0    92  44.6 │
│ BTC/USDT │    192 │          0.6 │         314.928 │        31.49 │ 2 days, 9:20:00 │   79     0   113  41.1 │
│ BNB/USDT │    168 │         0.66 │         261.346 │        26.13 │ 2 days, 0:10:00 │   58     0   110  34.5 │
│ XRP/USDT │    129 │         0.11 │          44.702 │         4.47 │ 1 day, 13:08:00 │   35     0    94  27.1 │
│ LTC/USDT │    125 │        -0.23 │         -56.122 │        -5.61 │ 1 day, 19:19:00 │   43     0    82  34.4 │
│    TOTAL │    780 │         0.53 │        1123.855 │       112.39 │ 2 days, 0:26:00 │  289     0   491  37.1 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         4.38 │          18.455 │         1.85 │ 5 days, 15:00:00 │    1     0     0   100 │
│ BTC/USDT │      1 │        -0.12 │          -0.517 │        -0.05 │         13:00:00 │    0     0     1     0 │
│ LTC/USDT │      1 │        -3.08 │         -12.948 │        -1.29 │         17:00:00 │    0     0     1     0 │
│    TOTAL │      3 │         0.39 │           4.990 │          0.5 │  2 days, 7:00:00 │    1     0     2  33.3 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                       ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │     620 │         0.46 │         718.381 │        71.84 │ 2 days, 0:10:00 │  228     0   392  36.8 │
│      engulfing_rebond │      79 │         0.81 │         245.723 │        24.57 │ 2 days, 2:44:00 │   28     0    51  35.4 │
│         hammer_rebond │      81 │         0.83 │         159.751 │        15.98 │ 2 days, 0:12:00 │   33     0    48  40.7 │
│                 TOTAL │     780 │         0.53 │        1123.855 │       112.39 │ 2 days, 0:26:00 │  289     0   491  37.1 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │   139 │        10.44 │        4591.427 │       459.14 │ 2 days, 5:47:00 │  139     0     0   100 │
│     force_exit │     3 │         0.39 │           4.990 │          0.5 │ 2 days, 7:00:00 │    1     0     2  33.3 │
│      stop_loss │    13 │       -10.18 │        -369.284 │       -36.93 │        18:09:00 │    0     0    13     0 │
│    exit_signal │   625 │        -1.45 │       -3103.278 │      -310.33 │ 1 day, 23:50:00 │  149     0   476  23.8 │
│          TOTAL │   780 │         0.53 │        1123.855 │       112.39 │ 2 days, 0:26:00 │  289     0   491  37.1 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                                MIXED TAG STATS                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_1R │    108 │        10.41 │        3523.030 │        352.3 │  2 days, 6:13:00 │  108     0     0   100 │
│      engulfing_rebond │ take_profit_1R │     16 │        10.41 │         584.136 │        58.41 │ 2 days, 14:03:00 │   16     0     0   100 │
│         hammer_rebond │ take_profit_1R │     15 │        10.65 │         484.260 │        48.43 │  1 day, 17:52:00 │   15     0     0   100 │
│ strong_bullish_rebond │     force_exit │      2 │         0.65 │           5.507 │         0.55 │  3 days, 4:00:00 │    1     0     1  50.0 │
│      engulfing_rebond │     force_exit │      1 │        -0.12 │          -0.517 │        -0.05 │         13:00:00 │    0     0     1     0 │
│      engulfing_rebond │      stop_loss │      1 │       -10.18 │         -45.911 │        -4.59 │         19:25:00 │    0     0     1     0 │
│         hammer_rebond │      stop_loss │      3 │       -10.18 │        -114.723 │       -11.47 │         15:53:00 │    0     0     3     0 │
│ strong_bullish_rebond │      stop_loss │      9 │       -10.18 │        -208.649 │       -20.86 │         18:46:00 │    0     0     9     0 │
│         hammer_rebond │    exit_signal │     63 │        -0.98 │        -209.786 │       -20.98 │  2 days, 3:15:00 │   18     0    45  28.6 │
│      engulfing_rebond │    exit_signal │     61 │        -1.51 │        -291.985 │        -29.2 │  2 days, 0:54:00 │   12     0    49  19.7 │
│ strong_bullish_rebond │    exit_signal │    501 │         -1.5 │       -2601.507 │      -260.15 │  1 day, 23:16:00 │  119     0   382  23.8 │
│                 TOTAL │                │    780 │         0.53 │        1123.855 │       112.39 │  2 days, 0:26:00 │  289     0   491  37.1 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2020-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-11 17:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 780 / 0.38                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 2123.855 USDT                  │
│ Absolute profit               │ 1123.855 USDT                  │
│ Total profit %                │ 112.39%                        │
│ CAGR %                        │ 14.13%                         │
│ Sortino                       │ 1.50                           │
│ Sharpe                        │ 0.59                           │
│ Calmar                        │ 6.52                           │
│ SQN                           │ 2.32                           │
│ Profit factor                 │ 1.25                           │
│ Expectancy (Ratio)            │ 1.44 (0.16)                    │
│ Avg. daily profit             │ 0.54 USDT                      │
│ Avg. stake amount             │ 337.744 USDT                   │
│ Total trade volume            │ 529061.501 USDT                │
│                               │                                │
│ Best Pair                     │ ETH/USDT 55.90%                │
│ Worst Pair                    │ LTC/USDT -5.61%                │
│ Best trade                    │ XRP/USDT 13.21%                │
│ Worst trade                   │ BNB/USDT -10.18%               │
│ Best day                      │ 119.423 USDT                   │
│ Worst day                     │ -56.777 USDT                   │
│ Days win/draw/lose            │ 201 / 1517 / 323               │
│ Min/Max/Avg. Duration Winners │ 0d 00:20 / 7d 19:35 / 2d 23:24 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 4d 07:00 / 1d 10:54 │
│ Max Consecutive Wins / Loss   │ 9 / 15                         │
│ Rejected Entry signals        │ 2139                           │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 900.019 USDT                   │
│ Max balance                   │ 2285.228 USDT                  │
│ Max % of account underwater   │ 16.69%                         │
│ Absolute Drawdown (Account)   │ 15.83%                         │
│ Absolute Drawdown             │ 361.81 USDT                    │
│ Drawdown high                 │ 1285.228 USDT                  │
│ Drawdown low                  │ 923.418 USDT                   │
│ Drawdown Start                │ 2024-12-01 19:50:00            │
│ Drawdown End                  │ 2025-05-04 03:00:00            │
│ Market change                 │ 2586.51%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2020-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                  
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃            Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    780 │         0.53 │        1123.855 │       112.39 │ 2 days, 0:26:00 │  289     0   491  37.1 │ 361.81 USDT  15.83% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴─────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-23T22:17:36.318904",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 9523,
  "total_daily_avg_trades": "780 / 0.38",
  "absolute_profit_usdt": 1123.855,
  "total_profit_pct": 112.39,
  "cagr_pct": 14.13,
  "sortino": 1.5,
  "sharpe": 0.59,
  "calmar": 6.52,
  "sqn": 2.32,
  "max_consecutive_wins_loss": "9 / 15",
  "min_balance_usdt": 900.019,
  "max_balance_usdt": 2285.228,
  "market_change_pct": 2586.51
}
```
