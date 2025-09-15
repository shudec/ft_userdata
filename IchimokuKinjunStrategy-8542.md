# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 110 / 0.3, Median: -0.71%, Total profit: -0.66%, Sortino: -0.1, Sharpe: -0.06, Calmar: -0.48, Drawdown: 0%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 8542  
**Timestamp:** 2025-09-15 16:14:43

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 8542,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 8542
```

## Hyperopt Output
```

Best result:

    50/100:    246 trades. 55/0/191 Wins/Draws/Losses. Avg profit  -0.18%. Median profit  -0.71%. Total profit -140.03113092 USDT ( -14.00%). Avg duration 5:59:00 min. Objective: 0.41125

{"params":{"lookback_period_for_stoploss":3,"stoploss_margin":0.997,"take_profit_multiplier":1.5,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ ETH/USDT │     13 │         0.51 │          21.534 │         2.15 │      4:18:00 │    6     0     7  46.2 │
│ LTC/USDT │     26 │         0.06 │           5.474 │         0.55 │      5:27:00 │   10     0    16  38.5 │
│ BNB/USDT │     27 │         0.05 │           3.192 │         0.32 │      4:19:00 │    9     0    18  33.3 │
│ BTC/USDT │     23 │        -0.13 │         -10.267 │        -1.03 │      6:05:00 │    5     0    18  21.7 │
│ XRP/USDT │     21 │        -0.37 │         -26.521 │        -2.65 │      3:54:00 │    5     0    16  23.8 │
│    TOTAL │    110 │        -0.01 │          -6.589 │        -0.66 │      4:53:00 │   35     0    75  31.8 │
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
│     OTHER │     110 │        -0.01 │          -6.589 │        -0.66 │      4:53:00 │   35     0    75  31.8 │
│     TOTAL │     110 │        -0.01 │          -6.589 │        -0.66 │      4:53:00 │   35     0    75  31.8 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │    31 │         2.41 │         250.996 │         25.1 │      6:55:00 │   31     0     0   100 │
│        stop_loss │    15 │        -1.45 │         -73.743 │        -7.37 │      3:16:00 │    0     0    15     0 │
│      exit_signal │    64 │        -0.85 │        -183.841 │       -18.38 │      4:16:00 │    4     0    60   6.2 │
│            TOTAL │   110 │        -0.01 │          -6.589 │        -0.66 │      4:53:00 │   35     0    75  31.8 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1.5R │     31 │         2.41 │         250.996 │         25.1 │      6:55:00 │   31     0     0   100 │
│           │        stop_loss │     15 │        -1.45 │         -73.743 │        -7.37 │      3:16:00 │    0     0    15     0 │
│           │      exit_signal │     64 │        -0.85 │        -183.841 │       -18.38 │      4:16:00 │    4     0    60   6.2 │
│     TOTAL │                  │    110 │        -0.01 │          -6.589 │        -0.66 │      4:53:00 │   35     0    75  31.8 │
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
│ Total/Daily Avg Trades        │ 110 / 0.3                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 993.411 USDT                   │
│ Absolute profit               │ -6.589 USDT                    │
│ Total profit %                │ -0.66%                         │
│ CAGR %                        │ -0.66%                         │
│ Sortino                       │ -0.10                          │
│ Sharpe                        │ -0.06                          │
│ Calmar                        │ -0.48                          │
│ SQN                           │ -0.10                          │
│ Profit factor                 │ 0.98                           │
│ Expectancy (Ratio)            │ -0.06 (-0.02)                  │
│ Avg. daily profit             │ -0.018 USDT                    │
│ Avg. stake amount             │ 337.016 USDT                   │
│ Total trade volume            │ 74285.254 USDT                 │
│                               │                                │
│ Best Pair                     │ ETH/USDT 2.15%                 │
│ Worst Pair                    │ XRP/USDT -2.65%                │
│ Best trade                    │ BTC/USDT 5.08%                 │
│ Worst trade                   │ BNB/USDT -7.54%                │
│ Best day                      │ 22.346 USDT                    │
│ Worst day                     │ -25.576 USDT                   │
│ Days win/draw/lose            │ 27 / 276 / 50                  │
│ Min/Max/Avg. Duration Winners │ 0d 00:25 / 1d 09:35 / 0d 08:14 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:15 / 1d 04:40 / 0d 03:18 │
│ Max Consecutive Wins / Loss   │ 3 / 8                          │
│ Rejected Entry signals        │ 24                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 983.48 USDT                    │
│ Max balance                   │ 1066.274 USDT                  │
│ Max % of account underwater   │ 7.26%                          │
│ Absolute drawdown             │ 77.429 USDT (7.26%)            │
│ Drawdown duration             │ 111 days 04:55:00              │
│ Profit at drawdown start      │ 66.274 USDT                    │
│ Profit at drawdown end        │ -11.155 USDT                   │
│ Drawdown start                │ 2022-08-08 08:50:00            │
│ Drawdown end                  │ 2022-11-27 13:45:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │    110 │        -0.01 │          -6.589 │        -0.66 │      4:53:00 │   35     0    75  31.8 │ 77.429 USDT  7.26% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```
