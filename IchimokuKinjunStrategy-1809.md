# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 19 / 0.05, Median: -0.95%, Total profit: 1.74%, Sortino: 0.3, Sharpe: 0.12, Calmar: 2.87, Drawdown: 3.18%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 1809  
**Timestamp:** 2025-09-15 21:37:48

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 1809,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 1809
```

## Hyperopt Output
```

Best result:

*    8/100:     64 trades. 17/0/47 Wins/Draws/Losses. Avg profit  -0.68%. Median profit  -0.95%. Total profit -141.63336258 USDT ( -14.16%). Avg duration 13:39:00 min. Objective: 0.22389

{"params":{"stoploss_margin":0.998,"lookback_period_for_stoploss":0,"take_profit_multiplier":1,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ BTC/USDT │      6 │         0.83 │          16.475 │         1.65 │     21:00:00 │    3     0     3  50.0 │
│ LTC/USDT │      2 │         0.43 │           3.049 │          0.3 │      5:30:00 │    1     0     1  50.0 │
│ ETH/USDT │      2 │         0.32 │           1.969 │          0.2 │     16:00:00 │    1     0     1  50.0 │
│ BNB/USDT │      5 │        -0.09 │          -1.787 │        -0.18 │      9:24:00 │    1     0     4  20.0 │
│ XRP/USDT │      4 │        -0.16 │          -2.321 │        -0.23 │      9:15:00 │    1     0     3  25.0 │
│    TOTAL │     19 │         0.29 │          17.385 │         1.74 │     13:19:00 │    7     0    12  36.8 │
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
│     OTHER │      19 │         0.29 │          17.385 │         1.74 │     13:19:00 │    7     0    12  36.8 │
│     TOTAL │      19 │         0.29 │          17.385 │         1.74 │     13:19:00 │    7     0    12  36.8 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                               EXIT REASON STATS                                               
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ exit_signal │    19 │         0.29 │          17.385 │         1.74 │     13:19:00 │    7     0    12  36.8 │
│       TOTAL │    19 │         0.29 │          17.385 │         1.74 │     13:19:00 │    7     0    12  36.8 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                      MIXED TAG STATS                                                       
┏━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ exit_signal │     19 │         0.29 │          17.385 │         1.74 │     13:19:00 │    7     0    12  36.8 │
│     TOTAL │             │     19 │         0.29 │          17.385 │         1.74 │     13:19:00 │    7     0    12  36.8 │
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
│ Total/Daily Avg Trades        │ 19 / 0.05                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1017.385 USDT                  │
│ Absolute profit               │ 17.385 USDT                    │
│ Total profit %                │ 1.74%                          │
│ CAGR %                        │ 1.74%                          │
│ Sortino                       │ 0.30                           │
│ Sharpe                        │ 0.12                           │
│ Calmar                        │ 2.87                           │
│ SQN                           │ 0.49                           │
│ Profit factor                 │ 1.35                           │
│ Expectancy (Ratio)            │ 0.91 (0.22)                    │
│ Avg. daily profit             │ 0.048 USDT                     │
│ Avg. stake amount             │ 340.423 USDT                   │
│ Total trade volume            │ 12979.401 USDT                 │
│                               │                                │
│ Best Pair                     │ BTC/USDT 1.65%                 │
│ Worst Pair                    │ XRP/USDT -0.23%                │
│ Best trade                    │ BTC/USDT 6.16%                 │
│ Worst trade                   │ BTC/USDT -3.79%                │
│ Best day                      │ 21.618 USDT                    │
│ Worst day                     │ -12.935 USDT                   │
│ Days win/draw/lose            │ 6 / 257 / 10                   │
│ Min/Max/Avg. Duration Winners │ 0d 04:00 / 2d 08:00 / 1d 03:34 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 1d 05:00 / 0d 05:00 │
│ Max Consecutive Wins / Loss   │ 3 / 6                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 1008.537 USDT                  │
│ Max balance                   │ 1050.75 USDT                   │
│ Max % of account underwater   │ 3.18%                          │
│ Absolute Drawdown (Account)   │ 3.18%                          │
│ Absolute Drawdown             │ 33.366 USDT                    │
│ Drawdown high                 │ 50.75 USDT                     │
│ Drawdown low                  │ 17.385 USDT                    │
│ Drawdown Start                │ 2022-07-20 20:00:00            │
│ Drawdown End                  │ 2022-11-07 10:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │     19 │         0.29 │          17.385 │         1.74 │     13:19:00 │    7     0    12  36.8 │ 33.366 USDT  3.18% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```
