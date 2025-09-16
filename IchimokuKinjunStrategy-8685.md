# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 8 / 0.02, Median: -0.31%, Total profit: 0.44%, Sortino: 0.15, Sharpe: 0.04, Calmar: 1.27, Drawdown: 0%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 8685  
**Timestamp:** 2025-09-16 10:19:55

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 8685,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 8685
```

## Hyperopt Output
```

Best result:

    98/100:     21 trades. 9/0/12 Wins/Draws/Losses. Avg profit   0.87%. Median profit  -0.31%. Total profit 60.71053331 USDT (   6.07%). Avg duration 17:37:00 min. Objective: -0.10943

{"params":{"rsi_entry_max":65,"rsi_entry_min":23,"volume_factor":1.269,"stoploss_margin":0.994,"lookback_period_for_stoploss":0,"take_profit_multiplier":1,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ BTC/USDT │      1 │         3.96 │          13.081 │         1.31 │ 1 day, 8:00:00 │    1     0     0   100 │
│ BNB/USDT │      3 │         0.53 │           5.283 │         0.53 │       14:00:00 │    1     0     2  33.3 │
│ LTC/USDT │      1 │        -0.84 │          -2.780 │        -0.28 │        1:00:00 │    0     0     1     0 │
│ XRP/USDT │      2 │         -0.7 │          -4.727 │        -0.47 │        3:30:00 │    0     0     2     0 │
│ ETH/USDT │      1 │        -1.94 │          -6.486 │        -0.65 │        1:00:00 │    0     0     1     0 │
│    TOTAL │      8 │         0.17 │           4.372 │         0.44 │       10:22:00 │    2     0     6  25.0 │
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
│     OTHER │       8 │         0.17 │           4.372 │         0.44 │     10:22:00 │    2     0     6  25.0 │
│     TOTAL │       8 │         0.17 │           4.372 │         0.44 │     10:22:00 │    2     0     6  25.0 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                               EXIT REASON STATS                                               
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ exit_signal │     8 │         0.17 │           4.372 │         0.44 │     10:22:00 │    2     0     6  25.0 │
│       TOTAL │     8 │         0.17 │           4.372 │         0.44 │     10:22:00 │    2     0     6  25.0 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                      MIXED TAG STATS                                                       
┏━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ exit_signal │      8 │         0.17 │           4.372 │         0.44 │     10:22:00 │    2     0     6  25.0 │
│     TOTAL │             │      8 │         0.17 │           4.372 │         0.44 │     10:22:00 │    2     0     6  25.0 │
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
│ Total/Daily Avg Trades        │ 8 / 0.02                       │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1004.372 USDT                  │
│ Absolute profit               │ 4.372 USDT                     │
│ Total profit %                │ 0.44%                          │
│ CAGR %                        │ 0.44%                          │
│ Sortino                       │ 0.15                           │
│ Sharpe                        │ 0.04                           │
│ Calmar                        │ 1.27                           │
│ SQN                           │ 0.22                           │
│ Profit factor                 │ 1.24                           │
│ Expectancy (Ratio)            │ 0.55 (0.18)                    │
│ Avg. daily profit             │ 0.012 USDT                     │
│ Avg. stake amount             │ 334.487 USDT                   │
│ Total trade volume            │ 5366.894 USDT                  │
│                               │                                │
│ Best Pair                     │ BTC/USDT 1.31%                 │
│ Worst Pair                    │ ETH/USDT -0.65%                │
│ Best trade                    │ BTC/USDT 3.96%                 │
│ Worst trade                   │ ETH/USDT -1.94%                │
│ Best day                      │ 13.081 USDT                    │
│ Worst day                     │ -8.995 USDT                    │
│ Days win/draw/lose            │ 2 / 266 / 5                    │
│ Min/Max/Avg. Duration Winners │ 1d 08:00 / 1d 08:00 / 1d 08:00 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 0d 09:00 / 0d 03:10 │
│ Max Consecutive Wins / Loss   │ 2 / 6                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 1004.372 USDT                  │
│ Max balance                   │ 1022.895 USDT                  │
│ Max % of account underwater   │ 1.81%                          │
│ Absolute drawdown             │ 18.524 USDT (1.81%)            │
│ Drawdown duration             │ 223 days 10:00:00              │
│ Profit at drawdown start      │ 22.895 USDT                    │
│ Profit at drawdown end        │ 4.372 USDT                     │
│ Drawdown start                │ 2022-03-29 00:00:00            │
│ Drawdown end                  │ 2022-11-07 10:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │      8 │         0.17 │           4.372 │         0.44 │     10:22:00 │    2     0     6  25.0 │ 18.524 USDT  1.81% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```
