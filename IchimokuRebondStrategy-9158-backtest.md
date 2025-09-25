# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 9158  
**Timestamp:** 2025-09-25 15:25:45

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 9158,
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
2025-09-25 13:16:07,269 - freqtrade - INFO - freqtrade 2025.8
2025-09-25 13:16:07,876 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-25 13:16:10,414 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-25 13:16:10,420 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-25 13:16:10,420 - freqtrade.loggers - INFO - Logfile configured
2025-09-25 13:16:10,421 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-25 13:16:10,421 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-25 13:16:10,422 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-25 13:16:10,422 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-25 13:16:10,423 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20231231 ...
2025-09-25 13:16:10,997 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-25 13:16:10,999 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-25 13:16:10,999 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-25 13:16:11,000 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-25 13:16:11,000 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-25 13:16:11,000 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20231231
2025-09-25 13:16:11,002 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-25 13:16:11,013 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-25 13:16:11,014 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 13:16:11,017 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-25 13:16:11,018 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-25 13:16:11,018 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-25 13:16:11,041 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-25 13:16:13,563 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-25 13:16:13,675 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-25 13:16:13,677 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-25 13:16:13,682 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-25 13:16:13,682 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-25 13:16:13,683 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-25 13:16:13,683 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-25 13:16:13,684 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-25 13:16:13,684 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-25 13:16:13,685 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-25 13:16:13,685 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-25 13:16:13,685 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-25 13:16:13,686 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-25 13:16:13,686 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-25 13:16:13,686 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-25 13:16:13,687 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-25 13:16:13,687 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-25 13:16:13,688 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-25 13:16:13,688 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-25 13:16:13,689 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-25 13:16:13,689 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-25 13:16:13,689 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-25 13:16:13,690 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-25 13:16:13,691 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-25 13:16:13,691 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-25 13:16:13,692 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-25 13:16:13,692 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-25 13:16:13,692 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-25 13:16:13,693 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-25 13:16:13,693 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-25 13:16:13,694 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-25 13:16:13,694 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-25 13:16:13,720 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-25 13:16:13,744 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-25 13:16:13,797 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-25 13:16:13,876 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-25 13:16:13,887 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-25 13:16:13,937 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-25 13:16:13,992 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-25 13:16:14,046 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-25 13:16:14,059 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-25 13:16:14,079 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2023-12-31 00:00:00 (2326 days).
2025-09-25 13:16:14,311 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data starts at 2017-08-17 04:00:00
2025-09-25 13:16:14,891 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data starts at 2017-08-17 04:00:00
2025-09-25 13:16:15,057 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 5m, spot between two candles of 48.50% detected.
2025-09-25 13:16:15,438 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data starts at 2017-12-13 03:30:00
2025-09-25 13:16:15,927 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-25 13:16:16,419 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data starts at 2017-11-06 03:50:00
2025-09-25 13:16:16,575 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 5m, spot between two candles of 23.53% detected.
2025-09-25 13:16:18,619 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-25 13:16:18,640 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-25 13:16:18,641 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-25 13:16:18,641 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-25 13:16:18,642 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-25 13:16:18,642 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-25 13:16:18,643 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 5
2025-09-25 13:16:18,643 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-25 13:16:18,644 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-25 13:16:18,644 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-25 13:16:18,645 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-25 13:16:18,645 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.007
2025-09-25 13:16:18,645 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-25 13:16:18,646 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-25 13:16:18,646 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-25 13:16:18,647 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.007
2025-09-25 13:16:18,647 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.25
2025-09-25 13:16:18,648 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 0.5
2025-09-25 13:16:18,648 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 6
2025-09-25 13:16:18,649 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.998
2025-09-25 13:16:18,649 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 2
2025-09-25 13:16:18,649 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.99
2025-09-25 13:16:18,650 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-25 13:16:18,650 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = False
2025-09-25 13:16:18,651 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-25 13:16:18,651 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-25 13:16:18,652 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-09-25 13:16:18,652 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-25 13:16:18,652 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-25 13:16:18,653 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-25 13:16:18,654 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-25 13:16:18,658 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 13:16:18,677 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-25 13:16:18,699 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 13:16:18,726 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data starts at 2017-08-17 04:00:00
2025-09-25 13:16:34,271 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 13:16:34,288 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-25 13:16:34,304 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 13:16:34,331 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data starts at 2017-08-17 04:00:00
2025-09-25 13:16:34,337 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 4h, spot between two candles of 48.50% detected.
2025-09-25 13:16:50,012 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 13:16:50,027 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-25 13:16:50,049 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 13:16:50,077 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data starts at 2017-12-13 00:00:00
2025-09-25 13:17:05,366 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 13:17:05,380 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-25 13:17:05,393 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 13:17:05,415 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data starts at 2018-05-04 08:00:00
2025-09-25 13:17:19,731 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 13:17:19,757 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-25 13:17:19,786 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2017-08-01 00:00:00 to 2023-12-31 00:00:00
2025-09-25 13:17:19,820 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data starts at 2017-11-06 00:00:00
2025-09-25 13:17:19,825 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 4h, spot between two candles of 23.53% detected.
2025-09-25 13:17:36,428 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2017-08-17 04:00:00 up to 2023-12-31 00:00:00 (2326 days).
2025-09-25 13:25:43,612 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-25_13-25-43.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │    199 │         1.66 │       32726.942 │      3272.69 │ 2 days, 10:50:00 │   71     0   128  35.7 │
│ BTC/USDT │    210 │         1.65 │       31624.714 │      3162.47 │ 2 days, 14:26:00 │   77     0   133  36.7 │
│ BNB/USDT │    183 │         3.03 │       21745.482 │      2174.55 │  2 days, 7:53:00 │   61     0   122  33.3 │
│ XRP/USDT │    110 │         1.89 │        9368.839 │       936.88 │  1 day, 20:43:00 │   33     0    77  30.0 │
│ LTC/USDT │    145 │          0.1 │       -9559.051 │      -955.91 │  2 days, 1:16:00 │   47     0    98  32.4 │
│    TOTAL │    847 │         1.72 │       85906.926 │      8590.69 │  2 days, 7:37:00 │  289     0   558  34.1 │
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
│ strong_bullish_rebond │     638 │         1.85 │       58301.198 │      5830.12 │ 2 days, 11:49:00 │  232     0   406  36.4 │
│         hammer_rebond │     143 │         1.77 │       18589.711 │      1858.97 │  1 day, 16:39:00 │   34     0   109  23.8 │
│      engulfing_rebond │      66 │         0.32 │        9016.016 │        901.6 │  1 day, 23:25:00 │   23     0    43  34.8 │
│                 TOTAL │     847 │         1.72 │       85906.926 │      8590.69 │  2 days, 7:37:00 │  289     0   558  34.1 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                        EXIT REASON STATS                                                         
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                 Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ichimoku_cloud_crossed_exit │   560 │         4.41 │      237817.521 │     23781.75 │ 3 days, 3:29:00 │  289     0   271  51.6 │
│                   stop_loss │   287 │        -3.54 │     -151910.596 │    -15191.06 │        16:51:00 │    0     0   287     0 │
│                       TOTAL │   847 │         1.72 │       85906.926 │      8590.69 │ 2 days, 7:37:00 │  289     0   558  34.1 │
└─────────────────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                                      MIXED TAG STATS                                                                       
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃                 Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ ichimoku_cloud_crossed_exit │    456 │         4.15 │      164871.345 │     16487.13 │  3 days, 4:19:00 │  232     0   224  50.9 │
│         hammer_rebond │ ichimoku_cloud_crossed_exit │     58 │         8.28 │       53715.399 │      5371.54 │  3 days, 8:39:00 │   34     0    24  58.6 │
│      engulfing_rebond │ ichimoku_cloud_crossed_exit │     46 │         2.08 │       19230.778 │      1923.08 │ 2 days, 12:39:00 │   23     0    23  50.0 │
│      engulfing_rebond │                   stop_loss │     20 │        -3.72 │      -10214.762 │     -1021.48 │         16:58:00 │    0     0    20     0 │
│         hammer_rebond │                   stop_loss │     85 │        -2.67 │      -35125.688 │     -3512.57 │         13:21:00 │    0     0    85     0 │
│ strong_bullish_rebond │                   stop_loss │    182 │        -3.93 │     -106570.147 │    -10657.01 │         18:29:00 │    0     0   182     0 │
│                 TOTAL │                             │    847 │         1.72 │       85906.926 │      8590.69 │  2 days, 7:37:00 │  289     0   558  34.1 │
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
│ Total/Daily Avg Trades        │ 847 / 0.36                      │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 86906.926 USDT                  │
│ Absolute profit               │ 85906.926 USDT                  │
│ Total profit %                │ 8590.69%                        │
│ CAGR %                        │ 101.50%                         │
│ Sortino                       │ 1.45                            │
│ Sharpe                        │ 0.46                            │
│ Calmar                        │ 224.50                          │
│ SQN                           │ 1.93                            │
│ Profit factor                 │ 1.36                            │
│ Expectancy (Ratio)            │ 101.42 (0.24)                   │
│ Avg. daily profit             │ 36.933 USDT                     │
│ Avg. stake amount             │ 16822.106 USDT                  │
│ Total trade volume            │ 28639776.401 USDT               │
│                               │                                 │
│ Best Pair                     │ ETH/USDT 3272.69%               │
│ Worst Pair                    │ LTC/USDT -955.91%               │
│ Best trade                    │ BNB/USDT 166.24%                │
│ Worst trade                   │ BNB/USDT -20.56%                │
│ Best day                      │ 18602.311 USDT                  │
│ Worst day                     │ -3647.272 USDT                  │
│ Days win/draw/lose            │ 217 / 1693 / 369                │
│ Min/Max/Avg. Duration Winners │ 1d 04:00 / 16d 07:00 / 4d 16:23 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:05 / 4d 15:00 / 1d 02:13  │
│ Max Consecutive Wins / Loss   │ 10 / 20                         │
│ Rejected Entry signals        │ 6145                            │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 988.027 USDT                    │
│ Max balance                   │ 100152.456 USDT                 │
│ Max % of account underwater   │ 31.43%                          │
│ Absolute drawdown             │ 31477.785 USDT (31.43%)         │
│ Drawdown duration             │ 705 days 17:45:00               │
│ Profit at drawdown start      │ 99152.456 USDT                  │
│ Profit at drawdown end        │ 67674.671 USDT                  │
│ Drawdown start                │ 2021-11-10 20:00:00             │
│ Drawdown end                  │ 2023-10-17 13:45:00             │
│ Market change                 │ 4006.86%                        │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2017-08-17 04:00:00 -> 2023-12-31 00:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                    
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃               Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    847 │         1.72 │       85906.926 │      8590.69 │ 2 days, 7:37:00 │  289     0   558  34.1 │ 31477.785 USDT  31.43% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴────────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-25T15:25:45.198000",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 9158,
  "total_daily_avg_trades": "847 / 0.36",
  "absolute_profit_usdt": 85906.926,
  "total_profit_pct": 8590.69,
  "cagr_pct": 101.5,
  "sortino": 1.45,
  "sharpe": 0.46,
  "calmar": 224.5,
  "sqn": 1.93,
  "max_consecutive_wins_loss": "10 / 20",
  "min_balance_usdt": 988.027,
  "max_balance_usdt": 100152.456,
  "absolute_drawdown_pct": 31.43,
  "market_change_pct": 4006.86,
  "win_draw_loss_winpct": "0 0 0 0"
}
```
