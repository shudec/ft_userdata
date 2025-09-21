# Freqtrade Hyperopt Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 3733  
**Timestamp:** 2025-09-19 22:25:58

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell buy roi",
  "random_state": 3733,
  "epochs": 200,
  "hyperopt_timerange": "20170801-20201231",
  "backtest_timerange": "20221101-20241231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 200 --spaces sell buy roi --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20201231 --random-state 3733
```

## Hyperopt Output
```
2025-09-19 20:22:30,538 - freqtrade - INFO - freqtrade 2025.7
2025-09-19 20:22:31,206 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-19 20:22:31,207 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-19 20:22:32,686 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-19 20:22:32,689 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-19 20:22:32,690 - freqtrade.loggers - INFO - Logfile configured
2025-09-19 20:22:32,690 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-19 20:22:32,691 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-19 20:22:32,691 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-19 20:22:32,691 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20201231 ...
2025-09-19 20:22:32,699 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-19 20:22:32,700 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-19 20:22:32,701 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-19 20:22:32,701 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 200 epochs ...
2025-09-19 20:22:32,702 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['sell', 'buy', 'roi']
2025-09-19 20:22:32,702 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-19 20:22:32,703 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-19 20:22:32,703 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 3733
2025-09-19 20:22:32,703 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-19 20:22:32,704 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-19 20:22:32,705 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-19 20:22:32,705 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20201231
2025-09-19 20:22:32,707 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-19 20:22:32,725 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-19 20:22:32,726 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 20:22:32,731 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-19 20:22:32,732 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-19 20:22:32,738 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-19 20:22:32,738 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-19 20:22:32,772 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-19 20:22:35,055 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-19 20:22:35,093 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-19 20:22:35,093 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-19 20:22:35,094 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-19 20:22:35,095 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-19 20:22:35,095 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-19 20:22:35,096 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-19 20:22:35,096 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-19 20:22:35,097 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-19 20:22:35,097 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-19 20:22:35,098 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-19 20:22:35,098 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-19 20:22:35,098 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-19 20:22:35,099 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-19 20:22:35,099 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-19 20:22:35,099 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-19 20:22:35,100 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-19 20:22:35,100 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-19 20:22:35,100 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-19 20:22:35,101 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-19 20:22:35,101 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-19 20:22:35,102 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-19 20:22:35,102 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-19 20:22:35,102 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-19 20:22:35,103 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-19 20:22:35,103 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-19 20:22:35,103 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-19 20:22:35,104 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-19 20:22:35,104 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-19 20:22:35,104 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-19 20:22:35,105 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-19 20:22:35,105 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-19 20:22:35,106 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 20:22:35,111 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-19 20:22:35,146 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-19 20:22:35,148 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-19 20:22:35,149 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.5
2025-09-19 20:22:35,149 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 4
2025-09-19 20:22:35,150 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.55
2025-09-19 20:22:35,151 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.9
2025-09-19 20:22:35,151 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.03
2025-09-19 20:22:35,151 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-19 20:22:35,152 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.001
2025-09-19 20:22:35,153 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-19 20:22:35,153 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 4
2025-09-19 20:22:35,154 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-19 20:22:35,154 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-19 20:22:35,154 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-19 20:22:35,155 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-19 20:22:35,155 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-19 20:22:35,165 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-19 20:22:35,166 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 3733
2025-09-19 20:22:35,167 - freqtrade.optimize.hyperopt.hyperopt_interface - INFO - Min roi table: {0: 0.069, 120: 0.046, 240: 0.023, 360: 0}
2025-09-19 20:22:35,168 - freqtrade.optimize.hyperopt.hyperopt_interface - INFO - Max roi table: {0: 0.711, 480: 0.252, 1200: 0.092, 2640: 0}
2025-09-19 20:22:35,207 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-19 20:22:35,260 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-19 20:22:35,269 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-19 20:22:35,306 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-19 20:22:35,353 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-19 20:22:35,397 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-19 20:22:35,408 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-19 20:22:35,429 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2020-12-31 00:00:00 (1231 days).
2025-09-19 20:22:36,580 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-19 20:22:36,581 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-19 20:22:36,589 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-19 20:22:39,015 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-19 20:22:39,022 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-19 20:22:41,460 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-19 20:22:41,467 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-19 20:22:43,653 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-19 20:22:43,662 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-19 20:22:45,553 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-19 20:22:45,562 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-19 20:22:47,827 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2020-12-31 00:00:00 (1231 days)..
2025-09-19 20:22:48,136 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 20 CPU cores. Let's make them scream!
2025-09-19 20:22:48,137 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-19 20:22:48,138 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-19 20:22:48,139] A new study created in memory with name: no-name-84549cd0-7974-47f6-89c5-37dae32095b3
2025-09-19 20:22:48,192 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                         ┏━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓                         
                         ┃ Best   ┃   Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃     Avg duration ┃ Objective ┃     Max Drawdown (Acct) ┃                         
                         ┡━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩                         
                         │ * Best │   1/200 │     10 │    3     0     7  30.0 │     -1.17% │ -67.662 USDT   (-6.77%) │         16:42:00 │   0.06485 │  67.662 USDT    (6.77%) │                         
                         │ * Best │   2/200 │     20 │    8    10     2  40.0 │      0.45% │  -9.622 USDT   (-0.96%) │ 5 days, 11:48:00 │   0.02044 │  20.637 USDT    (2.06%) │                         
                         │ * Best │   3/200 │     59 │   25     2    32  42.4 │      0.03% │  19.148 USDT    (1.91%) │          6:43:00 │  -0.01462 │ 167.100 USDT   (14.53%) │                         
                         │ * Best │  12/200 │     14 │    8     0     6  57.1 │      1.17% │ 143.347 USDT   (14.33%) │         10:56:00 │  -0.08345 │  38.265 USDT    (3.56%) │                         
                         │ * Best │  15/200 │     21 │   11     0    10  52.4 │      0.78% │ 139.490 USDT   (13.95%) │          6:26:00 │  -0.09951 │  43.612 USDT    (4.36%) │                         
                         │ Best   │  39/200 │     22 │    9     0    13  40.9 │      0.44% │  26.894 USDT    (2.69%) │         15:35:00 │  -0.10571 │   8.319 USDT    (0.83%) │                         
                         │ Best   │ 107/200 │     21 │   11     0    10  52.4 │      1.23% │ 218.356 USDT   (21.84%) │         12:54:00 │  -0.11345 │  64.802 USDT    (6.48%) │                         
                         │ Best   │ 124/200 │     30 │   13     0    17  43.3 │      0.84% │ 235.790 USDT   (23.58%) │          9:56:00 │  -0.12232 │  65.777 USDT    (6.40%) │                         
                         │ Best   │ 135/200 │     22 │   12     0    10  54.5 │      1.38% │ 245.931 USDT   (24.59%) │          7:52:00 │  -0.14883 │  45.305 USDT    (4.36%) │                         
                         └────────┴─────────┴────────┴────────────────────────┴────────────┴─────────────────────────┴──────────────────┴───────────┴─────────────────────────┘                         
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 200/200 100% • 0:03:08 • 0:00:00
2025-09-19 20:25:56,687 - freqtrade.optimize.hyperopt.hyperopt - INFO - 200 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-19_20-22-32.fthypt'.
2025-09-19 20:25:56,726 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

   135/200:     22 trades. 12/0/10 Wins/Draws/Losses. Avg profit   1.38%. Median profit   2.09%. Total profit 245.93146793 USDT (  24.59%). Avg duration 7:52:00 min. Objective: -0.14883

{"params":{"confirmation_candle":true,"engulfing_size_threshold":1.1,"flat_kinjun_threshold":16,"hammer_body_threshold":0.523,"hammer_head_threshold":0.85,"hammer_strength_threshold":0.022,"kinjun_proximity_threshold":0.0,"tenkan_proximity_threshold":0.001,"kinjun_threshold":0.999,"lookback_period_for_stoploss":6,"stoploss_margin":0.992,"take_profit_multiplier":1.5,"use_sell_signal_param":true,"use_custom_stoploss_param":true},"minimal_roi":{"0":0.49,"456":0.214,"795":0.085,"1564":0},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Hyperopt Results
```json
{
  "timestamp": "2025-09-19T22:25:58.823625",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 3733,
  "wins_draws_losses": "12/0/10",
  "avg_profit_pct": 1.38,
  "median_profit_pct": 2.09,
  "total_profit_usdt": 245.93146793,
  "avg_duration": "7:52:00",
  "objective": -0.14883,
  "avg_profit_per_day": 4.2102
}
```
