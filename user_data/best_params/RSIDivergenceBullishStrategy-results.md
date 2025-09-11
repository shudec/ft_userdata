# RSIDivergenceBullishStrategy

## Hyperopt 10000 sell buy roi

Best result:

    44/100:     87 trades. 46/15/26 Wins/Draws/Losses. Avg profit   0.43%. Median profit   0.18%. Total profit 129.67997315 USDT (  12.97%). Avg duration 15:48:00 min. Objective: -0.18514

```json
{
    "params": {
        "lookback_period_for_divergence": 23,
        "lookback_period_for_pivots": 19,
        "pivot_confirmation_period": 1,
        "rsi_oversold": 36,
        "rsi_period": 11,
        "lookback_period_for_stoploss": 4,
        "stoploss_margin": 0.991,
        "take_profit_multiplier": 1,
        "use_custom_stoploss_param": true
    },
    "minimal_roi": {
        "0": 0.255,
        "159": 0.097,
        "459": 0.056,
        "1462": 0
    },
    "stoploss": -0.1,
    "trailing_stop": false,
    "trailing_stop_positive": null,
    "trailing_stop_positive_offset": 0.0,
    "trailing_only_offset_is_reached": false,
    "max_open_trades": 3
}
```

### Backtesting

```

                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │     40 │         0.69 │         199.757 │        19.98 │     16:27:00 │   25     3    12  62.5 │
│ LTC/USDT │     75 │         0.42 │          95.649 │         9.56 │     14:00:00 │   41     7    27  54.7 │
│ XRP/USDT │     56 │         0.19 │          28.156 │         2.82 │     15:16:00 │   30     6    20  53.6 │
│ BNB/USDT │     48 │        -0.05 │           1.370 │         0.14 │     12:27:00 │   24     2    22  50.0 │
│ ETH/USDT │     73 │         0.33 │         -49.653 │        -4.97 │     15:23:00 │   39     8    26  53.4 │
│    TOTAL │    292 │         0.31 │         275.278 │        27.53 │     14:40:00 │  159    26   107  54.5 │
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
│     OTHER │     292 │         0.31 │         275.278 │        27.53 │     14:40:00 │  159    26   107  54.5 │
│     TOTAL │     292 │         0.31 │         275.278 │        27.53 │     14:40:00 │  159    26   107  54.5 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │    89 │         3.37 │        1995.883 │       199.59 │       10:31:00 │   89     0     0   100 │
│            roi │    96 │         2.15 │         636.471 │        63.65 │ 1 day, 0:14:00 │   70    26     0   100 │
│      stop_loss │   107 │        -3.88 │       -2357.076 │      -235.71 │        9:33:00 │    0     0   107     0 │
│          TOTAL │   292 │         0.31 │         275.278 │        27.53 │       14:40:00 │  159    26   107  54.5 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1R │     89 │         3.37 │        1995.883 │       199.59 │       10:31:00 │   89     0     0   100 │
│           │            roi │     96 │         2.15 │         636.471 │        63.65 │ 1 day, 0:14:00 │   70    26     0   100 │
│           │      stop_loss │    107 │        -3.88 │       -2357.076 │      -235.71 │        9:33:00 │    0     0   107     0 │
│     TOTAL │                │    292 │         0.31 │         275.278 │        27.53 │       14:40:00 │  159    26   107  54.5 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2019-01-01 00:00:00            │
│ Backtesting to                │ 2025-09-11 17:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 292 / 0.12                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1275.278 USDT                  │
│ Absolute profit               │ 275.278 USDT                   │
│ Total profit %                │ 27.53%                         │
│ CAGR %                        │ 3.70%                          │
│ Sortino                       │ 0.31                           │
│ Sharpe                        │ 0.11                           │
│ Calmar                        │ 1.08                           │
│ SQN                           │ 0.81                           │
│ Profit factor                 │ 1.12                           │
│ Expectancy (Ratio)            │ 0.94 (-0.05)                   │
│ Avg. daily profit             │ 0.113 USDT                     │
│ Avg. stake amount             │ 619.654 USDT                   │
│ Total trade volume            │ 362878.18 USDT                 │
│                               │                                │
│ Best Pair                     │ BTC/USDT 19.98%                │
│ Worst Pair                    │ ETH/USDT -4.97%                │
│ Best trade                    │ XRP/USDT 9.69%                 │
│ Worst trade                   │ XRP/USDT -17.94%               │
│ Best day                      │ 45.295 USDT                    │
│ Worst day                     │ -69.972 USDT                   │
│ Days win/draw/lose            │ 125 / 2223 / 83                │
│ Min/Max/Avg. Duration Winners │ 0d 01:10 / 1d 00:25 / 0d 14:56 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:15 / 1d 11:10 / 0d 09:33 │
│ Max Consecutive Wins / Loss   │ 12 / 6                         │
│ Rejected Entry signals        │ 84                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 1003.721 USDT                  │
│ Max balance                   │ 1437.605 USDT                  │
│ Max % of account underwater   │ 19.92%                         │
│ Absolute Drawdown (Account)   │ 19.92%                         │
│ Absolute Drawdown             │ 286.419 USDT                   │
│ Drawdown high                 │ 437.605 USDT                   │
│ Drawdown low                  │ 151.185 USDT                   │
│ Drawdown Start                │ 2022-04-10 02:25:00            │
│ Drawdown End                  │ 2024-08-05 00:55:00            │
│ Market change                 │ 4411.86%                       │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2019-01-01 00:00:00 -> 2025-09-11 17:00:00 | Max open trades : 3
                                                                    STRATEGY SUMMARY                                                                    
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃                     Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ RSIDivergenceBullishStrategy │    292 │         0.31 │         275.278 │        27.53 │     14:40:00 │  159    26   107  54.5 │ 286.419 USDT  19.92% │
└──────────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```