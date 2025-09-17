# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 36 / 0.03, Median: 2.03%, Total profit: -18.93%, Sortino: -0.75, Sharpe: -0.15, Calmar: -1.18, Drawdown: 0%)

---
            
**Strategy:** IchimokuRebondStrategy  
**Random State:** 5330  
**Timestamp:** 2025-09-17 17:34:15

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 5330,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 5330
```

## Hyperopt Output
```
2025-09-17 15:30:11,742 - freqtrade - INFO - freqtrade 2025.8
2025-09-17 15:30:12,926 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-17 15:30:14,748 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-17 15:30:14,754 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-17 15:30:14,754 - freqtrade.loggers - INFO - Logfile configured
2025-09-17 15:30:14,755 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-17 15:30:14,755 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-17 15:30:14,756 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-17 15:30:14,756 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-17 15:30:15,026 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-17 15:30:15,029 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-17 15:30:15,029 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-17 15:30:15,029 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 100 epochs ...
2025-09-17 15:30:15,030 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-17 15:30:15,030 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-17 15:30:15,031 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-17 15:30:15,031 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 5330
2025-09-17 15:30:15,031 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-17 15:30:15,032 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-17 15:30:15,032 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-17 15:30:15,032 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-17 15:30:15,033 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-17 15:30:15,045 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-17 15:30:15,046 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 15:30:15,048 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-17 15:30:15,055 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-17 15:30:15,063 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-17 15:30:15,064 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-17 15:30:15,090 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-17 15:30:17,462 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-17 15:30:17,567 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-17 15:30:17,569 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2025-09-17 15:30:17,570 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-17 15:30:17,570 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-17 15:30:17,570 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-17 15:30:17,571 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-17 15:30:17,571 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-17 15:30:17,572 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-17 15:30:17,572 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-17 15:30:17,572 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-17 15:30:17,573 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-17 15:30:17,573 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-17 15:30:17,573 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-17 15:30:17,574 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-17 15:30:17,574 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-17 15:30:17,575 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-17 15:30:17,575 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-17 15:30:17,575 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-17 15:30:17,576 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-17 15:30:17,577 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-17 15:30:17,577 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-17 15:30:17,578 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-17 15:30:17,579 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-17 15:30:17,580 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-17 15:30:17,580 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-17 15:30:17,580 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-17 15:30:17,581 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-17 15:30:17,581 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-17 15:30:17,582 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-17 15:30:17,582 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-17 15:30:17,582 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-17 15:30:17,583 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 15:30:17,602 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-17 15:30:17,628 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-17 15:30:17,629 - freqtrade.strategy.hyper - INFO - No params for buy found, using default values.
2025-09-17 15:30:17,630 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_kinjun_sup_spanA = False
2025-09-17 15:30:17,630 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_kinjun_sup_spanB = False
2025-09-17 15:30:17,631 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_kinjun_sup_tenkan = False
2025-09-17 15:30:17,631 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_sma200 = False
2025-09-17 15:30:17,631 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_spanA_sup_spanB = False
2025-09-17 15:30:17,632 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_span_futur = False
2025-09-17 15:30:17,632 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): hammer_body_threshold = 0.2
2025-09-17 15:30:17,633 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): hammer_head_threshold = 0.1
2025-09-17 15:30:17,633 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): hammer_strength_threshold = 0.01
2025-09-17 15:30:17,634 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 50
2025-09-17 15:30:17,634 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 20
2025-09-17 15:30:17,635 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): volume_factor = 1.0
2025-09-17 15:30:17,635 - freqtrade.strategy.hyper - INFO - No params for sell found, using default values.
2025-09-17 15:30:17,635 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): kinjun_threshold = 2
2025-09-17 15:30:17,636 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): lookback_period_for_stoploss = 5
2025-09-17 15:30:17,636 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): stoploss_margin = 0.999
2025-09-17 15:30:17,637 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): take_profit_multiplier = 2
2025-09-17 15:30:17,637 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_stoploss_param = True
2025-09-17 15:30:17,637 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_sell_signal_param = True
2025-09-17 15:30:17,638 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-17 15:30:17,659 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-17 15:30:17,659 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 5330
2025-09-17 15:30:17,717 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-17 15:30:17,786 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-17 15:30:17,794 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-17 15:30:17,854 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-17 15:30:17,909 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-17 15:30:17,964 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-17 15:30:17,972 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-17 15:30:17,984 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-17 15:30:18,610 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-17 15:30:18,613 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 15:30:18,630 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-17 15:30:20,893 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 15:30:20,911 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-17 15:30:23,411 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 15:30:23,427 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-17 15:30:25,089 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 15:30:25,107 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-17 15:30:26,351 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 15:30:26,366 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-17 15:30:28,086 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-17 15:30:28,537 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 16 CPU cores. Let's make them scream!
2025-09-17 15:30:28,538 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-17 15:30:28,539 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-17 15:30:28,540] A new study created in memory with name: no-name-6e3b95eb-e35a-466d-a991-2744a0f9ab23
2025-09-17 15:30:28,588 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                           Hyperopt results                                                                                             
                        ┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓                         
                        ┃ Best   ┃  Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                   Profit ┃      Avg duration ┃ Objective ┃     Max Drawdown (Acct) ┃                         
                        ┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩                         
                        │ * Best │  1/100 │    102 │   38     0    64  37.3 │     -0.61% │ -365.204 USDT  (-36.52%) │          21:38:00 │   0.43280 │ 461.444 USDT   (42.09%) │                         
                        │ * Best │  2/100 │     31 │    7     0    24  22.6 │     -1.15% │ -170.094 USDT  (-17.01%) │   1 day, 11:48:00 │   0.15578 │ 222.513 USDT   (21.32%) │                         
                        │ * Best │  4/100 │      5 │    3     0     2  60.0 │     63.56% │   81.443 USDT    (8.14%) │ 184 days, 4:48:00 │  -0.05863 │  21.904 USDT    (1.99%) │                         
                        │ * Best │  8/100 │     14 │    6     0     8  42.9 │      5.11% │  117.297 USDT   (11.73%) │   1 day, 23:21:00 │  -0.07071 │ 164.112 USDT   (12.81%) │                         
                        │ * Best │ 10/100 │     20 │   11     0     9  55.0 │      2.58% │  222.912 USDT   (22.29%) │          16:54:00 │  -0.17482 │  46.308 USDT    (3.65%) │                         
                        │ * Best │ 25/100 │     29 │   15     0    14  51.7 │      1.92% │  249.990 USDT   (25.00%) │          23:17:00 │  -0.18502 │  49.734 USDT    (3.83%) │                         
                        │ Best   │ 96/100 │     34 │   18     0    16  52.9 │      1.63% │  314.532 USDT   (31.45%) │          19:39:00 │  -0.22162 │ 141.462 USDT    (9.72%) │                         
                        └────────┴────────┴────────┴────────────────────────┴────────────┴──────────────────────────┴───────────────────┴───────────┴─────────────────────────┘                         
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100/100 100% • 0:03:01 • 0:00:00
2025-09-17 15:33:30,646 - freqtrade.optimize.hyperopt.hyperopt - INFO - 100 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-17_15-30-15.fthypt'.
2025-09-17 15:33:30,816 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

    96/100:     34 trades. 18/0/16 Wins/Draws/Losses. Avg profit   1.63%. Median profit   2.03%. Total profit 314.53183769 USDT (  31.45%). Avg duration 19:39:00 min. Objective: -0.22162

{"params":{"hammer_body_threshold":0.238,"hammer_head_threshold":0.567,"hammer_strength_threshold":0.009,"entry_kinjun_sup_spanA":false,"entry_kinjun_sup_spanB":false,"entry_kinjun_sup_tenkan":false,"entry_sma200":false,"entry_spanA_sup_spanB":false,"entry_span_futur":false,"rsi_entry_max":50,"rsi_entry_min":20,"volume_factor":1.0,"kinjun_threshold":5,"lookback_period_for_stoploss":8,"stoploss_margin":0.997,"take_profit_multiplier":1.5,"use_sell_signal_param":true,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231
```

## Backtesting Output
```
2025-09-17 15:33:35,247 - freqtrade - INFO - freqtrade 2025.8
2025-09-17 15:33:35,624 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-17 15:33:37,351 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-17 15:33:37,358 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-17 15:33:37,358 - freqtrade.loggers - INFO - Logfile configured
2025-09-17 15:33:37,358 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-17 15:33:37,359 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-17 15:33:37,359 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-17 15:33:37,360 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-17 15:33:37,360 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-17 15:33:37,621 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-17 15:33:37,623 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-17 15:33:37,623 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-17 15:33:37,624 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-17 15:33:37,624 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-17 15:33:37,625 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-17 15:33:37,626 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-17 15:33:37,643 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-17 15:33:37,644 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 15:33:37,649 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-17 15:33:37,650 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-17 15:33:37,651 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-17 15:33:37,703 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-17 15:33:39,953 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-17 15:33:40,075 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-17 15:33:40,077 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-17 15:33:40,083 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-17 15:33:40,083 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-17 15:33:40,084 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-17 15:33:40,085 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-17 15:33:40,086 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-17 15:33:40,087 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-17 15:33:40,087 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-17 15:33:40,088 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-17 15:33:40,088 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-17 15:33:40,088 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-17 15:33:40,089 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-17 15:33:40,089 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-17 15:33:40,090 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-17 15:33:40,090 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-17 15:33:40,091 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-17 15:33:40,092 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-17 15:33:40,092 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-17 15:33:40,092 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-17 15:33:40,093 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-17 15:33:40,093 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-17 15:33:40,094 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-17 15:33:40,094 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-17 15:33:40,095 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-17 15:33:40,096 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-17 15:33:40,096 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-17 15:33:40,097 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-17 15:33:40,097 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-17 15:33:40,098 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-17 15:33:40,098 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 15:33:40,124 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-17 15:33:40,162 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-17 15:33:40,231 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 15:33:40,304 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 15:33:40,386 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 15:33:40,444 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 15:33:40,506 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 15:33:40,530 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-17 15:33:40,788 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 15:33:41,248 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 15:33:41,643 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 15:33:42,092 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 15:33:42,503 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 15:33:44,059 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-17 15:33:44,064 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-17 15:33:44,064 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-17 15:33:44,065 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_spanA = False
2025-09-17 15:33:44,066 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_spanB = False
2025-09-17 15:33:44,067 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_tenkan = False
2025-09-17 15:33:44,067 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_sma200 = False
2025-09-17 15:33:44,068 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_spanA_sup_spanB = False
2025-09-17 15:33:44,068 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_span_futur = False
2025-09-17 15:33:44,069 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.238
2025-09-17 15:33:44,070 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.567
2025-09-17 15:33:44,070 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.009
2025-09-17 15:33:44,071 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 50
2025-09-17 15:33:44,071 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 20
2025-09-17 15:33:44,072 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1.0
2025-09-17 15:33:44,073 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 5
2025-09-17 15:33:44,073 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 8
2025-09-17 15:33:44,074 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.997
2025-09-17 15:33:44,075 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-17 15:33:44,076 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-17 15:33:44,076 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-17 15:33:44,077 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-17 15:33:44,080 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 15:33:44,101 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 15:33:47,568 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 15:33:47,586 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 15:33:50,922 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 15:33:50,941 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 15:33:54,551 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 15:33:54,569 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 15:33:57,492 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 15:33:57,509 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 15:34:00,820 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-17 15:34:14,386 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-17_15-34-14.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      3 │        -0.61 │         -12.373 │        -1.24 │          8:57:00 │    1     0     2  33.3 │
│ BTC/USDT │      6 │        -0.01 │         -13.404 │        -1.34 │  2 days, 5:14:00 │    2     0     4  33.3 │
│ LTC/USDT │      9 │         1.41 │         -30.911 │        -3.09 │         19:49:00 │    3     0     6  33.3 │
│ ETH/USDT │     10 │        -1.11 │         -40.582 │        -4.06 │ 2 days, 17:36:00 │    3     0     7  30.0 │
│ XRP/USDT │      8 │        -0.91 │         -92.043 │         -9.2 │         18:39:00 │    1     0     7  12.5 │
│    TOTAL │     36 │        -0.21 │        -189.312 │       -18.93 │  1 day, 12:56:00 │   10     0    26  27.8 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
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
│     OTHER │      36 │        -0.21 │        -189.312 │       -18.93 │ 1 day, 12:56:00 │   10     0    26  27.8 │
│     TOTAL │      36 │        -0.21 │        -189.312 │       -18.93 │ 1 day, 12:56:00 │   10     0    26  27.8 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                   EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │    10 │         5.91 │         233.581 │        23.36 │ 1 day, 13:30:00 │   10     0     0   100 │
│        stop_loss │    26 │        -2.57 │        -422.893 │       -42.29 │ 1 day, 12:44:00 │    0     0    26     0 │
│            TOTAL │    36 │        -0.21 │        -189.312 │       -18.93 │ 1 day, 12:56:00 │   10     0    26  27.8 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                          MIXED TAG STATS                                                           
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1.5R │     10 │         5.91 │         233.581 │        23.36 │ 1 day, 13:30:00 │   10     0     0   100 │
│           │        stop_loss │     26 │        -2.57 │        -422.893 │       -42.29 │ 1 day, 12:44:00 │    0     0    26     0 │
│     TOTAL │                  │     36 │        -0.21 │        -189.312 │       -18.93 │ 1 day, 12:56:00 │   10     0    26  27.8 │
└───────────┴──────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00             │
│ Backtesting to                │ 2025-09-10 08:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 36 / 0.03                       │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 810.688 USDT                    │
│ Absolute profit               │ -189.312 USDT                   │
│ Total profit %                │ -18.93%                         │
│ CAGR %                        │ -5.52%                          │
│ Sortino                       │ -0.75                           │
│ Sharpe                        │ -0.15                           │
│ Calmar                        │ -1.18                           │
│ SQN                           │ -1.71                           │
│ Profit factor                 │ 0.55                            │
│ Expectancy (Ratio)            │ -5.26 (-0.32)                   │
│ Avg. daily profit             │ -0.14 USDT                      │
│ Avg. stake amount             │ 679.679 USDT                    │
│ Total trade volume            │ 48845.147 USDT                  │
│                               │                                 │
│ Best Pair                     │ BNB/USDT -1.24%                 │
│ Worst Pair                    │ XRP/USDT -9.20%                 │
│ Best trade                    │ LTC/USDT 21.09%                 │
│ Worst trade                   │ ETH/USDT -7.33%                 │
│ Best day                      │ 28.472 USDT                     │
│ Worst day                     │ -35.367 USDT                    │
│ Days win/draw/lose            │ 10 / 1204 / 24                  │
│ Min/Max/Avg. Duration Winners │ 0d 03:55 / 4d 13:45 / 1d 13:30  │
│ Min/Max/Avg. Duration Losers  │ 0d 00:40 / 18d 18:35 / 1d 12:44 │
│ Max Consecutive Wins / Loss   │ 2 / 9                           │
│ Rejected Entry signals        │ 0                               │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 773.157 USDT                    │
│ Max balance                   │ 1000.773 USDT                   │
│ Max % of account underwater   │ 22.74%                          │
│ Absolute drawdown             │ 227.616 USDT (22.74%)           │
│ Drawdown duration             │ 726 days 19:55:00               │
│ Profit at drawdown start      │ 0.773 USDT                      │
│ Profit at drawdown end        │ -226.843 USDT                   │
│ Drawdown start                │ 2022-07-07 14:20:00             │
│ Drawdown end                  │ 2024-07-03 10:15:00             │
│ Market change                 │ 91.49%                          │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     36 │        -0.21 │        -189.312 │       -18.93 │ 1 day, 12:56:00 │   10     0    26  27.8 │ 227.616 USDT  22.74% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴──────────────────────┘

```
