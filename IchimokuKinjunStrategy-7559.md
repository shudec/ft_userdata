# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Median Profit: -0.63%, Profit Factor: 0.97)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 7559  
**Timestamp:** 2025-09-14 21:15:31

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 7559,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 7559
```

## Hyperopt Output
```

Best result:

    45/100:    759 trades. 152/0/607 Wins/Draws/Losses. Avg profit  -0.12%. Median profit  -0.63%. Total profit -288.39886140 USDT ( -28.84%). Avg duration 8:09:00 min. Objective: 0.64572

{"params":{"lookback_period_for_stoploss":9,"stoploss_margin":0.99,"take_profit_multiplier":3,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ LTC/USDT │     75 │         0.08 │          15.708 │         1.57 │     10:02:00 │   22     0    53  29.3 │
│ ETH/USDT │     72 │         0.07 │          14.002 │          1.4 │      7:27:00 │   18     0    54  25.0 │
│ BTC/USDT │     67 │         0.05 │           8.035 │          0.8 │      7:18:00 │   15     0    52  22.4 │
│ XRP/USDT │     63 │        -0.05 │         -10.366 │        -1.04 │      5:46:00 │   18     0    45  28.6 │
│ BNB/USDT │     72 │        -0.21 │         -57.614 │        -5.76 │      7:53:00 │   14     0    58  19.4 │
│    TOTAL │    349 │        -0.01 │         -30.235 │        -3.02 │      7:46:00 │   87     0   262  24.9 │
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
│     OTHER │     349 │        -0.01 │         -30.235 │        -3.02 │      7:46:00 │   87     0   262  24.9 │
│     TOTAL │     349 │        -0.01 │         -30.235 │        -3.02 │      7:46:00 │   87     0   262  24.9 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │    22 │         6.73 │         498.193 │        49.82 │     15:12:00 │   22     0     0   100 │
│      stop_loss │    10 │        -2.71 │         -92.748 │        -9.27 │      1:12:00 │    0     0    10     0 │
│    exit_signal │   317 │        -0.39 │        -435.680 │       -43.57 │      7:27:00 │   65     0   252  20.5 │
│          TOTAL │   349 │        -0.01 │         -30.235 │        -3.02 │      7:46:00 │   87     0   262  24.9 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_3R │     22 │         6.73 │         498.193 │        49.82 │     15:12:00 │   22     0     0   100 │
│           │      stop_loss │     10 │        -2.71 │         -92.748 │        -9.27 │      1:12:00 │    0     0    10     0 │
│           │    exit_signal │    317 │        -0.39 │        -435.680 │       -43.57 │      7:27:00 │   65     0   252  20.5 │
│     TOTAL │                │    349 │        -0.01 │         -30.235 │        -3.02 │      7:46:00 │   87     0   262  24.9 │
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
│ Total/Daily Avg Trades        │ 349 / 0.96                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 969.765 USDT                   │
│ Absolute profit               │ -30.235 USDT                   │
│ Total profit %                │ -3.02%                         │
│ CAGR %                        │ -3.03%                         │
│ Sortino                       │ -0.55                          │
│ Sharpe                        │ -0.20                          │
│ Calmar                        │ -0.93                          │
│ SQN                           │ -0.21                          │
│ Profit factor                 │ 0.97                           │
│ Expectancy (Ratio)            │ -0.09 (-0.03)                  │
│ Avg. daily profit             │ -0.083 USDT                    │
│ Avg. stake amount             │ 344.169 USDT                   │
│ Total trade volume            │ 240680.646 USDT                │
│                               │                                │
│ Best Pair                     │ LTC/USDT 1.57%                 │
│ Worst Pair                    │ BNB/USDT -5.76%                │
│ Best trade                    │ BTC/USDT 9.86%                 │
│ Worst trade                   │ BNB/USDT -7.54%                │
│ Best day                      │ 64.77 USDT                     │
│ Worst day                     │ -27.06 USDT                    │
│ Days win/draw/lose            │ 40 / 211 / 107                 │
│ Min/Max/Avg. Duration Winners │ 0d 00:35 / 1d 19:00 / 0d 19:31 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:00 / 1d 05:00 / 0d 03:52 │
│ Max Consecutive Wins / Loss   │ 4 / 15                         │
│ Rejected Entry signals        │ 108                            │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 952.754 USDT                   │
│ Max balance                   │ 1148.704 USDT                  │
│ Max % of account underwater   │ 17.06%                         │
│ Absolute Drawdown (Account)   │ 17.06%                         │
│ Absolute Drawdown             │ 195.95 USDT                    │
│ Drawdown high                 │ 148.704 USDT                   │
│ Drawdown low                  │ -47.246 USDT                   │
│ Drawdown Start                │ 2022-07-15 01:20:00            │
│ Drawdown End                  │ 2022-10-25 09:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃            Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │    349 │        -0.01 │         -30.235 │        -3.02 │      7:46:00 │   87     0   262  24.9 │ 195.95 USDT  17.06% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴─────────────────────┘

```
