# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 18 / 0.05, Median: -1.85%, Total profit: -19.73%, Sortino: -2.72, Sharpe: -0.58, Calmar: -5.21, Drawdown: 0%)

---
            
**Strategy:** EMAMACDStrategy  
**Random State:** 4699  
**Timestamp:** 2025-09-16 15:42:09

## Configuration
```json
{
  "strategy": "EMAMACDStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 4699,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy EMAMACDStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 4699
```

## Hyperopt Output
```
2025-09-16 13:39:58,817 - freqtrade - INFO - freqtrade 2025.8
2025-09-16 13:39:59,685 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-16 13:40:02,122 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-16 13:40:02,128 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-16 13:40:02,128 - freqtrade.loggers - INFO - Logfile configured
2025-09-16 13:40:02,129 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-16 13:40:02,129 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-16 13:40:02,130 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-16 13:40:02,130 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-16 13:40:02,481 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-16 13:40:02,484 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-16 13:40:02,484 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-16 13:40:02,484 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 100 epochs ...
2025-09-16 13:40:02,485 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-16 13:40:02,485 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-16 13:40:02,485 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-16 13:40:02,486 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 4699
2025-09-16 13:40:02,486 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-16 13:40:02,486 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-16 13:40:02,486 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-16 13:40:02,487 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-16 13:40:02,488 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-16 13:40:02,501 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-16 13:40:02,501 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 13:40:02,504 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-16 13:40:02,511 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-16 13:40:02,516 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-16 13:40:02,517 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-16 13:40:02,535 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-16 13:40:04,897 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-16 13:40:04,981 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy EMAMACDStrategy from '/freqtrade/user_data/strategies/EMAMACDStrategy.py'...
2025-09-16 13:40:04,983 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2025-09-16 13:40:04,984 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-16 13:40:04,985 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-16 13:40:04,985 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-16 13:40:04,986 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-16 13:40:04,987 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-16 13:40:04,987 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-16 13:40:04,988 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-16 13:40:04,988 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-16 13:40:04,989 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-16 13:40:04,990 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-16 13:40:04,990 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-16 13:40:04,991 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-16 13:40:04,991 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-16 13:40:04,992 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-16 13:40:04,993 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-16 13:40:04,993 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-16 13:40:04,995 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-16 13:40:04,996 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-16 13:40:04,997 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-16 13:40:04,998 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-16 13:40:04,999 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-16 13:40:04,999 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-16 13:40:05,000 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-16 13:40:05,001 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-16 13:40:05,001 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-16 13:40:05,002 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-16 13:40:05,002 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-16 13:40:05,003 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-16 13:40:05,003 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-16 13:40:05,004 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 13:40:05,036 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-16 13:40:05,064 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-16 13:40:05,066 - freqtrade.strategy.hyper - INFO - No params for buy found, using default values.
2025-09-16 13:40:05,066 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): volume_factor = 1.0
2025-09-16 13:40:05,067 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): window_macd_cross = 5
2025-09-16 13:40:05,067 - freqtrade.strategy.hyper - INFO - No params for sell found, using default values.
2025-09-16 13:40:05,068 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): lookback_period_for_stoploss = 5
2025-09-16 13:40:05,069 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): stoploss_margin = 0.999
2025-09-16 13:40:05,069 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): take_profit_multiplier = 2
2025-09-16 13:40:05,070 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_stoploss_param = True
2025-09-16 13:40:05,070 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-16 13:40:05,102 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-16 13:40:05,103 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 4699
2025-09-16 13:40:05,177 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-16 13:40:05,259 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-16 13:40:05,270 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-16 13:40:05,335 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-16 13:40:05,400 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-16 13:40:05,459 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-16 13:40:05,468 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-16 13:40:05,488 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-16 13:40:06,245 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-16 13:40:15,200 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-16 13:40:15,643 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 16 CPU cores. Let's make them scream!
2025-09-16 13:40:15,644 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-16 13:40:15,645 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-16 13:40:15,646] A new study created in memory with name: no-name-a90a8969-0715-4ee9-87e0-492cb286ab9b
2025-09-16 13:40:15,716 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                         ┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓                         
                         ┃ Best   ┃  Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                   Profit ┃     Avg duration ┃ Objective ┃     Max Drawdown (Acct) ┃                         
                         ┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩                         
                         │ * Best │  1/100 │     62 │   14     0    48  22.6 │     -1.24% │ -261.806 USDT  (-26.18%) │  3 days, 3:46:00 │   0.24925 │ 341.069 USDT   (31.60%) │                         
                         │ * Best │  2/100 │     10 │    1     0     9  10.0 │     -3.68% │ -127.146 USDT  (-12.71%) │ 2 days, 17:06:00 │   0.14924 │ 130.265 USDT   (12.99%) │                         
                         │ * Best │  3/100 │      7 │    1     0     6  14.3 │     -4.01% │  -65.270 USDT   (-6.53%) │ 3 days, 18:26:00 │   0.06002 │  74.376 USDT    (7.37%) │                         
                         │ Best   │ 33/100 │     63 │   19     0    44  30.2 │     -0.66% │  -61.794 USDT   (-6.18%) │ 2 days, 10:53:00 │   0.05237 │ 171.878 USDT   (16.53%) │                         
                         │ Best   │ 54/100 │     61 │   19     0    42  31.1 │     -0.61% │  -30.257 USDT   (-3.03%) │ 2 days, 12:25:00 │   0.02514 │ 171.878 USDT   (16.53%) │                         
                         └────────┴────────┴────────┴────────────────────────┴────────────┴──────────────────────────┴──────────────────┴───────────┴─────────────────────────┘                         
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100/100 100% • 0:01:30 • 0:00:00
2025-09-16 13:41:46,294 - freqtrade.optimize.hyperopt.hyperopt - INFO - 100 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_EMAMACDStrategy_2025-09-16_13-40-02.fthypt'.
2025-09-16 13:41:46,400 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/EMAMACDStrategy.json

Best result:

    54/100:     61 trades. 19/0/42 Wins/Draws/Losses. Avg profit  -0.61%. Median profit  -1.85%. Total profit -30.25685819 USDT (  -3.03%). Avg duration 2 days, 12:25:00 min. Objective: 0.02514

{"params":{"volume_factor":0.406,"window_macd_cross":3,"stoploss_margin":0.998,"lookback_period_for_stoploss":5,"take_profit_multiplier":2,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy EMAMACDStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20221231
```

## Backtesting Output
```
2025-09-16 13:41:50,186 - freqtrade - INFO - freqtrade 2025.8
2025-09-16 13:41:50,607 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-16 13:41:52,367 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-16 13:41:52,377 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-16 13:41:52,379 - freqtrade.loggers - INFO - Logfile configured
2025-09-16 13:41:52,379 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-16 13:41:52,381 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-16 13:41:52,382 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-16 13:41:52,383 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-16 13:41:52,383 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20221231 ...
2025-09-16 13:41:52,741 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-16 13:41:52,743 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-16 13:41:52,744 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-16 13:41:52,744 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-16 13:41:52,745 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-16 13:41:52,745 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20221231
2025-09-16 13:41:52,746 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-16 13:41:52,761 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-16 13:41:52,762 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 13:41:52,765 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-16 13:41:52,766 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-16 13:41:52,767 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-16 13:41:52,795 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-16 13:41:55,097 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-16 13:41:55,158 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy EMAMACDStrategy from '/freqtrade/user_data/strategies/EMAMACDStrategy.py'...
2025-09-16 13:41:55,161 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/EMAMACDStrategy.json
2025-09-16 13:41:55,166 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-16 13:41:55,166 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-16 13:41:55,167 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-16 13:41:55,167 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-16 13:41:55,167 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-16 13:41:55,168 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-16 13:41:55,168 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-16 13:41:55,169 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-16 13:41:55,169 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-16 13:41:55,169 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-16 13:41:55,170 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-16 13:41:55,170 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-16 13:41:55,171 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-16 13:41:55,171 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-16 13:41:55,171 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-16 13:41:55,172 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-16 13:41:55,172 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-16 13:41:55,173 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-16 13:41:55,174 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-16 13:41:55,175 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-16 13:41:55,175 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-16 13:41:55,176 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-16 13:41:55,177 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-16 13:41:55,177 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-16 13:41:55,178 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-16 13:41:55,178 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-16 13:41:55,178 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-16 13:41:55,179 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-16 13:41:55,179 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 13:41:55,197 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-16 13:41:55,225 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-16 13:41:55,517 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2022-12-31 00:00:00 (364 days).
2025-09-16 13:41:57,407 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-16 13:41:57,423 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy EMAMACDStrategy
2025-09-16 13:41:57,424 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 0.406
2025-09-16 13:41:57,425 - freqtrade.strategy.hyper - INFO - Strategy Parameter: window_macd_cross = 3
2025-09-16 13:41:57,426 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-09-16 13:41:57,427 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.998
2025-09-16 13:41:57,427 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-16 13:41:57,428 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-16 13:41:57,428 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-16 13:42:02,604 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2022-12-31 00:00:00 (364 days).
2025-09-16 13:42:08,260 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-16_13-42-08.meta.json"
Result for strategy EMAMACDStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ LTC/USDT │      1 │        -4.07 │         -20.643 │        -2.06 │          1:00:00 │    0     0     1     0 │
│ BNB/USDT │      5 │        -1.03 │         -31.659 │        -3.17 │         19:55:00 │    1     0     4  20.0 │
│ ETH/USDT │      2 │        -3.12 │         -33.211 │        -3.32 │   1 day, 1:38:00 │    0     0     2     0 │
│ BTC/USDT │      6 │          0.8 │         -36.692 │        -3.67 │ 3 days, 15:28:00 │    1     0     5  16.7 │
│ XRP/USDT │      4 │        -2.29 │         -75.107 │        -7.51 │         16:44:00 │    0     0     4     0 │
│    TOTAL │     18 │         -1.1 │        -197.312 │       -19.73 │  1 day, 17:19:00 │    2     0    16  11.1 │
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
│     OTHER │      18 │         -1.1 │        -197.312 │       -19.73 │ 1 day, 17:19:00 │    2     0    16  11.1 │
│     TOTAL │      18 │         -1.1 │        -197.312 │       -19.73 │ 1 day, 17:19:00 │    2     0    16  11.1 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │     2 │        10.58 │          76.352 │         7.64 │ 10 days, 7:55:00 │    2     0     0   100 │
│      stop_loss │    16 │        -2.56 │        -273.664 │       -27.37 │         15:29:00 │    0     0    16     0 │
│          TOTAL │    18 │         -1.1 │        -197.312 │       -19.73 │  1 day, 17:19:00 │    2     0    16  11.1 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                          MIXED TAG STATS                                                          
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │      2 │        10.58 │          76.352 │         7.64 │ 10 days, 7:55:00 │    2     0     0   100 │
│           │      stop_loss │     16 │        -2.56 │        -273.664 │       -27.37 │         15:29:00 │    0     0    16     0 │
│     TOTAL │                │     18 │         -1.1 │        -197.312 │       -19.73 │  1 day, 17:19:00 │    2     0    16  11.1 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                          SUMMARY METRICS                           
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                            ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00              │
│ Backtesting to                │ 2022-12-31 00:00:00              │
│ Trading Mode                  │ Spot                             │
│ Max open trades               │ 3                                │
│                               │                                  │
│ Total/Daily Avg Trades        │ 18 / 0.05                        │
│ Starting balance              │ 1000 USDT                        │
│ Final balance                 │ 802.688 USDT                     │
│ Absolute profit               │ -197.312 USDT                    │
│ Total profit %                │ -19.73%                          │
│ CAGR %                        │ -19.78%                          │
│ Sortino                       │ -2.72                            │
│ Sharpe                        │ -0.58                            │
│ Calmar                        │ -5.21                            │
│ SQN                           │ -2.55                            │
│ Profit factor                 │ 0.28                             │
│ Expectancy (Ratio)            │ -10.96 (-0.64)                   │
│ Avg. daily profit             │ -0.542 USDT                      │
│ Avg. stake amount             │ 727.967 USDT                     │
│ Total trade volume            │ 26061.577 USDT                   │
│                               │                                  │
│ Best Pair                     │ LTC/USDT -2.06%                  │
│ Worst Pair                    │ XRP/USDT -7.51%                  │
│ Best trade                    │ BTC/USDT 17.02%                  │
│ Worst trade                   │ BTC/USDT -4.92%                  │
│ Best day                      │ 38.373 USDT                      │
│ Worst day                     │ -20.94 USDT                      │
│ Days win/draw/lose            │ 2 / 312 / 16                     │
│ Min/Max/Avg. Duration Winners │ 1d 04:10 / 19d 11:40 / 10d 07:55 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 1d 23:00 / 0d 15:29   │
│ Max Consecutive Wins / Loss   │ 1 / 11                           │
│ Rejected Entry signals        │ 0                                │
│ Entry/Exit Timeouts           │ 0 / 0                            │
│                               │                                  │
│ Min balance                   │ 802.688 USDT                     │
│ Max balance                   │ 1001.791 USDT                    │
│ Max % of account underwater   │ 19.87%                           │
│ Absolute drawdown             │ 199.102 USDT (19.87%)            │
│ Drawdown duration             │ 277 days 19:10:00                │
│ Profit at drawdown start      │ 1.791 USDT                       │
│ Profit at drawdown end        │ -197.312 USDT                    │
│ Drawdown start                │ 2022-03-16 21:10:00              │
│ Drawdown end                  │ 2022-12-19 16:20:00              │
│ Market change                 │ -59.72%                          │
└───────────────────────────────┴──────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                               STRATEGY SUMMARY                                                               
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃        Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ EMAMACDStrategy │     18 │        -1.10 │        -197.312 │       -19.73 │ 1 day, 17:19:00 │    2     0    16  11.1 │ 199.102 USDT  19.87% │
└─────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┴──────────────────────┘

```
