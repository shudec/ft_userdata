# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 1 / 0.0, Median: 8.05%, Total profit: -2.08%, Sortino: -100.0, Sharpe: -100.0, Calmar: -100.0, Drawdown: 0.0%)

---
            
**Strategy:** IchimokuRebondStrategy  
**Random State:** 2138  
**Timestamp:** 2025-09-18 21:38:45

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 2138,
  "epochs": 200,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 200 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 2138
```

## Hyperopt Output
```
2025-09-18 19:35:24,178 - freqtrade - INFO - freqtrade 2025.7
2025-09-18 19:35:24,811 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-18 19:35:24,812 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-18 19:35:26,112 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-18 19:35:26,115 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-18 19:35:26,115 - freqtrade.loggers - INFO - Logfile configured
2025-09-18 19:35:26,116 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-18 19:35:26,116 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-18 19:35:26,116 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-18 19:35:26,117 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-18 19:35:26,125 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-18 19:35:26,126 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-18 19:35:26,126 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-18 19:35:26,127 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 200 epochs ...
2025-09-18 19:35:26,127 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-18 19:35:26,128 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-18 19:35:26,128 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-18 19:35:26,129 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 2138
2025-09-18 19:35:26,129 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-18 19:35:26,129 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-18 19:35:26,130 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-18 19:35:26,130 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-18 19:35:26,132 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-18 19:35:26,151 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-18 19:35:26,152 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 19:35:26,155 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-18 19:35:26,157 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-18 19:35:26,162 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-18 19:35:26,163 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-18 19:35:26,196 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-18 19:35:28,400 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-18 19:35:28,436 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-18 19:35:28,437 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-18 19:35:28,438 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-18 19:35:28,438 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-18 19:35:28,439 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-18 19:35:28,439 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-18 19:35:28,439 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-18 19:35:28,440 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-18 19:35:28,440 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-18 19:35:28,441 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-18 19:35:28,441 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-18 19:35:28,441 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-18 19:35:28,442 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-18 19:35:28,443 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-18 19:35:28,443 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-18 19:35:28,443 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-18 19:35:28,444 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-18 19:35:28,444 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-18 19:35:28,445 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-18 19:35:28,445 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-18 19:35:28,445 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-18 19:35:28,446 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-18 19:35:28,446 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-18 19:35:28,447 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-18 19:35:28,447 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-18 19:35:28,447 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-18 19:35:28,448 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-18 19:35:28,448 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-18 19:35:28,449 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-18 19:35:28,449 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-18 19:35:28,449 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-18 19:35:28,450 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 19:35:28,456 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-18 19:35:28,490 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-18 19:35:28,492 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-18 19:35:28,492 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_rolling_window = 5
2025-09-18 19:35:28,493 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.499
2025-09-18 19:35:28,493 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.675
2025-09-18 19:35:28,493 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): hammer_proximity_threshold = 0.001
2025-09-18 19:35:28,494 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.022
2025-09-18 19:35:28,494 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 8
2025-09-18 19:35:28,495 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 1
2025-09-18 19:35:28,495 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.99
2025-09-18 19:35:28,496 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-18 19:35:28,496 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-18 19:35:28,497 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-18 19:35:28,497 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-18 19:35:28,504 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-18 19:35:28,505 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 2138
2025-09-18 19:35:28,537 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-18 19:35:28,586 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-18 19:35:28,595 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-18 19:35:28,632 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-18 19:35:28,673 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-18 19:35:28,712 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-18 19:35:28,720 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-18 19:35:28,735 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-18 19:35:29,462 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-18 19:35:29,464 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 19:35:29,470 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-18 19:35:31,104 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 19:35:31,113 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-18 19:35:32,708 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 19:35:32,714 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-18 19:35:34,114 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 19:35:34,120 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-18 19:35:35,227 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 19:35:35,234 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-18 19:35:36,706 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-18 19:35:37,000 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 20 CPU cores. Let's make them scream!
2025-09-18 19:35:37,000 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-18 19:35:37,002 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-18 19:35:37,002] A new study created in memory with name: no-name-d4918ef7-1022-4c9c-8d2a-652bb57bcab8
2025-09-18 19:35:37,052 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                           ┏━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓                           
                           ┃ Best   ┃   Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃ Avg duration ┃ Objective ┃     Max Drawdown (Acct) ┃                           
                           ┡━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩                           
                           │ * Best │   3/200 │     32 │    8     0    24  25.0 │      0.27% │  88.953 USDT    (8.90%) │     13:17:00 │  -0.06292 │ 113.125 USDT   (10.11%) │                           
                           │ * Best │  10/200 │      2 │    2     0     0   100 │      6.26% │  58.686 USDT    (5.87%) │     12:30:00 │  -0.13647 │                      -- │                           
                           │ Best   │ 121/200 │     18 │    8     0    10  44.4 │      1.47% │ 293.452 USDT   (29.35%) │     20:37:00 │  -0.15556 │  83.215 USDT    (8.32%) │                           
                           │ Best   │ 130/200 │     29 │   14     0    15  48.3 │      1.19% │ 288.610 USDT   (28.86%) │     19:43:00 │  -0.17541 │ 139.595 USDT   (10.01%) │                           
                           │ Best   │ 152/200 │     21 │   10     0    11  47.6 │      2.81% │ 482.686 USDT   (48.27%) │     23:46:00 │  -0.19341 │  86.441 USDT    (5.73%) │                           
                           │ Best   │ 158/200 │     21 │   10     0    11  47.6 │      2.78% │ 492.261 USDT   (49.23%) │     23:26:00 │  -0.19651 │  84.438 USDT    (5.54%) │                           
                           │ Best   │ 165/200 │     21 │   10     0    11  47.6 │      2.70% │ 505.698 USDT   (50.57%) │     18:09:00 │  -0.21078 │  53.134 USDT    (3.57%) │                           
                           │ Best   │ 182/200 │     21 │   10     0    11  47.6 │      3.01% │ 511.448 USDT   (51.14%) │     17:03:00 │  -0.23397 │  44.904 USDT    (4.37%) │                           
                           │ Best   │ 195/200 │      3 │    3     0     0   100 │      6.85% │  92.833 USDT    (9.28%) │     11:20:00 │  -0.24465 │                      -- │                           
                           └────────┴─────────┴────────┴────────────────────────┴────────────┴─────────────────────────┴──────────────┴───────────┴─────────────────────────┘                           
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 200/200 100% • 0:02:39 • 0:00:00
2025-09-18 19:38:16,275 - freqtrade.optimize.hyperopt.hyperopt - INFO - 200 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-18_19-35-26.fthypt'.
2025-09-18 19:38:16,315 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

   195/200:      3 trades. 3/0/0 Wins/Draws/Losses. Avg profit   6.85%. Median profit   8.05%. Total profit 92.83336398 USDT (   9.28%). Avg duration 11:20:00 min. Objective: -0.24465

{"params":{"confirmation_candle":true,"flat_kinjun_rolling_window":4,"hammer_body_threshold":0.589,"hammer_head_threshold":0.845,"hammer_proximity_threshold":0.002,"hammer_strength_threshold":0.021,"kinjun_threshold":3,"lookback_period_for_stoploss":4,"stoploss_margin":1.0,"take_profit_multiplier":1,"use_sell_signal_param":true,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231
```

## Backtesting Output
```
2025-09-18 19:38:19,228 - freqtrade - INFO - freqtrade 2025.7
2025-09-18 19:38:19,576 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-18 19:38:19,576 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-18 19:38:21,043 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-18 19:38:21,046 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-18 19:38:21,046 - freqtrade.loggers - INFO - Logfile configured
2025-09-18 19:38:21,047 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-18 19:38:21,047 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-18 19:38:21,048 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-18 19:38:21,048 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-18 19:38:21,048 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-18 19:38:21,056 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-18 19:38:21,057 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-18 19:38:21,057 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-18 19:38:21,058 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-18 19:38:21,058 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-18 19:38:21,059 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-18 19:38:21,060 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-18 19:38:21,080 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-18 19:38:21,081 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 19:38:21,084 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-18 19:38:21,085 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-18 19:38:21,086 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-18 19:38:21,119 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-18 19:38:23,710 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-18 19:38:23,746 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-18 19:38:23,747 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-18 19:38:23,748 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-18 19:38:23,748 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-18 19:38:23,749 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-18 19:38:23,749 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-18 19:38:23,750 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-18 19:38:23,750 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-18 19:38:23,751 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-18 19:38:23,751 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-18 19:38:23,751 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-18 19:38:23,752 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-18 19:38:23,752 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-18 19:38:23,752 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-18 19:38:23,753 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-18 19:38:23,753 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-18 19:38:23,753 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-18 19:38:23,754 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-18 19:38:23,754 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-18 19:38:23,754 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-18 19:38:23,755 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-18 19:38:23,755 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-18 19:38:23,755 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-18 19:38:23,756 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-18 19:38:23,756 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-18 19:38:23,756 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-18 19:38:23,757 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-18 19:38:23,757 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-18 19:38:23,758 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-18 19:38:23,758 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-18 19:38:23,759 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 19:38:23,763 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-18 19:38:23,799 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-18 19:38:23,831 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-18 19:38:23,879 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-18 19:38:23,922 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-18 19:38:23,965 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-18 19:38:24,007 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-18 19:38:24,031 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-18 19:38:24,118 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-18 19:38:24,357 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-18 19:38:24,594 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-18 19:38:24,812 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-18 19:38:25,027 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-18 19:38:26,436 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-18 19:38:26,438 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-18 19:38:26,439 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-18 19:38:26,439 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-18 19:38:26,440 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_rolling_window = 4
2025-09-18 19:38:26,441 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.589
2025-09-18 19:38:26,441 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.845
2025-09-18 19:38:26,442 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_proximity_threshold = 0.002
2025-09-18 19:38:26,442 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.021
2025-09-18 19:38:26,443 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 3
2025-09-18 19:38:26,444 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 4
2025-09-18 19:38:26,444 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 1.0
2025-09-18 19:38:26,445 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-18 19:38:26,445 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-18 19:38:26,446 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-18 19:38:26,446 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-18 19:38:26,449 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 19:38:26,459 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-18 19:38:29,263 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 19:38:29,271 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-18 19:38:31,876 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 19:38:31,883 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-18 19:38:34,537 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 19:38:34,544 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-18 19:38:37,189 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 19:38:37,197 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-18 19:38:39,857 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-18 19:38:44,279 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-18_19-38-44.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │      0 │          0.0 │           0.000 │          0.0 │            0:00 │    0     0     0     0 │
│ ETH/USDT │      0 │          0.0 │           0.000 │          0.0 │            0:00 │    0     0     0     0 │
│ LTC/USDT │      0 │          0.0 │           0.000 │          0.0 │            0:00 │    0     0     0     0 │
│ BNB/USDT │      0 │          0.0 │           0.000 │          0.0 │            0:00 │    0     0     0     0 │
│ XRP/USDT │      1 │        -4.24 │         -20.756 │        -2.08 │ 4 days, 3:50:00 │    0     0     1     0 │
│    TOTAL │      1 │        -4.24 │         -20.756 │        -2.08 │ 4 days, 3:50:00 │    0     0     1     0 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 ENTER TAG STATS                                                  
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │       1 │        -4.24 │         -20.756 │        -2.08 │ 4 days, 3:50:00 │    0     0     1     0 │
│     TOTAL │       1 │        -4.24 │         -20.756 │        -2.08 │ 4 days, 3:50:00 │    0     0     1     0 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│   stop_loss │     1 │        -4.24 │         -20.756 │        -2.08 │ 4 days, 3:50:00 │    0     0     1     0 │
│       TOTAL │     1 │        -4.24 │         -20.756 │        -2.08 │ 4 days, 3:50:00 │    0     0     1     0 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │   stop_loss │      1 │        -4.24 │         -20.756 │        -2.08 │ 4 days, 3:50:00 │    0     0     1     0 │
│     TOTAL │             │      1 │        -4.24 │         -20.756 │        -2.08 │ 4 days, 3:50:00 │    0     0     1     0 │
└───────────┴─────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-11 17:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 1 / 0.0                        │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 979.244 USDT                   │
│ Absolute profit               │ -20.756 USDT                   │
│ Total profit %                │ -2.08%                         │
│ CAGR %                        │ -0.57%                         │
│ Sortino                       │ -100.00                        │
│ Sharpe                        │ -100.00                        │
│ Calmar                        │ -100.00                        │
│ SQN                           │ -100.00                        │
│ Profit factor                 │ 0.00                           │
│ Expectancy (Ratio)            │ -20.76 (-1.00)                 │
│ Avg. daily profit             │ -0.015 USDT                    │
│ Avg. stake amount             │ 488.741 USDT                   │
│ Total trade volume            │ 958.641 USDT                   │
│                               │                                │
│ Best Pair                     │ BTC/USDT 0.00%                 │
│ Worst Pair                    │ XRP/USDT -2.08%                │
│ Best trade                    │ XRP/USDT -4.24%                │
│ Worst trade                   │ XRP/USDT -4.24%                │
│ Best day                      │ -20.756 USDT                   │
│ Worst day                     │ -20.756 USDT                   │
│ Days win/draw/lose            │ 0 / 0 / 1                      │
│ Min/Max/Avg. Duration Winners │ 0d 00:00 / 0d 00:00 / 0d 00:00 │
│ Min/Max/Avg. Duration Losers  │ 4d 03:50 / 4d 03:50 / 4d 03:50 │
│ Max Consecutive Wins / Loss   │ 0 / 1                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 0 USDT                         │
│ Max balance                   │ 0 USDT                         │
│ Max % of account underwater   │ 0.00%                          │
│ Absolute Drawdown (Account)   │ 0.00%                          │
│ Absolute Drawdown             │ 0 USDT                         │
│ Drawdown high                 │ 0 USDT                         │
│ Drawdown low                  │ 0 USDT                         │
│ Drawdown Start                │ 1970-01-01 00:00:00+00:00      │
│ Drawdown End                  │ 1970-01-01 00:00:00+00:00      │
│ Market change                 │ 94.84%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                               STRATEGY SUMMARY                                                               
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃      Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │      1 │        -4.24 │         -20.756 │        -2.08 │ 4 days, 3:50:00 │    0     0     1     0 │ 0 USDT  0.00% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴───────────────┘

```
