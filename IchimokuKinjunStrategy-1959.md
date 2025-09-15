# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Median: -1.64%, Total profit: -10.5%, Sortino: -1.8, Sharpe: -0.56, Calmar: -3.66, Drawdown: 0%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 1959  
**Timestamp:** 2025-09-15 10:07:39

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 1959,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 1959
```

## Hyperopt Output
```

Best result:

    51/100:    138 trades. 64/0/74 Wins/Draws/Losses. Avg profit   0.23%. Median profit  -1.64%. Total profit 85.90218201 USDT (   8.59%). Avg duration 23:46:00 min. Objective: -0.10798

{"params":{"lookback_period_for_stoploss":4,"stoploss_margin":0.99,"take_profit_multiplier":1,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ XRP/USDT │      6 │         0.92 │          17.674 │         1.77 │     10:36:00 │    4     0     2  66.7 │
│ LTC/USDT │     14 │        -0.01 │           1.457 │         0.15 │     12:05:00 │    7     0     7  50.0 │
│ BTC/USDT │     16 │        -0.29 │         -14.281 │        -1.43 │     22:50:00 │    7     0     9  43.8 │
│ BNB/USDT │     15 │        -0.48 │         -25.398 │        -2.54 │     18:51:00 │    6     0     9  40.0 │
│ ETH/USDT │     13 │        -1.97 │         -84.454 │        -8.45 │      8:41:00 │    3     0    10  23.1 │
│    TOTAL │     64 │         -0.5 │        -105.001 │        -10.5 │     15:32:00 │   27     0    37  42.2 │
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
│     OTHER │      64 │         -0.5 │        -105.001 │        -10.5 │     15:32:00 │   27     0    37  42.2 │
│     TOTAL │      64 │         -0.5 │        -105.001 │        -10.5 │     15:32:00 │   27     0    37  42.2 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │    27 │         2.89 │         252.956 │         25.3 │     16:17:00 │   27     0     0   100 │
│      stop_loss │    37 │        -2.98 │        -357.957 │        -35.8 │     14:58:00 │    0     0    37     0 │
│          TOTAL │    64 │         -0.5 │        -105.001 │        -10.5 │     15:32:00 │   27     0    37  42.2 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1R │     27 │         2.89 │         252.956 │         25.3 │     16:17:00 │   27     0     0   100 │
│           │      stop_loss │     37 │        -2.98 │        -357.957 │        -35.8 │     14:58:00 │    0     0    37     0 │
│     TOTAL │                │     64 │         -0.5 │        -105.001 │        -10.5 │     15:32:00 │   27     0    37  42.2 │
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
│ Total/Daily Avg Trades        │ 64 / 0.18                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 894.999 USDT                   │
│ Absolute profit               │ -105.001 USDT                  │
│ Total profit %                │ -10.50%                        │
│ CAGR %                        │ -10.53%                        │
│ Sortino                       │ -1.80                          │
│ Sharpe                        │ -0.56                          │
│ Calmar                        │ -3.66                          │
│ SQN                           │ -1.33                          │
│ Profit factor                 │ 0.71                           │
│ Expectancy (Ratio)            │ -1.64 (-0.17)                  │
│ Avg. daily profit             │ -0.288 USDT                    │
│ Avg. stake amount             │ 323.903 USDT                   │
│ Total trade volume            │ 41437.345 USDT                 │
│                               │                                │
│ Best Pair                     │ XRP/USDT 1.77%                 │
│ Worst Pair                    │ ETH/USDT -8.45%                │
│ Best trade                    │ BTC/USDT 4.38%                 │
│ Worst trade                   │ ETH/USDT -4.88%                │
│ Best day                      │ 29.943 USDT                    │
│ Worst day                     │ -40.296 USDT                   │
│ Days win/draw/lose            │ 19 / 284 / 29                  │
│ Min/Max/Avg. Duration Winners │ 0d 01:10 / 2d 11:05 / 0d 16:17 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:50 / 3d 08:15 / 0d 14:58 │
│ Max Consecutive Wins / Loss   │ 7 / 7                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 894.999 USDT                   │
│ Max balance                   │ 1053.816 USDT                  │
│ Max % of account underwater   │ 15.07%                         │
│ Absolute drawdown             │ 158.817 USDT (15.07%)          │
│ Drawdown duration             │ 274 days 19:15:00              │
│ Profit at drawdown start      │ 53.816 USDT                    │
│ Profit at drawdown end        │ -105.001 USDT                  │
│ Drawdown start                │ 2022-03-27 22:10:00            │
│ Drawdown end                  │ 2022-12-27 17:25:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │     64 │        -0.50 │        -105.001 │        -10.5 │     15:32:00 │   27     0    37  42.2 │ 158.817 USDT  15.07% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
