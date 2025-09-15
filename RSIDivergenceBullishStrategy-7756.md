# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Median Profit: -1.66%, Profit Factor: 0.74)

---
            
**Strategy:** RSIDivergenceBullishStrategy  
**Random State:** 7756  
**Timestamp:** 2025-09-12 18:04:13

## Configuration
```json
{
  "strategy": "RSIDivergenceBullishStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy",
  "random_state": 7756,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy RSIDivergenceBullishStrategy --timeframe 1h --epochs 100 --spaces buy --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 7756
```

## Hyperopt Output
```

Best result:

*    7/100:     18 trades. 7/0/11 Wins/Draws/Losses. Avg profit   0.99%. Median profit  -1.66%. Total profit 36.40063506 USDT (   3.64%). Avg duration 16:47:00 min. Objective: -0.02979

{"params":{"lookback_period_for_divergence":47,"lookback_period_for_pivots":17,"pivot_confirmation_period":1,"rsi_oversold":29,"rsi_period":13,"lookback_period_for_stoploss":5,"stoploss_margin":0.998,"take_profit_multiplier":1.5,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ XRP/USDT │      7 │        -0.78 │          14.349 │         1.43 │ 1 day, 20:08:00 │    3     0     4  42.9 │
│ BNB/USDT │     12 │        -0.71 │           4.713 │         0.47 │         7:09:00 │    4     0     8  33.3 │
│ BTC/USDT │     11 │        -0.79 │          -7.957 │         -0.8 │        14:07:00 │    5     0     6  45.5 │
│ LTC/USDT │     20 │         -0.6 │         -85.878 │        -8.59 │        16:24:00 │    6     0    14  30.0 │
│ ETH/USDT │     12 │        -1.13 │        -102.307 │       -10.23 │        14:50:00 │    3     0     9  25.0 │
│    TOTAL │     62 │        -0.78 │        -177.080 │       -17.71 │        17:02:00 │   21     0    41  33.9 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
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
│     OTHER │      62 │        -0.78 │        -177.080 │       -17.71 │     17:02:00 │   21     0    41  33.9 │
│     TOTAL │      62 │        -0.78 │        -177.080 │       -17.71 │     17:02:00 │   21     0    41  33.9 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │    21 │         5.45 │         493.448 │        49.34 │     23:54:00 │   21     0     0   100 │
│        stop_loss │    41 │        -3.97 │        -670.528 │       -67.05 │     13:31:00 │    0     0    41     0 │
│            TOTAL │    62 │        -0.78 │        -177.080 │       -17.71 │     17:02:00 │   21     0    41  33.9 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1.5R │     21 │         5.45 │         493.448 │        49.34 │     23:54:00 │   21     0     0   100 │
│           │        stop_loss │     41 │        -3.97 │        -670.528 │       -67.05 │     13:31:00 │    0     0    41     0 │
│     TOTAL │                  │     62 │        -0.78 │        -177.080 │       -17.71 │     17:02:00 │   21     0    41  33.9 │
└───────────┴──────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2022-12-31 00:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 62 / 0.17                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 822.92 USDT                    │
│ Absolute profit               │ -177.08 USDT                   │
│ Total profit %                │ -17.71%                        │
│ CAGR %                        │ -17.75%                        │
│ Sortino                       │ -2.16                          │
│ Sharpe                        │ -0.47                          │
│ Calmar                        │ -3.78                          │
│ SQN                           │ -1.13                          │
│ Profit factor                 │ 0.74                           │
│ Expectancy (Ratio)            │ -2.86 (-0.17)                  │
│ Avg. daily profit             │ -0.486 USDT                    │
│ Avg. stake amount             │ 596.169 USDT                   │
│ Total trade volume            │ 73895.58 USDT                  │
│                               │                                │
│ Best Pair                     │ XRP/USDT 1.43%                 │
│ Worst Pair                    │ ETH/USDT -10.23%               │
│ Best trade                    │ XRP/USDT 17.29%                │
│ Worst trade                   │ XRP/USDT -17.35%               │
│ Best day                      │ 48.029 USDT                    │
│ Worst day                     │ -49.819 USDT                   │
│ Days win/draw/lose            │ 18 / 290 / 31                  │
│ Min/Max/Avg. Duration Winners │ 0d 04:50 / 4d 00:40 / 0d 23:54 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:25 / 4d 16:05 / 0d 13:31 │
│ Max Consecutive Wins / Loss   │ 4 / 7                          │
│ Rejected Entry signals        │ 36                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 796.576 USDT                   │
│ Max balance                   │ 1056.472 USDT                  │
│ Max % of account underwater   │ 24.60%                         │
│ Absolute drawdown             │ 259.896 USDT (24.60%)          │
│ Drawdown duration             │ 259 days 10:00:00              │
│ Profit at drawdown start      │ 56.472 USDT                    │
│ Profit at drawdown end        │ -203.424 USDT                  │
│ Drawdown start                │ 2022-04-01 20:00:00            │
│ Drawdown end                  │ 2022-12-17 06:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                    STRATEGY SUMMARY                                                                    
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃                     Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ RSIDivergenceBullishStrategy │     62 │        -0.78 │        -177.080 │       -17.71 │     17:02:00 │   21     0    41  33.9 │ 259.896 USDT  24.60% │
└──────────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
