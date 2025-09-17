# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 1886 / 1.4, Median: -0.63%, Total profit: -13.48%, Sortino: -2.03, Sharpe: -0.63, Calmar: -0.9, Drawdown: 0%)

---
            
**Strategy:** IchimokuRebondStrategy  
**Random State:** 2649  
**Timestamp:** 2025-09-17 12:39:49

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 2649,
  "epochs": 500,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 500 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 2649
```

## Hyperopt Output
```
2025-09-17 10:10:37,924 - freqtrade - INFO - freqtrade 2025.8
2025-09-17 10:10:38,779 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-17 10:10:40,938 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-17 10:10:40,944 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-17 10:10:40,945 - freqtrade.loggers - INFO - Logfile configured
2025-09-17 10:10:40,945 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-17 10:10:40,945 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-17 10:10:40,946 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-17 10:10:40,946 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-17 10:10:41,329 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-17 10:10:41,332 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-17 10:10:41,333 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-17 10:10:41,333 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 500 epochs ...
2025-09-17 10:10:41,333 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-17 10:10:41,334 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-17 10:10:41,334 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-17 10:10:41,334 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 2649
2025-09-17 10:10:41,335 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-17 10:10:41,335 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-17 10:10:41,335 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-17 10:10:41,335 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-17 10:10:41,337 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-17 10:10:41,347 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-17 10:10:41,347 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 10:10:41,350 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-17 10:10:41,356 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-17 10:10:41,362 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-17 10:10:41,362 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-17 10:10:41,380 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-17 10:10:45,882 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-17 10:10:45,984 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-17 10:10:45,986 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-17 10:10:45,990 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-17 10:10:45,990 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-17 10:10:45,990 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-17 10:10:45,991 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-17 10:10:45,991 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-17 10:10:45,992 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-17 10:10:45,992 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-17 10:10:45,993 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-17 10:10:45,993 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-17 10:10:45,993 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-17 10:10:45,994 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-17 10:10:45,994 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-17 10:10:45,994 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-17 10:10:45,994 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-17 10:10:45,995 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-17 10:10:45,995 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-17 10:10:45,995 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-17 10:10:45,996 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-17 10:10:45,996 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-17 10:10:45,997 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-17 10:10:45,997 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-17 10:10:45,997 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-17 10:10:45,998 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-17 10:10:45,998 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-17 10:10:45,998 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-17 10:10:45,999 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-17 10:10:45,999 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-17 10:10:46,000 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-17 10:10:46,000 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-17 10:10:46,000 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 10:10:46,023 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-17 10:10:46,046 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-17 10:10:46,047 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_spanA = False
2025-09-17 10:10:46,047 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_spanB = False
2025-09-17 10:10:46,047 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_tenkan = False
2025-09-17 10:10:46,048 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_sma200 = False
2025-09-17 10:10:46,048 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_spanA_sup_spanB = False
2025-09-17 10:10:46,048 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_span_futur = False
2025-09-17 10:10:46,049 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 3.335
2025-09-17 10:10:46,049 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.321
2025-09-17 10:10:46,049 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 50
2025-09-17 10:10:46,050 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 20
2025-09-17 10:10:46,050 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1.0
2025-09-17 10:10:46,050 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0
2025-09-17 10:10:46,051 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 0
2025-09-17 10:10:46,051 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 1.0
2025-09-17 10:10:46,051 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-17 10:10:46,052 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-17 10:10:46,052 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-17 10:10:46,053 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-17 10:10:46,071 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-17 10:10:46,072 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 2649
2025-09-17 10:10:46,175 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-17 10:10:46,270 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-17 10:10:46,282 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-17 10:10:46,332 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-17 10:10:46,382 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-17 10:10:46,432 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-17 10:10:46,440 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-17 10:10:46,452 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-17 10:10:47,053 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-17 10:10:47,055 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 10:10:47,070 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-17 10:10:48,371 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 10:10:48,386 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-17 10:10:49,849 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 10:10:49,867 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-17 10:10:51,199 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 10:10:51,219 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-17 10:10:52,313 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 10:10:52,332 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-17 10:10:53,797 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-17 10:10:54,258 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 16 CPU cores. Let's make them scream!
2025-09-17 10:10:54,259 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-17 10:10:54,261 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-17 10:10:54,261] A new study created in memory with name: no-name-e6a4aaf1-ea62-4470-97bd-68a2c343d5c0
2025-09-17 10:10:54,343 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                        ┏━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓                        
                        ┃ Best   ┃   Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                   Profit ┃     Avg duration ┃ Objective ┃      Max Drawdown (Acct) ┃                        
                        ┡━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩                        
                        │ * Best │   1/500 │    508 │  123     0   385  24.2 │     -0.04% │ -281.101 USDT  (-28.11%) │         23:50:00 │   0.19986 │ 1286.214 USDT   (65.52%) │                        
                        │ * Best │   2/500 │    450 │  145     0   305  32.2 │      0.00% │   -3.087 USDT   (-0.31%) │         17:56:00 │   0.00258 │  562.123 USDT   (37.53%) │                        
                        │ * Best │   5/500 │    157 │   56     0   101  35.7 │      0.95% │   42.249 USDT    (4.22%) │ 12 days, 5:14:00 │  -0.05083 │  206.830 USDT   (18.78%) │                        
                        │ * Best │   6/500 │    540 │  148     0   392  27.4 │      0.88% │  312.764 USDT   (31.28%) │         22:39:00 │  -0.82421 │  127.569 USDT    (8.89%) │                        
                        │ Best   │  35/500 │    444 │  150     0   294  33.8 │      1.04% │  461.180 USDT   (46.12%) │  2 days, 7:09:00 │  -0.84588 │  222.602 USDT   (13.25%) │                        
                        │ Best   │ 137/500 │    939 │  209     0   730  22.3 │      0.24% │  210.554 USDT   (21.06%) │          9:24:00 │  -0.89663 │   96.943 USDT    (7.44%) │                        
                        │ Best   │ 168/500 │    655 │  174     0   481  26.6 │      0.74% │  338.604 USDT   (33.86%) │         23:08:00 │  -0.91869 │  169.758 USDT   (11.32%) │                        
                        │ Best   │ 205/500 │    452 │  155     0   297  34.3 │      1.17% │  498.734 USDT   (49.87%) │  2 days, 5:33:00 │  -0.94546 │  229.173 USDT   (13.29%) │                        
                        │ Best   │ 209/500 │    939 │  209     0   730  22.3 │      0.25% │  245.520 USDT   (24.55%) │          9:15:00 │  -0.98418 │   95.927 USDT    (7.16%) │                        
                        │ Best   │ 266/500 │    988 │  222     0   766  22.5 │      0.29% │  253.188 USDT   (25.32%) │          9:19:00 │  -0.99950 │  115.510 USDT    (8.46%) │                        
                        │ Best   │ 288/500 │    949 │  214     0   735  22.6 │      0.25% │  249.441 USDT   (24.94%) │          9:17:00 │  -0.99993 │  105.514 USDT    (7.81%) │                        
                        │ Best   │ 302/500 │    949 │  214     0   735  22.6 │      0.25% │  256.399 USDT   (25.64%) │          9:14:00 │  -1.00918 │  106.675 USDT    (7.85%) │                        
                        │ Best   │ 309/500 │    987 │  222     0   765  22.5 │      0.30% │  255.662 USDT   (25.57%) │          9:21:00 │  -1.02627 │  115.079 USDT    (8.42%) │                        
                        │ Best   │ 311/500 │    973 │  218     0   755  22.4 │      0.31% │  258.536 USDT   (25.85%) │          9:20:00 │  -1.03906 │  111.968 USDT    (8.20%) │                        
                        │ Best   │ 381/500 │    972 │  217     0   755  22.3 │      0.31% │  258.195 USDT   (25.82%) │          9:20:00 │  -1.04410 │  111.327 USDT    (8.16%) │                        
                        │ Best   │ 386/500 │    973 │  220     0   753  22.6 │      0.35% │  253.586 USDT   (25.36%) │          9:11:00 │  -1.05121 │  122.942 USDT    (8.96%) │                        
                        │ Best   │ 437/500 │    950 │  211     0   739  22.2 │      0.32% │  264.174 USDT   (26.42%) │          9:20:00 │  -1.05196 │  106.258 USDT    (7.78%) │                        
                        │ Best   │ 487/500 │    986 │  221     0   765  22.4 │      0.30% │  259.780 USDT   (25.98%) │          9:23:00 │  -1.05492 │  113.503 USDT    (8.29%) │                        
                        └────────┴─────────┴────────┴────────────────────────┴────────────┴──────────────────────────┴──────────────────┴───────────┴──────────────────────────┘                        
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 500/500 100% • 0:24:59 • 0:00:00
2025-09-17 10:35:54,396 - freqtrade.optimize.hyperopt.hyperopt - INFO - 500 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-17_10-10-41.fthypt'.
2025-09-17 10:35:54,549 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

   487/500:    986 trades. 221/0/765 Wins/Draws/Losses. Avg profit   0.30%. Median profit  -0.63%. Total profit 259.77997233 USDT (  25.98%). Avg duration 9:23:00 min. Objective: -1.05492

{"params":{"hammer_body_threshold":4.91,"hammer_head_threshold":0.981,"entry_kinjun_sup_spanA":false,"entry_kinjun_sup_spanB":false,"entry_kinjun_sup_tenkan":false,"entry_sma200":false,"entry_spanA_sup_spanB":false,"entry_span_futur":false,"rsi_entry_max":50,"rsi_entry_min":20,"volume_factor":1.0,"kinjun_threshold":0,"lookback_period_for_stoploss":0,"stoploss_margin":0.991,"take_profit_multiplier":2,"use_sell_signal_param":false,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231
```

## Backtesting Output
```
2025-09-17 10:35:59,510 - freqtrade - INFO - freqtrade 2025.8
2025-09-17 10:36:00,190 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-17 10:36:02,359 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-17 10:36:02,367 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-17 10:36:02,367 - freqtrade.loggers - INFO - Logfile configured
2025-09-17 10:36:02,368 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-17 10:36:02,369 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-17 10:36:02,369 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-17 10:36:02,370 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-17 10:36:02,371 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-17 10:36:02,878 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-17 10:36:02,883 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-17 10:36:02,884 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-17 10:36:02,884 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-17 10:36:02,885 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-17 10:36:02,886 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-17 10:36:02,888 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-17 10:36:02,907 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-17 10:36:02,908 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 10:36:02,912 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-17 10:36:02,913 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-17 10:36:02,913 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-17 10:36:02,948 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-17 10:36:06,923 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-17 10:36:07,030 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-17 10:36:07,032 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-17 10:36:07,038 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-17 10:36:07,038 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-17 10:36:07,039 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-17 10:36:07,039 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-17 10:36:07,040 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-17 10:36:07,040 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-17 10:36:07,041 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-17 10:36:07,041 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-17 10:36:07,042 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-17 10:36:07,042 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-17 10:36:07,043 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-17 10:36:07,043 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-17 10:36:07,044 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-17 10:36:07,044 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-17 10:36:07,045 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-17 10:36:07,046 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-17 10:36:07,046 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-17 10:36:07,047 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-17 10:36:07,047 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-17 10:36:07,048 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-17 10:36:07,048 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-17 10:36:07,049 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-17 10:36:07,049 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-17 10:36:07,050 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-17 10:36:07,050 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-17 10:36:07,051 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-17 10:36:07,051 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-17 10:36:07,052 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-17 10:36:07,052 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 10:36:07,071 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-17 10:36:07,097 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-17 10:36:07,152 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 10:36:07,218 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 10:36:07,312 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 10:36:07,380 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 10:36:07,464 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 10:36:07,493 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-17 10:36:07,806 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 10:36:08,331 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 10:36:08,759 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 10:36:09,169 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 10:36:09,561 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 10:36:10,893 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-17 10:36:10,899 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-17 10:36:10,900 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-17 10:36:10,902 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_spanA = False
2025-09-17 10:36:10,903 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_spanB = False
2025-09-17 10:36:10,904 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_tenkan = False
2025-09-17 10:36:10,904 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_sma200 = False
2025-09-17 10:36:10,905 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_spanA_sup_spanB = False
2025-09-17 10:36:10,906 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_span_futur = False
2025-09-17 10:36:10,907 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 4.91
2025-09-17 10:36:10,908 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.981
2025-09-17 10:36:10,909 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 50
2025-09-17 10:36:10,910 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 20
2025-09-17 10:36:10,911 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1.0
2025-09-17 10:36:10,913 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 0
2025-09-17 10:36:10,914 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 0
2025-09-17 10:36:10,915 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.991
2025-09-17 10:36:10,916 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-17 10:36:10,917 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-17 10:36:10,918 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-17 10:36:10,919 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-17 10:36:10,923 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 10:36:10,943 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 10:36:13,258 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 10:36:13,274 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 10:36:15,487 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 10:36:15,506 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 10:36:18,002 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 10:36:18,021 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 10:36:20,660 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 10:36:20,684 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 10:36:23,162 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-17 10:39:47,910 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-17_10-39-47.meta.json"
Result for strategy IchimokuRebondStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │    384 │         0.34 │          57.356 │         5.74 │      8:35:00 │   91     0   293  23.7 │
│ BTC/USDT │    364 │          0.0 │           9.084 │         0.91 │      9:35:00 │   77     0   287  21.2 │
│ ETH/USDT │    348 │        -0.12 │         -56.760 │        -5.68 │      8:32:00 │   69     0   279  19.8 │
│ LTC/USDT │    400 │        -0.13 │         -64.386 │        -6.44 │      8:38:00 │   82     0   318  20.5 │
│ BNB/USDT │    390 │        -0.16 │         -80.105 │        -8.01 │      8:18:00 │   78     0   312  20.0 │
│    TOTAL │   1886 │        -0.01 │        -134.811 │       -13.48 │      8:43:00 │  397     0  1489  21.0 │
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
│     OTHER │    1886 │        -0.01 │        -134.811 │       -13.48 │      8:43:00 │  397     0  1489  21.0 │
│     TOTAL │    1886 │        -0.01 │        -134.811 │       -13.48 │      8:43:00 │  397     0  1489  21.0 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │     5 │        30.02 │         177.559 │        17.76 │ 1 day, 8:38:00 │    5     0     0   100 │
│    exit_signal │  1881 │        -0.09 │        -312.370 │       -31.24 │        8:39:00 │  392     0  1489  20.8 │
│          TOTAL │  1886 │        -0.01 │        -134.811 │       -13.48 │        8:43:00 │  397     0  1489  21.0 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │      5 │        30.02 │         177.559 │        17.76 │ 1 day, 8:38:00 │    5     0     0   100 │
│           │    exit_signal │   1881 │        -0.09 │        -312.370 │       -31.24 │        8:39:00 │  392     0  1489  20.8 │
│     TOTAL │                │   1886 │        -0.01 │        -134.811 │       -13.48 │        8:43:00 │  397     0  1489  21.0 │
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
│ Total/Daily Avg Trades        │ 1886 / 1.4                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 865.189 USDT                   │
│ Absolute profit               │ -134.811 USDT                  │
│ Total profit %                │ -13.48%                        │
│ CAGR %                        │ -3.85%                         │
│ Sortino                       │ -2.03                          │
│ Sharpe                        │ -0.63                          │
│ Calmar                        │ -0.90                          │
│ SQN                           │ -1.02                          │
│ Profit factor                 │ 0.90                           │
│ Expectancy (Ratio)            │ -0.07 (-0.08)                  │
│ Avg. daily profit             │ -0.1 USDT                      │
│ Avg. stake amount             │ 121.62 USDT                    │
│ Total trade volume            │ 459534.945 USDT                │
│                               │                                │
│ Best Pair                     │ XRP/USDT 5.74%                 │
│ Worst Pair                    │ BNB/USDT -8.01%                │
│ Best trade                    │ XRP/USDT 68.22%                │
│ Worst trade                   │ BNB/USDT -8.28%                │
│ Best day                      │ 52.886 USDT                    │
│ Worst day                     │ -16.191 USDT                   │
│ Days win/draw/lose            │ 202 / 578 / 564                │
│ Min/Max/Avg. Duration Winners │ 0d 01:00 / 3d 04:00 / 1d 00:57 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 2d 02:00 / 0d 04:23 │
│ Max Consecutive Wins / Loss   │ 5 / 43                         │
│ Rejected Entry signals        │ 1488                           │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 842.346 USDT                   │
│ Max balance                   │ 1069.84 USDT                   │
│ Max % of account underwater   │ 21.26%                         │
│ Absolute drawdown             │ 227.494 USDT (21.26%)          │
│ Drawdown duration             │ 836 days 05:00:00              │
│ Profit at drawdown start      │ 69.84 USDT                     │
│ Profit at drawdown end        │ -157.654 USDT                  │
│ Drawdown start                │ 2023-03-24 10:00:00            │
│ Drawdown end                  │ 2025-07-07 15:00:00            │
│ Market change                 │ 91.49%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │   1886 │        -0.01 │        -134.811 │       -13.48 │      8:43:00 │  397     0  1489  21.0 │ 227.494 USDT  21.26% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
