# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 9442  
**Timestamp:** 2025-09-23 09:32:11

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 9442,
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
2025-09-23 07:26:56,992 - freqtrade - INFO - freqtrade 2025.8
2025-09-23 07:26:57,761 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-23 07:27:01,431 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-23 07:27:01,439 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-23 07:27:01,440 - freqtrade.loggers - INFO - Logfile configured
2025-09-23 07:27:01,441 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-23 07:27:01,441 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-23 07:27:01,442 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-23 07:27:01,444 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-23 07:27:01,445 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20251231 ...
2025-09-23 07:27:01,878 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-23 07:27:01,881 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-23 07:27:01,881 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-23 07:27:01,881 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-23 07:27:01,882 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-23 07:27:01,882 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20251231
2025-09-23 07:27:01,884 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-23 07:27:01,897 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-23 07:27:01,898 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 07:27:01,902 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-23 07:27:01,903 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-23 07:27:01,903 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-23 07:27:01,931 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-23 07:27:04,524 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-23 07:27:04,690 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-23 07:27:04,693 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-23 07:27:04,701 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-23 07:27:04,702 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-23 07:27:04,702 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-23 07:27:04,703 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-23 07:27:04,704 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-23 07:27:04,704 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-23 07:27:04,705 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-23 07:27:04,705 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-23 07:27:04,706 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-23 07:27:04,706 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-23 07:27:04,707 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-23 07:27:04,708 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-23 07:27:04,710 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-23 07:27:04,712 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-23 07:27:04,713 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-23 07:27:04,714 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-23 07:27:04,715 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-23 07:27:04,716 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-23 07:27:04,717 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-23 07:27:04,718 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-23 07:27:04,718 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-23 07:27:04,719 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-23 07:27:04,719 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-23 07:27:04,720 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-23 07:27:04,720 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-23 07:27:04,721 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-23 07:27:04,721 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-23 07:27:04,722 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-23 07:27:04,722 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 07:27:04,767 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-23 07:27:04,809 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-23 07:27:05,024 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:27:05,249 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:27:05,352 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:27:05,495 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-23 07:27:05,496 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:27:05,665 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 07:27:05,727 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 07:27:06,144 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:27:07,044 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:27:07,845 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:27:08,780 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-23 07:27:08,781 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:27:09,623 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 07:27:12,892 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-23 07:27:12,928 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-23 07:27:12,928 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-23 07:27:12,929 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.5
2025-09-23 07:27:12,930 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-23 07:27:12,930 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-23 07:27:12,931 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2
2025-09-23 07:27:12,931 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 17
2025-09-23 07:27:12,932 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.557
2025-09-23 07:27:12,932 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.695
2025-09-23 07:27:12,933 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.007
2025-09-23 07:27:12,934 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-23 07:27:12,935 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-23 07:27:12,937 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss = True
2025-09-23 07:27:12,937 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 2
2025-09-23 07:27:12,938 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-23 07:27:12,938 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 9
2025-09-23 07:27:12,939 - freqtrade.strategy.hyper - INFO - Strategy Parameter: previous_low_stoploss = False
2025-09-23 07:27:12,939 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-23 07:27:12,940 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-23 07:27:12,941 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-23 07:27:12,941 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-23 07:27:12,942 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-23 07:27:12,947 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:27:12,970 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:27:37,147 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:27:37,167 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:28:02,721 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:28:02,742 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:28:26,000 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:28:26,019 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-23 07:28:26,020 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:28:50,016 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 07:28:50,036 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 07:29:13,603 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 07:32:08,128 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-23_07-32-08.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │    194 │        -0.17 │         -77.852 │        -7.79 │     18:10:00 │   71     0   123  36.6 │
│ BNB/USDT │    140 │        -0.05 │         -83.990 │         -8.4 │     16:07:00 │   52     0    88  37.1 │
│ XRP/USDT │    106 │         0.18 │         -88.943 │        -8.89 │     12:16:00 │   42     0    64  39.6 │
│ ETH/USDT │    134 │         -0.4 │        -181.121 │       -18.11 │     15:39:00 │   45     0    89  33.6 │
│ LTC/USDT │    119 │        -0.47 │        -277.768 │       -27.78 │     15:40:00 │   40     0    79  33.6 │
│    TOTAL │    693 │        -0.19 │        -709.674 │       -70.97 │     15:56:00 │  250     0   443  36.1 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                           LEFT OPEN TRADES REPORT                                           
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         0.04 │           0.113 │         0.01 │      2:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         0.04 │           0.113 │         0.01 │      2:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                   ENTER TAG STATS                                                    
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│    hammer_rebond │      67 │        -0.22 │        -191.421 │       -19.14 │     20:00:00 │   24     0    43  35.8 │
│ engulfing_rebond │     626 │        -0.18 │        -518.253 │       -51.83 │     15:30:00 │  226     0   400  36.1 │
│            TOTAL │     693 │        -0.19 │        -709.674 │       -70.97 │     15:56:00 │  250     0   443  36.1 │
└──────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │   249 │         3.25 │        3410.398 │       341.04 │     16:32:00 │  249     0     0   100 │
│       force_exit │     1 │         0.04 │           0.113 │         0.01 │      2:00:00 │    1     0     0   100 │
│        stop_loss │   443 │        -2.12 │       -4120.184 │      -412.02 │     15:38:00 │    0     0   443     0 │
│            TOTAL │   693 │        -0.19 │        -709.674 │       -70.97 │     15:56:00 │  250     0   443  36.1 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                            MIXED TAG STATS                                                             
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ engulfing_rebond │ take_profit_1.5R │    225 │         3.13 │        2893.422 │       289.34 │     15:56:00 │  225     0     0   100 │
│    hammer_rebond │ take_profit_1.5R │     24 │         4.37 │         516.976 │         51.7 │     22:09:00 │   24     0     0   100 │
│ engulfing_rebond │       force_exit │      1 │         0.04 │           0.113 │         0.01 │      2:00:00 │    1     0     0   100 │
│    hammer_rebond │        stop_loss │     43 │        -2.77 │        -708.397 │       -70.84 │     18:47:00 │    0     0    43     0 │
│ engulfing_rebond │        stop_loss │    400 │        -2.05 │       -3411.787 │      -341.18 │     15:17:00 │    0     0   400     0 │
│            TOTAL │                  │    693 │        -0.19 │        -709.674 │       -70.97 │     15:56:00 │  250     0   443  36.1 │
└──────────────────┴──────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2018-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 693 / 0.25                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 290.326 USDT                   │
│ Absolute profit               │ -709.674 USDT                  │
│ Total profit %                │ -70.97%                        │
│ CAGR %                        │ -14.85%                        │
│ Sortino                       │ -0.74                          │
│ Sharpe                        │ -0.36                          │
│ Calmar                        │ -0.65                          │
│ SQN                           │ -2.00                          │
│ Profit factor                 │ 0.83                           │
│ Expectancy (Ratio)            │ -1.02 (-0.11)                  │
│ Avg. daily profit             │ -0.253 USDT                    │
│ Avg. stake amount             │ 449.419 USDT                   │
│ Total trade volume            │ 623429.983 USDT                │
│                               │                                │
│ Best Pair                     │ BTC/USDT -7.79%                │
│ Worst Pair                    │ LTC/USDT -27.78%               │
│ Best trade                    │ BNB/USDT 11.67%                │
│ Worst trade                   │ XRP/USDT -7.68%                │
│ Best day                      │ 54.808 USDT                    │
│ Worst day                     │ -48.075 USDT                   │
│ Days win/draw/lose            │ 217 / 2188 / 377               │
│ Min/Max/Avg. Duration Winners │ 0d 00:15 / 3d 16:00 / 0d 16:28 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 7d 13:30 / 0d 15:38 │
│ Max Consecutive Wins / Loss   │ 8 / 17                         │
│ Rejected Entry signals        │ 12                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 258.816 USDT                   │
│ Max balance                   │ 993.05 USDT                    │
│ Max % of account underwater   │ 74.12%                         │
│ Absolute drawdown             │ 741.184 USDT (74.12%)          │
│ Drawdown duration             │ 2414 days 11:25:00             │
│ Profit at drawdown start      │ -21.494 USDT                   │
│ Profit at drawdown end        │ -741.184 USDT                  │
│ Drawdown start                │ 2018-01-29 01:25:00            │
│ Drawdown end                  │ 2024-09-08 12:50:00            │
│ Market change                 │ 2372.94%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    693 │        -0.19 │        -709.674 │       -70.97 │     15:56:00 │  250     0   443  36.1 │ 741.184 USDT  74.12% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-23T09:32:11.480174",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 9442,
  "total_daily_avg_trades": "693 / 0.25",
  "absolute_profit_usdt": -709.674,
  "total_profit_pct": -70.97,
  "cagr_pct": -14.85,
  "sortino": -0.74,
  "sharpe": -0.36,
  "calmar": -0.65,
  "sqn": -2.0,
  "max_consecutive_wins_loss": "8 / 17",
  "min_balance_usdt": 258.816,
  "max_balance_usdt": 993.05,
  "absolute_drawdown_pct": 74.12,
  "market_change_pct": 2372.94,
  "win_draw_loss_winpct": "250 0 443 36.1"
}
```
