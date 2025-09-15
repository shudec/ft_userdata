# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 71 / 0.2, Median: -0.71%, Total profit: -1.34%, Sortino: -0.3, Sharpe: -0.14, Calmar: -1.65, Drawdown: 0%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 1163  
**Timestamp:** 2025-09-15 11:33:32

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 1163,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 1163
```

## Hyperopt Output
```

Best result:

    33/100:    186 trades. 45/0/141 Wins/Draws/Losses. Avg profit  -0.20%. Median profit  -0.71%. Total profit -120.62190244 USDT ( -12.06%). Avg duration 5:59:00 min. Objective: 0.35062

{"params":{"lookback_period_for_stoploss":5,"stoploss_margin":0.993,"take_profit_multiplier":1,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ ETH/USDT │     11 │         0.36 │          12.823 │         1.28 │      3:48:00 │    5     0     6  45.5 │
│ LTC/USDT │     12 │         0.25 │           9.875 │         0.99 │      3:23:00 │    4     0     8  33.3 │
│ BNB/USDT │     19 │         0.01 │           0.442 │         0.04 │      4:10:00 │    5     0    14  26.3 │
│ BTC/USDT │     17 │        -0.22 │         -12.912 │        -1.29 │      6:45:00 │    4     0    13  23.5 │
│ XRP/USDT │     12 │        -0.59 │         -23.620 │        -2.36 │      3:32:00 │    2     0    10  16.7 │
│    TOTAL │     71 │        -0.05 │         -13.391 │        -1.34 │      4:29:00 │   20     0    51  28.2 │
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
│     OTHER │      71 │        -0.05 │         -13.391 │        -1.34 │      4:29:00 │   20     0    51  28.2 │
│     TOTAL │      71 │        -0.05 │         -13.391 │        -1.34 │      4:29:00 │   20     0    51  28.2 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │    18 │         2.31 │         136.917 │        13.69 │      6:54:00 │   18     0     0   100 │
│      stop_loss │     4 │         -2.4 │         -32.021 │         -3.2 │      7:40:00 │    0     0     4     0 │
│    exit_signal │    49 │        -0.73 │        -118.287 │       -11.83 │      3:21:00 │    2     0    47   4.1 │
│          TOTAL │    71 │        -0.05 │         -13.391 │        -1.34 │      4:29:00 │   20     0    51  28.2 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1R │     18 │         2.31 │         136.917 │        13.69 │      6:54:00 │   18     0     0   100 │
│           │      stop_loss │      4 │         -2.4 │         -32.021 │         -3.2 │      7:40:00 │    0     0     4     0 │
│           │    exit_signal │     49 │        -0.73 │        -118.287 │       -11.83 │      3:21:00 │    2     0    47   4.1 │
│     TOTAL │                │     71 │        -0.05 │         -13.391 │        -1.34 │      4:29:00 │   20     0    51  28.2 │
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
│ Total/Daily Avg Trades        │ 71 / 0.2                       │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 986.609 USDT                   │
│ Absolute profit               │ -13.391 USDT                   │
│ Total profit %                │ -1.34%                         │
│ CAGR %                        │ -1.34%                         │
│ Sortino                       │ -0.30                          │
│ Sharpe                        │ -0.14                          │
│ Calmar                        │ -1.65                          │
│ SQN                           │ -0.31                          │
│ Profit factor                 │ 0.91                           │
│ Expectancy (Ratio)            │ -0.19 (-0.06)                  │
│ Avg. daily profit             │ -0.037 USDT                    │
│ Avg. stake amount             │ 330.228 USDT                   │
│ Total trade volume            │ 46972.833 USDT                 │
│                               │                                │
│ Best Pair                     │ ETH/USDT 1.28%                 │
│ Worst Pair                    │ XRP/USDT -2.36%                │
│ Best trade                    │ BTC/USDT 3.80%                 │
│ Worst trade                   │ BTC/USDT -3.83%                │
│ Best day                      │ 14.118 USDT                    │
│ Worst day                     │ -12.8 USDT                     │
│ Days win/draw/lose            │ 16 / 295 / 34                  │
│ Min/Max/Avg. Duration Winners │ 0d 00:50 / 1d 09:20 / 0d 07:45 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:20 / 1d 04:50 / 0d 03:13 │
│ Max Consecutive Wins / Loss   │ 2 / 9                          │
│ Rejected Entry signals        │ 12                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 977.75 USDT                    │
│ Max balance                   │ 1030.524 USDT                  │
│ Max % of account underwater   │ 4.26%                          │
│ Absolute drawdown             │ 43.915 USDT (4.26%)            │
│ Drawdown duration             │ 144 days 06:55:00              │
│ Profit at drawdown start      │ 30.524 USDT                    │
│ Profit at drawdown end        │ -13.391 USDT                   │
│ Drawdown start                │ 2022-08-05 02:05:00            │
│ Drawdown end                  │ 2022-12-27 09:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │     71 │        -0.05 │         -13.391 │        -1.34 │      4:29:00 │   20     0    51  28.2 │ 43.915 USDT  4.26% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```
