# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Median Profit: -0.27%, Profit Factor: 1.35)

---
            
**Strategy:** RSIDivergenceBullishStrategy  
**Random State:** 4285  
**Timestamp:** 2025-09-12 21:58:07

## Configuration
```json
{
  "strategy": "RSIDivergenceBullishStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy",
  "random_state": 4285,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy RSIDivergenceBullishStrategy --timeframe 1h --epochs 100 --spaces buy --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 4285
```

## Hyperopt Output
```

Best result:

    35/100:      6 trades. 3/0/3 Wins/Draws/Losses. Avg profit  -0.30%. Median profit  -0.27%. Total profit 51.54754194 USDT (   5.15%). Avg duration 12:20:00 min. Objective: -0.03614

{"params":{"lookback_period_for_divergence":45,"lookback_period_for_pivots":13,"rsi_oversold":33,"rsi_period":15,"volume_factor":1.842,"volume_sma_period":48,"lookback_period_for_stoploss":5,"stoploss_margin":0.998,"take_profit_multiplier":1.5,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ BNB/USDT │      4 │         0.72 │          21.089 │         2.11 │      3:15:00 │    2     0     2  50.0 │
│ LTC/USDT │      7 │         0.78 │          10.066 │         1.01 │      6:21:00 │    4     0     3  57.1 │
│ BTC/USDT │      2 │         0.46 │           9.242 │         0.92 │      6:02:00 │    1     0     1  50.0 │
│ ETH/USDT │      1 │         6.43 │           3.003 │          0.3 │      9:20:00 │    1     0     0   100 │
│ XRP/USDT │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
│    TOTAL │     14 │         1.12 │          43.400 │         4.34 │      5:38:00 │    8     0     6  57.1 │
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
│     OTHER │      14 │         1.12 │          43.400 │         4.34 │      5:38:00 │    8     0     6  57.1 │
│     TOTAL │      14 │         1.12 │          43.400 │         4.34 │      5:38:00 │    8     0     6  57.1 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1.5R │     8 │         4.08 │         168.183 │        16.82 │      6:42:00 │    8     0     0   100 │
│        stop_loss │     6 │        -2.83 │        -124.784 │       -12.48 │      4:12:00 │    0     0     6     0 │
│            TOTAL │    14 │         1.12 │          43.400 │         4.34 │      5:38:00 │    8     0     6  57.1 │
└──────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃      Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1.5R │      8 │         4.08 │         168.183 │        16.82 │      6:42:00 │    8     0     0   100 │
│           │        stop_loss │      6 │        -2.83 │        -124.784 │       -12.48 │      4:12:00 │    0     0     6     0 │
│     TOTAL │                  │     14 │         1.12 │          43.400 │         4.34 │      5:38:00 │    8     0     6  57.1 │
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
│ Total/Daily Avg Trades        │ 14 / 0.04                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1043.4 USDT                    │
│ Absolute profit               │ 43.4 USDT                      │
│ Total profit %                │ 4.34%                          │
│ CAGR %                        │ 4.35%                          │
│ Sortino                       │ 0.83                           │
│ Sharpe                        │ 0.10                           │
│ Calmar                        │ 4.02                           │
│ SQN                           │ 0.50                           │
│ Profit factor                 │ 1.35                           │
│ Expectancy (Ratio)            │ 3.10 (0.15)                    │
│ Avg. daily profit             │ 0.119 USDT                     │
│ Avg. stake amount             │ 711.118 USDT                   │
│ Total trade volume            │ 19994.653 USDT                 │
│                               │                                │
│ Best Pair                     │ BNB/USDT 2.11%                 │
│ Worst Pair                    │ XRP/USDT 0.00%                 │
│ Best trade                    │ LTC/USDT 8.31%                 │
│ Worst trade                   │ LTC/USDT -4.46%                │
│ Best day                      │ 34.543 USDT                    │
│ Worst day                     │ -23.138 USDT                   │
│ Days win/draw/lose            │ 6 / 319 / 6                    │
│ Min/Max/Avg. Duration Winners │ 0d 02:30 / 0d 09:45 / 0d 06:42 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:15 / 0d 07:35 / 0d 04:12 │
│ Max Consecutive Wins / Loss   │ 6 / 3                          │
│ Rejected Entry signals        │ 24                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 943.296 USDT                   │
│ Max balance                   │ 1089.011 USDT                  │
│ Max % of account underwater   │ 5.67%                          │
│ Absolute Drawdown (Account)   │ 5.67%                          │
│ Absolute Drawdown             │ 56.704 USDT                    │
│ Drawdown high                 │ -20.633 USDT                   │
│ Drawdown low                  │ -56.704 USDT                   │
│ Drawdown Start                │ 2022-01-21 21:35:00            │
│ Drawdown End                  │ 2022-02-27 21:15:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃                     Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ RSIDivergenceBullishStrategy │     14 │         1.12 │          43.400 │         4.34 │      5:38:00 │    8     0     6  57.1 │ 56.704 USDT  5.67% │
└──────────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```
