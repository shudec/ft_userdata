# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 1209  
**Timestamp:** 2025-09-23 09:05:22

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 1209,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20180101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20180101-20251231
```

## Backtesting Output
```
2025-09-23 06:59:53,653 - freqtrade - INFO - freqtrade 2025.8
2025-09-23 06:59:54,402 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-23 06:59:57,893 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-23 06:59:57,899 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-23 06:59:57,899 - freqtrade.loggers - INFO - Logfile configured
2025-09-23 06:59:57,900 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-23 06:59:57,900 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-23 06:59:57,901 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-23 06:59:57,901 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-23 06:59:57,902 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20251231 ...
2025-09-23 06:59:58,258 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-23 06:59:58,261 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-23 06:59:58,261 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-23 06:59:58,262 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-23 06:59:58,262 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-23 06:59:58,263 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20251231
2025-09-23 06:59:58,267 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-23 06:59:58,280 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-23 06:59:58,281 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 06:59:58,283 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-23 06:59:58,284 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-23 06:59:58,285 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-23 06:59:58,305 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-23 07:00:00,862 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-23 07:00:01,017 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-23 07:00:01,021 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-23 07:00:01,030 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-23 07:00:01,031 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-23 07:00:01,031 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-23 07:00:01,032 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-23 07:00:01,033 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-23 07:00:01,034 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-23 07:00:01,035 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-23 07:00:01,036 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-23 07:00:01,037 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-23 07:00:01,038 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-23 07:00:01,040 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-23 07:00:01,043 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-23 07:00:01,044 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-23 07:00:01,045 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-23 07:00:01,046 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-23 07:00:01,047 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-23 07:00:01,047 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-23 07:00:01,048 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-23 07:00:01,048 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-23 07:00:01,049 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-23 07:00:01,049 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-23 07:00:01,050 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-23 07:00:01,050 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-23 07:00:01,050 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-23 07:00:01,051 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-23 07:00:01,052 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-23 07:00:01,052 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-23 07:00:01,053 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-23 07:00:01,054 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 07:00:01,107 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-23 07:00:01,137 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-23 07:00:01,267 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:00:01,413 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:00:01,509 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:00:01,601 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-23 07:00:01,602 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:00:01,686 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:00:01,733 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 07:00:02,153 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:00:03,729 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:00:04,705 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:00:05,499 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-23 07:00:05,500 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:00:06,230 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:00:09,011 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-23 07:00:09,019 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-23 07:00:09,020 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-23 07:00:09,020 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.498
2025-09-23 07:00:09,021 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-23 07:00:09,021 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-23 07:00:09,022 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2
2025-09-23 07:00:09,022 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 17
2025-09-23 07:00:09,023 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.557
2025-09-23 07:00:09,023 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.695
2025-09-23 07:00:09,024 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.007
2025-09-23 07:00:09,024 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-23 07:00:09,025 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-23 07:00:09,025 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss = True
2025-09-23 07:00:09,026 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 2
2025-09-23 07:00:09,027 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-23 07:00:09,028 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 9
2025-09-23 07:00:09,028 - freqtrade.strategy.hyper - INFO - Strategy Parameter: previous_low_stoploss = False
2025-09-23 07:00:09,029 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-23 07:00:09,029 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-23 07:00:09,030 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-23 07:00:09,030 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-23 07:00:09,030 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-23 07:00:09,035 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:00:09,055 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:00:39,606 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:00:39,637 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:01:14,035 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:01:14,059 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:01:37,367 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:01:37,428 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-23 07:01:37,430 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:02:02,560 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:02:02,581 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:02:36,284 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 07:05:20,727 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-23_07-05-20.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │    152 │        -0.22 │          32.994 │          3.3 │     12:25:00 │   70     0    82  46.1 │
│ BTC/USDT │    214 │        -0.12 │         -41.081 │        -4.11 │     13:21:00 │   97     0   117  45.3 │
│ BNB/USDT │    151 │        -0.13 │        -170.985 │        -17.1 │     13:43:00 │   66     0    85  43.7 │
│ LTC/USDT │    127 │         -0.2 │        -208.794 │       -20.88 │     11:20:00 │   57     0    70  44.9 │
│ XRP/USDT │    123 │        -0.23 │        -212.914 │       -21.29 │     10:20:00 │   52     0    71  42.3 │
│    TOTAL │    767 │        -0.17 │        -600.780 │       -60.08 │     12:25:00 │  342     0   425  44.6 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                           LEFT OPEN TRADES REPORT                                           
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         0.04 │           0.155 │         0.02 │      2:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         0.04 │           0.155 │         0.02 │      2:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                   ENTER TAG STATS                                                    
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│    hammer_rebond │     135 │        -0.19 │          -4.815 │        -0.48 │     16:49:00 │   63     0    72  46.7 │
│ engulfing_rebond │     632 │        -0.17 │        -595.965 │        -59.6 │     11:29:00 │  279     0   353  44.1 │
│            TOTAL │     767 │        -0.17 │        -600.780 │       -60.08 │     12:25:00 │  342     0   425  44.6 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │   341 │         2.29 │        4304.562 │       430.46 │     12:44:00 │  341     0     0   100 │
│     force_exit │     1 │         0.04 │           0.155 │         0.02 │      2:00:00 │    1     0     0   100 │
│      stop_loss │   425 │        -2.16 │       -4905.497 │      -490.55 │     12:12:00 │    0     0   425     0 │
│          TOTAL │   767 │        -0.17 │        -600.780 │       -60.08 │     12:25:00 │  342     0   425  44.6 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                           MIXED TAG STATS                                                            
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │ take_profit_1R │    278 │         2.17 │        3088.533 │       308.85 │     11:49:00 │  278     0     0   100 │
│    hammer_rebond │ take_profit_1R │     63 │         2.86 │        1216.029 │        121.6 │     16:44:00 │   63     0     0   100 │
│ engulfing_rebond │     force_exit │      1 │         0.04 │           0.155 │         0.02 │      2:00:00 │    1     0     0   100 │
│    hammer_rebond │      stop_loss │     72 │        -2.86 │       -1220.844 │      -122.08 │     16:53:00 │    0     0    72     0 │
│ engulfing_rebond │      stop_loss │    353 │        -2.01 │       -3684.653 │      -368.47 │     11:15:00 │    0     0   353     0 │
│            TOTAL │                │    767 │        -0.17 │        -600.780 │       -60.08 │     12:25:00 │  342     0   425  44.6 │
└──────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2018-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 767 / 0.27                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 399.22 USDT                    │
│ Absolute profit               │ -600.78 USDT                   │
│ Total profit %                │ -60.08%                        │
│ CAGR %                        │ -11.25%                        │
│ Sortino                       │ -0.57                          │
│ Sharpe                        │ -0.29                          │
│ Calmar                        │ -0.61                          │
│ SQN                           │ -1.54                          │
│ Profit factor                 │ 0.88                           │
│ Expectancy (Ratio)            │ -0.78 (-0.07)                  │
│ Avg. daily profit             │ -0.214 USDT                    │
│ Avg. stake amount             │ 573.247 USDT                   │
│ Total trade volume            │ 880520.127 USDT                │
│                               │                                │
│ Best Pair                     │ ETH/USDT 3.30%                 │
│ Worst Pair                    │ XRP/USDT -21.29%               │
│ Best trade                    │ BNB/USDT 8.33%                 │
│ Worst trade                   │ XRP/USDT -9.00%                │
│ Best day                      │ 61.491 USDT                    │
│ Worst day                     │ -56.411 USDT                   │
│ Days win/draw/lose            │ 283 / 2144 / 363               │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 4d 11:50 / 0d 12:42 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 3d 17:10 / 0d 12:12 │
│ Max Consecutive Wins / Loss   │ 8 / 16                         │
│ Rejected Entry signals        │ 12                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 390.842 USDT                   │
│ Max balance                   │ 1202.274 USDT                  │
│ Max % of account underwater   │ 67.49%                         │
│ Absolute drawdown             │ 811.432 USDT (67.49%)          │
│ Drawdown duration             │ 2188 days 18:45:00             │
│ Profit at drawdown start      │ 202.274 USDT                   │
│ Profit at drawdown end        │ -609.158 USDT                  │
│ Drawdown start                │ 2019-09-10 01:25:00            │
│ Drawdown end                  │ 2025-09-06 20:10:00            │
│ Market change                 │ 2372.94%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    767 │        -0.17 │        -600.780 │       -60.08 │     12:25:00 │  342     0   425  44.6 │ 811.432 USDT  67.49% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-23T09:05:22.797809",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 1209,
  "total_daily_avg_trades": "767 / 0.27",
  "absolute_profit_usdt": -600.78,
  "total_profit_pct": -60.08,
  "cagr_pct": -11.25,
  "sortino": -0.57,
  "sharpe": -0.29,
  "calmar": -0.61,
  "sqn": -1.54,
  "max_consecutive_wins_loss": "8 / 16",
  "min_balance_usdt": 390.842,
  "max_balance_usdt": 1202.274,
  "absolute_drawdown_pct": 67.49,
  "market_change_pct": 2372.94,
  "win_draw_loss_winpct": "342 0 425 44.6"
}
```
