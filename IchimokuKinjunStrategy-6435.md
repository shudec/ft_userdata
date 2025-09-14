# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Median Profit: -0.66%, Profit Factor: 0.74)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 6435  
**Timestamp:** 2025-09-14 21:06:04

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 6435,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 6435
```

## Hyperopt Output
```

Best result:

    98/100:   1614 trades. 329/0/1285 Wins/Draws/Losses. Avg profit   0.01%. Median profit  -0.66%. Total profit -109.15635349 USDT ( -10.92%). Avg duration 8:32:00 min. Objective: 0.20612

{"params":{"lookback_period_for_stoploss":8,"stoploss_margin":0.99,"take_profit_multiplier":3,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ XRP/USDT │    122 │        -0.02 │         -16.742 │        -1.67 │      6:43:00 │   28     0    94  23.0 │
│ LTC/USDT │    150 │        -0.11 │         -40.270 │        -4.03 │      9:01:00 │   33     0   117  22.0 │
│ ETH/USDT │    147 │        -0.16 │         -62.618 │        -6.26 │      7:35:00 │   30     0   117  20.4 │
│ BNB/USDT │    141 │        -0.34 │        -133.552 │       -13.36 │      7:42:00 │   26     0   115  18.4 │
│ BTC/USDT │    137 │        -0.37 │        -143.266 │       -14.33 │      5:48:00 │   19     0   118  13.9 │
│    TOTAL │    697 │        -0.21 │        -396.449 │       -39.64 │      7:25:00 │  136     0   561  19.5 │
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
│     OTHER │     697 │        -0.21 │        -396.449 │       -39.64 │      7:25:00 │  136     0   561  19.5 │
│     TOTAL │     697 │        -0.21 │        -396.449 │       -39.64 │      7:25:00 │  136     0   561  19.5 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │    28 │         7.59 │         572.258 │        57.23 │     15:41:00 │   28     0     0   100 │
│      stop_loss │    21 │        -2.47 │        -139.863 │       -13.99 │      1:17:00 │    0     0    21     0 │
│    exit_signal │   648 │        -0.47 │        -828.844 │       -82.88 │      7:15:00 │  108     0   540  16.7 │
│          TOTAL │   697 │        -0.21 │        -396.449 │       -39.64 │      7:25:00 │  136     0   561  19.5 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_3R │     28 │         7.59 │         572.258 │        57.23 │     15:41:00 │   28     0     0   100 │
│           │      stop_loss │     21 │        -2.47 │        -139.863 │       -13.99 │      1:17:00 │    0     0    21     0 │
│           │    exit_signal │    648 │        -0.47 │        -828.844 │       -82.88 │      7:15:00 │  108     0   540  16.7 │
│     TOTAL │                │    697 │        -0.21 │        -396.449 │       -39.64 │      7:25:00 │  136     0   561  19.5 │
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
│ Total/Daily Avg Trades        │ 697 / 1.91                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 603.551 USDT                   │
│ Absolute profit               │ -396.449 USDT                  │
│ Total profit %                │ -39.64%                        │
│ CAGR %                        │ -39.73%                        │
│ Sortino                       │ -9.35                          │
│ Sharpe                        │ -3.30                          │
│ Calmar                        │ -5.25                          │
│ SQN                           │ -2.38                          │
│ Profit factor                 │ 0.74                           │
│ Expectancy (Ratio)            │ -0.57 (-0.21)                  │
│ Avg. daily profit             │ -1.089 USDT                    │
│ Avg. stake amount             │ 275.554 USDT                   │
│ Total trade volume            │ 384494.054 USDT                │
│                               │                                │
│ Best Pair                     │ XRP/USDT -1.67%                │
│ Worst Pair                    │ BTC/USDT -14.33%               │
│ Best trade                    │ XRP/USDT 24.39%                │
│ Worst trade                   │ XRP/USDT -7.80%                │
│ Best day                      │ 54.988 USDT                    │
│ Worst day                     │ -46.297 USDT                   │
│ Days win/draw/lose            │ 49 / 164 / 147                 │
│ Min/Max/Avg. Duration Winners │ 0d 00:05 / 2d 16:00 / 0d 21:52 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 1d 05:00 / 0d 03:54 │
│ Max Consecutive Wins / Loss   │ 4 / 24                         │
│ Rejected Entry signals        │ 967                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 603.551 USDT                   │
│ Max balance                   │ 997.012 USDT                   │
│ Max % of account underwater   │ 39.64%                         │
│ Absolute Drawdown (Account)   │ 39.64%                         │
│ Absolute Drawdown             │ 396.449 USDT                   │
│ Drawdown high                 │ -2.988 USDT                    │
│ Drawdown low                  │ -396.449 USDT                  │
│ Drawdown Start                │ 2022-01-05 00:00:00            │
│ Drawdown End                  │ 2022-12-30 20:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │    697 │        -0.21 │        -396.449 │       -39.64 │      7:25:00 │  136     0   561  19.5 │ 396.449 USDT  39.64% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
