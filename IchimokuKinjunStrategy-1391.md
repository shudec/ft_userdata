# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Median: -0.61%, Total profit: -6.11%, Sortino: -1.01, Sharpe: -0.44, Calmar: -2.67, Drawdown: 12.01%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 1391  
**Timestamp:** 2025-09-14 22:08:59

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 1391,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 1391
```

## Hyperopt Output
```

Best result:

    48/100:    230 trades. 57/0/173 Wins/Draws/Losses. Avg profit  -0.14%. Median profit  -0.61%. Total profit -111.37270203 USDT ( -11.14%). Avg duration 8:49:00 min. Objective: 0.24958

{"params":{"lookback_period_for_stoploss":6,"stoploss_margin":0.998,"take_profit_multiplier":3,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ XRP/USDT │     15 │         0.06 │           2.484 │         0.25 │      8:41:00 │    6     0     9  40.0 │
│ BTC/USDT │     22 │        -0.05 │          -3.405 │        -0.34 │      7:15:00 │    5     0    17  22.7 │
│ BNB/USDT │     24 │        -0.16 │         -13.178 │        -1.32 │      6:42:00 │    6     0    18  25.0 │
│ LTC/USDT │     28 │        -0.22 │         -19.441 │        -1.94 │      6:51:00 │    7     0    21  25.0 │
│ ETH/USDT │     16 │        -0.49 │         -27.579 │        -2.76 │      4:15:00 │    2     0    14  12.5 │
│    TOTAL │    105 │        -0.17 │         -61.119 │        -6.11 │      6:46:00 │   26     0    79  24.8 │
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
│     OTHER │     105 │        -0.17 │         -61.119 │        -6.11 │      6:46:00 │   26     0    79  24.8 │
│     TOTAL │     105 │        -0.17 │         -61.119 │        -6.11 │      6:46:00 │   26     0    79  24.8 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │    14 │         4.48 │         209.421 │        20.94 │     11:41:00 │   14     0     0   100 │
│      stop_loss │    11 │        -1.91 │         -70.429 │        -7.04 │      4:05:00 │    0     0    11     0 │
│    exit_signal │    80 │        -0.74 │        -200.111 │       -20.01 │      6:16:00 │   12     0    68  15.0 │
│          TOTAL │   105 │        -0.17 │         -61.119 │        -6.11 │      6:46:00 │   26     0    79  24.8 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_3R │     14 │         4.48 │         209.421 │        20.94 │     11:41:00 │   14     0     0   100 │
│           │      stop_loss │     11 │        -1.91 │         -70.429 │        -7.04 │      4:05:00 │    0     0    11     0 │
│           │    exit_signal │     80 │        -0.74 │        -200.111 │       -20.01 │      6:16:00 │   12     0    68  15.0 │
│     TOTAL │                │    105 │        -0.17 │         -61.119 │        -6.11 │      6:46:00 │   26     0    79  24.8 │
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
│ Total/Daily Avg Trades        │ 105 / 0.29                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 938.881 USDT                   │
│ Absolute profit               │ -61.119 USDT                   │
│ Total profit %                │ -6.11%                         │
│ CAGR %                        │ -6.13%                         │
│ Sortino                       │ -1.01                          │
│ Sharpe                        │ -0.44                          │
│ Calmar                        │ -2.67                          │
│ SQN                           │ -0.82                          │
│ Profit factor                 │ 0.80                           │
│ Expectancy (Ratio)            │ -0.58 (-0.15)                  │
│ Avg. daily profit             │ -0.168 USDT                    │
│ Avg. stake amount             │ 335.139 USDT                   │
│ Total trade volume            │ 70458.888 USDT                 │
│                               │                                │
│ Best Pair                     │ XRP/USDT 0.25%                 │
│ Worst Pair                    │ ETH/USDT -2.76%                │
│ Best trade                    │ BNB/USDT 7.40%                 │
│ Worst trade                   │ BNB/USDT -7.54%                │
│ Best day                      │ 47.187 USDT                    │
│ Worst day                     │ -25.973 USDT                   │
│ Days win/draw/lose            │ 21 / 284 / 47                  │
│ Min/Max/Avg. Duration Winners │ 0d 01:20 / 1d 16:00 / 0d 15:11 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:15 / 1d 04:50 / 0d 04:00 │
│ Max Consecutive Wins / Loss   │ 6 / 10                         │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 935.774 USDT                   │
│ Max balance                   │ 1063.54 USDT                   │
│ Max % of account underwater   │ 12.01%                         │
│ Absolute Drawdown (Account)   │ 12.01%                         │
│ Absolute Drawdown             │ 127.766 USDT                   │
│ Drawdown high                 │ 63.54 USDT                     │
│ Drawdown low                  │ -64.226 USDT                   │
│ Drawdown Start                │ 2022-07-07 18:50:00            │
│ Drawdown End                  │ 2022-12-10 22:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │    105 │        -0.17 │         -61.119 │        -6.11 │      6:46:00 │   26     0    79  24.8 │ 127.766 USDT  12.01% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
