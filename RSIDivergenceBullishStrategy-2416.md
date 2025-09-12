# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Median Profit: 0.0%, Profit Factor: 0.76)

---
            
**Strategy:** RSIDivergenceBullishStrategy  
**Random State:** 2416  
**Timestamp:** 2025-09-12 17:09:30

## Configuration
```json
{
  "strategy": "RSIDivergenceBullishStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 2416,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy RSIDivergenceBullishStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 2416
```

## Hyperopt Output
```

Best result:

    45/100:    113 trades. 55/23/35 Wins/Draws/Losses. Avg profit   0.56%. Median profit   0.00%. Total profit 272.26488661 USDT (  27.23%). Avg duration 17:52:00 min. Objective: -0.29467

{"params":{"lookback_period_for_divergence":58,"lookback_period_for_pivots":4,"pivot_confirmation_period":1,"rsi_oversold":22,"rsi_period":11,"lookback_period_for_stoploss":6,"stoploss_margin":0.99,"take_profit_multiplier":1,"use_custom_stoploss_param":true},"minimal_roi":{"0":0.255,"159":0.097,"459":0.056,"1462":0},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ XRP/USDT │      8 │        -0.09 │          24.503 │         2.45 │     12:11:00 │    5     0     3  62.5 │
│ LTC/USDT │     11 │        -0.15 │           5.655 │         0.57 │     10:09:00 │    6     0     5  54.5 │
│ BTC/USDT │      5 │        -0.07 │          -6.770 │        -0.68 │     14:05:00 │    3     0     2  60.0 │
│ BNB/USDT │      7 │        -1.32 │         -20.491 │        -2.05 │      6:52:00 │    3     0     4  42.9 │
│ ETH/USDT │     10 │        -1.44 │         -95.073 │        -9.51 │     11:24:00 │    2     2     6  20.0 │
│    TOTAL │     41 │        -0.64 │         -92.176 │        -9.22 │     10:46:00 │   19     2    20  46.3 │
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
│     OTHER │      41 │        -0.64 │         -92.176 │        -9.22 │     10:46:00 │   19     2    20  46.3 │
│     TOTAL │      41 │        -0.64 │         -92.176 │        -9.22 │     10:46:00 │   19     2    20  46.3 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │    12 │         3.23 │         232.312 │        23.23 │      9:25:00 │   12     0     0   100 │
│            roi │     9 │         2.84 │          63.754 │         6.38 │     19:50:00 │    7     2     0   100 │
│      stop_loss │    20 │        -4.53 │        -388.242 │       -38.82 │      7:30:00 │    0     0    20     0 │
│          TOTAL │    41 │        -0.64 │         -92.176 │        -9.22 │     10:46:00 │   19     2    20  46.3 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1R │     12 │         3.23 │         232.312 │        23.23 │      9:25:00 │   12     0     0   100 │
│           │            roi │      9 │         2.84 │          63.754 │         6.38 │     19:50:00 │    7     2     0   100 │
│           │      stop_loss │     20 │        -4.53 │        -388.242 │       -38.82 │      7:30:00 │    0     0    20     0 │
│     TOTAL │                │     41 │        -0.64 │         -92.176 │        -9.22 │     10:46:00 │   19     2    20  46.3 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2022-12-31 00:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 41 / 0.11                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 907.824 USDT                   │
│ Absolute profit               │ -92.176 USDT                   │
│ Total profit %                │ -9.22%                         │
│ CAGR %                        │ -9.24%                         │
│ Sortino                       │ -2.23                          │
│ Sharpe                        │ -0.27                          │
│ Calmar                        │ -5.25                          │
│ SQN                           │ -0.80                          │
│ Profit factor                 │ 0.76                           │
│ Expectancy (Ratio)            │ -2.25 (-0.16)                  │
│ Avg. daily profit             │ -0.253 USDT                    │
│ Avg. stake amount             │ 510.485 USDT                   │
│ Total trade volume            │ 41851.241 USDT                 │
│                               │                                │
│ Best Pair                     │ XRP/USDT 2.45%                 │
│ Worst Pair                    │ ETH/USDT -9.51%                │
│ Best trade                    │ XRP/USDT 5.59%                 │
│ Worst trade                   │ XRP/USDT -12.19%               │
│ Best day                      │ 26.469 USDT                    │
│ Worst day                     │ -40.638 USDT                   │
│ Days win/draw/lose            │ 15 / 301 / 15                  │
│ Min/Max/Avg. Duration Winners │ 0d 04:40 / 1d 00:25 / 0d 12:43 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 0d 19:55 / 0d 07:30 │
│ Max Consecutive Wins / Loss   │ 4 / 3                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 907.824 USDT                   │
│ Max balance                   │ 995.537 USDT                   │
│ Max % of account underwater   │ 9.22%                          │
│ Absolute drawdown             │ 92.176 USDT (9.22%)            │
│ Drawdown duration             │ 329 days 08:35:00              │
│ Profit at drawdown start      │ -12.557 USDT                   │
│ Profit at drawdown end        │ -92.176 USDT                   │
│ Drawdown start                │ 2022-01-21 21:25:00            │
│ Drawdown end                  │ 2022-12-17 06:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃                     Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ RSIDivergenceBullishStrategy │     41 │        -0.64 │         -92.176 │        -9.22 │     10:46:00 │   19     2    20  46.3 │ 92.176 USDT  9.22% │
└──────────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```
