# Freqtrade Hyperopt Log

**Strategy:** IchimokuRebondStrategy  
**Random State:** 6098  
**Timestamp:** 2025-09-18 10:37:11

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 6098,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 6098
```

## Hyperopt Output
```
2025-09-18 08:35:18,266 - freqtrade - INFO - freqtrade 2025.8
2025-09-18 08:35:19,261 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-18 08:35:21,607 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-18 08:35:21,615 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-18 08:35:21,615 - freqtrade.loggers - INFO - Logfile configured
2025-09-18 08:35:21,616 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-18 08:35:21,616 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-18 08:35:21,617 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-18 08:35:21,618 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-18 08:35:22,027 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-18 08:35:22,031 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-18 08:35:22,032 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-18 08:35:22,032 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 100 epochs ...
2025-09-18 08:35:22,033 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-18 08:35:22,033 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-18 08:35:22,034 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-18 08:35:22,035 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 6098
2025-09-18 08:35:22,036 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-18 08:35:22,037 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-18 08:35:22,039 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-18 08:35:22,041 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-18 08:35:22,044 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-18 08:35:22,067 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-18 08:35:22,068 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 08:35:22,075 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-18 08:35:22,085 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-18 08:35:22,092 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-18 08:35:22,092 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-18 08:35:22,133 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-18 08:35:26,168 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-18 08:35:26,299 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-18 08:35:26,302 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-18 08:35:26,306 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-18 08:35:26,307 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-18 08:35:26,307 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-18 08:35:26,308 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-18 08:35:26,309 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-18 08:35:26,310 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-18 08:35:26,310 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-18 08:35:26,310 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-18 08:35:26,311 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-18 08:35:26,311 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-18 08:35:26,311 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-18 08:35:26,312 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-18 08:35:26,312 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-18 08:35:26,312 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-18 08:35:26,313 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-18 08:35:26,313 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-18 08:35:26,313 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-18 08:35:26,314 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-18 08:35:26,314 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-18 08:35:26,315 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-18 08:35:26,315 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-18 08:35:26,315 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-18 08:35:26,316 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-18 08:35:26,316 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-18 08:35:26,316 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-18 08:35:26,317 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-18 08:35:26,317 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-18 08:35:26,317 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-18 08:35:26,318 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-18 08:35:26,318 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-18 08:35:26,352 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-18 08:35:26,385 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-18 08:35:26,387 - freqtrade.strategy.hyper - INFO - Strategy Parameter: confirmation_candle = False
2025-09-18 08:35:26,388 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.642
2025-09-18 08:35:26,388 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.265
2025-09-18 08:35:26,389 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.009
2025-09-18 08:35:26,389 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 6
2025-09-18 08:35:26,390 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 0
2025-09-18 08:35:26,391 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.994
2025-09-18 08:35:26,391 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2.5
2025-09-18 08:35:26,392 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-18 08:35:26,393 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-18 08:35:26,394 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-18 08:35:26,426 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-18 08:35:26,427 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 6098
2025-09-18 08:35:26,538 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-18 08:35:26,633 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-18 08:35:26,643 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-18 08:35:26,697 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-18 08:35:26,757 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-18 08:35:26,820 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-18 08:35:26,831 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-18 08:35:26,863 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-18 08:35:27,580 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-18 08:35:27,583 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 08:35:27,600 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-18 08:35:29,278 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 08:35:29,294 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-18 08:35:30,584 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 08:35:30,599 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-18 08:35:31,748 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 08:35:31,764 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-18 08:35:32,654 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-18 08:35:32,670 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-18 08:35:33,936 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-18 08:35:34,392 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 16 CPU cores. Let's make them scream!
2025-09-18 08:35:34,393 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-18 08:35:34,394 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-18 08:35:34,394] A new study created in memory with name: no-name-3e7aaad6-239a-4ec9-a723-c7a23cc7b29a
2025-09-18 08:35:34,455 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                           ┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓                           
                           ┃ Best   ┃  Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃   Avg duration ┃ Objective ┃    Max Drawdown (Acct) ┃                           
                           ┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩                           
                           │ * Best │  1/100 │     19 │    8     0    11  42.1 │      2.45% │ 373.425 USDT   (37.34%) │ 1 day, 0:16:00 │  -0.15231 │ 83.398 USDT    (5.85%) │                           
                           │ Best   │ 79/100 │     16 │   10     0     6  62.5 │      3.72% │ 471.772 USDT   (47.18%) │       23:08:00 │  -0.23674 │ 44.115 USDT    (4.10%) │                           
                           └────────┴────────┴────────┴────────────────────────┴────────────┴─────────────────────────┴────────────────┴───────────┴────────────────────────┘                           
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100/100 100% • 0:01:33 • 0:00:00
2025-09-18 08:37:08,135 - freqtrade.optimize.hyperopt.hyperopt - INFO - 100 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-18_08-35-22.fthypt'.
2025-09-18 08:37:08,335 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

    79/100:     16 trades. 10/0/6 Wins/Draws/Losses. Avg profit   3.72%. Median profit   4.64%. Total profit 471.77210694 USDT (  47.18%). Avg duration 23:08:00 min. Objective: -0.23674

{"params":{"confirmation_candle":true,"hammer_body_threshold":0.491,"hammer_head_threshold":0.909,"hammer_strength_threshold":0.009,"kinjun_threshold":2,"lookback_period_for_stoploss":4,"stoploss_margin":0.991,"take_profit_multiplier":1.5,"use_sell_signal_param":false,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Hyperopt Results
```json
{
  "timestamp": "2025-09-18T10:37:11.010985",
  "strategy": "IchimokuRebondStrategy",
  "random_state": 6098,
  "wins_draws_losses": "10/0/6",
  "avg_profit_pct": 3.72,
  "median_profit_pct": 4.64,
  "total_profit_usdt": 471.77210694,
  "avg_duration": "23:08:00",
  "objective": -0.23674,
  "avg_profit_per_day": 3.8594
}
```
