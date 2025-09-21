# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 9002  
**Timestamp:** 2025-09-21 21:12:30

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell buy roi",
  "random_state": 9002,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20201231",
  "backtest_timerange": "20180101-20241231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20180101-20241231
```

## Backtesting Output
```
2025-09-21 19:11:51,881 - freqtrade - INFO - freqtrade 2025.7
2025-09-21 19:11:52,224 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-21 19:11:52,225 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-21 19:11:53,672 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-21 19:11:53,674 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-21 19:11:53,675 - freqtrade.loggers - INFO - Logfile configured
2025-09-21 19:11:53,675 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-21 19:11:53,675 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-21 19:11:53,676 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-21 19:11:53,676 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-21 19:11:53,676 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20241231 ...
2025-09-21 19:11:53,684 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-21 19:11:53,685 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-21 19:11:53,685 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-21 19:11:53,686 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-21 19:11:53,686 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-21 19:11:53,687 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20241231
2025-09-21 19:11:53,688 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-21 19:11:53,712 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-21 19:11:53,714 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 19:11:53,720 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-21 19:11:53,721 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-21 19:11:53,722 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-21 19:11:53,763 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-21 19:11:55,982 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-21 19:11:56,020 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-21 19:11:56,021 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-21 19:11:56,022 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-21 19:11:56,022 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-21 19:11:56,023 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-21 19:11:56,023 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-21 19:11:56,024 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-21 19:11:56,024 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.427, '474': 0.179, '800': 0.064, '1657': 0}
2025-09-21 19:11:56,025 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-21 19:11:56,025 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-21 19:11:56,025 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-21 19:11:56,026 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-21 19:11:56,026 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-21 19:11:56,026 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-21 19:11:56,027 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-21 19:11:56,027 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-21 19:11:56,028 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-21 19:11:56,028 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-21 19:11:56,029 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-21 19:11:56,029 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-21 19:11:56,029 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-21 19:11:56,030 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-21 19:11:56,031 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-21 19:11:56,031 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-21 19:11:56,031 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-21 19:11:56,032 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-21 19:11:56,032 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-21 19:11:56,032 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-21 19:11:56,033 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-21 19:11:56,033 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-21 19:11:56,034 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 19:11:56,040 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-21 19:11:56,073 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-21 19:11:56,259 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-21 19:11:56,340 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2024-12-31 00:00:00 (2556 days).
2025-09-21 19:11:57,454 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-21 19:12:00,224 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-21 19:12:00,227 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-21 19:12:00,227 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-21 19:12:00,228 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.2
2025-09-21 19:12:00,228 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 0
2025-09-21 19:12:00,228 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.926
2025-09-21 19:12:00,229 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.911
2025-09-21 19:12:00,229 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.031
2025-09-21 19:12:00,229 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-21 19:12:00,230 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-21 19:12:00,230 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.998
2025-09-21 19:12:00,230 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 2
2025-09-21 19:12:00,231 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-09-21 19:12:00,231 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-21 19:12:00,231 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-21 19:12:00,232 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-21 19:12:00,232 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-21 19:12:00,235 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2018-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:12:04,944 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2018-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:12:09,616 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2018-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:12:14,305 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2018-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:12:14,313 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-21 19:12:18,778 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2018-01-01 00:00:00 to 2024-12-31 00:00:00
2025-09-21 19:12:23,582 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2024-12-31 00:00:00 (2556 days).
2025-09-21 19:12:29,089 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-21_19-12-29.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ LTC/USDT │      1 │         2.09 │          21.093 │         2.11 │      2:05:00 │    1     0     0   100 │
│ ETH/USDT │      1 │         2.95 │          19.854 │         1.99 │      1:35:00 │    1     0     0   100 │
│ BTC/USDT │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
│ XRP/USDT │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
│ BNB/USDT │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
│    TOTAL │      2 │         2.52 │          40.947 │         4.09 │      1:50:00 │    2     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                  ENTER TAG STATS                                                  
┏━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ hammer_rebond │       2 │         2.52 │          40.947 │         4.09 │      1:50:00 │    2     0     0   100 │
│         TOTAL │       2 │         2.52 │          40.947 │         4.09 │      1:50:00 │    2     0     0   100 │
└───────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │     2 │         2.52 │          40.947 │         4.09 │      1:50:00 │    2     0     0   100 │
│          TOTAL │     2 │         2.52 │          40.947 │         4.09 │      1:50:00 │    2     0     0   100 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                          MIXED TAG STATS                                                          
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ hammer_rebond │ take_profit_1R │      2 │         2.52 │          40.947 │         4.09 │      1:50:00 │    2     0     0   100 │
│         TOTAL │                │      2 │         2.52 │          40.947 │         4.09 │      1:50:00 │    2     0     0   100 │
└───────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2018-01-01 00:00:00            │
│ Backtesting to                │ 2024-12-31 00:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 2 / 0.0                        │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1040.947 USDT                  │
│ Absolute profit               │ 40.947 USDT                    │
│ Total profit %                │ 4.09%                          │
│ CAGR %                        │ 0.57%                          │
│ Sortino                       │ -100.00                        │
│ Sharpe                        │ 0.49                           │
│ Calmar                        │ -100.00                        │
│ SQN                           │ 33.05                          │
│ Profit factor                 │ 0.00                           │
│ Expectancy (Ratio)            │ 20.47 (100.00)                 │
│ Avg. daily profit             │ 0.016 USDT                     │
│ Avg. stake amount             │ 840.978 USDT                   │
│ Total trade volume            │ 3411.676 USDT                  │
│                               │                                │
│ Best Pair                     │ LTC/USDT 2.11%                 │
│ Worst Pair                    │ BTC/USDT 0.00%                 │
│ Best trade                    │ ETH/USDT 2.95%                 │
│ Worst trade                   │ LTC/USDT 2.09%                 │
│ Best day                      │ 21.093 USDT                    │
│ Worst day                     │ 0 USDT                         │
│ Days win/draw/lose            │ 2 / 218 / 0                    │
│ Min/Max/Avg. Duration Winners │ 0d 01:35 / 0d 02:05 / 0d 01:50 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 0d 00:00 / 0d 00:00 │
│ Max Consecutive Wins / Loss   │ 2 / 0                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 1019.854 USDT                  │
│ Max balance                   │ 1040.947 USDT                  │
│ Max % of account underwater   │ 0.00%                          │
│ Absolute Drawdown (Account)   │ 0.00%                          │
│ Absolute Drawdown             │ 0 USDT                         │
│ Drawdown high                 │ 19.854 USDT                    │
│ Drawdown low                  │ 19.854 USDT                    │
│ Drawdown Start                │ 2018-01-10 02:35:00            │
│ Drawdown End                  │ 2018-01-10 02:35:00            │
│ Market change                 │ 1866.17%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2024-12-31 00:00:00 | Max open trades : 3
                                                             STRATEGY SUMMARY                                                              
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃      Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │      2 │         2.52 │          40.947 │         4.09 │      1:50:00 │    2     0     0   100 │ 0 USDT  0.00% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴───────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-21T21:12:30.199795",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 9002,
  "total_daily_avg_trades": "2 / 0.0",
  "absolute_profit_usdt": 40.947,
  "total_profit_pct": 4.09,
  "cagr_pct": 0.57,
  "sortino": -100.0,
  "sharpe": 0.49,
  "calmar": -100.0,
  "sqn": 33.05,
  "max_consecutive_wins_loss": "2 / 0",
  "min_balance_usdt": 1019.854,
  "max_balance_usdt": 1040.947,
  "absolute_drawdown_pct": 0.0,
  "market_change_pct": 1866.17,
  "win_draw_loss_winpct": "2 0 0 100"
}
```
