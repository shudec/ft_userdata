# Freqtrade Hyperopt Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 5881  
**Timestamp:** 2025-09-21 22:20:58

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "OnlyProfitHyperOptLoss",
  "spaces": "sell buy",
  "random_state": 5881,
  "epochs": 200,
  "hyperopt_timerange": "20170801-20201231",
  "backtest_timerange": "20210101-20241231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss OnlyProfitHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 200 --spaces sell buy --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20201231 --random-state 5881
```

## Hyperopt Output
```
2025-09-21 20:17:30,543 - freqtrade - INFO - freqtrade 2025.7
2025-09-21 20:17:31,274 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-21 20:17:31,275 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-21 20:17:33,162 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-21 20:17:33,165 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-21 20:17:33,166 - freqtrade.loggers - INFO - Logfile configured
2025-09-21 20:17:33,166 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-21 20:17:33,167 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-21 20:17:33,167 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-21 20:17:33,167 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20201231 ...
2025-09-21 20:17:33,176 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-21 20:17:33,177 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-21 20:17:33,177 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-21 20:17:33,177 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 200 epochs ...
2025-09-21 20:17:33,178 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['sell', 'buy']
2025-09-21 20:17:33,178 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-21 20:17:33,179 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-21 20:17:33,179 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 5881
2025-09-21 20:17:33,179 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-21 20:17:33,180 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: OnlyProfitHyperOptLoss
2025-09-21 20:17:33,180 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-21 20:17:33,181 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20201231
2025-09-21 20:17:33,182 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-21 20:17:33,201 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-21 20:17:33,202 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 20:17:33,206 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-21 20:17:33,207 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-21 20:17:33,215 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-21 20:17:33,216 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-21 20:17:33,250 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-21 20:17:35,896 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-21 20:17:35,933 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-21 20:17:35,933 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-21 20:17:35,934 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-21 20:17:35,935 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-21 20:17:35,935 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-21 20:17:35,936 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-21 20:17:35,937 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-21 20:17:35,937 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-21 20:17:35,938 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.672, '469': 0.23, '668': 0.076, '1337': 0}
2025-09-21 20:17:35,938 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-21 20:17:35,939 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-21 20:17:35,939 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-21 20:17:35,940 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-21 20:17:35,940 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-21 20:17:35,941 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-21 20:17:35,941 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-21 20:17:35,941 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-21 20:17:35,942 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-21 20:17:35,942 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-21 20:17:35,943 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-21 20:17:35,943 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-21 20:17:35,943 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-21 20:17:35,944 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-21 20:17:35,945 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-21 20:17:35,945 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-21 20:17:35,945 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-21 20:17:35,946 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-21 20:17:35,946 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-21 20:17:35,947 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-21 20:17:35,947 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-21 20:17:35,947 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-21 20:17:35,948 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-21 20:17:35,954 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-21 20:17:35,990 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-21 20:17:35,992 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-21 20:17:35,993 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 2.5
2025-09-21 20:17:35,994 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 5
2025-09-21 20:17:35,994 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.974
2025-09-21 20:17:35,994 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.293
2025-09-21 20:17:35,995 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.01
2025-09-21 20:17:35,996 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-21 20:17:35,996 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.0
2025-09-21 20:17:35,997 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0.999
2025-09-21 20:17:35,997 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 0
2025-09-21 20:17:35,998 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.996
2025-09-21 20:17:35,998 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-21 20:17:35,999 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-21 20:17:35,999 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-21 20:17:35,999 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-21 20:17:36,012 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss OnlyProfitHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_onlyprofit.py'...
2025-09-21 20:17:36,012 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 5881
2025-09-21 20:17:36,046 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-21 20:17:36,107 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-21 20:17:36,120 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-21 20:17:36,162 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-21 20:17:36,214 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-21 20:17:36,265 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-21 20:17:36,283 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-21 20:17:36,305 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2020-12-31 00:00:00 (1231 days).
2025-09-21 20:17:37,551 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-21 20:17:37,553 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 20:17:37,560 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-21 20:17:39,569 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 20:17:39,579 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-21 20:17:41,848 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 20:17:41,855 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-21 20:17:43,631 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 20:17:43,641 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-21 20:17:45,184 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2020-12-31 00:00:00
2025-09-21 20:17:45,192 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-21 20:17:47,008 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2020-12-31 00:00:00 (1231 days)..
2025-09-21 20:17:47,317 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 20 CPU cores. Let's make them scream!
2025-09-21 20:17:47,318 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-21 20:17:47,319 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-21 20:17:47,320] A new study created in memory with name: no-name-636bf36b-e47d-42fb-b423-4799229e3599
2025-09-21 20:17:47,371 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                           ┏━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓                           
                           ┃ Best   ┃   Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃ Avg duration ┃  Objective ┃    Max Drawdown (Acct) ┃                           
                           ┡━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩                           
                           │ * Best │   1/200 │     13 │    4     1     8  30.8 │     -0.58% │ -14.779 USDT   (-1.48%) │     11:51:00 │   14.77876 │ 57.849 USDT    (5.78%) │                           
                           │ * Best │   2/200 │     31 │    8     0    23  25.8 │     -0.40% │  -4.743 USDT   (-0.47%) │     12:41:00 │    4.74303 │ 19.480 USDT    (1.94%) │                           
                           │ * Best │   6/200 │      3 │    2     1     0   100 │      2.27% │  68.637 USDT    (6.86%) │     16:40:00 │  -68.63678 │                     -- │                           
                           │ * Best │  16/200 │     21 │   10     2     9  47.6 │      0.69% │  80.917 USDT    (8.09%) │     15:23:00 │  -80.91717 │ 60.240 USDT    (5.60%) │                           
                           │ * Best │  18/200 │     27 │    9     1    17  33.3 │      0.71% │ 141.774 USDT   (14.18%) │     11:18:00 │ -141.77439 │ 98.437 USDT    (8.71%) │                           
                           │ Best   │  58/200 │     20 │    8     1    11  40.0 │      1.02% │ 170.594 USDT   (17.06%) │      9:12:00 │ -170.59368 │ 81.472 USDT    (7.33%) │                           
                           │ Best   │ 110/200 │     22 │    9     1    12  40.9 │      1.10% │ 200.785 USDT   (20.08%) │     12:19:00 │ -200.78490 │ 79.119 USDT    (6.89%) │                           
                           │ Best   │ 199/200 │     20 │    9     1    10  45.0 │      1.28% │ 219.497 USDT   (21.95%) │     13:09:00 │ -219.49680 │ 88.179 USDT    (7.93%) │                           
                           └────────┴─────────┴────────┴────────────────────────┴────────────┴─────────────────────────┴──────────────┴────────────┴────────────────────────┘                           
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 200/200 100% • 0:03:08 • 0:00:00
2025-09-21 20:20:56,481 - freqtrade.optimize.hyperopt.hyperopt - INFO - 200 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-21_20-17-33.fthypt'.
2025-09-21 20:20:56,520 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

   199/200:     20 trades. 9/1/10 Wins/Draws/Losses. Avg profit   1.28%. Median profit  -0.92%. Total profit 219.49680173 USDT (  21.95%). Avg duration 13:09:00 min. Objective: -219.49680

{"params":{"confirmation_candle":false,"engulfing_size_threshold":1.1,"flat_kinjun_threshold":18,"hammer_body_threshold":0.913,"hammer_head_threshold":0.781,"hammer_strength_threshold":0.044,"kinjun_proximity_threshold":0.0,"tenkan_proximity_threshold":0.001,"kinjun_threshold":0.995,"lookback_period_for_stoploss":2,"stoploss_margin":0.99,"take_profit_multiplier":3,"use_sell_signal_param":false,"use_custom_stoploss_param":true},"minimal_roi":{"0":0.672,"469":0.23,"668":0.076,"1337":0},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Hyperopt Results
```json
{
  "timestamp": "2025-09-21T22:20:58.509836",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 5881,
  "wins_draws_losses": "9/1/10",
  "avg_profit_pct": 1.28,
  "median_profit_pct": -0.92,
  "total_profit_usdt": 219.49680173,
  "avg_duration": "13:09:00",
  "objective": -219.4968,
  "avg_profit_per_day": 2.3361
}
```
