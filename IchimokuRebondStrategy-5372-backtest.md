# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 5372  
**Timestamp:** 2025-09-19 16:53:48

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 5372,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231
```

## Backtesting Output
```
2025-09-19 14:42:35,714 - freqtrade - INFO - freqtrade 2025.8
2025-09-19 14:42:36,348 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-19 14:42:39,524 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-19 14:42:39,533 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-19 14:42:39,534 - freqtrade.loggers - INFO - Logfile configured
2025-09-19 14:42:39,535 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-19 14:42:39,536 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-19 14:42:39,537 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-19 14:42:39,538 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-19 14:42:39,539 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-19 14:42:40,001 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-19 14:42:40,003 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-19 14:42:40,004 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-19 14:42:40,004 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-19 14:42:40,005 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-19 14:42:40,005 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-19 14:42:40,007 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-19 14:42:40,021 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-19 14:42:40,022 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 14:42:40,025 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-19 14:42:40,026 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-19 14:42:40,027 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-19 14:42:40,056 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-19 14:42:44,300 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-19 14:42:44,435 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-19 14:42:44,438 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-19 14:42:44,443 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-19 14:42:44,443 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-19 14:42:44,444 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-19 14:42:44,444 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-19 14:42:44,445 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-19 14:42:44,446 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-19 14:42:44,446 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-19 14:42:44,447 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-19 14:42:44,447 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-19 14:42:44,448 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-19 14:42:44,448 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-19 14:42:44,448 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-19 14:42:44,449 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-19 14:42:44,449 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-19 14:42:44,450 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-19 14:42:44,450 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-19 14:42:44,451 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-19 14:42:44,452 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-19 14:42:44,453 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-19 14:42:44,454 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-19 14:42:44,454 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-19 14:42:44,455 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-19 14:42:44,456 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-19 14:42:44,456 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-19 14:42:44,457 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-19 14:42:44,457 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-19 14:42:44,457 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-19 14:42:44,458 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-19 14:42:44,458 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 14:42:44,489 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-19 14:42:44,518 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-19 14:42:44,583 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 14:42:44,653 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 14:42:44,714 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 14:42:44,780 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 14:42:44,858 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-19 14:42:44,891 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-19 14:42:45,225 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 14:42:45,824 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 14:42:46,300 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 14:42:46,794 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 14:42:47,248 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-19 14:42:49,204 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-19 14:42:49,223 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-19 14:42:49,224 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-19 14:42:49,225 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-19 14:42:49,227 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-19 14:42:49,228 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 1
2025-09-19 14:42:49,229 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.5
2025-09-19 14:42:49,230 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.5
2025-09-19 14:42:49,231 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.025
2025-09-19 14:42:49,232 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.05
2025-09-19 14:42:49,233 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.05
2025-09-19 14:42:49,235 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-19 14:42:49,236 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 2
2025-09-19 14:42:49,236 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-09-19 14:42:49,237 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-19 14:42:49,237 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-19 14:42:49,238 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-19 14:42:49,239 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-19 14:42:49,244 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 14:42:49,271 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 14:42:53,430 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 14:42:53,455 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 14:42:56,470 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 14:42:56,488 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 14:43:00,659 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 14:43:00,683 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 14:43:04,349 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-19 14:43:04,365 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-19 14:43:07,995 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-19 14:53:45,981 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-19_14-53-45.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │    632 │        -0.15 │        -138.333 │       -13.83 │      5:13:00 │  179     0   453  28.3 │
│ LTC/USDT │    647 │        -0.24 │        -140.471 │       -14.05 │      4:54:00 │  181     0   466  28.0 │
│ XRP/USDT │    561 │        -0.35 │        -210.842 │       -21.08 │      4:24:00 │  146     0   415  26.0 │
│ BTC/USDT │    687 │        -0.17 │        -249.461 │       -24.95 │      5:29:00 │  166     0   521  24.2 │
│ BNB/USDT │    566 │        -0.31 │        -255.328 │       -25.53 │      4:04:00 │  143     0   423  25.3 │
│    TOTAL │   3093 │        -0.24 │        -994.435 │       -99.44 │      4:51:00 │  815     0  2278  26.3 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
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
│     OTHER │    3093 │        -0.24 │        -994.435 │       -99.44 │      4:51:00 │  815     0  2278  26.3 │
│     TOTAL │    3093 │        -0.24 │        -994.435 │       -99.44 │      4:51:00 │  815     0  2278  26.3 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │   687 │         1.82 │        1764.849 │       176.48 │      4:43:00 │  687     0     0   100 │
│    exit_signal │  1020 │        -0.62 │        -739.718 │       -73.97 │      8:32:00 │  128     0   892  12.5 │
│      stop_loss │  1386 │        -0.98 │       -2019.566 │      -201.96 │      2:12:00 │    0     0  1386     0 │
│          TOTAL │  3093 │        -0.24 │        -994.435 │       -99.44 │      4:51:00 │  815     0  2278  26.3 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │    687 │         1.82 │        1764.849 │       176.48 │      4:43:00 │  687     0     0   100 │
│           │    exit_signal │   1020 │        -0.62 │        -739.718 │       -73.97 │      8:32:00 │  128     0   892  12.5 │
│           │      stop_loss │   1386 │        -0.98 │       -2019.566 │      -201.96 │      2:12:00 │    0     0  1386     0 │
│     TOTAL │                │   3093 │        -0.24 │        -994.435 │       -99.44 │      4:51:00 │  815     0  2278  26.3 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 3093 / 2.29                    │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 5.565 USDT                     │
│ Absolute profit               │ -994.435 USDT                  │
│ Total profit %                │ -99.44%                        │
│ CAGR %                        │ -75.48%                        │
│ Sortino                       │ -6.32                          │
│ Sharpe                        │ -4.03                          │
│ Calmar                        │ -1.42                          │
│ SQN                           │ -5.11                          │
│ Profit factor                 │ 0.66                           │
│ Expectancy (Ratio)            │ -0.32 (-0.25)                  │
│ Avg. daily profit             │ -0.738 USDT                    │
│ Avg. stake amount             │ 128.748 USDT                   │
│ Total trade volume            │ 797032.431 USDT                │
│                               │                                │
│ Best Pair                     │ ETH/USDT -13.83%               │
│ Worst Pair                    │ BNB/USDT -25.53%               │
│ Best trade                    │ BTC/USDT 11.98%                │
│ Worst trade                   │ XRP/USDT -7.80%                │
│ Best day                      │ 39.24 USDT                     │
│ Worst day                     │ -72.385 USDT                   │
│ Days win/draw/lose            │ 186 / 174 / 445                │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 2d 20:05 / 0d 07:43 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 1d 15:30 / 0d 03:49 │
│ Max Consecutive Wins / Loss   │ 10 / 25                        │
│ Rejected Entry signals        │ 20583                          │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 5.565 USDT                     │
│ Max balance                   │ 981.396 USDT                   │
│ Max % of account underwater   │ 99.44%                         │
│ Absolute drawdown             │ 994.435 USDT (99.44%)          │
│ Drawdown duration             │ 803 days 18:45:00              │
│ Profit at drawdown start      │ -18.604 USDT                   │
│ Profit at drawdown end        │ -994.435 USDT                  │
│ Drawdown start                │ 2022-01-04 19:00:00            │
│ Drawdown end                  │ 2024-03-18 13:45:00            │
│ Market change                 │ 91.49%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │   3093 │        -0.24 │        -994.435 │       -99.44 │      4:51:00 │  815     0  2278  26.3 │ 994.435 USDT  99.44% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-19T16:53:48.896596",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 5372,
  "total_daily_avg_trades": "3093 / 2.29",
  "absolute_profit_usdt": -994.435,
  "total_profit_pct": -99.44,
  "cagr_pct": -75.48,
  "sortino": -6.32,
  "sharpe": -4.03,
  "calmar": -1.42,
  "sqn": -5.11,
  "max_consecutive_wins_loss": "10 / 25",
  "min_balance_usdt": 5.565,
  "max_balance_usdt": 981.396,
  "market_change_pct": 91.49,
  "win_draw_loss_winpct": "815 0 2278 26.3"
}
```
