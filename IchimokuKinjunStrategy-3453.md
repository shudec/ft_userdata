# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 499 / 1.37, Median: -0.83%, Total profit: -20.04%, Sortino: -2.63, Sharpe: -1.21, Calmar: -2.93, Drawdown: 35.96%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 3453  
**Timestamp:** 2025-09-15 22:16:31

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 3453,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 3453
```

## Hyperopt Output
```

Best result:

*   17/100:   1043 trades. 333/0/710 Wins/Draws/Losses. Avg profit   0.39%. Median profit  -0.83%. Total profit 1852.78800928 USDT ( 185.28%). Avg duration 19:17:00 min. Objective: -1.20627

{"params":{"stoploss_margin":0.997,"lookback_period_for_stoploss":0,"take_profit_multiplier":3,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ BNB/USDT │     93 │         0.07 │          15.099 │         1.51 │     17:47:00 │   26     0    67  28.0 │
│ XRP/USDT │     89 │         0.08 │           7.944 │         0.79 │     17:53:00 │   25     0    64  28.1 │
│ ETH/USDT │    105 │        -0.03 │         -24.913 │        -2.49 │     18:53:00 │   37     0    68  35.2 │
│ BTC/USDT │    114 │        -0.19 │         -56.926 │        -5.69 │     17:43:00 │   31     0    83  27.2 │
│ LTC/USDT │     98 │        -0.43 │        -141.638 │       -14.16 │     17:11:00 │   29     0    69  29.6 │
│    TOTAL │    499 │        -0.11 │        -200.434 │       -20.04 │     17:54:00 │  148     0   351  29.7 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                           LEFT OPEN TRADES REPORT                                           
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │      1 │        -0.04 │          -0.098 │        -0.01 │      8:00:00 │    0     0     1     0 │
│ LTC/USDT │      1 │        -0.65 │          -1.729 │        -0.17 │      3:00:00 │    0     0     1     0 │
│    TOTAL │      2 │        -0.35 │          -1.827 │        -0.18 │      5:30:00 │    0     0     2     0 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                ENTER TAG STATS                                                
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │     499 │        -0.11 │        -200.434 │       -20.04 │     17:54:00 │  148     0   351  29.7 │
│     TOTAL │     499 │        -0.11 │        -200.434 │       -20.04 │     17:54:00 │  148     0   351  29.7 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                               EXIT REASON STATS                                               
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  force_exit │     2 │        -0.35 │          -1.827 │        -0.18 │      5:30:00 │    0     0     2     0 │
│   stop_loss │     2 │        -6.99 │         -44.531 │        -4.45 │      3:20:00 │    0     0     2     0 │
│ exit_signal │   495 │        -0.08 │        -154.076 │       -15.41 │     18:00:00 │  148     0   347  29.9 │
│       TOTAL │   499 │        -0.11 │        -200.434 │       -20.04 │     17:54:00 │  148     0   351  29.7 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                      MIXED TAG STATS                                                       
┏━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │  force_exit │      2 │        -0.35 │          -1.827 │        -0.18 │      5:30:00 │    0     0     2     0 │
│           │   stop_loss │      2 │        -6.99 │         -44.531 │        -4.45 │      3:20:00 │    0     0     2     0 │
│           │ exit_signal │    495 │        -0.08 │        -154.076 │       -15.41 │     18:00:00 │  148     0   347  29.9 │
│     TOTAL │             │    499 │        -0.11 │        -200.434 │       -20.04 │     17:54:00 │  148     0   351  29.7 │
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
│ Total/Daily Avg Trades        │ 499 / 1.37                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 799.566 USDT                   │
│ Absolute profit               │ -200.434 USDT                  │
│ Total profit %                │ -20.04%                        │
│ CAGR %                        │ -20.09%                        │
│ Sortino                       │ -2.63                          │
│ Sharpe                        │ -1.21                          │
│ Calmar                        │ -2.93                          │
│ SQN                           │ -1.03                          │
│ Profit factor                 │ 0.87                           │
│ Expectancy (Ratio)            │ -0.40 (-0.09)                  │
│ Avg. daily profit             │ -0.551 USDT                    │
│ Avg. stake amount             │ 283.065 USDT                   │
│ Total trade volume            │ 282863.65 USDT                 │
│                               │                                │
│ Best Pair                     │ BNB/USDT 1.51%                 │
│ Worst Pair                    │ LTC/USDT -14.16%               │
│ Best trade                    │ LTC/USDT 21.99%                │
│ Worst trade                   │ LTC/USDT -11.18%               │
│ Best day                      │ 77.057 USDT                    │
│ Worst day                     │ -43.884 USDT                   │
│ Days win/draw/lose            │ 76 / 148 / 138                 │
│ Min/Max/Avg. Duration Winners │ 0d 05:00 / 4d 07:00 / 1d 10:28 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 4d 09:00 / 0d 10:55 │
│ Max Consecutive Wins / Loss   │ 7 / 18                         │
│ Rejected Entry signals        │ 1740                           │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 698.916 USDT                   │
│ Max balance                   │ 1091.3 USDT                    │
│ Max % of account underwater   │ 35.96%                         │
│ Absolute Drawdown (Account)   │ 35.96%                         │
│ Absolute Drawdown             │ 392.385 USDT                   │
│ Drawdown high                 │ 91.3 USDT                      │
│ Drawdown low                  │ -301.084 USDT                  │
│ Drawdown Start                │ 2022-03-29 00:00:00            │
│ Drawdown End                  │ 2022-09-23 11:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │    499 │        -0.11 │        -200.434 │       -20.04 │     17:54:00 │  148     0   351  29.7 │ 392.385 USDT  35.96% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
