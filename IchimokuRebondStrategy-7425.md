# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 1163 / 0.86, Median: -0.61%, Total profit: -16.37%, Sortino: -2.14, Sharpe: -0.71, Calmar: -1.07, Drawdown: 0%)

---
            
**Strategy:** IchimokuRebondStrategy  
**Random State:** 7425  
**Timestamp:** 2025-09-17 11:38:25

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 7425,
  "epochs": 500,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 500 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 7425
```

## Hyperopt Output
```
2025-09-17 09:17:19,199 - freqtrade - INFO - freqtrade 2025.8
2025-09-17 09:17:19,736 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-17 09:17:21,018 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-17 09:17:21,025 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-17 09:17:21,025 - freqtrade.loggers - INFO - Logfile configured
2025-09-17 09:17:21,025 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-17 09:17:21,026 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-17 09:17:21,026 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-17 09:17:21,026 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-17 09:17:21,406 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-17 09:17:21,408 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-17 09:17:21,408 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-17 09:17:21,408 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 500 epochs ...
2025-09-17 09:17:21,409 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-17 09:17:21,409 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-17 09:17:21,410 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-17 09:17:21,410 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 7425
2025-09-17 09:17:21,410 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-17 09:17:21,411 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-17 09:17:21,411 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-17 09:17:21,411 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-17 09:17:21,412 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-17 09:17:21,423 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-17 09:17:21,424 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 09:17:21,426 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-17 09:17:21,433 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-17 09:17:21,440 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-17 09:17:21,440 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-17 09:17:21,462 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-17 09:17:25,351 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-17 09:17:25,434 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-17 09:17:25,436 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-17 09:17:25,440 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-17 09:17:25,440 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-17 09:17:25,441 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-17 09:17:25,442 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-17 09:17:25,442 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-17 09:17:25,443 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-17 09:17:25,443 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-17 09:17:25,443 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-17 09:17:25,444 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-17 09:17:25,444 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-17 09:17:25,444 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-17 09:17:25,445 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-17 09:17:25,445 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-17 09:17:25,445 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-17 09:17:25,446 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-17 09:17:25,446 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-17 09:17:25,446 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-17 09:17:25,447 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-17 09:17:25,447 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-17 09:17:25,447 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-17 09:17:25,448 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-17 09:17:25,448 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-17 09:17:25,448 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-17 09:17:25,449 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-17 09:17:25,449 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-17 09:17:25,449 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-17 09:17:25,450 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-17 09:17:25,450 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-17 09:17:25,451 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-17 09:17:25,451 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 09:17:25,467 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-17 09:17:25,489 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-17 09:17:25,490 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_spanA = False
2025-09-17 09:17:25,490 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_spanB = False
2025-09-17 09:17:25,491 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_tenkan = False
2025-09-17 09:17:25,491 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_sma200 = False
2025-09-17 09:17:25,492 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_spanA_sup_spanB = False
2025-09-17 09:17:25,493 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_span_futur = False
2025-09-17 09:17:25,493 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 3.551
2025-09-17 09:17:25,494 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.365
2025-09-17 09:17:25,494 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 50
2025-09-17 09:17:25,495 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 20
2025-09-17 09:17:25,495 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1.0
2025-09-17 09:17:25,495 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0
2025-09-17 09:17:25,496 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 0
2025-09-17 09:17:25,496 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 1.0
2025-09-17 09:17:25,497 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2.5
2025-09-17 09:17:25,497 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-17 09:17:25,498 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_sell_signal_param = True
2025-09-17 09:17:25,498 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-17 09:17:25,514 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-17 09:17:25,515 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 7425
2025-09-17 09:17:25,568 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-17 09:17:25,631 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-17 09:17:25,638 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-17 09:17:25,683 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-17 09:17:25,733 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-17 09:17:25,786 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-17 09:17:25,793 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-17 09:17:25,802 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-17 09:17:26,349 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-17 09:17:26,351 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 09:17:26,367 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-17 09:17:27,656 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 09:17:27,687 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-17 09:17:28,969 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 09:17:28,989 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-17 09:17:30,173 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 09:17:30,195 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-17 09:17:31,204 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 09:17:31,223 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-17 09:17:32,598 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-17 09:17:33,060 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 16 CPU cores. Let's make them scream!
2025-09-17 09:17:33,061 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-17 09:17:33,062 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-17 09:17:33,063] A new study created in memory with name: no-name-6078bb60-6021-40aa-bb77-fa315b74c8f2
2025-09-17 09:17:33,110 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                         ┏━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓                         
                         ┃ Best   ┃   Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                   Profit ┃   Avg duration ┃ Objective ┃      Max Drawdown (Acct) ┃                         
                         ┡━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩                         
                         │ * Best │   1/500 │    357 │   76     0   281  21.3 │      0.05% │ -442.275 USDT  (-44.23%) │ 1 day, 4:20:00 │   0.34857 │ 1022.562 USDT   (64.71%) │                         
                         │ * Best │   3/500 │    356 │  122     0   234  34.3 │     -0.08% │ -241.807 USDT  (-24.18%) │        8:43:00 │   0.28317 │  561.986 USDT   (42.80%) │                         
                         │ * Best │   4/500 │    484 │  113     0   371  23.3 │      0.10% │  -80.929 USDT   (-8.09%) │        6:55:00 │   0.09235 │  488.228 USDT   (38.09%) │                         
                         │ * Best │   7/500 │    386 │  102     0   284  26.4 │      0.43% │  724.825 USDT   (72.48%) │       14:13:00 │  -0.35509 │  920.858 USDT   (39.87%) │                         
                         │ Best   │  71/500 │    329 │   90     0   239  27.4 │      0.60% │ 1182.816 USDT  (118.28%) │       17:53:00 │  -0.57283 │  578.231 USDT   (29.02%) │                         
                         │ Best   │ 112/500 │    392 │  111     0   281  28.3 │      0.54% │ 1622.249 USDT  (162.22%) │       17:35:00 │  -0.66818 │  794.295 USDT   (32.54%) │                         
                         │ Best   │ 113/500 │    399 │  113     0   286  28.3 │      0.55% │ 1867.312 USDT  (186.73%) │       17:44:00 │  -0.69403 │  578.759 USDT   (23.60%) │                         
                         │ Best   │ 133/500 │    354 │   99     0   255  28.0 │      0.63% │ 1792.175 USDT  (179.22%) │       17:32:00 │  -0.73724 │  457.439 USDT   (14.08%) │                         
                         │ Best   │ 161/500 │    448 │  129     0   319  28.8 │      0.51% │ 2437.829 USDT  (243.78%) │       17:09:00 │  -0.77406 │  624.673 USDT   (15.38%) │                         
                         │ Best   │ 228/500 │    405 │  115     0   290  28.4 │      0.55% │ 2369.024 USDT  (236.90%) │       17:42:00 │  -0.78721 │  576.305 USDT   (14.61%) │                         
                         │ Best   │ 235/500 │    407 │  115     0   292  28.3 │      0.54% │ 2368.906 USDT  (236.89%) │       17:45:00 │  -0.79855 │  533.352 USDT   (13.67%) │                         
                         │ Best   │ 291/500 │    408 │  116     0   292  28.4 │      0.54% │ 2383.565 USDT  (238.36%) │       17:46:00 │  -0.80101 │  535.671 USDT   (13.67%) │                         
                         │ Best   │ 339/500 │    426 │  112     0   314  26.3 │      0.93% │  357.411 USDT   (35.74%) │       23:21:00 │  -0.82274 │   87.706 USDT    (6.07%) │                         
                         │ Best   │ 345/500 │    463 │  125     0   338  27.0 │      0.92% │  326.677 USDT   (32.67%) │       23:43:00 │  -0.82426 │   96.628 USDT    (7.46%) │                         
                         │ Best   │ 354/500 │    490 │  131     0   359  26.7 │      0.91% │  346.513 USDT   (34.65%) │       23:58:00 │  -0.88781 │   90.740 USDT    (6.94%) │                         
                         │ Best   │ 392/500 │    473 │  127     0   346  26.8 │      0.94% │  344.457 USDT   (34.45%) │ 1 day, 0:02:00 │  -0.89747 │   91.292 USDT    (7.03%) │                         
                         │ Best   │ 394/500 │    490 │  131     0   359  26.7 │      0.91% │  360.159 USDT   (36.02%) │       23:56:00 │  -0.90314 │   95.753 USDT    (6.60%) │                         
                         │ Best   │ 407/500 │    604 │  141     0   463  23.3 │      0.48% │  283.555 USDT   (28.36%) │        9:20:00 │  -0.93174 │   57.039 USDT    (4.25%) │                         
                         │ Best   │ 422/500 │    606 │  142     0   464  23.4 │      0.46% │  286.131 USDT   (28.61%) │        9:07:00 │  -0.95221 │   57.152 USDT    (4.25%) │                         
                         └────────┴─────────┴────────┴────────────────────────┴────────────┴──────────────────────────┴────────────────┴───────────┴──────────────────────────┘                         
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 500/500 100% • 0:18:10 • 0:00:00
2025-09-17 09:35:43,512 - freqtrade.optimize.hyperopt.hyperopt - INFO - 500 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-17_09-17-21.fthypt'.
2025-09-17 09:35:43,712 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

   422/500:    606 trades. 142/0/464 Wins/Draws/Losses. Avg profit   0.46%. Median profit  -0.61%. Total profit 286.13109263 USDT (  28.61%). Avg duration 9:07:00 min. Objective: -0.95221

{"params":{"hammer_body_threshold":3.335,"hammer_head_threshold":0.321,"entry_kinjun_sup_spanA":false,"entry_kinjun_sup_spanB":false,"entry_kinjun_sup_tenkan":false,"entry_sma200":false,"entry_spanA_sup_spanB":false,"entry_span_futur":false,"rsi_entry_max":50,"rsi_entry_min":20,"volume_factor":1.0,"kinjun_threshold":0,"lookback_period_for_stoploss":0,"stoploss_margin":1.0,"take_profit_multiplier":2,"use_sell_signal_param":false,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231
```

## Backtesting Output
```
2025-09-17 09:35:48,923 - freqtrade - INFO - freqtrade 2025.8
2025-09-17 09:35:49,456 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-17 09:35:51,690 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-17 09:35:51,698 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-17 09:35:51,699 - freqtrade.loggers - INFO - Logfile configured
2025-09-17 09:35:51,700 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-17 09:35:51,700 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-17 09:35:51,701 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-17 09:35:51,701 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-17 09:35:51,701 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-17 09:35:52,278 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-17 09:35:52,282 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-17 09:35:52,282 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-17 09:35:52,283 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-17 09:35:52,284 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-17 09:35:52,285 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-17 09:35:52,288 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-17 09:35:52,313 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-17 09:35:52,314 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 09:35:52,319 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-17 09:35:52,320 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-17 09:35:52,321 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-17 09:35:52,357 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-17 09:35:56,714 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-17 09:35:56,831 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-17 09:35:56,834 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-17 09:35:56,840 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-17 09:35:56,841 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-17 09:35:56,841 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-17 09:35:56,842 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-17 09:35:56,843 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-17 09:35:56,844 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-17 09:35:56,844 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-17 09:35:56,845 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-17 09:35:56,846 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-17 09:35:56,846 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-17 09:35:56,847 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-17 09:35:56,848 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-17 09:35:56,849 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-17 09:35:56,849 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-17 09:35:56,850 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-17 09:35:56,851 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-17 09:35:56,852 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-17 09:35:56,853 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-17 09:35:56,855 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-17 09:35:56,856 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-17 09:35:56,856 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-17 09:35:56,857 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-17 09:35:56,858 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-17 09:35:56,858 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-17 09:35:56,859 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-17 09:35:56,860 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-17 09:35:56,861 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-17 09:35:56,862 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-17 09:35:56,862 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 09:35:56,889 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-17 09:35:56,927 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-17 09:35:57,017 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 09:35:57,124 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 09:35:57,221 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 09:35:57,307 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 09:35:57,404 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 09:35:57,432 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-17 09:35:57,863 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 09:35:58,517 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 09:35:59,021 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 09:35:59,492 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 09:35:59,958 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 09:36:01,399 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-17 09:36:01,405 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-17 09:36:01,405 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-17 09:36:01,407 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_spanA = False
2025-09-17 09:36:01,409 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_spanB = False
2025-09-17 09:36:01,410 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_tenkan = False
2025-09-17 09:36:01,411 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_sma200 = False
2025-09-17 09:36:01,411 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_spanA_sup_spanB = False
2025-09-17 09:36:01,412 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_span_futur = False
2025-09-17 09:36:01,413 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 3.335
2025-09-17 09:36:01,414 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.321
2025-09-17 09:36:01,414 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 50
2025-09-17 09:36:01,415 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 20
2025-09-17 09:36:01,416 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1.0
2025-09-17 09:36:01,417 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0
2025-09-17 09:36:01,418 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 0
2025-09-17 09:36:01,418 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 1.0
2025-09-17 09:36:01,419 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-17 09:36:01,420 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-17 09:36:01,420 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-17 09:36:01,421 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-17 09:36:01,426 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 09:36:01,450 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 09:36:04,300 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 09:36:04,330 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 09:36:07,489 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 09:36:07,525 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 09:36:11,339 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 09:36:11,361 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 09:36:14,245 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 09:36:14,273 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 09:36:17,979 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-17 09:38:23,868 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-17_09-38-23.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │    237 │         0.15 │           6.693 │         0.67 │      8:34:00 │   57     0   180  24.1 │
│ BTC/USDT │    214 │         -0.0 │          -7.536 │        -0.75 │      9:34:00 │   47     0   167  22.0 │
│ ETH/USDT │    202 │        -0.07 │         -18.993 │         -1.9 │      8:07:00 │   43     0   159  21.3 │
│ LTC/USDT │    254 │        -0.15 │         -50.280 │        -5.03 │      8:14:00 │   46     0   208  18.1 │
│ BNB/USDT │    256 │        -0.18 │         -93.553 │        -9.36 │      7:59:00 │   52     0   204  20.3 │
│    TOTAL │   1163 │        -0.05 │        -163.669 │       -16.37 │      8:28:00 │  245     0   918  21.1 │
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
│     OTHER │    1163 │        -0.05 │        -163.669 │       -16.37 │      8:28:00 │  245     0   918  21.1 │
│     TOTAL │    1163 │        -0.05 │        -163.669 │       -16.37 │      8:28:00 │  245     0   918  21.1 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │     3 │        21.81 │         109.117 │        10.91 │ 1 day, 7:55:00 │    3     0     0   100 │
│    exit_signal │  1160 │        -0.11 │        -272.785 │       -27.28 │        8:25:00 │  242     0   918  20.9 │
│          TOTAL │  1163 │        -0.05 │        -163.669 │       -16.37 │        8:28:00 │  245     0   918  21.1 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │      3 │        21.81 │         109.117 │        10.91 │ 1 day, 7:55:00 │    3     0     0   100 │
│           │    exit_signal │   1160 │        -0.11 │        -272.785 │       -27.28 │        8:25:00 │  242     0   918  20.9 │
│     TOTAL │                │   1163 │        -0.05 │        -163.669 │       -16.37 │        8:28:00 │  245     0   918  21.1 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 1163 / 0.86                    │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 836.331 USDT                   │
│ Absolute profit               │ -163.669 USDT                  │
│ Total profit %                │ -16.37%                        │
│ CAGR %                        │ -4.72%                         │
│ Sortino                       │ -2.14                          │
│ Sharpe                        │ -0.71                          │
│ Calmar                        │ -1.07                          │
│ SQN                           │ -1.46                          │
│ Profit factor                 │ 0.83                           │
│ Expectancy (Ratio)            │ -0.14 (-0.13)                  │
│ Avg. daily profit             │ -0.121 USDT                    │
│ Avg. stake amount             │ 141.128 USDT                   │
│ Total trade volume            │ 328757.898 USDT                │
│                               │                                │
│ Best Pair                     │ XRP/USDT 0.67%                 │
│ Worst Pair                    │ BNB/USDT -9.36%                │
│ Best trade                    │ LTC/USDT 30.02%                │
│ Worst trade                   │ LTC/USDT -7.34%                │
│ Best day                      │ 41.301 USDT                    │
│ Worst day                     │ -16.793 USDT                   │
│ Days win/draw/lose            │ 152 / 720 / 472                │
│ Min/Max/Avg. Duration Winners │ 0d 01:00 / 3d 04:00 / 1d 00:01 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 2d 02:00 / 0d 04:19 │
│ Max Consecutive Wins / Loss   │ 3 / 31                         │
│ Rejected Entry signals        │ 312                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 835.883 USDT                   │
│ Max balance                   │ 1068.402 USDT                  │
│ Max % of account underwater   │ 21.76%                         │
│ Absolute drawdown             │ 232.518 USDT (21.76%)          │
│ Drawdown duration             │ 794 days 16:00:00              │
│ Profit at drawdown start      │ 68.402 USDT                    │
│ Profit at drawdown end        │ -164.117 USDT                  │
│ Drawdown start                │ 2023-07-04 06:00:00            │
│ Drawdown end                  │ 2025-09-05 22:00:00            │
│ Market change                 │ 91.49%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │   1163 │        -0.05 │        -163.669 │       -16.37 │      8:28:00 │  245     0   918  21.1 │ 232.518 USDT  21.76% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
