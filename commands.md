# backtesting
Run backtesting for a given strategy and timeframe.

```bash
podman-compose run --rm freqtrade backtesting --config //freqtrade/user_data/config.json --strategy RSIDivergenceBullishStrategy --timeframe 1h --timeframe-detail 5m --datadir //freqtrade/user_data/data/binance --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20220101-20221231
```

# hyperopt

Run hyperoptimization for a given strategy and timeframe.

```bash
podman-compose run --rm freqtrade hyperopt --config //freqtrade/user_data/config.json --hyperopt-loss SharpeHyperOptLoss --strategy RSIDivergenceBullishStrategy --timeframe 1h --epochs 100 --spaces sell --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20180101-20191231


podman-compose run --rm freqtrade hyperopt --config //freqtrade/user_data/config.json --hyperopt-loss SharpeHyperOptLoss --strategy RSIDivergenceBullishStrategy --timeframe 1h --epochs 100 --spaces sell buy stoploss --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20180101-20191231

```

## 2017
```
podman-compose run --rm freqtrade hyperopt --config //freqtrade/user_data/config.json --hyperopt-loss SharpeHyperOptLoss --strategy RSIDivergenceBullishStrategy --timeframe 1h --timeframe-detail 5m --epochs 200 --spaces buy sell trades --pairs BTC/USDT ETH/USDT LTC/USDT XRP/USDT BNB/USDT --timerange 20170101-20171231


```

