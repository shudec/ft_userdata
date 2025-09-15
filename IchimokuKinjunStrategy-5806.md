# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 110 / 0.3, Median: -0.72%, Total profit: -3.7%, Sortino: -0.6, Sharpe: -0.33, Calmar: -2.28, Drawdown: 0%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 5806  
**Timestamp:** 2025-09-15 16:17:50

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 5806,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 5806
```

## Hyperopt Output
```

Best result:

*   16/100:    246 trades. 58/0/188 Wins/Draws/Losses. Avg profit  -0.19%. Median profit  -0.72%. Total profit -147.89014856 USDT ( -14.79%). Avg duration 6:10:00 min. Objective: 0.42579

{"params":{"lookback_period_for_stoploss":3,"stoploss_margin":0.998,"take_profit_multiplier":1.5,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ ETH/USDT │     13 │         0.48 │          20.586 │         2.06 │      4:09:00 │    6     0     7  46.2 │
│ LTC/USDT │     26 │        -0.02 │          -0.886 │        -0.09 │      5:34:00 │   10     0    16  38.5 │
│ BNB/USDT │     27 │        -0.02 │          -2.455 │        -0.25 │      4:08:00 │    9     0    18  33.3 │
│ BTC/USDT │     23 │        -0.18 │         -14.088 │        -1.41 │      6:03:00 │    5     0    18  21.7 │
│ XRP/USDT │     21 │        -0.56 │         -40.137 │        -4.01 │      4:02:00 │    5     0    16  23.8 │
│    TOTAL │    110 │         -0.1 │         -36.979 │         -3.7 │      4:51:00 │   35     0    75  31.8 │
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
│     OTHER │     110 │         -0.1 │         -36.979 │         -3.7 │      4:51:00 │   35     0    75  31.8 │
│     TOTAL │     110 │         -0.1 │         -36.979 │         -3.7 │      4:51:00 │   35     0    75  31.8 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │    31 │         2.26 │         232.679 │        23.27 │      6:05:00 │   31     0     0   100 │
│        stop_loss │    21 │        -1.44 │        -100.942 │       -10.09 │      3:22:00 │    0     0    21     0 │
│      exit_signal │    58 │        -0.87 │        -168.716 │       -16.87 │      4:44:00 │    4     0    54   6.9 │
│            TOTAL │   110 │         -0.1 │         -36.979 │         -3.7 │      4:51:00 │   35     0    75  31.8 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1.5R │     31 │         2.26 │         232.679 │        23.27 │      6:05:00 │   31     0     0   100 │
│           │        stop_loss │     21 │        -1.44 │        -100.942 │       -10.09 │      3:22:00 │    0     0    21     0 │
│           │      exit_signal │     58 │        -0.87 │        -168.716 │       -16.87 │      4:44:00 │    4     0    54   6.9 │
│     TOTAL │                  │    110 │         -0.1 │         -36.979 │         -3.7 │      4:51:00 │   35     0    75  31.8 │
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
│ Final balance                 │ 963.021 USDT                   │
│ Absolute profit               │ -36.979 USDT                   │
│ Total profit %                │ -3.70%                         │
│ CAGR %                        │ -3.71%                         │
│ Sortino                       │ -0.60                          │
│ Sharpe                        │ -0.33                          │
│ Calmar                        │ -2.28                          │
│ SQN                           │ -0.59                          │
│ Profit factor                 │ 0.87                           │
│ Expectancy (Ratio)            │ -0.34 (-0.09)                  │
│ Avg. daily profit             │ -0.102 USDT                    │
│ Avg. stake amount             │ 332.489 USDT                   │
│ Total trade volume            │ 73256.861 USDT                 │
│                               │                                │
│ Best Pair                     │ ETH/USDT 2.06%                 │
│ Worst Pair                    │ XRP/USDT -4.01%                │
│ Best trade                    │ BTC/USDT 5.08%                 │
│ Worst trade                   │ BNB/USDT -7.54%                │
│ Best day                      │ 20.159 USDT                    │
│ Worst day                     │ -24.953 USDT                   │
│ Days win/draw/lose            │ 28 / 276 / 49                  │
│ Min/Max/Avg. Duration Winners │ 0d 00:25 / 1d 09:20 / 0d 07:58 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:15 / 1d 04:40 / 0d 03:25 │
│ Max Consecutive Wins / Loss   │ 3 / 9                          │
│ Rejected Entry signals        │ 24                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 959.004 USDT                   │
│ Max balance                   │ 1048.26 USDT                   │
│ Max % of account underwater   │ 8.51%                          │
│ Absolute drawdown             │ 89.256 USDT (8.51%)            │
│ Drawdown duration             │ 86 days 20:15:00               │
│ Profit at drawdown start      │ 48.26 USDT                     │
│ Profit at drawdown end        │ -40.996 USDT                   │
│ Drawdown start                │ 2022-09-01 17:30:00            │
│ Drawdown end                  │ 2022-11-27 13:45:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │    110 │        -0.10 │         -36.979 │         -3.7 │      4:51:00 │   35     0    75  31.8 │ 89.256 USDT  8.51% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```
