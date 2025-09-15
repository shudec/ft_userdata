# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 84 / 0.23, Median: -0.74%, Total profit: 2.11%, Sortino: 0.28, Sharpe: 0.12, Calmar: 1.71, Drawdown: 0%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 1069  
**Timestamp:** 2025-09-15 16:30:07

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 1069,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 1069
```

## Hyperopt Output
```

Best result:

*    9/100:    205 trades. 43/0/162 Wins/Draws/Losses. Avg profit  -0.36%. Median profit  -0.74%. Total profit -223.96105451 USDT ( -22.40%). Avg duration 9:02:00 min. Objective: 0.54383

{"params":{"lookback_period_for_stoploss":10,"stoploss_margin":0.994,"take_profit_multiplier":3,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ BNB/USDT │     24 │         0.44 │          34.466 │         3.45 │     11:19:00 │    8     0    16  33.3 │
│ ETH/USDT │     11 │         0.66 │          23.105 │         2.31 │      9:08:00 │    4     0     7  36.4 │
│ LTC/USDT │     16 │         0.27 │          14.789 │         1.48 │     10:42:00 │    5     0    11  31.2 │
│ BTC/USDT │     18 │        -0.01 │          -2.900 │        -0.29 │      8:27:00 │    4     0    14  22.2 │
│ XRP/USDT │     15 │        -0.95 │         -48.397 │        -4.84 │      9:56:00 │    2     0    13  13.3 │
│    TOTAL │     84 │         0.09 │          21.062 │         2.11 │     10:03:00 │   23     0    61  27.4 │
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
│     OTHER │      84 │         0.09 │          21.062 │         2.11 │     10:03:00 │   23     0    61  27.4 │
│     TOTAL │      84 │         0.09 │          21.062 │         2.11 │     10:03:00 │   23     0    61  27.4 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │    10 │         6.05 │         203.339 │        20.33 │     19:26:00 │   10     0     0   100 │
│      stop_loss │     6 │         -2.2 │         -45.558 │        -4.56 │     16:13:00 │    0     0     6     0 │
│    exit_signal │    68 │        -0.58 │        -136.720 │       -13.67 │      8:08:00 │   13     0    55  19.1 │
│          TOTAL │    84 │         0.09 │          21.062 │         2.11 │     10:03:00 │   23     0    61  27.4 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_3R │     10 │         6.05 │         203.339 │        20.33 │     19:26:00 │   10     0     0   100 │
│           │      stop_loss │      6 │         -2.2 │         -45.558 │        -4.56 │     16:13:00 │    0     0     6     0 │
│           │    exit_signal │     68 │        -0.58 │        -136.720 │       -13.67 │      8:08:00 │   13     0    55  19.1 │
│     TOTAL │                │     84 │         0.09 │          21.062 │         2.11 │     10:03:00 │   23     0    61  27.4 │
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
│ Total/Daily Avg Trades        │ 84 / 0.23                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 1021.062 USDT                  │
│ Absolute profit               │ 21.062 USDT                    │
│ Total profit %                │ 2.11%                          │
│ CAGR %                        │ 2.11%                          │
│ Sortino                       │ 0.28                           │
│ Sharpe                        │ 0.12                           │
│ Calmar                        │ 1.71                           │
│ SQN                           │ 0.26                           │
│ Profit factor                 │ 1.09                           │
│ Expectancy (Ratio)            │ 0.25 (0.06)                    │
│ Avg. daily profit             │ 0.058 USDT                     │
│ Avg. stake amount             │ 340.615 USDT                   │
│ Total trade volume            │ 57359.027 USDT                 │
│                               │                                │
│ Best Pair                     │ BNB/USDT 3.45%                 │
│ Worst Pair                    │ XRP/USDT -4.84%                │
│ Best trade                    │ BNB/USDT 8.13%                 │
│ Worst trade                   │ BNB/USDT -7.54%                │
│ Best day                      │ 47.444 USDT                    │
│ Worst day                     │ -26.511 USDT                   │
│ Days win/draw/lose            │ 17 / 288 / 41                  │
│ Min/Max/Avg. Duration Winners │ 0d 04:00 / 1d 19:00 / 0d 23:27 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:20 / 2d 13:45 / 0d 05:00 │
│ Max Consecutive Wins / Loss   │ 3 / 11                         │
│ Rejected Entry signals        │ 24                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 983.272 USDT                   │
│ Max balance                   │ 1090.467 USDT                  │
│ Max % of account underwater   │ 6.46%                          │
│ Absolute drawdown             │ 70.403 USDT (6.46%)            │
│ Drawdown duration             │ 89 days 17:00:00               │
│ Profit at drawdown start      │ 90.467 USDT                    │
│ Profit at drawdown end        │ 20.063 USDT                    │
│ Drawdown start                │ 2022-08-06 09:00:00            │
│ Drawdown end                  │ 2022-11-04 02:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │     84 │         0.09 │          21.062 │         2.11 │     10:03:00 │   23     0    61  27.4 │ 70.403 USDT  6.46% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```
