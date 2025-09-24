# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 8135  
**Timestamp:** 2025-09-24 10:36:02

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 8135,
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
2025-09-24 08:26:37,672 - freqtrade - INFO - freqtrade 2025.8
2025-09-24 08:26:38,087 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-24 08:26:39,854 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-24 08:26:39,860 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-24 08:26:39,861 - freqtrade.loggers - INFO - Logfile configured
2025-09-24 08:26:39,861 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-24 08:26:39,862 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-24 08:26:39,862 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-24 08:26:39,862 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-24 08:26:39,863 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20200101-20251231 ...
2025-09-24 08:26:40,335 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-24 08:26:40,338 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-24 08:26:40,339 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-24 08:26:40,339 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-24 08:26:40,340 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-24 08:26:40,341 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20200101-20251231
2025-09-24 08:26:40,342 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-24 08:26:40,353 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-24 08:26:40,354 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 08:26:40,357 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-24 08:26:40,358 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-24 08:26:40,359 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-24 08:26:40,381 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-24 08:26:42,584 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-24 08:26:42,692 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-24 08:26:42,695 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-24 08:26:42,703 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-24 08:26:42,704 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-24 08:26:42,704 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-24 08:26:42,705 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-24 08:26:42,705 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-24 08:26:42,706 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-24 08:26:42,706 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-24 08:26:42,707 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-24 08:26:42,707 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-24 08:26:42,708 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-24 08:26:42,708 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-24 08:26:42,709 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-24 08:26:42,709 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-24 08:26:42,709 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-24 08:26:42,710 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-24 08:26:42,710 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-24 08:26:42,711 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-24 08:26:42,712 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-24 08:26:42,713 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-24 08:26:42,714 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-24 08:26:42,715 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-24 08:26:42,716 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-24 08:26:42,717 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-24 08:26:42,717 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-24 08:26:42,718 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-24 08:26:42,718 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-24 08:26:42,719 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-24 08:26:42,719 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-24 08:26:42,720 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 08:26:42,741 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-24 08:26:42,769 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-24 08:26:42,828 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 08:26:42,912 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 08:26:42,991 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 08:26:43,060 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 08:26:43,131 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 08:26:43,161 - freqtrade.optimize.backtesting - INFO - Loading data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 08:26:43,481 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 08:26:44,301 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 08:26:45,278 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 08:26:45,929 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 08:26:46,830 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 08:26:49,243 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-24 08:26:49,248 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-24 08:26:49,248 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-24 08:26:49,249 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-24 08:26:49,249 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-24 08:26:49,250 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-24 08:26:49,250 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-24 08:26:49,251 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-24 08:26:49,251 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-24 08:26:49,252 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-24 08:26:49,252 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-24 08:26:49,253 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-24 08:26:49,253 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-09-24 08:26:49,254 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-09-24 08:26:49,254 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-24 08:26:49,254 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-24 08:26:49,255 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-24 08:26:49,255 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-24 08:26:49,256 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-24 08:26:49,256 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 8
2025-09-24 08:26:49,256 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-24 08:26:49,257 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-24 08:26:49,257 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-24 08:26:49,258 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-24 08:26:49,259 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-24 08:26:49,259 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-24 08:26:49,264 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:26:49,282 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 08:26:49,299 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:26:49,324 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 08:27:07,139 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:27:07,160 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 08:27:07,179 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:27:07,219 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 08:27:23,953 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:27:23,972 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 08:27:23,996 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:27:24,030 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-15 00:00:00
2025-09-24 08:27:40,706 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:27:40,731 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 08:27:40,753 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:27:40,784 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 08:27:58,656 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:27:58,673 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 08:27:58,690 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 08:27:58,727 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 08:28:17,160 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 08:36:01,215 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-24_08-36-01.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │    178 │         0.03 │          38.024 │          3.8 │     18:31:00 │  104     0    74  58.4 │
│ BNB/USDT │    260 │         0.06 │          -5.632 │        -0.56 │     21:35:00 │  156     0   104  60.0 │
│ ETH/USDT │    268 │        -0.07 │         -14.182 │        -1.42 │     20:16:00 │  166     0   102  61.9 │
│ BTC/USDT │    322 │        -0.04 │         -89.899 │        -8.99 │     19:38:00 │  214     0   108  66.5 │
│ LTC/USDT │    177 │        -0.36 │        -226.315 │       -22.63 │     22:51:00 │   94     0    83  53.1 │
│    TOTAL │   1205 │        -0.06 │        -298.003 │        -29.8 │     20:30:00 │  734     0   471  60.9 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                            LEFT OPEN TRADES REPORT                                            
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         0.07 │           0.250 │         0.03 │ 1 day, 1:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         0.07 │           0.250 │         0.03 │ 1 day, 1:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                       ENTER TAG STATS                                                       
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│         hammer_rebond │     136 │         0.27 │         159.510 │        15.95 │ 1 day, 6:37:00 │   67     0    69  49.3 │
│      engulfing_rebond │     127 │        -0.12 │         -44.741 │        -4.47 │       18:34:00 │   80     0    47  63.0 │
│ strong_bullish_rebond │     942 │         -0.1 │        -412.773 │       -41.28 │       19:18:00 │  587     0   355  62.3 │
│                 TOTAL │    1205 │        -0.06 │        -298.003 │        -29.8 │       20:30:00 │  734     0   471  60.9 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                       EXIT REASON STATS                                                       
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃               Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ sell_ichimoku_futur_cloud │   717 │          1.9 │        4070.914 │       407.09 │       12:42:00 │  717     0     0   100 │
│                force_exit │     1 │         0.07 │           0.250 │         0.03 │ 1 day, 1:00:00 │    1     0     0   100 │
│                 stop_loss │    41 │        -5.76 │        -781.738 │       -78.17 │       16:06:00 │    0     0    41     0 │
│               exit_signal │   446 │        -2.69 │       -3587.429 │      -358.74 │ 1 day, 9:27:00 │   16     0   430   3.6 │
│                     TOTAL │  1205 │        -0.06 │        -298.003 │        -29.8 │       20:30:00 │  734     0   471  60.9 │
└───────────────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                                     MIXED TAG STATS                                                                     
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃               Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ sell_ichimoku_futur_cloud │    575 │         1.75 │        2968.976 │        296.9 │        11:37:00 │  575     0     0   100 │
│         hammer_rebond │ sell_ichimoku_futur_cloud │     62 │          3.7 │         731.869 │        73.19 │  1 day, 0:40:00 │   62     0     0   100 │
│      engulfing_rebond │ sell_ichimoku_futur_cloud │     80 │         1.59 │         370.068 │        37.01 │        11:14:00 │   80     0     0   100 │
│ strong_bullish_rebond │                force_exit │      1 │         0.07 │           0.250 │         0.03 │  1 day, 1:00:00 │    1     0     0   100 │
│      engulfing_rebond │                 stop_loss │      5 │        -6.43 │         -89.845 │        -8.98 │        12:16:00 │    0     0     5     0 │
│         hammer_rebond │                 stop_loss │      8 │         -6.0 │        -165.990 │        -16.6 │        15:02:00 │    0     0     8     0 │
│      engulfing_rebond │               exit_signal │     42 │        -2.63 │        -324.963 │        -32.5 │  1 day, 9:17:00 │    0     0    42     0 │
│         hammer_rebond │               exit_signal │     66 │        -2.19 │        -406.369 │       -40.64 │ 1 day, 14:05:00 │    5     0    61   7.6 │
│ strong_bullish_rebond │                 stop_loss │     28 │        -5.58 │        -525.902 │       -52.59 │        17:05:00 │    0     0    28     0 │
│ strong_bullish_rebond │               exit_signal │    338 │         -2.8 │       -2856.097 │      -285.61 │  1 day, 8:34:00 │   11     0   327   3.3 │
│                 TOTAL │                           │   1205 │        -0.06 │        -298.003 │        -29.8 │        20:30:00 │  734     0   471  60.9 │
└───────────────────────┴───────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2020-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 1205 / 0.58                    │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 701.997 USDT                   │
│ Absolute profit               │ -298.003 USDT                  │
│ Total profit %                │ -29.80%                        │
│ CAGR %                        │ -6.02%                         │
│ Sortino                       │ -0.51                          │
│ Sharpe                        │ -0.30                          │
│ Calmar                        │ -0.53                          │
│ SQN                           │ -0.94                          │
│ Profit factor                 │ 0.93                           │
│ Expectancy (Ratio)            │ -0.25 (-0.03)                  │
│ Avg. daily profit             │ -0.143 USDT                    │
│ Avg. stake amount             │ 320.656 USDT                   │
│ Total trade volume            │ 774028.798 USDT                │
│                               │                                │
│ Best Pair                     │ XRP/USDT 3.80%                 │
│ Worst Pair                    │ LTC/USDT -22.63%               │
│ Best trade                    │ LTC/USDT 15.88%                │
│ Worst trade                   │ LTC/USDT -14.45%               │
│ Best day                      │ 54.93 USDT                     │
│ Worst day                     │ -54.43 USDT                    │
│ Days win/draw/lose            │ 383 / 1330 / 331               │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 4d 17:00 / 0d 14:20 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:30 / 4d 09:00 / 1d 06:07 │
│ Max Consecutive Wins / Loss   │ 15 / 7                         │
│ Rejected Entry signals        │ 823                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 639.903 USDT                   │
│ Max balance                   │ 1322.106 USDT                  │
│ Max % of account underwater   │ 51.60%                         │
│ Absolute drawdown             │ 682.203 USDT (51.60%)          │
│ Drawdown duration             │ 1337 days 14:15:00             │
│ Profit at drawdown start      │ 322.106 USDT                   │
│ Profit at drawdown end        │ -360.097 USDT                  │
│ Drawdown start                │ 2021-11-09 00:45:00            │
│ Drawdown end                  │ 2025-07-08 15:00:00            │
│ Market change                 │ 2537.81%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2020-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │   1205 │        -0.06 │        -298.003 │        -29.8 │     20:30:00 │  734     0   471  60.9 │ 682.203 USDT  51.60% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-24T10:36:02.856808",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 8135,
  "total_daily_avg_trades": "1205 / 0.58",
  "absolute_profit_usdt": -298.003,
  "total_profit_pct": -29.8,
  "cagr_pct": -6.02,
  "sortino": -0.51,
  "sharpe": -0.3,
  "calmar": -0.53,
  "sqn": -0.94,
  "max_consecutive_wins_loss": "15 / 7",
  "min_balance_usdt": 639.903,
  "max_balance_usdt": 1322.106,
  "absolute_drawdown_pct": 51.6,
  "market_change_pct": 2537.81,
  "win_draw_loss_winpct": "734 0 471 60.9"
}
```
