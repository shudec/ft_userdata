# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 8 / 0.02, Median: -1.65%, Total profit: -4.17%, Sortino: -0.37, Sharpe: -0.22, Calmar: -4.6, Drawdown: 0%)

---
            
**Strategy:** EMAMACDStrategy  
**Random State:** 8701  
**Timestamp:** 2025-09-16 17:09:44

## Configuration
```json
{
  "strategy": "EMAMACDStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 8701,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy EMAMACDStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 8701
```

## Hyperopt Output
```
2025-09-16 15:07:45,041 - freqtrade - INFO - freqtrade 2025.8
2025-09-16 15:07:46,272 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-16 15:07:49,247 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-16 15:07:49,255 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-16 15:07:49,256 - freqtrade.loggers - INFO - Logfile configured
2025-09-16 15:07:49,256 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-16 15:07:49,256 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-16 15:07:49,257 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-16 15:07:49,257 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-16 15:07:49,703 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-16 15:07:49,705 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-16 15:07:49,706 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-16 15:07:49,706 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 100 epochs ...
2025-09-16 15:07:49,707 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-16 15:07:49,707 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-16 15:07:49,707 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-16 15:07:49,708 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 8701
2025-09-16 15:07:49,708 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-16 15:07:49,708 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-16 15:07:49,709 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-16 15:07:49,709 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-16 15:07:49,711 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-16 15:07:49,728 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-16 15:07:49,729 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 15:07:49,732 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-16 15:07:49,742 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-16 15:07:49,748 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-16 15:07:49,749 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-16 15:07:49,774 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-16 15:07:52,473 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-16 15:07:52,563 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy EMAMACDStrategy from '/freqtrade/user_data/strategies/EMAMACDStrategy.py'...
2025-09-16 15:07:52,566 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/EMAMACDStrategy.json
2025-09-16 15:07:52,571 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-16 15:07:52,572 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-16 15:07:52,573 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-16 15:07:52,573 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-16 15:07:52,574 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-16 15:07:52,575 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-16 15:07:52,576 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-16 15:07:52,576 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-16 15:07:52,577 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-16 15:07:52,578 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-16 15:07:52,578 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-16 15:07:52,579 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-16 15:07:52,580 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-16 15:07:52,581 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-16 15:07:52,581 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-16 15:07:52,582 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-16 15:07:52,583 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-16 15:07:52,583 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-16 15:07:52,584 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-16 15:07:52,585 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-16 15:07:52,586 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-16 15:07:52,587 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-16 15:07:52,588 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-16 15:07:52,589 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-16 15:07:52,590 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-16 15:07:52,591 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-16 15:07:52,591 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-16 15:07:52,592 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-16 15:07:52,592 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-16 15:07:52,593 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 15:07:52,632 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-16 15:07:52,675 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-16 15:07:52,678 - freqtrade.strategy.hyper - INFO - Strategy Parameter: macd_threshold = -1
2025-09-16 15:07:52,679 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.333
2025-09-16 15:07:52,679 - freqtrade.strategy.hyper - INFO - Strategy Parameter: window_macd_cross = 4
2025-09-16 15:07:52,680 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-09-16 15:07:52,681 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.995
2025-09-16 15:07:52,681 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-16 15:07:52,682 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-16 15:07:52,683 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-16 15:07:52,724 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-16 15:07:52,725 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 8701
2025-09-16 15:07:52,837 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-16 15:07:52,961 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-16 15:07:52,984 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-16 15:07:53,057 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-16 15:07:53,134 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-16 15:07:53,209 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-16 15:07:53,223 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-16 15:07:53,247 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-16 15:07:54,409 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-16 15:08:05,714 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-16 15:08:06,115 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 16 CPU cores. Let's make them scream!
2025-09-16 15:08:06,117 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-16 15:08:06,119 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-16 15:08:06,119] A new study created in memory with name: no-name-73d2983e-ee06-4c4b-8eef-0b6c13db52bb
2025-09-16 15:08:06,187 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                            ┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓                            
                            ┃ Best   ┃  Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃ Avg duration ┃ Objective ┃    Max Drawdown (Acct) ┃                            
                            ┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩                            
                            │ * Best │  1/100 │      4 │    1     0     3  25.0 │     -1.66% │ -27.537 USDT   (-2.75%) │     12:15:00 │   0.07255 │ 29.725 USDT    (2.97%) │                            
                            │ * Best │  2/100 │      3 │    1     0     2  33.3 │     -1.76% │ -20.130 USDT   (-2.01%) │     13:40:00 │   0.05772 │ 22.153 USDT    (2.21%) │                            
                            │ * Best │ 12/100 │      3 │    1     0     2  33.3 │     -1.76% │ -20.510 USDT   (-2.05%) │     13:40:00 │   0.05765 │ 22.572 USDT    (2.25%) │                            
                            │ * Best │ 19/100 │      3 │    1     0     2  33.3 │     -1.98% │ -24.120 USDT   (-2.41%) │     13:20:00 │   0.05658 │ 26.265 USDT    (2.62%) │                            
                            └────────┴────────┴────────┴────────────────────────┴────────────┴─────────────────────────┴──────────────┴───────────┴────────────────────────┘                            
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100/100 100% • 0:01:14 • 0:00:00
2025-09-16 15:09:21,077 - freqtrade.optimize.hyperopt.hyperopt - INFO - 100 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_EMAMACDStrategy_2025-09-16_15-07-49.fthypt'.
2025-09-16 15:09:21,225 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/EMAMACDStrategy.json

Best result:

*   19/100:      3 trades. 1/0/2 Wins/Draws/Losses. Avg profit  -1.98%. Median profit  -1.65%. Total profit -24.12032259 USDT (  -2.41%). Avg duration 13:20:00 min. Objective: 0.05658

{"params":{"volume_factor":1.461,"window_macd_cross":7,"macd_threshold":-1,"stoploss_margin":0.998,"lookback_period_for_stoploss":5,"take_profit_multiplier":2,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy EMAMACDStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20221231
```

## Backtesting Output
```
2025-09-16 15:09:26,230 - freqtrade - INFO - freqtrade 2025.8
2025-09-16 15:09:26,707 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-16 15:09:29,236 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-16 15:09:29,242 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-16 15:09:29,243 - freqtrade.loggers - INFO - Logfile configured
2025-09-16 15:09:29,244 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-16 15:09:29,245 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-16 15:09:29,246 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-16 15:09:29,246 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-16 15:09:29,247 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20221231 ...
2025-09-16 15:09:29,656 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-16 15:09:29,659 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-16 15:09:29,659 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-16 15:09:29,660 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-16 15:09:29,661 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-16 15:09:29,662 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20221231
2025-09-16 15:09:29,663 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-16 15:09:29,676 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-16 15:09:29,677 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 15:09:29,681 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-16 15:09:29,682 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-16 15:09:29,682 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-16 15:09:29,704 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-16 15:09:32,292 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-16 15:09:32,350 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy EMAMACDStrategy from '/freqtrade/user_data/strategies/EMAMACDStrategy.py'...
2025-09-16 15:09:32,352 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/EMAMACDStrategy.json
2025-09-16 15:09:32,357 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-16 15:09:32,358 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-16 15:09:32,358 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-16 15:09:32,359 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-16 15:09:32,359 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-16 15:09:32,360 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-16 15:09:32,360 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-16 15:09:32,360 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-16 15:09:32,361 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-16 15:09:32,361 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-16 15:09:32,361 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-16 15:09:32,362 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-16 15:09:32,362 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-16 15:09:32,363 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-16 15:09:32,363 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-16 15:09:32,364 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-16 15:09:32,364 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-16 15:09:32,365 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-16 15:09:32,365 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-16 15:09:32,365 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-16 15:09:32,366 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-16 15:09:32,366 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-16 15:09:32,367 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-16 15:09:32,367 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-16 15:09:32,367 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-16 15:09:32,367 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-16 15:09:32,368 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-16 15:09:32,368 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-16 15:09:32,368 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 15:09:32,385 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-16 15:09:32,408 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-16 15:09:32,675 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2022-12-31 00:00:00 (364 days).
2025-09-16 15:09:34,920 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-16 15:09:34,938 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy EMAMACDStrategy
2025-09-16 15:09:34,938 - freqtrade.strategy.hyper - INFO - Strategy Parameter: macd_threshold = -1
2025-09-16 15:09:34,939 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1.461
2025-09-16 15:09:34,939 - freqtrade.strategy.hyper - INFO - Strategy Parameter: window_macd_cross = 7
2025-09-16 15:09:34,940 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-09-16 15:09:34,941 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-16 15:09:34,941 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-16 15:09:34,942 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-16 15:09:34,942 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-16 15:09:40,761 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2022-12-31 00:00:00 (364 days).
2025-09-16 15:09:42,759 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-16_15-09-42.meta.json"
Result for strategy EMAMACDStrategy
                                              BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ LTC/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│ XRP/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│ BNB/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│ ETH/USDT │      2 │         1.23 │          -2.365 │        -0.24 │ 1 day, 4:30:00 │    1     0     1  50.0 │
│ BTC/USDT │      6 │        -1.01 │         -39.353 │        -3.94 │       16:46:00 │    2     0     4  33.3 │
│    TOTAL │      8 │        -0.45 │         -41.718 │        -4.17 │       19:42:00 │    3     0     5  37.5 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
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
│     OTHER │       8 │        -0.45 │         -41.718 │        -4.17 │     19:42:00 │    3     0     5  37.5 │
│     TOTAL │       8 │        -0.45 │         -41.718 │        -4.17 │     19:42:00 │    3     0     5  37.5 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                               EXIT REASON STATS                                               
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│   stop_loss │     1 │        -3.21 │         -20.773 │        -2.08 │      2:35:00 │    0     0     1     0 │
│ exit_signal │     7 │        -0.06 │         -20.944 │        -2.09 │     22:09:00 │    3     0     4  42.9 │
│       TOTAL │     8 │        -0.45 │         -41.718 │        -4.17 │     19:42:00 │    3     0     5  37.5 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                      MIXED TAG STATS                                                       
┏━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │   stop_loss │      1 │        -3.21 │         -20.773 │        -2.08 │      2:35:00 │    0     0     1     0 │
│           │ exit_signal │      7 │        -0.06 │         -20.944 │        -2.09 │     22:09:00 │    3     0     4  42.9 │
│     TOTAL │             │      8 │        -0.45 │         -41.718 │        -4.17 │     19:42:00 │    3     0     5  37.5 │
└───────────┴─────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2022-12-31 00:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 8 / 0.02                       │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 958.282 USDT                   │
│ Absolute profit               │ -41.718 USDT                   │
│ Total profit %                │ -4.17%                         │
│ CAGR %                        │ -4.18%                         │
│ Sortino                       │ -0.37                          │
│ Sharpe                        │ -0.22                          │
│ Calmar                        │ -4.60                          │
│ SQN                           │ -1.36                          │
│ Profit factor                 │ 0.30                           │
│ Expectancy (Ratio)            │ -5.21 (-0.43)                  │
│ Avg. daily profit             │ -0.115 USDT                    │
│ Avg. stake amount             │ 531.735 USDT                   │
│ Total trade volume            │ 8482.994 USDT                  │
│                               │                                │
│ Best Pair                     │ LTC/USDT 0.00%                 │
│ Worst Pair                    │ BTC/USDT -3.94%                │
│ Best trade                    │ ETH/USDT 4.62%                 │
│ Worst trade                   │ BTC/USDT -3.21%                │
│ Best day                      │ 10.418 USDT                    │
│ Worst day                     │ -20.773 USDT                   │
│ Days win/draw/lose            │ 3 / 192 / 5                    │
│ Min/Max/Avg. Duration Winners │ 1d 06:00 / 2d 03:00 / 1d 18:00 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 0d 19:00 / 0d 06:19 │
│ Max Consecutive Wins / Loss   │ 1 / 2                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 952.361 USDT                   │
│ Max balance                   │ 987.113 USDT                   │
│ Max % of account underwater   │ 4.76%                          │
│ Absolute drawdown             │ 47.639 USDT (4.76%)            │
│ Drawdown duration             │ 66 days 11:00:00               │
│ Profit at drawdown start      │ -12.887 USDT                   │
│ Profit at drawdown end        │ -47.639 USDT                   │
│ Drawdown start                │ 2022-01-24 03:00:00            │
│ Drawdown end                  │ 2022-03-31 14:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                            STRATEGY SUMMARY                                                             
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃        Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ EMAMACDStrategy │      8 │        -0.45 │         -41.718 │        -4.17 │     19:42:00 │    3     0     5  37.5 │ 47.639 USDT  4.76% │
└─────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```
