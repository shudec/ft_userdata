# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 29 / 0.08, Median: -0.78%, Total profit: -8.51%, Sortino: -0.98, Sharpe: -0.42, Calmar: -4.78, Drawdown: 0%)

---
            
**Strategy:** EMAMACDStrategy  
**Random State:** 8209  
**Timestamp:** 2025-09-16 17:13:14

## Configuration
```json
{
  "strategy": "EMAMACDStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 8209,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy EMAMACDStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 8209
```

## Hyperopt Output
```
2025-09-16 15:11:24,210 - freqtrade - INFO - freqtrade 2025.8
2025-09-16 15:11:24,756 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-16 15:11:26,149 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-16 15:11:26,155 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-16 15:11:26,155 - freqtrade.loggers - INFO - Logfile configured
2025-09-16 15:11:26,156 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-16 15:11:26,156 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-16 15:11:26,157 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-16 15:11:26,157 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-16 15:11:26,538 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-16 15:11:26,540 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-16 15:11:26,541 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-16 15:11:26,541 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 100 epochs ...
2025-09-16 15:11:26,542 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-16 15:11:26,542 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-16 15:11:26,542 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-16 15:11:26,543 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 8209
2025-09-16 15:11:26,543 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-16 15:11:26,543 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-16 15:11:26,543 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-16 15:11:26,544 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-16 15:11:26,545 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-16 15:11:26,562 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-16 15:11:26,562 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 15:11:26,565 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-16 15:11:26,572 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-16 15:11:26,578 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-16 15:11:26,578 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-16 15:11:26,601 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-16 15:11:29,243 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-16 15:11:29,308 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy EMAMACDStrategy from '/freqtrade/user_data/strategies/EMAMACDStrategy.py'...
2025-09-16 15:11:29,310 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2025-09-16 15:11:29,310 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-16 15:11:29,311 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-16 15:11:29,311 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-16 15:11:29,312 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-16 15:11:29,312 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-16 15:11:29,312 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-16 15:11:29,313 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-16 15:11:29,313 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-16 15:11:29,313 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-16 15:11:29,314 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-16 15:11:29,314 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-16 15:11:29,315 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-16 15:11:29,315 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-16 15:11:29,316 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-16 15:11:29,316 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-16 15:11:29,316 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-16 15:11:29,317 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-16 15:11:29,317 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-16 15:11:29,318 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-16 15:11:29,318 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-16 15:11:29,319 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-16 15:11:29,320 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-16 15:11:29,321 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-16 15:11:29,321 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-16 15:11:29,322 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-16 15:11:29,322 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-16 15:11:29,322 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-16 15:11:29,323 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-16 15:11:29,323 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-16 15:11:29,324 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 15:11:29,343 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-16 15:11:29,369 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-16 15:11:29,371 - freqtrade.strategy.hyper - INFO - No params for buy found, using default values.
2025-09-16 15:11:29,371 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): macd_threshold = 0
2025-09-16 15:11:29,372 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): volume_factor = 0.1
2025-09-16 15:11:29,372 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): window_macd_cross = 5
2025-09-16 15:11:29,373 - freqtrade.strategy.hyper - INFO - No params for sell found, using default values.
2025-09-16 15:11:29,373 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): lookback_period_for_stoploss = 5
2025-09-16 15:11:29,374 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): stoploss_margin = 0.999
2025-09-16 15:11:29,374 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): take_profit_multiplier = 2
2025-09-16 15:11:29,375 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_stoploss_param = True
2025-09-16 15:11:29,375 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-16 15:11:29,393 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-16 15:11:29,393 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 8209
2025-09-16 15:11:29,449 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-16 15:11:29,517 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-16 15:11:29,526 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-16 15:11:29,575 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-16 15:11:29,628 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-16 15:11:29,678 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-16 15:11:29,686 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-16 15:11:29,697 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-16 15:11:30,282 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-16 15:11:38,955 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-16 15:11:39,394 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 16 CPU cores. Let's make them scream!
2025-09-16 15:11:39,395 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-16 15:11:39,396 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-16 15:11:39,397] A new study created in memory with name: no-name-e3ff1f5b-c102-4477-b7ac-68796a50cc42
2025-09-16 15:11:39,444 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
2025-09-16 15:12:33,689 - freqtrade.optimize.hyperopt.hyperopt - WARNING - Duplicate params detected. Maybe your search space is too small?
                                                                                           Hyperopt results                                                                                             
                           ┏━━━━━━━━┳━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓                            
                           ┃ Best   ┃ Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                   Profit ┃ Avg duration ┃ Objective ┃     Max Drawdown (Acct) ┃                            
                           ┡━━━━━━━━╇━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩                            
                           │ * Best │ 1/100 │     72 │   13     0    59  18.1 │     -0.47% │ -190.440 USDT  (-19.04%) │     10:59:00 │   0.42675 │ 192.321 USDT   (19.20%) │                            
                           │ * Best │ 2/100 │     72 │   13     0    59  18.1 │     -0.47% │ -199.138 USDT  (-19.91%) │     10:36:00 │   0.36703 │ 201.283 USDT   (20.09%) │                            
                           │ * Best │ 3/100 │     72 │   13     0    59  18.1 │     -0.45% │ -191.640 USDT  (-19.16%) │     10:40:00 │   0.35295 │ 193.702 USDT   (19.33%) │                            
                           └────────┴───────┴────────┴────────────────────────┴────────────┴──────────────────────────┴──────────────┴───────────┴─────────────────────────┘                            
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                    79/100  79% • 0:01:09 • 0:00:16
2025-09-16 15:12:48,916 - freqtrade.optimize.hyperopt.hyperopt - INFO - 21 epochs skipped due to duplicate parameters.
2025-09-16 15:12:48,917 - freqtrade.optimize.hyperopt.hyperopt - INFO - 79 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_EMAMACDStrategy_2025-09-16_15-11-26.fthypt'.
2025-09-16 15:12:49,040 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/EMAMACDStrategy.json

Best result:

*    3/100:     72 trades. 13/0/59 Wins/Draws/Losses. Avg profit  -0.45%. Median profit  -0.78%. Total profit -191.64012303 USDT ( -19.16%). Avg duration 10:40:00 min. Objective: 0.35295

{"params":{"window_macd_cross":4,"macd_threshold":0,"volume_factor":0.1,"stoploss_margin":0.996,"lookback_period_for_stoploss":5,"take_profit_multiplier":2,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy EMAMACDStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20221231
```

## Backtesting Output
```
2025-09-16 15:12:53,328 - freqtrade - INFO - freqtrade 2025.8
2025-09-16 15:12:53,980 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-16 15:12:57,247 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-16 15:12:57,258 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-16 15:12:57,259 - freqtrade.loggers - INFO - Logfile configured
2025-09-16 15:12:57,260 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-16 15:12:57,262 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-16 15:12:57,263 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-16 15:12:57,266 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-16 15:12:57,267 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20221231 ...
2025-09-16 15:12:57,733 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-16 15:12:57,737 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-16 15:12:57,737 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-16 15:12:57,738 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-16 15:12:57,739 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-16 15:12:57,740 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20221231
2025-09-16 15:12:57,743 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-16 15:12:57,765 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-16 15:12:57,767 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 15:12:57,772 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-16 15:12:57,774 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-16 15:12:57,775 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-16 15:12:57,818 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-16 15:13:00,967 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-16 15:13:01,079 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy EMAMACDStrategy from '/freqtrade/user_data/strategies/EMAMACDStrategy.py'...
2025-09-16 15:13:01,083 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/EMAMACDStrategy.json
2025-09-16 15:13:01,090 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-16 15:13:01,091 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-16 15:13:01,092 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-16 15:13:01,093 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-16 15:13:01,094 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-16 15:13:01,094 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-16 15:13:01,095 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-16 15:13:01,096 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-16 15:13:01,097 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-16 15:13:01,098 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-16 15:13:01,099 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-16 15:13:01,099 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-16 15:13:01,100 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-16 15:13:01,102 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-16 15:13:01,103 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-16 15:13:01,104 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-16 15:13:01,105 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-16 15:13:01,107 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-16 15:13:01,108 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-16 15:13:01,110 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-16 15:13:01,111 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-16 15:13:01,112 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-16 15:13:01,113 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-16 15:13:01,114 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-16 15:13:01,115 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-16 15:13:01,116 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-16 15:13:01,117 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-16 15:13:01,118 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-16 15:13:01,119 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 15:13:01,149 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-16 15:13:01,199 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-16 15:13:01,620 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2022-12-31 00:00:00 (364 days).
2025-09-16 15:13:04,179 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-16 15:13:04,200 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy EMAMACDStrategy
2025-09-16 15:13:04,201 - freqtrade.strategy.hyper - INFO - Strategy Parameter: macd_threshold = 0
2025-09-16 15:13:04,202 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.1
2025-09-16 15:13:04,203 - freqtrade.strategy.hyper - INFO - Strategy Parameter: window_macd_cross = 4
2025-09-16 15:13:04,205 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-09-16 15:13:04,206 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.996
2025-09-16 15:13:04,208 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-16 15:13:04,209 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-16 15:13:04,210 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-16 15:13:09,781 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2022-12-31 00:00:00 (364 days).
2025-09-16 15:13:13,300 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-16_15-13-13.meta.json"
Result for strategy EMAMACDStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │      7 │        -0.06 │           7.924 │         0.79 │     10:10:00 │    2     0     5  28.6 │
│ BNB/USDT │     10 │        -0.25 │         -11.534 │        -1.15 │     11:06:00 │    3     0     7  30.0 │
│ LTC/USDT │      3 │        -1.34 │         -18.408 │        -1.84 │     12:40:00 │    1     0     2  33.3 │
│ ETH/USDT │      2 │         -1.3 │         -21.135 │        -2.11 │     13:38:00 │    0     0     2     0 │
│ BTC/USDT │      7 │        -1.49 │         -41.953 │         -4.2 │      5:26:00 │    0     0     7     0 │
│    TOTAL │     29 │        -0.69 │         -85.105 │        -8.51 │      9:51:00 │    6     0    23  20.7 │
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
│     OTHER │      29 │        -0.69 │         -85.105 │        -8.51 │      9:51:00 │    6     0    23  20.7 │
│     TOTAL │      29 │        -0.69 │         -85.105 │        -8.51 │      9:51:00 │    6     0    23  20.7 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │     1 │         4.29 │          41.133 │         4.11 │     10:10:00 │    1     0     0   100 │
│      stop_loss │     1 │        -1.89 │         -18.139 │        -1.81 │      4:15:00 │    0     0     1     0 │
│    exit_signal │    27 │        -0.83 │        -108.100 │       -10.81 │     10:02:00 │    5     0    22  18.5 │
│          TOTAL │    29 │        -0.69 │         -85.105 │        -8.51 │      9:51:00 │    6     0    23  20.7 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │      1 │         4.29 │          41.133 │         4.11 │     10:10:00 │    1     0     0   100 │
│           │      stop_loss │      1 │        -1.89 │         -18.139 │        -1.81 │      4:15:00 │    0     0     1     0 │
│           │    exit_signal │     27 │        -0.83 │        -108.100 │       -10.81 │     10:02:00 │    5     0    22  18.5 │
│     TOTAL │                │     29 │        -0.69 │         -85.105 │        -8.51 │      9:51:00 │    6     0    23  20.7 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2022-12-31 00:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 29 / 0.08                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 914.895 USDT                   │
│ Absolute profit               │ -85.105 USDT                   │
│ Total profit %                │ -8.51%                         │
│ CAGR %                        │ -8.53%                         │
│ Sortino                       │ -0.98                          │
│ Sharpe                        │ -0.42                          │
│ Calmar                        │ -4.78                          │
│ SQN                           │ -1.44                          │
│ Profit factor                 │ 0.48                           │
│ Expectancy (Ratio)            │ -2.93 (-0.42)                  │
│ Avg. daily profit             │ -0.234 USDT                    │
│ Avg. stake amount             │ 748.475 USDT                   │
│ Total trade volume            │ 43413.176 USDT                 │
│                               │                                │
│ Best Pair                     │ XRP/USDT 0.79%                 │
│ Worst Pair                    │ BTC/USDT -4.20%                │
│ Best trade                    │ XRP/USDT 4.29%                 │
│ Worst trade                   │ BTC/USDT -5.12%                │
│ Best day                      │ 41.133 USDT                    │
│ Worst day                     │ -18.139 USDT                   │
│ Days win/draw/lose            │ 6 / 324 / 22                   │
│ Min/Max/Avg. Duration Winners │ 0d 10:10 / 1d 09:00 / 0d 22:22 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 0d 23:00 / 0d 06:35 │
│ Max Consecutive Wins / Loss   │ 1 / 8                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 914.895 USDT                   │
│ Max balance                   │ 1009.145 USDT                  │
│ Max % of account underwater   │ 9.34%                          │
│ Absolute drawdown             │ 94.25 USDT (9.34%)             │
│ Drawdown duration             │ 280 days 11:50:00              │
│ Profit at drawdown start      │ 9.145 USDT                     │
│ Profit at drawdown end        │ -85.105 USDT                   │
│ Drawdown start                │ 2022-03-21 20:10:00            │
│ Drawdown end                  │ 2022-12-27 08:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                            STRATEGY SUMMARY                                                            
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃        Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃          Drawdown ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ EMAMACDStrategy │     29 │        -0.69 │         -85.105 │        -8.51 │      9:51:00 │    6     0    23  20.7 │ 94.25 USDT  9.34% │
└─────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴───────────────────┘

```
