# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 284 / 0.21, Median: -1.12%, Total profit: 18.84%, Sortino: 0.35, Sharpe: 0.11, Calmar: 0.83, Drawdown: 32.0%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 6146  
**Timestamp:** 2025-09-16 21:17:19

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell buy",
  "random_state": 6146,
  "epochs": 200,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 200 --spaces sell buy --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 6146
```

## Hyperopt Output
```
2025-09-16 19:12:53,510 - freqtrade - INFO - freqtrade 2025.7
2025-09-16 19:12:54,190 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-16 19:12:54,191 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-16 19:12:55,545 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-16 19:12:55,547 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-16 19:12:55,548 - freqtrade.loggers - INFO - Logfile configured
2025-09-16 19:12:55,548 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-16 19:12:55,549 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-16 19:12:55,549 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-16 19:12:55,549 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-16 19:12:55,557 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-16 19:12:55,557 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-16 19:12:55,558 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-16 19:12:55,558 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 200 epochs ...
2025-09-16 19:12:55,559 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['sell', 'buy']
2025-09-16 19:12:55,559 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-16 19:12:55,559 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-16 19:12:55,560 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 6146
2025-09-16 19:12:55,560 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-16 19:12:55,561 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-16 19:12:55,561 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-16 19:12:55,561 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-16 19:12:55,563 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-16 19:12:55,582 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-16 19:12:55,583 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 19:12:55,586 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-16 19:12:55,588 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-16 19:12:55,593 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-16 19:12:55,594 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-16 19:12:55,627 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-16 19:12:58,146 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-16 19:12:58,199 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuKinjunStrategy from '/freqtrade/user_data/strategies/IchimokuKinjunStrategy.py'...
2025-09-16 19:12:58,200 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuKinjunStrategy.json
2025-09-16 19:12:58,201 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-16 19:12:58,202 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-16 19:12:58,202 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-16 19:12:58,202 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-16 19:12:58,203 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-16 19:12:58,203 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-16 19:12:58,204 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-16 19:12:58,204 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-16 19:12:58,205 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-16 19:12:58,205 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-16 19:12:58,205 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-16 19:12:58,206 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-16 19:12:58,206 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-16 19:12:58,207 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-16 19:12:58,207 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-16 19:12:58,208 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-16 19:12:58,208 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-16 19:12:58,208 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-16 19:12:58,209 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-16 19:12:58,209 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-16 19:12:58,210 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-16 19:12:58,210 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-16 19:12:58,211 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-16 19:12:58,211 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-16 19:12:58,211 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-16 19:12:58,212 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-16 19:12:58,213 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-16 19:12:58,213 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-16 19:12:58,213 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-16 19:12:58,214 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 19:12:58,220 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-16 19:12:58,254 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-16 19:12:58,256 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_spanA = False
2025-09-16 19:12:58,256 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_spanB = True
2025-09-16 19:12:58,257 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_tenkan = False
2025-09-16 19:12:58,258 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_sma200 = False
2025-09-16 19:12:58,258 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_spanA_sup_spanB = True
2025-09-16 19:12:58,259 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_span_futur = False
2025-09-16 19:12:58,259 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 68
2025-09-16 19:12:58,260 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 15
2025-09-16 19:12:58,260 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 2.111
2025-09-16 19:12:58,261 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 2
2025-09-16 19:12:58,262 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 1
2025-09-16 19:12:58,262 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 1.0
2025-09-16 19:12:58,263 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2.5
2025-09-16 19:12:58,263 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-16 19:12:58,264 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-16 19:12:58,271 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-16 19:12:58,271 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 6146
2025-09-16 19:12:58,305 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-16 19:12:58,356 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-16 19:12:58,365 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-16 19:12:58,402 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-16 19:12:58,441 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-16 19:12:58,485 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-16 19:12:58,495 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-16 19:12:58,515 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-16 19:12:59,294 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-16 19:12:59,296 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-16 19:12:59,303 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-16 19:13:01,000 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-16 19:13:01,007 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-16 19:13:02,692 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-16 19:13:02,700 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-16 19:13:04,178 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-16 19:13:04,185 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-16 19:13:05,400 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-16 19:13:05,407 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-16 19:13:06,990 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-16 19:13:07,281 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 20 CPU cores. Let's make them scream!
2025-09-16 19:13:07,282 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-16 19:13:07,283 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-16 19:13:07,284] A new study created in memory with name: no-name-8f3cee15-4995-47f0-b5c9-21ecc706d0d0
2025-09-16 19:13:07,336 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                         ┏━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓                         
                         ┃ Best   ┃   Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                  Profit ┃     Avg duration ┃ Objective ┃     Max Drawdown (Acct) ┃                         
                         ┡━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩                         
                         │ * Best │   5/200 │     38 │    9     0    29  23.7 │      0.11% │ -32.688 USDT   (-3.27%) │ 2 days, 14:09:00 │   0.02221 │ 222.920 USDT   (21.01%) │                         
                         │ * Best │   8/200 │    107 │   27     0    80  25.2 │      0.04% │  36.699 USDT    (3.67%) │          7:52:00 │  -0.04257 │ 169.048 USDT   (15.93%) │                         
                         │ * Best │  21/200 │     36 │   15     0    21  41.7 │      0.79% │ 101.574 USDT   (10.16%) │   1 day, 1:45:00 │  -0.07873 │  93.049 USDT    (9.06%) │                         
                         │ Best   │  31/200 │     55 │   17     0    38  30.9 │      0.05% │ 110.176 USDT   (11.02%) │  2 days, 4:33:00 │  -0.08344 │ 153.681 USDT   (15.37%) │                         
                         │ Best   │  35/200 │    120 │   38     0    82  31.7 │      0.35% │ 217.811 USDT   (21.78%) │         18:50:00 │  -0.17277 │ 182.093 USDT   (16.92%) │                         
                         │ Best   │  95/200 │    328 │   86     0   242  26.2 │      0.00% │ 362.039 USDT   (36.20%) │  1 day, 16:00:00 │  -0.23302 │ 461.643 USDT   (25.97%) │                         
                         │ Best   │ 101/200 │    128 │   44     0    84  34.4 │      0.86% │ 897.300 USDT   (89.73%) │         15:20:00 │  -0.49695 │ 178.853 USDT   (15.97%) │                         
                         │ Best   │ 133/200 │    120 │   47     0    73  39.2 │      0.87% │ 949.387 USDT   (94.94%) │         19:22:00 │  -0.55806 │ 178.251 USDT   (16.09%) │                         
                         └────────┴─────────┴────────┴────────────────────────┴────────────┴─────────────────────────┴──────────────────┴───────────┴─────────────────────────┘                         
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 200/200 100% • 0:02:55 • 0:00:00
2025-09-16 19:16:02,588 - freqtrade.optimize.hyperopt.hyperopt - INFO - 200 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuKinjunStrategy_2025-09-16_19-12-55.fthypt'.
2025-09-16 19:16:02,621 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuKinjunStrategy.json

Best result:

   133/200:    120 trades. 47/0/73 Wins/Draws/Losses. Avg profit   0.87%. Median profit  -1.12%. Total profit 949.38691338 USDT (  94.94%). Avg duration 19:22:00 min. Objective: -0.55806

{"params":{"entry_kinjun_sup_spanA":false,"entry_kinjun_sup_spanB":false,"entry_kinjun_sup_tenkan":false,"entry_spanA_sup_spanB":true,"entry_span_futur":false,"rsi_entry_max":66,"rsi_entry_min":28,"volume_factor":1.742,"entry_sma200":false,"kinjun_threshold":1,"lookback_period_for_stoploss":5,"stoploss_margin":0.999,"take_profit_multiplier":2.5,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuKinjunStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231
```

## Backtesting Output
```
2025-09-16 19:16:05,684 - freqtrade - INFO - freqtrade 2025.7
2025-09-16 19:16:06,034 - numexpr.utils - INFO - Note: NumExpr detected 20 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
2025-09-16 19:16:06,035 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-16 19:16:07,708 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-16 19:16:07,712 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-16 19:16:07,712 - freqtrade.loggers - INFO - Logfile configured
2025-09-16 19:16:07,712 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-16 19:16:07,713 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-16 19:16:07,713 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-16 19:16:07,714 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-16 19:16:07,714 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-16 19:16:07,723 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-16 19:16:07,724 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-16 19:16:07,725 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-16 19:16:07,726 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-16 19:16:07,726 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-16 19:16:07,727 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-16 19:16:07,728 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-16 19:16:07,748 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-16 19:16:07,749 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 19:16:07,753 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-16 19:16:07,754 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-16 19:16:07,755 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.96
2025-09-16 19:16:07,792 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-16 19:16:10,300 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-16 19:16:10,343 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuKinjunStrategy from '/freqtrade/user_data/strategies/IchimokuKinjunStrategy.py'...
2025-09-16 19:16:10,344 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuKinjunStrategy.json
2025-09-16 19:16:10,345 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-16 19:16:10,345 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-16 19:16:10,346 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-16 19:16:10,346 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-16 19:16:10,347 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-16 19:16:10,347 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-16 19:16:10,348 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-16 19:16:10,349 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-16 19:16:10,349 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-16 19:16:10,350 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-16 19:16:10,350 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-16 19:16:10,351 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-16 19:16:10,352 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-16 19:16:10,352 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-16 19:16:10,353 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-16 19:16:10,353 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-16 19:16:10,354 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-16 19:16:10,354 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-16 19:16:10,355 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-16 19:16:10,356 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-16 19:16:10,356 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-16 19:16:10,357 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-16 19:16:10,358 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-16 19:16:10,359 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-16 19:16:10,360 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-16 19:16:10,361 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-16 19:16:10,362 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-16 19:16:10,363 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-16 19:16:10,364 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-16 19:16:10,374 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-16 19:16:10,427 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-16 19:16:10,473 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-16 19:16:10,533 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-16 19:16:10,582 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-16 19:16:10,626 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-16 19:16:10,682 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-11 17:00:00
2025-09-16 19:16:10,711 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-16 19:16:10,810 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-16 19:16:11,063 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-16 19:16:11,281 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-16 19:16:11,505 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-16 19:16:11,742 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-11 18:30:00
2025-09-16 19:16:13,138 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-16 19:16:13,139 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-16 19:16:13,140 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuKinjunStrategy
2025-09-16 19:16:13,141 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_spanA = False
2025-09-16 19:16:13,142 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_spanB = False
2025-09-16 19:16:13,142 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_tenkan = False
2025-09-16 19:16:13,143 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_sma200 = False
2025-09-16 19:16:13,143 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_spanA_sup_spanB = True
2025-09-16 19:16:13,144 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_span_futur = False
2025-09-16 19:16:13,144 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 66
2025-09-16 19:16:13,145 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 28
2025-09-16 19:16:13,145 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1.742
2025-09-16 19:16:13,146 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 1
2025-09-16 19:16:13,146 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 5
2025-09-16 19:16:13,147 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.999
2025-09-16 19:16:13,147 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2.5
2025-09-16 19:16:13,148 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-16 19:16:13,148 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-16 19:16:13,151 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-16 19:16:13,163 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-16 19:16:15,742 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-16 19:16:15,754 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-16 19:16:18,384 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-16 19:16:18,395 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-16 19:16:21,063 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-16 19:16:21,074 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-16 19:16:23,727 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-16 19:16:23,738 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-10 00:00:00
2025-09-16 19:16:26,369 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-11 17:00:00 (1349 days).
2025-09-16 19:17:18,460 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-16_19-17-18.meta.json"
Result for strategy IchimokuKinjunStrategy
                                              BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │     42 │         0.22 │         139.251 │        13.93 │ 1 day, 0:07:00 │   15     0    27  35.7 │
│ ETH/USDT │     68 │        -0.01 │         100.021 │         10.0 │       22:53:00 │   21     0    47  30.9 │
│ XRP/USDT │     46 │        -0.28 │          30.870 │         3.09 │       14:32:00 │   16     0    30  34.8 │
│ BTC/USDT │     66 │        -0.08 │         -10.779 │        -1.08 │ 1 day, 3:08:00 │   24     0    42  36.4 │
│ LTC/USDT │     62 │        -0.54 │         -70.949 │        -7.09 │       17:03:00 │   18     0    44  29.0 │
│    TOTAL │    284 │        -0.15 │         188.414 │        18.84 │       21:26:00 │   94     0   190  33.1 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                            LEFT OPEN TRADES REPORT                                             
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         1.15 │          13.411 │         1.34 │ 1 day, 18:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         1.15 │          13.411 │         1.34 │ 1 day, 18:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                ENTER TAG STATS                                                
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │     284 │        -0.15 │         188.414 │        18.84 │     21:26:00 │   94     0   190  33.1 │
│     TOTAL │     284 │        -0.15 │         188.414 │        18.84 │     21:26:00 │   94     0   190  33.1 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                   EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2.5R │    61 │         4.41 │        2360.984 │        236.1 │        21:10:00 │   61     0     0   100 │
│       force_exit │     1 │         1.15 │          13.411 │         1.34 │ 1 day, 18:00:00 │    1     0     0   100 │
│      exit_signal │   123 │        -0.93 │        -661.113 │       -66.11 │  1 day, 4:48:00 │   32     0    91  26.0 │
│        stop_loss │    99 │        -2.01 │       -1524.867 │      -152.49 │        12:14:00 │    0     0    99     0 │
│            TOTAL │   284 │        -0.15 │         188.414 │        18.84 │        21:26:00 │   94     0   190  33.1 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                          MIXED TAG STATS                                                           
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2.5R │     61 │         4.41 │        2360.984 │        236.1 │        21:10:00 │   61     0     0   100 │
│           │       force_exit │      1 │         1.15 │          13.411 │         1.34 │ 1 day, 18:00:00 │    1     0     0   100 │
│           │      exit_signal │    123 │        -0.93 │        -661.113 │       -66.11 │  1 day, 4:48:00 │   32     0    91  26.0 │
│           │        stop_loss │     99 │        -2.01 │       -1524.867 │      -152.49 │        12:14:00 │    0     0    99     0 │
│     TOTAL │                  │    284 │        -0.15 │         188.414 │        18.84 │        21:26:00 │   94     0   190  33.1 │
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
│ Total/Daily Avg Trades        │ 284 / 0.21                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1188.414 USDT                  │
│ Absolute profit               │ 188.414 USDT                   │
│ Total profit %                │ 18.84%                         │
│ CAGR %                        │ 4.78%                          │
│ Sortino                       │ 0.35                           │
│ Sharpe                        │ 0.11                           │
│ Calmar                        │ 0.83                           │
│ SQN                           │ 0.47                           │
│ Profit factor                 │ 1.08                           │
│ Expectancy (Ratio)            │ 0.66 (0.05)                    │
│ Avg. daily profit             │ 0.14 USDT                      │
│ Avg. stake amount             │ 788.121 USDT                   │
│ Total trade volume            │ 448737.841 USDT                │
│                               │                                │
│ Best Pair                     │ BNB/USDT 13.93%                │
│ Worst Pair                    │ LTC/USDT -7.09%                │
│ Best trade                    │ ETH/USDT 9.52%                 │
│ Worst trade                   │ XRP/USDT -7.80%                │
│ Best day                      │ 83.123 USDT                    │
│ Worst day                     │ -49.26 USDT                    │
│ Days win/draw/lose            │ 87 / 1105 / 154                │
│ Min/Max/Avg. Duration Winners │ 0d 00:15 / 6d 00:00 / 1d 07:55 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 5d 09:00 / 0d 16:15 │
│ Max Consecutive Wins / Loss   │ 5 / 9                          │
│ Rejected Entry signals        │ 24                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 835.473 USDT                   │
│ Max balance                   │ 1395.015 USDT                  │
│ Max % of account underwater   │ 32.00%                         │
│ Absolute Drawdown (Account)   │ 32.00%                         │
│ Absolute Drawdown             │ 393.154 USDT                   │
│ Drawdown high                 │ 228.627 USDT                   │
│ Drawdown low                  │ -164.527 USDT                  │
│ Drawdown Start                │ 2022-07-18 21:00:00            │
│ Drawdown End                  │ 2023-11-21 23:00:00            │
│ Market change                 │ 94.84%                         │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │    284 │        -0.15 │         188.414 │        18.84 │     21:26:00 │   94     0   190  33.1 │ 393.154 USDT  32.00% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
