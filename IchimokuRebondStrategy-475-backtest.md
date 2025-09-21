# Freqtrade Backtest Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 475  
**Timestamp:** 2025-09-20 22:28:03

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell buy roi",
  "random_state": 475,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20201231",
  "backtest_timerange": "20221101-20241231"
}
```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20221101-20241231
```

## Backtesting Output
```
2025-09-20 20:27:46,788 - freqtrade - INFO - freqtrade 2025.7
2025-09-20 20:27:47,126 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-20 20:27:47,127 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-20 20:27:48,695 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-20 20:27:48,698 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-20 20:27:48,698 - freqtrade.loggers - INFO - Logfile configured
2025-09-20 20:27:48,699 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-20 20:27:48,699 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-20 20:27:48,699 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-20 20:27:48,700 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-20 20:27:48,700 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20221101-20241231 ...
2025-09-20 20:27:48,708 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-20 20:27:48,709 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-20 20:27:48,710 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-20 20:27:48,710 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-20 20:27:48,710 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-20 20:27:48,711 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20221101-20241231
2025-09-20 20:27:48,712 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-20 20:27:48,731 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-20 20:27:48,732 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-20 20:27:48,736 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-20 20:27:48,737 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-20 20:27:48,738 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-20 20:27:48,772 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-20 20:27:51,055 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-20 20:27:51,098 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-20 20:27:51,099 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-20 20:27:51,101 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-20 20:27:51,102 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-20 20:27:51,102 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-20 20:27:51,103 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-20 20:27:51,103 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-20 20:27:51,104 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.49, '456': 0.214, '795': 0.085, '1564': 0}
2025-09-20 20:27:51,104 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-20 20:27:51,105 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-20 20:27:51,105 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-20 20:27:51,106 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-20 20:27:51,106 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-20 20:27:51,107 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-20 20:27:51,107 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-20 20:27:51,107 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-20 20:27:51,108 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-20 20:27:51,108 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-20 20:27:51,109 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-20 20:27:51,109 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-20 20:27:51,110 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-20 20:27:51,110 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-20 20:27:51,110 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-20 20:27:51,111 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-20 20:27:51,111 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-20 20:27:51,112 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-20 20:27:51,112 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-20 20:27:51,112 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-20 20:27:51,113 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-20 20:27:51,113 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-20 20:27:51,114 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-20 20:27:51,119 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-20 20:27:51,156 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-20 20:27:51,345 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-11-01 00:00:00 up to 2024-12-31 00:00:00 (791 days).
2025-09-20 20:27:52,905 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-20 20:27:52,907 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-20 20:27:52,908 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-20 20:27:52,908 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.1
2025-09-20 20:27:52,909 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 16
2025-09-20 20:27:52,909 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.523
2025-09-20 20:27:52,909 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.85
2025-09-20 20:27:52,910 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.022
2025-09-20 20:27:52,910 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.0
2025-09-20 20:27:52,910 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.001
2025-09-20 20:27:52,911 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-20 20:27:52,911 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 6
2025-09-20 20:27:52,911 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.992
2025-09-20 20:27:52,912 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-20 20:27:52,912 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-20 20:27:52,912 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-20 20:27:52,912 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-20 20:27:52,914 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-11-01 00:00:00 to 2024-12-31 00:00:00
2025-09-20 20:27:54,541 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-11-01 00:00:00 to 2024-12-31 00:00:00
2025-09-20 20:27:56,129 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-11-01 00:00:00 to 2024-12-31 00:00:00
2025-09-20 20:27:57,751 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-11-01 00:00:00 to 2024-12-31 00:00:00
2025-09-20 20:27:59,429 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-11-01 00:00:00 to 2024-12-31 00:00:00
2025-09-20 20:28:00,968 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-11-01 00:00:00 up to 2024-12-31 00:00:00 (791 days).
2025-09-20 20:28:02,762 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-20_20-28-02.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
│ ETH/USDT │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
│ LTC/USDT │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
│ XRP/USDT │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
│ BNB/USDT │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
│    TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                ENTER TAG STATS                                                
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     TOTAL │       0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                               EXIT REASON STATS                                               
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│       TOTAL │     0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                      MIXED TAG STATS                                                       
┏━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     TOTAL │             │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────────┴─────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
No trades made. Your starting balance was 1000 USDT, and your stake was unlimited.

Backtested 2022-11-01 00:00:00 -> 2024-12-31 00:00:00 | Max open trades : 3
                                                             STRATEGY SUMMARY                                                              
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃      Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │      0 │         0.00 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │ 0 USDT  0.00% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴───────────────┘

```

## Backtest Results
```json
{
  "timestamp": "2025-09-20T22:28:03.789382",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 475,
  "win_draw_loss_winpct": "0 0 0 0"
}
```
