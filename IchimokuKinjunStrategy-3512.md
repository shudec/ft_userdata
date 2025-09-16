# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 19 / 0.05, Median: -0.95%, Total profit: 2.01%, Sortino: 0.59, Sharpe: 0.17, Calmar: 5.64, Drawdown: 1.87%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 3512  
**Timestamp:** 2025-09-15 21:57:29

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 3512,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 3512
```

## Hyperopt Output
```

Best result:

*    1/100:     64 trades. 17/0/47 Wins/Draws/Losses. Avg profit  -0.28%. Median profit  -0.95%. Total profit -37.95335059 USDT (  -3.80%). Avg duration 12:44:00 min. Objective: 0.12431

{"params":{"stoploss_margin":0.997,"lookback_period_for_stoploss":0,"take_profit_multiplier":1,"use_custom_stoploss_param":false},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ BTC/USDT │      6 │         1.69 │          20.595 │         2.06 │     19:05:00 │    3     0     3  50.0 │
│ LTC/USDT │      2 │         0.43 │           1.798 │         0.18 │      5:30:00 │    1     0     1  50.0 │
│ ETH/USDT │      2 │         0.32 │           0.160 │         0.02 │     16:00:00 │    1     0     1  50.0 │
│ BNB/USDT │      5 │        -0.09 │          -1.058 │        -0.11 │      9:24:00 │    1     0     4  20.0 │
│ XRP/USDT │      4 │        -0.16 │          -1.348 │        -0.13 │      9:15:00 │    1     0     3  25.0 │
│    TOTAL │     19 │         0.56 │          20.147 │         2.01 │     12:43:00 │    7     0    12  36.8 │
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
│     OTHER │      19 │         0.56 │          20.147 │         2.01 │     12:43:00 │    7     0    12  36.8 │
│     TOTAL │      19 │         0.56 │          20.147 │         2.01 │     12:43:00 │    7     0    12  36.8 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                  EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │     1 │        11.32 │          22.795 │         2.28 │ 1 day, 20:30:00 │    1     0     0   100 │
│    exit_signal │    18 │        -0.04 │          -2.648 │        -0.26 │        10:57:00 │    6     0    12  33.3 │
│          TOTAL │    19 │         0.56 │          20.147 │         2.01 │        12:43:00 │    7     0    12  36.8 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                          
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1R │      1 │        11.32 │          22.795 │         2.28 │ 1 day, 20:30:00 │    1     0     0   100 │
│           │    exit_signal │     18 │        -0.04 │          -2.648 │        -0.26 │        10:57:00 │    6     0    12  33.3 │
│     TOTAL │                │     19 │         0.56 │          20.147 │         2.01 │        12:43:00 │    7     0    12  36.8 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2022-12-31 00:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 19 / 0.05                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1020.147 USDT                  │
│ Absolute profit               │ 20.147 USDT                    │
│ Total profit %                │ 2.01%                          │
│ CAGR %                        │ 2.02%                          │
│ Sortino                       │ 0.59                           │
│ Sharpe                        │ 0.17                           │
│ Calmar                        │ 5.64                           │
│ SQN                           │ 0.71                           │
│ Profit factor                 │ 1.69                           │
│ Expectancy (Ratio)            │ 1.06 (0.43)                    │
│ Avg. daily profit             │ 0.055 USDT                     │
│ Avg. stake amount             │ 198.815 USDT                   │
│ Total trade volume            │ 7590.274 USDT                  │
│                               │                                │
│ Best Pair                     │ BTC/USDT 2.06%                 │
│ Worst Pair                    │ XRP/USDT -0.13%                │
│ Best trade                    │ BTC/USDT 11.32%                │
│ Worst trade                   │ BTC/USDT -3.79%                │
│ Best day                      │ 22.795 USDT                    │
│ Worst day                     │ -7.729 USDT                    │
│ Days win/draw/lose            │ 6 / 257 / 10                   │
│ Min/Max/Avg. Duration Winners │ 0d 04:00 / 1d 20:30 / 1d 01:56 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 1d 05:00 / 0d 05:00 │
│ Max Consecutive Wins / Loss   │ 3 / 6                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 1004.096 USDT                  │
│ Max balance                   │ 1039.624 USDT                  │
│ Max % of account underwater   │ 1.87%                          │
│ Absolute Drawdown (Account)   │ 1.87%                          │
│ Absolute Drawdown             │ 19.477 USDT                    │
│ Drawdown high                 │ 39.624 USDT                    │
│ Drawdown low                  │ 20.147 USDT                    │
│ Drawdown Start                │ 2022-07-20 20:00:00            │
│ Drawdown End                  │ 2022-11-07 10:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │     19 │         0.56 │          20.147 │         2.01 │     12:43:00 │    7     0    12  36.8 │ 19.477 USDT  1.87% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```
