# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 71 / 0.2, Median: -0.71%, Total profit: 0.17%, Sortino: 0.05, Sharpe: 0.02, Calmar: 0.24, Drawdown: 0%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 4983  
**Timestamp:** 2025-09-15 14:09:47

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 4983,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 4983
```

## Hyperopt Output
```

Best result:

*   22/100:    186 trades. 45/0/141 Wins/Draws/Losses. Avg profit  -0.11%. Median profit  -0.71%. Total profit -73.11592968 USDT (  -7.31%). Avg duration 6:08:00 min. Objective: 0.19934

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
│ ETH/USDT │     11 │         0.43 │          15.331 │         1.53 │      4:03:00 │    5     0     6  45.5 │
│ LTC/USDT │     12 │         0.25 │          10.016 │          1.0 │      3:23:00 │    4     0     8  33.3 │
│ BNB/USDT │     19 │        -0.01 │          -1.134 │        -0.11 │      3:49:00 │    5     0    14  26.3 │
│ BTC/USDT │     17 │        -0.02 │          -1.543 │        -0.15 │      6:54:00 │    4     0    13  23.5 │
│ XRP/USDT │     12 │        -0.52 │         -20.927 │        -2.09 │      3:30:00 │    2     0    10  16.7 │
│    TOTAL │     71 │         0.01 │           1.744 │         0.17 │      4:28:00 │   20     0    51  28.2 │
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
│     OTHER │      71 │         0.01 │           1.744 │         0.17 │      4:28:00 │   20     0    51  28.2 │
│     TOTAL │      71 │         0.01 │           1.744 │         0.17 │      4:28:00 │   20     0    51  28.2 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │    18 │         2.45 │         146.400 │        14.64 │      7:05:00 │   18     0     0   100 │
│        stop_loss │    12 │        -1.29 │         -51.879 │        -5.19 │      3:58:00 │    0     0    12     0 │
│      exit_signal │    41 │        -0.68 │         -92.776 │        -9.28 │      3:28:00 │    2     0    39   4.9 │
│            TOTAL │    71 │         0.01 │           1.744 │         0.17 │      4:28:00 │   20     0    51  28.2 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1.5R │     18 │         2.45 │         146.400 │        14.64 │      7:05:00 │   18     0     0   100 │
│           │        stop_loss │     12 │        -1.29 │         -51.879 │        -5.19 │      3:58:00 │    0     0    12     0 │
│           │      exit_signal │     41 │        -0.68 │         -92.776 │        -9.28 │      3:28:00 │    2     0    39   4.9 │
│     TOTAL │                  │     71 │         0.01 │           1.744 │         0.17 │      4:28:00 │   20     0    51  28.2 │
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
│ Total/Daily Avg Trades        │ 71 / 0.2                       │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1001.744 USDT                  │
│ Absolute profit               │ 1.744 USDT                     │
│ Total profit %                │ 0.17%                          │
│ CAGR %                        │ 0.17%                          │
│ Sortino                       │ 0.05                           │
│ Sharpe                        │ 0.02                           │
│ Calmar                        │ 0.24                           │
│ SQN                           │ 0.04                           │
│ Profit factor                 │ 1.01                           │
│ Expectancy (Ratio)            │ 0.02 (0.01)                    │
│ Avg. daily profit             │ 0.005 USDT                     │
│ Avg. stake amount             │ 333.011 USDT                   │
│ Total trade volume            │ 47384.031 USDT                 │
│                               │                                │
│ Best Pair                     │ ETH/USDT 1.53%                 │
│ Worst Pair                    │ XRP/USDT -2.09%                │
│ Best trade                    │ BTC/USDT 5.08%                 │
│ Worst trade                   │ BTC/USDT -2.75%                │
│ Best day                      │ 16.846 USDT                    │
│ Worst day                     │ -10.767 USDT                   │
│ Days win/draw/lose            │ 17 / 295 / 33                  │
│ Min/Max/Avg. Duration Winners │ 0d 00:50 / 1d 09:20 / 0d 07:56 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:15 / 1d 04:40 / 0d 03:07 │
│ Max Consecutive Wins / Loss   │ 2 / 9                          │
│ Rejected Entry signals        │ 12                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 982.249 USDT                   │
│ Max balance                   │ 1041.112 USDT                  │
│ Max % of account underwater   │ 3.78%                          │
│ Absolute drawdown             │ 39.368 USDT (3.78%)            │
│ Drawdown duration             │ 144 days 06:55:00              │
│ Profit at drawdown start      │ 41.112 USDT                    │
│ Profit at drawdown end        │ 1.744 USDT                     │
│ Drawdown start                │ 2022-08-05 02:05:00            │
│ Drawdown end                  │ 2022-12-27 09:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │     71 │         0.01 │           1.744 │         0.17 │      4:28:00 │   20     0    51  28.2 │ 39.368 USDT  3.78% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```
