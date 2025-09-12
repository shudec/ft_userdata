# Freqtrade Automation Log
            
**Strategy:** RSIDivergenceBullishStrategy  
**Random State:** 5649  
**Timestamp:** 2025-09-12 13:59:39

## Configuration
```json
{
  "strategy": "RSIDivergenceBullishStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 5649,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy RSIDivergenceBullishStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 5649
```

## Hyperopt Output
```

Best result:

*    7/100:    101 trades. 40/38/23 Wins/Draws/Losses. Avg profit  -0.64%. Median profit   0.00%. Total profit -112.57690085 USDT ( -11.26%). Avg duration 23:44:00 min. Objective: 0.25711

{"params":{"lookback_period_for_divergence":95,"lookback_period_for_pivots":16,"pivot_confirmation_period":1,"rsi_oversold":22,"rsi_period":18,"lookback_period_for_stoploss":6,"stoploss_margin":0.996,"take_profit_multiplier":1,"use_custom_stoploss_param":false},"minimal_roi":{"0":0.255,"159":0.097,"459":0.056,"1462":0},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy RSIDivergenceBullishStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20221231
```

## Backtesting Output
```
Result for strategy RSIDivergenceBullishStrategy
                                               BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │      8 │        -0.29 │          -8.619 │        -0.86 │        17:06:00 │    4     2     2  50.0 │
│ BTC/USDT │      9 │        -1.04 │         -18.711 │        -1.87 │  1 day, 2:24:00 │    5     2     2  55.6 │
│ ETH/USDT │      9 │        -1.43 │         -22.821 │        -2.28 │  1 day, 5:01:00 │    3     4     2  33.3 │
│ BNB/USDT │     12 │        -2.28 │         -34.180 │        -3.42 │        22:51:00 │    5     3     4  41.7 │
│ LTC/USDT │     19 │        -1.26 │         -41.220 │        -4.12 │ 1 day, 10:59:00 │    9     5     5  47.4 │
│    TOTAL │     57 │        -1.33 │        -125.550 │       -12.56 │  1 day, 3:37:00 │   26    16    15  45.6 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 ENTER TAG STATS                                                 
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │      57 │        -1.33 │        -125.550 │       -12.56 │ 1 day, 3:37:00 │   26    16    15  45.6 │
│     TOTAL │      57 │        -1.33 │        -125.550 │       -12.56 │ 1 day, 3:37:00 │   26    16    15  45.6 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│         roi │    42 │         1.83 │         132.681 │        13.27 │ 1 day, 8:24:00 │   26    16     0   100 │
│   stop_loss │    15 │       -10.18 │        -258.231 │       -25.82 │       14:15:00 │    0     0    15     0 │
│       TOTAL │    57 │        -1.33 │        -125.550 │       -12.56 │ 1 day, 3:37:00 │   26    16    15  45.6 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                       MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │         roi │     42 │         1.83 │         132.681 │        13.27 │ 1 day, 8:24:00 │   26    16     0   100 │
│           │   stop_loss │     15 │       -10.18 │        -258.231 │       -25.82 │       14:15:00 │    0     0    15     0 │
│     TOTAL │             │     57 │        -1.33 │        -125.550 │       -12.56 │ 1 day, 3:37:00 │   26    16    15  45.6 │
└───────────┴─────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2022-12-31 00:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 57 / 0.16                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 874.45 USDT                    │
│ Absolute profit               │ -125.55 USDT                   │
│ Total profit %                │ -12.56%                        │
│ CAGR %                        │ -12.59%                        │
│ Sortino                       │ -3.06                          │
│ Sharpe                        │ -0.69                          │
│ Calmar                        │ -4.78                          │
│ SQN                           │ -1.72                          │
│ Profit factor                 │ 0.51                           │
│ Expectancy (Ratio)            │ -2.20 (-0.41)                  │
│ Avg. daily profit             │ -0.345 USDT                    │
│ Avg. stake amount             │ 169.78 USDT                    │
│ Total trade volume            │ 19267.881 USDT                 │
│                               │                                │
│ Best Pair                     │ XRP/USDT -0.86%                │
│ Worst Pair                    │ LTC/USDT -4.12%                │
│ Best trade                    │ XRP/USDT 5.59%                 │
│ Worst trade                   │ BTC/USDT -10.18%               │
│ Best day                      │ 13.649 USDT                    │
│ Worst day                     │ -51.018 USDT                   │
│ Days win/draw/lose            │ 19 / 312 / 9                   │
│ Min/Max/Avg. Duration Winners │ 0d 08:30 / 1d 00:25 / 0d 21:22 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:15 / 3d 02:55 / 0d 14:15 │
│ Max Consecutive Wins / Loss   │ 7 / 6                          │
│ Rejected Entry signals        │ 48                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 864.861 USDT                   │
│ Max balance                   │ 1003.084 USDT                  │
│ Max % of account underwater   │ 13.78%                         │
│ Absolute drawdown             │ 138.222 USDT (13.78%)          │
│ Drawdown duration             │ 293 days 10:40:00              │
│ Profit at drawdown start      │ 3.084 USDT                     │
│ Profit at drawdown end        │ -135.139 USDT                  │
│ Drawdown start                │ 2022-01-20 10:25:00            │
│ Drawdown end                  │ 2022-11-09 21:05:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                     STRATEGY SUMMARY                                                                     
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃                     Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ RSIDivergenceBullishStrategy │     57 │        -1.33 │        -125.550 │       -12.56 │ 1 day, 3:37:00 │   26    16    15  45.6 │ 138.222 USDT  13.78% │
└──────────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┴──────────────────────┘

```
