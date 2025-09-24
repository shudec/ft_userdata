# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 5995  
**Timestamp:** 2025-09-24 09:30:50

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 5995,
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
2025-09-24 07:24:23,575 - freqtrade - INFO - freqtrade 2025.8
2025-09-24 07:24:24,336 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-24 07:24:27,434 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-24 07:24:27,440 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-24 07:24:27,441 - freqtrade.loggers - INFO - Logfile configured
2025-09-24 07:24:27,441 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-24 07:24:27,442 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-24 07:24:27,442 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-24 07:24:27,442 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-24 07:24:27,443 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20200101-20251231 ...
2025-09-24 07:24:27,960 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-24 07:24:27,962 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-24 07:24:27,963 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-24 07:24:27,963 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-24 07:24:27,963 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-24 07:24:27,964 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20200101-20251231
2025-09-24 07:24:27,966 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-24 07:24:27,977 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-24 07:24:27,978 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 07:24:27,981 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-24 07:24:27,982 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-24 07:24:27,982 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-24 07:24:28,004 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-24 07:24:38,294 - freqtrade.exchange.common - WARNING - _load_async_markets() returned exception: "Error in reload_markets due to RequestTimeout. Message: binance GET 
https://fapi.binance.com/fapi/v1/exchangeInfo". Retrying still for 3 times.
2025-09-24 07:24:41,608 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-24 07:24:41,727 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-24 07:24:41,729 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-24 07:24:41,735 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-24 07:24:41,735 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-24 07:24:41,735 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-24 07:24:41,736 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-24 07:24:41,736 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-24 07:24:41,737 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-24 07:24:41,737 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-24 07:24:41,737 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-24 07:24:41,738 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-24 07:24:41,738 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-24 07:24:41,738 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-24 07:24:41,739 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-24 07:24:41,739 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-24 07:24:41,740 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-24 07:24:41,740 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-24 07:24:41,740 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-24 07:24:41,741 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-24 07:24:41,741 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-24 07:24:41,741 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-24 07:24:41,742 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-24 07:24:41,742 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-24 07:24:41,743 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-24 07:24:41,743 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-24 07:24:41,744 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-24 07:24:41,744 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-24 07:24:41,745 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-24 07:24:41,746 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-24 07:24:41,746 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-24 07:24:41,747 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 07:24:41,776 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-24 07:24:41,803 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-24 07:24:41,864 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 07:24:41,931 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 07:24:41,996 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 07:24:42,057 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 07:24:42,136 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 07:24:42,170 - freqtrade.optimize.backtesting - INFO - Loading data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 07:24:42,466 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 07:24:43,072 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 07:24:43,751 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 07:24:44,262 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 07:24:44,807 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 07:24:46,641 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-24 07:24:46,648 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-24 07:24:46,648 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-24 07:24:46,649 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-24 07:24:46,650 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-24 07:24:46,650 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-24 07:24:46,651 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-24 07:24:46,652 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-24 07:24:46,653 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-24 07:24:46,653 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-24 07:24:46,654 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-24 07:24:46,654 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-24 07:24:46,655 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-09-24 07:24:46,655 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-09-24 07:24:46,655 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-24 07:24:46,656 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-24 07:24:46,656 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-24 07:24:46,657 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-24 07:24:46,658 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-24 07:24:46,658 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 8
2025-09-24 07:24:46,659 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-24 07:24:46,660 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-24 07:24:46,660 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-24 07:24:46,661 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-24 07:24:46,662 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-24 07:24:46,663 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-24 07:24:46,667 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:24:46,688 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 07:24:46,708 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:24:46,736 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 07:25:04,522 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:25:04,539 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 07:25:04,560 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:25:04,592 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 07:25:21,566 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:25:21,582 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 07:25:21,598 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:25:21,622 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-15 00:00:00
2025-09-24 07:25:41,696 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:25:41,718 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 07:25:41,745 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:25:41,779 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 07:26:01,338 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:26:01,372 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 07:26:01,399 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:26:01,446 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 07:26:23,140 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 07:30:48,976 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-24_07-30-48.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │    304 │         0.02 │          36.850 │         3.69 │     18:11:00 │  130     0   174  42.8 │
│ BNB/USDT │    265 │        -0.07 │         -66.460 │        -6.65 │     15:18:00 │  120     0   145  45.3 │
│ ETH/USDT │    269 │        -0.08 │         -91.231 │        -9.12 │     15:25:00 │  118     0   151  43.9 │
│ XRP/USDT │    181 │         -0.2 │         -92.765 │        -9.28 │     15:12:00 │   79     0   102  43.6 │
│ LTC/USDT │    181 │        -0.23 │        -119.206 │       -11.92 │     18:41:00 │   77     0   104  42.5 │
│    TOTAL │   1200 │        -0.09 │        -332.812 │       -33.28 │     16:33:00 │  524     0   676  43.7 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                            LEFT OPEN TRADES REPORT                                            
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         0.07 │           0.238 │         0.02 │ 1 day, 1:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         0.07 │           0.238 │         0.02 │ 1 day, 1:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                       ENTER TAG STATS                                                       
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│         hammer_rebond │     146 │         0.19 │         113.002 │         11.3 │ 1 day, 4:26:00 │   71     0    75  48.6 │
│      engulfing_rebond │     131 │         0.03 │          38.346 │         3.83 │       13:59:00 │   66     0    65  50.4 │
│ strong_bullish_rebond │     923 │        -0.16 │        -484.160 │       -48.42 │       15:02:00 │  387     0   536  41.9 │
│                 TOTAL │    1200 │        -0.09 │        -332.812 │       -33.28 │       16:33:00 │  524     0   676  43.7 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │    88 │         5.67 │        1483.661 │       148.37 │ 1 day, 2:52:00 │   88     0     0   100 │
│     force_exit │     1 │         0.07 │           0.238 │         0.02 │ 1 day, 1:00:00 │    1     0     0   100 │
│      stop_loss │    37 │        -5.26 │        -639.775 │       -63.98 │       13:20:00 │    0     0    37     0 │
│    exit_signal │  1074 │        -0.39 │       -1176.935 │      -117.69 │       15:49:00 │  435     0   639  40.5 │
│          TOTAL │  1200 │        -0.09 │        -332.812 │       -33.28 │       16:33:00 │  524     0   676  43.7 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                               MIXED TAG STATS                                                               
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_1R │     60 │         5.22 │         992.525 │        99.25 │ 1 day, 0:56:00 │   60     0     0   100 │
│         hammer_rebond │ take_profit_1R │     19 │         6.75 │         339.780 │        33.98 │ 1 day, 9:13:00 │   19     0     0   100 │
│      engulfing_rebond │ take_profit_1R │      9 │         6.38 │         151.356 │        15.14 │ 1 day, 2:21:00 │    9     0     0   100 │
│ strong_bullish_rebond │     force_exit │      1 │         0.07 │           0.238 │         0.02 │ 1 day, 1:00:00 │    1     0     0   100 │
│      engulfing_rebond │      stop_loss │      3 │        -5.76 │         -45.264 │        -4.53 │        2:17:00 │    0     0     3     0 │
│      engulfing_rebond │    exit_signal │    119 │         -0.3 │         -67.746 │        -6.77 │       13:20:00 │   57     0    62  47.9 │
│         hammer_rebond │    exit_signal │    119 │        -0.42 │         -72.827 │        -7.28 │ 1 day, 4:44:00 │   52     0    67  43.7 │
│         hammer_rebond │      stop_loss │      8 │        -6.35 │        -153.951 │        -15.4 │       12:31:00 │    0     0     8     0 │
│ strong_bullish_rebond │      stop_loss │     26 │        -4.86 │        -440.560 │       -44.06 │       14:52:00 │    0     0    26     0 │
│ strong_bullish_rebond │    exit_signal │    836 │         -0.4 │       -1036.363 │      -103.64 │       14:19:00 │  326     0   510  39.0 │
│                 TOTAL │                │   1200 │        -0.09 │        -332.812 │       -33.28 │       16:33:00 │  524     0   676  43.7 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2020-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 1200 / 0.58                    │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 667.188 USDT                   │
│ Absolute profit               │ -332.812 USDT                  │
│ Total profit %                │ -33.28%                        │
│ CAGR %                        │ -6.86%                         │
│ Sortino                       │ -0.60                          │
│ Sharpe                        │ -0.37                          │
│ Calmar                        │ -0.59                          │
│ SQN                           │ -1.16                          │
│ Profit factor                 │ 0.91                           │
│ Expectancy (Ratio)            │ -0.28 (-0.05)                  │
│ Avg. daily profit             │ -0.16 USDT                     │
│ Avg. stake amount             │ 294.002 USDT                   │
│ Total trade volume            │ 706683.335 USDT                │
│                               │                                │
│ Best Pair                     │ BTC/USDT 3.69%                 │
│ Worst Pair                    │ LTC/USDT -11.92%               │
│ Best trade                    │ XRP/USDT 13.21%                │
│ Worst trade                   │ XRP/USDT -12.68%               │
│ Best day                      │ 46.98 USDT                     │
│ Worst day                     │ -50.947 USDT                   │
│ Days win/draw/lose            │ 321 / 1305 / 417               │
│ Min/Max/Avg. Duration Winners │ 0d 00:50 / 5d 01:00 / 0d 16:25 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:30 / 3d 11:00 / 0d 16:39 │
│ Max Consecutive Wins / Loss   │ 9 / 17                         │
│ Rejected Entry signals        │ 546                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 587.602 USDT                   │
│ Max balance                   │ 1228.83 USDT                   │
│ Max % of account underwater   │ 52.18%                         │
│ Absolute drawdown             │ 641.228 USDT (52.18%)          │
│ Drawdown duration             │ 1526 days 22:30:00             │
│ Profit at drawdown start      │ 228.83 USDT                    │
│ Profit at drawdown end        │ -412.398 USDT                  │
│ Drawdown start                │ 2021-05-03 16:30:00            │
│ Drawdown end                  │ 2025-07-08 15:00:00            │
│ Market change                 │ 2537.81%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2020-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │   1200 │        -0.09 │        -332.812 │       -33.28 │     16:33:00 │  524     0   676  43.7 │ 641.228 USDT  52.18% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-24T09:30:50.784078",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 5995,
  "total_daily_avg_trades": "1200 / 0.58",
  "absolute_profit_usdt": -332.812,
  "total_profit_pct": -33.28,
  "cagr_pct": -6.86,
  "sortino": -0.6,
  "sharpe": -0.37,
  "calmar": -0.59,
  "sqn": -1.16,
  "max_consecutive_wins_loss": "9 / 17",
  "min_balance_usdt": 587.602,
  "max_balance_usdt": 1228.83,
  "absolute_drawdown_pct": 52.18,
  "market_change_pct": 2537.81,
  "win_draw_loss_winpct": "524 0 676 43.7"
}
```
