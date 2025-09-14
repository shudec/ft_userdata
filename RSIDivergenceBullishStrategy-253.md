# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Median Profit: 0.0%, Profit Factor: 5.88)

---
            
**Strategy:** RSIDivergenceBullishStrategy  
**Random State:** 253  
**Timestamp:** 2025-09-13 22:08:13

## Configuration
```json
{
  "strategy": "RSIDivergenceBullishStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell roi",
  "random_state": 253,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy RSIDivergenceBullishStrategy --timeframe 1h --epochs 100 --spaces buy sell roi --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 253
```

## Hyperopt Output
```

Best result:

    76/100:     17 trades. 7/2/8 Wins/Draws/Losses. Avg profit   0.49%. Median profit   0.00%. Total profit -45.62063698 USDT (  -4.56%). Avg duration 17:00:00 min. Objective: 0.06014

{"params":{"rsi_oversold":21,"lookback_period_for_divergence":72,"lookback_period_for_pivots":12,"rsi_period":14,"volume_factor":2,"volume_sma_period":20,"lookback_period_for_stoploss":4,"stoploss_margin":0.992,"take_profit_multiplier":1.5,"use_custom_stoploss_param":true},"minimal_roi":{"0":0.605,"324":0.184,"905":0.072,"1949":0},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy RSIDivergenceBullishStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20221231
```

## Backtesting Output
```
Result for strategy RSIDivergenceBullishStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         9.05 │          58.263 │         5.83 │     10:10:00 │    1     0     0   100 │
│ LTC/USDT │      2 │          6.9 │          35.840 │         3.58 │     10:42:00 │    2     0     0   100 │
│ BTC/USDT │      1 │         4.48 │          33.046 │          3.3 │      9:20:00 │    1     0     0   100 │
│ XRP/USDT │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
│ ETH/USDT │      2 │         1.93 │         -14.365 │        -1.44 │      5:22:00 │    1     0     1  50.0 │
│    TOTAL │      6 │          5.2 │         112.783 │        11.28 │      8:37:00 │    5     0     1  83.3 │
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
│     OTHER │       6 │          5.2 │         112.783 │        11.28 │      8:37:00 │    5     0     1  83.3 │
│     TOTAL │       6 │          5.2 │         112.783 │        11.28 │      8:37:00 │    5     0     1  83.3 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │     5 │         6.75 │         135.897 │        13.59 │     10:03:00 │    5     0     0   100 │
│        stop_loss │     1 │        -2.56 │         -23.113 │        -2.31 │      1:25:00 │    0     0     1     0 │
│            TOTAL │     6 │          5.2 │         112.783 │        11.28 │      8:37:00 │    5     0     1  83.3 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1.5R │      5 │         6.75 │         135.897 │        13.59 │     10:03:00 │    5     0     0   100 │
│           │        stop_loss │      1 │        -2.56 │         -23.113 │        -2.31 │      1:25:00 │    0     0     1     0 │
│     TOTAL │                  │      6 │          5.2 │         112.783 │        11.28 │      8:37:00 │    5     0     1  83.3 │
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
│ Total/Daily Avg Trades        │ 6 / 0.02                       │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1112.783 USDT                  │
│ Absolute profit               │ 112.783 USDT                   │
│ Total profit %                │ 11.28%                         │
│ CAGR %                        │ 11.31%                         │
│ Sortino                       │ -100.00                        │
│ Sharpe                        │ 0.23                           │
│ Calmar                        │ 27.60                          │
│ SQN                           │ 1.64                           │
│ Profit factor                 │ 5.88                           │
│ Expectancy (Ratio)            │ 18.80 (0.81)                   │
│ Avg. daily profit             │ 0.31 USDT                      │
│ Avg. stake amount             │ 475.87 USDT                    │
│ Total trade volume            │ 5834.877 USDT                  │
│                               │                                │
│ Best Pair                     │ BNB/USDT 5.83%                 │
│ Worst Pair                    │ ETH/USDT -1.44%                │
│ Best trade                    │ LTC/USDT 9.47%                 │
│ Worst trade                   │ ETH/USDT -2.56%                │
│ Best day                      │ 58.263 USDT                    │
│ Worst day                     │ -23.113 USDT                   │
│ Days win/draw/lose            │ 3 / 179 / 1                    │
│ Min/Max/Avg. Duration Winners │ 0d 09:20 / 0d 12:05 / 0d 10:03 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:25 / 0d 01:25 / 0d 01:25 │
│ Max Consecutive Wins / Loss   │ 4 / 1                          │
│ Rejected Entry signals        │ 24                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 1030.994 USDT                  │
│ Max balance                   │ 1112.783 USDT                  │
│ Max % of account underwater   │ 2.14%                          │
│ Absolute Drawdown (Account)   │ 2.14%                          │
│ Absolute Drawdown             │ 23.113 USDT                    │
│ Drawdown high                 │ 77.634 USDT                    │
│ Drawdown low                  │ 54.521 USDT                    │
│ Drawdown Start                │ 2022-07-13 23:20:00            │
│ Drawdown End                  │ 2022-09-16 16:25:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃                     Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ RSIDivergenceBullishStrategy │      6 │         5.20 │         112.783 │        11.28 │      8:37:00 │    5     0     1  83.3 │ 23.113 USDT  2.14% │
└──────────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```
