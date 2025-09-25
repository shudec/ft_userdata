# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 6464  
**Timestamp:** 2025-09-25 14:03:57

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 6464,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20231231",
  "backtest_timerange": "20240101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20240101-20251231
```

## Backtesting Output
```
2025-09-25 12:01:40,735 - freqtrade - INFO - freqtrade 2025.8
2025-09-25 12:01:41,312 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-25 12:01:43,988 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-25 12:01:43,995 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-25 12:01:43,996 - freqtrade.loggers - INFO - Logfile configured
2025-09-25 12:01:43,997 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-25 12:01:43,998 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-25 12:01:43,998 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-25 12:01:43,999 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-25 12:01:43,999 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20240101-20251231 ...
2025-09-25 12:01:44,675 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-25 12:01:44,678 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-25 12:01:44,678 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-25 12:01:44,679 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-25 12:01:44,679 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-25 12:01:44,680 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20240101-20251231
2025-09-25 12:01:44,682 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-25 12:01:44,695 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-25 12:01:44,696 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 12:01:44,699 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-25 12:01:44,700 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-25 12:01:44,700 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-25 12:01:44,725 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-25 12:01:47,211 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-25 12:01:47,334 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-25 12:01:47,336 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-25 12:01:47,341 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-25 12:01:47,342 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-25 12:01:47,342 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-25 12:01:47,342 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-25 12:01:47,343 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-25 12:01:47,343 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-25 12:01:47,344 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-25 12:01:47,344 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-25 12:01:47,345 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-25 12:01:47,345 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-25 12:01:47,345 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-25 12:01:47,346 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-25 12:01:47,346 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-25 12:01:47,347 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-25 12:01:47,347 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-25 12:01:47,347 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-25 12:01:47,348 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-25 12:01:47,348 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-25 12:01:47,349 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-25 12:01:47,349 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-25 12:01:47,350 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-25 12:01:47,350 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-25 12:01:47,350 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-25 12:01:47,351 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-25 12:01:47,351 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-25 12:01:47,351 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-25 12:01:47,352 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-25 12:01:47,352 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-25 12:01:47,352 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 12:01:47,380 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-25 12:01:47,406 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-25 12:01:47,475 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-25 12:01:47,536 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-25 12:01:47,585 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-25 12:01:47,636 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-25 12:01:47,685 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-25 12:01:47,701 - freqtrade.optimize.backtesting - INFO - Loading data from 2024-01-01 00:00:00 up to 2025-09-10 08:00:00 (618 days).
2025-09-25 12:01:47,960 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-25 12:01:48,295 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-25 12:01:48,596 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-25 12:01:48,852 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-25 12:01:49,124 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-25 12:01:49,677 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-25 12:01:49,694 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-25 12:01:49,695 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-25 12:01:49,696 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-25 12:01:49,696 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-25 12:01:49,697 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-25 12:01:49,697 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-25 12:01:49,697 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 10
2025-09-25 12:01:49,698 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-25 12:01:49,698 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-25 12:01:49,699 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-25 12:01:49,699 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-25 12:01:49,700 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.007
2025-09-25 12:01:49,700 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-25 12:01:49,700 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-25 12:01:49,701 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-25 12:01:49,701 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.007
2025-09-25 12:01:49,701 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.25
2025-09-25 12:01:49,702 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 0.5
2025-09-25 12:01:49,702 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 6
2025-09-25 12:01:49,702 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.998
2025-09-25 12:01:49,703 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 2
2025-09-25 12:01:49,703 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.99
2025-09-25 12:01:49,704 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-25 12:01:49,704 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = False
2025-09-25 12:01:49,704 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-25 12:01:49,705 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-25 12:01:49,705 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-09-25 12:01:49,705 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-25 12:01:49,706 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-25 12:01:49,706 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-25 12:01:49,707 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-25 12:01:49,708 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 12:01:49,728 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-25 12:01:49,743 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 12:01:49,769 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-25 12:01:54,560 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 12:01:54,579 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-25 12:01:54,593 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 12:01:54,625 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-25 12:01:59,411 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 12:01:59,431 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-25 12:01:59,455 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 12:01:59,481 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-15 00:00:00
2025-09-25 12:02:04,401 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 12:02:04,417 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-25 12:02:04,430 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 12:02:04,456 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-25 12:02:09,619 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 12:02:09,634 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-25 12:02:09,648 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2024-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-25 12:02:09,675 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-25 12:02:14,778 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2024-01-01 00:00:00 up to 2025-09-10 08:00:00 (618 days).
2025-09-25 12:03:55,815 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-25_12-03-55.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │     41 │         3.52 │         686.617 │        68.66 │  2 days, 7:54:00 │    9     0    32  22.0 │
│ BTC/USDT │     58 │          0.7 │         238.236 │        23.82 │ 2 days, 17:55:00 │   21     0    37  36.2 │
│ LTC/USDT │     38 │         0.46 │         189.405 │        18.94 │  2 days, 2:45:00 │   13     0    25  34.2 │
│ BNB/USDT │     64 │         0.25 │          83.012 │          8.3 │  2 days, 7:07:00 │   19     0    45  29.7 │
│ ETH/USDT │     44 │        -0.19 │         -36.761 │        -3.68 │  1 day, 20:48:00 │   12     0    32  27.3 │
│    TOTAL │    245 │         0.86 │        1160.510 │       116.05 │  2 days, 7:17:00 │   74     0   171  30.2 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         3.08 │          32.725 │         3.27 │  4 days, 6:00:00 │    1     0     0   100 │
│ XRP/USDT │      1 │        -1.49 │         -15.774 │        -1.58 │   1 day, 0:00:00 │    0     0     1     0 │
│    TOTAL │      2 │          0.8 │          16.951 │          1.7 │ 2 days, 15:00:00 │    1     0     1  50.0 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                        ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │     204 │         0.51 │         893.631 │        89.36 │  2 days, 6:59:00 │   60     0   144  29.4 │
│      engulfing_rebond │      22 │         4.17 │         279.384 │        27.94 │ 2 days, 20:57:00 │    9     0    13  40.9 │
│         hammer_rebond │      19 │         0.69 │         -12.506 │        -1.25 │  1 day, 18:33:00 │    5     0    14  26.3 │
│                 TOTAL │     245 │         0.86 │        1160.510 │       116.05 │  2 days, 7:17:00 │   74     0   171  30.2 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                         EXIT REASON STATS                                                         
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                 Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ichimoku_cloud_crossed_exit │   171 │         2.59 │        2563.933 │       256.39 │ 2 days, 23:30:00 │   73     0    98  42.7 │
│                  force_exit │     2 │          0.8 │          16.951 │          1.7 │ 2 days, 15:00:00 │    1     0     1  50.0 │
│                   stop_loss │    72 │        -3.26 │       -1420.375 │      -142.04 │         16:32:00 │    0     0    72     0 │
│                       TOTAL │   245 │         0.86 │        1160.510 │       116.05 │  2 days, 7:17:00 │   74     0   171  30.2 │
└─────────────────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                                      MIXED TAG STATS                                                                       
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃                 Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ ichimoku_cloud_crossed_exit │    144 │         2.12 │        2046.498 │       204.65 │ 2 days, 21:54:00 │   59     0    85  41.0 │
│      engulfing_rebond │ ichimoku_cloud_crossed_exit │     18 │         5.78 │         366.841 │        36.68 │  3 days, 9:13:00 │    9     0     9  50.0 │
│         hammer_rebond │ ichimoku_cloud_crossed_exit │      9 │         3.82 │         150.594 │        15.06 │  3 days, 5:40:00 │    5     0     4  55.6 │
│ strong_bullish_rebond │                  force_exit │      2 │          0.8 │          16.951 │          1.7 │ 2 days, 15:00:00 │    1     0     1  50.0 │
│      engulfing_rebond │                   stop_loss │      4 │        -3.09 │         -87.457 │        -8.75 │         13:42:00 │    0     0     4     0 │
│         hammer_rebond │                   stop_loss │     10 │        -2.13 │        -163.100 │       -16.31 │         10:58:00 │    0     0    10     0 │
│ strong_bullish_rebond │                   stop_loss │     58 │        -3.47 │       -1169.819 │      -116.98 │         17:42:00 │    0     0    58     0 │
│                 TOTAL │                             │    245 │         0.86 │        1160.510 │       116.05 │  2 days, 7:17:00 │   74     0   171  30.2 │
└───────────────────────┴─────────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2024-01-01 00:00:00             │
│ Backtesting to                │ 2025-09-10 08:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 245 / 0.4                       │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 2160.51 USDT                    │
│ Absolute profit               │ 1160.51 USDT                    │
│ Total profit %                │ 116.05%                         │
│ CAGR %                        │ 57.61%                          │
│ Sortino                       │ 3.50                            │
│ Sharpe                        │ 0.70                            │
│ Calmar                        │ 14.81                           │
│ SQN                           │ 1.44                            │
│ Profit factor                 │ 1.46                            │
│ Expectancy (Ratio)            │ 4.74 (0.32)                     │
│ Avg. daily profit             │ 1.878 USDT                      │
│ Avg. stake amount             │ 658.509 USDT                    │
│ Total trade volume            │ 324478.16 USDT                  │
│                               │                                 │
│ Best Pair                     │ XRP/USDT 68.66%                 │
│ Worst Pair                    │ ETH/USDT -3.68%                 │
│ Best trade                    │ XRP/USDT 65.08%                 │
│ Worst trade                   │ XRP/USDT -13.33%                │
│ Best day                      │ 487.296 USDT                    │
│ Worst day                     │ -78.274 USDT                    │
│ Days win/draw/lose            │ 55 / 414 / 115                  │
│ Min/Max/Avg. Duration Winners │ 1d 16:00 / 15d 18:00 / 4d 18:38 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:05 / 3d 07:00 / 1d 05:35  │
│ Max Consecutive Wins / Loss   │ 5 / 15                          │
│ Rejected Entry signals        │ 1566                            │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 992.719 USDT                    │
│ Max balance                   │ 2416.451 USDT                   │
│ Max % of account underwater   │ 25.81%                          │
│ Absolute drawdown             │ 506.719 USDT (24.23%)           │
│ Drawdown duration             │ 169 days 15:00:00               │
│ Profit at drawdown start      │ 1091.465 USDT                   │
│ Profit at drawdown end        │ 584.746 USDT                    │
│ Drawdown start                │ 2025-01-20 00:00:00             │
│ Drawdown end                  │ 2025-07-08 15:00:00             │
│ Market change                 │ 174.13%                         │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2024-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    245 │         0.86 │        1160.510 │       116.05 │ 2 days, 7:17:00 │   74     0   171  30.2 │ 506.719 USDT  24.23% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-25T14:03:57.089737",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 6464,
  "total_daily_avg_trades": "245 / 0.4",
  "absolute_profit_usdt": 1160.51,
  "total_profit_pct": 116.05,
  "cagr_pct": 57.61,
  "sortino": 3.5,
  "sharpe": 0.7,
  "calmar": 14.81,
  "sqn": 1.44,
  "max_consecutive_wins_loss": "5 / 15",
  "min_balance_usdt": 992.719,
  "max_balance_usdt": 2416.451,
  "absolute_drawdown_pct": 24.23,
  "market_change_pct": 174.13
}
```
