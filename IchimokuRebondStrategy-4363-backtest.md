# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 4363  
**Timestamp:** 2025-09-18 10:09:38

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 4363,
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
2025-09-18 08:02:25,594 - freqtrade - INFO - freqtrade 2025.8
2025-09-18 08:02:26,424 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-18 08:02:30,135 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-18 08:02:30,152 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-18 08:02:30,153 - freqtrade.loggers - INFO - Logfile configured
2025-09-18 08:02:30,154 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-18 08:02:30,155 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-18 08:02:30,157 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-18 08:02:30,157 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-18 08:02:30,158 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-18 08:02:30,643 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-18 08:02:30,648 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-18 08:02:30,650 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-18 08:02:30,651 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-18 08:02:30,653 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-18 08:02:30,653 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-18 08:02:30,661 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-18 08:02:30,692 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-18 08:02:30,693 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 08:02:30,701 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-18 08:02:30,703 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-18 08:02:30,703 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-18 08:02:30,739 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-18 08:02:34,053 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-18 08:02:34,254 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-18 08:02:34,257 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-18 08:02:34,264 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-18 08:02:34,265 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-18 08:02:34,266 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-18 08:02:34,266 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-18 08:02:34,267 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-18 08:02:34,267 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-18 08:02:34,268 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-18 08:02:34,269 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-18 08:02:34,269 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-18 08:02:34,270 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-18 08:02:34,270 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-18 08:02:34,271 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-18 08:02:34,271 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-18 08:02:34,272 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-18 08:02:34,273 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-18 08:02:34,274 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-18 08:02:34,274 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-18 08:02:34,275 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-18 08:02:34,275 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-18 08:02:34,276 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-18 08:02:34,277 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-18 08:02:34,277 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-18 08:02:34,278 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-18 08:02:34,278 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-18 08:02:34,279 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-18 08:02:34,280 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-18 08:02:34,281 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-18 08:02:34,282 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-18 08:02:34,283 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 08:02:34,320 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-18 08:02:34,359 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-18 08:02:34,499 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-18 08:02:34,629 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-18 08:02:34,728 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-18 08:02:34,812 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-18 08:02:34,908 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-18 08:02:34,941 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-18 08:02:35,508 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-18 08:02:36,091 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-18 08:02:36,577 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-18 08:02:37,026 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-18 08:02:37,476 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-18 08:02:38,741 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-18 08:02:38,748 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-18 08:02:38,749 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-18 08:02:38,749 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-18 08:02:38,750 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.642
2025-09-18 08:02:38,750 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.265
2025-09-18 08:02:38,751 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.009
2025-09-18 08:02:38,752 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 6
2025-09-18 08:02:38,753 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 0
2025-09-18 08:02:38,754 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.994
2025-09-18 08:02:38,755 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2.5
2025-09-18 08:02:38,756 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-18 08:02:38,756 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-18 08:02:38,757 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-18 08:02:38,760 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 08:02:38,779 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-18 08:02:41,529 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 08:02:41,555 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-18 08:02:44,279 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 08:02:44,300 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-18 08:02:46,538 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 08:02:46,556 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-18 08:02:48,634 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 08:02:48,650 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-18 08:02:51,115 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-18 08:09:36,338 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-18_08-09-36.meta.json"
Result for strategy IchimokuRebondStrategy
                                                BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      4 │        31.12 │         103.304 │        10.33 │ 158 days, 2:44:00 │    3     0     1  75.0 │
│ LTC/USDT │      4 │        12.27 │          51.454 │         5.15 │  66 days, 3:46:00 │    2     0     2  50.0 │
│ BTC/USDT │      3 │        30.58 │          46.987 │          4.7 │ 246 days, 7:58:00 │    2     0     1  66.7 │
│ ETH/USDT │      2 │       -23.56 │         -32.925 │        -3.29 │ 29 days, 14:35:00 │    0     0     2     0 │
│ XRP/USDT │      3 │       -16.42 │         -53.818 │        -5.38 │  55 days, 9:57:00 │    0     0     3     0 │
│    TOTAL │     16 │        10.56 │         115.001 │         11.5 │ 116 days, 8:18:00 │    7     0     9  43.8 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                              LEFT OPEN TRADES REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃       Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │        66.95 │          31.145 │         3.11 │ 546 days, 19:00:00 │    1     0     0   100 │
│ BTC/USDT │      1 │        29.11 │          17.493 │         1.75 │ 301 days, 17:00:00 │    1     0     0   100 │
│    TOTAL │      2 │        48.03 │          48.638 │         4.86 │  424 days, 6:00:00 │    2     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────────┴────────────────────────┘
                                                  ENTER TAG STATS                                                   
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │      16 │        10.56 │         115.001 │         11.5 │ 116 days, 8:18:00 │    7     0     9  43.8 │
│     TOTAL │      16 │        10.56 │         115.001 │         11.5 │ 116 days, 8:18:00 │    7     0     9  43.8 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                    EXIT REASON STATS                                                    
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2.5R │     5 │         48.3 │         224.478 │        22.45 │ 113 days, 7:09:00 │    5     0     0   100 │
│       force_exit │     2 │        48.03 │          48.638 │         4.86 │ 424 days, 6:00:00 │    2     0     0   100 │
│        stop_loss │     9 │       -18.74 │        -158.114 │       -15.81 │ 49 days, 14:48:00 │    0     0     9     0 │
│            TOTAL │    16 │        10.56 │         115.001 │         11.5 │ 116 days, 8:18:00 │    7     0     9  43.8 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                           MIXED TAG STATS                                                            
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2.5R │      5 │         48.3 │         224.478 │        22.45 │ 113 days, 7:09:00 │    5     0     0   100 │
│           │       force_exit │      2 │        48.03 │          48.638 │         4.86 │ 424 days, 6:00:00 │    2     0     0   100 │
│           │        stop_loss │      9 │       -18.74 │        -158.114 │       -15.81 │ 49 days, 14:48:00 │    0     0     9     0 │
│     TOTAL │                  │     16 │        10.56 │         115.001 │         11.5 │ 116 days, 8:18:00 │    7     0     9  43.8 │
└───────────┴──────────────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                            SUMMARY METRICS                            
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                               ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00                 │
│ Backtesting to                │ 2025-09-10 08:00:00                 │
│ Trading Mode                  │ Spot                                │
│ Max open trades               │ 3                                   │
│                               │                                     │
│ Total/Daily Avg Trades        │ 16 / 0.01                           │
│ Starting balance              │ 1000 USDT                           │
│ Final balance                 │ 1115.001 USDT                       │
│ Absolute profit               │ 115.001 USDT                        │
│ Total profit %                │ 11.50%                              │
│ CAGR %                        │ 2.99%                               │
│ Sortino                       │ 1.03                                │
│ Sharpe                        │ 0.06                                │
│ Calmar                        │ 1.77                                │
│ SQN                           │ 0.96                                │
│ Profit factor                 │ 1.73                                │
│ Expectancy (Ratio)            │ 7.19 (0.41)                         │
│ Avg. daily profit             │ 0.085 USDT                          │
│ Avg. stake amount             │ 98.135 USDT                         │
│ Total trade volume            │ 3261.842 USDT                       │
│                               │                                     │
│ Best Pair                     │ BNB/USDT 10.33%                     │
│ Worst Pair                    │ XRP/USDT -5.38%                     │
│ Best trade                    │ BTC/USDT 75.62%                     │
│ Worst trade                   │ ETH/USDT -33.31%                    │
│ Best day                      │ 48.638 USDT                         │
│ Worst day                     │ -37.682 USDT                        │
│ Days win/draw/lose            │ 6 / 1208 / 8                        │
│ Min/Max/Avg. Duration Winners │ 19d 06:05 / 546d 19:00 / 202d 03:24 │
│ Min/Max/Avg. Duration Losers  │ 4d 18:20 / 155d 02:05 / 49d 14:48   │
│ Max Consecutive Wins / Loss   │ 4 / 5                               │
│ Rejected Entry signals        │ 0                                   │
│ Entry/Exit Timeouts           │ 0 / 0                               │
│                               │                                     │
│ Min balance                   │ 907.994 USDT                        │
│ Max balance                   │ 1115.001 USDT                       │
│ Max % of account underwater   │ 9.20%                               │
│ Absolute drawdown             │ 92.006 USDT (9.20%)                 │
│ Drawdown duration             │ 238 days 22:50:00                   │
│ Profit at drawdown start      │ -16.757 USDT                        │
│ Profit at drawdown end        │ -92.006 USDT                        │
│ Drawdown start                │ 2022-05-08 02:15:00                 │
│ Drawdown end                  │ 2023-01-02 01:05:00                 │
│ Market change                 │ 91.49%                              │
└───────────────────────────────┴─────────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     16 │        10.56 │         115.001 │         11.5 │ 116 days, 8:18:00 │    7     0     9  43.8 │ 92.006 USDT  9.20% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┴────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-18T10:09:37.919922",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 4363,
  "total_daily_avg_trades": "16 / 0.01",
  "absolute_profit_usdt": 115.001,
  "total_profit_pct": 11.5,
  "cagr_pct": 2.99,
  "sortino": 1.03,
  "sharpe": 0.06,
  "calmar": 1.77,
  "sqn": 0.96,
  "max_consecutive_wins_loss": "4 / 5",
  "min_balance_usdt": 907.994,
  "max_balance_usdt": 1115.001,
  "market_change_pct": 91.49
}
```
