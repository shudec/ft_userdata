# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 349 / 0.96, Median: -0.8%, Total profit: -15.14%, Sortino: -1.88, Sharpe: -0.9, Calmar: -2.81, Drawdown: 28.26%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 8153  
**Timestamp:** 2025-09-15 22:21:53

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 8153,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 8153
```

## Hyperopt Output
```

Best result:

*    5/100:    695 trades. 227/0/468 Wins/Draws/Losses. Avg profit   0.54%. Median profit  -0.80%. Total profit 1945.35650770 USDT ( 194.54%). Avg duration 19:40:00 min. Objective: -1.35122

{"params":{"stoploss_margin":1.0,"lookback_period_for_stoploss":0,"take_profit_multiplier":3,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ XRP/USDT │     68 │         0.33 │          59.211 │         5.92 │     17:34:00 │   23     0    45  33.8 │
│ BNB/USDT │     74 │        -0.05 │          -4.568 │        -0.46 │     16:49:00 │   21     0    53  28.4 │
│ ETH/USDT │     66 │        -0.04 │         -15.803 │        -1.58 │     18:12:00 │   22     0    44  33.3 │
│ BTC/USDT │     75 │        -0.22 │         -45.898 │        -4.59 │     17:56:00 │   20     0    55  26.7 │
│ LTC/USDT │     66 │        -0.65 │        -144.327 │       -14.43 │     19:21:00 │   20     0    46  30.3 │
│    TOTAL │    349 │        -0.12 │        -151.385 │       -15.14 │     17:57:00 │  106     0   243  30.4 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                           LEFT OPEN TRADES REPORT                                           
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │        -0.04 │          -0.104 │        -0.01 │      8:00:00 │    0     0     1     0 │
│    TOTAL │      1 │        -0.04 │          -0.104 │        -0.01 │      8:00:00 │    0     0     1     0 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                ENTER TAG STATS                                                
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │     349 │        -0.12 │        -151.385 │       -15.14 │     17:57:00 │  106     0   243  30.4 │
│     TOTAL │     349 │        -0.12 │        -151.385 │       -15.14 │     17:57:00 │  106     0   243  30.4 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                               EXIT REASON STATS                                               
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  force_exit │     1 │        -0.04 │          -0.104 │        -0.01 │      8:00:00 │    0     0     1     0 │
│   stop_loss │     1 │        -3.57 │         -11.782 │        -1.18 │      3:50:00 │    0     0     1     0 │
│ exit_signal │   347 │        -0.11 │        -139.499 │       -13.95 │     18:01:00 │  106     0   241  30.5 │
│       TOTAL │   349 │        -0.12 │        -151.385 │       -15.14 │     17:57:00 │  106     0   243  30.4 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                      MIXED TAG STATS                                                       
┏━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │  force_exit │      1 │        -0.04 │          -0.104 │        -0.01 │      8:00:00 │    0     0     1     0 │
│           │   stop_loss │      1 │        -3.57 │         -11.782 │        -1.18 │      3:50:00 │    0     0     1     0 │
│           │ exit_signal │    347 │        -0.11 │        -139.499 │       -13.95 │     18:01:00 │  106     0   241  30.5 │
│     TOTAL │             │    349 │        -0.12 │        -151.385 │       -15.14 │     17:57:00 │  106     0   243  30.4 │
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
│ Total/Daily Avg Trades        │ 349 / 0.96                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 848.615 USDT                   │
│ Absolute profit               │ -151.385 USDT                  │
│ Total profit %                │ -15.14%                        │
│ CAGR %                        │ -15.18%                        │
│ Sortino                       │ -1.88                          │
│ Sharpe                        │ -0.90                          │
│ Calmar                        │ -2.81                          │
│ SQN                           │ -0.92                          │
│ Profit factor                 │ 0.87                           │
│ Expectancy (Ratio)            │ -0.43 (-0.09)                  │
│ Avg. daily profit             │ -0.416 USDT                    │
│ Avg. stake amount             │ 310.015 USDT                   │
│ Total trade volume            │ 216671.964 USDT                │
│                               │                                │
│ Best Pair                     │ XRP/USDT 5.92%                 │
│ Worst Pair                    │ LTC/USDT -14.43%               │
│ Best trade                    │ XRP/USDT 17.78%                │
│ Worst trade                   │ LTC/USDT -11.18%               │
│ Best day                      │ 68.33 USDT                     │
│ Worst day                     │ -45.44 USDT                    │
│ Days win/draw/lose            │ 59 / 189 / 114                 │
│ Min/Max/Avg. Duration Winners │ 0d 05:00 / 4d 07:00 / 1d 10:32 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 3d 00:00 / 0d 10:42 │
│ Max Consecutive Wins / Loss   │ 6 / 16                         │
│ Rejected Entry signals        │ 444                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 794.42 USDT                    │
│ Max balance                   │ 1107.319 USDT                  │
│ Max % of account underwater   │ 28.26%                         │
│ Absolute Drawdown (Account)   │ 28.26%                         │
│ Absolute Drawdown             │ 312.898 USDT                   │
│ Drawdown high                 │ 107.319 USDT                   │
│ Drawdown low                  │ -205.58 USDT                   │
│ Drawdown Start                │ 2022-03-29 00:00:00            │
│ Drawdown End                  │ 2022-10-20 18:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │    349 │        -0.12 │        -151.385 │       -15.14 │     17:57:00 │  106     0   243  30.4 │ 312.898 USDT  28.26% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
