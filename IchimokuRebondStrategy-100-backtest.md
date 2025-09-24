# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 100  
**Timestamp:** 2025-09-24 13:12:41

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "roi",
  "random_state": 100,
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
2025-09-24 11:06:33,892 - freqtrade - INFO - freqtrade 2025.8
2025-09-24 11:06:34,233 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-24 11:06:36,144 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-24 11:06:36,150 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-24 11:06:36,150 - freqtrade.loggers - INFO - Logfile configured
2025-09-24 11:06:36,151 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-24 11:06:36,152 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-24 11:06:36,152 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-24 11:06:36,153 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-24 11:06:36,154 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20200101-20251231 ...
2025-09-24 11:06:36,692 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-24 11:06:36,695 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-24 11:06:36,695 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-24 11:06:36,696 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-24 11:06:36,696 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-24 11:06:36,697 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20200101-20251231
2025-09-24 11:06:36,698 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-24 11:06:36,713 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-24 11:06:36,714 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 11:06:36,718 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-24 11:06:36,720 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-24 11:06:36,721 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-24 11:06:36,744 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-24 11:06:41,138 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-24 11:06:41,233 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-24 11:06:41,236 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-24 11:06:41,241 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-24 11:06:41,241 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-24 11:06:41,241 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-24 11:06:41,242 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-24 11:06:41,242 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-24 11:06:41,243 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-24 11:06:41,243 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-24 11:06:41,243 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-24 11:06:41,244 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-24 11:06:41,244 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-24 11:06:41,245 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-24 11:06:41,245 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-24 11:06:41,246 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-24 11:06:41,247 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-24 11:06:41,247 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-24 11:06:41,248 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-24 11:06:41,248 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-24 11:06:41,249 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-24 11:06:41,249 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-24 11:06:41,250 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-24 11:06:41,250 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-24 11:06:41,250 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-24 11:06:41,251 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-24 11:06:41,252 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-24 11:06:41,253 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-24 11:06:41,253 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-24 11:06:41,253 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-24 11:06:41,254 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-24 11:06:41,254 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-24 11:06:41,272 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-24 11:06:41,296 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-24 11:06:41,353 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 11:06:41,456 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 11:06:41,536 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 11:06:41,634 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 11:06:41,716 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-24 11:06:41,765 - freqtrade.optimize.backtesting - INFO - Loading data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 11:06:42,065 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 11:06:42,560 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 11:06:43,084 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 11:06:43,573 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 11:06:44,138 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-24 11:06:46,176 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-24 11:06:46,180 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-24 11:06:46,181 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-24 11:06:46,181 - freqtrade.strategy.hyper - INFO - Strategy Parameter: bullish_engulfing_upper_wick_threshold = 0.156
2025-09-24 11:06:46,182 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-24 11:06:46,182 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_chiku = False
2025-09-24 11:06:46,183 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-24 11:06:46,183 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 6
2025-09-24 11:06:46,184 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.951
2025-09-24 11:06:46,184 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.899
2025-09-24 11:06:46,184 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-24 11:06:46,185 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.002
2025-09-24 11:06:46,185 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 70
2025-09-24 11:06:46,185 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 10
2025-09-24 11:06:46,186 - freqtrade.strategy.hyper - INFO - Strategy Parameter: strong_bullish_upper_wick_threshold = 0.433
2025-09-24 11:06:46,186 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.002
2025-09-24 11:06:46,187 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.5
2025-09-24 11:06:46,187 - freqtrade.strategy.hyper - INFO - Strategy Parameter: atr_stoploss_multiplier = 3
2025-09-24 11:06:46,188 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): custom_sell_atr_factor = 4.5
2025-09-24 11:06:46,188 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-24 11:06:46,189 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 8
2025-09-24 11:06:46,189 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.993
2025-09-24 11:06:46,189 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-24 11:06:46,190 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-24 11:06:46,191 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_type = lower_and_atr
2025-09-24 11:06:46,191 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-24 11:06:46,192 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-24 11:06:46,196 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 11:06:46,212 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 11:06:46,230 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 11:06:46,258 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 11:07:04,721 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 11:07:04,739 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 11:07:04,758 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 11:07:04,786 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 11:07:20,476 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 11:07:20,491 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 11:07:20,507 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 11:07:20,533 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 4h, data ends at 2025-09-15 00:00:00
2025-09-24 11:07:35,814 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 11:07:35,829 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 11:07:35,844 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 11:07:35,865 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 11:07:52,196 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 11:07:52,212 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-24 11:07:52,229 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 4h from 2020-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-24 11:07:52,255 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 4h, data ends at 2025-09-23 12:00:00
2025-09-24 11:08:09,669 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2020-01-01 00:00:00 up to 2025-09-10 08:00:00 (2079 days).
2025-09-24 11:12:39,880 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-24_11-12-39.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │    100 │         1.88 │         836.967 │         83.7 │ 2 days, 18:28:00 │   45     0    55  45.0 │
│ BTC/USDT │    112 │         0.69 │         448.614 │        44.86 │ 2 days, 17:41:00 │   48     0    64  42.9 │
│ XRP/USDT │     63 │         1.26 │         318.167 │        31.82 │  2 days, 5:46:00 │   14     0    49  22.2 │
│ BNB/USDT │     83 │         1.13 │         193.499 │        19.35 │ 2 days, 10:44:00 │   31     0    52  37.3 │
│ LTC/USDT │     65 │        -0.51 │           5.876 │         0.59 │  2 days, 4:08:00 │   22     0    43  33.8 │
│    TOTAL │    423 │         0.96 │        1803.124 │       180.31 │ 2 days, 12:39:00 │  160     0   263  37.8 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         2.14 │          29.389 │         2.94 │ 3 days, 17:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         2.14 │          29.389 │         2.94 │ 3 days, 17:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                        ENTER TAG STATS                                                        
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │     313 │         1.21 │        1555.736 │       155.57 │ 2 days, 13:03:00 │  119     0   194  38.0 │
│         hammer_rebond │      61 │         1.13 │         333.230 │        33.32 │ 2 days, 11:29:00 │   25     0    36  41.0 │
│      engulfing_rebond │      49 │        -0.84 │         -85.842 │        -8.58 │ 2 days, 11:33:00 │   16     0    33  32.7 │
│                 TOTAL │     423 │         0.96 │        1803.124 │       180.31 │ 2 days, 12:39:00 │  160     0   263  37.8 │
└───────────────────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │    41 │        17.39 │        3683.023 │        368.3 │ 3 days, 14:51:00 │   41     0     0   100 │
│     force_exit │     1 │         2.14 │          29.389 │         2.94 │ 3 days, 17:00:00 │    1     0     0   100 │
│    exit_signal │   349 │        -0.37 │        -891.098 │       -89.11 │ 2 days, 13:44:00 │  118     0   231  33.8 │
│      stop_loss │    32 │        -5.65 │       -1018.190 │      -101.82 │         14:27:00 │    0     0    32     0 │
│          TOTAL │   423 │         0.96 │        1803.124 │       180.31 │ 2 days, 12:39:00 │  160     0   263  37.8 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                                MIXED TAG STATS                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ strong_bullish_rebond │ take_profit_3R │     33 │        17.72 │        2974.089 │       297.41 │ 3 days, 13:59:00 │   33     0     0   100 │
│         hammer_rebond │ take_profit_3R │      6 │         17.5 │         552.597 │        55.26 │ 3 days, 11:12:00 │    6     0     0   100 │
│      engulfing_rebond │ take_profit_3R │      2 │        11.61 │         156.336 │        15.63 │ 4 days, 16:00:00 │    2     0     0   100 │
│      engulfing_rebond │     force_exit │      1 │         2.14 │          29.389 │         2.94 │ 3 days, 17:00:00 │    1     0     0   100 │
│         hammer_rebond │    exit_signal │     49 │         0.04 │         -56.397 │        -5.64 │ 2 days, 14:11:00 │   19     0    30  38.8 │
│      engulfing_rebond │      stop_loss │      3 │        -6.83 │        -102.575 │       -10.26 │         12:57:00 │    0     0     3     0 │
│         hammer_rebond │      stop_loss │      6 │        -6.32 │        -162.970 │        -16.3 │         13:43:00 │    0     0     6     0 │
│      engulfing_rebond │    exit_signal │     43 │        -1.07 │        -168.992 │        -16.9 │ 2 days, 11:40:00 │   13     0    30  30.2 │
│ strong_bullish_rebond │    exit_signal │    257 │        -0.33 │        -665.709 │       -66.57 │ 2 days, 13:59:00 │   86     0   171  33.5 │
│ strong_bullish_rebond │      stop_loss │     23 │        -5.33 │        -752.645 │       -75.26 │         14:50:00 │    0     0    23     0 │
│                 TOTAL │                │    423 │         0.96 │        1803.124 │       180.31 │ 2 days, 12:39:00 │  160     0   263  37.8 │
└───────────────────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2020-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 423 / 0.2                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 2803.124 USDT                  │
│ Absolute profit               │ 1803.124 USDT                  │
│ Total profit %                │ 180.31%                        │
│ CAGR %                        │ 19.84%                         │
│ Sortino                       │ 1.45                           │
│ Sharpe                        │ 0.46                           │
│ Calmar                        │ 12.99                          │
│ SQN                           │ 2.41                           │
│ Profit factor                 │ 1.44                           │
│ Expectancy (Ratio)            │ 4.26 (0.27)                    │
│ Avg. daily profit             │ 0.867 USDT                     │
│ Avg. stake amount             │ 563.755 USDT                   │
│ Total trade volume            │ 479697.976 USDT                │
│                               │                                │
│ Best Pair                     │ ETH/USDT 83.70%                │
│ Worst Pair                    │ LTC/USDT 0.59%                 │
│ Best trade                    │ BNB/USDT 65.35%                │
│ Worst trade                   │ BNB/USDT -11.20%               │
│ Best day                      │ 286.221 USDT                   │
│ Worst day                     │ -67.367 USDT                   │
│ Days win/draw/lose            │ 127 / 1721 / 192               │
│ Min/Max/Avg. Duration Winners │ 1d 07:00 / 9d 20:25 / 3d 23:22 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 4d 10:00 / 1d 15:32 │
│ Max Consecutive Wins / Loss   │ 6 / 13                         │
│ Rejected Entry signals        │ 744                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 929.679 USDT                   │
│ Max balance                   │ 2913.882 USDT                  │
│ Max % of account underwater   │ 14.96%                         │
│ Absolute drawdown             │ 336.62 USDT (12.75%)           │
│ Drawdown duration             │ 143 days 07:10:00              │
│ Profit at drawdown start      │ 1639.389 USDT                  │
│ Profit at drawdown end        │ 1302.769 USDT                  │
│ Drawdown start                │ 2024-12-02 00:50:00            │
│ Drawdown end                  │ 2025-04-24 08:00:00            │
│ Market change                 │ 2537.81%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2020-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃            Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │    423 │         0.96 │        1803.124 │       180.31 │ 2 days, 12:39:00 │  160     0   263  37.8 │ 336.62 USDT  12.75% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┴─────────────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-24T13:12:41.757268",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 100,
  "total_daily_avg_trades": "423 / 0.2",
  "absolute_profit_usdt": 1803.124,
  "total_profit_pct": 180.31,
  "cagr_pct": 19.84,
  "sortino": 1.45,
  "sharpe": 0.46,
  "calmar": 12.99,
  "sqn": 2.41,
  "max_consecutive_wins_loss": "6 / 13",
  "min_balance_usdt": 929.679,
  "max_balance_usdt": 2913.882,
  "absolute_drawdown_pct": 12.75,
  "market_change_pct": 2537.81
}
```
