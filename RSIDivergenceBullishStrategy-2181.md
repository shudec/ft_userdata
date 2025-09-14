# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Median Profit: 7.18%, Profit Factor: 0.0)

---
            
**Strategy:** RSIDivergenceBullishStrategy  
**Random State:** 2181  
**Timestamp:** 2025-09-12 22:16:32

## Configuration
```json
{
  "strategy": "RSIDivergenceBullishStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy",
  "random_state": 2181,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy RSIDivergenceBullishStrategy --timeframe 1h --epochs 100 --spaces buy --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 2181
```

## Hyperopt Output
```

Best result:

    42/100:      6 trades. 4/0/2 Wins/Draws/Losses. Avg profit   4.30%. Median profit   7.18%. Total profit 86.33535994 USDT (   8.63%). Avg duration 11:40:00 min. Objective: -0.07565

{"params":{"lookback_period_for_divergence":28,"lookback_period_for_pivots":17,"rsi_oversold":35,"rsi_period":12,"volume_factor":2.876,"volume_sma_period":29,"lookback_period_for_stoploss":5,"stoploss_margin":0.998,"take_profit_multiplier":1.5,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ BTC/USDT │      1 │         3.28 │          30.732 │         3.07 │      8:05:00 │    1     0     0   100 │
│ LTC/USDT │      1 │         8.31 │          30.017 │          3.0 │      5:45:00 │    1     0     0   100 │
│ ETH/USDT │      1 │         6.43 │           3.037 │          0.3 │      9:20:00 │    1     0     0   100 │
│ BNB/USDT │      1 │         2.57 │           0.967 │          0.1 │      3:05:00 │    1     0     0   100 │
│ XRP/USDT │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
│    TOTAL │      4 │         5.15 │          64.752 │         6.48 │      6:34:00 │    4     0     0   100 │
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
│     OTHER │       4 │         5.15 │          64.752 │         6.48 │      6:34:00 │    4     0     0   100 │
│     TOTAL │       4 │         5.15 │          64.752 │         6.48 │      6:34:00 │    4     0     0   100 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │     4 │         5.15 │          64.752 │         6.48 │      6:34:00 │    4     0     0   100 │
│            TOTAL │     4 │         5.15 │          64.752 │         6.48 │      6:34:00 │    4     0     0   100 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1.5R │      4 │         5.15 │          64.752 │         6.48 │      6:34:00 │    4     0     0   100 │
│     TOTAL │                  │      4 │         5.15 │          64.752 │         6.48 │      6:34:00 │    4     0     0   100 │
└───────────┴──────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2022-12-31 00:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 4 / 0.01                       │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1064.752 USDT                  │
│ Absolute profit               │ 64.752 USDT                    │
│ Total profit %                │ 6.48%                          │
│ CAGR %                        │ 6.49%                          │
│ Sortino                       │ -100.00                        │
│ Sharpe                        │ 0.24                           │
│ Calmar                        │ -100.00                        │
│ SQN                           │ 1.97                           │
│ Profit factor                 │ 0.00                           │
│ Expectancy (Ratio)            │ 16.19 (100.00)                 │
│ Avg. daily profit             │ 0.178 USDT                     │
│ Avg. stake amount             │ 345.098 USDT                   │
│ Total trade volume            │ 2831.193 USDT                  │
│                               │                                │
│ Best Pair                     │ BTC/USDT 3.07%                 │
│ Worst Pair                    │ XRP/USDT 0.00%                 │
│ Best trade                    │ LTC/USDT 8.31%                 │
│ Worst trade                   │ BNB/USDT 2.57%                 │
│ Best day                      │ 34.735 USDT                    │
│ Worst day                     │ 0 USDT                         │
│ Days win/draw/lose            │ 2 / 63 / 0                     │
│ Min/Max/Avg. Duration Winners │ 0d 03:05 / 0d 09:20 / 0d 06:34 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 0d 00:00 / 0d 00:00 │
│ Max Consecutive Wins / Loss   │ 4 / 0                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 1030.017 USDT                  │
│ Max balance                   │ 1064.752 USDT                  │
│ Max % of account underwater   │ 0.00%                          │
│ Absolute Drawdown (Account)   │ 0.00%                          │
│ Absolute Drawdown             │ 0 USDT                         │
│ Drawdown high                 │ 30.017 USDT                    │
│ Drawdown low                  │ 30.017 USDT                    │
│ Drawdown Start                │ 2022-05-10 06:45:00            │
│ Drawdown End                  │ 2022-05-10 06:45:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃                     Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃      Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ RSIDivergenceBullishStrategy │      4 │         5.15 │          64.752 │         6.48 │      6:34:00 │    4     0     0   100 │ 0 USDT  0.00% │
└──────────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴───────────────┘

```
