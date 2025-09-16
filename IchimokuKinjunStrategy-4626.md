# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 269 / 0.74, Median: -0.72%, Total profit: -17.29%, Sortino: -2.13, Sharpe: -1.08, Calmar: -3.84, Drawdown: 23.62%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 4626  
**Timestamp:** 2025-09-15 22:24:34

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 4626,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 4626
```

## Hyperopt Output
```

Best result:

*   16/100:    502 trades. 168/0/334 Wins/Draws/Losses. Avg profit   0.77%. Median profit  -0.72%. Total profit 2163.84719663 USDT ( 216.38%). Avg duration 19:28:00 min. Objective: -1.36663

{"params":{"stoploss_margin":1.0,"lookback_period_for_stoploss":0,"take_profit_multiplier":3,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuKinjunStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20221231
```

## Backtesting Output
```
Result for strategy IchimokuKinjunStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ XRP/USDT │     50 │         0.11 │          12.051 │         1.21 │     14:41:00 │   15     0    35  30.0 │
│ BNB/USDT │     60 │        -0.05 │          -4.073 │        -0.41 │     15:59:00 │   18     0    42  30.0 │
│ ETH/USDT │     60 │        -0.08 │         -22.616 │        -2.26 │     17:51:00 │   19     0    41  31.7 │
│ BTC/USDT │     52 │        -0.38 │         -55.798 │        -5.58 │     17:21:00 │   13     0    39  25.0 │
│ LTC/USDT │     47 │        -0.66 │        -102.465 │       -10.25 │     21:28:00 │   15     0    32  31.9 │
│    TOTAL │    269 │         -0.2 │        -172.901 │       -17.29 │     17:23:00 │   80     0   189  29.7 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                           LEFT OPEN TRADES REPORT                                           
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │         0.09 │           0.233 │         0.02 │      1:00:00 │    1     0     0   100 │
│    TOTAL │      1 │         0.09 │           0.233 │         0.02 │      1:00:00 │    1     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                ENTER TAG STATS                                                
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │     269 │         -0.2 │        -172.901 │       -17.29 │     17:23:00 │   80     0   189  29.7 │
│     TOTAL │     269 │         -0.2 │        -172.901 │       -17.29 │     17:23:00 │   80     0   189  29.7 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                               EXIT REASON STATS                                               
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  force_exit │     1 │         0.09 │           0.233 │         0.02 │      1:00:00 │    1     0     0   100 │
│   stop_loss │     1 │        -3.57 │         -11.782 │        -1.18 │      3:50:00 │    0     0     1     0 │
│ exit_signal │   267 │        -0.18 │        -161.352 │       -16.14 │     17:29:00 │   79     0   188  29.6 │
│       TOTAL │   269 │         -0.2 │        -172.901 │       -17.29 │     17:23:00 │   80     0   189  29.7 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                      MIXED TAG STATS                                                       
┏━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │  force_exit │      1 │         0.09 │           0.233 │         0.02 │      1:00:00 │    1     0     0   100 │
│           │   stop_loss │      1 │        -3.57 │         -11.782 │        -1.18 │      3:50:00 │    0     0     1     0 │
│           │ exit_signal │    267 │        -0.18 │        -161.352 │       -16.14 │     17:29:00 │   79     0   188  29.6 │
│     TOTAL │             │    269 │         -0.2 │        -172.901 │       -17.29 │     17:23:00 │   80     0   189  29.7 │
└───────────┴─────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2022-12-31 00:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 269 / 0.74                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 827.099 USDT                   │
│ Absolute profit               │ -172.901 USDT                  │
│ Total profit %                │ -17.29%                        │
│ CAGR %                        │ -17.33%                        │
│ Sortino                       │ -2.13                          │
│ Sharpe                        │ -1.08                          │
│ Calmar                        │ -3.84                          │
│ SQN                           │ -1.25                          │
│ Profit factor                 │ 0.80                           │
│ Expectancy (Ratio)            │ -0.64 (-0.14)                  │
│ Avg. daily profit             │ -0.475 USDT                    │
│ Avg. stake amount             │ 305.941 USDT                   │
│ Total trade volume            │ 164752.354 USDT                │
│                               │                                │
│ Best Pair                     │ XRP/USDT 1.21%                 │
│ Worst Pair                    │ LTC/USDT -10.25%               │
│ Best trade                    │ XRP/USDT 17.78%                │
│ Worst trade                   │ LTC/USDT -11.18%               │
│ Best day                      │ 55.032 USDT                    │
│ Worst day                     │ -38.97 USDT                    │
│ Days win/draw/lose            │ 50 / 218 / 94                  │
│ Min/Max/Avg. Duration Winners │ 0d 01:00 / 4d 07:00 / 1d 09:20 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 3d 00:00 / 0d 10:37 │
│ Max Consecutive Wins / Loss   │ 6 / 17                         │
│ Rejected Entry signals        │ 252                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 806.23 USDT                    │
│ Max balance                   │ 1055.607 USDT                  │
│ Max % of account underwater   │ 23.62%                         │
│ Absolute Drawdown (Account)   │ 23.62%                         │
│ Absolute Drawdown             │ 249.377 USDT                   │
│ Drawdown high                 │ 55.607 USDT                    │
│ Drawdown low                  │ -193.77 USDT                   │
│ Drawdown Start                │ 2022-02-16 04:00:00            │
│ Drawdown End                  │ 2022-09-23 09:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │    269 │        -0.20 │        -172.901 │       -17.29 │     17:23:00 │   80     0   189  29.7 │ 249.377 USDT  23.62% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
