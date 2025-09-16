# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 272 / 0.75, Median: -0.61%, Total profit: -9.87%, Sortino: -1.29, Sharpe: -0.64, Calmar: -3.13, Drawdown: 0%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 3718  
**Timestamp:** 2025-09-16 11:17:27

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "buy sell",
  "random_state": 3718,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces buy sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 3718
```

## Hyperopt Output
```

Best result:

    80/100:    621 trades. 140/0/481 Wins/Draws/Losses. Avg profit   0.40%. Median profit  -0.61%. Total profit 973.25924859 USDT (  97.33%). Avg duration 13:05:00 min. Objective: -0.78733

{"params":{"rsi_entry_max":55,"rsi_entry_min":15,"volume_factor":0.573,"stoploss_margin":0.999,"lookback_period_for_stoploss":0,"take_profit_multiplier":1,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ XRP/USDT │     51 │         0.65 │         106.370 │        10.64 │     15:03:00 │   17     0    34  33.3 │
│ BTC/USDT │     57 │        -0.07 │         -13.764 │        -1.38 │     11:41:00 │   14     0    43  24.6 │
│ ETH/USDT │     50 │        -0.28 │         -47.931 │        -4.79 │      7:38:00 │    8     0    42  16.0 │
│ LTC/USDT │     53 │        -0.36 │         -63.562 │        -6.36 │     15:50:00 │   17     0    36  32.1 │
│ BNB/USDT │     61 │         -0.4 │         -79.825 │        -7.98 │      9:06:00 │    9     0    52  14.8 │
│    TOTAL │    272 │         -0.1 │         -98.712 │        -9.87 │     11:48:00 │   65     0   207  23.9 │
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
│     OTHER │     272 │         -0.1 │         -98.712 │        -9.87 │     11:48:00 │   65     0   207  23.9 │
│     TOTAL │     272 │         -0.1 │         -98.712 │        -9.87 │     11:48:00 │   65     0   207  23.9 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS                                                  
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │     8 │         8.86 │         229.677 │        22.97 │ 1 day, 0:19:00 │    8     0     0   100 │
│      stop_loss │     2 │        -6.32 │         -41.019 │         -4.1 │       11:00:00 │    0     0     2     0 │
│    exit_signal │   262 │        -0.33 │        -287.370 │       -28.74 │       11:26:00 │   57     0   205  21.8 │
│          TOTAL │   272 │         -0.1 │         -98.712 │        -9.87 │       11:48:00 │   65     0   207  23.9 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                                         MIXED TAG STATS                                                         
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1R │      8 │         8.86 │         229.677 │        22.97 │ 1 day, 0:19:00 │    8     0     0   100 │
│           │      stop_loss │      2 │        -6.32 │         -41.019 │         -4.1 │       11:00:00 │    0     0     2     0 │
│           │    exit_signal │    262 │        -0.33 │        -287.370 │       -28.74 │       11:26:00 │   57     0   205  21.8 │
│     TOTAL │                │    272 │         -0.1 │         -98.712 │        -9.87 │       11:48:00 │   65     0   207  23.9 │
└───────────┴────────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                         SUMMARY METRICS                          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                        ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from              │ 2022-01-01 00:00:00            │
│ Backtesting to                │ 2022-12-31 00:00:00            │
│ Trading Mode                  │ Spot                           │
│ Max open trades               │ 3                              │
│                               │                                │
│ Total/Daily Avg Trades        │ 272 / 0.75                     │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 901.288 USDT                   │
│ Absolute profit               │ -98.712 USDT                   │
│ Total profit %                │ -9.87%                         │
│ CAGR %                        │ -9.90%                         │
│ Sortino                       │ -1.29                          │
│ Sharpe                        │ -0.64                          │
│ Calmar                        │ -3.13                          │
│ SQN                           │ -0.74                          │
│ Profit factor                 │ 0.85                           │
│ Expectancy (Ratio)            │ -0.36 (-0.11)                  │
│ Avg. daily profit             │ -0.271 USDT                    │
│ Avg. stake amount             │ 326.008 USDT                   │
│ Total trade volume            │ 177604.51 USDT                 │
│                               │                                │
│ Best Pair                     │ XRP/USDT 10.64%                │
│ Worst Pair                    │ BNB/USDT -7.98%                │
│ Best trade                    │ XRP/USDT 17.82%                │
│ Worst trade                   │ LTC/USDT -11.18%               │
│ Best day                      │ 59.552 USDT                    │
│ Worst day                     │ -37.901 USDT                   │
│ Days win/draw/lose            │ 37 / 213 / 107                 │
│ Min/Max/Avg. Duration Winners │ 0d 03:00 / 2d 21:35 / 1d 00:33 │
│ Min/Max/Avg. Duration Losers  │ 0d 01:00 / 4d 09:00 / 0d 07:48 │
│ Max Consecutive Wins / Loss   │ 4 / 15                         │
│ Rejected Entry signals        │ 48                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 901.288 USDT                   │
│ Max balance                   │ 1079.837 USDT                  │
│ Max % of account underwater   │ 16.53%                         │
│ Absolute drawdown             │ 178.549 USDT (16.53%)          │
│ Drawdown duration             │ 139 days 23:00:00              │
│ Profit at drawdown start      │ 79.837 USDT                    │
│ Profit at drawdown end        │ -98.712 USDT                   │
│ Drawdown start                │ 2022-08-09 02:00:00            │
│ Drawdown end                  │ 2022-12-27 01:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │    272 │        -0.10 │         -98.712 │        -9.87 │     11:48:00 │   65     0   207  23.9 │ 178.549 USDT  16.53% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
