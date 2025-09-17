# Freqtrade Automation Log

## Performance Indicator
**Status:** 🟠 ORANGE  
**Description:** Moderate Performance (Total trades: 36 / 0.03, Median: -3.39%, Total profit: 25.14%, Sortino: 0.53, Sharpe: 0.12, Calmar: 2.92, Drawdown: 0%)

---
            
**Strategy:** IchimokuRebondStrategy  
**Random State:** 2419  
**Timestamp:** 2025-09-17 17:24:14

## Configuration
```json
{
  "strategy": "IchimokuRebondStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 2419,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20251231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuRebondStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 2419
```

## Hyperopt Output
```
2025-09-17 15:17:22,990 - freqtrade - INFO - freqtrade 2025.8
2025-09-17 15:17:24,110 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-17 15:17:26,568 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-17 15:17:26,578 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-17 15:17:26,579 - freqtrade.loggers - INFO - Logfile configured
2025-09-17 15:17:26,579 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-17 15:17:26,580 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-17 15:17:26,581 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-17 15:17:26,582 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20170801-20191231 ...
2025-09-17 15:17:27,149 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-17 15:17:27,152 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-17 15:17:27,153 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-17 15:17:27,153 - freqtrade.configuration.configuration - INFO - Parameter --epochs detected ... Will run Hyperopt with for 100 epochs ...
2025-09-17 15:17:27,154 - freqtrade.configuration.configuration - INFO - Parameter -s/--spaces detected: ['buy', 'sell']
2025-09-17 15:17:27,155 - freqtrade.configuration.configuration - INFO - Parameter --print-json detected ...
2025-09-17 15:17:27,155 - freqtrade.configuration.configuration - INFO - Parameter -j/--job-workers detected: 8
2025-09-17 15:17:27,156 - freqtrade.configuration.configuration - INFO - Parameter --random-state detected: 2419
2025-09-17 15:17:27,157 - freqtrade.configuration.configuration - INFO - Parameter --min-trades detected: 1
2025-09-17 15:17:27,158 - freqtrade.configuration.configuration - INFO - Using Hyperopt loss class name: SharpeHyperOptLoss
2025-09-17 15:17:27,159 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-17 15:17:27,160 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20170801-20191231
2025-09-17 15:17:27,162 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-17 15:17:27,178 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-17 15:17:27,179 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 15:17:27,183 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Hyperopt mode
2025-09-17 15:17:27,194 - freqtrade.optimize.hyperopt.hyperopt - INFO - Removing `/freqtrade/user_data/hyperopt_results/hyperopt_tickerdata.pkl`.
2025-09-17 15:17:27,203 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-17 15:17:27,204 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-17 15:17:27,233 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-17 15:17:30,457 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-17 15:17:30,618 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-17 15:17:30,621 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2025-09-17 15:17:30,623 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-17 15:17:30,624 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-17 15:17:30,625 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-17 15:17:30,625 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-17 15:17:30,626 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'use_exit_signal' with value in config file: True.
2025-09-17 15:17:30,627 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-17 15:17:30,628 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-17 15:17:30,628 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-17 15:17:30,629 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-17 15:17:30,630 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-17 15:17:30,631 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-17 15:17:30,632 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-17 15:17:30,633 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-17 15:17:30,634 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-17 15:17:30,636 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-17 15:17:30,637 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-17 15:17:30,637 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-17 15:17:30,638 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-17 15:17:30,640 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-17 15:17:30,641 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-17 15:17:30,642 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-17 15:17:30,642 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-17 15:17:30,643 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-17 15:17:30,644 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-17 15:17:30,645 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-17 15:17:30,646 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-17 15:17:30,648 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-17 15:17:30,649 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-17 15:17:30,650 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-17 15:17:30,651 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 15:17:30,688 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-17 15:17:30,727 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-17 15:17:30,731 - freqtrade.strategy.hyper - INFO - No params for buy found, using default values.
2025-09-17 15:17:30,733 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_kinjun_sup_spanA = False
2025-09-17 15:17:30,735 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_kinjun_sup_spanB = False
2025-09-17 15:17:30,736 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_kinjun_sup_tenkan = False
2025-09-17 15:17:30,737 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_sma200 = False
2025-09-17 15:17:30,738 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_spanA_sup_spanB = False
2025-09-17 15:17:30,739 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): entry_span_futur = False
2025-09-17 15:17:30,741 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): hammer_body_threshold = 2
2025-09-17 15:17:30,742 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): hammer_head_threshold = 0.1
2025-09-17 15:17:30,743 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): hammer_strength_threshold = 0.01
2025-09-17 15:17:30,745 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_max = 50
2025-09-17 15:17:30,748 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): rsi_entry_min = 20
2025-09-17 15:17:30,750 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): volume_factor = 1.0
2025-09-17 15:17:30,752 - freqtrade.strategy.hyper - INFO - No params for sell found, using default values.
2025-09-17 15:17:30,753 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): kinjun_threshold = 2
2025-09-17 15:17:30,755 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): lookback_period_for_stoploss = 5
2025-09-17 15:17:30,756 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): stoploss_margin = 0.999
2025-09-17 15:17:30,758 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): take_profit_multiplier = 2
2025-09-17 15:17:30,760 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_custom_stoploss_param = True
2025-09-17 15:17:30,760 - freqtrade.strategy.hyper - INFO - Strategy Parameter(default): use_sell_signal_param = True
2025-09-17 15:17:30,761 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-17 15:17:30,799 - freqtrade.resolvers.iresolver - INFO - Using resolved hyperoptloss SharpeHyperOptLoss from '/freqtrade/freqtrade/optimize/hyperopt_loss/hyperopt_loss_sharpe.py'...
2025-09-17 15:17:30,800 - freqtrade.optimize.hyperopt.hyperopt - INFO - Using optimizer random state: 2419
2025-09-17 15:17:30,889 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-17 15:17:30,987 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data starts at 2017-08-17 04:00:00
2025-09-17 15:17:30,998 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in ETH/USDT, 1h, spot between two candles of 48.50% detected.
2025-09-17 15:17:31,077 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data starts at 2017-12-13 03:00:00
2025-09-17 15:17:31,176 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data starts at 2018-05-04 08:00:00
2025-09-17 15:17:31,278 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data starts at 2017-11-06 03:00:00
2025-09-17 15:17:31,293 - freqtrade.data.history.datahandlers.idatahandler - INFO - Price jump in BNB/USDT, 1h, spot between two candles of 23.53% detected.
2025-09-17 15:17:31,319 - freqtrade.optimize.backtesting - INFO - Loading data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days).
2025-09-17 15:17:32,448 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Dataload complete. Calculating indicators
2025-09-17 15:17:32,453 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 15:17:32,483 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-17 15:17:37,284 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 15:17:37,309 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data starts at 2017-08-17 00:00:00
2025-09-17 15:17:40,817 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 15:17:40,841 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data starts at 2017-12-13 00:00:00
2025-09-17 15:17:44,370 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 15:17:44,396 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data starts at 2018-05-04 00:00:00
2025-09-17 15:17:47,679 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2017-08-01 00:00:00 to 2019-12-31 00:00:00
2025-09-17 15:17:47,703 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data starts at 2017-11-06 00:00:00
2025-09-17 15:17:50,566 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Hyperopting with data from 2017-08-17 04:00:00 up to 2019-12-31 00:00:00 (865 days)..
2025-09-17 15:17:51,150 - freqtrade.optimize.hyperopt.hyperopt - INFO - Found 16 CPU cores. Let's make them scream!
2025-09-17 15:17:51,151 - freqtrade.optimize.hyperopt.hyperopt - INFO - Number of parallel jobs set as: 8
2025-09-17 15:17:51,155 - freqtrade.optimize.hyperopt.hyperopt_optimizer - INFO - Using optuna sampler NSGAIIISampler.
[I 2025-09-17 15:17:51,157] A new study created in memory with name: no-name-0b8f970f-eff4-417e-9f26-5b79b9efb5e4
2025-09-17 15:17:51,262 - freqtrade.optimize.hyperopt.hyperopt - INFO - Effective number of parallel workers used: 8
                                                                                            Hyperopt results                                                                                            
                        ┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓                        
                        ┃ Best   ┃  Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                   Profit ┃      Avg duration ┃ Objective ┃      Max Drawdown (Acct) ┃                        
                        ┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩                        
                        │ * Best │  1/100 │    136 │   26     0   110  19.1 │     -0.38% │ -473.985 USDT  (-47.40%) │   1 day, 19:48:00 │   0.45714 │  547.938 USDT   (51.02%) │                        
                        │ * Best │  2/100 │    468 │   98     0   370  20.9 │     -0.18% │ -570.978 USDT  (-57.10%) │    1 day, 7:24:00 │   0.38913 │ 1782.813 USDT   (81.01%) │                        
                        │ * Best │  6/100 │     23 │    3     0    20  13.0 │     -1.61% │ -146.436 USDT  (-14.64%) │    1 day, 1:18:00 │   0.09825 │  308.783 USDT   (26.57%) │                        
                        │ * Best │  7/100 │     97 │   26     0    71  26.8 │      0.84% │  -92.156 USDT   (-9.22%) │   2 days, 2:12:00 │   0.06378 │  345.825 USDT   (27.59%) │                        
                        │ * Best │ 13/100 │     59 │   21     0    38  35.6 │      1.49% │  126.605 USDT   (12.66%) │   2 days, 5:31:00 │  -0.08324 │  160.332 USDT   (12.92%) │                        
                        │ Best   │ 68/100 │     16 │    8     0     8  50.0 │     27.39% │  153.035 USDT   (15.30%) │ 114 days, 0:56:00 │  -0.10752 │   90.459 USDT    (7.27%) │                        
                        │ Best   │ 78/100 │     80 │   28     0    52  35.0 │      1.39% │  164.949 USDT   (16.49%) │  2 days, 18:37:00 │  -0.11146 │  234.118 USDT   (17.46%) │                        
                        └────────┴────────┴────────┴────────────────────────┴────────────┴──────────────────────────┴───────────────────┴───────────┴──────────────────────────┘                        
Epochs ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100/100 100% • 0:05:08 • 0:00:00
2025-09-17 15:22:59,705 - freqtrade.optimize.hyperopt.hyperopt - INFO - 100 epochs saved to '/freqtrade/user_data/hyperopt_results/strategy_IchimokuRebondStrategy_2025-09-17_15-17-27.fthypt'.
2025-09-17 15:22:59,879 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to /freqtrade/user_data/strategies/IchimokuRebondStrategy.json

Best result:

    78/100:     80 trades. 28/0/52 Wins/Draws/Losses. Avg profit   1.39%. Median profit  -3.39%. Total profit 164.94881932 USDT (  16.49%). Avg duration 2 days, 18:37:00 min. Objective: -0.11146

{"params":{"hammer_body_threshold":4.564,"hammer_head_threshold":0.932,"hammer_strength_threshold":0.045,"entry_kinjun_sup_spanA":false,"entry_kinjun_sup_spanB":false,"entry_kinjun_sup_tenkan":false,"entry_sma200":false,"entry_spanA_sup_spanB":false,"entry_span_futur":false,"rsi_entry_max":50,"rsi_entry_min":20,"volume_factor":1.0,"kinjun_threshold":7,"lookback_period_for_stoploss":8,"stoploss_margin":0.996,"take_profit_multiplier":2,"use_sell_signal_param":false,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuRebondStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20251231
```

## Backtesting Output
```
2025-09-17 15:23:04,135 - freqtrade - INFO - freqtrade 2025.8
2025-09-17 15:23:04,539 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-09-17 15:23:06,449 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-09-17 15:23:06,459 - freqtrade.loggers - INFO - Enabling colorized output.
2025-09-17 15:23:06,461 - freqtrade.loggers - INFO - Logfile configured
2025-09-17 15:23:06,462 - freqtrade.loggers - INFO - Verbosity set to 0
2025-09-17 15:23:06,463 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2025-09-17 15:23:06,464 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 3 ...
2025-09-17 15:23:06,464 - freqtrade.configuration.configuration - INFO - Parameter --timeframe-detail detected, using 5m for intra-candle backtesting ...
2025-09-17 15:23:06,465 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20220101-20251231 ...
2025-09-17 15:23:06,868 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-09-17 15:23:06,871 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2025-09-17 15:23:06,872 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2025-09-17 15:23:06,872 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-09-17 15:23:06,874 - freqtrade.configuration.configuration - INFO - Using pairs ['BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'XRP/USDT', 'BNB/USDT']
2025-09-17 15:23:06,875 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20220101-20251231
2025-09-17 15:23:06,877 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-09-17 15:23:06,899 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2025-09-17 15:23:06,900 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 15:23:06,905 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-09-17 15:23:06,906 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-09-17 15:23:06,908 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.2
2025-09-17 15:23:06,947 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2025-09-17 15:23:09,550 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2025-09-17 15:23:09,684 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy IchimokuRebondStrategy from '/freqtrade/user_data/strategies/IchimokuRebondStrategy.py'...
2025-09-17 15:23:09,687 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/IchimokuRebondStrategy.json
2025-09-17 15:23:09,694 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2025-09-17 15:23:09,695 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-09-17 15:23:09,696 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-09-17 15:23:09,697 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 
'minutes'}.
2025-09-17 15:23:09,697 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 3.
2025-09-17 15:23:09,698 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {}
2025-09-17 15:23:09,699 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2025-09-17 15:23:09,699 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.1
2025-09-17 15:23:09,700 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-09-17 15:23:09,701 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-09-17 15:23:09,701 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-09-17 15:23:09,702 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2025-09-17 15:23:09,703 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-09-17 15:23:09,703 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 
'stoploss_on_exchange_interval': 60}
2025-09-17 15:23:09,704 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-09-17 15:23:09,704 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-09-17 15:23:09,705 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-09-17 15:23:09,705 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2025-09-17 15:23:09,706 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-09-17 15:23:09,706 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-09-17 15:23:09,706 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-09-17 15:23:09,707 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-09-17 15:23:09,707 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-09-17 15:23:09,708 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-09-17 15:23:09,708 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-09-17 15:23:09,709 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2025-09-17 15:23:09,709 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-09-17 15:23:09,709 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 3
2025-09-17 15:23:09,710 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-09-17 15:23:09,738 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-09-17 15:23:09,771 - freqtrade.optimize.backtesting - INFO - Using fee 0.1000% - worst case fee from exchange (lowest tier).
2025-09-17 15:23:09,837 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 15:23:09,932 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 15:23:10,009 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 15:23:10,083 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 15:23:10,177 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1h, data ends at 2025-09-10 08:00:00
2025-09-17 15:23:10,223 - freqtrade.optimize.backtesting - INFO - Loading data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-17 15:23:10,685 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 15:23:11,276 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 15:23:11,709 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 15:23:12,136 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 15:23:12,575 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 5m, data ends at 2025-09-10 09:15:00
2025-09-17 15:23:13,912 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-09-17 15:23:13,917 - freqtrade.optimize.backtesting - WARNING - Backtest result caching disabled due to use of open-ended timerange.
2025-09-17 15:23:13,917 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy IchimokuRebondStrategy
2025-09-17 15:23:13,918 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_spanA = False
2025-09-17 15:23:13,919 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_spanB = False
2025-09-17 15:23:13,920 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_kinjun_sup_tenkan = False
2025-09-17 15:23:13,920 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_sma200 = False
2025-09-17 15:23:13,921 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_spanA_sup_spanB = False
2025-09-17 15:23:13,921 - freqtrade.strategy.hyper - INFO - Strategy Parameter: entry_span_futur = False
2025-09-17 15:23:13,922 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_body_threshold = 4.564
2025-09-17 15:23:13,922 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_head_threshold = 0.932
2025-09-17 15:23:13,923 - freqtrade.strategy.hyper - INFO - Strategy Parameter: hammer_strength_threshold = 0.045
2025-09-17 15:23:13,923 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_max = 50
2025-09-17 15:23:13,923 - freqtrade.strategy.hyper - INFO - Strategy Parameter: rsi_entry_min = 20
2025-09-17 15:23:13,924 - freqtrade.strategy.hyper - INFO - Strategy Parameter: volume_factor = 1.0
2025-09-17 15:23:13,925 - freqtrade.strategy.hyper - INFO - Strategy Parameter: kinjun_threshold = 7
2025-09-17 15:23:13,925 - freqtrade.strategy.hyper - INFO - Strategy Parameter: lookback_period_for_stoploss = 8
2025-09-17 15:23:13,926 - freqtrade.strategy.hyper - INFO - Strategy Parameter: stoploss_margin = 0.996
2025-09-17 15:23:13,926 - freqtrade.strategy.hyper - INFO - Strategy Parameter: take_profit_multiplier = 2
2025-09-17 15:23:13,926 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_custom_stoploss_param = True
2025-09-17 15:23:13,927 - freqtrade.strategy.hyper - INFO - Strategy Parameter: use_sell_signal_param = False
2025-09-17 15:23:13,927 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-09-17 15:23:13,929 - freqtrade.data.dataprovider - INFO - Loading data for BTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 15:23:13,947 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 15:23:17,103 - freqtrade.data.dataprovider - INFO - Loading data for ETH/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 15:23:17,127 - freqtrade.data.history.datahandlers.idatahandler - WARNING - ETH/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 15:23:20,989 - freqtrade.data.dataprovider - INFO - Loading data for LTC/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 15:23:21,006 - freqtrade.data.history.datahandlers.idatahandler - WARNING - LTC/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 15:23:23,929 - freqtrade.data.dataprovider - INFO - Loading data for XRP/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 15:23:23,947 - freqtrade.data.history.datahandlers.idatahandler - WARNING - XRP/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 15:23:27,755 - freqtrade.data.dataprovider - INFO - Loading data for BNB/USDT 1d from 2022-01-01 00:00:00 to 2025-12-31 00:00:00
2025-09-17 15:23:27,778 - freqtrade.data.history.datahandlers.idatahandler - WARNING - BNB/USDT, spot, 1d, data ends at 2025-09-01 00:00:00
2025-09-17 15:23:31,804 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2022-01-01 00:00:00 up to 2025-09-10 08:00:00 (1348 days).
2025-09-17 15:24:12,983 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2025-09-17_15-24-12.meta.json"
Result for strategy IchimokuRebondStrategy
                                               BACKTESTING REPORT                                                
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ LTC/USDT │     12 │         5.39 │         168.849 │        16.88 │  1 day, 14:41:00 │    7     0     5  58.3 │
│ XRP/USDT │     12 │         3.65 │         121.668 │        12.17 │ 10 days, 8:59:00 │    6     0     6  50.0 │
│ BNB/USDT │      3 │         1.59 │          20.871 │         2.09 │  1 day, 17:47:00 │    1     0     2  33.3 │
│ BTC/USDT │      1 │        -5.52 │         -20.674 │        -2.07 │          2:05:00 │    0     0     1     0 │
│ ETH/USDT │      8 │        -1.58 │         -39.271 │        -3.93 │  6 days, 7:54:00 │    2     0     6  25.0 │
│    TOTAL │     36 │         2.64 │         251.443 │        25.14 │ 5 days, 13:11:00 │   16     0    20  44.4 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                  ENTER TAG STATS                                                  
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │      36 │         2.64 │         251.443 │        25.14 │ 5 days, 13:11:00 │   16     0    20  44.4 │
│     TOTAL │      36 │         2.64 │         251.443 │        25.14 │ 5 days, 13:11:00 │   16     0    20  44.4 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                   
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_2R │    16 │        13.61 │         613.705 │        61.37 │ 2 days, 16:54:00 │   16     0     0   100 │
│      stop_loss │    20 │        -6.13 │        -362.262 │       -36.23 │ 7 days, 19:49:00 │    0     0    20     0 │
│          TOTAL │    36 │         2.64 │         251.443 │        25.14 │ 5 days, 13:11:00 │   16     0    20  44.4 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                          MIXED TAG STATS                                                          
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_2R │     16 │        13.61 │         613.705 │        61.37 │ 2 days, 16:54:00 │   16     0     0   100 │
│           │      stop_loss │     20 │        -6.13 │        -362.262 │       -36.23 │ 7 days, 19:49:00 │    0     0    20     0 │
│     TOTAL │                │     36 │         2.64 │         251.443 │        25.14 │ 5 days, 13:11:00 │   16     0    20  44.4 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
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
│ Final balance                 │ 1251.443 USDT                   │
│ Absolute profit               │ 251.443 USDT                    │
│ Total profit %                │ 25.14%                          │
│ CAGR %                        │ 6.26%                           │
│ Sortino                       │ 0.53                            │
│ Sharpe                        │ 0.12                            │
│ Calmar                        │ 2.92                            │
│ SQN                           │ 1.41                            │
│ Profit factor                 │ 1.69                            │
│ Expectancy (Ratio)            │ 6.98 (0.39)                     │
│ Avg. daily profit             │ 0.187 USDT                      │
│ Avg. stake amount             │ 356.413 USDT                    │
│ Total trade volume            │ 25965.085 USDT                  │
│                               │                                 │
│ Best Pair                     │ LTC/USDT 16.88%                 │
│ Worst Pair                    │ ETH/USDT -3.93%                 │
│ Best trade                    │ LTC/USDT 29.80%                 │
│ Worst trade                   │ XRP/USDT -18.72%                │
│ Best day                      │ 57.364 USDT                     │
│ Worst day                     │ -41.902 USDT                    │
│ Days win/draw/lose            │ 16 / 1143 / 16                  │
│ Min/Max/Avg. Duration Winners │ 0d 02:45 / 10d 21:05 / 2d 16:54 │
│ Min/Max/Avg. Duration Losers  │ 0d 02:05 / 79d 02:20 / 7d 19:49 │
│ Max Consecutive Wins / Loss   │ 4 / 9                           │
│ Rejected Entry signals        │ 36                              │
│ Entry/Exit Timeouts           │ 0 / 0                           │
│                               │                                 │
│ Min balance                   │ 884.985 USDT                    │
│ Max balance                   │ 1277.658 USDT                   │
│ Max % of account underwater   │ 12.19%                          │
│ Absolute drawdown             │ 122.838 USDT (12.19%)           │
│ Drawdown duration             │ 267 days 23:45:00               │
│ Profit at drawdown start      │ 7.823 USDT                      │
│ Profit at drawdown end        │ -115.015 USDT                   │
│ Drawdown start                │ 2022-05-17 21:45:00             │
│ Drawdown end                  │ 2023-02-09 21:30:00             │
│ Market change                 │ 91.49%                          │
└───────────────────────────────┴─────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2025-09-10 08:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuRebondStrategy │     36 │         2.64 │         251.443 │        25.14 │ 5 days, 13:11:00 │   16     0    20  44.4 │ 122.838 USDT  12.19% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┴──────────────────────┘

```
