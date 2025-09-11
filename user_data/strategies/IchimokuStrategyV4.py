# pragma pylint: disable=missing-docstring, invalid-name, pointless-string-statement

# --- Do not remove these libs ---
import datetime
import numpy as np  # noqa
import pandas as pd  # noqa
from pandas import DataFrame

from freqtrade.strategy.interface import IStrategy
from freqtrade.persistence import Trade
from freqtrade.strategy.informative_decorator import informative

# --------------------------------
# Add your lib to import here
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib


class IchimokuStrategyV4(IStrategy):
    """
    This is a strategy template to get you started.
    More information in https://github.com/freqtrade/freqtrade/blob/develop/docs/bot-optimization.md

    You can:
        :return: a Dataframe with all mandatory indicators for the strategies
    - Rename the class name (Do not forget to update class_name)
    - Add any methods you want to build your strategy
    - Add any lib you need to build your strategy

    You must keep:
    - the lib in the section "Do not remove these libs"
    - the prototype for the methods: minimal_roi, stoploss, populate_indicators, populate_buy_trend,
    populate_sell_trend, hyperopt_space, buy_strategy_generator
    """

    # Minimal ROI designed for the strategy.
    # This attribute will be overridden if the config file contains "minimal_roi".
    # minimal_roi = {
    #     "0": 0.45,
    #     "120": 0.20,
    #     "420": 0.07,
    #     "540" : 0
    # }
    minimal_roi = {
         "0": 2
    }

    # Optimal stoploss designed for the strategy.
    # This attribute will be overridden if the config file contains "stoploss".
    stoploss = -0.1

    # Trailing stoploss
    trailing_stop = False
    trailing_only_offset_is_reached = True 
    trailing_stop_positive = 0.01
    trailing_stop_positive_offset = 0.017

    # Optimal ticker interval for the strategy.
    ticker_interval = '1h'

    # Run "populate_indicators()" only for new candle.
    process_only_new_candles = False

    # These values can be overridden in the "ask_strategy" section in the config.
    use_sell_signal = True
    sell_profit_only = False
    ignore_roi_if_buy_signal = False

    use_custom_stoploss = True

    # Number of candles the strategy requires before producing valid signals
    startup_candle_count: int = 150

    timeframe = '1h'

    @property
    def protections(self):
        return  [
            {
                "method": "CooldownPeriod",
                "stop_duration_candles": 14
            }
        ]

    # Optional order type mapping.
    order_types = {
        'buy': 'limit',
        'sell': 'limit',
        'stoploss': 'market',
        'stoploss_on_exchange': True
    }

    # Optional order time in force.
    order_time_in_force = {
        'buy': 'gtc',
        'sell': 'gtc'
    }

    plot_config = {
        'main_plot': {
            # Configuration for main plot indicators.
            # Specifies `ema10` to be red, and `ema50` to be a shade of gray
            'ichimoku-tenkan': {'color': 'red'},
            'ichimoku-kinjun': {'color': 'blue'},
            # By omitting color, a random color is selected.
            'sma150': {'color': 'black'},
            # fill area between senkou_a and senkou_b
            'ichimoku-spanA': {
                'color': 'lightgreen', #optional
                'fill_to': 'ichimoku-spanB',
                'fill_label': 'Ichimoku Cloud', #optional
                'fill_color': 'rgba(255,76,46,0.2)', #optional
            },
            # plot senkou_b, too. Not only the area to it.
            'ichimoku-spanB': {'color': 'darkgreen'}
        },
        'subplots': {
            # Create subplot MACD
            "STOCH": {
                'slowd':{},
                'slowk':{}
            },
            "Nuage": {
                'ichimoku-futur': {'color': 'black'}
            },
            'ichimoku-tenkan-distance': {
                'ichimoku-tenkan-distance':{}
            }
            # Additional subplot RSI
            # "RSI": {
            #     'rsi': {'color': 'red'}
            # }
        }
    }

    def informative_pairs(self):
        """
        Define additional, informative pair/interval combinations to be cached from the exchange.
        These pair/interval combinations are non-tradeable, unless they are part
        of the whitelist as well.
        For more information, please consult the documentation
        :return: List of tuples in the format (pair, interval)
            Sample: return [("ETH/USDT", "5m"),
                            ("BTC/USDT", "15m"),
                            ]
        """
        return []

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Adds several different TA indicators to the given DataFrame

        Performance Note: For the best performance be frugal on the number of indicators
        you are using. Let uncomment only the indicator you are using in your strategies
        or your hyperopt configuration, otherwise you will waste your memory and CPU usage.
        :param dataframe: Raw data from the exchange and parsed by parse_ticker_dataframe()
        :param metadata: Additional information, like the currently traded pair
        :return: a Dataframe with all mandatory indicators for the strategies
        """
        
        # dataframe['stoploss'] = (dataframe['low']).rolling(window=20).min().mul(0.98)

        # Volume
        dataframe['volume_sma5'] = dataframe['volume'].rolling(window=5).mean()

        # Momentum Indicators
        # ------------------------------------

        # for val in self.buy_sma.range:
        #     dataframe[f'buy_sma_{val}'] = ta.SMA(dataframe, timeperiod=val)

        # RSI
        dataframe['rsi'] = ta.RSI(dataframe)

        # Candle-size
        dataframe['candle-top'] = dataframe[['open','close']].max(axis=1)
        dataframe['candle-bottom'] = dataframe[['open','close']].min(axis=1)
        dataframe['candle-size'] = ((dataframe['candle-top'] - dataframe['candle-bottom']) / dataframe['candle-bottom']) * 100
        dataframe['candle-top-shadow'] = ((dataframe['high'] - dataframe['candle-top']) / dataframe['candle-top']) * 100
        dataframe['candle-bottom-shadow'] = ((dataframe['candle-bottom'] - dataframe['low']) / dataframe['candle-bottom']) * 100

        #Ichimoku
        dataframe['ichimoku-tenkan'] = ((dataframe['high'].rolling(window=9).max()) + (dataframe['low'].rolling(window=9).min())) / 2
        dataframe['ichimoku-kinjun'] = ((dataframe['high'].rolling(window=26).max()) + (dataframe['low'].rolling(window=26).min())) / 2
        dataframe['ichimoku-spanA'] = ((dataframe['ichimoku-tenkan']) + (dataframe['ichimoku-kinjun'])).shift(26) / 2
        dataframe['ichimoku-spanB'] = ((dataframe['high'].rolling(window=52).max()) + (dataframe['low'].rolling(window=52).min())).shift(26) / 2
        dataframe['ichimoku-chiku'] = (dataframe['close'].shift(-26))
      
        dataframe['ichimoku-spanA-futur'] = ((dataframe['ichimoku-tenkan']) + (dataframe['ichimoku-kinjun'])) / 2
        dataframe['ichimoku-spanB-futur'] = ((dataframe['high'].rolling(window=52).max()) + (dataframe['low'].rolling(window=52).min())) / 2
        dataframe['ichimoku-futur'] = (dataframe['ichimoku-spanA-futur'] > dataframe['ichimoku-spanB-futur'])

        stoch = ta.STOCH(dataframe, fastk_period=5 )
        dataframe['slowd'] = stoch['slowd']
        dataframe['slowk'] = stoch['slowk']

        dataframe['stoploss'] = dataframe['ichimoku-kinjun'] * 0.9975

        dataframe['tenkan_kinjun_gap'] = (dataframe['ichimoku-tenkan'] - dataframe['ichimoku-kinjun']) / dataframe['ichimoku-kinjun']
        dataframe['close_tenkan_gap'] = (dataframe['close'] - dataframe['ichimoku-tenkan']) / dataframe['ichimoku-tenkan']
        dataframe['close_kinjun_gap'] = (dataframe['close'] - dataframe['ichimoku-kinjun']) / dataframe['ichimoku-kinjun']
        dataframe['close_tenkan_gap_sup'] = dataframe['close_tenkan_gap'] >= 0.06

        # Retrieve best bid and best ask from the orderbook
        # ------------------------------------
        """
        # first check if dataprovider is available
        if self.dp:
            if self.dp.runmode in ('live', 'dry_run'):
                ob = self.dp.orderbook(metadata['pair'], 1)
                dataframe['best_bid'] = ob['bids'][0][0]
                dataframe['best_ask'] = ob['asks'][0][0]
        """

        return dataframe

    @informative('1d')
    # @informative('1d', 'BTC/{stake}', fmt='{base}_{column}_{timeframe}')
    def populate_indicators_1d(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        #Ichimoku
        dataframe['ichimoku-tenkan'] = ((dataframe['high'].rolling(window=9).max()) + (dataframe['low'].rolling(window=9).min())) / 2
        dataframe['ichimoku-kinjun'] = ((dataframe['high'].rolling(window=26).max()) + (dataframe['low'].rolling(window=26).min())) / 2
        dataframe['ichimoku-spanA'] = ((dataframe['ichimoku-tenkan']) + (dataframe['ichimoku-kinjun'])).shift(26) / 2
        dataframe['ichimoku-spanB'] = ((dataframe['high'].rolling(window=52).max()) + (dataframe['low'].rolling(window=52).min())).shift(26) / 2
        dataframe['ichimoku-chiku'] = (dataframe['close'].shift(-26))
        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Based on TA indicators, populates the buy signal for the given dataframe
        :param dataframe: DataFrame populated with indicators
        :param metadata: Additional information, like the currently traded pair
        :return: DataFrame with buy column
        """
        dataframe.loc[
            (
                (dataframe['ichimoku-tenkan'] >= dataframe['ichimoku-kinjun']) &
                (dataframe['ichimoku-tenkan'].shift(3) < dataframe['ichimoku-tenkan']) &
                (dataframe['close'] > dataframe['ichimoku-kinjun']) &
                # (dataframe['ichimoku-spanA-futur'] > dataframe['ichimoku-spanB-futur']) &
                # (dataframe['close'] > dataframe['ichimoku-spanA']) &
                (dataframe['close'] > dataframe['ichimoku-spanB']) &
                (dataframe['close_1d'] > dataframe['ichimoku-kinjun_1d']) &
                # (dataframe['close'] > dataframe['close'].shift(26)) &
                (dataframe['slowk'] > dataframe['slowd']) #&
                # (dataframe['close_tenkan_gap'] < 0.06)
                # (dataframe['close'] > dataframe['sma150']) # &
                # (dataframe['slowk'] < 50) &
                # (dataframe['close'] > dataframe['ichimoku-spanA-daily']) &
                # (dataframe['close'] > dataframe['ichimoku-spanB-daily']) &
                # ((dataframe['close_1d'] > dataframe['ichimoku-spanA_1d']) | (dataframe['close_1d'] > dataframe['ichimoku-spanB_1d'])) &
                # (dataframe['ichimoku-spanA'] <= dataframe['ichimoku-spanB']) &
                # (dataframe['close'] > dataframe['ichimoku-tenkan']) &
                # (dataframe['close'] > dataframe['ema200'])
                # ((qtpylib.crossed_above(dataframe['close'], dataframe['ichimoku-kinjun'])) | (qtpylib.crossed_above(dataframe['close'], dataframe['ichimoku-tenkan'])))
            ),
            'buy'] = 1
        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Based on TA indicators, populates the sell signal for the given dataframe
        :param dataframe: DataFrame populated with indicators
        :param metadata: Additional information, like the currently traded pair
        :return: DataFrame with buy column
        """
        dataframe.loc[
            (   
                (qtpylib.crossed_below(dataframe['close'], dataframe['ichimoku-kinjun'])) 
            ),
            'sell'] = 1
        return dataframe


    def custom_stoploss(self, pair: str, trade: Trade, current_time: datetime,
                        current_rate: float, current_profit: float, **kwargs) -> float:
        dataframe, _ = self.dp.get_analyzed_dataframe(pair, self.timeframe)
        last_candle = dataframe.iloc[-1].squeeze()
        stoploss_price = last_candle['stoploss']
        if trade.initial_stop_loss >= trade.stop_loss:
            sl = (stoploss_price / current_rate) - 1
            return sl
        return 1

    def custom_stake_amount(self, pair: str, current_time: datetime, current_rate: float,
                            proposed_stake: float, min_stake: float, max_stake: float,
                            **kwargs) -> float:
        dataframe, _ = self.dp.get_analyzed_dataframe(pair=pair, timeframe=self.timeframe)
        current_candle = dataframe.iloc[-1].squeeze()

        stoploss_price = current_candle['stoploss']
        stop_distance = current_rate - stoploss_price
        K = max_stake
        stake = (K / 100) / stop_distance * current_rate

        if stake > max_stake:
            return max_stake

        return stake


    def getNbR(self, pair: str, trade: Trade, current_rate: float) -> float:
        r = trade.open_rate - trade.stop_loss
        if r != 0:
            return (current_rate - trade.open_rate) / r
        else:
            return 0


    def custom_sell(self, pair: str, trade: Trade, current_time: 'datetime', current_rate: float,
                    current_profit: float, **kwargs):
        dataframe, _ = self.dp.get_analyzed_dataframe(pair, self.timeframe)
        last_candle = dataframe.iloc[-1].squeeze()
        previous_candle = dataframe.iloc[-2].squeeze()
        if current_profit > 0.05:
        # if self.getNbR(pair, trade, current_rate) >= 5:
            if last_candle['ichimoku-tenkan'] < previous_candle['ichimoku-tenkan']:
                return 'tenkan-weakness'


### Meilleurs Résultats

#0.05: 3823 cooldown 12
#0.05: 3907 cooldown 13
#0.05: 4313 cooldown 14

#multitimeframe=false, 6634, drawdown=264%
#multitimeframe=true(close>kinjun), 7249%, drawdown=151%