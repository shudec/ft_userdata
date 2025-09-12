# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Median Profit: -1.29%, Profit Factor: 0.66)

---
            
**Strategy:** RSIDivergenceBullishStrategy  
**Random State:** 4788  
**Timestamp:** 2025-09-12 17:43:25

## Configuration
```json
{
  "strategy": "RSIDivergenceBullishStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 4788,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy RSIDivergenceBullishStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 4788
```

## Hyperopt Output
```

Best result:

*   28/100:     97 trades. 41/0/56 Wins/Draws/Losses. Avg profit   0.39%. Median profit  -1.29%. Total profit -41.95752682 USDT (  -4.20%). Avg duration 16:25:00 min. Objective: 0.04412

{"params":{"lookback_period_for_divergence":55,"lookback_period_for_pivots":14,"pivot_confirmation_period":2,"rsi_oversold":29,"rsi_period":13,"lookback_period_for_stoploss":3,"stoploss_margin":0.998,"take_profit_multiplier":1,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ XRP/USDT │      8 │        -0.73 │          11.158 │         1.12 │     11:15:00 │    4     0     4  50.0 │
│ BNB/USDT │     10 │         0.05 │         -13.347 │        -1.33 │      6:55:00 │    4     0     6  40.0 │
│ ETH/USDT │     19 │        -0.64 │         -43.176 │        -4.32 │     11:36:00 │    8     0    11  42.1 │
│ BTC/USDT │     16 │        -0.83 │         -49.848 │        -4.98 │     11:23:00 │    7     0     9  43.8 │
│ LTC/USDT │     13 │        -1.29 │         -79.274 │        -7.93 │     10:46:00 │    3     0    10  23.1 │
│    TOTAL │     66 │        -0.72 │        -174.487 │       -17.45 │     10:38:00 │   26     0    40  39.4 │
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
│     OTHER │      66 │        -0.72 │        -174.487 │       -17.45 │     10:38:00 │   26     0    40  39.4 │
│     TOTAL │      66 │        -0.72 │        -174.487 │       -17.45 │     10:38:00 │   26     0    40  39.4 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │    26 │         2.88 │         336.996 │         33.7 │     10:20:00 │   26     0     0   100 │
│      stop_loss │    40 │        -3.07 │        -511.483 │       -51.15 │     10:50:00 │    0     0    40     0 │
│          TOTAL │    66 │        -0.72 │        -174.487 │       -17.45 │     10:38:00 │   26     0    40  39.4 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1R │     26 │         2.88 │         336.996 │         33.7 │     10:20:00 │   26     0     0   100 │
│           │      stop_loss │     40 │        -3.07 │        -511.483 │       -51.15 │     10:50:00 │    0     0    40     0 │
│     TOTAL │                │     66 │        -0.72 │        -174.487 │       -17.45 │     10:38:00 │   26     0    40  39.4 │
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
│ Total/Daily Avg Trades        │ 66 / 0.18                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 825.513 USDT                   │
│ Absolute profit               │ -174.487 USDT                  │
│ Total profit %                │ -17.45%                        │
│ CAGR %                        │ -17.49%                        │
│ Sortino                       │ -1.51                          │
│ Sharpe                        │ -0.66                          │
│ Calmar                        │ -4.46                          │
│ SQN                           │ -1.54                          │
│ Profit factor                 │ 0.66                           │
│ Expectancy (Ratio)            │ -2.64 (-0.21)                  │
│ Avg. daily profit             │ -0.479 USDT                    │
│ Avg. stake amount             │ 532.654 USDT                   │
│ Total trade volume            │ 70276.191 USDT                 │
│                               │                                │
│ Best Pair                     │ XRP/USDT 1.12%                 │
│ Worst Pair                    │ LTC/USDT -7.93%                │
│ Best trade                    │ LTC/USDT 8.16%                 │
│ Worst trade                   │ XRP/USDT -12.95%               │
│ Best day                      │ 20.464 USDT                    │
│ Worst day                     │ -39.696 USDT                   │
│ Days win/draw/lose            │ 20 / 308 / 29                  │
│ Min/Max/Avg. Duration Winners │ 0d 02:25 / 1d 09:10 / 0d 10:20 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:20 / 1d 21:05 / 0d 10:50 │
│ Max Consecutive Wins / Loss   │ 8 / 8                          │
│ Rejected Entry signals        │ 24                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 807.812 USDT                   │
│ Max balance                   │ 1016.675 USDT                  │
│ Max % of account underwater   │ 20.54%                         │
│ Absolute drawdown             │ 208.863 USDT (20.54%)          │
│ Drawdown duration             │ 344 days 03:20:00              │
│ Profit at drawdown start      │ 16.675 USDT                    │
│ Profit at drawdown end        │ -192.188 USDT                  │
│ Drawdown start                │ 2022-01-06 19:15:00            │
│ Drawdown end                  │ 2022-12-16 22:35:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                    STRATEGY SUMMARY                                                                    
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃                     Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ RSIDivergenceBullishStrategy │     66 │        -0.72 │        -174.487 │       -17.45 │     10:38:00 │   26     0    40  39.4 │ 208.863 USDT  20.54% │
└──────────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
