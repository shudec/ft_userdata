# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Total trades: 290 / 0.8, Median: -0.62%, Total profit: -7.21%, Sortino: -1.47, Sharpe: -0.53, Calmar: -2.75, Drawdown: 0%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 1358  
**Timestamp:** 2025-09-15 15:09:20

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 1358,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 1358
```

## Hyperopt Output
```

Best result:

*    9/100:    643 trades. 123/0/520 Wins/Draws/Losses. Avg profit  -0.13%. Median profit  -0.62%. Total profit -268.14904122 USDT ( -26.81%). Avg duration 7:18:00 min. Objective: 0.58540

{"params":{"lookback_period_for_stoploss":10,"stoploss_margin":0.99,"take_profit_multiplier":3,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ ETH/USDT │     58 │         0.26 │          48.455 │         4.85 │      7:13:00 │   14     0    44  24.1 │
│ XRP/USDT │     53 │         -0.1 │         -18.008 │         -1.8 │      6:03:00 │   16     0    37  30.2 │
│ BTC/USDT │     57 │        -0.13 │         -25.662 │        -2.57 │      6:11:00 │   12     0    45  21.1 │
│ BNB/USDT │     60 │        -0.13 │         -30.028 │         -3.0 │      8:22:00 │   12     0    48  20.0 │
│ LTC/USDT │     62 │        -0.23 │         -46.891 │        -4.69 │      7:49:00 │   14     0    48  22.6 │
│    TOTAL │    290 │        -0.07 │         -72.135 │        -7.21 │      7:10:00 │   68     0   222  23.4 │
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
│     OTHER │     290 │        -0.07 │         -72.135 │        -7.21 │      7:10:00 │   68     0   222  23.4 │
│     TOTAL │     290 │        -0.07 │         -72.135 │        -7.21 │      7:10:00 │   68     0   222  23.4 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_3R │    17 │         7.16 │         392.426 │        39.24 │     17:46:00 │   17     0     0   100 │
│      stop_loss │     8 │        -2.46 │         -65.299 │        -6.53 │      1:31:00 │    0     0     8     0 │
│    exit_signal │   265 │        -0.46 │        -399.262 │       -39.93 │      6:39:00 │   51     0   214  19.2 │
│          TOTAL │   290 │        -0.07 │         -72.135 │        -7.21 │      7:10:00 │   68     0   222  23.4 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_3R │     17 │         7.16 │         392.426 │        39.24 │     17:46:00 │   17     0     0   100 │
│           │      stop_loss │      8 │        -2.46 │         -65.299 │        -6.53 │      1:31:00 │    0     0     8     0 │
│           │    exit_signal │    265 │        -0.46 │        -399.262 │       -39.93 │      6:39:00 │   51     0   214  19.2 │
│     TOTAL │                │    290 │        -0.07 │         -72.135 │        -7.21 │      7:10:00 │   68     0   222  23.4 │
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
│ Total/Daily Avg Trades        │ 290 / 0.8                      │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 927.865 USDT                   │
│ Absolute profit               │ -72.135 USDT                   │
│ Total profit %                │ -7.21%                         │
│ CAGR %                        │ -7.23%                         │
│ Sortino                       │ -1.47                          │
│ Sharpe                        │ -0.53                          │
│ Calmar                        │ -2.75                          │
│ SQN                           │ -0.59                          │
│ Profit factor                 │ 0.89                           │
│ Expectancy (Ratio)            │ -0.25 (-0.08)                  │
│ Avg. daily profit             │ -0.198 USDT                    │
│ Avg. stake amount             │ 328.508 USDT                   │
│ Total trade volume            │ 190844.084 USDT                │
│                               │                                │
│ Best Pair                     │ ETH/USDT 4.85%                 │
│ Worst Pair                    │ LTC/USDT -4.69%                │
│ Best trade                    │ ETH/USDT 12.52%                │
│ Worst trade                   │ BNB/USDT -7.54%                │
│ Best day                      │ 54.205 USDT                    │
│ Worst day                     │ -27.035 USDT                   │
│ Days win/draw/lose            │ 35 / 226 / 97                  │
│ Min/Max/Avg. Duration Winners │ 0d 01:55 / 1d 21:30 / 0d 18:32 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:20 / 1d 05:00 / 0d 03:41 │
│ Max Consecutive Wins / Loss   │ 4 / 14                         │
│ Rejected Entry signals        │ 84                             │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 927.865 USDT                   │
│ Max balance                   │ 1076.142 USDT                  │
│ Max % of account underwater   │ 13.78%                         │
│ Absolute drawdown             │ 148.277 USDT (13.78%)          │
│ Drawdown duration             │ 173 days 02:30:00              │
│ Profit at drawdown start      │ 76.142 USDT                    │
│ Profit at drawdown end        │ -72.135 USDT                   │
│ Drawdown start                │ 2022-07-08 01:30:00            │
│ Drawdown end                  │ 2022-12-28 04:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                 STRATEGY SUMMARY                                                                 
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │    290 │        -0.07 │         -72.135 │        -7.21 │      7:10:00 │   68     0   222  23.4 │ 148.277 USDT  13.78% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘

```
