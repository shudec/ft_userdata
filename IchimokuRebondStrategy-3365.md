# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 69 / 0.05, Median: -1.33%, Total profit: -34.82%, Sortino: -1.34, Sharpe: -0.29, Calmar: -1.41, Drawdown: 0%)

---
            
**Strategy:** IchimokuRebondStrategy  
**Random State:** 3365  
**Timestamp:** 2025-09-17 18:08:20

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 3365,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 3365
```

## Hyperopt Output
```
2025-09-17 16:04:35,116 - freqtrade - INFO - freqtrade 2025.8
2025-09-17 16:04:36,101 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-17 16:04:38,365 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-17 16:04:38,376 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-17 16:04:38,378 - freqtrade.loggers - INFO - Logfile configured
2025-09-17 16:04:38,379 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-17 16:04:38,380 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-17 16:04:38,381 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-17 16:04:38,382 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-17 16:04:38,766 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-17 16:04:38,769 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-17 16:04:38,770 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-17 16:04:38,771 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 100 epochs ...
2025-09-17 16:04:38,772 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-17 16:04:38,773 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-17 16:04:38,774 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-17 16:04:38,775 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 3365
2025-09-17 16:04:38,776 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-17 16:04:38,777 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-17 16:04:38,778 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-17 16:04:38,779 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-17 16:04:38,781 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-17 16:04:38,807 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-17 16:04:38,809 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 16:04:38,813 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-17 16:04:38,826 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-17 16:04:38,827 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-17 16:04:38,874 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-17 16:04:41,700 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-17 16:04:41,820 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-17 16:04:41,825 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-17 16:04:41,831 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-17 16:04:41,832 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-17 16:04:41,833 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-17 16:04:41,833 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-17 16:04:41,834 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-17 16:04:41,835 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-17 16:04:41,836 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-17 16:04:41,836 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-17 16:04:41,837 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-17 16:04:41,837 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-17 16:04:41,838 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-17 16:04:41,839 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-17 16:04:41,839 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-17 16:04:41,841 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-17 16:04:41,842 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-17 16:04:41,843 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-17 16:04:41,844 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-17 16:04:41,845 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-17 16:04:41,846 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-17 16:04:41,846 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-17 16:04:41,847 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-17 16:04:41,847 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-17 16:04:41,848 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-17 16:04:41,848 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-17 16:04:41,849 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-17 16:04:41,849 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-17 16:04:41,850 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-17 16:04:41,850 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-17 16:04:41,851 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-17 16:04:41,852 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 16:04:41,879 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-17 16:04:41,915 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-17 16:04:41,917 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.499
2025-09-17 16:04:41,918 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.658
2025-09-17 16:04:41,918 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.01
2025-09-17 16:04:41,919 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0
2025-09-17 16:04:41,920 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 10
2025-09-17 16:04:41,921 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 1.0
2025-09-17 16:04:41,921 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-17 16:04:41,922 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-17 16:04:41,922 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-17 16:04:41,923 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-17 16:04:41,949 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-17 16:04:41,949 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 3365
2025-09-17 16:04:42,023 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-17 16:04:42,122 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-17 16:04:42,137 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-17 16:04:42,241 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-17 16:04:42,466 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-17 16:04:42,618 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-17 16:04:42,639 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-17 16:04:42,681 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-17 16:04:43,627 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-17 16:04:43,631 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 16:04:43,662 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-17 16:04:47,061 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 16:04:47,083 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-17 16:04:50,975 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 16:04:50,996 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-17 16:04:53,927 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 16:04:53,951 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-17 16:04:55,892 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 16:04:55,909 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-17 16:04:59,060 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-17 16:04:59,582 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 16 CPU cores. Let's make them scream!
2025-09-17 16:04:59,582 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-17 16:04:59,584 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-17 16:04:59,584] A new study created in memory with name: no-name-1abea58c-1a2f-4950-be8f-e31e90a37af2
2025-09-17 16:04:59,657 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                          ┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓                          
                          ┃ Best   ┃  Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃    Avg duration ┃ Objective ┃     Max Drawdown (Acct) ┃                          
                          ┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩                          
                          │ * Best │  2/100 │     22 │    8     0    14  36.4 │     -0.34% │ -29.427 USDT   (-2.94%) │         6:33:00 │   0.03715 │ 110.193 USDT   (10.75%) │                          
                          │ * Best │  4/100 │      4 │    1     0     3  25.0 │     -0.62% │ -27.181 USDT   (-2.72%) │         6:00:00 │   0.02405 │  63.628 USDT    (6.14%) │                          
                          │ * Best │  6/100 │     20 │    7     0    13  35.0 │     -0.05% │  -9.440 USDT   (-0.94%) │         5:30:00 │   0.01268 │  46.851 USDT    (4.52%) │                          
                          │ * Best │  8/100 │      4 │    2     0     2  50.0 │      1.94% │  76.997 USDT    (7.70%) │ 1 day, 10:15:00 │  -0.04083 │  43.762 USDT    (4.16%) │                          
                          │ * Best │ 10/100 │      6 │    3     0     3  50.0 │      2.18% │  87.122 USDT    (8.71%) │         8:40:00 │  -0.05712 │  35.807 USDT    (3.58%) │                          
                          │ * Best │ 30/100 │     43 │   14     0    29  32.6 │      0.90% │ 336.811 USDT   (33.68%) │        11:43:00 │  -0.16932 │ 117.939 USDT   (10.13%) │                          
                          │ Best   │ 64/100 │     48 │   14     0    34  29.2 │      0.85% │ 326.345 USDT   (32.63%) │        11:32:00 │  -0.16935 │ 117.848 USDT    (9.93%) │                          
                          └────────┴────────┴────────┴────────────────────────┴────────────┴─────────────────────────┴─────────────────┴───────────┴─────────────────────────┘                          
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100/100 100% • 0:02:22 • 0:00:00
2025-09-17 16:07:22,128 - freqtrade.optimize.hyperopt.hyperopt - INFO - 100 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-17_16-04-38.fthypt'.
2025-09-17 16:07:22,300 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

    64/100:     48 trades. 14/0/34 Wins/Draws/Losses. Avg profit   0.85%. Median profit  -1.33%. Total profit 326.34503981 USDT (  32.63%). Avg duration 11:32:00 min. Objective: -0.16935

{"params":{"hammer_body_threshold":0.655,"hammer_head_threshold":0.937,"hammer_strength_threshold":0.007,"kinjun_threshold":0,"lookback_period_for_stoploss":4,"stoploss_margin":0.996,"take_profit_multiplier":2.5,"use_sell_signal_param":false,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231
```

## Backtesting Output
```
2025-09-17 16:07:27,390 - freqtrade - INFO - freqtrade 2025.8
2025-09-17 16:07:28,264 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-17 16:07:31,752 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-17 16:07:31,760 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-17 16:07:31,761 - freqtrade.loggers - INFO - Logfile configured
2025-09-17 16:07:31,762 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-17 16:07:31,762 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-17 16:07:31,763 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-17 16:07:31,763 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-17 16:07:31,764 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-17 16:07:32,170 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-17 16:07:32,173 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-17 16:07:32,174 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-17 16:07:32,174 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-17 16:07:32,175 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-17 16:07:32,175 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-17 16:07:32,177 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-17 16:07:32,198 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-17 16:07:32,199 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 16:07:32,205 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-17 16:07:32,206 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-17 16:07:32,207 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-17 16:07:32,242 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-17 16:07:35,072 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-17 16:07:35,196 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-17 16:07:35,199 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-17 16:07:35,206 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-17 16:07:35,207 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-17 16:07:35,208 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-17 16:07:35,209 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-17 16:07:35,210 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-17 16:07:35,211 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-17 16:07:35,212 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-17 16:07:35,213 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-17 16:07:35,214 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-17 16:07:35,215 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-17 16:07:35,216 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-17 16:07:35,216 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-17 16:07:35,217 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-17 16:07:35,218 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-17 16:07:35,218 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-17 16:07:35,219 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-17 16:07:35,219 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-17 16:07:35,220 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-17 16:07:35,221 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-17 16:07:35,223 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-17 16:07:35,224 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-17 16:07:35,226 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-17 16:07:35,227 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-17 16:07:35,229 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-17 16:07:35,230 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-17 16:07:35,231 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-17 16:07:35,232 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-17 16:07:35,233 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-17 16:07:35,235 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 16:07:35,269 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-17 16:07:35,314 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-17 16:07:35,400 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 16:07:35,497 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 16:07:35,626 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 16:07:35,713 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 16:07:35,816 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 16:07:35,863 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-17 16:07:36,483 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 16:07:37,312 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 16:07:38,012 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 16:07:39,093 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 16:07:39,812 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 16:07:41,963 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-17 16:07:41,973 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-17 16:07:41,974 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-17 16:07:41,975 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.655
2025-09-17 16:07:41,977 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.937
2025-09-17 16:07:41,977 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.007
2025-09-17 16:07:41,979 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0
2025-09-17 16:07:41,980 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 4
2025-09-17 16:07:41,981 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.996
2025-09-17 16:07:41,983 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2.5
2025-09-17 16:07:41,984 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-17 16:07:41,985 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-17 16:07:41,986 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-17 16:07:41,991 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 16:07:42,025 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 16:07:48,189 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 16:07:48,214 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 16:07:53,113 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 16:07:53,135 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 16:07:57,190 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 16:07:57,216 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 16:08:01,523 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 16:08:01,548 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 16:08:06,186 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-17 16:08:19,001 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-17_16-08-18.meta.json"
Result for strategy IchimokuRebondStrategy
                                              BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │     10 │         0.82 │          41.498 │         4.15 │ 1 day, 0:54:00 │    3     0     7  30.0 │
│ BNB/USDT │     11 │        -0.08 │          -9.603 │        -0.96 │       19:33:00 │    3     0     8  27.3 │
│ XRP/USDT │     22 │        -0.84 │        -110.097 │       -11.01 │       13:17:00 │    4     0    18  18.2 │
│ ETH/USDT │     10 │        -1.56 │        -127.726 │       -12.77 │       16:26:00 │    0     0    10     0 │
│ LTC/USDT │     16 │        -1.27 │        -142.223 │       -14.22 │       10:30:00 │    1     0    15   6.2 │
│    TOTAL │     69 │        -0.68 │        -348.152 │       -34.82 │       15:46:00 │   11     0    58  15.9 │
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
│     OTHER │      69 │        -0.68 │        -348.152 │       -34.82 │     15:46:00 │   11     0    58  15.9 │
│     TOTAL │      69 │        -0.68 │        -348.152 │       -34.82 │     15:46:00 │   11     0    58  15.9 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                   EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2.5R │    11 │         4.37 │         350.357 │        35.04 │ 1 day, 23:05:00 │   11     0     0   100 │
│        stop_loss │    58 │        -1.64 │        -698.509 │       -69.85 │         9:50:00 │    0     0    58     0 │
│            TOTAL │    69 │        -0.68 │        -348.152 │       -34.82 │        15:46:00 │   11     0    58  15.9 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                          MIXED TAG STATS                                                           
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2.5R │     11 │         4.37 │         350.357 │        35.04 │ 1 day, 23:05:00 │   11     0     0   100 │
│           │        stop_loss │     58 │        -1.64 │        -698.509 │       -69.85 │         9:50:00 │    0     0    58     0 │
│     TOTAL │                  │     69 │        -0.68 │        -348.152 │       -34.82 │        15:46:00 │   11     0    58  15.9 │
└───────────┴──────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 69 / 0.05                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 651.848 USDT                   │
│ Absolute profit               │ -348.152 USDT                  │
│ Total profit %                │ -34.82%                        │
│ CAGR %                        │ -10.94%                        │
│ Sortino                       │ -1.34                          │
│ Sharpe                        │ -0.29                          │
│ Calmar                        │ -1.41                          │
│ SQN                           │ -2.49                          │
│ Profit factor                 │ 0.50                           │
│ Expectancy (Ratio)            │ -5.05 (-0.42)                  │
│ Avg. daily profit             │ -0.258 USDT                    │
│ Avg. stake amount             │ 767.018 USDT                   │
│ Total trade volume            │ 105711.539 USDT                │
│                               │                                │
│ Best Pair                     │ BTC/USDT 4.15%                 │
│ Worst Pair                    │ LTC/USDT -14.22%               │
│ Best trade                    │ BTC/USDT 6.90%                 │
│ Worst trade                   │ XRP/USDT -4.43%                │
│ Best day                      │ 46.386 USDT                    │
│ Worst day                     │ -21.192 USDT                   │
│ Days win/draw/lose            │ 11 / 1222 / 55                 │
│ Min/Max/Avg. Duration Winners │ 0d 14:30 / 4d 10:10 / 1d 23:05 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:15 / 4d 04:55 / 0d 09:50 │
│ Max Consecutive Wins / Loss   │ 2 / 18                         │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 651.848 USDT                   │
│ Max balance                   │ 1002.862 USDT                  │
│ Max % of account underwater   │ 35.00%                         │
│ Absolute drawdown             │ 351.014 USDT (35.00%)          │
│ Drawdown duration             │ 1100 days 00:05:00             │
│ Profit at drawdown start      │ 2.862 USDT                     │
│ Profit at drawdown end        │ -348.152 USDT                  │
│ Drawdown start                │ 2022-07-19 16:25:00            │
│ Drawdown end                  │ 2025-07-23 16:30:00            │
│ Market change                 │ 91.49%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     69 │        -0.68 │        -348.152 │       -34.82 │     15:46:00 │   11     0    58  15.9 │ 351.014 USDT  35.00% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
