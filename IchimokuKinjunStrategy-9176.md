# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Median: -0.95%, Total profit: 1.39%, Sortino: 0.23, Sharpe: 0.11, Calmar: 2.92, Drawdown: 0%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 9176  
**Timestamp:** 2025-09-15 11:23:47

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 9176,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 9176
```

## Hyperopt Output
```

Best result:

*   15/100:     67 trades. 22/0/45 Wins/Draws/Losses. Avg profit   0.20%. Median profit  -0.95%. Total profit 41.31481319 USDT (   4.13%). Avg duration 8:23:00 min. Objective: -0.08169

{"params":{"lookback_period_for_stoploss":10,"stoploss_margin":0.993,"take_profit_multiplier":1,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ LTC/USDT │      3 │         1.23 │          12.550 │         1.26 │      2:28:00 │    2     0     1  66.7 │
│ BTC/USDT │      6 │         0.25 │           4.806 │         0.48 │     13:46:00 │    3     0     3  50.0 │
│ ETH/USDT │      2 │         0.12 │           0.672 │         0.07 │      2:08:00 │    1     0     1  50.0 │
│ XRP/USDT │      4 │         0.02 │           0.076 │         0.01 │      3:06:00 │    1     0     3  25.0 │
│ BNB/USDT │      5 │        -0.24 │          -4.208 │        -0.42 │      4:09:00 │    1     0     4  20.0 │
│    TOTAL │     20 │         0.22 │          13.896 │         1.39 │      6:22:00 │    8     0    12  40.0 │
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
│     OTHER │      20 │         0.22 │          13.896 │         1.39 │      6:22:00 │    8     0    12  40.0 │
│     TOTAL │      20 │         0.22 │          13.896 │         1.39 │      6:22:00 │    8     0    12  40.0 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │     8 │         2.39 │          64.095 │         6.41 │        8:27:00 │    8     0     0   100 │
│      stop_loss │     1 │        -3.96 │         -13.463 │        -1.35 │ 1 day, 4:50:00 │    0     0     1     0 │
│    exit_signal │    11 │        -0.98 │         -36.736 │        -3.67 │        2:49:00 │    0     0    11     0 │
│          TOTAL │    20 │         0.22 │          13.896 │         1.39 │        6:22:00 │    8     0    12  40.0 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1R │      8 │         2.39 │          64.095 │         6.41 │        8:27:00 │    8     0     0   100 │
│           │      stop_loss │      1 │        -3.96 │         -13.463 │        -1.35 │ 1 day, 4:50:00 │    0     0     1     0 │
│           │    exit_signal │     11 │        -0.98 │         -36.736 │        -3.67 │        2:49:00 │    0     0    11     0 │
│     TOTAL │                │     20 │         0.22 │          13.896 │         1.39 │        6:22:00 │    8     0    12  40.0 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2022-12-31 00:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 20 / 0.05                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1013.896 USDT                  │
│ Absolute profit               │ 13.896 USDT                    │
│ Total profit %                │ 1.39%                          │
│ CAGR %                        │ 1.39%                          │
│ Sortino                       │ 0.23                           │
│ Sharpe                        │ 0.11                           │
│ Calmar                        │ 2.92                           │
│ SQN                           │ 0.47                           │
│ Profit factor                 │ 1.28                           │
│ Expectancy (Ratio)            │ 0.69 (0.17)                    │
│ Avg. daily profit             │ 0.038 USDT                     │
│ Avg. stake amount             │ 337.937 USDT                   │
│ Total trade volume            │ 13558.464 USDT                 │
│                               │                                │
│ Best Pair                     │ LTC/USDT 1.26%                 │
│ Worst Pair                    │ BNB/USDT -0.42%                │
│ Best trade                    │ XRP/USDT 2.96%                 │
│ Worst trade                   │ BTC/USDT -3.96%                │
│ Best day                      │ 14.947 USDT                    │
│ Worst day                     │ -13.463 USDT                   │
│ Days win/draw/lose            │ 7 / 257 / 10                   │
│ Min/Max/Avg. Duration Winners │ 0d 02:35 / 1d 09:20 / 0d 08:27 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 1d 04:50 / 0d 04:59 │
│ Max Consecutive Wins / Loss   │ 3 / 6                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 1007.219 USDT                  │
│ Max balance                   │ 1039.886 USDT                  │
│ Max % of account underwater   │ 2.50%                          │
│ Absolute drawdown             │ 25.99 USDT (2.50%)             │
│ Drawdown duration             │ 109 days 20:10:00              │
│ Profit at drawdown start      │ 39.886 USDT                    │
│ Profit at drawdown end        │ 13.896 USDT                    │
│ Drawdown start                │ 2022-07-20 13:50:00            │
│ Drawdown end                  │ 2022-11-07 10:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                               STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃          Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │     20 │         0.22 │          13.896 │         1.39 │      6:22:00 │    8     0    12  40.0 │ 25.99 USDT  2.50% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴───────────────────┘

```
