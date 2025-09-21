# Freqtrade Hyperopt Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 9153  
**Timestamp:** 2025-09-19 21:59:53

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy",
  "random_state": 9153,
  "epochs": 200,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 200 --spaces buy --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 9153
```

## Hyperopt Output
```
2025-09-19 19:57:03,118 - freqtrade - INFO - freqtrade 2025.7
2025-09-19 19:57:03,795 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-19 19:57:03,796 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-19 19:57:05,197 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-19 19:57:05,200 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-19 19:57:05,200 - freqtrade.loggers - INFO - Logfile configured
2025-09-19 19:57:05,201 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-19 19:57:05,201 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-19 19:57:05,202 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-19 19:57:05,202 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-19 19:57:05,211 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-19 19:57:05,212 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-19 19:57:05,213 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-19 19:57:05,213 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 200 epochs ...
2025-09-19 19:57:05,214 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy']
2025-09-19 19:57:05,215 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-19 19:57:05,216 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-19 19:57:05,216 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 9153
2025-09-19 19:57:05,217 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-19 19:57:05,217 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-19 19:57:05,218 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-19 19:57:05,218 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-19 19:57:05,220 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-19 19:57:05,240 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-19 19:57:05,241 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 19:57:05,244 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-19 19:57:05,246 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-19 19:57:05,251 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-19 19:57:05,251 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-19 19:57:05,288 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-19 19:57:07,767 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-19 19:57:07,804 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-19 19:57:07,805 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-19 19:57:07,806 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-19 19:57:07,806 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-19 19:57:07,807 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-19 19:57:07,807 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-19 19:57:07,808 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-19 19:57:07,808 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-19 19:57:07,808 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-19 19:57:07,809 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-19 19:57:07,809 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-19 19:57:07,810 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-19 19:57:07,810 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-19 19:57:07,810 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-19 19:57:07,811 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-19 19:57:07,811 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-19 19:57:07,812 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-19 19:57:07,812 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-19 19:57:07,812 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-19 19:57:07,813 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-19 19:57:07,813 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-19 19:57:07,813 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-19 19:57:07,814 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-19 19:57:07,814 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-19 19:57:07,814 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-19 19:57:07,815 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-19 19:57:07,815 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-19 19:57:07,816 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-19 19:57:07,816 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-19 19:57:07,816 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-19 19:57:07,817 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-19 19:57:07,824 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-19 19:57:07,862 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-19 19:57:07,864 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = True
2025-09-19 19:57:07,865 - freqtrade.strategy.hyper - INFO - Strategy Parameter: engulfing_size_threshold = 1.2
2025-09-19 19:57:07,866 - freqtrade.strategy.hyper - INFO - Strategy Parameter: flat_kinjun_threshold = 7
2025-09-19 19:57:07,866 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.41
2025-09-19 19:57:07,866 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.967
2025-09-19 19:57:07,867 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.012
2025-09-19 19:57:07,867 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_proximity_threshold = 0.001
2025-09-19 19:57:07,868 - freqtrade.strategy.hyper - INFO - Strategy Parameter: tenkan_proximity_threshold = 0.001
2025-09-19 19:57:07,868 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1.0
2025-09-19 19:57:07,869 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 2
2025-09-19 19:57:07,869 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-09-19 19:57:07,870 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 3
2025-09-19 19:57:07,870 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-19 19:57:07,870 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-19 19:57:07,871 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-19 19:57:07,880 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-19 19:57:07,881 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 9153
2025-09-19 19:57:07,923 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-19 19:57:07,975 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-19 19:57:07,984 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-19 19:57:08,015 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-19 19:57:08,055 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-19 19:57:08,096 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-19 19:57:08,104 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-19 19:57:08,121 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-19 19:57:08,902 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-19 19:57:08,904 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 19:57:08,914 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-19 19:57:10,628 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 19:57:10,635 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-19 19:57:12,378 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 19:57:12,389 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-19 19:57:13,856 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 19:57:13,866 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-19 19:57:15,109 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-19 19:57:15,116 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-19 19:57:16,684 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-19 19:57:16,983 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 20 CPU cores. Let's make them scream!
2025-09-19 19:57:16,984 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-19 19:57:16,985 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-19 19:57:16,986] A new study created in memory with name: no-name-d6ca934e-3521-4ff5-bae4-8f524c4a59d8
2025-09-19 19:57:17,035 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                           Hyperopt results                                                                                             
                           ┏━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓                            
                           ┃ Best   ┃   Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃ Avg duration ┃ Objective ┃    Max Drawdown (Acct) ┃                            
                           ┡━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩                            
                           │ * Best │   1/200 │     10 │    3     0     7  30.0 │      0.50% │  48.366 USDT    (4.84%) │      2:54:00 │  -0.04703 │ 31.939 USDT    (3.08%) │                            
                           │ * Best │  10/200 │      7 │    3     0     4  42.9 │      1.06% │  73.587 USDT    (7.36%) │      4:09:00 │  -0.06347 │ 32.534 USDT    (3.08%) │                            
                           │ * Best │  18/200 │     14 │    4     0    10  28.6 │      0.89% │  89.143 USDT    (8.91%) │      4:09:00 │  -0.07376 │ 46.430 USDT    (4.24%) │                            
                           │ * Best │  28/200 │      9 │    4     0     5  44.4 │      1.80% │ 130.313 USDT   (13.03%) │      5:33:00 │  -0.09299 │ 47.675 USDT    (4.24%) │                            
                           │ Best   │ 126/200 │      8 │    4     0     4  50.0 │      2.24% │ 143.972 USDT   (14.40%) │      5:52:00 │  -0.10185 │ 34.666 USDT    (3.08%) │                            
                           └────────┴─────────┴────────┴────────────────────────┴────────────┴─────────────────────────┴──────────────┴───────────┴────────────────────────┘                            
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 200/200 100% • 0:02:33 • 0:00:00
2025-09-19 19:59:51,165 - freqtrade.optimize.hyperopt.hyperopt - INFO - 200 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-19_19-57-05.fthypt'.
2025-09-19 19:59:51,207 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

   126/200:      8 trades. 4/0/4 Wins/Draws/Losses. Avg profit   2.24%. Median profit   0.78%. Total profit 143.97212871 USDT (  14.40%). Avg duration 5:52:00 min. Objective: -0.10185

{"params":{"confirmation_candle":true,"engulfing_size_threshold":1.5,"flat_kinjun_threshold":5,"hammer_body_threshold":0.879,"hammer_head_threshold":0.765,"hammer_strength_threshold":0.03,"kinjun_proximity_threshold":0.0,"tenkan_proximity_threshold":0.001,"kinjun_threshold":1.0,"lookback_period_for_stoploss":2,"stoploss_margin":0.999,"take_profit_multiplier":3,"use_custom_stoploss_param":true,"use_sell_signal_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Hyperopt Results
```json
{
  "timestamp": "2025-09-19T21:59:53.221617",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 9153,
  "wins_draws_losses": "4/0/4",
  "avg_profit_pct": 2.24,
  "median_profit_pct": 0.78,
  "total_profit_usdt": 143.97212871,
  "avg_duration": "5:52:00",
  "objective": -0.10185,
  "avg_profit_per_day": 9.1636
}
```
