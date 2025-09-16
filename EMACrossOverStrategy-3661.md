# Freqtrade Automation Log

## Performance Indicator
**Status:** 🟠 ORANGE  
**Description:** Moderate Performance (Total trades: 521 / 0.39, Median: -2.09%, Total profit: 18.67%, Sortino: 1.67, Sharpe: 0.29, Calmar: 2.04, Drawdown: 0%)

---
            
**Strategy:** EMACrossOverStrategy  
**Random State:** 3661  
**Timestamp:** 2025-09-16 17:53:49

## Configuration
```json
{
  "strategy": "EMACrossOverStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "trailing",
  "random_state": 3661,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy EMACrossOverStrategy --timeframe 1h --epochs 100 --spaces trailing --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 3661
```

## Hyperopt Output
```
2025-09-16 15:44:30,120 - freqtrade - INFO - freqtrade 2025.8
2025-09-16 15:44:30,747 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-16 15:44:32,028 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-16 15:44:32,034 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-16 15:44:32,034 - freqtrade.loggers - INFO - Logfile configured
2025-09-16 15:44:32,034 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-16 15:44:32,035 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-16 15:44:32,035 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-16 15:44:32,036 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-16 15:44:32,339 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-16 15:44:32,341 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-16 15:44:32,341 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-16 15:44:32,342 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 100 epochs ...
2025-09-16 15:44:32,342 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['trailing']
2025-09-16 15:44:32,342 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-16 15:44:32,343 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-16 15:44:32,343 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 3661
2025-09-16 15:44:32,343 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-16 15:44:32,344 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-16 15:44:32,344 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-16 15:44:32,344 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-16 15:44:32,345 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-16 15:44:32,354 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-16 15:44:32,355 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 15:44:32,358 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-16 15:44:32,364 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-16 15:44:32,370 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-16 15:44:32,370 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-16 15:44:32,390 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-16 15:44:36,413 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-16 15:44:36,476 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy EMACrossOverStrategy from '/freqtrade/user_data/strategies/EMACrossOverStrategy.py'...
2025-09-16 15:44:36,479 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2025-09-16 15:44:36,480 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-16 15:44:36,482 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-16 15:44:36,483 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-16 15:44:36,483 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-16 15:44:36,484 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-16 15:44:36,485 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-16 15:44:36,486 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-16 15:44:36,486 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.15
2025-09-16 15:44:36,487 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: True
2025-09-16 15:44:36,487 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-16 15:44:36,488 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-16 15:44:36,488 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-16 15:44:36,489 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-16 15:44:36,489 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-16 15:44:36,490 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-16 15:44:36,490 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-16 15:44:36,490 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-16 15:44:36,491 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-16 15:44:36,491 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-16 15:44:36,491 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-16 15:44:36,492 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-16 15:44:36,493 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-16 15:44:36,493 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-16 15:44:36,494 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-16 15:44:36,494 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-16 15:44:36,495 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-16 15:44:36,496 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-16 15:44:36,496 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-16 15:44:36,497 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 15:44:36,516 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-16 15:44:36,542 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-16 15:44:36,543 - freqtrade.strategy.hyper - INFO - No params for buy found, using default values.
2025-09-16 15:44:36,544 - freqtrade.strategy.hyper - INFO - No params for sell found, using default values.
2025-09-16 15:44:36,545 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): lookback_period_for_stoploss = 5
2025-09-16 15:44:36,545 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): stoploss_margin = 0.999
2025-09-16 15:44:36,546 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): take_profit_multiplier = 2
2025-09-16 15:44:36,546 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): threshold_percentage = 1
2025-09-16 15:44:36,546 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_stoploss_param = False
2025-09-16 15:44:36,547 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-16 15:44:36,564 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-16 15:44:36,565 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 3661
2025-09-16 15:44:36,615 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-16 15:44:36,676 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-16 15:44:36,686 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-16 15:44:36,734 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-16 15:44:36,783 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-16 15:44:36,836 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-16 15:44:36,844 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-16 15:44:36,855 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-16 15:44:37,469 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-16 15:44:37,550 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-16 15:44:37,942 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 16 CPU cores. Let's make them scream!
2025-09-16 15:44:37,942 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-16 15:44:37,944 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-16 15:44:37,944] A new study created in memory with name: no-name-eb9d0f9c-d5fc-47ad-baeb-ab009e08e03e
2025-09-16 15:44:37,991 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                         ┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓                         
                         ┃ Best   ┃  Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                   Profit ┃     Avg duration ┃ Objective ┃     Max Drawdown (Acct) ┃                         
                         ┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩                         
                         │ * Best │  1/100 │    356 │   86     0   270  24.2 │     -0.32% │ -127.051 USDT  (-12.71%) │   1 day, 5:35:00 │   0.52801 │ 174.112 USDT   (17.18%) │                         
                         │ * Best │  2/100 │    318 │   49     0   269  15.4 │      0.08% │   25.909 USDT    (2.59%) │ 2 days, 14:02:00 │  -0.05751 │ 164.830 USDT   (15.71%) │                         
                         │ * Best │  3/100 │    321 │   49     0   272  15.3 │      0.09% │   47.013 USDT    (4.70%) │ 2 days, 11:14:00 │  -0.10617 │ 164.234 USDT   (15.22%) │                         
                         │ * Best │ 22/100 │    308 │   41     0   267  13.3 │      0.18% │   61.324 USDT    (6.13%) │ 2 days, 19:12:00 │  -0.12129 │ 175.940 USDT   (16.20%) │                         
                         │ Best   │ 50/100 │    308 │   41     0   267  13.3 │      0.19% │   64.408 USDT    (6.44%) │ 2 days, 19:11:00 │  -0.12714 │ 173.988 USDT   (16.02%) │                         
                         │ Best   │ 79/100 │    308 │   42     0   266  13.6 │      0.19% │   66.161 USDT    (6.62%) │ 2 days, 19:10:00 │  -0.13023 │ 179.431 USDT   (16.42%) │                         
                         │ Best   │ 83/100 │    308 │   42     0   266  13.6 │      0.21% │   71.219 USDT    (7.12%) │ 2 days, 19:11:00 │  -0.13986 │ 175.095 USDT   (16.02%) │                         
                         │ Best   │ 88/100 │    323 │   52     0   271  16.1 │      0.15% │   71.812 USDT    (7.18%) │  2 days, 9:49:00 │  -0.15947 │ 168.132 USDT   (15.22%) │                         
                         └────────┴────────┴────────┴────────────────────────┴────────────┴──────────────────────────┴──────────────────┴───────────┴─────────────────────────┘                         
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100/100 100% • 0:03:18 • 0:00:00
2025-09-16 15:47:57,116 - freqtrade.optimize.hyperopt.hyperopt - INFO - 100 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_EMACrossOverStrategy_2025-09-16_15-44-32.fthypt'.
2025-09-16 15:47:57,278 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/EMACrossOverStrategy.json

Best result:

    88/100:    323 trades. 52/0/271 Wins/Draws/Losses. Avg profit   0.15%. Median profit  -2.09%. Total profit 71.81246845 USDT (   7.18%). Avg duration 2 days, 9:49:00 min. Objective: -0.15947

{"params":{"lookback_period_for_stoploss":5,"stoploss_margin":0.999,"take_profit_multiplier":2,"threshold_percentage":1,"use_custom_stoploss_param":false},"minimal_roi":{},"stoploss":-0.15,"trailing_stop":true,"trailing_stop_positive":0.094,"trailing_stop_positive_offset":0.153,"trailing_only_offset_is_reached":true,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy EMACrossOverStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231
```

## Backtesting Output
```
2025-09-16 15:48:01,398 - freqtrade - INFO - freqtrade 2025.8
2025-09-16 15:48:01,740 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-16 15:48:03,173 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-16 15:48:03,181 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-16 15:48:03,181 - freqtrade.loggers - INFO - Logfile configured
2025-09-16 15:48:03,182 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-16 15:48:03,182 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-16 15:48:03,183 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-16 15:48:03,183 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-16 15:48:03,184 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-16 15:48:03,615 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-16 15:48:03,618 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-16 15:48:03,619 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-16 15:48:03,619 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-16 15:48:03,620 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-16 15:48:03,621 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-16 15:48:03,622 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-16 15:48:03,637 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-16 15:48:03,638 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 15:48:03,642 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-16 15:48:03,643 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-16 15:48:03,644 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-16 15:48:03,674 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-16 15:48:07,143 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-16 15:48:07,252 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy EMACrossOverStrategy from '/freqtrade/user_data/strategies/EMACrossOverStrategy.py'...
2025-09-16 15:48:07,255 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/EMACrossOverStrategy.json
2025-09-16 15:48:07,263 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-16 15:48:07,264 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-16 15:48:07,264 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-16 15:48:07,265 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-16 15:48:07,266 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-16 15:48:07,267 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-16 15:48:07,268 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-16 15:48:07,269 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.15
2025-09-16 15:48:07,270 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: True
2025-09-16 15:48:07,271 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive: 0.094
2025-09-16 15:48:07,272 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.153
2025-09-16 15:48:07,273 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: True
2025-09-16 15:48:07,275 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-16 15:48:07,276 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-16 15:48:07,277 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-16 15:48:07,278 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-16 15:48:07,279 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-16 15:48:07,280 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-16 15:48:07,281 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-16 15:48:07,282 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-16 15:48:07,283 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-16 15:48:07,285 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-16 15:48:07,286 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-16 15:48:07,287 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-16 15:48:07,288 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-16 15:48:07,289 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-16 15:48:07,290 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-16 15:48:07,291 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-16 15:48:07,293 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-16 15:48:07,294 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 15:48:07,385 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-16 15:48:07,437 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-16 15:48:07,532 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-16 15:48:07,672 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-16 15:48:07,778 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-16 15:48:07,904 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-16 15:48:08,030 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-16 15:48:08,078 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-16 15:48:08,498 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-16 15:48:09,101 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-16 15:48:09,748 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-16 15:48:10,280 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-16 15:48:10,824 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-16 15:48:11,977 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-16 15:48:11,982 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-16 15:48:11,983 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy EMACrossOverStrategy
2025-09-16 15:48:11,983 - freqtrade.strategy.hyper - INFO - No params for buy found, using default values.
2025-09-16 15:48:11,984 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-09-16 15:48:11,985 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-09-16 15:48:11,985 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-16 15:48:11,985 - freqtrade.strategy.hyper - INFO - Strategy Parameter: threshold_percentage = 1
2025-09-16 15:48:11,986 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-16 15:48:11,986 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-16 15:48:12,047 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-16 15:53:47,908 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-16_15-53-47.meta.json"
Result for strategy EMACrossOverStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │     84 │         1.15 │         102.681 │        10.27 │ 3 days, 19:01:00 │   15     0    69  17.9 │
│ BNB/USDT │    109 │         0.76 │          82.744 │         8.27 │ 4 days, 20:45:00 │   23     0    86  21.1 │
│ BTC/USDT │     85 │         0.51 │          56.025 │          5.6 │ 5 days, 15:26:00 │   17     0    68  20.0 │
│ LTC/USDT │    115 │         0.06 │          -2.770 │        -0.28 │  2 days, 9:17:00 │   14     0   101  12.2 │
│ XRP/USDT │    128 │        -0.33 │         -51.956 │         -5.2 │ 2 days, 15:09:00 │   16     0   112  12.5 │
│    TOTAL │    521 │         0.36 │         186.724 │        18.67 │ 3 days, 17:21:00 │   85     0   436  16.3 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │        18.69 │          29.319 │         2.93 │ 38 days, 11:00:00 │    1     0     0   100 │
│ XRP/USDT │      1 │         1.43 │           1.634 │         0.16 │   1 day, 22:00:00 │    1     0     0   100 │
│    TOTAL │      2 │        10.06 │          30.953 │          3.1 │  20 days, 4:30:00 │    2     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                  ENTER TAG STATS                                                  
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │     521 │         0.36 │         186.724 │        18.67 │ 3 days, 17:21:00 │   85     0   436  16.3 │
│     TOTAL │     521 │         0.36 │         186.724 │        18.67 │ 3 days, 17:21:00 │   85     0   436  16.3 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                     EXIT REASON STATS                                                     
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     take_profit_2R │    23 │        30.59 │         833.460 │        83.35 │ 14 days, 16:12:00 │   23     0     0   100 │
│ trailing_stop_loss │    33 │        10.27 │         416.082 │        41.61 │  10 days, 5:29:00 │   33     0     0   100 │
│         force_exit │     2 │        10.06 │          30.953 │          3.1 │  20 days, 4:30:00 │    2     0     0   100 │
│          stop_loss │     1 │       -15.15 │         -16.244 │        -1.62 │   1 day, 18:05:00 │    0     0     1     0 │
│        exit_signal │   462 │        -1.86 │       -1077.527 │      -107.75 │  2 days, 15:31:00 │   27     0   435   5.8 │
│              TOTAL │   521 │         0.36 │         186.724 │        18.67 │  3 days, 17:21:00 │   85     0   436  16.3 │
└────────────────────┴───────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                                            MIXED TAG STATS                                                             
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃        Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │     take_profit_2R │     23 │        30.59 │         833.460 │        83.35 │ 14 days, 16:12:00 │   23     0     0   100 │
│           │ trailing_stop_loss │     33 │        10.27 │         416.082 │        41.61 │  10 days, 5:29:00 │   33     0     0   100 │
│           │         force_exit │      2 │        10.06 │          30.953 │          3.1 │  20 days, 4:30:00 │    2     0     0   100 │
│           │          stop_loss │      1 │       -15.15 │         -16.244 │        -1.62 │   1 day, 18:05:00 │    0     0     1     0 │
│           │        exit_signal │    462 │        -1.86 │       -1077.527 │      -107.75 │  2 days, 15:31:00 │   27     0   435   5.8 │
│     TOTAL │                    │    521 │         0.36 │         186.724 │        18.67 │  3 days, 17:21:00 │   85     0   436  16.3 │
└───────────┴────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                          SUMMARY METRICS                           
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                            ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00              │
│ Backtesting to                │ 2025-09-10 08:00:00              │
│ Trading Mode                  │ Spot                             │
│ Max open trades               │ 3                                │
│                               │                                  │
│ Total/Daily Avg Trades        │ 521 / 0.39                       │
│ Starting balance              │ 1000 USDT                        │
│ Final balance                 │ 1186.724 USDT                    │
│ Absolute profit               │ 186.724 USDT                     │
│ Total profit %                │ 18.67%                           │
│ CAGR %                        │ 4.74%                            │
│ Sortino                       │ 1.67                             │
│ Sharpe                        │ 0.29                             │
│ Calmar                        │ 2.04                             │
│ SQN                           │ 0.90                             │
│ Profit factor                 │ 1.16                             │
│ Expectancy (Ratio)            │ 0.36 (0.13)                      │
│ Avg. daily profit             │ 0.139 USDT                       │
│ Avg. stake amount             │ 123.744 USDT                     │
│ Total trade volume            │ 129386.211 USDT                  │
│                               │                                  │
│ Best Pair                     │ ETH/USDT 10.27%                  │
│ Worst Pair                    │ XRP/USDT -5.20%                  │
│ Best trade                    │ ETH/USDT 32.99%                  │
│ Worst trade                   │ XRP/USDT -15.15%                 │
│ Best day                      │ 45.488 USDT                      │
│ Worst day                     │ -20.603 USDT                     │
│ Days win/draw/lose            │ 68 / 949 / 296                   │
│ Min/Max/Avg. Duration Winners │ 0d 02:10 / 38d 21:00 / 13d 16:34 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 20d 06:00 / 1d 18:43  │
│ Max Consecutive Wins / Loss   │ 6 / 30                           │
│ Rejected Entry signals        │ 2904                             │
│ Entry/Exit Timeouts           │ 0 / 0                            │
│                               │                                  │
│ Min balance                   │ 931.756 USDT                     │
│ Max balance                   │ 1211.16 USDT                     │
│ Max % of account underwater   │ 12.97%                           │
│ Absolute drawdown             │ 157.111 USDT (12.97%)            │
│ Drawdown duration             │ 139 days 07:20:00                │
│ Profit at drawdown start      │ 211.16 USDT                      │
│ Profit at drawdown end        │ 54.049 USDT                      │
│ Drawdown start                │ 2024-12-18 06:40:00              │
│ Drawdown end                  │ 2025-05-06 14:00:00              │
│ Market change                 │ 91.49%                           │
└───────────────────────────────┴──────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                  
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃             Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ EMACrossOverStrategy │    521 │         0.36 │         186.724 │        18.67 │ 3 days, 17:21:00 │   85     0   436  16.3 │ 157.111 USDT  12.97% │
└──────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┴──────────────────────┘

```
