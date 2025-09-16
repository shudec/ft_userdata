# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 17 / 0.05, Median: -0.59%, Total profit: 1.51%, Sortino: 0.26, Sharpe: 0.1, Calmar: 2.39, Drawdown: 0%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 4770  
**Timestamp:** 2025-09-16 10:12:43

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 4770,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 4770
```

## Hyperopt Output
```

Best result:

   100/100:     32 trades. 11/0/21 Wins/Draws/Losses. Avg profit   0.53%. Median profit  -0.59%. Total profit 55.88030388 USDT (   5.59%). Avg duration 14:19:00 min. Objective: -0.10805

{"params":{"rsi_entry_max":66,"rsi_entry_min":11,"volume_factor":1.113,"stoploss_margin":0.99,"lookback_period_for_stoploss":0,"take_profit_multiplier":1,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy IchimokuKinjunStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20221231
```

## Backtesting Output
```
Result for strategy IchimokuKinjunStrategy
                                              BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT │      5 │         1.21 │          20.024 │          2.0 │ 1 day, 0:24:00 │    3     0     2  60.0 │
│ ETH/USDT │      2 │         0.32 │           1.981 │          0.2 │       16:00:00 │    1     0     1  50.0 │
│ BNB/USDT │      5 │        -0.09 │          -1.765 │        -0.18 │        9:24:00 │    1     0     4  20.0 │
│ XRP/USDT │      4 │        -0.16 │          -2.290 │        -0.23 │        9:15:00 │    1     0     3  25.0 │
│ LTC/USDT │      1 │        -0.84 │          -2.810 │        -0.28 │        1:00:00 │    0     0     1     0 │
│    TOTAL │     17 │         0.28 │          15.141 │         1.51 │       14:04:00 │    6     0    11  35.3 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
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
│     OTHER │      17 │         0.28 │          15.141 │         1.51 │     14:04:00 │    6     0    11  35.3 │
│     TOTAL │      17 │         0.28 │          15.141 │         1.51 │     14:04:00 │    6     0    11  35.3 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                               EXIT REASON STATS                                               
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ exit_signal │    17 │         0.28 │          15.141 │         1.51 │     14:04:00 │    6     0    11  35.3 │
│       TOTAL │    17 │         0.28 │          15.141 │         1.51 │     14:04:00 │    6     0    11  35.3 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                      MIXED TAG STATS                                                       
┏━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ exit_signal │     17 │         0.28 │          15.141 │         1.51 │     14:04:00 │    6     0    11  35.3 │
│     TOTAL │             │     17 │         0.28 │          15.141 │         1.51 │     14:04:00 │    6     0    11  35.3 │
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
│ Total/Daily Avg Trades        │ 17 / 0.05                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1015.141 USDT                  │
│ Absolute profit               │ 15.141 USDT                    │
│ Total profit %                │ 1.51%                          │
│ CAGR %                        │ 1.52%                          │
│ Sortino                       │ 0.26                           │
│ Sharpe                        │ 0.10                           │
│ Calmar                        │ 2.39                           │
│ SQN                           │ 0.44                           │
│ Profit factor                 │ 1.33                           │
│ Expectancy (Ratio)            │ 0.89 (0.21)                    │
│ Avg. daily profit             │ 0.042 USDT                     │
│ Avg. stake amount             │ 339.224 USDT                   │
│ Total trade volume            │ 11571.876 USDT                 │
│                               │                                │
│ Best Pair                     │ BTC/USDT 2.00%                 │
│ Worst Pair                    │ LTC/USDT -0.28%                │
│ Best trade                    │ BTC/USDT 6.16%                 │
│ Worst trade                   │ BTC/USDT -3.79%                │
│ Best day                      │ 21.618 USDT                    │
│ Worst day                     │ -12.902 USDT                   │
│ Days win/draw/lose            │ 5 / 258 / 10                   │
│ Min/Max/Avg. Duration Winners │ 0d 04:00 / 2d 08:00 / 1d 06:30 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 1d 05:00 / 0d 05:05 │
│ Max Consecutive Wins / Loss   │ 3 / 6                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 1008.537 USDT                  │
│ Max balance                   │ 1050.012 USDT                  │
│ Max % of account underwater   │ 3.32%                          │
│ Absolute drawdown             │ 34.872 USDT (3.32%)            │
│ Drawdown duration             │ 121 days 21:00:00              │
│ Profit at drawdown start      │ 50.012 USDT                    │
│ Profit at drawdown end        │ 15.141 USDT                    │
│ Drawdown start                │ 2022-07-08 13:00:00            │
│ Drawdown end                  │ 2022-11-07 10:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │     17 │         0.28 │          15.141 │         1.51 │     14:04:00 │    6     0    11  35.3 │ 34.872 USDT  3.32% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```
