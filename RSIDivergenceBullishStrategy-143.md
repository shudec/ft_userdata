# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Median Profit: 0.0%, Profit Factor: 6.26)

---
            
**Strategy:** RSIDivergenceBullishStrategy  
**Random State:** 143  
**Timestamp:** 2025-09-13 22:11:12

## Configuration
```json
{
  "strategy": "RSIDivergenceBullishStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell roi",
  "random_state": 143,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy RSIDivergenceBullishStrategy --timeframe 1h --epochs 100 --spaces buy sell roi --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 143
```

## Hyperopt Output
```

Best result:

*   23/100:     17 trades. 7/2/8 Wins/Draws/Losses. Avg profit   0.82%. Median profit   0.00%. Total profit -33.43727551 USDT (  -3.34%). Avg duration 16:39:00 min. Objective: 0.04160

{"params":{"rsi_oversold":37,"lookback_period_for_divergence":72,"lookback_period_for_pivots":12,"rsi_period":14,"volume_factor":2,"volume_sma_period":20,"lookback_period_for_stoploss":4,"stoploss_margin":0.993,"take_profit_multiplier":2,"use_custom_stoploss_param":true},"minimal_roi":{"0":0.27,"271":0.122,"590":0.089,"1949":0},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ BNB/USDT │      1 │         8.89 │          59.493 │         5.95 │     10:05:00 │    1     0     0   100 │
│ BTC/USDT │      1 │         5.38 │          41.115 │         4.11 │     10:05:00 │    1     0     0   100 │
│ LTC/USDT │      2 │         7.21 │          35.230 │         3.52 │     18:50:00 │    2     0     0   100 │
│ XRP/USDT │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
│ ETH/USDT │      2 │         3.01 │         -12.719 │        -1.27 │     13:35:00 │    1     0     1  50.0 │
│    TOTAL │      6 │         5.78 │         123.120 │        12.31 │     14:10:00 │    5     0     1  83.3 │
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
│     OTHER │       6 │         5.78 │         123.120 │        12.31 │     14:10:00 │    5     0     1  83.3 │
│     TOTAL │       6 │         5.78 │         123.120 │        12.31 │     14:10:00 │    5     0     1  83.3 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│            roi │     2 │         8.89 │          89.059 │         8.91 │     10:58:00 │    2     0     0   100 │
│ take_profit_2R │     3 │         6.46 │          57.449 │         5.74 │     20:33:00 │    3     0     0   100 │
│      stop_loss │     1 │        -2.46 │         -23.388 │        -2.34 │      1:25:00 │    0     0     1     0 │
│          TOTAL │     6 │         5.78 │         123.120 │        12.31 │     14:10:00 │    5     0     1  83.3 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │            roi │      2 │         8.89 │          89.059 │         8.91 │     10:58:00 │    2     0     0   100 │
│           │ take_profit_2R │      3 │         6.46 │          57.449 │         5.74 │     20:33:00 │    3     0     0   100 │
│           │      stop_loss │      1 │        -2.46 │         -23.388 │        -2.34 │      1:25:00 │    0     0     1     0 │
│     TOTAL │                │      6 │         5.78 │         123.120 │        12.31 │     14:10:00 │    5     0     1  83.3 │
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
│ Total/Daily Avg Trades        │ 6 / 0.02                       │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1123.12 USDT                   │
│ Absolute profit               │ 123.12 USDT                    │
│ Total profit %                │ 12.31%                         │
│ CAGR %                        │ 12.35%                         │
│ Sortino                       │ -100.00                        │
│ Sharpe                        │ 0.24                           │
│ Calmar                        │ 30.03                          │
│ SQN                           │ 1.72                           │
│ Profit factor                 │ 6.26                           │
│ Expectancy (Ratio)            │ 20.52 (0.88)                   │
│ Avg. daily profit             │ 0.338 USDT                     │
│ Avg. stake amount             │ 489.975 USDT                   │
│ Total trade volume            │ 6014.833 USDT                  │
│                               │                                │
│ Best Pair                     │ BNB/USDT 5.95%                 │
│ Worst Pair                    │ ETH/USDT -1.27%                │
│ Best trade                    │ LTC/USDT 8.89%                 │
│ Worst trade                   │ ETH/USDT -2.46%                │
│ Best day                      │ 59.493 USDT                    │
│ Worst day                     │ -23.388 USDT                   │
│ Days win/draw/lose            │ 3 / 179 / 1                    │
│ Min/Max/Avg. Duration Winners │ 0d 10:05 / 1d 01:50 / 0d 16:43 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:25 / 0d 01:25 / 0d 01:25 │
│ Max Consecutive Wins / Loss   │ 4 / 1                          │
│ Rejected Entry signals        │ 24                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 1029.566 USDT                  │
│ Max balance                   │ 1123.12 USDT                   │
│ Max % of account underwater   │ 2.15%                          │
│ Absolute Drawdown (Account)   │ 2.15%                          │
│ Absolute Drawdown             │ 23.388 USDT                    │
│ Drawdown high                 │ 87.015 USDT                    │
│ Drawdown low                  │ 63.627 USDT                    │
│ Drawdown Start                │ 2022-07-14 15:50:00            │
│ Drawdown End                  │ 2022-09-16 16:25:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                   STRATEGY SUMMARY                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃                     Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ RSIDivergenceBullishStrategy │      6 │         5.78 │         123.120 │        12.31 │     14:10:00 │    5     0     1  83.3 │ 23.388 USDT  2.15% │
└──────────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```
