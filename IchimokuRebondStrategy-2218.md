# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 35 / 0.03, Median: 2.72%, Total profit: -18.27%, Sortino: -0.84, Sharpe: -0.12, Calmar: -0.97, Drawdown: 26.66%)

---
            
**Strategy:** IchimokuRebondStrategy  
**Random State:** 2218  
**Timestamp:** 2025-09-18 21:05:06

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 2218,
  "epochs": 200,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 200 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 2218
```

## Hyperopt Output
```
2025-09-18 19:01:29,181 - freqtrade - INFO - freqtrade 2025.7
2025-09-18 19:01:29,829 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-18 19:01:29,830 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-18 19:01:31,256 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-18 19:01:31,259 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-18 19:01:31,259 - freqtrade.loggers - INFO - Logfile configured
2025-09-18 19:01:31,260 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-18 19:01:31,260 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-18 19:01:31,261 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-18 19:01:31,261 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-18 19:01:31,273 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-18 19:01:31,274 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-18 19:01:31,275 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-18 19:01:31,275 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 200 epochs ...
2025-09-18 19:01:31,276 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-18 19:01:31,276 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-18 19:01:31,277 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-18 19:01:31,277 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 2218
2025-09-18 19:01:31,278 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-18 19:01:31,278 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-18 19:01:31,279 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-18 19:01:31,279 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-18 19:01:31,281 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-18 19:01:31,305 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-18 19:01:31,306 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 19:01:31,311 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-18 19:01:31,312 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-18 19:01:31,318 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-18 19:01:31,319 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-18 19:01:31,353 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-18 19:01:33,641 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-18 19:01:33,676 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-18 19:01:33,677 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2025-09-18 19:01:33,678 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-18 19:01:33,678 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-18 19:01:33,679 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-18 19:01:33,679 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-18 19:01:33,680 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-18 19:01:33,680 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-18 19:01:33,680 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-18 19:01:33,681 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-18 19:01:33,681 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-18 19:01:33,682 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-18 19:01:33,682 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-18 19:01:33,682 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-18 19:01:33,683 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-18 19:01:33,683 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-18 19:01:33,683 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-18 19:01:33,684 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-18 19:01:33,684 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-18 19:01:33,685 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-18 19:01:33,685 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-18 19:01:33,685 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-18 19:01:33,686 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-18 19:01:33,686 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-18 19:01:33,686 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-18 19:01:33,687 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-18 19:01:33,687 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-18 19:01:33,688 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-18 19:01:33,688 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-18 19:01:33,688 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-18 19:01:33,689 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-18 19:01:33,689 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 19:01:33,695 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-18 19:01:33,727 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-18 19:01:33,729 - freqtrade.strategy.hyper - INFO - No params for buy found, using default values.
2025-09-18 19:01:33,730 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): confirmation_candle = True
2025-09-18 19:01:33,731 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): hammer_body_threshold = 0.2
2025-09-18 19:01:33,731 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): hammer_head_threshold = 0.1
2025-09-18 19:01:33,732 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): hammer_strength_threshold = 0.01
2025-09-18 19:01:33,732 - freqtrade.strategy.hyper - INFO - No params for sell found, using default values.
2025-09-18 19:01:33,733 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): kinjun_threshold = 2
2025-09-18 19:01:33,733 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): lookback_period_for_stoploss = 5
2025-09-18 19:01:33,733 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): stoploss_margin = 0.999
2025-09-18 19:01:33,734 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): take_profit_multiplier = 2
2025-09-18 19:01:33,734 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_stoploss_param = True
2025-09-18 19:01:33,735 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_sell_signal_param = True
2025-09-18 19:01:33,735 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-18 19:01:33,742 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-18 19:01:33,742 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 2218
2025-09-18 19:01:33,780 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-18 19:01:33,838 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-18 19:01:33,846 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-18 19:01:33,885 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-18 19:01:33,935 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-18 19:01:33,974 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-18 19:01:33,983 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-18 19:01:34,000 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-18 19:01:34,748 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-18 19:01:34,750 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 19:01:34,761 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-18 19:01:36,504 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 19:01:36,511 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-18 19:01:38,181 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 19:01:38,188 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-18 19:01:39,649 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 19:01:39,656 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-18 19:01:40,829 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 19:01:40,838 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-18 19:01:42,396 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-18 19:01:42,689 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 20 CPU cores. Let's make them scream!
2025-09-18 19:01:42,690 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-18 19:01:42,691 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-18 19:01:42,692] A new study created in memory with name: no-name-355c0b6e-1c17-47e2-b181-2d0449432bc1
2025-09-18 19:01:42,742 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                           ┏━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓                           
                           ┃ Best   ┃   Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃ Avg duration ┃ Objective ┃     Max Drawdown (Acct) ┃                           
                           ┡━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩                           
                           │ * Best │   1/200 │     60 │   12     0    48  20.0 │     -0.01% │ -53.729 USDT   (-5.37%) │     18:29:00 │   0.03163 │ 291.077 USDT   (23.52%) │                           
                           │ * Best │   2/200 │     21 │    8     0    13  38.1 │      1.79% │ 279.355 USDT   (27.94%) │     16:54:00 │  -0.13663 │  80.280 USDT    (8.03%) │                           
                           │ Best   │  48/200 │     21 │   10     0    11  47.6 │      2.17% │ 393.965 USDT   (39.40%) │     20:51:00 │  -0.19218 │  81.359 USDT    (8.14%) │                           
                           │ Best   │ 110/200 │     24 │   13     0    11  54.2 │      2.46% │ 438.325 USDT   (43.83%) │     18:32:00 │  -0.23348 │  56.429 USDT    (5.34%) │                           
                           │ Best   │ 147/200 │     14 │   10     0     4  71.4 │      2.72% │ 397.781 USDT   (39.78%) │     22:21:00 │  -0.24057 │  35.874 USDT    (3.32%) │                           
                           │ Best   │ 181/200 │     21 │   12     0     9  57.1 │      3.23% │ 561.717 USDT   (56.17%) │     22:17:00 │  -0.26707 │  56.576 USDT    (5.39%) │                           
                           └────────┴─────────┴────────┴────────────────────────┴────────────┴─────────────────────────┴──────────────┴───────────┴─────────────────────────┘                           
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 200/200 100% • 0:02:46 • 0:00:00
2025-09-18 19:04:29,643 - freqtrade.optimize.hyperopt.hyperopt - INFO - 200 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-18_19-01-31.fthypt'.
2025-09-18 19:04:29,680 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

   181/200:     21 trades. 12/0/9 Wins/Draws/Losses. Avg profit   3.23%. Median profit   2.72%. Total profit 561.71678865 USDT (  56.17%). Avg duration 22:17:00 min. Objective: -0.26707

{"params":{"confirmation_candle":true,"hammer_body_threshold":0.557,"hammer_head_threshold":0.955,"hammer_strength_threshold":0.006,"kinjun_threshold":6,"lookback_period_for_stoploss":7,"stoploss_margin":0.995,"take_profit_multiplier":2,"use_sell_signal_param":true,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231
```

## Backtesting Output
```
2025-09-18 19:04:32,955 - freqtrade - INFO - freqtrade 2025.7
2025-09-18 19:04:33,387 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-18 19:04:33,388 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-18 19:04:35,209 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-18 19:04:35,212 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-18 19:04:35,213 - freqtrade.loggers - INFO - Logfile configured
2025-09-18 19:04:35,213 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-18 19:04:35,214 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-18 19:04:35,214 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-18 19:04:35,214 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-18 19:04:35,215 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-18 19:04:35,223 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-18 19:04:35,224 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-18 19:04:35,225 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-18 19:04:35,225 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-18 19:04:35,226 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-18 19:04:35,226 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-18 19:04:35,228 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-18 19:04:35,248 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-18 19:04:35,249 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 19:04:35,253 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-18 19:04:35,255 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-18 19:04:35,255 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-18 19:04:35,299 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-18 19:04:37,763 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-18 19:04:37,804 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-18 19:04:37,805 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-18 19:04:37,806 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-18 19:04:37,807 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-18 19:04:37,807 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-18 19:04:37,808 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-18 19:04:37,808 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-18 19:04:37,809 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-18 19:04:37,809 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-18 19:04:37,810 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-18 19:04:37,810 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-18 19:04:37,811 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-18 19:04:37,811 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-18 19:04:37,812 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-18 19:04:37,812 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-18 19:04:37,813 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-18 19:04:37,813 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-18 19:04:37,814 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-18 19:04:37,814 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-18 19:04:37,815 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-18 19:04:37,815 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-18 19:04:37,816 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-18 19:04:37,816 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-18 19:04:37,817 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-18 19:04:37,817 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-18 19:04:37,818 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-18 19:04:37,818 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-18 19:04:37,819 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-18 19:04:37,819 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-18 19:04:37,820 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-18 19:04:37,820 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 19:04:37,827 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-18 19:04:37,866 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-18 19:04:37,905 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-18 19:04:37,961 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-18 19:04:38,003 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-18 19:04:38,049 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-18 19:04:38,096 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-18 19:04:38,119 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-18 19:04:38,198 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-18 19:04:38,455 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-18 19:04:38,675 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-18 19:04:38,915 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-18 19:04:39,127 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-18 19:04:40,672 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-18 19:04:40,673 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-18 19:04:40,674 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-18 19:04:40,674 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-18 19:04:40,675 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.557
2025-09-18 19:04:40,675 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.955
2025-09-18 19:04:40,676 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.006
2025-09-18 19:04:40,677 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 6
2025-09-18 19:04:40,677 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 7
2025-09-18 19:04:40,677 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.995
2025-09-18 19:04:40,678 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-18 19:04:40,678 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-18 19:04:40,679 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-18 19:04:40,679 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-18 19:04:40,682 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 19:04:40,694 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-18 19:04:43,577 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 19:04:43,588 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-18 19:04:46,453 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 19:04:46,462 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-18 19:04:49,271 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 19:04:49,283 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-18 19:04:52,130 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-18 19:04:52,161 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-18 19:04:55,017 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-18 19:05:05,337 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-18_19-05-05.meta.json"
Result for strategy IchimokuRebondStrategy
                                              BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      5 │         1.28 │          37.093 │         3.71 │ 1 day, 3:23:00 │    3     0     2  60.0 │
│ BTC/USDT │      6 │         1.24 │          16.048 │          1.6 │ 1 day, 9:00:00 │    2     0     4  33.3 │
│ ETH/USDT │      4 │        -0.57 │         -16.981 │         -1.7 │       14:51:00 │    1     0     3  25.0 │
│ LTC/USDT │      7 │        -1.36 │         -86.221 │        -8.62 │        7:23:00 │    1     0     6  14.3 │
│ XRP/USDT │     13 │        -1.39 │        -132.598 │       -13.26 │ 1 day, 0:45:00 │    2     0    11  15.4 │
│    TOTAL │     35 │        -0.46 │        -182.658 │       -18.27 │       21:56:00 │    9     0    26  25.7 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
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
│     OTHER │      35 │        -0.46 │        -182.658 │       -18.27 │     21:56:00 │    9     0    26  25.7 │
│     TOTAL │      35 │        -0.46 │        -182.658 │       -18.27 │     21:56:00 │    9     0    26  25.7 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │     9 │         4.37 │         264.817 │        26.48 │ 1 day, 21:33:00 │    9     0     0   100 │
│      stop_loss │    26 │        -2.13 │        -447.475 │       -44.75 │        13:46:00 │    0     0    26     0 │
│          TOTAL │    35 │        -0.46 │        -182.658 │       -18.27 │        21:56:00 │    9     0    26  25.7 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                          
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │      9 │         4.37 │         264.817 │        26.48 │ 1 day, 21:33:00 │    9     0     0   100 │
│           │      stop_loss │     26 │        -2.13 │        -447.475 │       -44.75 │        13:46:00 │    0     0    26     0 │
│     TOTAL │                │     35 │        -0.46 │        -182.658 │       -18.27 │        21:56:00 │    9     0    26  25.7 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-11 17:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 35 / 0.03                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 817.342 USDT                   │
│ Absolute profit               │ -182.658 USDT                  │
│ Total profit %                │ -18.27%                        │
│ CAGR %                        │ -5.31%                         │
│ Sortino                       │ -0.84                          │
│ Sharpe                        │ -0.12                          │
│ Calmar                        │ -0.97                          │
│ SQN                           │ -1.44                          │
│ Profit factor                 │ 0.59                           │
│ Expectancy (Ratio)            │ -5.22 (-0.30)                  │
│ Avg. daily profit             │ -0.135 USDT                    │
│ Avg. stake amount             │ 825.434 USDT                   │
│ Total trade volume            │ 57713.052 USDT                 │
│                               │                                │
│ Best Pair                     │ BNB/USDT 3.71%                 │
│ Worst Pair                    │ XRP/USDT -13.26%               │
│ Best trade                    │ BTC/USDT 9.64%                 │
│ Worst trade                   │ XRP/USDT -4.70%                │
│ Best day                      │ 45.706 USDT                    │
│ Worst day                     │ -23.828 USDT                   │
│ Days win/draw/lose            │ 9 / 1095 / 26                  │
│ Min/Max/Avg. Duration Winners │ 0d 04:35 / 4d 18:30 / 1d 21:33 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:20 / 4d 03:55 / 0d 13:46 │
│ Max Consecutive Wins / Loss   │ 3 / 12                         │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 806.231 USDT                   │
│ Max balance                   │ 1099.344 USDT                  │
│ Max % of account underwater   │ 26.66%                         │
│ Absolute Drawdown (Account)   │ 26.66%                         │
│ Absolute Drawdown             │ 293.113 USDT                   │
│ Drawdown high                 │ 99.344 USDT                    │
│ Drawdown low                  │ -193.769 USDT                  │
│ Drawdown Start                │ 2022-07-07 18:40:00            │
│ Drawdown End                  │ 2024-02-16 14:50:00            │
│ Market change                 │ 94.84%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     35 │        -0.46 │        -182.658 │       -18.27 │     21:56:00 │    9     0    26  25.7 │ 293.113 USDT  26.66% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
