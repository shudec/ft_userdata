# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Median Profit: -0.64%, Profit Factor: 0.7)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 4444  
**Timestamp:** 2025-09-13 22:46:58

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 4444,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 4444
```

## Hyperopt Output
```

Best result:

    58/100:   3592 trades. 735/0/2857 Wins/Draws/Losses. Avg profit  -0.08%. Median profit  -0.64%. Total profit -716.64249270 USDT ( -71.66%). Avg duration 8:42:00 min. Objective: 1.79609

{"params":{"lookback_period_for_stoploss":5,"stoploss_margin":0.99,"take_profit_multiplier":3,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ ETH/USDT │    343 │        -0.07 │         -33.087 │        -3.31 │      8:56:00 │   72     0   271  21.0 │
│ BNB/USDT │    261 │        -0.18 │        -117.324 │       -11.73 │      8:46:00 │   50     0   211  19.2 │
│ XRP/USDT │    272 │        -0.31 │        -168.984 │        -16.9 │      7:22:00 │   44     0   228  16.2 │
│ LTC/USDT │    350 │        -0.28 │        -192.330 │       -19.23 │      8:29:00 │   68     0   282  19.4 │
│ BTC/USDT │    378 │        -0.28 │        -209.096 │       -20.91 │      8:17:00 │   67     0   311  17.7 │
│    TOTAL │   1604 │        -0.22 │        -720.822 │       -72.08 │      8:23:00 │  301     0  1303  18.8 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                           LEFT OPEN TRADES REPORT                                           
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ LTC/USDT │      1 │         1.25 │           1.142 │         0.11 │      9:00:00 │    1     0     0   100 │
│ ETH/USDT │      1 │         0.21 │           0.193 │         0.02 │      8:00:00 │    1     0     0   100 │
│ BTC/USDT │      1 │         0.11 │           0.105 │         0.01 │      8:00:00 │    1     0     0   100 │
│    TOTAL │      3 │         0.52 │           1.440 │         0.14 │      8:20:00 │    3     0     0   100 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                ENTER TAG STATS                                                
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │    1604 │        -0.22 │        -720.822 │       -72.08 │      8:23:00 │  301     0  1303  18.8 │
│     TOTAL │    1604 │        -0.22 │        -720.822 │       -72.08 │      8:23:00 │  301     0  1303  18.8 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │    70 │         7.52 │         873.687 │        87.37 │     19:56:00 │   70     0     0   100 │
│     force_exit │     3 │         0.52 │           1.440 │         0.14 │      8:20:00 │    3     0     0   100 │
│      stop_loss │    69 │        -2.77 │        -332.005 │        -33.2 │      3:18:00 │    0     0    69     0 │
│    exit_signal │  1462 │        -0.48 │       -1263.944 │      -126.39 │      8:05:00 │  228     0  1234  15.6 │
│          TOTAL │  1604 │        -0.22 │        -720.822 │       -72.08 │      8:23:00 │  301     0  1303  18.8 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_3R │     70 │         7.52 │         873.687 │        87.37 │     19:56:00 │   70     0     0   100 │
│           │     force_exit │      3 │         0.52 │           1.440 │         0.14 │      8:20:00 │    3     0     0   100 │
│           │      stop_loss │     69 │        -2.77 │        -332.005 │        -33.2 │      3:18:00 │    0     0    69     0 │
│           │    exit_signal │   1462 │        -0.48 │       -1263.944 │      -126.39 │      8:05:00 │  228     0  1234  15.6 │
│     TOTAL │                │   1604 │        -0.22 │        -720.822 │       -72.08 │      8:23:00 │  301     0  1303  18.8 │
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
│ Total/Daily Avg Trades        │ 1604 / 4.41                    │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 279.178 USDT                   │
│ Absolute profit               │ -720.822 USDT                  │
│ Total profit %                │ -72.08%                        │
│ CAGR %                        │ -72.18%                        │
│ Sortino                       │ -22.83                         │
│ Sharpe                        │ -8.96                          │
│ Calmar                        │ -5.23                          │
│ SQN                           │ -4.26                          │
│ Profit factor                 │ 0.70                           │
│ Expectancy (Ratio)            │ -0.45 (-0.24)                  │
│ Avg. daily profit             │ -1.98 USDT                     │
│ Avg. stake amount             │ 176.829 USDT                   │
│ Total trade volume            │ 567679.665 USDT                │
│                               │                                │
│ Best Pair                     │ ETH/USDT -3.31%                │
│ Worst Pair                    │ BTC/USDT -20.91%               │
│ Best trade                    │ ETH/USDT 22.25%                │
│ Worst trade                   │ ETH/USDT -6.57%                │
│ Best day                      │ 46.907 USDT                    │
│ Worst day                     │ -59.504 USDT                   │
│ Days win/draw/lose            │ 109 / 33 / 222                 │
│ Min/Max/Avg. Duration Winners │ 0d 00:10 / 2d 21:00 / 1d 00:06 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 1d 07:00 / 0d 04:46 │
│ Max Consecutive Wins / Loss   │ 4 / 34                         │
│ Rejected Entry signals        │ 7087                           │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 277.729 USDT                   │
│ Max balance                   │ 1002.55 USDT                   │
│ Max % of account underwater   │ 72.30%                         │
│ Absolute Drawdown (Account)   │ 72.30%                         │
│ Absolute Drawdown             │ 724.82 USDT                    │
│ Drawdown high                 │ 2.55 USDT                      │
│ Drawdown low                  │ -722.271 USDT                  │
│ Drawdown Start                │ 2022-01-03 04:00:00            │
│ Drawdown End                  │ 2022-12-25 19:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃            Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │   1604 │        -0.22 │        -720.822 │       -72.08 │      8:23:00 │  301     0  1303  18.8 │ 724.82 USDT  72.30% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴─────────────────────┘

```
