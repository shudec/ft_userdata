# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 269 / 0.74, Median: -0.84%, Total profit: -28.55%, Sortino: -3.59, Sharpe: -1.32, Calmar: -4.07, Drawdown: 36.79%)

---
            
**Strategy:** IchimokuStrategyV4  
**Random State:** 8885  
**Timestamp:** 2025-09-15 21:52:30

## Configuration
```json
{
  "strategy": "IchimokuStrategyV4",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 8885,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuStrategyV4 --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 8885
```

## Hyperopt Output
```

Best result:

*   14/100:    712 trades. 228/0/484 Wins/Draws/Losses. Avg profit   0.58%. Median profit  -0.84%. Total profit 7621.83303743 USDT ( 762.18%). Avg duration 15:52:00 min. Objective: -1.42911

{"params":{"stoploss_margin":0.992,"lookback_period_for_stoploss":5,"take_profit_multiplier":2,"use_custom_stoploss_param":true},"minimal_roi":{"0":2},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":0.01,"trailing_stop_positive_offset":0.017,"trailing_only_offset_is_reached":true,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuStrategyV4 --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20221231
```

## Backtesting Output
```
Result for strategy IchimokuStrategyV4
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ETH/USDT │     49 │         0.06 │          32.658 │         3.27 │     16:35:00 │   15     0    34  30.6 │
│ BTC/USDT │     53 │        -0.56 │         -36.311 │        -3.63 │     14:47:00 │   15     0    38  28.3 │
│ BNB/USDT │     59 │        -0.45 │         -55.063 │        -5.51 │     15:07:00 │   14     0    45  23.7 │
│ XRP/USDT │     47 │        -0.34 │        -106.229 │       -10.62 │     12:02:00 │   10     0    37  21.3 │
│ LTC/USDT │     61 │        -0.68 │        -120.531 │       -12.05 │     12:20:00 │   14     0    47  23.0 │
│    TOTAL │    269 │        -0.41 │        -285.476 │       -28.55 │     14:09:00 │   68     0   201  25.3 │
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
│     OTHER │     269 │        -0.41 │        -285.476 │       -28.55 │     14:09:00 │   68     0   201  25.3 │
│     TOTAL │     269 │        -0.41 │        -285.476 │       -28.55 │     14:09:00 │   68     0   201  25.3 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ tenkan-weakness │    15 │         7.95 │         477.767 │        47.78 │ 1 day, 8:13:00 │   15     0     0   100 │
│       stop_loss │    31 │        -2.54 │        -223.668 │       -22.37 │        7:53:00 │    0     0    31     0 │
│     exit_signal │   223 │        -0.67 │        -539.575 │       -53.96 │       13:48:00 │   53     0   170  23.8 │
│           TOTAL │   269 │        -0.41 │        -285.476 │       -28.55 │       14:09:00 │   68     0   201  25.3 │
└─────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                          
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃     Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ tenkan-weakness │     15 │         7.95 │         477.767 │        47.78 │ 1 day, 8:13:00 │   15     0     0   100 │
│           │       stop_loss │     31 │        -2.54 │        -223.668 │       -22.37 │        7:53:00 │    0     0    31     0 │
│           │     exit_signal │    223 │        -0.67 │        -539.575 │       -53.96 │       13:48:00 │   53     0   170  23.8 │
│     TOTAL │                 │    269 │        -0.41 │        -285.476 │       -28.55 │       14:09:00 │   68     0   201  25.3 │
└───────────┴─────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
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
│ Final balance                 │ 714.524 USDT                   │
│ Absolute profit               │ -285.476 USDT                  │
│ Total profit %                │ -28.55%                        │
│ CAGR %                        │ -28.61%                        │
│ Sortino                       │ -3.59                          │
│ Sharpe                        │ -1.32                          │
│ Calmar                        │ -4.07                          │
│ SQN                           │ -1.54                          │
│ Profit factor                 │ 0.73                           │
│ Expectancy (Ratio)            │ -1.06 (-0.20)                  │
│ Avg. daily profit             │ -0.784 USDT                    │
│ Avg. stake amount             │ 354.77 USDT                    │
│ Total trade volume            │ 190962.319 USDT                │
│                               │                                │
│ Best Pair                     │ ETH/USDT 3.27%                 │
│ Worst Pair                    │ LTC/USDT -12.05%               │
│ Best trade                    │ XRP/USDT 18.51%                │
│ Worst trade                   │ XRP/USDT -7.80%                │
│ Best day                      │ 68.07 USDT                     │
│ Worst day                     │ -33.625 USDT                   │
│ Days win/draw/lose            │ 33 / 206 / 94                  │
│ Min/Max/Avg. Duration Winners │ 0d 05:00 / 2d 13:00 / 1d 04:28 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:40 / 1d 14:00 / 0d 09:18 │
│ Max Consecutive Wins / Loss   │ 5 / 14                         │
│ Rejected Entry signals        │ 2604                           │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 664.172 USDT                   │
│ Max balance                   │ 1050.805 USDT                  │
│ Max % of account underwater   │ 36.79%                         │
│ Absolute Drawdown (Account)   │ 36.79%                         │
│ Absolute Drawdown             │ 386.633 USDT                   │
│ Drawdown high                 │ 50.805 USDT                    │
│ Drawdown low                  │ -335.828 USDT                  │
│ Drawdown Start                │ 2022-02-08 13:00:00            │
│ Drawdown End                  │ 2022-09-30 20:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                               STRATEGY SUMMARY                                                               
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃           Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuStrategyV4 │    269 │        -0.41 │        -285.476 │       -28.55 │     14:09:00 │   68     0   201  25.3 │ 386.633 USDT  36.79% │
└────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
