# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 3040  
**Timestamp:** 2025-09-23 18:29:32

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 3040,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20180101-20251231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20180101-20251231
```

## Backtesting Output
```
2025-09-23 16:23:56,606 - freqtrade - INFO - freqtrade 2025.8
2025-09-23 16:23:56,959 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-23 16:23:58,461 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-23 16:23:58,466 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-23 16:23:58,467 - freqtrade.loggers - INFO - Logfile configured
2025-09-23 16:23:58,467 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-23 16:23:58,468 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-23 16:23:58,468 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-23 16:23:58,469 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-23 16:23:58,469 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20180101-20251231 ...
2025-09-23 16:23:58,858 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-23 16:23:58,861 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-23 16:23:58,862 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-23 16:23:58,862 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-23 16:23:58,863 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-23 16:23:58,863 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20180101-20251231
2025-09-23 16:23:58,864 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-23 16:23:58,874 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-23 16:23:58,875 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 16:23:58,877 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-23 16:23:58,878 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-23 16:23:58,879 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-23 16:23:58,900 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-23 16:24:01,507 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-23 16:24:01,602 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-23 16:24:01,604 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-23 16:24:01,608 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-23 16:24:01,608 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-23 16:24:01,609 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-23 16:24:01,609 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-23 16:24:01,609 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-23 16:24:01,610 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-23 16:24:01,610 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-23 16:24:01,611 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-23 16:24:01,611 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-23 16:24:01,611 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-23 16:24:01,612 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-23 16:24:01,612 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-23 16:24:01,612 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-23 16:24:01,612 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-23 16:24:01,613 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-23 16:24:01,614 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-23 16:24:01,614 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-23 16:24:01,615 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-23 16:24:01,616 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-23 16:24:01,616 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-23 16:24:01,617 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-23 16:24:01,618 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-23 16:24:01,619 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-23 16:24:01,619 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-23 16:24:01,619 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-23 16:24:01,620 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-23 16:24:01,620 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-23 16:24:01,621 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-23 16:24:01,621 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-23 16:24:01,640 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-23 16:24:01,671 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-23 16:24:01,734 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 16:24:01,833 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 16:24:01,907 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 16:24:01,988 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-23 16:24:01,989 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 16:24:02,086 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-23 16:24:02,141 - freqtrade.optimize.backtesting - INFO - Loading data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 16:24:02,445 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 16:24:03,214 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 16:24:03,928 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 16:24:04,644 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data starts at 2018-05-04 08:10:00
2025-09-23 16:24:04,646 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 16:24:05,376 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-23 16:24:08,980 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-23 16:24:08,986 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-23 16:24:08,986 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-23 16:24:08,987 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-23 16:24:08,988 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-23 16:24:08,989 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-23 16:24:08,990 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-23 16:24:08,990 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-23 16:24:08,990 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-23 16:24:08,991 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-23 16:24:08,991 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-23 16:24:08,992 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-23 16:24:08,992 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 40
2025-09-23 16:24:08,992 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-09-23 16:24:08,993 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-23 16:24:08,993 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-23 16:24:08,994 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-23 16:24:08,994 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-23 16:24:08,994 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-23 16:24:08,995 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 1
2025-09-23 16:24:08,995 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-23 16:24:08,995 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-23 16:24:08,996 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-23 16:24:08,996 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower
2025-09-23 16:24:08,996 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-23 16:24:08,997 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-23 16:24:09,000 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:24:09,018 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 16:24:09,039 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:24:09,064 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-23 16:24:26,950 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:24:26,968 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 16:24:26,987 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:24:27,014 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-23 16:24:42,311 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:24:42,329 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 16:24:42,351 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:24:42,383 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-15 00:00:00
2025-09-23 16:24:56,637 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:24:56,652 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-23 16:24:56,653 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 16:24:56,669 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:24:56,692 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data starts at 2018-05-04 08:00:00
2025-09-23 16:24:56,693 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-23 16:25:10,228 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:25:10,255 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-23 16:25:10,284 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2018-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-23 16:25:10,312 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-23 16:25:24,780 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2018-01-01 00:00:00 up to 2025-09-10 08:00:00 (2809 days).
2025-09-23 16:29:31,046 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-23_16-29-30.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │    209 │         0.66 │         448.457 │        44.85 │     14:11:00 │   79     0   130  37.8 │
│ ETH/USDT │    295 │          0.4 │         413.501 │        41.35 │     16:32:00 │  104     0   191  35.3 │
│ BTC/USDT │    354 │          0.3 │         281.234 │        28.12 │     17:40:00 │  118     0   236  33.3 │
│ BNB/USDT │    303 │         0.14 │          40.971 │          4.1 │     16:25:00 │   96     0   207  31.7 │
│ LTC/USDT │    211 │         -0.2 │        -231.638 │       -23.16 │     15:05:00 │   62     0   149  29.4 │
│    TOTAL │   1372 │         0.27 │         952.525 │        95.25 │     16:13:00 │  459     0   913  33.5 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                           LEFT OPEN TRADES REPORT                                           
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         0.05 │           0.186 │         0.02 │      5:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         0.05 │           0.186 │         0.02 │      5:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                      ENTER TAG STATS                                                      
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │    1051 │         0.27 │         738.196 │        73.82 │     16:53:00 │  360     0   691  34.3 │
│      engulfing_rebond │     140 │         0.31 │         135.748 │        13.57 │     15:48:00 │   49     0    91  35.0 │
│         hammer_rebond │     181 │         0.21 │          78.580 │         7.86 │     12:44:00 │   50     0   131  27.6 │
│                 TOTAL │    1372 │         0.27 │         952.525 │        95.25 │     16:13:00 │  459     0   913  33.5 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │   114 │        10.47 │        3719.121 │       371.91 │     23:49:00 │  114     0     0   100 │
│     force_exit │     1 │         0.05 │           0.186 │         0.02 │      5:00:00 │    1     0     0   100 │
│      stop_loss │     5 │       -10.18 │        -134.512 │       -13.45 │      4:51:00 │    0     0     5     0 │
│    exit_signal │  1252 │        -0.62 │       -2632.271 │      -263.23 │     15:35:00 │  344     0   908  27.5 │
│          TOTAL │  1372 │         0.27 │         952.525 │        95.25 │     16:13:00 │  459     0   913  33.5 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                               MIXED TAG STATS                                                               
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_1R │     86 │        10.45 │        2796.318 │       279.63 │       23:32:00 │   86     0     0   100 │
│      engulfing_rebond │ take_profit_1R │     14 │        10.56 │         470.704 │        47.07 │       20:20:00 │   14     0     0   100 │
│         hammer_rebond │ take_profit_1R │     14 │        10.56 │         452.100 │        45.21 │ 1 day, 5:04:00 │   14     0     0   100 │
│ strong_bullish_rebond │     force_exit │      1 │         0.05 │           0.186 │         0.02 │        5:00:00 │    1     0     0   100 │
│ strong_bullish_rebond │      stop_loss │      5 │       -10.18 │        -134.512 │       -13.45 │        4:51:00 │    0     0     5     0 │
│      engulfing_rebond │    exit_signal │    126 │        -0.83 │        -334.955 │        -33.5 │       15:18:00 │   35     0    91  27.8 │
│         hammer_rebond │    exit_signal │    167 │        -0.66 │        -373.520 │       -37.35 │       11:22:00 │   36     0   131  21.6 │
│ strong_bullish_rebond │    exit_signal │    959 │        -0.59 │       -1923.796 │      -192.38 │       16:21:00 │  273     0   686  28.5 │
│                 TOTAL │                │   1372 │         0.27 │         952.525 │        95.25 │       16:13:00 │  459     0   913  33.5 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2018-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 1372 / 0.49                    │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1952.525 USDT                  │
│ Absolute profit               │ 952.525 USDT                   │
│ Total profit %                │ 95.25%                         │
│ CAGR %                        │ 9.08%                          │
│ Sortino                       │ 1.42                           │
│ Sharpe                        │ 0.54                           │
│ Calmar                        │ 3.17                           │
│ SQN                           │ 2.13                           │
│ Profit factor                 │ 1.19                           │
│ Expectancy (Ratio)            │ 0.69 (0.13)                    │
│ Avg. daily profit             │ 0.339 USDT                     │
│ Avg. stake amount             │ 339.785 USDT                   │
│ Total trade volume            │ 935190.864 USDT                │
│                               │                                │
│ Best Pair                     │ XRP/USDT 44.85%                │
│ Worst Pair                    │ LTC/USDT -23.16%               │
│ Best trade                    │ XRP/USDT 13.21%                │
│ Worst trade                   │ LTC/USDT -10.18%               │
│ Best day                      │ 112.106 USDT                   │
│ Worst day                     │ -58.998 USDT                   │
│ Days win/draw/lose            │ 284 / 1937 / 539               │
│ Min/Max/Avg. Duration Winners │ 0d 00:20 / 3d 05:35 / 1d 03:53 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 1d 22:00 / 0d 10:21 │
│ Max Consecutive Wins / Loss   │ 6 / 23                         │
│ Rejected Entry signals        │ 1207                           │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 978.853 USDT                   │
│ Max balance                   │ 2162.416 USDT                  │
│ Max % of account underwater   │ 20.41%                         │
│ Absolute drawdown             │ 441.299 USDT (20.41%)          │
│ Drawdown duration             │ 1198 days 15:00:00             │
│ Profit at drawdown start      │ 1162.416 USDT                  │
│ Profit at drawdown end        │ 721.118 USDT                   │
│ Drawdown start                │ 2022-03-29 00:00:00            │
│ Drawdown end                  │ 2025-07-09 15:00:00            │
│ Market change                 │ 2372.94%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2018-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │   1372 │         0.27 │         952.525 │        95.25 │     16:13:00 │  459     0   913  33.5 │ 441.299 USDT  20.41% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-23T18:29:32.773907",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 3040,
  "total_daily_avg_trades": "1372 / 0.49",
  "absolute_profit_usdt": 952.525,
  "total_profit_pct": 95.25,
  "cagr_pct": 9.08,
  "sortino": 1.42,
  "sharpe": 0.54,
  "calmar": 3.17,
  "sqn": 2.13,
  "max_consecutive_wins_loss": "6 / 23",
  "min_balance_usdt": 978.853,
  "max_balance_usdt": 2162.416,
  "absolute_drawdown_pct": 20.41,
  "market_change_pct": 2372.94,
  "win_draw_loss_winpct": "459 0 913 33.5"
}
```
