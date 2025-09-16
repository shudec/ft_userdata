# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 191 / 0.14, Median: -1.1%, Total profit: -31.39%, Sortino: -0.89, Sharpe: -0.28, Calmar: -1.11, Drawdown: 40.04%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 962  
**Timestamp:** 2025-09-16 20:40:06

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell buy",
  "random_state": 962,
  "epochs": 200,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 200 --spaces sell buy --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 962
```

## Hyperopt Output
```
2025-09-16 18:35:37,809 - freqtrade - INFO - freqtrade 2025.7
2025-09-16 18:35:38,513 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-16 18:35:38,514 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-16 18:35:39,974 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-16 18:35:39,978 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-16 18:35:39,978 - freqtrade.loggers - INFO - Logfile configured
2025-09-16 18:35:39,978 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-16 18:35:39,979 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-16 18:35:39,979 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-16 18:35:39,980 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-16 18:35:39,991 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-16 18:35:39,991 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-16 18:35:39,992 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-16 18:35:39,992 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 200 epochs ...
2025-09-16 18:35:39,993 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['sell', 'buy']
2025-09-16 18:35:39,993 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-16 18:35:39,994 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-16 18:35:39,994 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 962
2025-09-16 18:35:39,995 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-16 18:35:39,995 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-16 18:35:39,995 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-16 18:35:39,996 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-16 18:35:39,998 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-16 18:35:40,022 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-16 18:35:40,024 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 18:35:40,028 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-16 18:35:40,029 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-16 18:35:40,030 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-16 18:35:40,031 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-16 18:35:40,068 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-16 18:35:42,548 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-16 18:35:42,595 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuKinjunStrategy from '/freqtrade/user_data/strategies/IchimokuKinjunStrategy.py'...
2025-09-16 18:35:42,595 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2025-09-16 18:35:42,596 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-16 18:35:42,597 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-16 18:35:42,597 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-16 18:35:42,598 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-16 18:35:42,598 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-16 18:35:42,598 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-16 18:35:42,599 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-16 18:35:42,599 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-16 18:35:42,600 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-16 18:35:42,600 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-16 18:35:42,600 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-16 18:35:42,601 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-16 18:35:42,601 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-16 18:35:42,602 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-16 18:35:42,602 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-16 18:35:42,603 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-16 18:35:42,603 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-16 18:35:42,603 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-16 18:35:42,604 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-16 18:35:42,604 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-16 18:35:42,605 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-16 18:35:42,605 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-16 18:35:42,605 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-16 18:35:42,606 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-16 18:35:42,606 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-16 18:35:42,606 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-16 18:35:42,607 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-16 18:35:42,607 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-16 18:35:42,608 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-16 18:35:42,608 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 18:35:42,614 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-16 18:35:42,648 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-16 18:35:42,650 - freqtrade.strategy.hyper - INFO - No params for buy found, using default values.
2025-09-16 18:35:42,651 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_kinjun_sup_spanA = False
2025-09-16 18:35:42,651 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_kinjun_sup_spanB = False
2025-09-16 18:35:42,652 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_kinjun_sup_tenkan = False
2025-09-16 18:35:42,652 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_sma200 = False
2025-09-16 18:35:42,652 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_spanA_sup_spanB = False
2025-09-16 18:35:42,653 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_span_futur = False
2025-09-16 18:35:42,653 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 50
2025-09-16 18:35:42,654 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 20
2025-09-16 18:35:42,654 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): volume_factor = 1.0
2025-09-16 18:35:42,655 - freqtrade.strategy.hyper - INFO - No params for sell found, using default values.
2025-09-16 18:35:42,655 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): kinjun_threshold = 2
2025-09-16 18:35:42,656 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): lookback_period_for_stoploss = 5
2025-09-16 18:35:42,656 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): stoploss_margin = 0.999
2025-09-16 18:35:42,656 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): take_profit_multiplier = 2
2025-09-16 18:35:42,657 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_stoploss_param = True
2025-09-16 18:35:42,657 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-16 18:35:42,665 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-16 18:35:42,666 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 962
2025-09-16 18:35:42,711 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-16 18:35:42,772 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-16 18:35:42,782 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-16 18:35:42,826 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-16 18:35:42,873 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-16 18:35:42,917 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-16 18:35:42,927 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-16 18:35:42,945 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-16 18:35:43,696 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-16 18:35:43,698 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-16 18:35:43,707 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-16 18:35:45,433 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-16 18:35:45,446 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-16 18:35:47,086 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-16 18:35:47,097 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-16 18:35:48,608 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-16 18:35:48,619 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-16 18:35:49,794 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-16 18:35:49,806 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-16 18:35:51,345 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-16 18:35:51,641 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 20 CPU cores. Let's make them scream!
2025-09-16 18:35:51,642 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-16 18:35:51,643 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-16 18:35:51,644] A new study created in memory with name: no-name-d08f4660-c64b-465e-be71-017de7ee293b
2025-09-16 18:35:51,698 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                         ┏━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓                         
                         ┃ Best   ┃   Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃     Avg duration ┃ Objective ┃     Max Drawdown (Acct) ┃                         
                         ┡━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩                         
                         │ * Best │   2/200 │      6 │    1     0     5  16.7 │     -0.78% │ -50.166 USDT   (-5.02%) │   1 day, 9:40:00 │   0.05841 │  50.166 USDT    (5.02%) │                         
                         │ * Best │  19/200 │      2 │    1     0     1  50.0 │     -0.17% │  -3.606 USDT   (-0.36%) │  1 day, 13:30:00 │   0.00523 │  17.043 USDT    (1.70%) │                         
                         │ * Best │  28/200 │     11 │    4     0     7  36.4 │     -0.51% │  47.300 USDT    (4.73%) │         16:33:00 │  -0.03434 │  51.395 USDT    (5.14%) │                         
                         │ Best   │  36/200 │      2 │    1     0     1  50.0 │      2.98% │  27.322 USDT    (2.73%) │ 4 days, 21:00:00 │  -0.03759 │   2.394 USDT    (0.24%) │                         
                         │ Best   │  72/200 │     47 │   18     0    29  38.3 │      0.28% │ 174.739 USDT   (17.47%) │  1 day, 18:31:00 │  -0.13212 │ 237.552 USDT   (22.58%) │                         
                         │ Best   │  99/200 │     48 │   18     0    30  37.5 │      0.36% │ 180.520 USDT   (18.05%) │  1 day, 19:15:00 │  -0.13661 │ 237.360 USDT   (22.25%) │                         
                         │ Best   │ 101/200 │     62 │   26     0    36  41.9 │      0.89% │ 385.917 USDT   (38.59%) │ 2 days, 20:16:00 │  -0.26456 │ 204.848 USDT   (19.17%) │                         
                         │ Best   │ 141/200 │     63 │   25     0    38  39.7 │      0.96% │ 523.184 USDT   (52.32%) │         19:57:00 │  -0.35890 │ 131.608 USDT   (12.31%) │                         
                         └────────┴─────────┴────────┴────────────────────────┴────────────┴─────────────────────────┴──────────────────┴───────────┴─────────────────────────┘                         
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 200/200 100% • 0:03:17 • 0:00:00
2025-09-16 18:39:09,473 - freqtrade.optimize.hyperopt.hyperopt - INFO - 200 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuKinjunStrategy_2025-09-16_18-35-40.fthypt'.
2025-09-16 18:39:09,508 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuKinjunStrategy.json

Best result:

   141/200:     63 trades. 25/0/38 Wins/Draws/Losses. Avg profit   0.96%. Median profit  -1.10%. Total profit 523.18410394 USDT (  52.32%). Avg duration 19:57:00 min. Objective: -0.35890

{"params":{"entry_kinjun_sup_spanA":false,"entry_kinjun_sup_spanB":true,"entry_kinjun_sup_tenkan":false,"entry_spanA_sup_spanB":true,"entry_span_futur":false,"rsi_entry_max":68,"rsi_entry_min":15,"volume_factor":2.111,"entry_sma200":false,"kinjun_threshold":2,"lookback_period_for_stoploss":1,"stoploss_margin":1.0,"take_profit_multiplier":2.5,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuKinjunStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231
```

## Backtesting Output
```
2025-09-16 18:39:15,447 - freqtrade - INFO - freqtrade 2025.7
2025-09-16 18:39:15,821 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-16 18:39:15,822 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-16 18:39:17,689 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-16 18:39:17,692 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-16 18:39:17,692 - freqtrade.loggers - INFO - Logfile configured
2025-09-16 18:39:17,693 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-16 18:39:17,693 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-16 18:39:17,694 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-16 18:39:17,694 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-16 18:39:17,694 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-16 18:39:17,702 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-16 18:39:17,703 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-16 18:39:17,704 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-16 18:39:17,704 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-16 18:39:17,705 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-16 18:39:17,705 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-16 18:39:17,706 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-16 18:39:17,727 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-16 18:39:17,727 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 18:39:17,731 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-16 18:39:17,732 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-16 18:39:17,733 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-16 18:39:17,768 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-16 18:39:20,396 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-16 18:39:20,440 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuKinjunStrategy from '/freqtrade/user_data/strategies/IchimokuKinjunStrategy.py'...
2025-09-16 18:39:20,441 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuKinjunStrategy.json
2025-09-16 18:39:20,442 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-16 18:39:20,442 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-16 18:39:20,443 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-16 18:39:20,443 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-16 18:39:20,444 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-16 18:39:20,444 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-16 18:39:20,445 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-16 18:39:20,445 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-16 18:39:20,446 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-16 18:39:20,446 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-16 18:39:20,446 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-16 18:39:20,447 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-16 18:39:20,447 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-16 18:39:20,448 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-16 18:39:20,448 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-16 18:39:20,449 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-16 18:39:20,449 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-16 18:39:20,450 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-16 18:39:20,450 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-16 18:39:20,450 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-16 18:39:20,451 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-16 18:39:20,451 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-16 18:39:20,452 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-16 18:39:20,452 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-16 18:39:20,453 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-16 18:39:20,454 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-16 18:39:20,455 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-16 18:39:20,456 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-16 18:39:20,456 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 18:39:20,462 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-16 18:39:20,501 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-16 18:39:20,539 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-16 18:39:20,592 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-16 18:39:20,639 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-16 18:39:20,678 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-16 18:39:20,727 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-16 18:39:20,758 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-16 18:39:20,841 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-16 18:39:21,123 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-16 18:39:21,403 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-16 18:39:21,642 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-16 18:39:21,859 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-16 18:39:23,189 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-16 18:39:23,190 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-16 18:39:23,191 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuKinjunStrategy
2025-09-16 18:39:23,192 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_spanA = False
2025-09-16 18:39:23,192 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_spanB = True
2025-09-16 18:39:23,192 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_tenkan = False
2025-09-16 18:39:23,193 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_sma200 = False
2025-09-16 18:39:23,193 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_spanA_sup_spanB = True
2025-09-16 18:39:23,193 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_span_futur = False
2025-09-16 18:39:23,194 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 68
2025-09-16 18:39:23,194 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 15
2025-09-16 18:39:23,194 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 2.111
2025-09-16 18:39:23,195 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 2
2025-09-16 18:39:23,195 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 1
2025-09-16 18:39:23,196 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 1.0
2025-09-16 18:39:23,196 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2.5
2025-09-16 18:39:23,196 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-16 18:39:23,196 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-16 18:39:23,198 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-16 18:39:23,207 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-16 18:39:25,875 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-16 18:39:25,883 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-16 18:39:28,421 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-16 18:39:28,431 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-16 18:39:30,990 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-16 18:39:30,998 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-16 18:39:33,539 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-16 18:39:33,546 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-16 18:39:36,113 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-16 18:40:05,591 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-16_18-40-05.meta.json"
Result for strategy IchimokuKinjunStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │     48 │        -0.08 │           0.843 │         0.08 │     20:03:00 │   17     0    31  35.4 │
│ LTC/USDT │     43 │         -0.5 │         -46.732 │        -4.67 │     19:46:00 │   11     0    32  25.6 │
│ XRP/USDT │     38 │         0.15 │         -52.471 │        -5.25 │     12:20:00 │   11     0    27  28.9 │
│ BNB/USDT │     19 │        -0.78 │         -92.331 │        -9.23 │     22:08:00 │    3     0    16  15.8 │
│ ETH/USDT │     43 │        -0.31 │        -123.231 │       -12.32 │     16:22:00 │   11     0    32  25.6 │
│    TOTAL │    191 │        -0.25 │        -313.922 │       -31.39 │     17:50:00 │   53     0   138  27.7 │
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
│     OTHER │     191 │        -0.25 │        -313.922 │       -31.39 │     17:50:00 │   53     0   138  27.7 │
│     TOTAL │     191 │        -0.25 │        -313.922 │       -31.39 │     17:50:00 │   53     0   138  27.7 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                   EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2.5R │    49 │          3.6 │        1077.097 │       107.71 │        21:08:00 │   49     0     0   100 │
│      exit_signal │    16 │        -1.08 │         -69.543 │        -6.95 │ 1 day, 18:19:00 │    4     0    12  25.0 │
│        stop_loss │   126 │        -1.65 │       -1321.477 │      -132.15 │        13:26:00 │    0     0   126     0 │
│            TOTAL │   191 │        -0.25 │        -313.922 │       -31.39 │        17:50:00 │   53     0   138  27.7 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                          MIXED TAG STATS                                                           
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2.5R │     49 │          3.6 │        1077.097 │       107.71 │        21:08:00 │   49     0     0   100 │
│           │      exit_signal │     16 │        -1.08 │         -69.543 │        -6.95 │ 1 day, 18:19:00 │    4     0    12  25.0 │
│           │        stop_loss │    126 │        -1.65 │       -1321.477 │      -132.15 │        13:26:00 │    0     0   126     0 │
│     TOTAL │                  │    191 │        -0.25 │        -313.922 │       -31.39 │        17:50:00 │   53     0   138  27.7 │
└───────────┴──────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-11 17:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 191 / 0.14                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 686.078 USDT                   │
│ Absolute profit               │ -313.922 USDT                  │
│ Total profit %                │ -31.39%                        │
│ CAGR %                        │ -9.69%                         │
│ Sortino                       │ -0.89                          │
│ Sharpe                        │ -0.28                          │
│ Calmar                        │ -1.11                          │
│ SQN                           │ -1.42                          │
│ Profit factor                 │ 0.78                           │
│ Expectancy (Ratio)            │ -1.64 (-0.16)                  │
│ Avg. daily profit             │ -0.233 USDT                    │
│ Avg. stake amount             │ 660.812 USDT                   │
│ Total trade volume            │ 252621.072 USDT                │
│                               │                                │
│ Best Pair                     │ BTC/USDT 0.08%                 │
│ Worst Pair                    │ ETH/USDT -12.32%               │
│ Best trade                    │ XRP/USDT 16.13%                │
│ Worst trade                   │ XRP/USDT -7.80%                │
│ Best day                      │ 46.537 USDT                    │
│ Worst day                     │ -32.107 USDT                   │
│ Days win/draw/lose            │ 46 / 1170 / 120                │
│ Min/Max/Avg. Duration Winners │ 0d 00:10 / 9d 09:00 / 1d 00:39 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 5d 06:00 / 0d 15:12 │
│ Max Consecutive Wins / Loss   │ 6 / 15                         │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 636.873 USDT                   │
│ Max balance                   │ 1062.231 USDT                  │
│ Max % of account underwater   │ 40.04%                         │
│ Absolute Drawdown (Account)   │ 40.04%                         │
│ Absolute Drawdown             │ 425.358 USDT                   │
│ Drawdown high                 │ 62.231 USDT                    │
│ Drawdown low                  │ -363.127 USDT                  │
│ Drawdown Start                │ 2022-02-07 03:30:00            │
│ Drawdown End                  │ 2025-06-05 13:45:00            │
│ Market change                 │ 94.84%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │    191 │        -0.25 │        -313.922 │       -31.39 │     17:50:00 │   53     0   138  27.7 │ 425.358 USDT  40.04% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
