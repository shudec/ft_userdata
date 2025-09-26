# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 5524  
**Timestamp:** 2025-09-26 10:34:30

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 5524,
  "epochs": 100,
  "hyperopt_timerange": "20220101-20231231",
  "backtest_timerange": "20220101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231
```

## Backtesting Output
```
2025-09-26 08:31:13,021 - freqtrade - INFO - freqtrade 2025.8
2025-09-26 08:31:13,921 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-26 08:31:17,054 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-26 08:31:17,064 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-26 08:31:17,065 - freqtrade.loggers - INFO - Logfile configured
2025-09-26 08:31:17,066 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-26 08:31:17,067 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-26 08:31:17,068 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-26 08:31:17,069 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-26 08:31:17,070 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-26 08:31:17,778 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-26 08:31:17,780 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-26 08:31:17,781 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-26 08:31:17,781 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-26 08:31:17,781 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-26 08:31:17,782 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-26 08:31:17,783 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-26 08:31:17,795 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-26 08:31:17,796 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-26 08:31:17,799 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-26 08:31:17,799 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-26 08:31:17,800 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-26 08:31:17,819 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-26 08:31:24,662 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-26 08:31:24,802 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-26 08:31:24,804 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-26 08:31:24,810 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-26 08:31:24,810 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-26 08:31:24,811 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-26 08:31:24,811 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-26 08:31:24,812 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-26 08:31:24,812 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-26 08:31:24,813 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-26 08:31:24,813 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.05
2025-09-26 08:31:24,814 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-26 08:31:24,815 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-26 08:31:24,816 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-26 08:31:24,816 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-26 08:31:24,817 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-26 08:31:24,817 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-26 08:31:24,818 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-26 08:31:24,818 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-26 08:31:24,818 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-26 08:31:24,819 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-26 08:31:24,819 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-26 08:31:24,820 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-26 08:31:24,820 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-26 08:31:24,821 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-26 08:31:24,821 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-26 08:31:24,822 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-26 08:31:24,822 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-26 08:31:24,823 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-26 08:31:24,823 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-26 08:31:24,823 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-26 08:31:24,824 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-26 08:31:24,861 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-26 08:31:24,893 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-26 08:31:25,024 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-26 08:31:25,122 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-26 08:31:25,180 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-26 08:31:25,240 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-26 08:31:25,302 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-26 08:31:25,324 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-26 08:31:25,752 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-26 08:31:26,236 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-26 08:31:26,635 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-26 08:31:27,081 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-26 08:31:27,683 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-26 08:31:29,655 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-26 08:31:29,667 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-26 08:31:29,667 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-26 08:31:29,668 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.4
2025-09-26 08:31:29,669 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-26 08:31:29,669 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-26 08:31:29,670 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-26 08:31:29,670 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_adx_threshold = 20
2025-09-26 08:31:29,670 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 11
2025-09-26 08:31:29,671 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.614
2025-09-26 08:31:29,671 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.127
2025-09-26 08:31:29,672 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.04
2025-09-26 08:31:29,672 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.003
2025-09-26 08:31:29,673 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 70
2025-09-26 08:31:29,674 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 10
2025-09-26 08:31:29,675 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.409
2025-09-26 08:31:29,675 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.0
2025-09-26 08:31:29,676 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 2.5
2025-09-26 08:31:29,677 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 1
2025-09-26 08:31:29,677 - freqtrade.strategy.hyper - INFO - Strategy Parameter: custom_sell_atr_factor = 5
2025-09-26 08:31:29,678 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-26 08:31:29,678 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 4
2025-09-26 08:31:29,679 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-26 08:31:29,679 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-26 08:31:29,680 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_sell = True
2025-09-26 08:31:29,681 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-26 08:31:29,681 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = atr
2025-09-26 08:31:29,682 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_cloud_signal = True
2025-09-26 08:31:29,682 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_ichimoku_futur_cloud_signal = True
2025-09-26 08:31:29,682 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_kinjun_signal = False
2025-09-26 08:31:29,683 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-26 08:31:29,683 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-26 08:31:29,686 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-26 08:31:29,709 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-26 08:31:29,738 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-26 08:31:29,777 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-26 08:31:38,037 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-26 08:31:38,086 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-26 08:31:38,101 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-26 08:31:38,147 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-26 08:31:45,584 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-26 08:31:45,622 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-26 08:31:45,644 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-26 08:31:45,704 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-15 00:00:00
2025-09-26 08:31:53,571 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-26 08:31:53,617 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-26 08:31:53,651 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-26 08:31:53,694 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-26 08:32:03,725 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-26 08:32:03,744 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-26 08:32:03,763 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-26 08:32:03,806 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-26 08:32:10,990 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-26 08:34:28,548 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-26_08-34-28.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │     19 │         5.77 │         677.431 │        67.74 │ 6 days, 10:13:00 │   10     0     9  52.6 │
│ BNB/USDT │     13 │         5.36 │         378.568 │        37.86 │ 13 days, 5:23:00 │    7     0     6  53.8 │
│ BTC/USDT │     17 │         3.19 │         260.553 │        26.06 │ 17 days, 2:54:00 │    7     0    10  41.2 │
│ XRP/USDT │      5 │         4.25 │          82.344 │         8.23 │ 2 days, 13:31:00 │    2     0     3  40.0 │
│ LTC/USDT │      9 │        -2.81 │        -122.104 │       -12.21 │  3 days, 2:39:00 │    1     0     8  11.1 │
│    TOTAL │     63 │         3.64 │        1276.792 │       127.68 │ 9 days, 22:26:00 │   27     0    36  42.9 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         6.83 │          31.387 │         3.14 │ 30 days, 5:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         6.83 │          31.387 │         3.14 │ 30 days, 5:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                        ENTER TAG STATS                                                         
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │      50 │         3.07 │         721.271 │        72.13 │  9 days, 11:08:00 │   20     0    30  40.0 │
│      engulfing_rebond │      13 │         5.83 │         555.521 │        55.55 │ 11 days, 17:51:00 │    7     0     6  53.8 │
│                 TOTAL │      63 │         3.64 │        1276.792 │       127.68 │  9 days, 22:26:00 │   27     0    36  42.9 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │    26 │        15.75 │        2360.176 │       236.02 │ 12 days, 7:40:00 │   26     0     0   100 │
│     force_exit │     1 │         6.83 │          31.387 │         3.14 │ 30 days, 5:00:00 │    1     0     0   100 │
│      stop_loss │    36 │        -5.19 │       -1114.772 │      -111.48 │ 7 days, 15:35:00 │    0     0    36     0 │
│          TOTAL │    63 │         3.64 │        1276.792 │       127.68 │ 9 days, 22:26:00 │   27     0    36  42.9 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                                MIXED TAG STATS                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_3R │     19 │        15.93 │        1597.660 │       159.77 │ 11 days, 13:56:00 │   19     0     0   100 │
│      engulfing_rebond │ take_profit_3R │      7 │        15.28 │         762.517 │        76.25 │  14 days, 7:46:00 │    7     0     0   100 │
│ strong_bullish_rebond │     force_exit │      1 │         6.83 │          31.387 │         3.14 │  30 days, 5:00:00 │    1     0     0   100 │
│      engulfing_rebond │      stop_loss │      6 │        -5.19 │        -206.996 │        -20.7 │  8 days, 17:37:00 │    0     0     6     0 │
│ strong_bullish_rebond │      stop_loss │     30 │        -5.19 │        -907.776 │       -90.78 │  7 days, 10:22:00 │    0     0    30     0 │
│                 TOTAL │                │     63 │         3.64 │        1276.792 │       127.68 │  9 days, 22:26:00 │   27     0    36  42.9 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                          SUMMARY METRICS                           
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                            ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00              │
│ Backtesting to                │ 2025-09-10 08:00:00              │
│ Trading Mode                  │ Spot                             │
│ Max open trades               │ 3                                │
│                               │                                  │
│ Total/Daily Avg Trades        │ 63 / 0.05                        │
│ Starting balance              │ 1000 USDT                        │
│ Final balance                 │ 2276.792 USDT                    │
│ Absolute profit               │ 1276.792 USDT                    │
│ Total profit %                │ 127.68%                          │
│ CAGR %                        │ 24.95%                           │
│ Sortino                       │ 1.81                             │
│ Sharpe                        │ 0.29                             │
│ Calmar                        │ 11.79                            │
│ SQN                           │ 2.57                             │
│ Profit factor                 │ 2.15                             │
│ Expectancy (Ratio)            │ 20.27 (0.65)                     │
│ Avg. daily profit             │ 0.947 USDT                       │
│ Avg. stake amount             │ 586.577 USDT                     │
│ Total trade volume            │ 75335.967 USDT                   │
│                               │                                  │
│ Best Pair                     │ ETH/USDT 67.74%                  │
│ Worst Pair                    │ LTC/USDT -12.21%                 │
│ Best trade                    │ XRP/USDT 21.53%                  │
│ Worst trade                   │ BNB/USDT -5.19%                  │
│ Best day                      │ 132.451 USDT                     │
│ Worst day                     │ -45.26 USDT                      │
│ Days win/draw/lose            │ 26 / 1241 / 35                   │
│ Min/Max/Avg. Duration Winners │ 0d 00:25 / 41d 04:15 / 12d 23:34 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:30 / 45d 15:45 / 7d 15:35  │
│ Max Consecutive Wins / Loss   │ 6 / 8                            │
│ Rejected Entry signals        │ 12                               │
│ Entry/Exit Timeouts           │ 0 / 0                            │
│                               │                                  │
│ Min balance                   │ 979.441 USDT                     │
│ Max balance                   │ 2288.069 USDT                    │
│ Max % of account underwater   │ 15.35%                           │
│ Absolute drawdown             │ 323.881 USDT (15.35%)            │
│ Drawdown duration             │ 239 days 09:00:00                │
│ Profit at drawdown start      │ 1109.402 USDT                    │
│ Profit at drawdown end        │ 785.521 USDT                     │
│ Drawdown start                │ 2024-02-19 06:05:00              │
│ Drawdown end                  │ 2024-10-15 15:05:00              │
│ Market change                 │ 91.49%                           │
└───────────────────────────────┴──────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     63 │         3.64 │        1276.792 │       127.68 │ 9 days, 22:26:00 │   27     0    36  42.9 │ 323.881 USDT  15.35% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-26T10:34:30.005960",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 5524,
  "total_daily_avg_trades": "63 / 0.05",
  "absolute_profit_usdt": 1276.792,
  "total_profit_pct": 127.68,
  "cagr_pct": 24.95,
  "sortino": 1.81,
  "sharpe": 0.29,
  "calmar": 11.79,
  "sqn": 2.57,
  "max_consecutive_wins_loss": "6 / 8",
  "min_balance_usdt": 979.441,
  "max_balance_usdt": 2288.069,
  "absolute_drawdown_pct": 15.35,
  "market_change_pct": 91.49
}
```
