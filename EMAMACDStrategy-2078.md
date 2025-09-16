# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 115 / 0.09, Median: -0.74%, Total profit: -19.11%, Sortino: -0.79, Sharpe: -0.32, Calmar: -1.31, Drawdown: 20.66%)

---
            
**Strategy:** EMAMACDStrategy  
**Random State:** 2078  
**Timestamp:** 2025-09-16 21:25:22

## Configuration
```json
{
  "strategy": "EMAMACDStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell buy",
  "random_state": 2078,
  "epochs": 200,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy EMAMACDStrategy --timeframe 1h --epochs 200 --spaces sell buy --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 2078
```

## Hyperopt Output
```
2025-09-16 19:23:09,040 - freqtrade - INFO - freqtrade 2025.7
2025-09-16 19:23:09,656 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-16 19:23:09,656 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-16 19:23:11,286 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-16 19:23:11,290 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-16 19:23:11,291 - freqtrade.loggers - INFO - Logfile configured
2025-09-16 19:23:11,292 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-16 19:23:11,293 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-16 19:23:11,293 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-16 19:23:11,294 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-16 19:23:11,304 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-16 19:23:11,305 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-16 19:23:11,305 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-16 19:23:11,306 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 200 epochs ...
2025-09-16 19:23:11,306 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['sell', 'buy']
2025-09-16 19:23:11,307 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-16 19:23:11,307 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-16 19:23:11,307 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 2078
2025-09-16 19:23:11,308 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-16 19:23:11,308 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-16 19:23:11,309 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-16 19:23:11,309 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-16 19:23:11,311 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-16 19:23:11,331 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-16 19:23:11,332 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 19:23:11,336 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-16 19:23:11,337 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-16 19:23:11,342 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-16 19:23:11,343 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-16 19:23:11,380 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-16 19:23:13,940 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-16 19:23:13,971 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy EMAMACDStrategy from '/freqtrade/user_data/strategies/EMAMACDStrategy.py'...
2025-09-16 19:23:13,972 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2025-09-16 19:23:13,973 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-16 19:23:13,973 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-16 19:23:13,974 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-16 19:23:13,974 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-16 19:23:13,975 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-16 19:23:13,975 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-16 19:23:13,976 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-16 19:23:13,976 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-16 19:23:13,977 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-16 19:23:13,977 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-16 19:23:13,978 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-16 19:23:13,978 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-16 19:23:13,978 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-16 19:23:13,979 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-16 19:23:13,979 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-16 19:23:13,980 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-16 19:23:13,980 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-16 19:23:13,980 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-16 19:23:13,981 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-16 19:23:13,981 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-16 19:23:13,982 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-16 19:23:13,982 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-16 19:23:13,982 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-16 19:23:13,983 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-16 19:23:13,983 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-16 19:23:13,984 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-16 19:23:13,984 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-16 19:23:13,984 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-16 19:23:13,985 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-16 19:23:13,985 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 19:23:13,991 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-16 19:23:14,027 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-16 19:23:14,029 - freqtrade.strategy.hyper - INFO - No params for buy found, using default values.
2025-09-16 19:23:14,030 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): macd_threshold = 0
2025-09-16 19:23:14,031 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): volume_factor = 0.1
2025-09-16 19:23:14,031 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): window_macd_cross = 5
2025-09-16 19:23:14,032 - freqtrade.strategy.hyper - INFO - No params for sell found, using default values.
2025-09-16 19:23:14,032 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): lookback_period_for_stoploss = 5
2025-09-16 19:23:14,033 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): stoploss_margin = 0.999
2025-09-16 19:23:14,033 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): take_profit_multiplier = 2
2025-09-16 19:23:14,034 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_stoploss_param = True
2025-09-16 19:23:14,034 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-16 19:23:14,044 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-16 19:23:14,045 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 2078
2025-09-16 19:23:14,079 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-16 19:23:14,131 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-16 19:23:14,139 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-16 19:23:14,172 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-16 19:23:14,215 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-16 19:23:14,257 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-16 19:23:14,266 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-16 19:23:14,284 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-16 19:23:15,117 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-16 19:23:23,683 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-16 19:23:23,974 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 20 CPU cores. Let's make them scream!
2025-09-16 19:23:23,975 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-16 19:23:23,976 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-16 19:23:23,977] A new study created in memory with name: no-name-ce2dc9c2-30b2-43cf-b606-5e8cd5b24b08
2025-09-16 19:23:24,030 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
2025-09-16 19:23:50,318 - freqtrade.optimize.hyperopt.hyperopt - WARNING - Duplicate params detected. Maybe your search space is too small?
                                                                                            Hyperopt results                                                                                            
                           ┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓                           
                           ┃ Best   ┃  Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                   Profit ┃ Avg duration ┃ Objective ┃     Max Drawdown (Acct) ┃                           
                           ┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩                           
                           │ * Best │  1/200 │     72 │   14     0    58  19.4 │     -0.54% │ -224.022 USDT  (-22.40%) │      8:39:00 │   0.52397 │ 224.022 USDT   (22.40%) │                           
                           │ * Best │  2/200 │     72 │   14     0    58  19.4 │     -0.51% │ -201.725 USDT  (-20.17%) │      8:49:00 │   0.50159 │ 201.725 USDT   (20.17%) │                           
                           │ * Best │  4/200 │     72 │   14     0    58  19.4 │     -0.52% │ -220.822 USDT  (-22.08%) │      8:37:00 │   0.47748 │ 222.075 USDT   (22.21%) │                           
                           │ * Best │ 14/200 │     72 │   14     0    58  19.4 │     -0.48% │ -185.815 USDT  (-18.58%) │      8:51:00 │   0.47324 │ 185.815 USDT   (18.58%) │                           
                           │ * Best │ 20/200 │     72 │   14     0    58  19.4 │     -0.48% │ -187.783 USDT  (-18.78%) │      8:51:00 │   0.46713 │ 187.783 USDT   (18.78%) │                           
                           └────────┴────────┴────────┴────────────────────────┴────────────┴──────────────────────────┴──────────────┴───────────┴─────────────────────────┘                           
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸                                                                                        92/200  46% • 0:01:20 • 0:01:40
2025-09-16 19:24:44,917 - freqtrade.optimize.hyperopt.hyperopt - INFO - 108 epochs skipped due to duplicate parameters.
2025-09-16 19:24:44,917 - freqtrade.optimize.hyperopt.hyperopt - INFO - 92 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_EMAMACDStrategy_2025-09-16_19-23-11.fthypt'.
2025-09-16 19:24:44,948 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/EMAMACDStrategy.json

Best result:

*   20/200:     72 trades. 14/0/58 Wins/Draws/Losses. Avg profit  -0.48%. Median profit  -0.74%. Total profit -187.78347927 USDT ( -18.78%). Avg duration 8:51:00 min. Objective: 0.46713

{"params":{"window_macd_cross":4,"macd_threshold":0,"volume_factor":0.1,"stoploss_margin":0.991,"lookback_period_for_stoploss":5,"take_profit_multiplier":2,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy EMAMACDStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231
```

## Backtesting Output
```
2025-09-16 19:24:48,147 - freqtrade - INFO - freqtrade 2025.7
2025-09-16 19:24:48,560 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-16 19:24:48,561 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-16 19:24:50,696 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-16 19:24:50,699 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-16 19:24:50,700 - freqtrade.loggers - INFO - Logfile configured
2025-09-16 19:24:50,700 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-16 19:24:50,701 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-16 19:24:50,701 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-16 19:24:50,702 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-16 19:24:50,702 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-16 19:24:50,710 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-16 19:24:50,711 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-16 19:24:50,712 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-16 19:24:50,712 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-16 19:24:50,713 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-16 19:24:50,714 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-16 19:24:50,716 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-16 19:24:50,736 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-16 19:24:50,737 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 19:24:50,742 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-16 19:24:50,743 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-16 19:24:50,744 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-16 19:24:50,783 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-16 19:24:53,090 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-16 19:24:53,126 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy EMAMACDStrategy from '/freqtrade/user_data/strategies/EMAMACDStrategy.py'...
2025-09-16 19:24:53,127 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/EMAMACDStrategy.json
2025-09-16 19:24:53,128 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-16 19:24:53,128 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-16 19:24:53,129 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-16 19:24:53,129 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-16 19:24:53,130 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-16 19:24:53,130 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-16 19:24:53,130 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-16 19:24:53,131 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-16 19:24:53,131 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-16 19:24:53,131 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-16 19:24:53,132 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-16 19:24:53,132 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-16 19:24:53,133 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-16 19:24:53,133 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-16 19:24:53,133 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-16 19:24:53,134 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-16 19:24:53,134 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-16 19:24:53,134 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-16 19:24:53,135 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-16 19:24:53,135 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-16 19:24:53,136 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-16 19:24:53,136 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-16 19:24:53,136 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-16 19:24:53,137 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-16 19:24:53,137 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-16 19:24:53,137 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-16 19:24:53,138 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-16 19:24:53,138 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-16 19:24:53,139 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 19:24:53,144 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-16 19:24:53,178 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-16 19:24:53,216 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-16 19:24:53,276 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-16 19:24:53,321 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-16 19:24:53,368 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-16 19:24:53,422 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-16 19:24:53,457 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-16 19:24:53,546 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-16 19:24:53,786 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-16 19:24:54,032 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-16 19:24:54,335 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-16 19:24:54,606 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-16 19:24:56,060 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-16 19:24:56,061 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-16 19:24:56,062 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy EMAMACDStrategy
2025-09-16 19:24:56,062 - freqtrade.strategy.hyper - INFO - Strategy Parameter: macd_threshold = 0
2025-09-16 19:24:56,063 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.1
2025-09-16 19:24:56,063 - freqtrade.strategy.hyper - INFO - Strategy Parameter: window_macd_cross = 4
2025-09-16 19:24:56,064 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-09-16 19:24:56,064 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.991
2025-09-16 19:24:56,064 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-16 19:24:56,065 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-16 19:24:56,065 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-16 19:25:09,666 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-16 19:25:21,750 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-16_19-25-21.meta.json"
Result for strategy EMAMACDStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │     19 │        -0.03 │           2.898 │         0.29 │     11:54:00 │    9     0    10  47.4 │
│ XRP/USDT │     26 │         0.07 │          -5.693 │        -0.57 │     10:01:00 │    9     0    17  34.6 │
│ ETH/USDT │     23 │        -0.38 │         -43.188 │        -4.32 │      9:41:00 │    5     0    18  21.7 │
│ BTC/USDT │     25 │        -0.44 │         -51.437 │        -5.14 │      8:36:00 │    5     0    20  20.0 │
│ LTC/USDT │     22 │        -0.77 │         -93.692 │        -9.37 │      7:11:00 │    4     0    18  18.2 │
│    TOTAL │    115 │        -0.31 │        -191.113 │       -19.11 │      9:25:00 │   32     0    83  27.8 │
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
│     OTHER │     115 │        -0.31 │        -191.113 │       -19.11 │      9:25:00 │   32     0    83  27.8 │
│     TOTAL │     115 │        -0.31 │        -191.113 │       -19.11 │      9:25:00 │   32     0    83  27.8 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │     3 │         4.38 │          81.335 │         8.13 │     14:55:00 │    3     0     0   100 │
│      stop_loss │     2 │        -2.14 │         -25.374 │        -2.54 │      3:38:00 │    0     0     2     0 │
│    exit_signal │   110 │         -0.4 │        -247.074 │       -24.71 │      9:22:00 │   29     0    81  26.4 │
│          TOTAL │   115 │        -0.31 │        -191.113 │       -19.11 │      9:25:00 │   32     0    83  27.8 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │      3 │         4.38 │          81.335 │         8.13 │     14:55:00 │    3     0     0   100 │
│           │      stop_loss │      2 │        -2.14 │         -25.374 │        -2.54 │      3:38:00 │    0     0     2     0 │
│           │    exit_signal │    110 │         -0.4 │        -247.074 │       -24.71 │      9:22:00 │   29     0    81  26.4 │
│     TOTAL │                │    115 │        -0.31 │        -191.113 │       -19.11 │      9:25:00 │   32     0    83  27.8 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-11 17:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 115 / 0.09                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 808.887 USDT                   │
│ Absolute profit               │ -191.113 USDT                  │
│ Total profit %                │ -19.11%                        │
│ CAGR %                        │ -5.58%                         │
│ Sortino                       │ -0.79                          │
│ Sharpe                        │ -0.32                          │
│ Calmar                        │ -1.31                          │
│ SQN                           │ -2.10                          │
│ Profit factor                 │ 0.59                           │
│ Expectancy (Ratio)            │ -1.66 (-0.30)                  │
│ Avg. daily profit             │ -0.142 USDT                    │
│ Avg. stake amount             │ 661.92 USDT                    │
│ Total trade volume            │ 152354.976 USDT                │
│                               │                                │
│ Best Pair                     │ BNB/USDT 0.29%                 │
│ Worst Pair                    │ LTC/USDT -9.37%                │
│ Best trade                    │ XRP/USDT 5.99%                 │
│ Worst trade                   │ BTC/USDT -5.12%                │
│ Best day                      │ 40.693 USDT                    │
│ Worst day                     │ -21.201 USDT                   │
│ Days win/draw/lose            │ 31 / 1227 / 80                 │
│ Min/Max/Avg. Duration Winners │ 0d 07:05 / 1d 06:00 / 0d 17:13 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 0d 23:00 / 0d 06:24 │
│ Max Consecutive Wins / Loss   │ 2 / 10                         │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 805.129 USDT                   │
│ Max balance                   │ 1014.843 USDT                  │
│ Max % of account underwater   │ 20.66%                         │
│ Absolute Drawdown (Account)   │ 20.66%                         │
│ Absolute Drawdown             │ 209.714 USDT                   │
│ Drawdown high                 │ 14.843 USDT                    │
│ Drawdown low                  │ -194.871 USDT                  │
│ Drawdown Start                │ 2022-03-22 03:20:00            │
│ Drawdown End                  │ 2025-06-20 04:00:00            │
│ Market change                 │ 94.84%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                             STRATEGY SUMMARY                                                              
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃        Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ EMAMACDStrategy │    115 │        -0.31 │        -191.113 │       -19.11 │      9:25:00 │   32     0    83  27.8 │ 209.714 USDT  20.66% │
└─────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
