# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 246 / 0.68, Median: -0.61%, Total profit: -10.42%, Sortino: -1.26, Sharpe: -0.65, Calmar: -3.12, Drawdown: 0%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 3905  
**Timestamp:** 2025-09-16 11:38:15

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 3905,
  "epochs": 200,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 200 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 3905
```

## Hyperopt Output
```

Best result:

   134/200:    552 trades. 124/0/428 Wins/Draws/Losses. Avg profit   0.52%. Median profit  -0.61%. Total profit 1280.53172991 USDT ( 128.05%). Avg duration 13:11:00 min. Objective: -0.92086

{"params":{"rsi_entry_max":55,"rsi_entry_min":41,"volume_factor":0.649,"stoploss_margin":0.99,"lookback_period_for_stoploss":0,"take_profit_multiplier":1,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ XRP/USDT │     50 │         0.58 │          93.193 │         9.32 │     15:20:00 │   17     0    33  34.0 │
│ BTC/USDT │     48 │        -0.03 │          -3.551 │        -0.36 │     13:14:00 │   13     0    35  27.1 │
│ ETH/USDT │     45 │        -0.28 │         -42.438 │        -4.24 │      7:51:00 │    7     0    38  15.6 │
│ LTC/USDT │     49 │        -0.32 │         -53.935 │        -5.39 │     15:57:00 │   16     0    33  32.7 │
│ BNB/USDT │     54 │        -0.55 │         -97.512 │        -9.75 │      8:32:00 │    7     0    47  13.0 │
│    TOTAL │    246 │        -0.12 │        -104.243 │       -10.42 │     12:11:00 │   60     0   186  24.4 │
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
│     OTHER │     246 │        -0.12 │        -104.243 │       -10.42 │     12:11:00 │   60     0   186  24.4 │
│     TOTAL │     246 │        -0.12 │        -104.243 │       -10.42 │     12:11:00 │   60     0   186  24.4 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │     5 │        10.94 │         177.738 │        17.77 │     19:55:00 │    5     0     0   100 │
│      stop_loss │     2 │        -7.16 │         -46.096 │        -4.61 │     11:22:00 │    0     0     2     0 │
│    exit_signal │   239 │         -0.3 │        -235.885 │       -23.59 │     12:02:00 │   55     0   184  23.0 │
│          TOTAL │   246 │        -0.12 │        -104.243 │       -10.42 │     12:11:00 │   60     0   186  24.4 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1R │      5 │        10.94 │         177.738 │        17.77 │     19:55:00 │    5     0     0   100 │
│           │      stop_loss │      2 │        -7.16 │         -46.096 │        -4.61 │     11:22:00 │    0     0     2     0 │
│           │    exit_signal │    239 │         -0.3 │        -235.885 │       -23.59 │     12:02:00 │   55     0   184  23.0 │
│     TOTAL │                │    246 │        -0.12 │        -104.243 │       -10.42 │     12:11:00 │   60     0   186  24.4 │
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
│ Total/Daily Avg Trades        │ 246 / 0.68                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 895.757 USDT                   │
│ Absolute profit               │ -104.243 USDT                  │
│ Total profit %                │ -10.42%                        │
│ CAGR %                        │ -10.45%                        │
│ Sortino                       │ -1.26                          │
│ Sharpe                        │ -0.65                          │
│ Calmar                        │ -3.12                          │
│ SQN                           │ -0.79                          │
│ Profit factor                 │ 0.84                           │
│ Expectancy (Ratio)            │ -0.42 (-0.12)                  │
│ Avg. daily profit             │ -0.286 USDT                    │
│ Avg. stake amount             │ 325.95 USDT                    │
│ Total trade volume            │ 160583.994 USDT                │
│                               │                                │
│ Best Pair                     │ XRP/USDT 9.32%                 │
│ Worst Pair                    │ BNB/USDT -9.75%                │
│ Best trade                    │ XRP/USDT 19.10%                │
│ Worst trade                   │ LTC/USDT -11.18%               │
│ Best day                      │ 61.983 USDT                    │
│ Worst day                     │ -38.392 USDT                   │
│ Days win/draw/lose            │ 37 / 223 / 97                  │
│ Min/Max/Avg. Duration Winners │ 0d 03:00 / 2d 23:00 / 1d 01:11 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 4d 09:00 / 0d 08:00 │
│ Max Consecutive Wins / Loss   │ 5 / 14                         │
│ Rejected Entry signals        │ 47                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 891.087 USDT                   │
│ Max balance                   │ 1080.226 USDT                  │
│ Max % of account underwater   │ 17.51%                         │
│ Absolute drawdown             │ 189.139 USDT (17.51%)          │
│ Drawdown duration             │ 94 days 14:00:00               │
│ Profit at drawdown start      │ 80.226 USDT                    │
│ Profit at drawdown end        │ -108.913 USDT                  │
│ Drawdown start                │ 2022-07-20 20:00:00            │
│ Drawdown end                  │ 2022-10-23 10:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │    246 │        -0.12 │        -104.243 │       -10.42 │     12:11:00 │   60     0   186  24.4 │ 189.139 USDT  17.51% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
