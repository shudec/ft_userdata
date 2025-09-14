# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Median: -0.62%, Total: -10.13%, Sortino: -2.18, Sharpe: -0.83, Calmar: -3.56, Drawdown: 14.93%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 9469  
**Timestamp:** 2025-09-14 21:33:31

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 9469,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 9469
```

## Hyperopt Output
```

Best result:

    98/100:    643 trades. 124/0/519 Wins/Draws/Losses. Avg profit  -0.12%. Median profit  -0.62%. Total profit -257.85409094 USDT ( -25.79%). Avg duration 6:47:00 min. Objective: 0.54503

{"params":{"lookback_period_for_stoploss":10,"stoploss_margin":0.996,"take_profit_multiplier":3,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ ETH/USDT │     58 │         0.12 │          22.180 │         2.22 │      6:16:00 │   14     0    44  24.1 │
│ BTC/USDT │     57 │        -0.11 │         -21.582 │        -2.16 │      5:55:00 │   12     0    45  21.1 │
│ XRP/USDT │     53 │        -0.14 │         -26.883 │        -2.69 │      5:55:00 │   16     0    37  30.2 │
│ BNB/USDT │     61 │        -0.15 │         -32.259 │        -3.23 │      6:54:00 │   12     0    49  19.7 │
│ LTC/USDT │     62 │        -0.22 │         -42.790 │        -4.28 │      7:37:00 │   14     0    48  22.6 │
│    TOTAL │    291 │         -0.1 │        -101.335 │       -10.13 │      6:33:00 │   68     0   223  23.4 │
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
│     OTHER │     291 │         -0.1 │        -101.335 │       -10.13 │      6:33:00 │   68     0   223  23.4 │
│     TOTAL │     291 │         -0.1 │        -101.335 │       -10.13 │      6:33:00 │   68     0   223  23.4 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │    26 │         5.15 │         432.278 │        43.23 │     13:57:00 │   26     0     0   100 │
│      stop_loss │    19 │        -1.71 │        -106.719 │       -10.67 │      3:32:00 │    0     0    19     0 │
│    exit_signal │   246 │        -0.53 │        -426.893 │       -42.69 │      6:00:00 │   42     0   204  17.1 │
│          TOTAL │   291 │         -0.1 │        -101.335 │       -10.13 │      6:33:00 │   68     0   223  23.4 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_3R │     26 │         5.15 │         432.278 │        43.23 │     13:57:00 │   26     0     0   100 │
│           │      stop_loss │     19 │        -1.71 │        -106.719 │       -10.67 │      3:32:00 │    0     0    19     0 │
│           │    exit_signal │    246 │        -0.53 │        -426.893 │       -42.69 │      6:00:00 │   42     0   204  17.1 │
│     TOTAL │                │    291 │         -0.1 │        -101.335 │       -10.13 │      6:33:00 │   68     0   223  23.4 │
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
│ Total/Daily Avg Trades        │ 291 / 0.8                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 898.665 USDT                   │
│ Absolute profit               │ -101.335 USDT                  │
│ Total profit %                │ -10.13%                        │
│ CAGR %                        │ -10.16%                        │
│ Sortino                       │ -2.18                          │
│ Sharpe                        │ -0.83                          │
│ Calmar                        │ -3.56                          │
│ SQN                           │ -0.93                          │
│ Profit factor                 │ 0.85                           │
│ Expectancy (Ratio)            │ -0.35 (-0.12)                  │
│ Avg. daily profit             │ -0.278 USDT                    │
│ Avg. stake amount             │ 325.887 USDT                   │
│ Total trade volume            │ 189944.162 USDT                │
│                               │                                │
│ Best Pair                     │ ETH/USDT 2.22%                 │
│ Worst Pair                    │ LTC/USDT -4.28%                │
│ Best trade                    │ ETH/USDT 9.51%                 │
│ Worst trade                   │ BNB/USDT -7.54%                │
│ Best day                      │ 58.418 USDT                    │
│ Worst day                     │ -27.088 USDT                   │
│ Days win/draw/lose            │ 34 / 227 / 97                  │
│ Min/Max/Avg. Duration Winners │ 0d 01:35 / 1d 19:00 / 0d 16:05 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:15 / 1d 04:50 / 0d 03:39 │
│ Max Consecutive Wins / Loss   │ 4 / 14                         │
│ Rejected Entry signals        │ 84                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 898.665 USDT                   │
│ Max balance                   │ 1056.413 USDT                  │
│ Max % of account underwater   │ 14.93%                         │
│ Absolute Drawdown (Account)   │ 14.93%                         │
│ Absolute Drawdown             │ 157.747 USDT                   │
│ Drawdown high                 │ 56.413 USDT                    │
│ Drawdown low                  │ -101.335 USDT                  │
│ Drawdown Start                │ 2022-07-07 19:30:00            │
│ Drawdown End                  │ 2022-12-28 04:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │    291 │        -0.10 │        -101.335 │       -10.13 │      6:33:00 │   68     0   223  23.4 │ 157.747 USDT  14.93% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
