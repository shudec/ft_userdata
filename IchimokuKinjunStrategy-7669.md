# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 8 / 0.02, Median: -0.63%, Total profit: -0.57%, Sortino: -0.08, Sharpe: -0.04, Calmar: -1.07, Drawdown: 0%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 7669  
**Timestamp:** 2025-09-16 11:07:31

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 7669,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 7669
```

## Hyperopt Output
```

Best result:

*    9/100:     27 trades. 10/0/17 Wins/Draws/Losses. Avg profit   0.40%. Median profit  -0.63%. Total profit 34.45266668 USDT (   3.45%). Avg duration 15:47:00 min. Objective: -0.06066

{"params":{"rsi_entry_max":69,"rsi_entry_min":10,"volume_factor":1.305,"stoploss_margin":1.0,"lookback_period_for_stoploss":0,"take_profit_multiplier":1,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ BNB/USDT │      3 │         0.53 │           5.283 │         0.53 │       14:00:00 │    1     0     2  33.3 │
│ BTC/USDT │      2 │         0.09 │           0.381 │         0.04 │ 1 day, 6:30:00 │    1     0     1  50.0 │
│ XRP/USDT │      1 │        -0.66 │          -2.218 │        -0.22 │        1:00:00 │    0     0     1     0 │
│ LTC/USDT │      1 │        -0.84 │          -2.752 │        -0.28 │        1:00:00 │    0     0     1     0 │
│ ETH/USDT │      1 │        -1.94 │          -6.419 │        -0.64 │        1:00:00 │    0     0     1     0 │
│    TOTAL │      8 │        -0.21 │          -5.724 │        -0.57 │       13:15:00 │    2     0     6  25.0 │
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
│     OTHER │       8 │        -0.21 │          -5.724 │        -0.57 │     13:15:00 │    2     0     6  25.0 │
│     TOTAL │       8 │        -0.21 │          -5.724 │        -0.57 │     13:15:00 │    2     0     6  25.0 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                               EXIT REASON STATS                                               
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ exit_signal │     8 │        -0.21 │          -5.724 │        -0.57 │     13:15:00 │    2     0     6  25.0 │
│       TOTAL │     8 │        -0.21 │          -5.724 │        -0.57 │     13:15:00 │    2     0     6  25.0 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                      MIXED TAG STATS                                                       
┏━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ exit_signal │      8 │        -0.21 │          -5.724 │        -0.57 │     13:15:00 │    2     0     6  25.0 │
│     TOTAL │             │      8 │        -0.21 │          -5.724 │        -0.57 │     13:15:00 │    2     0     6  25.0 │
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
│ Final balance                 │ 994.276 USDT                   │
│ Absolute profit               │ -5.724 USDT                    │
│ Total profit %                │ -0.57%                         │
│ CAGR %                        │ -0.57%                         │
│ Sortino                       │ -0.08                          │
│ Sharpe                        │ -0.04                          │
│ Calmar                        │ -1.07                          │
│ SQN                           │ -0.24                          │
│ Profit factor                 │ 0.80                           │
│ Expectancy (Ratio)            │ -0.72 (-0.15)                  │
│ Avg. daily profit             │ -0.016 USDT                    │
│ Avg. stake amount             │ 333.624 USDT                   │
│ Total trade volume            │ 5342.943 USDT                  │
│                               │                                │
│ Best Pair                     │ BNB/USDT 0.53%                 │
│ Worst Pair                    │ ETH/USDT -0.64%                │
│ Best trade                    │ BTC/USDT 3.96%                 │
│ Worst trade                   │ BTC/USDT -3.79%                │
│ Best day                      │ 13.081 USDT                    │
│ Worst day                     │ -12.7 USDT                     │
│ Days win/draw/lose            │ 2 / 265 / 6                    │
│ Min/Max/Avg. Duration Winners │ 1d 08:00 / 1d 08:00 / 1d 08:00 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 1d 05:00 / 0d 07:00 │
│ Max Consecutive Wins / Loss   │ 2 / 6                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 994.276 USDT                   │
│ Max balance                   │ 1022.895 USDT                  │
│ Max % of account underwater   │ 2.80%                          │
│ Absolute drawdown             │ 28.62 USDT (2.80%)             │
│ Drawdown duration             │ 223 days 10:00:00              │
│ Profit at drawdown start      │ 22.895 USDT                    │
│ Profit at drawdown end        │ -5.724 USDT                    │
│ Drawdown start                │ 2022-03-29 00:00:00            │
│ Drawdown end                  │ 2022-11-07 10:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                               STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃          Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │      8 │        -0.21 │          -5.724 │        -0.57 │     13:15:00 │    2     0     6  25.0 │ 28.62 USDT  2.80% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴───────────────────┘

```
