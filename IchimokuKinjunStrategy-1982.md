# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 14 / 0.04, Median: -0.74%, Total profit: 0.16%, Sortino: 0.01, Sharpe: 0.01, Calmar: 0.25, Drawdown: 0%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 1982  
**Timestamp:** 2025-09-15 17:56:24

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 1982,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 1982
```

## Hyperopt Output
```

Best result:

    49/100:     54 trades. 9/0/45 Wins/Draws/Losses. Avg profit  -0.29%. Median profit  -0.74%. Total profit -51.57713967 USDT (  -5.16%). Avg duration 9:49:00 min. Objective: 0.14838

{"params":{"lookback_period_for_stoploss":3,"stoploss_margin":0.999,"take_profit_multiplier":3,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ LTC/USDT │      6 │         0.56 │          10.764 │         1.08 │      5:44:00 │    2     0     4  33.3 │
│ BTC/USDT │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
│ ETH/USDT │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
│ BNB/USDT │      4 │        -0.25 │          -4.164 │        -0.42 │      8:50:00 │    1     0     3  25.0 │
│ XRP/USDT │      4 │        -0.37 │          -4.950 │         -0.5 │      8:59:00 │    1     0     3  25.0 │
│    TOTAL │     14 │         0.06 │           1.650 │         0.16 │      7:33:00 │    4     0    10  28.6 │
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
│     OTHER │      14 │         0.06 │           1.650 │         0.16 │      7:33:00 │    4     0    10  28.6 │
│     TOTAL │      14 │         0.06 │           1.650 │         0.16 │      7:33:00 │    4     0    10  28.6 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │     3 │         4.88 │          48.090 │         4.81 │     14:05:00 │    3     0     0   100 │
│      stop_loss │     2 │        -1.86 │         -12.316 │        -1.23 │      3:42:00 │    0     0     2     0 │
│    exit_signal │     9 │        -1.12 │         -34.125 │        -3.41 │      6:13:00 │    1     0     8  11.1 │
│          TOTAL │    14 │         0.06 │           1.650 │         0.16 │      7:33:00 │    4     0    10  28.6 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_3R │      3 │         4.88 │          48.090 │         4.81 │     14:05:00 │    3     0     0   100 │
│           │      stop_loss │      2 │        -1.86 │         -12.316 │        -1.23 │      3:42:00 │    0     0     2     0 │
│           │    exit_signal │      9 │        -1.12 │         -34.125 │        -3.41 │      6:13:00 │    1     0     8  11.1 │
│     TOTAL │                │     14 │         0.06 │           1.650 │         0.16 │      7:33:00 │    4     0    10  28.6 │
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
│ Total/Daily Avg Trades        │ 14 / 0.04                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1001.65 USDT                   │
│ Absolute profit               │ 1.65 USDT                      │
│ Total profit %                │ 0.16%                          │
│ CAGR %                        │ 0.17%                          │
│ Sortino                       │ 0.01                           │
│ Sharpe                        │ 0.01                           │
│ Calmar                        │ 0.25                           │
│ SQN                           │ 0.04                           │
│ Profit factor                 │ 1.03                           │
│ Expectancy (Ratio)            │ 0.12 (0.02)                    │
│ Avg. daily profit             │ 0.005 USDT                     │
│ Avg. stake amount             │ 330.969 USDT                   │
│ Total trade volume            │ 9287.327 USDT                  │
│                               │                                │
│ Best Pair                     │ LTC/USDT 1.08%                 │
│ Worst Pair                    │ XRP/USDT -0.50%                │
│ Best trade                    │ BNB/USDT 7.40%                 │
│ Worst trade                   │ BNB/USDT -7.54%                │
│ Best day                      │ 39.736 USDT                    │
│ Worst day                     │ -25.633 USDT                   │
│ Days win/draw/lose            │ 3 / 83 / 9                     │
│ Min/Max/Avg. Duration Winners │ 0d 04:15 / 1d 04:00 / 0d 17:34 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:55 / 0d 11:00 / 0d 03:32 │
│ Max Consecutive Wins / Loss   │ 2 / 4                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 992.525 USDT                   │
│ Max balance                   │ 1033.603 USDT                  │
│ Max % of account underwater   │ 3.53%                          │
│ Absolute drawdown             │ 36.516 USDT (3.53%)            │
│ Drawdown duration             │ 21 days 13:40:00               │
│ Profit at drawdown start      │ 33.603 USDT                    │
│ Profit at drawdown end        │ -2.913 USDT                    │
│ Drawdown start                │ 2022-11-04 09:20:00            │
│ Drawdown end                  │ 2022-11-25 23:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │     14 │         0.06 │           1.650 │         0.16 │      7:33:00 │    4     0    10  28.6 │ 36.516 USDT  3.53% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```
