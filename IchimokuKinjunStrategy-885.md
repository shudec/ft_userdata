# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 1219 / 3.35, Median: -0.66%, Total profit: -61.6%, Sortino: -11.95, Sharpe: -5.87, Calmar: -5.15, Drawdown: 0%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 885  
**Timestamp:** 2025-09-15 18:36:27

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 885,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 885
```

## Hyperopt Output
```

Best result:

*    4/100:   2698 trades. 660/0/2038 Wins/Draws/Losses. Avg profit  -0.05%. Median profit  -0.66%. Total profit -605.14218654 USDT ( -60.51%). Avg duration 13:49:00 min. Objective: 0.81541

{"params":{"stoploss_margin":1.0,"lookback_period_for_stoploss":0,"take_profit_multiplier":1,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ ETH/USDT │    263 │         -0.1 │         -51.259 │        -5.13 │     13:01:00 │   63     0   200  24.0 │
│ LTC/USDT │    265 │        -0.08 │        -104.134 │       -10.41 │     13:21:00 │   64     0   201  24.2 │
│ BNB/USDT │    191 │        -0.28 │        -133.108 │       -13.31 │     12:39:00 │   40     0   151  20.9 │
│ XRP/USDT │    207 │        -0.39 │        -153.828 │       -15.38 │     12:36:00 │   43     0   164  20.8 │
│ BTC/USDT │    293 │        -0.27 │        -173.700 │       -17.37 │     12:17:00 │   66     0   227  22.5 │
│    TOTAL │   1219 │        -0.21 │        -616.029 │        -61.6 │     12:47:00 │  276     0   943  22.6 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                           LEFT OPEN TRADES REPORT                                           
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ LTC/USDT │      1 │         1.25 │           1.572 │         0.16 │      9:00:00 │    1     0     0   100 │
│ BTC/USDT │      1 │         0.11 │           0.145 │         0.01 │      8:00:00 │    1     0     0   100 │
│ ETH/USDT │      1 │        -0.01 │          -0.010 │         -0.0 │     21:00:00 │    0     0     1     0 │
│    TOTAL │      3 │         0.45 │           1.707 │         0.17 │     12:40:00 │    2     0     1  66.7 │
└──────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                ENTER TAG STATS                                                
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│     OTHER │    1219 │        -0.21 │        -616.029 │        -61.6 │     12:47:00 │  276     0   943  22.6 │
│     TOTAL │    1219 │        -0.21 │        -616.029 │        -61.6 │     12:47:00 │  276     0   943  22.6 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │    39 │         7.94 │         552.167 │        55.22 │     21:53:00 │   39     0     0   100 │
│     force_exit │     3 │         0.45 │           1.707 │         0.17 │     12:40:00 │    2     0     1  66.7 │
│      stop_loss │    14 │        -6.71 │        -178.879 │       -17.89 │     13:39:00 │    0     0    14     0 │
│    exit_signal │  1163 │        -0.41 │        -991.024 │        -99.1 │     12:28:00 │  235     0   928  20.2 │
│          TOTAL │  1219 │        -0.21 │        -616.029 │        -61.6 │     12:47:00 │  276     0   943  22.6 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1R │     39 │         7.94 │         552.167 │        55.22 │     21:53:00 │   39     0     0   100 │
│           │     force_exit │      3 │         0.45 │           1.707 │         0.17 │     12:40:00 │    2     0     1  66.7 │
│           │      stop_loss │     14 │        -6.71 │        -178.879 │       -17.89 │     13:39:00 │    0     0    14     0 │
│           │    exit_signal │   1163 │        -0.41 │        -991.024 │        -99.1 │     12:28:00 │  235     0   928  20.2 │
│     TOTAL │                │   1219 │        -0.21 │        -616.029 │        -61.6 │     12:47:00 │  276     0   943  22.6 │
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
│ Total/Daily Avg Trades        │ 1219 / 3.35                    │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 383.971 USDT                   │
│ Absolute profit               │ -616.029 USDT                  │
│ Total profit %                │ -61.60%                        │
│ CAGR %                        │ -61.70%                        │
│ Sortino                       │ -11.95                         │
│ Sharpe                        │ -5.87                          │
│ Calmar                        │ -5.15                          │
│ SQN                           │ -3.20                          │
│ Profit factor                 │ 0.74                           │
│ Expectancy (Ratio)            │ -0.51 (-0.20)                  │
│ Avg. daily profit             │ -1.692 USDT                    │
│ Avg. stake amount             │ 199.126 USDT                   │
│ Total trade volume            │ 485822.689 USDT                │
│                               │                                │
│ Best Pair                     │ ETH/USDT -5.13%                │
│ Worst Pair                    │ BTC/USDT -17.37%               │
│ Best trade                    │ XRP/USDT 25.31%                │
│ Worst trade                   │ XRP/USDT -17.51%               │
│ Best day                      │ 46.529 USDT                    │
│ Worst day                     │ -57.916 USDT                   │
│ Days win/draw/lose            │ 105 / 50 / 209                 │
│ Min/Max/Avg. Duration Winners │ 0d 03:00 / 3d 14:00 / 1d 04:31 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 4d 09:00 / 0d 08:11 │
│ Max Consecutive Wins / Loss   │ 4 / 28                         │
│ Rejected Entry signals        │ 7208                           │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 378.32 USDT                    │
│ Max balance                   │ 1015.491 USDT                  │
│ Max % of account underwater   │ 62.75%                         │
│ Absolute drawdown             │ 637.171 USDT (62.75%)          │
│ Drawdown duration             │ 323 days 13:00:00              │
│ Profit at drawdown start      │ 15.491 USDT                    │
│ Profit at drawdown end        │ -621.68 USDT                   │
│ Drawdown start                │ 2022-01-02 17:00:00            │
│ Drawdown end                  │ 2022-11-22 06:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │   1219 │        -0.21 │        -616.029 │        -61.6 │     12:47:00 │  276     0   943  22.6 │ 637.171 USDT  62.75% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
