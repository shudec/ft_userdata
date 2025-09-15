# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 110 / 0.3, Median: -0.72%, Total profit: 1.79%, Sortino: 0.25, Sharpe: 0.11, Calmar: 1.12, Drawdown: 0%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 9109  
**Timestamp:** 2025-09-15 16:22:28

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 9109,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 9109
```

## Hyperopt Output
```

Best result:

*   16/100:    246 trades. 50/0/196 Wins/Draws/Losses. Avg profit  -0.37%. Median profit  -0.72%. Total profit -271.00937373 USDT ( -27.10%). Avg duration 8:36:00 min. Objective: 0.70740

{"params":{"lookback_period_for_stoploss":10,"stoploss_margin":0.993,"take_profit_multiplier":3,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ ETH/USDT │     13 │         1.13 │          48.057 │         4.81 │      8:48:00 │    5     0     8  38.5 │
│ BNB/USDT │     27 │          0.3 │          26.396 │         2.64 │     11:06:00 │    8     0    19  29.6 │
│ LTC/USDT │     26 │         0.17 │          15.485 │         1.55 │     10:21:00 │    9     0    17  34.6 │
│ BTC/USDT │     23 │        -0.01 │          -2.894 │        -0.29 │      7:46:00 │    5     0    18  21.7 │
│ XRP/USDT │     21 │        -0.95 │         -69.155 │        -6.92 │      9:30:00 │    4     0    17  19.0 │
│    TOTAL │    110 │         0.06 │          17.889 │         1.79 │      9:39:00 │   31     0    79  28.2 │
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
│     OTHER │     110 │         0.06 │          17.889 │         1.79 │      9:39:00 │   31     0    79  28.2 │
│     TOTAL │     110 │         0.06 │          17.889 │         1.79 │      9:39:00 │   31     0    79  28.2 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │    11 │         6.52 │         244.334 │        24.43 │     18:51:00 │   11     0     0   100 │
│      stop_loss │     7 │        -2.53 │         -61.730 │        -6.17 │     16:21:00 │    0     0     7     0 │
│    exit_signal │    92 │        -0.51 │        -164.715 │       -16.47 │      8:03:00 │   20     0    72  21.7 │
│          TOTAL │   110 │         0.06 │          17.889 │         1.79 │      9:39:00 │   31     0    79  28.2 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_3R │     11 │         6.52 │         244.334 │        24.43 │     18:51:00 │   11     0     0   100 │
│           │      stop_loss │      7 │        -2.53 │         -61.730 │        -6.17 │     16:21:00 │    0     0     7     0 │
│           │    exit_signal │     92 │        -0.51 │        -164.715 │       -16.47 │      8:03:00 │   20     0    72  21.7 │
│     TOTAL │                │    110 │         0.06 │          17.889 │         1.79 │      9:39:00 │   31     0    79  28.2 │
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
│ Total/Daily Avg Trades        │ 110 / 0.3                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1017.889 USDT                  │
│ Absolute profit               │ 17.889 USDT                    │
│ Total profit %                │ 1.79%                          │
│ CAGR %                        │ 1.79%                          │
│ Sortino                       │ 0.25                           │
│ Sharpe                        │ 0.11                           │
│ Calmar                        │ 1.12                           │
│ SQN                           │ 0.19                           │
│ Profit factor                 │ 1.06                           │
│ Expectancy (Ratio)            │ 0.16 (0.04)                    │
│ Avg. daily profit             │ 0.049 USDT                     │
│ Avg. stake amount             │ 345.71 USDT                    │
│ Total trade volume            │ 76226.281 USDT                 │
│                               │                                │
│ Best Pair                     │ ETH/USDT 4.81%                 │
│ Worst Pair                    │ XRP/USDT -6.92%                │
│ Best trade                    │ LTC/USDT 8.27%                 │
│ Worst trade                   │ BNB/USDT -7.54%                │
│ Best day                      │ 49.21 USDT                     │
│ Worst day                     │ -26.737 USDT                   │
│ Days win/draw/lose            │ 23 / 277 / 53                  │
│ Min/Max/Avg. Duration Winners │ 0d 04:00 / 1d 19:00 / 0d 21:39 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:20 / 2d 13:45 / 0d 04:57 │
│ Max Consecutive Wins / Loss   │ 3 / 9                          │
│ Rejected Entry signals        │ 24                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 991.888 USDT                   │
│ Max balance                   │ 1110.71 USDT                   │
│ Max % of account underwater   │ 8.36%                          │
│ Absolute drawdown             │ 92.821 USDT (8.36%)            │
│ Drawdown duration             │ 116 days 15:20:00              │
│ Profit at drawdown start      │ 110.71 USDT                    │
│ Profit at drawdown end        │ 17.889 USDT                    │
│ Drawdown start                │ 2022-09-02 12:40:00            │
│ Drawdown end                  │ 2022-12-28 04:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │    110 │         0.06 │          17.889 │         1.79 │      9:39:00 │   31     0    79  28.2 │ 92.821 USDT  8.36% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```
