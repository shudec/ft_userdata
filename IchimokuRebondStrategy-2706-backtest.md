# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 2706  
**Timestamp:** 2025-09-24 08:40:12

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 2706,
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
2025-09-24 06:32:11,874 - freqtrade - INFO - freqtrade 2025.8
2025-09-24 06:32:12,652 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-24 06:32:15,568 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-24 06:32:15,575 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-24 06:32:15,576 - freqtrade.loggers - INFO - Logfile configured
2025-09-24 06:32:15,576 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-24 06:32:15,577 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-24 06:32:15,577 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-24 06:32:15,578 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-24 06:32:15,579 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20200101-20251231 ...
2025-09-24 06:32:16,106 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-24 06:32:16,108 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-24 06:32:16,109 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-24 06:32:16,109 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-24 06:32:16,109 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-24 06:32:16,110 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20200101-20251231
2025-09-24 06:32:16,111 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-24 06:32:16,124 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-24 06:32:16,125 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 06:32:16,128 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-24 06:32:16,129 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-24 06:32:16,130 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-24 06:32:16,157 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-24 06:32:18,951 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-24 06:32:19,146 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-24 06:32:19,153 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-24 06:32:19,162 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-24 06:32:19,163 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-24 06:32:19,164 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-24 06:32:19,165 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-24 06:32:19,166 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-24 06:32:19,167 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-24 06:32:19,168 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-24 06:32:19,171 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-24 06:32:19,173 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-24 06:32:19,178 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-24 06:32:19,179 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-24 06:32:19,180 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-24 06:32:19,181 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-24 06:32:19,182 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-24 06:32:19,183 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-24 06:32:19,184 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-24 06:32:19,185 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-24 06:32:19,186 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-24 06:32:19,186 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-24 06:32:19,188 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-24 06:32:19,191 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-24 06:32:19,194 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-24 06:32:19,197 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-24 06:32:19,197 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-24 06:32:19,198 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-24 06:32:19,199 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-24 06:32:19,200 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-24 06:32:19,201 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-24 06:32:19,202 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 06:32:19,257 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-24 06:32:19,304 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-24 06:32:19,504 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 06:32:19,698 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 06:32:19,883 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 06:32:20,030 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 06:32:20,172 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 06:32:20,227 - freqtrade.optimize.backtesting - INFO - Loading data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 06:32:20,680 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 06:32:21,501 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 06:32:22,235 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 06:32:22,916 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 06:32:23,574 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 06:32:25,703 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-24 06:32:25,711 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-24 06:32:25,712 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-24 06:32:25,712 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-24 06:32:25,713 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-24 06:32:25,713 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-24 06:32:25,714 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-24 06:32:25,715 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-24 06:32:25,716 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-24 06:32:25,717 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-24 06:32:25,717 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-24 06:32:25,718 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-24 06:32:25,719 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-09-24 06:32:25,719 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-09-24 06:32:25,720 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-24 06:32:25,721 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-24 06:32:25,721 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-24 06:32:25,722 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-24 06:32:25,723 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-24 06:32:25,723 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 8
2025-09-24 06:32:25,724 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-24 06:32:25,724 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-24 06:32:25,724 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-24 06:32:25,725 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-24 06:32:25,725 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-24 06:32:25,726 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-24 06:32:25,729 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 06:32:25,750 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 06:32:25,775 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 06:32:25,811 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 06:32:44,779 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 06:32:44,799 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 06:32:44,814 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 06:32:44,842 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 06:33:03,028 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 06:33:03,050 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 06:33:03,066 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 06:33:03,095 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-15 00:00:00
2025-09-24 06:33:19,930 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 06:33:19,950 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 06:33:19,967 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 06:33:19,999 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 06:33:38,294 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 06:33:38,316 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 06:33:38,344 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 06:33:38,382 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 06:33:55,779 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 06:40:11,157 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-24_06-40-11.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │    194 │         0.76 │         571.809 │        57.18 │ 1 day, 16:01:00 │   85     0   109  43.8 │
│ BTC/USDT │    219 │         0.31 │         281.429 │        28.14 │ 1 day, 18:33:00 │   90     0   129  41.1 │
│ BNB/USDT │    189 │         0.57 │         199.832 │        19.98 │ 1 day, 14:19:00 │   72     0   117  38.1 │
│ XRP/USDT │    136 │         0.26 │         198.310 │        19.83 │ 1 day, 10:46:00 │   44     0    92  32.4 │
│ LTC/USDT │    134 │         0.12 │         -15.248 │        -1.52 │ 1 day, 12:28:00 │   48     0    86  35.8 │
│    TOTAL │    872 │         0.43 │        1236.131 │       123.61 │ 1 day, 14:55:00 │  339     0   533  38.9 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                            LEFT OPEN TRADES REPORT                                            
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         0.07 │           0.798 │         0.08 │ 1 day, 1:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         0.07 │           0.798 │         0.08 │ 1 day, 1:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                       ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │     688 │         0.43 │         917.350 │        91.74 │ 1 day, 14:56:00 │  268     0   420  39.0 │
│         hammer_rebond │      97 │         0.54 │         168.858 │        16.89 │ 1 day, 13:13:00 │   38     0    59  39.2 │
│      engulfing_rebond │      87 │         0.32 │         149.923 │        14.99 │ 1 day, 16:43:00 │   33     0    54  37.9 │
│                 TOTAL │     872 │         0.43 │        1236.131 │       123.61 │ 1 day, 14:55:00 │  339     0   533  38.9 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │   278 │         6.46 │        9622.171 │       962.22 │ 1 day, 12:48:00 │  278     0     0   100 │
│     force_exit │     1 │         0.07 │           0.798 │         0.08 │  1 day, 1:00:00 │    1     0     0   100 │
│      stop_loss │    40 │        -5.77 │       -1374.659 │      -137.47 │        17:34:00 │    0     0    40     0 │
│    exit_signal │   553 │        -2.16 │       -7012.179 │      -701.22 │ 1 day, 17:34:00 │   60     0   493  10.8 │
│          TOTAL │   872 │         0.43 │        1236.131 │       123.61 │ 1 day, 14:55:00 │  339     0   533  38.9 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                               MIXED TAG STATS                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_1R │    220 │         6.45 │        7620.176 │       762.02 │ 1 day, 13:08:00 │  220     0     0   100 │
│         hammer_rebond │ take_profit_1R │     31 │         6.56 │        1069.312 │       106.93 │  1 day, 8:09:00 │   31     0     0   100 │
│      engulfing_rebond │ take_profit_1R │     27 │         6.42 │         932.683 │        93.27 │ 1 day, 15:22:00 │   27     0     0   100 │
│ strong_bullish_rebond │     force_exit │      1 │         0.07 │           0.798 │         0.08 │  1 day, 1:00:00 │    1     0     0   100 │
│      engulfing_rebond │      stop_loss │      2 │        -7.88 │         -73.392 │        -7.34 │  1 day, 9:28:00 │    0     0     2     0 │
│         hammer_rebond │      stop_loss │      6 │        -6.32 │        -201.521 │       -20.15 │        12:08:00 │    0     0     6     0 │
│         hammer_rebond │    exit_signal │     60 │        -1.89 │        -698.933 │       -69.89 │ 1 day, 18:21:00 │    7     0    53  11.7 │
│      engulfing_rebond │    exit_signal │     58 │        -2.23 │        -709.368 │       -70.94 │ 1 day, 17:36:00 │    6     0    52  10.3 │
│ strong_bullish_rebond │      stop_loss │     32 │        -5.53 │       -1099.745 │      -109.97 │        17:36:00 │    0     0    32     0 │
│ strong_bullish_rebond │    exit_signal │    435 │        -2.18 │       -5603.878 │      -560.39 │ 1 day, 17:27:00 │   47     0   388  10.8 │
│                 TOTAL │                │    872 │         0.43 │        1236.131 │       123.61 │ 1 day, 14:55:00 │  339     0   533  38.9 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2020-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 872 / 0.42                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 2236.131 USDT                  │
│ Absolute profit               │ 1236.131 USDT                  │
│ Total profit %                │ 123.61%                        │
│ CAGR %                        │ 15.18%                         │
│ Sortino                       │ 1.05                           │
│ Sharpe                        │ 0.44                           │
│ Calmar                        │ 4.13                           │
│ SQN                           │ 1.61                           │
│ Profit factor                 │ 1.14                           │
│ Expectancy (Ratio)            │ 1.42 (0.09)                    │
│ Avg. daily profit             │ 0.595 USDT                     │
│ Avg. stake amount             │ 633.22 USDT                    │
│ Total trade volume            │ 1107784.943 USDT               │
│                               │                                │
│ Best Pair                     │ ETH/USDT 57.18%                │
│ Worst Pair                    │ LTC/USDT -1.52%                │
│ Best trade                    │ XRP/USDT 20.23%                │
│ Worst trade                   │ LTC/USDT -11.67%               │
│ Best day                      │ 164.493 USDT                   │
│ Worst day                     │ -107.255 USDT                  │
│ Days win/draw/lose            │ 236 / 1460 / 344               │
│ Min/Max/Avg. Duration Winners │ 0d 00:50 / 6d 21:00 / 1d 22:00 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 4d 07:00 / 1d 10:26 │
│ Max Consecutive Wins / Loss   │ 10 / 16                        │
│ Rejected Entry signals        │ 1525                           │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 856.982 USDT                   │
│ Max balance                   │ 2583.316 USDT                  │
│ Max % of account underwater   │ 27.51%                         │
│ Absolute drawdown             │ 674.733 USDT (27.51%)          │
│ Drawdown duration             │ 256 days 08:10:00              │
│ Profit at drawdown start      │ 1452.881 USDT                  │
│ Profit at drawdown end        │ 778.148 USDT                   │
│ Drawdown start                │ 2023-01-14 06:50:00            │
│ Drawdown end                  │ 2023-09-27 15:00:00            │
│ Market change                 │ 2537.81%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2020-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    872 │         0.43 │        1236.131 │       123.61 │ 1 day, 14:55:00 │  339     0   533  38.9 │ 674.733 USDT  27.51% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴──────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-24T08:40:12.879967",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 2706,
  "total_daily_avg_trades": "872 / 0.42",
  "absolute_profit_usdt": 1236.131,
  "total_profit_pct": 123.61,
  "cagr_pct": 15.18,
  "sortino": 1.05,
  "sharpe": 0.44,
  "calmar": 4.13,
  "sqn": 1.61,
  "max_consecutive_wins_loss": "10 / 16",
  "min_balance_usdt": 856.982,
  "max_balance_usdt": 2583.316,
  "absolute_drawdown_pct": 27.51,
  "market_change_pct": 2537.81
}
```
