# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 69 / 0.19, Median: -0.73%, Total profit: 1.83%, Sortino: 0.43, Sharpe: 0.13, Calmar: 2.02, Drawdown: 4.76%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 9305  
**Timestamp:** 2025-09-15 22:39:36

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 9305,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 9305
```

## Hyperopt Output
```

Best result:

*   12/100:    176 trades. 36/0/140 Wins/Draws/Losses. Avg profit  -0.34%. Median profit  -0.73%. Total profit -193.06278244 USDT ( -19.31%). Avg duration 10:57:00 min. Objective: 0.38254

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
│ LTC/USDT │     11 │         0.76 │          27.592 │         2.76 │     12:27:00 │    3     0     8  27.3 │
│ ETH/USDT │     11 │         0.38 │          13.293 │         1.33 │     12:00:00 │    4     0     7  36.4 │
│ BNB/USDT │     19 │         0.08 │           4.951 │          0.5 │     12:03:00 │    5     0    14  26.3 │
│ BTC/USDT │     17 │        -0.09 │          -6.101 │        -0.61 │     10:14:00 │    4     0    13  23.5 │
│ XRP/USDT │     11 │        -0.58 │         -21.388 │        -2.14 │      7:33:00 │    2     0     9  18.2 │
│    TOTAL │     69 │         0.09 │          18.348 │         1.83 │     10:57:00 │   18     0    51  26.1 │
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
│     OTHER │      69 │         0.09 │          18.348 │         1.83 │     10:57:00 │   18     0    51  26.1 │
│     TOTAL │      69 │         0.09 │          18.348 │         1.83 │     10:57:00 │   18     0    51  26.1 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                               EXIT REASON STATS                                               
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ exit_signal │    69 │         0.09 │          18.348 │         1.83 │     10:57:00 │   18     0    51  26.1 │
│       TOTAL │    69 │         0.09 │          18.348 │         1.83 │     10:57:00 │   18     0    51  26.1 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                      MIXED TAG STATS                                                       
┏━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ exit_signal │     69 │         0.09 │          18.348 │         1.83 │     10:57:00 │   18     0    51  26.1 │
│     TOTAL │             │     69 │         0.09 │          18.348 │         1.83 │     10:57:00 │   18     0    51  26.1 │
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
│ Total/Daily Avg Trades        │ 69 / 0.19                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1018.348 USDT                  │
│ Absolute profit               │ 18.348 USDT                    │
│ Total profit %                │ 1.83%                          │
│ CAGR %                        │ 1.84%                          │
│ Sortino                       │ 0.43                           │
│ Sharpe                        │ 0.13                           │
│ Calmar                        │ 2.02                           │
│ SQN                           │ 0.31                           │
│ Profit factor                 │ 1.12                           │
│ Expectancy (Ratio)            │ 0.27 (0.09)                    │
│ Avg. daily profit             │ 0.05 USDT                      │
│ Avg. stake amount             │ 333.356 USDT                   │
│ Total trade volume            │ 46113.63 USDT                  │
│                               │                                │
│ Best Pair                     │ LTC/USDT 2.76%                 │
│ Worst Pair                    │ XRP/USDT -2.14%                │
│ Best trade                    │ LTC/USDT 10.63%                │
│ Worst trade                   │ BTC/USDT -3.79%                │
│ Best day                      │ 34.976 USDT                    │
│ Worst day                     │ -12.725 USDT                   │
│ Days win/draw/lose            │ 12 / 299 / 34                  │
│ Min/Max/Avg. Duration Winners │ 0d 04:00 / 2d 08:00 / 1d 06:50 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 1d 05:00 / 0d 03:55 │
│ Max Consecutive Wins / Loss   │ 2 / 10                         │
│ Rejected Entry signals        │ 12                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 982.426 USDT                   │
│ Max balance                   │ 1043.773 USDT                  │
│ Max % of account underwater   │ 4.76%                          │
│ Absolute Drawdown (Account)   │ 4.76%                          │
│ Absolute Drawdown             │ 49.658 USDT                    │
│ Drawdown high                 │ 43.773 USDT                    │
│ Drawdown low                  │ -5.885 USDT                    │
│ Drawdown Start                │ 2022-08-06 09:00:00            │
│ Drawdown End                  │ 2022-10-05 08:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │     69 │         0.09 │          18.348 │         1.83 │     10:57:00 │   18     0    51  26.1 │ 49.658 USDT  4.76% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```
