# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 4228  
**Timestamp:** 2025-09-24 09:09:09

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 4228,
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
2025-09-24 07:00:47,374 - freqtrade - INFO - freqtrade 2025.8
2025-09-24 07:00:47,663 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-24 07:00:49,188 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-24 07:00:49,194 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-24 07:00:49,195 - freqtrade.loggers - INFO - Logfile configured
2025-09-24 07:00:49,196 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-24 07:00:49,197 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-24 07:00:49,197 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-24 07:00:49,198 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-24 07:00:49,198 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20200101-20251231 ...
2025-09-24 07:00:49,650 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-24 07:00:49,652 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-24 07:00:49,653 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-24 07:00:49,653 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-24 07:00:49,654 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-24 07:00:49,654 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20200101-20251231
2025-09-24 07:00:49,655 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-24 07:00:49,667 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-24 07:00:49,668 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 07:00:49,670 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-24 07:00:49,671 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-24 07:00:49,671 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-24 07:00:49,693 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-24 07:00:52,026 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-24 07:00:52,122 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-24 07:00:52,125 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-24 07:00:52,129 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-24 07:00:52,130 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-24 07:00:52,130 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-24 07:00:52,130 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-24 07:00:52,131 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-24 07:00:52,131 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-24 07:00:52,132 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-24 07:00:52,132 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-24 07:00:52,133 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-24 07:00:52,133 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-24 07:00:52,134 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-24 07:00:52,134 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-24 07:00:52,134 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-24 07:00:52,135 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-24 07:00:52,135 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-24 07:00:52,136 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-24 07:00:52,136 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-24 07:00:52,136 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-24 07:00:52,137 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-24 07:00:52,137 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-24 07:00:52,137 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-24 07:00:52,138 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-24 07:00:52,138 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-24 07:00:52,138 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-24 07:00:52,139 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-24 07:00:52,139 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-24 07:00:52,139 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-24 07:00:52,140 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-24 07:00:52,140 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 07:00:52,156 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-24 07:00:52,179 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-24 07:00:52,227 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 07:00:52,294 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 07:00:52,355 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 07:00:52,415 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 07:00:52,478 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 07:00:52,511 - freqtrade.optimize.backtesting - INFO - Loading data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 07:00:52,785 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 07:00:53,358 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 07:00:53,895 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 07:00:54,386 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 07:00:54,910 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 07:00:56,793 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-24 07:00:56,799 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-24 07:00:56,800 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-24 07:00:56,801 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-24 07:00:56,802 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-24 07:00:56,803 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-24 07:00:56,803 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-24 07:00:56,804 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-24 07:00:56,804 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-24 07:00:56,805 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-24 07:00:56,805 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-24 07:00:56,806 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-24 07:00:56,807 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-09-24 07:00:56,808 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-09-24 07:00:56,808 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-24 07:00:56,809 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-24 07:00:56,809 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-24 07:00:56,810 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-24 07:00:56,810 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-24 07:00:56,811 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 8
2025-09-24 07:00:56,811 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-24 07:00:56,812 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-24 07:00:56,813 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-24 07:00:56,814 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-24 07:00:56,814 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-24 07:00:56,815 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-24 07:00:56,820 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:00:56,842 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 07:00:56,867 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:00:56,900 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 07:01:12,540 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:01:12,556 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 07:01:12,570 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:01:12,593 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 07:01:30,246 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:01:30,263 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 07:01:30,281 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:01:30,304 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-15 00:00:00
2025-09-24 07:01:46,952 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:01:46,978 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 07:01:47,016 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:01:47,067 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 07:02:03,045 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:02:03,062 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 07:02:03,077 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 07:02:03,100 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 07:02:19,835 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 07:09:07,455 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-24_07-09-07.meta.json"
Result for strategy IchimokuRebondStrategy
                                              BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │    281 │         0.08 │          50.675 │         5.07 │ 1 day, 5:42:00 │  144     0   137  51.2 │
│ LTC/USDT │    165 │        -0.11 │         -28.327 │        -2.83 │ 1 day, 8:59:00 │   87     0    78  52.7 │
│ ETH/USDT │    248 │        -0.03 │        -110.491 │       -11.05 │ 1 day, 0:09:00 │  127     0   121  51.2 │
│ BNB/USDT │    243 │        -0.13 │        -129.725 │       -12.97 │ 1 day, 2:50:00 │  128     0   115  52.7 │
│ XRP/USDT │    167 │        -0.56 │        -205.653 │       -20.57 │ 1 day, 4:50:00 │   86     0    81  51.5 │
│    TOTAL │   1104 │        -0.11 │        -423.521 │       -42.35 │ 1 day, 4:11:00 │  572     0   532  51.8 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                            LEFT OPEN TRADES REPORT                                            
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         0.07 │           0.205 │         0.02 │ 1 day, 1:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         0.07 │           0.205 │         0.02 │ 1 day, 1:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                       ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│         hammer_rebond │     142 │         0.17 │          54.155 │         5.42 │ 1 day, 23:55:00 │   88     0    54  62.0 │
│      engulfing_rebond │     121 │         0.09 │          44.712 │         4.47 │        22:08:00 │   69     0    52  57.0 │
│ strong_bullish_rebond │     841 │        -0.19 │        -522.388 │       -52.24 │  1 day, 1:43:00 │  415     0   426  49.3 │
│                 TOTAL │    1104 │        -0.11 │        -423.521 │       -42.35 │  1 day, 4:11:00 │  572     0   532  51.8 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│    exit_signal │   772 │         0.76 │        1507.404 │       150.74 │        20:04:00 │  470     0   302  60.9 │
│ take_profit_1R │   101 │         5.75 │        1500.328 │       150.03 │ 1 day, 15:47:00 │  101     0     0   100 │
│     force_exit │     1 │         0.07 │           0.205 │         0.02 │  1 day, 1:00:00 │    1     0     0   100 │
│      stop_loss │   230 │        -5.63 │       -3431.458 │      -343.15 │ 2 days, 2:21:00 │    0     0   230     0 │
│          TOTAL │  1104 │        -0.11 │        -423.521 │       -42.35 │  1 day, 4:11:00 │  572     0   532  51.8 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                               MIXED TAG STATS                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │    exit_signal │    612 │         0.63 │         962.252 │        96.23 │        17:57:00 │  349     0   263  57.0 │
│ strong_bullish_rebond │ take_profit_1R │     65 │         5.39 │         944.087 │        94.41 │ 1 day, 14:31:00 │   65     0     0   100 │
│         hammer_rebond │ take_profit_1R │     25 │         6.49 │         408.477 │        40.85 │ 1 day, 20:41:00 │   25     0     0   100 │
│         hammer_rebond │    exit_signal │     69 │          2.1 │         383.720 │        38.37 │ 1 day, 19:39:00 │   63     0     6  91.3 │
│      engulfing_rebond │    exit_signal │     91 │         0.64 │         161.432 │        16.14 │        16:22:00 │   58     0    33  63.7 │
│      engulfing_rebond │ take_profit_1R │     11 │         6.19 │         147.764 │        14.78 │ 1 day, 12:04:00 │   11     0     0   100 │
│ strong_bullish_rebond │     force_exit │      1 │         0.07 │           0.205 │         0.02 │  1 day, 1:00:00 │    1     0     0   100 │
│      engulfing_rebond │      stop_loss │     19 │        -6.08 │        -264.485 │       -26.45 │ 1 day, 17:39:00 │    0     0    19     0 │
│         hammer_rebond │      stop_loss │     48 │         -5.9 │        -738.042 │        -73.8 │ 2 days, 7:45:00 │    0     0    48     0 │
│ strong_bullish_rebond │      stop_loss │    163 │         -5.5 │       -2428.932 │      -242.89 │ 2 days, 1:47:00 │    0     0   163     0 │
│                 TOTAL │                │   1104 │        -0.11 │        -423.521 │       -42.35 │  1 day, 4:11:00 │  572     0   532  51.8 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2020-01-01 00:00:00             │
│ Backtesting to                │ 2025-09-10 08:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 1104 / 0.53                     │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 576.479 USDT                    │
│ Absolute profit               │ -423.521 USDT                   │
│ Total profit %                │ -42.35%                         │
│ CAGR %                        │ -9.22%                          │
│ Sortino                       │ -0.52                           │
│ Sharpe                        │ -0.41                           │
│ Calmar                        │ -0.67                           │
│ SQN                           │ -1.36                           │
│ Profit factor                 │ 0.89                            │
│ Expectancy (Ratio)            │ -0.38 (-0.05)                   │
│ Avg. daily profit             │ -0.204 USDT                     │
│ Avg. stake amount             │ 259.409 USDT                    │
│ Total trade volume            │ 573497.381 USDT                 │
│                               │                                 │
│ Best Pair                     │ BTC/USDT 5.07%                  │
│ Worst Pair                    │ XRP/USDT -20.57%                │
│ Best trade                    │ XRP/USDT 13.21%                 │
│ Worst trade                   │ XRP/USDT -17.81%                │
│ Best day                      │ 43.101 USDT                     │
│ Worst day                     │ -61.934 USDT                    │
│ Days win/draw/lose            │ 375 / 1348 / 320                │
│ Min/Max/Avg. Duration Winners │ 0d 00:50 / 9d 18:00 / 1d 04:15  │
│ Min/Max/Avg. Duration Losers  │ 0d 00:30 / 11d 17:00 / 1d 04:06 │
│ Max Consecutive Wins / Loss   │ 12 / 15                         │
│ Rejected Entry signals        │ 866                             │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 496.568 USDT                    │
│ Max balance                   │ 1173.144 USDT                   │
│ Max % of account underwater   │ 57.67%                          │
│ Absolute drawdown             │ 676.576 USDT (57.67%)           │
│ Drawdown duration             │ 1319 days 00:00:00              │
│ Profit at drawdown start      │ 173.144 USDT                    │
│ Profit at drawdown end        │ -503.432 USDT                   │
│ Drawdown start                │ 2021-11-13 19:00:00             │
│ Drawdown end                  │ 2025-06-24 19:00:00             │
│ Market change                 │ 2537.81%                        │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2020-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                  
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │   1104 │        -0.11 │        -423.521 │       -42.35 │ 1 day, 4:11:00 │  572     0   532  51.8 │ 676.576 USDT  57.67% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-24T09:09:09.339525",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 4228,
  "total_daily_avg_trades": "1104 / 0.53",
  "absolute_profit_usdt": -423.521,
  "total_profit_pct": -42.35,
  "cagr_pct": -9.22,
  "sortino": -0.52,
  "sharpe": -0.41,
  "calmar": -0.67,
  "sqn": -1.36,
  "max_consecutive_wins_loss": "12 / 15",
  "min_balance_usdt": 496.568,
  "max_balance_usdt": 1173.144,
  "absolute_drawdown_pct": 57.67,
  "market_change_pct": 2537.81
}
```
