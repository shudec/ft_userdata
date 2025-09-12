# Freqtrade Automation Log
            
**Strategy:** RSIDivergenceBullishStrategy  
**Random State:** 5742  
**Timestamp:** 2025-09-12 16:17:32

## Configuration
```json
{
  "strategy": "RSIDivergenceBullishStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 5742,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy RSIDivergenceBullishStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 5742
```

## Hyperopt Output
```

Best result:

    80/100:     93 trades. 48/15/30 Wins/Draws/Losses. Avg profit   0.25%. Median profit   0.04%. Total profit 48.32643728 USDT (   4.83%). Avg duration 16:21:00 min. Objective: -0.07082

{"params":{"lookback_period_for_divergence":62,"lookback_period_for_pivots":13,"pivot_confirmation_period":3,"rsi_oversold":33,"rsi_period":15,"lookback_period_for_stoploss":8,"stoploss_margin":0.991,"take_profit_multiplier":1,"use_custom_stoploss_param":true},"minimal_roi":{"0":0.255,"159":0.097,"459":0.056,"1462":0},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy RSIDivergenceBullishStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20221231
```

## Backtesting Output
```
Result for strategy RSIDivergenceBullishStrategy
                                             BACKTESTING REPORT                                              
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BNB/USDT │     12 │        -0.06 │          55.026 │          5.5 │     13:05:00 │    6     1     5  50.0 │
│ ETH/USDT │     13 │         0.76 │          51.994 │          5.2 │     18:17:00 │    9     1     3  69.2 │
│ LTC/USDT │     10 │         0.36 │          -9.093 │        -0.91 │     15:29:00 │    4     3     3  40.0 │
│ BTC/USDT │     11 │        -1.08 │         -36.982 │         -3.7 │     18:32:00 │    5     1     5  45.5 │
│ XRP/USDT │     16 │        -1.61 │         -62.222 │        -6.22 │     18:31:00 │    7     3     6  43.8 │
│    TOTAL │     62 │         -0.4 │          -1.276 │        -0.13 │     16:56:00 │   31     9    22  50.0 │
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
│     OTHER │      62 │         -0.4 │          -1.276 │        -0.13 │     16:56:00 │   31     9    22  50.0 │
│     TOTAL │      62 │         -0.4 │          -1.276 │        -0.13 │     16:56:00 │   31     9    22  50.0 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │    13 │         3.62 │         245.195 │        24.52 │      9:30:00 │   13     0     0   100 │
│            roi │    27 │         1.95 │         149.223 │        14.92 │     23:41:00 │   18     9     0   100 │
│      stop_loss │    22 │        -5.67 │        -395.694 │       -39.57 │     13:02:00 │    0     0    22     0 │
│          TOTAL │    62 │         -0.4 │          -1.276 │        -0.13 │     16:56:00 │   31     9    22  50.0 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1R │     13 │         3.62 │         245.195 │        24.52 │      9:30:00 │   13     0     0   100 │
│           │            roi │     27 │         1.95 │         149.223 │        14.92 │     23:41:00 │   18     9     0   100 │
│           │      stop_loss │     22 │        -5.67 │        -395.694 │       -39.57 │     13:02:00 │    0     0    22     0 │
│     TOTAL │                │     62 │         -0.4 │          -1.276 │        -0.13 │     16:56:00 │   31     9    22  50.0 │
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
│ Total/Daily Avg Trades        │ 62 / 0.17                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 998.724 USDT                   │
│ Absolute profit               │ -1.276 USDT                    │
│ Total profit %                │ -0.13%                         │
│ CAGR %                        │ -0.13%                         │
│ Sortino                       │ -0.01                          │
│ Sharpe                        │ -0.00                          │
│ Calmar                        │ -0.07                          │
│ SQN                           │ -0.01                          │
│ Profit factor                 │ 1.00                           │
│ Expectancy (Ratio)            │ -0.02 (-0.15)                  │
│ Avg. daily profit             │ -0.004 USDT                    │
│ Avg. stake amount             │ 440.541 USDT                   │
│ Total trade volume            │ 54735.11 USDT                  │
│                               │                                │
│ Best Pair                     │ BNB/USDT 5.50%                 │
│ Worst Pair                    │ XRP/USDT -6.22%                │
│ Best trade                    │ BNB/USDT 9.69%                 │
│ Worst trade                   │ XRP/USDT -18.25%               │
│ Best day                      │ 33.626 USDT                    │
│ Worst day                     │ -47.889 USDT                   │
│ Days win/draw/lose            │ 26 / 304 / 16                  │
│ Min/Max/Avg. Duration Winners │ 0d 02:45 / 1d 00:25 / 0d 16:15 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:40 / 1d 18:05 / 0d 13:02 │
│ Max Consecutive Wins / Loss   │ 8 / 3                          │
│ Rejected Entry signals        │ 36                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 970.189 USDT                   │
│ Max balance                   │ 1074.731 USDT                  │
│ Max % of account underwater   │ 9.59%                          │
│ Absolute drawdown             │ 103.06 USDT (9.59%)            │
│ Drawdown duration             │ 29 days 20:05:00               │
│ Profit at drawdown start      │ 74.731 USDT                    │
│ Profit at drawdown end        │ -28.329 USDT                   │
│ Drawdown start                │ 2022-04-12 08:15:00            │
│ Drawdown end                  │ 2022-05-12 04:20:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃                     Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ RSIDivergenceBullishStrategy │     62 │        -0.40 │          -1.276 │        -0.13 │     16:56:00 │   31     9    22  50.0 │ 103.06 USDT  9.59% │
└──────────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```
