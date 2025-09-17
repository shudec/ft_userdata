# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 47 / 0.03, Median: -1.08%, Total profit: -22.71%, Sortino: -0.79, Sharpe: -0.2, Calmar: -1.39, Drawdown: 0%)

---
            
**Strategy:** IchimokuRebondStrategy  
**Random State:** 2723  
**Timestamp:** 2025-09-17 18:00:48

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 2723,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 2723
```

## Hyperopt Output
```
2025-09-17 15:57:31,207 - freqtrade - INFO - freqtrade 2025.8
2025-09-17 15:57:31,903 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-17 15:57:33,604 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-17 15:57:33,614 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-17 15:57:33,615 - freqtrade.loggers - INFO - Logfile configured
2025-09-17 15:57:33,616 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-17 15:57:33,617 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-17 15:57:33,617 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-17 15:57:33,618 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-17 15:57:33,975 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-17 15:57:33,979 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-17 15:57:33,980 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-17 15:57:33,981 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 100 epochs ...
2025-09-17 15:57:33,982 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-17 15:57:33,982 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-17 15:57:33,984 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-17 15:57:33,985 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 2723
2025-09-17 15:57:33,986 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-17 15:57:33,986 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-17 15:57:33,987 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-17 15:57:33,988 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-17 15:57:33,992 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-17 15:57:34,015 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-17 15:57:34,016 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 15:57:34,020 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-17 15:57:34,033 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-17 15:57:34,043 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-17 15:57:34,044 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-17 15:57:34,087 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-17 15:57:36,737 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-17 15:57:36,837 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-17 15:57:36,840 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-17 15:57:36,845 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-17 15:57:36,846 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-17 15:57:36,847 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-17 15:57:36,847 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-17 15:57:36,848 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-17 15:57:36,849 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-17 15:57:36,849 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-17 15:57:36,849 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-17 15:57:36,850 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-17 15:57:36,850 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-17 15:57:36,851 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-17 15:57:36,851 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-17 15:57:36,851 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-17 15:57:36,852 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-17 15:57:36,852 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-17 15:57:36,853 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-17 15:57:36,853 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-17 15:57:36,854 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-17 15:57:36,854 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-17 15:57:36,855 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-17 15:57:36,855 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-17 15:57:36,856 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-17 15:57:36,856 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-17 15:57:36,857 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-17 15:57:36,857 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-17 15:57:36,857 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-17 15:57:36,858 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-17 15:57:36,858 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-17 15:57:36,858 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-17 15:57:36,859 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 15:57:36,877 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-17 15:57:36,905 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-17 15:57:36,907 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.454
2025-09-17 15:57:36,907 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.256
2025-09-17 15:57:36,908 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.003
2025-09-17 15:57:36,908 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1
2025-09-17 15:57:36,908 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 6
2025-09-17 15:57:36,909 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-09-17 15:57:36,909 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-17 15:57:36,910 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-17 15:57:36,910 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = True
2025-09-17 15:57:36,910 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-17 15:57:36,932 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-17 15:57:36,933 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 2723
2025-09-17 15:57:36,996 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-17 15:57:37,087 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-17 15:57:37,097 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-17 15:57:37,168 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-17 15:57:37,241 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-17 15:57:37,315 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-17 15:57:37,328 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-17 15:57:37,346 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-17 15:57:38,175 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-17 15:57:38,178 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 15:57:38,198 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-17 15:57:40,436 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 15:57:40,453 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-17 15:57:42,701 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 15:57:42,720 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-17 15:57:44,872 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 15:57:44,889 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-17 15:57:46,188 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 15:57:46,202 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-17 15:57:47,772 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-17 15:57:48,255 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 16 CPU cores. Let's make them scream!
2025-09-17 15:57:48,256 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-17 15:57:48,258 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-17 15:57:48,259] A new study created in memory with name: no-name-c90bc915-3070-43de-b1ef-84cc155a58f2
2025-09-17 15:57:48,345 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                           ┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓                           
                           ┃ Best   ┃  Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                   Profit ┃ Avg duration ┃ Objective ┃     Max Drawdown (Acct) ┃                           
                           ┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩                           
                           │ * Best │  1/100 │    158 │   38     0   120  24.1 │     -0.07% │ -140.039 USDT  (-14.00%) │     10:27:00 │   0.13285 │ 310.148 USDT   (26.64%) │                           
                           │ * Best │  3/100 │      5 │    1     0     4  20.0 │     -4.09% │  -61.302 USDT   (-6.13%) │      9:00:00 │   0.08436 │  61.302 USDT    (6.13%) │                           
                           │ * Best │  4/100 │     13 │    5     0     8  38.5 │      1.22% │  112.957 USDT   (11.30%) │      5:18:00 │  -0.09100 │  57.869 USDT    (4.94%) │                           
                           │ * Best │ 26/100 │     45 │   14     0    31  31.1 │      1.43% │  467.478 USDT   (46.75%) │     17:37:00 │  -0.17568 │ 267.818 USDT   (16.74%) │                           
                           │ Best   │ 49/100 │     57 │   24     0    33  42.1 │      0.75% │  243.963 USDT   (24.40%) │     11:54:00 │  -0.19443 │  98.370 USDT    (8.18%) │                           
                           └────────┴────────┴────────┴────────────────────────┴────────────┴──────────────────────────┴──────────────┴───────────┴─────────────────────────┘                           
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100/100 100% • 0:02:21 • 0:00:00
2025-09-17 16:00:09,587 - freqtrade.optimize.hyperopt.hyperopt - INFO - 100 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-17_15-57-34.fthypt'.
2025-09-17 16:00:09,756 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

    49/100:     57 trades. 24/0/33 Wins/Draws/Losses. Avg profit   0.75%. Median profit  -1.08%. Total profit 243.96297846 USDT (  24.40%). Avg duration 11:54:00 min. Objective: -0.19443

{"params":{"hammer_body_threshold":0.499,"hammer_head_threshold":0.658,"hammer_strength_threshold":0.01,"kinjun_threshold":0,"lookback_period_for_stoploss":10,"stoploss_margin":1.0,"take_profit_multiplier":1.5,"use_sell_signal_param":false,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231
```

## Backtesting Output
```
2025-09-17 16:00:13,903 - freqtrade - INFO - freqtrade 2025.8
2025-09-17 16:00:14,302 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-17 16:00:16,338 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-17 16:00:16,344 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-17 16:00:16,345 - freqtrade.loggers - INFO - Logfile configured
2025-09-17 16:00:16,345 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-17 16:00:16,346 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-17 16:00:16,346 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-17 16:00:16,347 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-17 16:00:16,347 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-17 16:00:16,677 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-17 16:00:16,680 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-17 16:00:16,681 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-17 16:00:16,681 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-17 16:00:16,682 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-17 16:00:16,682 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-17 16:00:16,684 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-17 16:00:16,697 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-17 16:00:16,698 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 16:00:16,701 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-17 16:00:16,702 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-17 16:00:16,703 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-17 16:00:16,742 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-17 16:00:19,437 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-17 16:00:19,569 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-17 16:00:19,571 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-17 16:00:19,577 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-17 16:00:19,578 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-17 16:00:19,578 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-17 16:00:19,579 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-17 16:00:19,580 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-17 16:00:19,580 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-17 16:00:19,581 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-17 16:00:19,581 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-17 16:00:19,581 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-17 16:00:19,582 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-17 16:00:19,582 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-17 16:00:19,583 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-17 16:00:19,583 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-17 16:00:19,583 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-17 16:00:19,584 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-17 16:00:19,584 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-17 16:00:19,585 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-17 16:00:19,586 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-17 16:00:19,586 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-17 16:00:19,587 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-17 16:00:19,587 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-17 16:00:19,588 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-17 16:00:19,588 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-17 16:00:19,588 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-17 16:00:19,589 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-17 16:00:19,589 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-17 16:00:19,590 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-17 16:00:19,591 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-17 16:00:19,592 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 16:00:19,615 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-17 16:00:19,647 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-17 16:00:19,717 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 16:00:19,790 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 16:00:19,859 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 16:00:19,925 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 16:00:19,989 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 16:00:20,012 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-17 16:00:20,250 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 16:00:20,646 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 16:00:21,030 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 16:00:21,477 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 16:00:21,888 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 16:00:23,445 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-17 16:00:23,455 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-17 16:00:23,456 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-17 16:00:23,458 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 0.499
2025-09-17 16:00:23,460 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.658
2025-09-17 16:00:23,461 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.01
2025-09-17 16:00:23,462 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0
2025-09-17 16:00:23,463 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 10
2025-09-17 16:00:23,466 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 1.0
2025-09-17 16:00:23,467 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 1.5
2025-09-17 16:00:23,469 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-17 16:00:23,470 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-17 16:00:23,471 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-17 16:00:23,476 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 16:00:23,506 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 16:00:27,783 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 16:00:27,801 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 16:00:30,581 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 16:00:30,597 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 16:00:33,624 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 16:00:33,641 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 16:00:36,827 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 16:00:36,842 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 16:00:39,576 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-17 16:00:47,098 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-17_16-00-47.meta.json"
Result for strategy IchimokuRebondStrategy
                                              BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │     11 │        -0.01 │          -0.058 │        -0.01 │        8:12:00 │    4     0     7  36.4 │
│ ETH/USDT │      6 │        -0.73 │         -29.111 │        -2.91 │        6:38:00 │    2     0     4  33.3 │
│ BTC/USDT │      8 │        -0.12 │         -37.905 │        -3.79 │ 1 day, 0:22:00 │    2     0     6  25.0 │
│ LTC/USDT │     10 │        -0.68 │         -72.250 │        -7.22 │        3:32:00 │    2     0     8  20.0 │
│ XRP/USDT │     12 │        -0.74 │         -87.811 │        -8.78 │       14:54:00 │    3     0     9  25.0 │
│    TOTAL │     47 │        -0.45 │        -227.135 │       -22.71 │       11:28:00 │   13     0    34  27.7 │
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
│     OTHER │      47 │        -0.45 │        -227.135 │       -22.71 │     11:28:00 │   13     0    34  27.7 │
│     TOTAL │      47 │        -0.45 │        -227.135 │       -22.71 │     11:28:00 │   13     0    34  27.7 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │    13 │         3.14 │         255.647 │        25.56 │     17:29:00 │   13     0     0   100 │
│        stop_loss │    34 │        -1.82 │        -482.781 │       -48.28 │      9:10:00 │    0     0    34     0 │
│            TOTAL │    47 │        -0.45 │        -227.135 │       -22.71 │     11:28:00 │   13     0    34  27.7 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1.5R │     13 │         3.14 │         255.647 │        25.56 │     17:29:00 │   13     0     0   100 │
│           │        stop_loss │     34 │        -1.82 │        -482.781 │       -48.28 │      9:10:00 │    0     0    34     0 │
│     TOTAL │                  │     47 │        -0.45 │        -227.135 │       -22.71 │     11:28:00 │   13     0    34  27.7 │
└───────────┴──────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-10 08:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 47 / 0.03                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 772.865 USDT                   │
│ Absolute profit               │ -227.135 USDT                  │
│ Total profit %                │ -22.71%                        │
│ CAGR %                        │ -6.74%                         │
│ Sortino                       │ -0.79                          │
│ Sharpe                        │ -0.20                          │
│ Calmar                        │ -1.39                          │
│ SQN                           │ -2.06                          │
│ Profit factor                 │ 0.53                           │
│ Expectancy (Ratio)            │ -4.83 (-0.34)                  │
│ Avg. daily profit             │ -0.168 USDT                    │
│ Avg. stake amount             │ 806.74 USDT                    │
│ Total trade volume            │ 75757.785 USDT                 │
│                               │                                │
│ Best Pair                     │ BNB/USDT -0.01%                │
│ Worst Pair                    │ XRP/USDT -8.78%                │
│ Best trade                    │ XRP/USDT 7.17%                 │
│ Worst trade                   │ XRP/USDT -4.05%                │
│ Best day                      │ 29.139 USDT                    │
│ Worst day                     │ -20.368 USDT                   │
│ Days win/draw/lose            │ 13 / 1234 / 34                 │
│ Min/Max/Avg. Duration Winners │ 0d 00:25 / 4d 02:30 / 0d 17:29 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:10 / 4d 04:50 / 0d 09:10 │
│ Max Consecutive Wins / Loss   │ 3 / 9                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 772.865 USDT                   │
│ Max balance                   │ 1006.29 USDT                   │
│ Max % of account underwater   │ 23.20%                         │
│ Absolute drawdown             │ 233.425 USDT (23.20%)          │
│ Drawdown duration             │ 1113 days 18:40:00             │
│ Profit at drawdown start      │ 6.29 USDT                      │
│ Profit at drawdown end        │ -227.135 USDT                  │
│ Drawdown start                │ 2022-07-18 23:10:00            │
│ Drawdown end                  │ 2025-08-05 17:50:00            │
│ Market change                 │ 91.49%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     47 │        -0.45 │        -227.135 │       -22.71 │     11:28:00 │   13     0    34  27.7 │ 233.425 USDT  23.20% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
