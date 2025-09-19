# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 6447  
**Timestamp:** 2025-09-18 11:59:19

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 6447,
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
2025-09-18 09:58:41,292 - freqtrade - INFO - freqtrade 2025.8
2025-09-18 09:58:41,693 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-18 09:58:43,462 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-18 09:58:43,469 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-18 09:58:43,470 - freqtrade.loggers - INFO - Logfile configured
2025-09-18 09:58:43,471 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-18 09:58:43,472 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-18 09:58:43,472 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-18 09:58:43,473 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-18 09:58:43,473 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-18 09:58:43,777 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-18 09:58:43,779 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-18 09:58:43,780 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-18 09:58:43,781 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-18 09:58:43,782 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-18 09:58:43,783 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-18 09:58:43,784 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-18 09:58:43,794 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-18 09:58:43,795 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 09:58:43,797 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-18 09:58:43,798 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-18 09:58:43,798 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-18 09:58:43,820 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-18 09:58:46,062 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-18 09:58:46,139 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-18 09:58:46,141 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-18 09:58:46,144 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-18 09:58:46,145 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-18 09:58:46,145 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-18 09:58:46,145 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-18 09:58:46,146 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-18 09:58:46,146 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-18 09:58:46,146 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-18 09:58:46,147 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-18 09:58:46,147 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-18 09:58:46,147 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-18 09:58:46,148 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-18 09:58:46,148 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-18 09:58:46,148 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-18 09:58:46,148 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-18 09:58:46,149 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-18 09:58:46,149 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-18 09:58:46,149 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-18 09:58:46,150 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-18 09:58:46,150 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-18 09:58:46,150 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-18 09:58:46,151 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-18 09:58:46,152 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-18 09:58:46,152 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-18 09:58:46,153 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-18 09:58:46,153 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-18 09:58:46,154 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-18 09:58:46,154 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-18 09:58:46,154 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-18 09:58:46,155 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 09:58:46,170 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-18 09:58:46,192 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-18 09:58:46,237 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-18 09:58:46,292 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-18 09:58:46,343 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-18 09:58:46,393 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-18 09:58:46,444 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-18 09:58:46,465 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-18 09:58:46,693 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-18 09:58:47,068 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-18 09:58:47,395 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-18 09:58:47,724 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-18 09:58:48,073 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-18 09:58:49,390 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-18 09:58:49,394 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-18 09:58:49,395 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-18 09:58:49,396 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-18 09:58:49,396 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 4
2025-09-18 09:58:49,397 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.796
2025-09-18 09:58:49,397 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.971
2025-09-18 09:58:49,398 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.013
2025-09-18 09:58:49,398 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 10
2025-09-18 09:58:49,399 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-09-18 09:58:49,399 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.995
2025-09-18 09:58:49,400 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-18 09:58:49,400 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-18 09:58:49,400 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-18 09:58:49,401 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-18 09:58:49,403 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 09:58:49,421 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-18 09:58:52,831 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 09:58:52,848 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-18 09:58:55,624 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 09:58:55,642 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-18 09:58:58,498 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 09:58:58,515 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-18 09:59:01,875 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 09:59:01,892 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-18 09:59:05,962 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-18 09:59:18,033 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-18_09-59-18.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │      3 │         2.61 │          35.160 │         3.52 │ 2 days, 0:22:00 │    2     0     1  66.7 │
│ BNB/USDT │      8 │         0.46 │          32.650 │         3.27 │         6:35:00 │    4     0     4  50.0 │
│ XRP/USDT │     13 │        -0.09 │          27.070 │         2.71 │        16:59:00 │    6     0     7  46.2 │
│ LTC/USDT │     10 │        -1.43 │         -96.010 │         -9.6 │        10:38:00 │    2     0     8  20.0 │
│ ETH/USDT │      6 │        -2.05 │        -115.474 │       -11.55 │        10:10:00 │    0     0     6     0 │
│    TOTAL │     40 │        -0.41 │        -116.605 │       -11.66 │        14:39:00 │   14     0    26  35.0 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
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
│     OTHER │      40 │        -0.41 │        -116.605 │       -11.66 │     14:39:00 │   14     0    26  35.0 │
│     TOTAL │      40 │        -0.41 │        -116.605 │       -11.66 │     14:39:00 │   14     0    26  35.0 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │    14 │         3.01 │         353.626 │        35.36 │     21:54:00 │   14     0     0   100 │
│        stop_loss │    26 │        -2.25 │        -470.231 │       -47.02 │     10:44:00 │    0     0    26     0 │
│            TOTAL │    40 │        -0.41 │        -116.605 │       -11.66 │     14:39:00 │   14     0    26  35.0 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1.5R │     14 │         3.01 │         353.626 │        35.36 │     21:54:00 │   14     0     0   100 │
│           │        stop_loss │     26 │        -2.25 │        -470.231 │       -47.02 │     10:44:00 │    0     0    26     0 │
│     TOTAL │                  │     40 │        -0.41 │        -116.605 │       -11.66 │     14:39:00 │   14     0    26  35.0 │
└───────────┴──────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 40 / 0.03                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 883.395 USDT                   │
│ Absolute profit               │ -116.605 USDT                  │
│ Total profit %                │ -11.66%                        │
│ CAGR %                        │ -3.30%                         │
│ Sortino                       │ -0.48                          │
│ Sharpe                        │ -0.08                          │
│ Calmar                        │ -0.89                          │
│ SQN                           │ -0.87                          │
│ Profit factor                 │ 0.75                           │
│ Expectancy (Ratio)            │ -2.92 (-0.16)                  │
│ Avg. daily profit             │ -0.087 USDT                    │
│ Avg. stake amount             │ 863.164 USDT                   │
│ Total trade volume            │ 69074.547 USDT                 │
│                               │                                │
│ Best Pair                     │ BTC/USDT 3.52%                 │
│ Worst Pair                    │ ETH/USDT -11.55%               │
│ Best trade                    │ BTC/USDT 5.73%                 │
│ Worst trade                   │ XRP/USDT -4.51%                │
│ Best day                      │ 47.85 USDT                     │
│ Worst day                     │ -22.848 USDT                   │
│ Days win/draw/lose            │ 13 / 1123 / 25                 │
│ Min/Max/Avg. Duration Winners │ 0d 01:25 / 4d 02:45 / 0d 21:54 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:45 / 4d 04:55 / 0d 10:44 │
│ Max Consecutive Wins / Loss   │ 4 / 6                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 857.273 USDT                   │
│ Max balance                   │ 1053.347 USDT                  │
│ Max % of account underwater   │ 18.61%                         │
│ Absolute drawdown             │ 196.073 USDT (18.61%)          │
│ Drawdown duration             │ 482 days 04:00:00              │
│ Profit at drawdown start      │ 53.347 USDT                    │
│ Profit at drawdown end        │ -142.727 USDT                  │
│ Drawdown start                │ 2022-07-18 23:55:00            │
│ Drawdown end                  │ 2023-11-13 03:55:00            │
│ Market change                 │ 91.49%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     40 │        -0.41 │        -116.605 │       -11.66 │     14:39:00 │   14     0    26  35.0 │ 196.073 USDT  18.61% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-18T11:59:19.408272",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 6447,
  "total_daily_avg_trades": "40 / 0.03",
  "absolute_profit_usdt": -116.605,
  "total_profit_pct": -11.66,
  "cagr_pct": -3.3,
  "sortino": -0.48,
  "sharpe": -0.08,
  "calmar": -0.89,
  "sqn": -0.87,
  "max_consecutive_wins_loss": "4 / 6",
  "min_balance_usdt": 857.273,
  "max_balance_usdt": 1053.347,
  "market_change_pct": 91.49,
  "win_draw_loss_winpct": "14 0 26 35.0"
}
```
