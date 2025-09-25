# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 6867  
**Timestamp:** 2025-09-25 08:54:41

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 6867,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20231231",
  "backtest_timerange": "20170801-20231231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20231231
```

## Backtesting Output
```
2025-09-25 06:44:35,455 - freqtrade - INFO - freqtrade 2025.8
2025-09-25 06:44:35,995 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-25 06:44:39,188 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-25 06:44:39,198 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-25 06:44:39,198 - freqtrade.loggers - INFO - Logfile configured
2025-09-25 06:44:39,199 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-25 06:44:39,200 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-25 06:44:39,201 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-25 06:44:39,202 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-25 06:44:39,202 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20231231 ...
2025-09-25 06:44:40,270 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-25 06:44:40,273 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-25 06:44:40,274 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-25 06:44:40,275 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-25 06:44:40,276 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-25 06:44:40,277 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20231231
2025-09-25 06:44:40,280 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-25 06:44:40,296 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-25 06:44:40,297 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 06:44:40,300 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-25 06:44:40,301 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-25 06:44:40,302 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-25 06:44:40,334 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-25 06:44:42,636 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-25 06:44:42,756 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-25 06:44:42,758 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-25 06:44:42,763 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-25 06:44:42,763 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-25 06:44:42,763 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-25 06:44:42,764 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-25 06:44:42,764 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-25 06:44:42,765 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-25 06:44:42,765 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-25 06:44:42,765 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.293
2025-09-25 06:44:42,766 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-25 06:44:42,767 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-25 06:44:42,767 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-25 06:44:42,767 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-25 06:44:42,768 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-25 06:44:42,769 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-25 06:44:42,769 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-25 06:44:42,770 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-25 06:44:42,770 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-25 06:44:42,771 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-25 06:44:42,771 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-25 06:44:42,771 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-25 06:44:42,772 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-25 06:44:42,772 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-25 06:44:42,773 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-25 06:44:42,773 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-25 06:44:42,773 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-25 06:44:42,774 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-25 06:44:42,774 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-25 06:44:42,775 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-25 06:44:42,775 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 06:44:42,803 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-25 06:44:42,828 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-25 06:44:42,960 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-25 06:44:43,073 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-25 06:44:43,084 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-25 06:44:43,151 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-25 06:44:43,228 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-25 06:44:43,304 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-25 06:44:43,317 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-25 06:44:43,341 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2023-12-31 00:00:00 (2326 days).
2025-09-25 06:44:43,717 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data starts at 2017-08-17 04:00:00
2025-09-25 06:44:44,447 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data starts at 2017-08-17 04:00:00
2025-09-25 06:44:44,595 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 5m, spot between two candles of 48.50% detected.
2025-09-25 06:44:45,092 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data starts at 2017-12-13 03:30:00
2025-09-25 06:44:45,863 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-25 06:44:46,454 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data starts at 2017-11-06 03:50:00
2025-09-25 06:44:46,609 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 5m, spot between two candles of 23.53% detected.
2025-09-25 06:44:49,665 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-25 06:44:49,718 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-25 06:44:49,721 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-25 06:44:49,730 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-25 06:44:49,734 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-25 06:44:49,735 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-25 06:44:49,736 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 10
2025-09-25 06:44:49,738 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-25 06:44:49,739 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-25 06:44:49,740 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-25 06:44:49,741 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-25 06:44:49,742 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.007
2025-09-25 06:44:49,744 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-25 06:44:49,746 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-25 06:44:49,749 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-25 06:44:49,751 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.007
2025-09-25 06:44:49,752 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.25
2025-09-25 06:44:49,753 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1.5
2025-09-25 06:44:49,755 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-09-25 06:44:49,756 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.998
2025-09-25 06:44:49,757 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 1
2025-09-25 06:44:49,759 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.996
2025-09-25 06:44:49,760 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-25 06:44:49,761 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-25 06:44:49,764 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = none
2025-09-25 06:44:49,768 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-09-25 06:44:49,771 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-25 06:44:49,773 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-25 06:44:49,775 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-25 06:44:49,777 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-25 06:44:49,784 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 06:44:49,843 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-25 06:44:49,890 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 06:44:49,984 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data starts at 2017-08-17 04:00:00
2025-09-25 06:45:04,671 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 06:45:04,691 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-25 06:45:04,712 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 06:45:04,745 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data starts at 2017-08-17 04:00:00
2025-09-25 06:45:04,749 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 4h, spot between two candles of 48.50% detected.
2025-09-25 06:45:19,796 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 06:45:19,817 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-25 06:45:19,840 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 06:45:19,881 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data starts at 2017-12-13 00:00:00
2025-09-25 06:45:31,784 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 06:45:31,817 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-25 06:45:31,848 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 06:45:31,897 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data starts at 2018-05-04 08:00:00
2025-09-25 06:45:41,171 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 06:45:41,189 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-25 06:45:41,202 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 06:45:41,229 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data starts at 2017-11-06 00:00:00
2025-09-25 06:45:41,234 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 4h, spot between two candles of 23.53% detected.
2025-09-25 06:45:52,884 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2017-08-17 04:00:00 up to 2023-12-31 00:00:00 (2326 days).
2025-09-25 06:54:39,924 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-25_06-54-39.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │    196 │         3.48 │         817.652 │        81.77 │ 2 days, 15:34:00 │   74     0   122  37.8 │
│ ETH/USDT │    203 │         2.08 │         535.994 │         53.6 │ 2 days, 20:03:00 │   82     0   121  40.4 │
│ BTC/USDT │    221 │         1.66 │         399.100 │        39.91 │ 2 days, 21:37:00 │   85     0   136  38.5 │
│ XRP/USDT │    128 │         1.72 │         286.494 │        28.65 │  2 days, 0:03:00 │   41     0    87  32.0 │
│ LTC/USDT │    155 │         0.23 │          42.147 │         4.21 │  2 days, 6:12:00 │   55     0   100  35.5 │
│    TOTAL │    903 │         1.91 │        2081.387 │       208.14 │ 2 days, 14:15:00 │  337     0   566  37.3 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │     704 │         1.74 │        1459.337 │       145.93 │ 2 days, 14:37:00 │  264     0   440  37.5 │
│         hammer_rebond │     131 │         2.63 │         401.363 │        40.14 │ 2 days, 10:54:00 │   42     0    89  32.1 │
│      engulfing_rebond │      68 │         2.33 │         220.686 │        22.07 │ 2 days, 16:54:00 │   31     0    37  45.6 │
│                 TOTAL │     903 │         1.91 │        2081.387 │       208.14 │ 2 days, 14:15:00 │  337     0   566  37.3 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                         EXIT REASON STATS                                                         
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                 Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ichimoku_cloud_crossed_exit │   894 │         1.12 │        1250.771 │       125.08 │ 2 days, 14:03:00 │  328     0   566  36.7 │
│              take_profit_3R │     8 │        90.36 │         819.549 │        81.95 │ 3 days, 20:28:00 │    8     0     0   100 │
│   ichimoku_cloud_futur_exit │     1 │         5.48 │          11.067 │         1.11 │          1:00:00 │    1     0     0   100 │
│                       TOTAL │   903 │         1.91 │        2081.387 │       208.14 │ 2 days, 14:15:00 │  337     0   566  37.3 │
└─────────────────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                                      MIXED TAG STATS                                                                       
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃                 Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ ichimoku_cloud_crossed_exit │    697 │         0.97 │         849.853 │        84.99 │ 2 days, 14:30:00 │  257     0   440  36.9 │
│ strong_bullish_rebond │              take_profit_3R │      6 │        90.85 │         598.417 │        59.84 │ 3 days, 14:43:00 │    6     0     0   100 │
│         hammer_rebond │              take_profit_3R │      2 │        88.89 │         221.132 │        22.11 │ 4 days, 13:42:00 │    2     0     0   100 │
│      engulfing_rebond │ ichimoku_cloud_crossed_exit │     68 │         2.33 │         220.686 │        22.07 │ 2 days, 16:54:00 │   31     0    37  45.6 │
│         hammer_rebond │ ichimoku_cloud_crossed_exit │    129 │         1.29 │         180.232 │        18.02 │ 2 days, 10:07:00 │   40     0    89  31.0 │
│ strong_bullish_rebond │   ichimoku_cloud_futur_exit │      1 │         5.48 │          11.067 │         1.11 │          1:00:00 │    1     0     0   100 │
│                 TOTAL │                             │    903 │         1.91 │        2081.387 │       208.14 │ 2 days, 14:15:00 │  337     0   566  37.3 │
└───────────────────────┴─────────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2017-08-17 04:00:00             │
│ Backtesting to                │ 2023-12-31 00:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 903 / 0.39                      │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 3081.387 USDT                   │
│ Absolute profit               │ 2081.387 USDT                   │
│ Total profit %                │ 208.14%                         │
│ CAGR %                        │ 19.31%                          │
│ Sortino                       │ 5.03                            │
│ Sharpe                        │ 1.15                            │
│ Calmar                        │ 22.20                           │
│ SQN                           │ 4.65                            │
│ Profit factor                 │ 1.87                            │
│ Expectancy (Ratio)            │ 2.30 (0.55)                     │
│ Avg. daily profit             │ 0.895 USDT                      │
│ Avg. stake amount             │ 146.312 USDT                    │
│ Total trade volume            │ 266853.874 USDT                 │
│                               │                                 │
│ Best Pair                     │ BNB/USDT 81.77%                 │
│ Worst Pair                    │ LTC/USDT 4.21%                  │
│ Best trade                    │ BNB/USDT 93.73%                 │
│ Worst trade                   │ BNB/USDT -20.56%                │
│ Best day                      │ 149.186 USDT                    │
│ Worst day                     │ -37.591 USDT                    │
│ Days win/draw/lose            │ 241 / 1680 / 358                │
│ Min/Max/Avg. Duration Winners │ 0d 01:00 / 16d 07:00 / 4d 14:30 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 5d 09:00 / 1d 09:31  │
│ Max Consecutive Wins / Loss   │ 7 / 17                          │
│ Rejected Entry signals        │ 9936                            │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 998.932 USDT                    │
│ Max balance                   │ 3081.387 USDT                   │
│ Max % of account underwater   │ 7.70%                           │
│ Absolute drawdown             │ 232.626 USDT (7.70%)            │
│ Drawdown duration             │ 241 days 21:00:00               │
│ Profit at drawdown start      │ 2020.526 USDT                   │
│ Profit at drawdown end        │ 1787.9 USDT                     │
│ Drawdown start                │ 2021-11-10 22:00:00             │
│ Drawdown end                  │ 2022-07-10 19:00:00             │
│ Market change                 │ 4006.86%                        │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2017-08-17 04:00:00 -> 2023-12-31 00:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃            Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    903 │         1.91 │        2081.387 │       208.14 │ 2 days, 14:15:00 │  337     0   566  37.3 │ 232.626 USDT  7.70% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┴─────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-25T08:54:41.406342",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 6867,
  "total_daily_avg_trades": "903 / 0.39",
  "absolute_profit_usdt": 2081.387,
  "total_profit_pct": 208.14,
  "cagr_pct": 19.31,
  "sortino": 5.03,
  "sharpe": 1.15,
  "calmar": 22.2,
  "sqn": 4.65,
  "max_consecutive_wins_loss": "7 / 17",
  "min_balance_usdt": 998.932,
  "max_balance_usdt": 3081.387,
  "absolute_drawdown_pct": 7.7,
  "market_change_pct": 4006.86,
  "win_draw_loss_winpct": "0 0 0 0"
}
```
