# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 3 / 0.0, Median: 44.11%, Total profit: -0.8%, Sortino: -0.06, Sharpe: -0.0, Calmar: -0.55, Drawdown: 2.04%)

---
            
**Strategy:** IchimokuRebondStrategy  
**Random State:** 77  
**Timestamp:** 2025-09-18 21:43:41

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 77,
  "epochs": 200,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 200 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 77
```

## Hyperopt Output
```
2025-09-18 19:39:27,717 - freqtrade - INFO - freqtrade 2025.7
2025-09-18 19:39:28,359 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-18 19:39:28,359 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-18 19:39:29,687 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-18 19:39:29,691 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-18 19:39:29,691 - freqtrade.loggers - INFO - Logfile configured
2025-09-18 19:39:29,692 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-18 19:39:29,692 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-18 19:39:29,692 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-18 19:39:29,693 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-18 19:39:29,701 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-18 19:39:29,702 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-18 19:39:29,702 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-18 19:39:29,703 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 200 epochs ...
2025-09-18 19:39:29,703 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-18 19:39:29,703 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-18 19:39:29,704 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-18 19:39:29,704 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 77
2025-09-18 19:39:29,705 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-18 19:39:29,705 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-18 19:39:29,706 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-18 19:39:29,706 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-18 19:39:29,707 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-18 19:39:29,727 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-18 19:39:29,728 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 19:39:29,732 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-18 19:39:29,733 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-18 19:39:29,738 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-18 19:39:29,739 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-18 19:39:29,773 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-18 19:39:32,062 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-18 19:39:32,100 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-18 19:39:32,101 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-18 19:39:32,102 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-18 19:39:32,103 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-18 19:39:32,103 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-18 19:39:32,103 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-18 19:39:32,104 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-18 19:39:32,104 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-18 19:39:32,105 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-18 19:39:32,105 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-18 19:39:32,105 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-18 19:39:32,106 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-18 19:39:32,106 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-18 19:39:32,106 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-18 19:39:32,107 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-18 19:39:32,107 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-18 19:39:32,108 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-18 19:39:32,108 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-18 19:39:32,109 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-18 19:39:32,110 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-18 19:39:32,110 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-18 19:39:32,111 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-18 19:39:32,111 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-18 19:39:32,112 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-18 19:39:32,112 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-18 19:39:32,113 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-18 19:39:32,113 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-18 19:39:32,114 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-18 19:39:32,114 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-18 19:39:32,115 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-18 19:39:32,115 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-18 19:39:32,116 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 19:39:32,121 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-18 19:39:32,153 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-18 19:39:32,155 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-18 19:39:32,156 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_rolling_window = 4
2025-09-18 19:39:32,156 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.589
2025-09-18 19:39:32,157 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.845
2025-09-18 19:39:32,157 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_proximity_threshold = 0.002
2025-09-18 19:39:32,157 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.021
2025-09-18 19:39:32,158 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 3
2025-09-18 19:39:32,158 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 4
2025-09-18 19:39:32,159 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 1.0
2025-09-18 19:39:32,159 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1
2025-09-18 19:39:32,159 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-18 19:39:32,160 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-18 19:39:32,160 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-18 19:39:32,181 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-18 19:39:32,182 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 77
2025-09-18 19:39:32,214 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-18 19:39:32,261 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-18 19:39:32,270 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-18 19:39:32,305 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-18 19:39:32,343 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-18 19:39:32,383 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-18 19:39:32,392 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-18 19:39:32,409 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-18 19:39:33,144 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-18 19:39:33,146 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 19:39:33,153 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-18 19:39:34,783 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 19:39:34,790 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-18 19:39:36,389 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 19:39:36,396 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-18 19:39:37,779 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 19:39:37,786 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-18 19:39:38,943 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 19:39:38,951 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-18 19:39:40,437 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-18 19:39:40,731 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 20 CPU cores. Let's make them scream!
2025-09-18 19:39:40,731 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-18 19:39:40,733 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-18 19:39:40,733] A new study created in memory with name: no-name-889c6670-0cc8-44da-abd0-06a8f27284ae
2025-09-18 19:39:40,791 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                         ┏━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓                         
                         ┃ Best   ┃   Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃      Avg duration ┃ Objective ┃    Max Drawdown (Acct) ┃                         
                         ┡━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩                         
                         │ * Best │   4/200 │     11 │    4     0     7  36.4 │      0.28% │  16.767 USDT    (1.68%) │          11:27:00 │  -0.01591 │ 56.522 USDT    (5.40%) │                         
                         │ * Best │   7/200 │     17 │    8     0     9  47.1 │      0.29% │  25.440 USDT    (2.54%) │          21:56:00 │  -0.02360 │ 54.432 USDT    (5.04%) │                         
                         │ * Best │   8/200 │     17 │    6     0    11  35.3 │      3.43% │  45.275 USDT    (4.53%) │  2 days, 13:18:00 │  -0.07337 │ 30.219 USDT    (2.81%) │                         
                         │ * Best │  16/200 │      9 │    4     0     5  44.4 │      3.15% │ 225.066 USDT   (22.51%) │          13:13:00 │  -0.08810 │ 44.628 USDT    (4.08%) │                         
                         │ Best   │  49/200 │     17 │    7     0    10  41.2 │      1.46% │ 243.012 USDT   (24.30%) │    1 day, 1:14:00 │  -0.11964 │ 68.870 USDT    (5.25%) │                         
                         │ Best   │  83/200 │     24 │   12     0    12  50.0 │      0.90% │ 242.275 USDT   (24.23%) │          19:02:00 │  -0.15356 │ 63.117 USDT    (5.97%) │                         
                         │ Best   │ 104/200 │      2 │    2     0     0   100 │     16.40% │  25.071 USDT    (2.51%) │  4 days, 17:30:00 │  -0.21255 │                     -- │                         
                         │ Best   │ 143/200 │      2 │    2     0     0   100 │     44.11% │  62.432 USDT    (6.24%) │ 15 days, 22:00:00 │  -1.61285 │                     -- │                         
                         └────────┴─────────┴────────┴────────────────────────┴────────────┴─────────────────────────┴───────────────────┴───────────┴────────────────────────┘                         
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 200/200 100% • 0:03:17 • 0:00:00
2025-09-18 19:42:58,743 - freqtrade.optimize.hyperopt.hyperopt - INFO - 200 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-18_19-39-29.fthypt'.
2025-09-18 19:42:58,774 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

   143/200:      2 trades. 2/0/0 Wins/Draws/Losses. Avg profit  44.11%. Median profit  44.11%. Total profit 62.43189198 USDT (   6.24%). Avg duration 15 days, 22:00:00 min. Objective: -1.61285

{"params":{"confirmation_candle":false,"flat_kinjun_rolling_window":6,"hammer_body_threshold":0.131,"hammer_head_threshold":0.434,"hammer_proximity_threshold":0.003,"hammer_strength_threshold":0.005,"kinjun_threshold":2,"lookback_period_for_stoploss":0,"stoploss_margin":0.991,"take_profit_multiplier":1.5,"use_sell_signal_param":false,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231
```

## Backtesting Output
```
2025-09-18 19:43:01,696 - freqtrade - INFO - freqtrade 2025.7
2025-09-18 19:43:02,034 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-18 19:43:02,035 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-18 19:43:03,477 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-18 19:43:03,479 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-18 19:43:03,480 - freqtrade.loggers - INFO - Logfile configured
2025-09-18 19:43:03,480 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-18 19:43:03,481 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-18 19:43:03,481 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-18 19:43:03,481 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-18 19:43:03,482 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-18 19:43:03,489 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-18 19:43:03,490 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-18 19:43:03,491 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-18 19:43:03,491 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-18 19:43:03,492 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-18 19:43:03,492 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-18 19:43:03,494 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-18 19:43:03,513 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-18 19:43:03,515 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 19:43:03,518 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-18 19:43:03,519 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-18 19:43:03,520 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-18 19:43:03,553 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-18 19:43:05,780 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-18 19:43:05,815 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-18 19:43:05,816 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-18 19:43:05,818 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-18 19:43:05,818 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-18 19:43:05,819 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-18 19:43:05,819 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-18 19:43:05,820 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-18 19:43:05,820 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-18 19:43:05,821 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-18 19:43:05,821 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-18 19:43:05,822 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-18 19:43:05,822 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-18 19:43:05,823 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-18 19:43:05,823 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-18 19:43:05,824 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-18 19:43:05,824 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-18 19:43:05,824 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-18 19:43:05,825 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-18 19:43:05,825 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-18 19:43:05,826 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-18 19:43:05,826 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-18 19:43:05,827 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-18 19:43:05,827 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-18 19:43:05,828 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-18 19:43:05,828 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-18 19:43:05,828 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-18 19:43:05,829 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-18 19:43:05,829 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-18 19:43:05,830 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-18 19:43:05,830 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-18 19:43:05,831 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 19:43:05,837 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-18 19:43:05,874 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-18 19:43:05,910 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-18 19:43:05,968 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-18 19:43:06,015 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-18 19:43:06,067 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-18 19:43:06,108 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-18 19:43:06,136 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-18 19:43:06,208 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-18 19:43:06,419 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-18 19:43:06,642 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-18 19:43:06,864 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-18 19:43:07,092 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-18 19:43:08,428 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-18 19:43:08,429 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-18 19:43:08,430 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-18 19:43:08,430 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-18 19:43:08,431 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_rolling_window = 6
2025-09-18 19:43:08,431 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.131
2025-09-18 19:43:08,431 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.434
2025-09-18 19:43:08,431 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_proximity_threshold = 0.003
2025-09-18 19:43:08,432 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.005
2025-09-18 19:43:08,432 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 2
2025-09-18 19:43:08,433 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 0
2025-09-18 19:43:08,433 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.991
2025-09-18 19:43:08,433 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-18 19:43:08,433 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-18 19:43:08,434 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-18 19:43:08,434 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-18 19:43:08,436 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 19:43:08,444 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-18 19:43:10,459 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 19:43:10,466 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-18 19:43:12,516 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 19:43:12,524 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-18 19:43:14,904 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 19:43:14,913 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-18 19:43:17,362 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 19:43:17,373 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-18 19:43:19,756 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-18 19:43:40,257 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-18_19-43-40.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │        21.73 │          29.192 │         2.92 │ 24 days, 6:20:00 │    1     0     0   100 │
│ BTC/USDT │      0 │          0.0 │           0.000 │          0.0 │             0:00 │    0     0     0     0 │
│ LTC/USDT │      0 │          0.0 │           0.000 │          0.0 │             0:00 │    0     0     0     0 │
│ ETH/USDT │      1 │       -31.52 │         -16.762 │        -1.68 │ 71 days, 5:05:00 │    0     0     1     0 │
│ XRP/USDT │      1 │        -6.27 │         -20.384 │        -2.04 │   1 day, 8:30:00 │    0     0     1     0 │
│    TOTAL │      3 │        -5.36 │          -7.954 │         -0.8 │ 32 days, 6:38:00 │    1     0     2  33.3 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                  ENTER TAG STATS                                                  
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │       3 │        -5.36 │          -7.954 │         -0.8 │ 32 days, 6:38:00 │    1     0     2  33.3 │
│     TOTAL │       3 │        -5.36 │          -7.954 │         -0.8 │ 32 days, 6:38:00 │    1     0     2  33.3 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                   EXIT REASON STATS                                                    
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │     1 │        21.73 │          29.192 │         2.92 │ 24 days, 6:20:00 │    1     0     0   100 │
│        stop_loss │     2 │        -18.9 │         -37.146 │        -3.71 │ 36 days, 6:48:00 │    0     0     2     0 │
│            TOTAL │     3 │        -5.36 │          -7.954 │         -0.8 │ 32 days, 6:38:00 │    1     0     2  33.3 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                           MIXED TAG STATS                                                           
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1.5R │      1 │        21.73 │          29.192 │         2.92 │ 24 days, 6:20:00 │    1     0     0   100 │
│           │        stop_loss │      2 │        -18.9 │         -37.146 │        -3.71 │ 36 days, 6:48:00 │    0     0     2     0 │
│     TOTAL │                  │      3 │        -5.36 │          -7.954 │         -0.8 │ 32 days, 6:38:00 │    1     0     2  33.3 │
└───────────┴──────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                           SUMMARY METRICS                           
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                             ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00               │
│ Backtesting to                │ 2025-09-11 17:00:00               │
│ Trading Mode                  │ Spot                              │
│ Max open trades               │ 3                                 │
│                               │                                   │
│ Total/Daily Avg Trades        │ 3 / 0.0                           │
│ Starting balance              │ 1000 USDT                         │
│ Final balance                 │ 992.046 USDT                      │
│ Absolute profit               │ -7.954 USDT                       │
│ Total profit %                │ -0.80%                            │
│ CAGR %                        │ -0.22%                            │
│ Sortino                       │ -0.06                             │
│ Sharpe                        │ -0.00                             │
│ Calmar                        │ -0.55                             │
│ SQN                           │ -0.17                             │
│ Profit factor                 │ 0.79                              │
│ Expectancy (Ratio)            │ -2.65 (-0.14)                     │
│ Avg. daily profit             │ -0.006 USDT                       │
│ Avg. stake amount             │ 170.646 USDT                      │
│ Total trade volume            │ 1017.954 USDT                     │
│                               │                                   │
│ Best Pair                     │ BNB/USDT 2.92%                    │
│ Worst Pair                    │ XRP/USDT -2.04%                   │
│ Best trade                    │ BNB/USDT 21.73%                   │
│ Worst trade                   │ ETH/USDT -31.52%                  │
│ Best day                      │ 29.192 USDT                       │
│ Worst day                     │ -20.384 USDT                      │
│ Days win/draw/lose            │ 1 / 701 / 2                       │
│ Min/Max/Avg. Duration Winners │ 24d 06:20 / 24d 06:20 / 24d 06:20 │
│ Min/Max/Avg. Duration Losers  │ 1d 08:30 / 71d 05:05 / 36d 06:48  │
│ Max Consecutive Wins / Loss   │ 1 / 1                             │
│ Rejected Entry signals        │ 0                                 │
│ Entry/Exit Timeouts           │ 0 / 0                             │
│                               │                                   │
│ Min balance                   │ 979.616 USDT                      │
│ Max balance                   │ 1008.808 USDT                     │
│ Max % of account underwater   │ 2.04%                             │
│ Absolute Drawdown (Account)   │ 2.04%                             │
│ Absolute Drawdown             │ 20.384 USDT                       │
│ Drawdown high                 │ -20.384 USDT                      │
│ Drawdown low                  │ -20.384 USDT                      │
│ Drawdown Start                │ 2023-03-03 01:30:00               │
│ Drawdown End                  │ 2023-03-03 01:30:00               │
│ Market change                 │ 94.84%                            │
└───────────────────────────────┴───────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                  
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │      3 │        -5.36 │          -7.954 │         -0.8 │ 32 days, 6:38:00 │    1     0     2  33.3 │ 20.384 USDT  2.04% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┴────────────────────┘

```
