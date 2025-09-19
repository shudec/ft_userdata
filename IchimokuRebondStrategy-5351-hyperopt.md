# Freqtrade Hyperopt Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 5351  
**Timestamp:** 2025-09-19 11:43:24

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 5351,
  "epochs": 200,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 200 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 5351
```

## Hyperopt Output
```
2025-09-19 09:39:54,583 - freqtrade - INFO - freqtrade 2025.8
2025-09-19 09:39:55,270 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-19 09:39:56,851 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-19 09:39:56,858 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-19 09:39:56,859 - freqtrade.loggers - INFO - Logfile configured
2025-09-19 09:39:56,859 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-19 09:39:56,860 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-19 09:39:56,860 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-19 09:39:56,861 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-19 09:39:57,167 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-19 09:39:57,169 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-19 09:39:57,170 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-19 09:39:57,170 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 200 epochs ...
2025-09-19 09:39:57,170 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-19 09:39:57,171 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-19 09:39:57,171 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-19 09:39:57,171 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 5351
2025-09-19 09:39:57,172 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-19 09:39:57,172 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-19 09:39:57,172 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-19 09:39:57,173 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-19 09:39:57,174 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-19 09:39:57,184 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-19 09:39:57,185 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 09:39:57,187 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-19 09:39:57,194 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-19 09:39:57,200 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-19 09:39:57,200 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-19 09:39:57,219 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-19 09:40:01,168 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-19 09:40:01,269 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-19 09:40:01,271 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-19 09:40:01,275 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-19 09:40:01,276 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-19 09:40:01,276 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-19 09:40:01,276 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-19 09:40:01,277 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-19 09:40:01,277 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-19 09:40:01,278 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-19 09:40:01,278 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-19 09:40:01,278 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-19 09:40:01,279 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-19 09:40:01,280 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-19 09:40:01,280 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-19 09:40:01,281 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-19 09:40:01,282 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-19 09:40:01,282 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-19 09:40:01,283 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-19 09:40:01,283 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-19 09:40:01,284 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-19 09:40:01,284 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-19 09:40:01,285 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-19 09:40:01,285 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-19 09:40:01,286 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-19 09:40:01,286 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-19 09:40:01,286 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-19 09:40:01,287 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-19 09:40:01,287 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-19 09:40:01,288 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-19 09:40:01,288 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-19 09:40:01,289 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-19 09:40:01,289 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 09:40:01,307 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-19 09:40:01,330 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-19 09:40:01,332 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-19 09:40:01,332 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): engulfing_size_threshold = 2
2025-09-19 09:40:01,333 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 4
2025-09-19 09:40:01,333 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.796
2025-09-19 09:40:01,333 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.971
2025-09-19 09:40:01,334 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.013
2025-09-19 09:40:01,334 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): kinjun_proximity_threshold = 0.01
2025-09-19 09:40:01,335 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 10
2025-09-19 09:40:01,335 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-09-19 09:40:01,335 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.995
2025-09-19 09:40:01,336 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-19 09:40:01,336 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-19 09:40:01,336 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-19 09:40:01,337 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-19 09:40:01,353 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-19 09:40:01,353 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 5351
2025-09-19 09:40:01,403 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-19 09:40:01,472 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-19 09:40:01,480 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-19 09:40:01,528 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-19 09:40:01,577 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-19 09:40:01,645 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-19 09:40:01,656 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-19 09:40:01,669 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-19 09:40:02,332 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-19 09:40:02,335 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 09:40:02,358 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-19 09:40:04,458 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 09:40:04,475 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-19 09:40:06,439 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 09:40:06,453 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-19 09:40:08,019 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 09:40:08,041 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-19 09:40:09,669 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 09:40:09,684 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-19 09:40:11,640 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-19 09:40:12,105 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 16 CPU cores. Let's make them scream!
2025-09-19 09:40:12,106 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-19 09:40:12,107 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-19 09:40:12,107] A new study created in memory with name: no-name-795b7f5d-35eb-44ae-b6be-b0abd5d6d291
2025-09-19 09:40:12,161 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                         ┏━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓                         
                         ┃ Best   ┃   Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃      Avg duration ┃ Objective ┃    Max Drawdown (Acct) ┃                         
                         ┡━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩                         
                         │ * Best │   1/200 │      5 │    0     0     5     0 │     -1.53% │ -71.773 USDT   (-7.18%) │          17:00:00 │   0.43298 │ 71.773 USDT    (7.18%) │                         
                         │ * Best │   2/200 │      5 │    0     0     5     0 │     -1.36% │ -44.611 USDT   (-4.46%) │          13:24:00 │   0.14488 │ 44.611 USDT    (4.46%) │                         
                         │ * Best │   6/200 │      7 │    2     0     5  28.6 │      0.78% │ -18.230 USDT   (-1.82%) │   1 day, 12:09:00 │   0.01670 │ 84.647 USDT    (8.08%) │                         
                         │ * Best │  16/200 │     13 │    4     0     9  30.8 │      0.29% │  20.747 USDT    (2.07%) │          14:05:00 │  -0.02162 │ 81.208 USDT    (7.84%) │                         
                         │ Best   │  75/200 │     10 │    4     0     6  40.0 │      5.09% │  38.149 USDT    (3.81%) │  25 days, 5:24:00 │  -0.02878 │ 77.318 USDT    (6.93%) │                         
                         │ Best   │ 129/200 │      7 │    4     0     3  57.1 │      1.04% │  67.272 USDT    (6.73%) │          10:51:00 │  -0.07480 │ 34.744 USDT    (3.35%) │                         
                         │ Best   │ 166/200 │      6 │    4     0     2  66.7 │     18.82% │ 114.919 USDT   (11.49%) │ 31 days, 19:50:00 │  -0.08379 │ 46.583 USDT    (4.01%) │                         
                         └────────┴─────────┴────────┴────────────────────────┴────────────┴─────────────────────────┴───────────────────┴───────────┴────────────────────────┘                         
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 200/200 100% • 0:03:09 • 0:00:00
2025-09-19 09:43:21,994 - freqtrade.optimize.hyperopt.hyperopt - INFO - 200 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-19_09-39-57.fthypt'.
2025-09-19 09:43:22,163 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

   166/200:      6 trades. 4/0/2 Wins/Draws/Losses. Avg profit  18.82%. Median profit  19.47%. Total profit 114.91878729 USDT (  11.49%). Avg duration 31 days, 19:50:00 min. Objective: -0.08379

{"params":{"confirmation_candle":false,"engulfing_size_threshold":2.5,"flat_kinjun_threshold":3,"hammer_body_threshold":0.962,"hammer_head_threshold":0.064,"hammer_strength_threshold":0.035,"kinjun_proximity_threshold":0.019,"kinjun_threshold":9,"lookback_period_for_stoploss":0,"stoploss_margin":0.999,"take_profit_multiplier":2,"use_sell_signal_param":true,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Hyperopt Results
```json
{
  "timestamp": "2025-09-19T11:43:24.699619",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 5351,
  "wins_draws_losses": "4/0/2",
  "avg_profit_pct": 18.82,
  "median_profit_pct": 19.47,
  "total_profit_usdt": 114.91878729,
  "avg_duration": "31 days, 19:50:00",
  "objective": -0.08379,
  "avg_profit_per_day": 0.5913
}
```
