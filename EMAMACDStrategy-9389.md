# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 1 / 0.0, Median: -1.52%, Total profit: 2.66%, Sortino: -100.0, Sharpe: -100.0, Calmar: -100.0, Drawdown: 0%)

---
            
**Strategy:** EMAMACDStrategy  
**Random State:** 9389  
**Timestamp:** 2025-09-16 15:28:02

## Configuration
```json
{
  "strategy": "EMAMACDStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 9389,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy EMAMACDStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 9389
```

## Hyperopt Output
```
2025-09-16 13:26:14,421 - freqtrade - INFO - freqtrade 2025.8
2025-09-16 13:26:15,136 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-16 13:26:16,420 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-16 13:26:16,427 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-16 13:26:16,428 - freqtrade.loggers - INFO - Logfile configured
2025-09-16 13:26:16,429 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-16 13:26:16,430 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-16 13:26:16,431 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-16 13:26:16,431 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-16 13:26:16,810 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-16 13:26:16,815 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-16 13:26:16,816 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-16 13:26:16,817 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 100 epochs ...
2025-09-16 13:26:16,817 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-16 13:26:16,818 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-16 13:26:16,819 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-16 13:26:16,819 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 9389
2025-09-16 13:26:16,820 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-16 13:26:16,820 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-16 13:26:16,821 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-16 13:26:16,821 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-16 13:26:16,823 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-16 13:26:16,840 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-16 13:26:16,841 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 13:26:16,846 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-16 13:26:16,854 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-16 13:26:16,862 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-16 13:26:16,863 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-16 13:26:16,893 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-16 13:26:19,415 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-16 13:26:19,475 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy EMAMACDStrategy from '/freqtrade/user_data/strategies/EMAMACDStrategy.py'...
2025-09-16 13:26:19,477 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/EMAMACDStrategy.json
2025-09-16 13:26:19,481 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-16 13:26:19,482 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-16 13:26:19,483 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-16 13:26:19,483 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-16 13:26:19,483 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-16 13:26:19,484 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-16 13:26:19,484 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-16 13:26:19,485 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-16 13:26:19,485 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-16 13:26:19,486 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-16 13:26:19,486 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-16 13:26:19,486 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-16 13:26:19,487 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-16 13:26:19,487 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-16 13:26:19,487 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-16 13:26:19,487 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-16 13:26:19,488 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-16 13:26:19,488 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-16 13:26:19,488 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-16 13:26:19,489 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-16 13:26:19,489 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-16 13:26:19,490 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-16 13:26:19,490 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-16 13:26:19,490 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-16 13:26:19,491 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-16 13:26:19,491 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-16 13:26:19,491 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-16 13:26:19,492 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-16 13:26:19,492 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-16 13:26:19,492 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 13:26:19,510 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-16 13:26:19,537 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-16 13:26:19,539 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1.216
2025-09-16 13:26:19,539 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-09-16 13:26:19,540 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-09-16 13:26:19,540 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-16 13:26:19,541 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-16 13:26:19,541 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-16 13:26:19,560 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-16 13:26:19,560 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 9389
2025-09-16 13:26:19,616 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-16 13:26:19,678 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-16 13:26:19,689 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-16 13:26:19,739 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-16 13:26:19,792 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-16 13:26:19,855 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-16 13:26:19,864 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-16 13:26:19,878 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-16 13:26:20,560 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-16 13:26:29,002 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-16 13:26:29,392 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 16 CPU cores. Let's make them scream!
2025-09-16 13:26:29,393 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-16 13:26:29,394 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-16 13:26:29,395] A new study created in memory with name: no-name-9ed882df-90ed-44db-bbaa-0f01fca8be57
2025-09-16 13:26:29,445 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                         ┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓                         
                         ┃ Best   ┃  Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                   Profit ┃     Avg duration ┃ Objective ┃     Max Drawdown (Acct) ┃                         
                         ┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩                         
                         │ * Best │  1/100 │      2 │    0     0     2     0 │     -6.65% │  -40.778 USDT   (-4.08%) │  5 days, 8:00:00 │   4.38945 │  40.778 USDT    (4.08%) │                         
                         │ * Best │  2/100 │      4 │    0     0     4     0 │     -4.39% │  -78.123 USDT   (-7.81%) │ 3 days, 15:15:00 │   1.12334 │  78.123 USDT    (7.81%) │                         
                         │ * Best │  5/100 │     14 │    3     0    11  21.4 │     -1.78% │ -120.154 USDT  (-12.02%) │  2 days, 0:00:00 │   0.13933 │ 130.368 USDT   (13.04%) │                         
                         │ * Best │  7/100 │      6 │    1     0     5  16.7 │     -3.01% │  -63.745 USDT   (-6.37%) │ 3 days, 14:00:00 │   0.06491 │  63.745 USDT    (6.37%) │                         
                         │ * Best │ 17/100 │      9 │    2     0     7  22.2 │     -1.96% │  -56.026 USDT   (-5.60%) │  3 days, 4:27:00 │   0.04684 │  80.594 USDT    (8.06%) │                         
                         │ Best   │ 32/100 │      8 │    2     0     6  25.0 │     -1.23% │  -22.507 USDT   (-2.25%) │  2 days, 4:52:00 │   0.01860 │  55.935 USDT    (5.59%) │                         
                         │ Best   │ 37/100 │     11 │    3     0     8  27.3 │     -0.93% │  -19.156 USDT   (-1.92%) │  1 day, 20:11:00 │   0.01659 │  84.590 USDT    (8.46%) │                         
                         │ Best   │ 39/100 │     10 │    3     0     7  30.0 │     -0.98% │  -15.348 USDT   (-1.53%) │  1 day, 23:48:00 │   0.01288 │  75.981 USDT    (7.60%) │                         
                         │ Best   │ 67/100 │      9 │    3     0     6  33.3 │     -0.70% │   12.520 USDT    (1.25%) │  2 days, 1:27:00 │  -0.00988 │  55.026 USDT    (5.50%) │                         
                         └────────┴────────┴────────┴────────────────────────┴────────────┴──────────────────────────┴──────────────────┴───────────┴─────────────────────────┘                         
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100/100 100% • 0:01:12 • 0:00:00
2025-09-16 13:27:41,786 - freqtrade.optimize.hyperopt.hyperopt - INFO - 100 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_EMAMACDStrategy_2025-09-16_13-26-16.fthypt'.
2025-09-16 13:27:41,900 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/EMAMACDStrategy.json

Best result:

    67/100:      9 trades. 3/0/6 Wins/Draws/Losses. Avg profit  -0.70%. Median profit  -1.52%. Total profit 12.52016550 USDT (   1.25%). Avg duration 2 days, 1:27:00 min. Objective: -0.00988

{"params":{"volume_factor":1.183,"stoploss_margin":1.0,"lookback_period_for_stoploss":5,"take_profit_multiplier":2,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy EMAMACDStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20221231
```

## Backtesting Output
```
2025-09-16 13:27:46,124 - freqtrade - INFO - freqtrade 2025.8
2025-09-16 13:27:46,446 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-16 13:27:48,060 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-16 13:27:48,067 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-16 13:27:48,067 - freqtrade.loggers - INFO - Logfile configured
2025-09-16 13:27:48,067 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-16 13:27:48,069 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-16 13:27:48,070 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-16 13:27:48,070 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-16 13:27:48,071 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20221231 ...
2025-09-16 13:27:48,474 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-16 13:27:48,476 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-16 13:27:48,477 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-16 13:27:48,477 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-16 13:27:48,477 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-16 13:27:48,478 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20221231
2025-09-16 13:27:48,479 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-16 13:27:48,492 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-16 13:27:48,493 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 13:27:48,495 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-16 13:27:48,497 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-16 13:27:48,497 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-16 13:27:48,526 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-16 13:27:51,096 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-16 13:27:51,163 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy EMAMACDStrategy from '/freqtrade/user_data/strategies/EMAMACDStrategy.py'...
2025-09-16 13:27:51,165 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/EMAMACDStrategy.json
2025-09-16 13:27:51,171 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-16 13:27:51,173 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-16 13:27:51,173 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-16 13:27:51,174 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-16 13:27:51,175 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-16 13:27:51,176 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-16 13:27:51,176 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-16 13:27:51,177 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-16 13:27:51,177 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-16 13:27:51,178 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-16 13:27:51,178 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-16 13:27:51,179 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-16 13:27:51,179 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-16 13:27:51,180 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-16 13:27:51,180 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-16 13:27:51,181 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-16 13:27:51,181 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-16 13:27:51,182 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-16 13:27:51,183 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-16 13:27:51,183 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-16 13:27:51,184 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-16 13:27:51,185 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-16 13:27:51,185 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-16 13:27:51,186 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-16 13:27:51,186 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-16 13:27:51,187 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-16 13:27:51,187 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-16 13:27:51,189 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-16 13:27:51,190 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 13:27:51,218 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-16 13:27:51,259 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-16 13:27:51,562 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2022-12-31 00:00:00 (364 days).
2025-09-16 13:27:53,932 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-16 13:27:53,952 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy EMAMACDStrategy
2025-09-16 13:27:53,954 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1.183
2025-09-16 13:27:53,955 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-09-16 13:27:53,955 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 1.0
2025-09-16 13:27:53,956 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-16 13:27:53,957 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-16 13:27:53,958 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-16 13:27:58,842 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2022-12-31 00:00:00 (364 days).
2025-09-16 13:27:59,826 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-16_13-27-59.meta.json"
Result for strategy EMAMACDStrategy
                                              BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │      1 │         2.68 │          26.575 │         2.66 │ 1 day, 3:15:00 │    1     0     0   100 │
│ BTC/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│ ETH/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│ LTC/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│ BNB/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│    TOTAL │      1 │         2.68 │          26.575 │         2.66 │ 1 day, 3:15:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 ENTER TAG STATS                                                 
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │       1 │         2.68 │          26.575 │         2.66 │ 1 day, 3:15:00 │    1     0     0   100 │
│     TOTAL │       1 │         2.68 │          26.575 │         2.66 │ 1 day, 3:15:00 │    1     0     0   100 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │     1 │         2.68 │          26.575 │         2.66 │ 1 day, 3:15:00 │    1     0     0   100 │
│          TOTAL │     1 │         2.68 │          26.575 │         2.66 │ 1 day, 3:15:00 │    1     0     0   100 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │      1 │         2.68 │          26.575 │         2.66 │ 1 day, 3:15:00 │    1     0     0   100 │
│     TOTAL │                │      1 │         2.68 │          26.575 │         2.66 │ 1 day, 3:15:00 │    1     0     0   100 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2022-12-31 00:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 1 / 0.0                        │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1026.575 USDT                  │
│ Absolute profit               │ 26.575 USDT                    │
│ Total profit %                │ 2.66%                          │
│ CAGR %                        │ 2.66%                          │
│ Sortino                       │ -100.00                        │
│ Sharpe                        │ -100.00                        │
│ Calmar                        │ -100.00                        │
│ SQN                           │ -100.00                        │
│ Profit factor                 │ 0.00                           │
│ Expectancy (Ratio)            │ 26.58 (100.00)                 │
│ Avg. daily profit             │ 0.073 USDT                     │
│ Avg. stake amount             │ 989.959 USDT                   │
│ Total trade volume            │ 2010.511 USDT                  │
│                               │                                │
│ Best Pair                     │ XRP/USDT 2.66%                 │
│ Worst Pair                    │ BTC/USDT 0.00%                 │
│ Best trade                    │ XRP/USDT 2.68%                 │
│ Worst trade                   │ XRP/USDT 2.68%                 │
│ Best day                      │ 26.575 USDT                    │
│ Worst day                     │ 26.575 USDT                    │
│ Days win/draw/lose            │ 1 / 0 / 0                      │
│ Min/Max/Avg. Duration Winners │ 1d 03:15 / 1d 03:15 / 1d 03:15 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 0d 00:00 / 0d 00:00 │
│ Max Consecutive Wins / Loss   │ 1 / 0                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 0 USDT                         │
│ Max balance                   │ 0 USDT                         │
│ Max % of account underwater   │ 0.00%                          │
│ Absolute drawdown             │ 0 USDT (0.00%)                 │
│ Drawdown duration             │ N/A                            │
│ Profit at drawdown start      │ 0 USDT                         │
│ Profit at drawdown end        │ 0 USDT                         │
│ Drawdown start                │ 1970-01-01 00:00:00+00:00      │
│ Drawdown end                  │ 1970-01-01 00:00:00+00:00      │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                           STRATEGY SUMMARY                                                           
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃        Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃      Drawdown ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ EMAMACDStrategy │      1 │         2.68 │          26.575 │         2.66 │ 1 day, 3:15:00 │    1     0     0   100 │ 0 USDT  0.00% │
└─────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┴───────────────┘

```
