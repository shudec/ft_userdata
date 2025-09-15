# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 71 / 0.2, Median: -0.72%, Total profit: 0.56%, Sortino: 0.14, Sharpe: 0.05, Calmar: 0.75, Drawdown: 0%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 3750  
**Timestamp:** 2025-09-15 11:37:44

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 3750,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 3750
```

## Hyperopt Output
```

Best result:

    98/100:    186 trades. 45/0/141 Wins/Draws/Losses. Avg profit  -0.12%. Median profit  -0.72%. Total profit -78.34022384 USDT (  -7.83%). Avg duration 6:18:00 min. Objective: 0.21500

{"params":{"lookback_period_for_stoploss":4,"stoploss_margin":0.997,"take_profit_multiplier":1.5,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ ETH/USDT │     11 │         0.44 │          15.717 │         1.57 │      4:07:00 │    5     0     6  45.5 │
│ LTC/USDT │     12 │         0.27 │          10.897 │         1.09 │      3:25:00 │    4     0     8  33.3 │
│ BNB/USDT │     19 │         0.01 │           0.497 │         0.05 │      4:19:00 │    5     0    14  26.3 │
│ BTC/USDT │     17 │        -0.02 │          -1.307 │        -0.13 │      6:58:00 │    4     0    13  23.5 │
│ XRP/USDT │     12 │         -0.5 │         -20.235 │        -2.02 │      4:21:00 │    2     0    10  16.7 │
│    TOTAL │     71 │         0.03 │           5.568 │         0.56 │      4:46:00 │   20     0    51  28.2 │
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
│     OTHER │      71 │         0.03 │           5.568 │         0.56 │      4:46:00 │   20     0    51  28.2 │
│     TOTAL │      71 │         0.03 │           5.568 │         0.56 │      4:46:00 │   20     0    51  28.2 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │    18 │         2.58 │         154.378 │        15.44 │      8:14:00 │   18     0     0   100 │
│        stop_loss │    11 │        -1.44 │         -53.347 │        -5.33 │      3:59:00 │    0     0    11     0 │
│      exit_signal │    42 │        -0.68 │         -95.463 │        -9.55 │      3:30:00 │    2     0    40   4.8 │
│            TOTAL │    71 │         0.03 │           5.568 │         0.56 │      4:46:00 │   20     0    51  28.2 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1.5R │     18 │         2.58 │         154.378 │        15.44 │      8:14:00 │   18     0     0   100 │
│           │        stop_loss │     11 │        -1.44 │         -53.347 │        -5.33 │      3:59:00 │    0     0    11     0 │
│           │      exit_signal │     42 │        -0.68 │         -95.463 │        -9.55 │      3:30:00 │    2     0    40   4.8 │
│     TOTAL │                  │     71 │         0.03 │           5.568 │         0.56 │      4:46:00 │   20     0    51  28.2 │
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
│ Final balance                 │ 1005.568 USDT                  │
│ Absolute profit               │ 5.568 USDT                     │
│ Total profit %                │ 0.56%                          │
│ CAGR %                        │ 0.56%                          │
│ Sortino                       │ 0.14                           │
│ Sharpe                        │ 0.05                           │
│ Calmar                        │ 0.75                           │
│ SQN                           │ 0.12                           │
│ Profit factor                 │ 1.04                           │
│ Expectancy (Ratio)            │ 0.08 (0.03)                    │
│ Avg. daily profit             │ 0.015 USDT                     │
│ Avg. stake amount             │ 333.784 USDT                   │
│ Total trade volume            │ 47497.861 USDT                 │
│                               │                                │
│ Best Pair                     │ ETH/USDT 1.57%                 │
│ Worst Pair                    │ XRP/USDT -2.02%                │
│ Best trade                    │ BTC/USDT 5.08%                 │
│ Worst trade                   │ BTC/USDT -3.05%                │
│ Best day                      │ 16.866 USDT                    │
│ Worst day                     │ -10.302 USDT                   │
│ Days win/draw/lose            │ 17 / 294 / 34                  │
│ Min/Max/Avg. Duration Winners │ 0d 00:50 / 1d 09:35 / 0d 08:58 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:15 / 1d 04:50 / 0d 03:08 │
│ Max Consecutive Wins / Loss   │ 2 / 9                          │
│ Rejected Entry signals        │ 12                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 982.301 USDT                   │
│ Max balance                   │ 1045.224 USDT                  │
│ Max % of account underwater   │ 3.87%                          │
│ Absolute drawdown             │ 40.481 USDT (3.87%)            │
│ Drawdown duration             │ 50 days 04:55:00               │
│ Profit at drawdown start      │ 45.224 USDT                    │
│ Profit at drawdown end        │ 4.743 USDT                     │
│ Drawdown start                │ 2022-08-05 02:05:00            │
│ Drawdown end                  │ 2022-09-24 07:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │     71 │         0.03 │           5.568 │         0.56 │      4:46:00 │   20     0    51  28.2 │ 40.481 USDT  3.87% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```
