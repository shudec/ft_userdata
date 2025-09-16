# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 66 / 0.18, Median: -5.0%, Total profit: -20.7%, Sortino: -2.39, Sharpe: -0.81, Calmar: -5.22, Drawdown: 0%)

---
            
**Strategy:** EMACrossOverStrategy  
**Random State:** 1113  
**Timestamp:** 2025-09-16 17:35:04

## Configuration
```json
{
  "strategy": "EMACrossOverStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 1113,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy EMACrossOverStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 1113
```

## Hyperopt Output
```
2025-09-16 15:32:56,935 - freqtrade - INFO - freqtrade 2025.8
2025-09-16 15:32:57,454 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-16 15:32:58,885 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-16 15:32:58,892 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-16 15:32:58,893 - freqtrade.loggers - INFO - Logfile configured
2025-09-16 15:32:58,893 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-16 15:32:58,894 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-16 15:32:58,894 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-16 15:32:58,894 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-16 15:32:59,272 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-16 15:32:59,274 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-16 15:32:59,275 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-16 15:32:59,276 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 100 epochs ...
2025-09-16 15:32:59,276 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['sell']
2025-09-16 15:32:59,277 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-16 15:32:59,277 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-16 15:32:59,277 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 1113
2025-09-16 15:32:59,278 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-16 15:32:59,278 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-16 15:32:59,278 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-16 15:32:59,279 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-16 15:32:59,280 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-16 15:32:59,291 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-16 15:32:59,292 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 15:32:59,295 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-16 15:32:59,303 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-16 15:32:59,309 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-16 15:32:59,310 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-16 15:32:59,332 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-16 15:33:01,645 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-16 15:33:01,697 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy EMACrossOverStrategy from '/freqtrade/user_data/strategies/EMACrossOverStrategy.py'...
2025-09-16 15:33:01,699 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/EMACrossOverStrategy.json
2025-09-16 15:33:01,703 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-16 15:33:01,703 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-16 15:33:01,704 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-16 15:33:01,704 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-16 15:33:01,704 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-16 15:33:01,705 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-16 15:33:01,705 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-16 15:33:01,705 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-16 15:33:01,706 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-16 15:33:01,706 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: True
2025-09-16 15:33:01,706 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-16 15:33:01,707 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-16 15:33:01,707 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-16 15:33:01,707 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-16 15:33:01,707 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-16 15:33:01,708 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-16 15:33:01,708 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-16 15:33:01,708 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-16 15:33:01,709 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-16 15:33:01,709 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-16 15:33:01,709 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-16 15:33:01,710 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-16 15:33:01,710 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-16 15:33:01,710 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-16 15:33:01,711 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-16 15:33:01,712 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-16 15:33:01,712 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-16 15:33:01,713 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-16 15:33:01,713 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-16 15:33:01,714 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 15:33:01,728 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-16 15:33:01,752 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-16 15:33:01,753 - freqtrade.strategy.hyper - INFO - No params for buy found, using default values.
2025-09-16 15:33:01,753 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-09-16 15:33:01,754 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-09-16 15:33:01,754 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-16 15:33:01,754 - freqtrade.strategy.hyper - INFO - Strategy Parameter: threshold_percentage = 9
2025-09-16 15:33:01,755 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-16 15:33:01,755 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-16 15:33:01,770 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-16 15:33:01,770 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 1113
2025-09-16 15:33:01,817 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-16 15:33:01,875 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-16 15:33:01,883 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-16 15:33:01,927 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-16 15:33:01,974 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-16 15:33:02,025 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-16 15:33:02,033 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-16 15:33:02,045 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-16 15:33:02,590 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-16 15:33:02,671 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-16 15:33:03,047 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 16 CPU cores. Let's make them scream!
2025-09-16 15:33:03,049 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-16 15:33:03,049 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-16 15:33:03,050] A new study created in memory with name: no-name-21b34097-7dea-4f3a-92ae-9b327198d6e9
2025-09-16 15:33:03,102 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
2025-09-16 15:33:23,381 - freqtrade.optimize.hyperopt.hyperopt - WARNING - Duplicate params detected. Maybe your search space is too small?
                                                                                           Hyperopt results                                                                                             
                         ┏━━━━━━━━┳━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓                          
                         ┃ Best   ┃ Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                   Profit ┃     Avg duration ┃ Objective ┃     Max Drawdown (Acct) ┃                          
                         ┡━━━━━━━━╇━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩                          
                         │ * Best │ 1/100 │    181 │   57     0   124  31.5 │     -0.81% │ -228.019 USDT  (-22.80%) │ 4 days, 23:12:00 │   0.35353 │ 367.854 USDT   (35.70%) │                          
                         └────────┴───────┴────────┴────────────────────────┴────────────┴──────────────────────────┴──────────────────┴───────────┴─────────────────────────┘                          
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━╸                                                                                                                                        16/100  16% • 0:00:40 • 0:01:48
2025-09-16 15:33:43,689 - freqtrade.optimize.hyperopt.hyperopt - INFO - 84 epochs skipped due to duplicate parameters.
2025-09-16 15:33:43,690 - freqtrade.optimize.hyperopt.hyperopt - INFO - 16 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_EMACrossOverStrategy_2025-09-16_15-32-59.fthypt'.
2025-09-16 15:33:43,795 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/EMACrossOverStrategy.json

Best result:

*    1/100:    181 trades. 57/0/124 Wins/Draws/Losses. Avg profit  -0.81%. Median profit  -5.00%. Total profit -228.01870053 USDT ( -22.80%). Avg duration 4 days, 23:12:00 min. Objective: 0.35353

{"params":{"threshold_percentage":10,"lookback_period_for_stoploss":5,"stoploss_margin":0.999,"take_profit_multiplier":2,"use_custom_stoploss_param":false},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":true,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy EMACrossOverStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20221231
```

## Backtesting Output
```
2025-09-16 15:33:47,194 - freqtrade - INFO - freqtrade 2025.8
2025-09-16 15:33:47,520 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-16 15:33:49,163 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-16 15:33:49,170 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-16 15:33:49,171 - freqtrade.loggers - INFO - Logfile configured
2025-09-16 15:33:49,171 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-16 15:33:49,172 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-16 15:33:49,173 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-16 15:33:49,173 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-16 15:33:49,175 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20221231 ...
2025-09-16 15:33:49,575 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-16 15:33:49,577 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-16 15:33:49,578 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-16 15:33:49,578 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-16 15:33:49,579 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-16 15:33:49,579 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20221231
2025-09-16 15:33:49,580 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-16 15:33:49,592 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-16 15:33:49,593 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 15:33:49,596 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-16 15:33:49,597 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-16 15:33:49,597 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-16 15:33:49,625 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-16 15:33:52,235 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-16 15:33:52,301 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy EMACrossOverStrategy from '/freqtrade/user_data/strategies/EMACrossOverStrategy.py'...
2025-09-16 15:33:52,303 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/EMACrossOverStrategy.json
2025-09-16 15:33:52,307 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-16 15:33:52,308 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-16 15:33:52,308 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-16 15:33:52,309 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-16 15:33:52,309 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-16 15:33:52,309 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-16 15:33:52,310 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-16 15:33:52,310 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-16 15:33:52,311 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: True
2025-09-16 15:33:52,311 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-16 15:33:52,312 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-16 15:33:52,312 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-16 15:33:52,313 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-16 15:33:52,313 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-16 15:33:52,314 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-16 15:33:52,314 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-16 15:33:52,314 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-16 15:33:52,315 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-16 15:33:52,315 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-16 15:33:52,315 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-16 15:33:52,316 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-16 15:33:52,316 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-16 15:33:52,316 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-16 15:33:52,317 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-16 15:33:52,317 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-16 15:33:52,317 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-16 15:33:52,318 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-16 15:33:52,318 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-16 15:33:52,318 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 15:33:52,337 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-16 15:33:52,360 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-16 15:33:52,593 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2022-12-31 00:00:00 (364 days).
2025-09-16 15:33:54,285 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-16 15:33:54,302 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy EMACrossOverStrategy
2025-09-16 15:33:54,303 - freqtrade.strategy.hyper - INFO - No params for buy found, using default values.
2025-09-16 15:33:54,304 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-09-16 15:33:54,305 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-09-16 15:33:54,305 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-16 15:33:54,305 - freqtrade.strategy.hyper - INFO - Strategy Parameter: threshold_percentage = 10
2025-09-16 15:33:54,306 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = False
2025-09-16 15:33:54,306 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-16 15:33:54,345 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2022-12-31 00:00:00 (364 days).
2025-09-16 15:35:03,053 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-16_15-35-03.meta.json"
Result for strategy EMACrossOverStrategy
                                                BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ LTC/USDT │     11 │         0.42 │           3.079 │         0.31 │   5 days, 9:41:00 │    4     0     7  36.4 │
│ ETH/USDT │     14 │        -0.32 │         -15.302 │        -1.53 │  4 days, 22:26:00 │    3     0    11  21.4 │
│ BTC/USDT │     11 │        -3.43 │         -52.672 │        -5.27 │ 10 days, 23:24:00 │    3     0     8  27.3 │
│ XRP/USDT │     18 │        -2.59 │         -54.820 │        -5.48 │   6 days, 9:19:00 │    4     0    14  22.2 │
│ BNB/USDT │     12 │        -4.35 │         -87.295 │        -8.73 │  6 days, 21:12:00 │    2     0    10  16.7 │
│    TOTAL │     66 │        -2.07 │        -207.011 │        -20.7 │  6 days, 18:29:00 │   16     0    50  24.2 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴───────────────────┴────────────────────────┘
                                             LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ LTC/USDT │      1 │        -2.29 │          -3.608 │        -0.36 │ 4 days, 21:00:00 │    0     0     1     0 │
│    TOTAL │      1 │        -2.29 │          -3.608 │        -0.36 │ 4 days, 21:00:00 │    0     0     1     0 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                  ENTER TAG STATS                                                  
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │      66 │        -2.07 │        -207.011 │        -20.7 │ 6 days, 18:29:00 │   16     0    50  24.2 │
│     TOTAL │      66 │        -2.07 │        -207.011 │        -20.7 │ 6 days, 18:29:00 │   16     0    50  24.2 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                    EXIT REASON STATS                                                     
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     take_profit_2R │     8 │        20.47 │         232.801 │        23.28 │ 6 days, 15:14:00 │    8     0     0   100 │
│         force_exit │     1 │        -2.29 │          -3.608 │        -0.36 │ 4 days, 21:00:00 │    0     0     1     0 │
│ trailing_stop_loss │    57 │        -5.23 │        -436.204 │       -43.62 │ 6 days, 19:44:00 │    8     0    49  14.0 │
│              TOTAL │    66 │        -2.07 │        -207.011 │        -20.7 │ 6 days, 18:29:00 │   16     0    50  24.2 │
└────────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                            MIXED TAG STATS                                                            
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃        Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │     take_profit_2R │      8 │        20.47 │         232.801 │        23.28 │ 6 days, 15:14:00 │    8     0     0   100 │
│           │         force_exit │      1 │        -2.29 │          -3.608 │        -0.36 │ 4 days, 21:00:00 │    0     0     1     0 │
│           │ trailing_stop_loss │     57 │        -5.23 │        -436.204 │       -43.62 │ 6 days, 19:44:00 │    8     0    49  14.0 │
│     TOTAL │                    │     66 │        -2.07 │        -207.011 │        -20.7 │ 6 days, 18:29:00 │   16     0    50  24.2 │
└───────────┴────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                          SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00             │
│ Backtesting to                │ 2022-12-31 00:00:00             │
│ Trading Mode                  │ Spot                            │
│ Max open trades               │ 3                               │
│                               │                                 │
│ Total/Daily Avg Trades        │ 66 / 0.18                       │
│ Starting balance              │ 1000 USDT                       │
│ Final balance                 │ 792.989 USDT                    │
│ Absolute profit               │ -207.011 USDT                   │
│ Total profit %                │ -20.70%                         │
│ CAGR %                        │ -20.75%                         │
│ Sortino                       │ -2.39                           │
│ Sharpe                        │ -0.81                           │
│ Calmar                        │ -5.22                           │
│ SQN                           │ -1.88                           │
│ Profit factor                 │ 0.56                            │
│ Expectancy (Ratio)            │ -3.14 (-0.33)                   │
│ Avg. daily profit             │ -0.569 USDT                     │
│ Avg. stake amount             │ 148.937 USDT                    │
│ Total trade volume            │ 19491.565 USDT                  │
│                               │                                 │
│ Best Pair                     │ LTC/USDT 0.31%                  │
│ Worst Pair                    │ BNB/USDT -8.73%                 │
│ Best trade                    │ ETH/USDT 21.01%                 │
│ Worst trade                   │ BNB/USDT -10.11%                │
│ Best day                      │ 61.037 USDT                     │
│ Worst day                     │ -35.623 USDT                    │
│ Days win/draw/lose            │ 9 / 279 / 36                    │
│ Min/Max/Avg. Duration Winners │ 1d 09:50 / 24d 09:30 / 8d 23:54 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:20 / 25d 12:40 / 6d 01:23 │
│ Max Consecutive Wins / Loss   │ 4 / 10                          │
│ Rejected Entry signals        │ 444                             │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 792.989 USDT                    │
│ Max balance                   │ 1001.653 USDT                   │
│ Max % of account underwater   │ 20.83%                          │
│ Absolute drawdown             │ 208.664 USDT (20.83%)           │
│ Drawdown duration             │ 322 days 05:00:00               │
│ Profit at drawdown start      │ 1.653 USDT                      │
│ Profit at drawdown end        │ -207.011 USDT                   │
│ Drawdown start                │ 2022-02-11 19:00:00             │
│ Drawdown end                  │ 2022-12-31 00:00:00             │
│ Market change                 │ -59.72%                         │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                  STRATEGY SUMMARY                                                                  
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃             Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ EMACrossOverStrategy │     66 │        -2.07 │        -207.011 │        -20.7 │ 6 days, 18:29:00 │   16     0    50  24.2 │ 208.664 USDT  20.83% │
└──────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┴──────────────────────┘

```
