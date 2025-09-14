# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Median: -0.61%, Total profit: -8.33%, Sortino: -1.73, Sharpe: -0.63, Calmar: -3.2, Drawdown: 13.68%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 4586  
**Timestamp:** 2025-09-14 22:06:33

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 4586,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 4586
```

## Hyperopt Output
```

Best result:

    90/100:    643 trades. 124/0/519 Wins/Draws/Losses. Avg profit  -0.13%. Median profit  -0.61%. Total profit -269.63715015 USDT ( -26.96%). Avg duration 7:17:00 min. Objective: 0.58855

{"params":{"lookback_period_for_stoploss":9,"stoploss_margin":0.99,"take_profit_multiplier":3,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ ETH/USDT │     58 │         0.19 │          33.942 │         3.39 │      7:01:00 │   14     0    44  24.1 │
│ XRP/USDT │     53 │         -0.1 │         -17.968 │         -1.8 │      6:03:00 │   16     0    37  30.2 │
│ BTC/USDT │     57 │        -0.12 │         -23.741 │        -2.37 │      6:10:00 │   12     0    45  21.1 │
│ BNB/USDT │     60 │        -0.13 │         -29.426 │        -2.94 │      8:22:00 │   12     0    48  20.0 │
│ LTC/USDT │     62 │        -0.23 │         -46.061 │        -4.61 │      7:49:00 │   14     0    48  22.6 │
│    TOTAL │    290 │        -0.08 │         -83.253 │        -8.33 │      7:08:00 │   68     0   222  23.4 │
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
│     OTHER │     290 │        -0.08 │         -83.253 │        -8.33 │      7:08:00 │   68     0   222  23.4 │
│     TOTAL │     290 │        -0.08 │         -83.253 │        -8.33 │      7:08:00 │   68     0   222  23.4 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │    17 │          6.9 │         375.958 │         37.6 │     17:08:00 │   17     0     0   100 │
│      stop_loss │     8 │        -2.41 │         -63.306 │        -6.33 │      1:30:00 │    0     0     8     0 │
│    exit_signal │   265 │        -0.46 │        -395.905 │       -39.59 │      6:39:00 │   51     0   214  19.2 │
│          TOTAL │   290 │        -0.08 │         -83.253 │        -8.33 │      7:08:00 │   68     0   222  23.4 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_3R │     17 │          6.9 │         375.958 │         37.6 │     17:08:00 │   17     0     0   100 │
│           │      stop_loss │      8 │        -2.41 │         -63.306 │        -6.33 │      1:30:00 │    0     0     8     0 │
│           │    exit_signal │    265 │        -0.46 │        -395.905 │       -39.59 │      6:39:00 │   51     0   214  19.2 │
│     TOTAL │                │    290 │        -0.08 │         -83.253 │        -8.33 │      7:08:00 │   68     0   222  23.4 │
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
│ Total/Daily Avg Trades        │ 290 / 0.8                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 916.747 USDT                   │
│ Absolute profit               │ -83.253 USDT                   │
│ Total profit %                │ -8.33%                         │
│ CAGR %                        │ -8.35%                         │
│ Sortino                       │ -1.73                          │
│ Sharpe                        │ -0.63                          │
│ Calmar                        │ -3.20                          │
│ SQN                           │ -0.71                          │
│ Profit factor                 │ 0.88                           │
│ Expectancy (Ratio)            │ -0.29 (-0.09)                  │
│ Avg. daily profit             │ -0.229 USDT                    │
│ Avg. stake amount             │ 326.357 USDT                   │
│ Total trade volume            │ 189582.824 USDT                │
│                               │                                │
│ Best Pair                     │ ETH/USDT 3.39%                 │
│ Worst Pair                    │ LTC/USDT -4.61%                │
│ Best trade                    │ ETH/USDT 9.65%                 │
│ Worst trade                   │ BNB/USDT -7.54%                │
│ Best day                      │ 60.778 USDT                    │
│ Worst day                     │ -27.035 USDT                   │
│ Days win/draw/lose            │ 34 / 226 / 98                  │
│ Min/Max/Avg. Duration Winners │ 0d 01:55 / 1d 19:00 / 0d 18:22 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:20 / 1d 05:00 / 0d 03:41 │
│ Max Consecutive Wins / Loss   │ 4 / 14                         │
│ Rejected Entry signals        │ 84                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 916.747 USDT                   │
│ Max balance                   │ 1061.98 USDT                   │
│ Max % of account underwater   │ 13.68%                         │
│ Absolute Drawdown (Account)   │ 13.68%                         │
│ Absolute Drawdown             │ 145.233 USDT                   │
│ Drawdown high                 │ 61.98 USDT                     │
│ Drawdown low                  │ -83.253 USDT                   │
│ Drawdown Start                │ 2022-07-07 20:00:00            │
│ Drawdown End                  │ 2022-12-28 04:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │    290 │        -0.08 │         -83.253 │        -8.33 │      7:08:00 │   68     0   222  23.4 │ 145.233 USDT  13.68% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
