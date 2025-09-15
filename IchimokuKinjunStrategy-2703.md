# Freqtrade Automation Log

## Performance Indicator
**Status:** 🔴 RED  
**Description:** Poor Performance (Median: -0.61%, Total profit: -5.21%, Sortino: -1.26, Sharpe: -0.49, Calmar: -3.59, Drawdown: 0%)

---
            
**Strategy:** IchimokuKinjunStrategy  
**Random State:** 2703  
**Timestamp:** 2025-09-15 10:36:01

## Configuration
```json
{
  "strategy": "IchimokuKinjunStrategy",
  "timeframe": "1h",
  "hyperopt_loss": "SharpeHyperOptLoss",
  "spaces": "sell",
  "random_state": 2703,
  "epochs": 100,
  "hyperopt_timerange": "20170801-20191231",
  "backtest_timerange": "20220101-20221231"
}
```

## Hyperopt Command
```bash
docker compose run --rm freqtrade hyperopt -j 8 --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy IchimokuKinjunStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231 --random-state 2703
```

## Hyperopt Output
```

Best result:

    91/100:    164 trades. 46/0/118 Wins/Draws/Losses. Avg profit  -0.19%. Median profit  -0.61%. Total profit -103.32780238 USDT ( -10.33%). Avg duration 6:23:00 min. Objective: 0.27077

{"params":{"lookback_period_for_stoploss":10,"stoploss_margin":0.994,"take_profit_multiplier":1,"use_custom_stoploss_param":true},"minimal_roi":{},"stoploss":-0.1,"trailing_stop":false,"trailing_stop_positive":null,"trailing_stop_positive_offset":0.0,"trailing_only_offset_is_reached":false,"max_open_trades":3}

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
│ XRP/USDT │      9 │         0.37 │          10.634 │         1.06 │      2:59:00 │    4     0     5  44.4 │
│ BTC/USDT │     16 │         0.11 │           6.052 │         0.61 │      6:49:00 │    6     0    10  37.5 │
│ LTC/USDT │     17 │        -0.24 │         -13.165 │        -1.32 │      3:09:00 │    4     0    13  23.5 │
│ BNB/USDT │     17 │        -0.45 │         -25.408 │        -2.54 │      4:40:00 │    4     0    13  23.5 │
│ ETH/USDT │     13 │         -0.7 │         -30.236 │        -3.02 │      2:55:00 │    2     0    11  15.4 │
│    TOTAL │     72 │        -0.22 │         -52.122 │        -5.21 │      4:16:00 │   20     0    52  27.8 │
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
│     OTHER │      72 │        -0.22 │         -52.122 │        -5.21 │      4:16:00 │   20     0    52  27.8 │
│     TOTAL │      72 │        -0.22 │         -52.122 │        -5.21 │      4:16:00 │   20     0    52  27.8 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                EXIT REASON STATS                                                 
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ take_profit_1R │    17 │         2.59 │         144.262 │        14.43 │      6:37:00 │   17     0     0   100 │
│      stop_loss │     4 │        -2.64 │         -34.331 │        -3.43 │      8:40:00 │    0     0     4     0 │
│    exit_signal │    51 │        -0.96 │        -162.053 │       -16.21 │      3:08:00 │    3     0    48   5.9 │
│          TOTAL │    72 │        -0.22 │         -52.122 │        -5.21 │      4:16:00 │   20     0    52  27.8 │
└────────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                        MIXED TAG STATS                                                        
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃    Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │ take_profit_1R │     17 │         2.59 │         144.262 │        14.43 │      6:37:00 │   17     0     0   100 │
│           │      stop_loss │      4 │        -2.64 │         -34.331 │        -3.43 │      8:40:00 │    0     0     4     0 │
│           │    exit_signal │     51 │        -0.96 │        -162.053 │       -16.21 │      3:08:00 │    3     0    48   5.9 │
│     TOTAL │                │     72 │        -0.22 │         -52.122 │        -5.21 │      4:16:00 │   20     0    52  27.8 │
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
│ Total/Daily Avg Trades        │ 72 / 0.2                       │
│ Starting balance              │ 1000 USDT                      │
│ Final balance                 │ 947.878 USDT                   │
│ Absolute profit               │ -52.122 USDT                   │
│ Total profit %                │ -5.21%                         │
│ CAGR %                        │ -5.23%                         │
│ Sortino                       │ -1.26                          │
│ Sharpe                        │ -0.49                          │
│ Calmar                        │ -3.59                          │
│ SQN                           │ -1.09                          │
│ Profit factor                 │ 0.74                           │
│ Expectancy (Ratio)            │ -0.72 (-0.19)                  │
│ Avg. daily profit             │ -0.143 USDT                    │
│ Avg. stake amount             │ 328.448 USDT                   │
│ Total trade volume            │ 47339.014 USDT                 │
│                               │                                │
│ Best Pair                     │ XRP/USDT 1.06%                 │
│ Worst Pair                    │ ETH/USDT -3.02%                │
│ Best trade                    │ LTC/USDT 4.34%                 │
│ Worst trade                   │ BTC/USDT -3.86%                │
│ Best day                      │ 27.844 USDT                    │
│ Worst day                     │ -19.19 USDT                    │
│ Days win/draw/lose            │ 15 / 284 / 33                  │
│ Min/Max/Avg. Duration Winners │ 0d 01:10 / 1d 03:20 / 0d 06:31 │
│ Min/Max/Avg. Duration Losers  │ 0d 00:50 / 1d 04:50 / 0d 03:24 │
│ Max Consecutive Wins / Loss   │ 5 / 14                         │
│ Rejected Entry signals        │ 0                              │
│ Entry/Exit Timeouts           │ 0 / 0                          │
│                               │                                │
│ Min balance                   │ 947.878 USDT                   │
│ Max balance                   │ 1026.119 USDT                  │
│ Max % of account underwater   │ 7.62%                          │
│ Absolute drawdown             │ 78.241 USDT (7.62%)            │
│ Drawdown duration             │ 274 days 13:15:00              │
│ Profit at drawdown start      │ 26.119 USDT                    │
│ Profit at drawdown end        │ -52.122 USDT                   │
│ Drawdown start                │ 2022-03-27 21:45:00            │
│ Drawdown end                  │ 2022-12-27 11:00:00            │
│ Market change                 │ -59.72%                        │
└───────────────────────────────┴────────────────────────────────┘

Backtested 2022-01-01 00:00:00 -> 2022-12-31 00:00:00 | Max open trades : 3
                                                                STRATEGY SUMMARY                                                                
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃               Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃           Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ IchimokuKinjunStrategy │     72 │        -0.22 │         -52.122 │        -5.21 │      4:16:00 │   20     0    52  27.8 │ 78.241 USDT  7.62% │
└────────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴────────────────────┘

```
