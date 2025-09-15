# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 291 / 0.8, Median: -0.62%, Total profit: -11.52%, Sortino: -2.53, Sharpe: -0.98, Calmar: -3.95, Drawdown: 0%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 9706  
**Timestamp:** 2025-09-15 15:36:22

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 9706,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 9706
```

## Hyperopt Output
```

Best result:

    86/100:    643 trades. 124/0/519 Wins/Draws/Losses. Avg profit  -0.14%. Median profit  -0.62%. Total profit -276.89665186 USDT ( -27.69%). Avg duration 6:42:00 min. Objective: 0.59797

{"params":{"lookback_period_for_stoploss":9,"stoploss_margin":0.996,"take_profit_multiplier":3,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ ETH/USDT │     58 │         0.07 │          12.196 │         1.22 │      6:10:00 │   14     0    44  24.1 │
│ BTC/USDT │     57 │         -0.1 │         -18.747 │        -1.87 │      5:55:00 │   12     0    45  21.1 │
│ XRP/USDT │     53 │        -0.15 │         -28.086 │        -2.81 │      5:54:00 │   16     0    37  30.2 │
│ BNB/USDT │     61 │        -0.16 │         -34.392 │        -3.44 │      6:53:00 │   12     0    49  19.7 │
│ LTC/USDT │     62 │        -0.24 │         -46.165 │        -4.62 │      7:37:00 │   14     0    48  22.6 │
│    TOTAL │    291 │        -0.12 │        -115.194 │       -11.52 │      6:32:00 │   68     0   223  23.4 │
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
│     OTHER │     291 │        -0.12 │        -115.194 │       -11.52 │      6:32:00 │   68     0   223  23.4 │
│     TOTAL │     291 │        -0.12 │        -115.194 │       -11.52 │      6:32:00 │   68     0   223  23.4 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │    26 │         4.98 │         414.561 │        41.46 │     13:44:00 │   26     0     0   100 │
│      stop_loss │    23 │        -1.65 │        -123.832 │       -12.38 │      3:10:00 │    0     0    23     0 │
│    exit_signal │   242 │        -0.52 │        -405.923 │       -40.59 │      6:04:00 │   42     0   200  17.4 │
│          TOTAL │   291 │        -0.12 │        -115.194 │       -11.52 │      6:32:00 │   68     0   223  23.4 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_3R │     26 │         4.98 │         414.561 │        41.46 │     13:44:00 │   26     0     0   100 │
│           │      stop_loss │     23 │        -1.65 │        -123.832 │       -12.38 │      3:10:00 │    0     0    23     0 │
│           │    exit_signal │    242 │        -0.52 │        -405.923 │       -40.59 │      6:04:00 │   42     0   200  17.4 │
│     TOTAL │                │    291 │        -0.12 │        -115.194 │       -11.52 │      6:32:00 │   68     0   223  23.4 │
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
│ Total/Daily Avg Trades        │ 291 / 0.8                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 884.806 USDT                   │
│ Absolute profit               │ -115.194 USDT                  │
│ Total profit %                │ -11.52%                        │
│ CAGR %                        │ -11.55%                        │
│ Sortino                       │ -2.53                          │
│ Sharpe                        │ -0.98                          │
│ Calmar                        │ -3.95                          │
│ SQN                           │ -1.09                          │
│ Profit factor                 │ 0.83                           │
│ Expectancy (Ratio)            │ -0.40 (-0.13)                  │
│ Avg. daily profit             │ -0.316 USDT                    │
│ Avg. stake amount             │ 323.151 USDT                   │
│ Total trade volume            │ 188334.925 USDT                │
│                               │                                │
│ Best Pair                     │ ETH/USDT 1.22%                 │
│ Worst Pair                    │ LTC/USDT -4.62%                │
│ Best trade                    │ BNB/USDT 7.40%                 │
│ Worst trade                   │ BNB/USDT -7.54%                │
│ Best day                      │ 48.567 USDT                    │
│ Worst day                     │ -27.116 USDT                   │
│ Days win/draw/lose            │ 34 / 227 / 97                  │
│ Min/Max/Avg. Duration Winners │ 0d 01:35 / 1d 19:00 / 0d 16:00 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:15 / 1d 04:50 / 0d 03:38 │
│ Max Consecutive Wins / Loss   │ 4 / 14                         │
│ Rejected Entry signals        │ 84                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 884.806 USDT                   │
│ Max balance                   │ 1044.798 USDT                  │
│ Max % of account underwater   │ 15.31%                         │
│ Absolute drawdown             │ 159.992 USDT (15.31%)          │
│ Drawdown duration             │ 322 days 21:50:00              │
│ Profit at drawdown start      │ 44.798 USDT                    │
│ Profit at drawdown end        │ -115.194 USDT                  │
│ Drawdown start                │ 2022-02-08 06:10:00            │
│ Drawdown end                  │ 2022-12-28 04:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │    291 │        -0.12 │        -115.194 │       -11.52 │      6:32:00 │   68     0   223  23.4 │ 159.992 USDT  15.31% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
