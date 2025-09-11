# download data

```bash

docker compose run --rm freqtrade download-data --config //freqtrade/user_data/config.json --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timeframes 5m 15m 1h 4h 1d 1w --timerange 20170801- 

```

# lookahead analysis

```bash
docker compose run --rm freqtrade lookahead-analysis --config //freqtrade/user_data/config.json --strategy RSIDivergenceBullishStrategy --timeframe 1h --timeframe-detail 5m  --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20221231 --backtest-filename backtest-result-2025-09-10_13-34-10.meta.json
```

# backtesting
Run backtesting for a given strategy and timeframe.

```bash
podman-compose run --rm freqtrade backtesting --config //freqtrade/user_data/config.json --strategy RSIDivergenceBullishStrategy --timeframe 1h --timeframe-detail 5m --datadir //freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20221231 
```

# hyperopt

Run hyperoptimization for a given strategy and timeframe.

```bash
podman-compose run --rm freqtrade hyperopt --config //freqtrade/user_data/config.json --hyperopt-loss SharpeHyperOptLoss --strategy RSIDivergenceBullishStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20180101-20191231


docker compose run --rm freqtrade hyperopt --config /freqtrade/user_data/config.json --print-json --hyperopt-loss SharpeHyperOptLoss --strategy RSIDivergenceBullishStrategy --timeframe 1h --epochs 100 --spaces sell buy --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170801-20191231  --random-state 10

```

## 2017

```bash
podman-compose run --rm freqtrade hyperopt --config //freqtrade/user_data/config.json --hyperopt-loss SharpeHyperOptLoss --strategy RSIDivergenceBullishStrategy --timeframe 1h --timeframe-detail 5m --epochs 200 --spaces buy sell trades --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170101-20171231


```

