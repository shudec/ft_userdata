# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 12 / 0.03, Median: -0.74%, Total profit: -1.33%, Sortino: -0.1, Sharpe: -0.06, Calmar: -1.98, Drawdown: 0%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 7365  
**Timestamp:** 2025-09-15 16:51:55

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 7365,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 7365
```

## Hyperopt Output
```

Best result:

    31/100:     54 trades. 9/0/45 Wins/Draws/Losses. Avg profit  -0.29%. Median profit  -0.74%. Total profit -51.57713967 USDT (  -5.16%). Avg duration 9:49:00 min. Objective: 0.14838

{"params":{"lookback_period_for_stoploss":3,"stoploss_margin":0.999,"take_profit_multiplier":3,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ BTC/USDT │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
│ ETH/USDT │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
│ BNB/USDT │      4 │        -0.25 │          -3.772 │        -0.38 │      8:50:00 │    1     0     3  25.0 │
│ LTC/USDT │      4 │        -0.34 │          -4.608 │        -0.46 │      7:18:00 │    1     0     3  25.0 │
│ XRP/USDT │      4 │        -0.37 │          -4.950 │         -0.5 │      8:59:00 │    1     0     3  25.0 │
│    TOTAL │     12 │        -0.32 │         -13.330 │        -1.33 │      8:22:00 │    3     0     9  25.0 │
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
│     OTHER │      12 │        -0.32 │         -13.330 │        -1.33 │      8:22:00 │    3     0     9  25.0 │
│     TOTAL │      12 │        -0.32 │         -13.330 │        -1.33 │      8:22:00 │    3     0     9  25.0 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │     2 │         4.77 │          31.202 │         3.12 │     19:00:00 │    2     0     0   100 │
│      stop_loss │     2 │        -1.86 │         -12.221 │        -1.22 │      3:42:00 │    0     0     2     0 │
│    exit_signal │     8 │        -1.21 │         -32.312 │        -3.23 │      6:52:00 │    1     0     7  12.5 │
│          TOTAL │    12 │        -0.32 │         -13.330 │        -1.33 │      8:22:00 │    3     0     9  25.0 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_3R │      2 │         4.77 │          31.202 │         3.12 │     19:00:00 │    2     0     0   100 │
│           │      stop_loss │      2 │        -1.86 │         -12.221 │        -1.22 │      3:42:00 │    0     0     2     0 │
│           │    exit_signal │      8 │        -1.21 │         -32.312 │        -3.23 │      6:52:00 │    1     0     7  12.5 │
│     TOTAL │                │     12 │        -0.32 │         -13.330 │        -1.33 │      8:22:00 │    3     0     9  25.0 │
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
│ Total/Daily Avg Trades        │ 12 / 0.03                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 986.67 USDT                    │
│ Absolute profit               │ -13.33 USDT                    │
│ Total profit %                │ -1.33%                         │
│ CAGR %                        │ -1.34%                         │
│ Sortino                       │ -0.10                          │
│ Sharpe                        │ -0.06                          │
│ Calmar                        │ -1.98                          │
│ SQN                           │ -0.34                          │
│ Profit factor                 │ 0.74                           │
│ Expectancy (Ratio)            │ -1.11 (-0.19)                  │
│ Avg. daily profit             │ -0.037 USDT                    │
│ Avg. stake amount             │ 329.035 USDT                   │
│ Total trade volume            │ 7899.283 USDT                  │
│                               │                                │
│ Best Pair                     │ BTC/USDT 0.00%                 │
│ Worst Pair                    │ XRP/USDT -0.50%                │
│ Best trade                    │ BNB/USDT 7.40%                 │
│ Worst trade                   │ BNB/USDT -7.54%                │
│ Best day                      │ 24.294 USDT                    │
│ Worst day                     │ -25.264 USDT                   │
│ Days win/draw/lose            │ 3 / 83 / 9                     │
│ Min/Max/Avg. Duration Winners │ 0d 18:20 / 1d 04:00 / 0d 22:00 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:55 / 0d 11:00 / 0d 03:49 │
│ Max Consecutive Wins / Loss   │ 1 / 4                          │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 982.175 USDT                   │
│ Max balance                   │ 1018.161 USDT                  │
│ Max % of account underwater   │ 3.53%                          │
│ Absolute drawdown             │ 35.986 USDT (3.53%)            │
│ Drawdown duration             │ 21 days 13:40:00               │
│ Profit at drawdown start      │ 18.161 USDT                    │
│ Profit at drawdown end        │ -17.825 USDT                   │
│ Drawdown start                │ 2022-11-04 09:20:00            │
│ Drawdown end                  │ 2022-11-25 23:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │     12 │        -0.32 │         -13.330 │        -1.33 │      8:22:00 │    3     0     9  25.0 │ 35.986 USDT  3.53% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```
