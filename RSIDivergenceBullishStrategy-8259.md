# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Median Profit: 0.0%, Profit Factor: 0.73)

---
            
**Strategy:** RSIDivergenceBullishStrategy  
**Random State:** 8259  
**Timestamp:** 2025-09-12 17:18:02

## Configuration
```json
{
  "strategy": "RSIDivergenceBullishStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 8259,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy RSIDivergenceBullishStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 8259
```

## Hyperopt Output
```

Best result:

*    1/100:     69 trades. 34/21/14 Wins/Draws/Losses. Avg profit  -0.35%. Median profit   0.00%. Total profit -35.64000126 USDT (  -3.56%). Avg duration 21:18:00 min. Objective: 0.08345

{"params":{"lookback_period_for_divergence":44,"lookback_period_for_pivots":13,"pivot_confirmation_period":0,"rsi_oversold":21,"rsi_period":13,"lookback_period_for_stoploss":3,"stoploss_margin":0.99,"take_profit_multiplier":1,"use_custom_stoploss_param":false},"minimal_roi":{"0":0.255,"159":0.097,"459":0.056,"1462":0},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

```

## Backtesting Command
```bash
docker compose run --rm freqtrade backtesting --config /freqtrade/user_data/config.json --strategy RSIDivergenceBullishStrategy --timeframe 1h --timeframe-detail 5m --datadir /freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20221231
```

## Backtesting Output
```
Result for strategy RSIDivergenceBullishStrategy
                                               BACKTESTING REPORT                                               
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ LTC/USDT │     15 │         0.23 │           7.145 │         0.71 │  1 day, 0:34:00 │    9     3     3  60.0 │
│ BNB/USDT │     10 │        -0.11 │           0.190 │         0.02 │        21:32:00 │    5     3     2  50.0 │
│ BTC/USDT │      6 │        -0.34 │          -4.993 │         -0.5 │        23:48:00 │    4     1     1  66.7 │
│ ETH/USDT │     12 │        -0.89 │         -21.240 │        -2.12 │  1 day, 5:22:00 │    4     5     3  33.3 │
│ XRP/USDT │      6 │        -3.04 │         -35.943 │        -3.59 │ 1 day, 17:23:00 │    2     2     2  33.3 │
│    TOTAL │     49 │        -0.58 │         -54.841 │        -5.48 │  1 day, 3:05:00 │   24    14    11  49.0 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴─────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT                                          
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 ENTER TAG STATS                                                 
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │      49 │        -0.58 │         -54.841 │        -5.48 │ 1 day, 3:05:00 │   24    14    11  49.0 │
│     TOTAL │      49 │        -0.58 │         -54.841 │        -5.48 │ 1 day, 3:05:00 │   24    14    11  49.0 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│         roi │    38 │          2.2 │         147.998 │         14.8 │ 1 day, 3:50:00 │   24    14     0   100 │
│   stop_loss │    11 │       -10.18 │        -202.839 │       -20.28 │ 1 day, 0:30:00 │    0     0    11     0 │
│       TOTAL │    49 │        -0.58 │         -54.841 │        -5.48 │ 1 day, 3:05:00 │   24    14    11  49.0 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                       MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │         roi │     38 │          2.2 │         147.998 │         14.8 │ 1 day, 3:50:00 │   24    14     0   100 │
│           │   stop_loss │     11 │       -10.18 │        -202.839 │       -20.28 │ 1 day, 0:30:00 │    0     0    11     0 │
│     TOTAL │             │     49 │        -0.58 │         -54.841 │        -5.48 │ 1 day, 3:05:00 │   24    14    11  49.0 │
└───────────┴─────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2022-12-31 00:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 49 / 0.13                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 945.159 USDT                   │
│ Absolute profit               │ -54.841 USDT                   │
│ Total profit %                │ -5.48%                         │
│ CAGR %                        │ -5.50%                         │
│ Sortino                       │ -1.28                          │
│ Sharpe                        │ -0.29                          │
│ Calmar                        │ -3.58                          │
│ SQN                           │ -0.77                          │
│ Profit factor                 │ 0.73                           │
│ Expectancy (Ratio)            │ -1.12 (-0.35)                  │
│ Avg. daily profit             │ -0.151 USDT                    │
│ Avg. stake amount             │ 177.933 USDT                   │
│ Total trade volume            │ 17417.378 USDT                 │
│                               │                                │
│ Best Pair                     │ LTC/USDT 0.71%                 │
│ Worst Pair                    │ XRP/USDT -3.59%                │
│ Best trade                    │ LTC/USDT 5.99%                 │
│ Worst trade                   │ LTC/USDT -10.18%               │
│ Best day                      │ 19.166 USDT                    │
│ Worst day                     │ -38.448 USDT                   │
│ Days win/draw/lose            │ 18 / 325 / 8                   │
│ Min/Max/Avg. Duration Winners │ 0d 07:40 / 1d 00:25 / 0d 20:26 │
│ Min/Max/Avg. Duration Losers  │ 0d 08:45 / 3d 08:10 / 1d 00:30 │
│ Max Consecutive Wins / Loss   │ 9 / 6                          │
│ Rejected Entry signals        │ 48                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 924.552 USDT                   │
│ Max balance                   │ 1005.345 USDT                  │
│ Max % of account underwater   │ 8.04%                          │
│ Absolute drawdown             │ 80.793 USDT (8.04%)            │
│ Drawdown duration             │ 293 days 11:50:00              │
│ Profit at drawdown start      │ 5.345 USDT                     │
│ Profit at drawdown end        │ -75.448 USDT                   │
│ Drawdown start                │ 2022-01-20 09:25:00            │
│ Drawdown end                  │ 2022-11-09 21:15:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                    STRATEGY SUMMARY                                                                    
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃                     Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ RSIDivergenceBullishStrategy │     49 │        -0.58 │         -54.841 │        -5.48 │ 1 day, 3:05:00 │   24    14    11  49.0 │ 80.793 USDT  8.04% │
└──────────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┴────────────────────┘

```
