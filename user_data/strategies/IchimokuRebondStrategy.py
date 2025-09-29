# pragma pylint: disable=missing-docstring, invalid-name, pointless-string-statement
# flake8: noqa: F401
# isort: skip_file
# --- Do not remove these libs ---
import datetime
import os
import numpy as np  # noqa
import pandas as pd  # noqa
from pandas import DataFrame

from freqtrade.strategy import (
    BooleanParameter,
    CategoricalParameter,
    DecimalParameter,
    IStrategy,
    IntParameter,
    Trade,
    stoploss_from_absolute,
)

# --------------------------------
# Add your lib to import here
import talib.abstract as ta
from freqtrade.strategy.informative_decorator import informative
import freqtrade.vendor.qtpylib.indicators as qtpylib


class IchimokuRebondStrategy(IStrategy):
    """
    Stratégie basée sur la divergence RSI haussière
    - Achat : divergence RSI bullish + bougie verte importante
    - Stop Loss : sous la bougie la plus basse ayant créé la divergence
    - Take Profit : 2 fois le risque (ratio 1:2)
    """

    # Strategy interface version - allow new iterations of the strategy interface.
    INTERFACE_VERSION = 3

    # Optimal timeframe for the strategy.
    timeframe = "1h"

    # Can this strategy go short?
    can_short: bool = False

    # Minimal ROI designed for the strategy.
    minimal_roi = {
        # "0": 0.6,  # 60% ROI maximum
        # "60": 0.3,  # 30% après 1h
        # "120": 0.15,  # 15% après 2h
        # "180": 0.05   # 5% après 3h
    }

    EXPORT_FILE = "/freqtrade/user_data/analysis/ichimoku_rebond_entries.csv"

    # Trailing stoploss
    trailing_stop = False

    # Hyperopt parameters
    rsi_entry_max = IntParameter(30, 70, default=70, space="buy", optimize=False)
    rsi_entry_min = IntParameter(10, 50, default=10, space="buy", optimize=False)
    volume_factor = CategoricalParameter([0, 0.25, 0.5, 1, 1.5, 2, 2.5, 3], default=0.5, space="buy", optimize=True)
    # entry_kinjun_sup_tenkan = BooleanParameter(default=False, space="buy", optimize=False)
    # entry_sma200 = BooleanParameter(default=False, space="buy", optimize=False)
    # entry_span_futur = BooleanParameter(default=False, space="buy", optimize=False)
    # entry_spanA_sup_spanB = BooleanParameter(default=False, space="buy", optimize=False)
    # entry_kinjun_sup_spanA = BooleanParameter(default=False, space="buy", optimize=False)
    # entry_kinjun_sup_spanB = BooleanParameter(default=False, space="buy", optimize=False)
    use_hammer_entry = BooleanParameter(default=True, space="buy", optimize=False)
    hammer_body_threshold = DecimalParameter(0.1, 1, default=0.2, space="buy", optimize=False)
    hammer_head_threshold = DecimalParameter(0.01, 0.99, default=0.1, space="buy", optimize=False)
    hammer_strength_threshold = DecimalParameter(0.001, 0.05, default=0.01, space="buy", optimize=False)

    use_engulfing_entry = BooleanParameter(default=False, space="buy", optimize=False)
    bullish_engulfing_upper_wick_threshold = DecimalParameter(0.01, 0.5, default=0.25, space="buy", optimize=False)
    engulfing_strength_threshold = DecimalParameter(0.001, 0.05, default=0.01, space="buy", optimize=False)
    engulfing_size_threshold = CategoricalParameter([1.1, 1.2, 1.5, 2, 2.5, 3], default=2, space="buy", optimize=False)

    use_strong_bullish_entry = BooleanParameter(default=False, space="buy", optimize=False)
    strong_bullish_strength_threshold = DecimalParameter(0.01, 0.05, default=0.02, space="buy", optimize=False)
    strong_bullish_size_threshold = CategoricalParameter([1.1, 1.2, 1.5, 2, 2.5, 3], default=2, space="buy", optimize=False)
    strong_bullish_upper_wick_threshold = DecimalParameter(0.01, 0.5, default=0.25, space="buy", optimize=False)

    confirmation_candle = BooleanParameter(default=True, space="buy", optimize=False)
    flat_kinjun_threshold = IntParameter(0, 20, default=4, space="buy", optimize=False)
    kinjun_proximity_threshold = DecimalParameter(0, 0.01, default=0.001, space="buy", optimize=False)
    tenkan_proximity_threshold = DecimalParameter(0, 0.01, default=0.001, space="buy", optimize=False)
    confirmation_chiku = BooleanParameter(default=True, space="buy", optimize=False)
    entry_adx_threshold = CategoricalParameter([5, 10, 15, 20, 25, 30, 40, 50], default=5, space="buy", optimize=False)


    use_custom_stoploss_param = BooleanParameter(default=True, space="sell", optimize=False)
    lookback_period_for_stoploss = IntParameter(1, 10, default=5, space="sell", optimize=False)
    take_profit_multiplier = CategoricalParameter([1, 1.5, 2, 2.5, 3], default=2, space="sell", optimize=False)
    stoploss_margin = DecimalParameter(0.990, 1, default=0.999, space="sell", optimize=False)
    kinjun_threshold = DecimalParameter(0.995, 1, default=1, space="sell", optimize=False)
    use_custom_stoploss_type = CategoricalParameter(['lower', 'atr', 'lower_and_atr', 'none'], default='lower', space="sell", optimize=False)
    use_custom_sell = BooleanParameter(default=True, space="sell", optimize=False)
    use_sell_signal_param = BooleanParameter(default=True, space="sell", optimize=False)
    atr_stoploss_multiplier = CategoricalParameter([0.5, 1, 1.5, 2, 2.5, 3], default=1.5, space="sell", optimize=False)
    custom_sell_atr_factor = CategoricalParameter([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6], default=4.5, space="sell", optimize=False)
    use_sell_kinjun_signal = BooleanParameter(default=False, space="sell", optimize=False)
    use_sell_ichimoku_cloud_signal = BooleanParameter(default=True, space="sell", optimize=False)
    use_sell_ichimoku_futur_cloud_signal = BooleanParameter(default=False, space="sell", optimize=False)

    ml_signal_strength_threshold = DecimalParameter(0, 100, default=50, space="buy", optimize=False)

    use_custom_stoploss = use_custom_stoploss_param.value

    # Strategy configuration - plain boolean values expected by Freqtrade
    use_exit_signal = use_sell_signal_param.value

    # Optimal stoploss designed for the strategy.
    stoploss = -0.1  # Stoploss initial de -10% (sera ajusté dynamiquement)
    # stoploss = -fix_stoploss_value_param.value  # Stoploss initial de -10% (sera ajusté dynamiquement)

    # Plotting configuration
    plot_config = {
        "main_plot": {
            'ichimoku-tenkan': {'color': 'red'},
            'ichimoku-kinjun': {'color': 'blue'},
            # 'kinjun_threshold': {'color': 'orange', 'linestyle': 'dotted'},
            # By omitting color, a random color is selected.
            # 'sma200_4h': {'color': 'lightblue'},
            # fill area between senkou_a and senkou_b
            'ichimoku-spanA': {
                'color': 'lightgreen', #optional
                'fill_to': 'ichimoku-spanB',
                'fill_label': 'Ichimoku Cloud', #optional
                'fill_color': 'green', #optional
            },
            # plot senkou_b, too. Not only the area to it.
            'ichimoku-spanB': {'color': 'darkgreen'},
            "ichimoku-chiku": {'color': 'purple'},
            "stoploss_prices": {
                "color": "grey",
                "linestyle": "dotted",
            },
            "custom_exit_signal": {
                "color": "orange",
            },
            # "custom_sell_signal": {
            #     "color": "yellow",
            # },
        },
        "subplots": {
            "close_sup_sma200_4h": {
                "close_sup_sma200_4h": {"color": "blue", "type": "bar"},
            },
            "ishammer": {
                "is_hammer": {"color": "green", "type": "bar"},
            },
            "is_bullish_engulfing": {
                "is_bullish_engulfing": {"color": "white", "type": "bar"},
            },
            "is_strong_bullish_candle": {
                "is_strong_bullish_candle": {"color": "purple", "type": "bar"},
            },
            # "engulfing": {
            #     "engulfing": {"color": "white", "type": "bar"},
            # },
            # "Proximities": {
            #     # "kinjun_proximity": {"color": "blue", "type": "bar"},
            #     # "tenkan_proximity": {"color": "orange", "type": "bar"},
            #     "proximity": {"color": "green", "type": "bar"},
            # },
            # "Ichimoku Future": {
            #     "ichimoku-futur": {"color": "green", "type": "bar"},
            # },
            # "Tenkan/Kinjun Increasing": {
            #     "tenkan_kinjun_increasing": {"color": "green", "type": "bar"},
            # },
            # "Last Candle Under Cloud": {
            #     "last_candle_under_cloud": {"color": "red", "type": "bar"},
            # },
            # "Ichimoku Chikou Free": {
            #     "ichimoku-chiku-free": {"color": "purple", "type": "bar"},
            # },
            # "rsi": {
            #     "rsi": {"color": "purple"},
            # },
            # "Volume": {
            #     "volume": {"color": "blue", "type": "bar"},
            #     "volume_sma": {"color": "orange"},
            # },
            "ADX": {
                "adx_range": {"color": "red"},
                "adx": {"color": "red"},
            },
        },
    }


    def informative_pairs(self):
        """
        Define additional, informative pair/interval combinations to be cached from the exchange.
        """
        return []

    @informative('1d')
    # @informative('1d', 'BTC/{stake}', fmt='{base}_{column}_{timeframe}')
    def populate_indicators_1d(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # Ichimoku
        dataframe['sma200'] = ta.SMA(dataframe, timeperiod=200)
        dataframe['ichimoku-tenkan'] = ((dataframe['high'].rolling(window=9).max()) + (dataframe['low'].rolling(window=9).min())) / 2
        dataframe['ichimoku-kinjun'] = ((dataframe['high'].rolling(window=26).max()) + (dataframe['low'].rolling(window=26).min())) / 2
        dataframe['ichimoku-spanA'] = ((dataframe['ichimoku-tenkan']) + (dataframe['ichimoku-kinjun'])).shift(26) / 2
        dataframe['ichimoku-spanB'] = ((dataframe['high'].rolling(window=52).max()) + (dataframe['low'].rolling(window=52).min())).shift(26) / 2
        dataframe['ichimoku-chiku'] = (dataframe['close'].shift(-26))

        dataframe['close_sup_sma200'] = dataframe['close'] > dataframe['sma200']
        return dataframe

    @informative('4h')
    # @informative('1d', 'BTC/{stake}', fmt='{base}_{column}_{timeframe}')
    def populate_indicators_4h(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # Ichimoku
        dataframe['sma200'] = ta.SMA(dataframe, timeperiod=200)
        dataframe["close_sup_sma200"] = dataframe["close"] > dataframe["sma200"]
        return dataframe

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Ajoute les indicateurs techniques nécessaires
        """

        # Volume moyen pour confirmation
        dataframe["volume_sma"] = dataframe["volume"].rolling(window=20).mean()

        # Ichimoku
        dataframe['ichimoku-tenkan'] = ((dataframe['high'].rolling(window=9).max()) + (dataframe['low'].rolling(window=9).min())) / 2
        dataframe['ichimoku-kinjun'] = ((dataframe['high'].rolling(window=26).max()) + (dataframe['low'].rolling(window=26).min())) / 2
        dataframe['ichimoku-spanA'] = ((dataframe['ichimoku-tenkan']) + (dataframe['ichimoku-kinjun'])).shift(26) / 2
        dataframe['ichimoku-spanB'] = ((dataframe['high'].rolling(window=52).max()) + (dataframe['low'].rolling(window=52).min())).shift(26) / 2
        dataframe['ichimoku-chiku'] = (dataframe['close'])

        dataframe['ichimoku-spanA-futur'] = ((dataframe['ichimoku-tenkan']) + (dataframe['ichimoku-kinjun'])) / 2
        dataframe['ichimoku-spanB-futur'] = ((dataframe['high'].rolling(window=52).max()) + (dataframe['low'].rolling(window=52).min())) / 2
        dataframe['ichimoku-futur'] = (dataframe['ichimoku-spanA-futur'] > dataframe['ichimoku-spanB-futur'])

        dataframe['sma200'] = ta.SMA(dataframe, timeperiod=200)
        dataframe['atr'] = ta.ATR(dataframe, timeperiod=14)

        # Calcul du stoploss effectif pour chaque bougie selon la méthode sélectionnée
        if self.use_custom_stoploss_param.value:
            stoploss_prices = []
            
            for i in range(len(dataframe)):
                if i < self.lookback_period_for_stoploss.value:
                    stoploss_prices.append(np.nan)
                else:
                    # Use existing helper methods for consistency
                    if self.use_custom_stoploss_type.value == 'lower':
                        stoploss_price = self._calculate_stoploss_price_lower(dataframe, i)
                    elif self.use_custom_stoploss_type.value == 'atr':
                        stoploss_price = self._calculate_stoploss_price_atr(dataframe, i)
                    elif self.use_custom_stoploss_type.value == 'lower_and_atr':
                        stoploss_price = self._calculate_stoploss_price_lower_and_atr(dataframe, i)
                    else:
                        # Default fallback
                        stoploss_price = dataframe["close"].iloc[i] * (1 + self.stoploss)
                    
                    stoploss_prices.append(stoploss_price)
            
            dataframe["stoploss_prices"] = stoploss_prices
        else:
            dataframe["stoploss_prices"] = dataframe["close"] * (1 + self.stoploss)

        dataframe['kinjun_threshold'] = dataframe["ichimoku-kinjun"] * self.kinjun_threshold.value


        dataframe['engulfing'] = self.is_bullish_engulfing(dataframe['open'].shift(1), dataframe['close'].shift(1), dataframe['open'], dataframe['close'], dataframe['low'], dataframe['high'])
        dataframe['ichimoku-futur'] = (dataframe['ichimoku-spanA-futur'] > dataframe['ichimoku-spanB-futur'])


        # Calculate last_candle_under_cloud iteratively
        dataframe['last_candle_under_cloud'] = 0
        
        for i in range(len(dataframe)):
            # Check if current candle is under cloud
            current_under_cloud = (
                (dataframe['close'].iloc[i] < dataframe['ichimoku-spanA'].iloc[i]) or 
                (dataframe['close'].iloc[i] < dataframe['ichimoku-spanB'].iloc[i])
            )
            
            if current_under_cloud:
                # Under cloud = 0
                dataframe.loc[dataframe.index[i], 'last_candle_under_cloud'] = 0
            else:
                # Above cloud
                if i == 0:
                    # First candle, set to 1
                    dataframe.loc[dataframe.index[i], 'last_candle_under_cloud'] = 1
                else:
                    # Check if previous candle was under cloud
                    previous_under_cloud = (
                        (dataframe['close'].iloc[i-1] < dataframe['ichimoku-spanA'].iloc[i-1]) and 
                        (dataframe['close'].iloc[i-1] < dataframe['ichimoku-spanB'].iloc[i-1])
                    )
                    
                    if previous_under_cloud:
                        # Cross up = 1
                        dataframe.loc[dataframe.index[i], 'last_candle_under_cloud'] = 1
                    else:
                        # Continue above cloud = previous + 1
                        prev_value = dataframe['last_candle_under_cloud'].iloc[i-1]
                        dataframe.loc[dataframe.index[i], 'last_candle_under_cloud'] = prev_value + 1

        # dataframe['ichimoku-chiku-free'] = ((dataframe['ichimoku-chiku'] > dataframe['close'].shift(26)) & (dataframe['ichimoku-chiku'] > dataframe['ichimoku-spanA'].shift(26)) & (dataframe['ichimoku-chiku'] > dataframe['ichimoku-spanB'].shift(26)))

        dataframe['custom_sell_signal'] = dataframe[['ichimoku-spanA-futur','ichimoku-spanB-futur']].max(axis=1) + dataframe['atr'] * 2
        dataframe['custom_exit_signal'] = (dataframe[['ichimoku-spanA-futur','ichimoku-spanB-futur']].max(axis=1) + dataframe['atr'] * self.custom_sell_atr_factor.value).shift(1)


        dataframe['adx_range'] = ta.ADX(dataframe, timeperiod=14) < self.entry_adx_threshold.value

        dataframe['is_hammer'] = self.is_hammer_candle(dataframe['open'], dataframe['high'], dataframe['low'], dataframe['close']).fillna(True)
        dataframe['is_bullish_engulfing'] = self.is_bullish_engulfing(dataframe['open'].shift(1), dataframe['close'].shift(1), dataframe['open'], dataframe['close'], dataframe['low'], dataframe['high'])
        dataframe['is_strong_bullish_candle'] = self.is_strong_bullish_candle(dataframe['open'].shift(1), dataframe['close'].shift(1), dataframe['open'], dataframe['close'], dataframe['low'], dataframe['high'])

        # indicators to help debugging and strategy tuning
        dataframe['rsi'] = ta.RSI(dataframe, timeperiod=14)
        dataframe['atr_strength'] = (dataframe['atr'] / dataframe['close']) * 100
        dataframe['adx'] = ta.ADX(dataframe, timeperiod=14)
        dataframe['close_sup_sma200'] = dataframe['close'] > dataframe['sma200']
        dataframe['ichimoku-chiku-free'] = ((dataframe['ichimoku-chiku'] > dataframe['close'].shift(26)) & (dataframe['ichimoku-chiku'] > dataframe['ichimoku-spanA'].shift(26)) & (dataframe['ichimoku-chiku'] > dataframe['ichimoku-spanB'].shift(26)))
        dataframe['kinjun_flat'] = dataframe['ichimoku-kinjun'].shift(1) == dataframe['ichimoku-kinjun']
        dataframe['ichimoku-tenkan_sup_kinjun'] = dataframe['ichimoku-tenkan'] >= dataframe['ichimoku-kinjun']
        dataframe["tenkan_kinjun_increasing"] = (
            (dataframe["ichimoku-tenkan"] >= dataframe["ichimoku-kinjun"])
            & (dataframe["ichimoku-tenkan"].shift(1) < dataframe["ichimoku-tenkan"])
            & (dataframe["ichimoku-kinjun"].shift(1) <= dataframe["ichimoku-kinjun"])
        )
        dataframe['kinjun_proximity'] = ((dataframe[["close","open"]].min(axis=1) - dataframe["ichimoku-kinjun"]) / dataframe["ichimoku-kinjun"]).abs()
        dataframe['tenkan_proximity'] = ((dataframe[["close","open"]].min(axis=1) - dataframe["ichimoku-tenkan"]) / dataframe["ichimoku-tenkan"]).abs()
        dataframe['proximity'] = ((dataframe['kinjun_proximity'] < self.kinjun_proximity_threshold.value)) | ((dataframe['tenkan_proximity'] < self.tenkan_proximity_threshold.value))
        dataframe['volume_sup_avg'] = dataframe['volume'] > dataframe['volume_sma']




        # ML-based filtering of buy signals for hammer
        rsi_tenkan_score = indicators['rsi'] * indicators['tenkan_proximity']
        kinjun_tenkan_score = indicators['kinjun_proximity'] * indicators['tenkan_proximity']
        atr_adx_score = indicators['atr_strength'] * indicators['adx']
        
        # Combined signal strength
        ml_signal_strength_hammer = (rsi_tenkan_score + kinjun_tenkan_score + atr_adx_score) / 3
       


        return dataframe

    def is_hammer_candle(self, open_price, high_price, low_price, close_price) -> bool:
        """
        Détermine si une bougie est un marteau (hammer pattern)
        
        Args:
            open_price: Prix d'ouverture (pandas Series ou scalaire)
            high_price: Prix le plus haut (pandas Series ou scalaire)
            low_price: Prix le plus bas (pandas Series ou scalaire)
            close_price: Prix de clôture (pandas Series ou scalaire)
            
        Returns:
            bool/Series: True si la bougie respecte les critères d'un marteau
        """
        body_size = (close_price - open_price).abs()
        # Use np.minimum and np.maximum for element-wise operations
        lower_wick = np.minimum(close_price, open_price) - low_price
        upper_wick = high_price - np.maximum(close_price, open_price)
        total_range = high_price - low_price

        # Avoid division by zero - use np.where for safer division
        body_vs_lower_wick = (lower_wick > 0) & (
            np.where(lower_wick > 0, body_size / lower_wick, np.inf) < self.hammer_body_threshold.value
        )

        # Avoid division by zero - use np.where for safer division
        upper_wick_vs_body = (body_size > 0) & (
            np.where(body_size > 0, upper_wick / body_size, np.inf) < self.hammer_head_threshold.value
        )

        # Bougie importante
        significant_candle = (low_price > 0) & (
            np.where(low_price > 0, total_range / low_price, 0) > self.hammer_strength_threshold.value
        )

        return body_vs_lower_wick & upper_wick_vs_body & significant_candle

    def is_bullish_engulfing(self, prev_open, prev_close, curr_open, curr_close, curr_low, curr_high) -> bool:
        """
        Détermine si deux bougies consécutives forment un pattern d'engulfing haussier
        
        Args:
            prev_open: Prix d'ouverture de la bougie précédente
            prev_close: Prix de clôture de la bougie précédente
            curr_open: Prix d'ouverture de la bougie actuelle
            curr_close: Prix de clôture de la bougie actuelle
            
        Returns:
            bool: True si le pattern d'engulfing haussier est détecté
        """
        # Handle NaN values by filling with False
        prev_open = prev_open.fillna(0)
        prev_close = prev_close.fillna(0) 
        curr_open = curr_open.fillna(0)
        curr_close = curr_close.fillna(0)

        # La bougie précédente doit être baissière (rouge)
        prev_is_bearish = prev_close < prev_open

        # La bougie actuelle doit être haussière (verte)
        curr_is_bullish = curr_close > curr_open

        # La bougie actuelle doit englober complètement le corps de la précédente
        curr_engulfs_prev = (curr_open <= prev_close) & (curr_close > prev_open)

        # la taille de la bougie doit être x fois supérieure à la précédente
        prev_body_size = (prev_open - prev_close).abs()
        curr_body_size = (curr_close - curr_open).abs()
        
        # Avoid division by zero using np.where
        curr_is_big = np.where(
            prev_body_size > 0,
            curr_body_size > prev_body_size * self.engulfing_size_threshold.value,
            False
        )

        body_size = (curr_close - curr_open).abs()
        # Use np.minimum and np.maximum for element-wise operations
        lower_wick = np.minimum(curr_close, curr_open) - curr_low
        upper_wick = curr_high - np.maximum(curr_close, curr_open)
        total_range = curr_high - curr_low
        # Bougie importante
        significant_candle = (curr_low > 0) & (
            np.where(curr_low > 0, total_range / curr_low, 0) > self.engulfing_strength_threshold.value
        )

        return prev_is_bearish & curr_is_bullish & curr_engulfs_prev & curr_is_big & significant_candle


    def is_strong_bullish_candle(self, prev_open, prev_close, curr_open, curr_close, curr_low, curr_high) -> bool:
        """
        Détermine si une bougie forment un pattern de bougie haussière puissante
        
        Args:
            prev_open: Prix d'ouverture de la bougie précédente
            prev_close: Prix de clôture de la bougie précédente
            curr_open: Prix d'ouverture de la bougie actuelle
            curr_close: Prix de clôture de la bougie actuelle
            
        Returns:
            bool: True si le pattern d'engulfing haussier est détecté
        """
        # Handle NaN values by filling with False
        prev_open = prev_open.fillna(0)
        prev_close = prev_close.fillna(0) 
        curr_open = curr_open.fillna(0)
        curr_close = curr_close.fillna(0)

        # La bougie précédente doit être haussière (verte) - FIXED: was prev_close > prev_open
        prev_is_bullish = prev_close > prev_open

        # La bougie actuelle doit être haussière (verte)
        curr_is_bullish = curr_close > curr_open

        # Bougie importante
        total_range = curr_high - curr_low
        significant_candle = (curr_low > 0) & (
            np.where(curr_low > 0, total_range / curr_low, 0) > self.strong_bullish_strength_threshold.value
        )

        # la taille de la bougie doit être x fois supérieure à la précédente
        prev_body_size = (prev_open - prev_close).abs()
        curr_body_size = (curr_close - curr_open).abs()
        curr_is_big = np.where(
            prev_body_size > 0,
            curr_body_size > prev_body_size * self.strong_bullish_size_threshold.value,
            False
        )

        # la mèche haute doit être inférieure à x% de la bougie
        upper_wick_threshold = curr_body_size * self.strong_bullish_upper_wick_threshold.value
        upper_wick = curr_high - np.maximum(curr_close, curr_open)
        upper_wick_ok = upper_wick < upper_wick_threshold

        return prev_is_bullish & curr_is_bullish & curr_is_big & upper_wick_ok & significant_candle

    def is_bearish_engulfing(self, prev_open, prev_close, curr_open, curr_close) -> bool:
        """
        Détermine si deux bougies consécutives forment un pattern d'engulfing baissier
        
        Args:
            prev_open: Prix d'ouverture de la bougie précédente
            prev_close: Prix de clôture de la bougie précédente
            curr_open: Prix d'ouverture de la bougie actuelle
            curr_close: Prix de clôture de la bougie actuelle
            
        Returns:
            bool: True si le pattern d'engulfing baissier est détecté
        """
        # La bougie précédente doit être haussière (verte)
        prev_is_bullish = prev_close > prev_open

        # La bougie actuelle doit être baissière (rouge)
        curr_is_bearish = curr_close < curr_open

        # La bougie actuelle doit englober complètement le corps de la précédente
        curr_engulfs_prev = (curr_open >= prev_close) & (curr_close < prev_open)

        # la taille de la bougie doit être x fois supérieure à la précédente
        curr_is_big = (curr_close - curr_open) > (prev_open - prev_close) * self.engulfing_size_threshold.value

        return prev_is_bullish & curr_is_bearish & curr_engulfs_prev & curr_is_big


    def log_entries(self, dataframe: DataFrame, condition, metadata: dict, tag: str):
        """
        Sauvegarde les indicateurs pour les lignes où condition est vraie
        """
        entries = dataframe[condition].copy()
        if not entries.empty:
            # print(f"Logging {len(entries)} entries for {metadata} with tag {tag}")
            # print(f"dataframe columns: {dataframe.columns.tolist()}")
            entries['pair'] = metadata['pair']
            entries['timestamp'] = pd.to_datetime(dataframe['date']) + pd.Timedelta(hours=1)
            entries['entry_type'] = tag
            entries.to_csv(
                self.EXPORT_FILE,
                mode='a',
                header=not os.path.exists(self.EXPORT_FILE)
            )


    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Signaux d'achat basés sur divergence RSI haussière + bougie verte importante
        """

        # Filtrer si bougie journalière < nuage ichimoku ?


        if self.confirmation_candle.value:
            # Variables pour la bougie précédente (setup)
            rebond_tenkan = dataframe['ichimoku-tenkan'].shift(1)
            rebond_kinjun = dataframe['ichimoku-kinjun'].shift(1)
            rebond_close = dataframe['close'].shift(1)
            rebond_open = dataframe['open'].shift(1)
            rebond_high = dataframe['high'].shift(1)
            rebond_low = dataframe['low'].shift(1)
            rebond_spanA = dataframe['ichimoku-spanA'].shift(1)
            rebond_spanB = dataframe['ichimoku-spanB'].shift(1)
            rebond_volume = dataframe['volume'].shift(1)
            kinjun_proximity = dataframe['kinjun_proximity'].shift(1)
            tenkan_proximity = dataframe['tenkan_proximity'].shift(1)
            rebond_kinjun_spanA_futur = dataframe['ichimoku-spanA-futur'].shift(1)
            rebond_kinjun_spanB_futur = dataframe['ichimoku-spanB-futur'].shift(1)
            rebond_adx = dataframe['adx'].shift(1)
        else:
            # Variables pour la bougie actuelle (setup)
            rebond_tenkan = dataframe['ichimoku-tenkan']
            rebond_kinjun = dataframe['ichimoku-kinjun']
            rebond_close = dataframe['close']
            rebond_open = dataframe['open']
            rebond_high = dataframe['high']
            rebond_low = dataframe['low']
            rebond_spanA = dataframe['ichimoku-spanA']
            rebond_spanB = dataframe['ichimoku-spanB']
            rebond_volume = dataframe['volume']
            kinjun_proximity = dataframe['kinjun_proximity']
            tenkan_proximity = dataframe['tenkan_proximity']
            rebond_kinjun_spanA_futur = dataframe['ichimoku-spanA-futur']
            rebond_kinjun_spanB_futur = dataframe['ichimoku-spanB-futur']
            rebond_adx = dataframe['adx']

        if self.use_hammer_entry.value:
            buy_hammer_conditions = (
                # (rebond_adx > self.entry_adx_threshold.value) &
                # Conditions sur la bougie précédente (setup du rebond)
                # (rebond_tenkan >= rebond_kinjun)
                # &
                # (rebond_close < rebond_tenkan) &
                # (rebond_open < rebond_tenkan) &
                # (rebond_close > rebond_kinjun) &
                # (rebond_open > rebond_kinjun) &
                # (
                #     ((kinjun_proximity > 0) & (kinjun_proximity < self.kinjun_proximity_threshold.value)) |
                #     ((tenkan_proximity > 0) & (tenkan_proximity < self.tenkan_proximity_threshold.value))
                # ) &
                # la tenkan doit être ascendante et la kinjun plate ou ascendante
                # (
                #     (rebond_tenkan.shift(1) < rebond_tenkan) &
                #     (rebond_kinjun.shift(1) <= rebond_kinjun)
                # ) &
                # hammer
                (
                    # plat kinjun sur les 4 dernièreres bougies (bougie précédente)
                    # (rebond_kinjun.rolling(window=self.flat_kinjun_threshold.value).std() < 0.001) &
                    # low sous la kinjun
                    # (rebond_low < rebond_kinjun) &
                    # hammer
                    (
                        self.is_hammer_candle(
                            rebond_open, rebond_high, rebond_low, rebond_close
                        )
                    )
                    # &
                    # # confirmation bougie actuelle verte (sans biais)
                    # (
                    #     rebond_close > rebond_open
                    #     if self.confirmation_candle.value
                    #     else True
                    # )
                )  # &
                # (rebond_kinjun_spanA_futur > rebond_kinjun_spanB_futur) &
                # (rebond_close > rebond_spanA) &
                # (rebond_close > rebond_spanB) &
                # (dataframe['ichimoku-chiku-free'] if self.confirmation_chiku.value else True) &
                # (rebond_volume > self.volume_factor.value * dataframe['volume_sma']) &
                # (dataframe["close"] < (dataframe[['ichimoku-spanA-futur','ichimoku-spanB-futur']].max(axis=1) + dataframe['atr'] * 2)) &
                # (dataframe['close_4h'] > dataframe['sma200_4h'])
                # (dataframe['close_1d'] > dataframe[['ichimoku-spanA_1d','ichimoku-spanB_1d']].max(axis=1))
                # (dataframe['rsi'] < self.rsi_entry_max.value) # &
                # (dataframe['rsi'] > self.rsi_entry_min.value)
                & (self.ml_signal_strength_hammer > self.ml_signal_strength_threshold.value)
            )
            dataframe.loc[buy_hammer_conditions, ["enter_long", "enter_tag"]] = (
                1,
                "hammer_rebond",
            )
            self.log_entries(dataframe, buy_hammer_conditions, metadata, "hammer_rebond")

        if self.use_engulfing_entry.value:
            buy_engulfing_conditions = (
                (dataframe['adx'] > self.entry_adx_threshold.value) &
                # Conditions sur la bougie précédente (setup du rebond)
                (dataframe['ichimoku-tenkan'] >= dataframe['ichimoku-kinjun']) &
                # (rebond_open > rebond_kinjun) &
                (
                    ((dataframe['kinjun_proximity'] > 0) & (dataframe['kinjun_proximity'] < self.kinjun_proximity_threshold.value)) |
                    ((dataframe['tenkan_proximity'] > 0) & (dataframe['tenkan_proximity'] < self.tenkan_proximity_threshold.value))
                ) &
                # la tenkan doit être ascendante et la kinjun plate ou ascendante
                (
                    (dataframe['ichimoku-tenkan'].shift(1) < dataframe['ichimoku-tenkan']) &
                    (dataframe['ichimoku-kinjun'].shift(1) <= dataframe['ichimoku-kinjun'])
                ) &
                (
                    # bullish engulfing
                    ((dataframe['high'] - dataframe['close']) / (dataframe['high'] - dataframe['open']) < self.bullish_engulfing_upper_wick_threshold.value) &  # petite mèche haute
                    (self.is_bullish_engulfing(dataframe['open'].shift(1), dataframe['close'].shift(1), dataframe['open'], dataframe['close'], dataframe['low'], dataframe['high']))
                ) &

                (dataframe['ichimoku-spanA-futur'] > dataframe['ichimoku-spanB-futur']) &
                (dataframe['close'] > dataframe['ichimoku-spanA']) &
                (dataframe['close'] > dataframe['ichimoku-spanB']) &
                (dataframe['ichimoku-chiku-free'] if self.confirmation_chiku.value else True) &
                (rebond_volume > self.volume_factor.value * dataframe['volume_sma']) &
                # (dataframe["close"] < (dataframe[['ichimoku-spanA-futur','ichimoku-spanB-futur']].max(axis=1) + dataframe['atr'] * 2)) &
                (dataframe['close_4h'] > dataframe['sma200_4h']) 
                # (dataframe['close_1d'] > dataframe[['ichimoku-spanA_1d','ichimoku-spanB_1d']].max(axis=1))
                # (dataframe['rsi'] < self.rsi_entry_max.value) # & 
                # (dataframe['rsi'] > self.rsi_entry_min.value) 
            )
            dataframe.loc[buy_engulfing_conditions, ['enter_long', 'enter_tag']] = (1, 'engulfing_rebond')
            self.log_entries(dataframe, buy_engulfing_conditions, metadata, "engulfing_rebond")


        if self.use_strong_bullish_entry.value:
            strong_bullish_conditions = (
                (dataframe['adx'] > self.entry_adx_threshold.value) &
                # Conditions sur la bougie précédente (setup du rebond)
                (dataframe['ichimoku-tenkan'] >= dataframe['ichimoku-kinjun']) &
                # (rebond_open > rebond_kinjun) &
                (
                    ((dataframe['kinjun_proximity'] > 0) & (dataframe['kinjun_proximity'] < self.kinjun_proximity_threshold.value)) |
                    ((dataframe['tenkan_proximity'] > 0) & (dataframe['tenkan_proximity'] < self.tenkan_proximity_threshold.value))
                ) &
                # la tenkan doit être ascendante et la kinjun plate ou ascendante
                (
                    (dataframe['ichimoku-tenkan'].shift(1) < dataframe['ichimoku-tenkan']) &
                    (dataframe['ichimoku-kinjun'].shift(1) <= dataframe['ichimoku-kinjun'])
                ) &
                (
                    # bullish engulfing
                    ((dataframe['high'] - dataframe['close']) / (dataframe['high'] - dataframe['open']) < self.strong_bullish_upper_wick_threshold.value) &  # petite mèche haute
                    (self.is_strong_bullish_candle(dataframe['open'].shift(1), dataframe['close'].shift(1), dataframe['open'], dataframe['close'], dataframe['low'], dataframe['high']))
                ) &

                (dataframe['ichimoku-spanA-futur'] > dataframe['ichimoku-spanB-futur']) &
                (dataframe['close'] > dataframe['ichimoku-spanA']) &
                (dataframe['close'] > dataframe['ichimoku-spanB']) &
                (dataframe['ichimoku-chiku-free'] if self.confirmation_chiku.value else True) &
                (rebond_volume > self.volume_factor.value * dataframe['volume_sma']) &
                # (dataframe["close"] < (dataframe[['ichimoku-spanA-futur','ichimoku-spanB-futur']].max(axis=1) + dataframe['atr'] * 2)) &
                (dataframe['close_4h'] > dataframe['sma200_4h']) 
                # (dataframe['close_1d'] > dataframe[['ichimoku-spanA_1d','ichimoku-spanB_1d']].max(axis=1))
                # (dataframe['rsi'] < self.rsi_entry_max.value) # & 
                # (dataframe['rsi'] > self.rsi_entry_min.value) 
            )
            dataframe.loc[strong_bullish_conditions, ['enter_long', 'enter_tag']] = (1, 'strong_bullish_rebond')
            self.log_entries(dataframe, strong_bullish_conditions, metadata, "strong_bullish_rebond")

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Signaux de vente (optionnel, la stratégie utilise principalement ROI et stoploss)
        """

        if self.use_sell_signal_param.value:
            if self.use_sell_kinjun_signal.value :
                dataframe.loc[
                    (
                        qtpylib.crossed_below(dataframe["close"], dataframe["ichimoku-kinjun"] * self.kinjun_threshold.value)
                    ),
                    ["exit_long", "exit_tag"]] = (1, 'kinjun_crossed_exit')
            if self.use_sell_ichimoku_cloud_signal.value :
                dataframe.loc[
                    (
                        qtpylib.crossed_below(dataframe["close"], dataframe[["ichimoku-spanA","ichimoku-spanB"]].min(axis=1)) 
                    ),
                    ["exit_long", "exit_tag"]] = (1, 'ichimoku_cloud_crossed_exit')
            if self.use_sell_ichimoku_futur_cloud_signal.value :
                dataframe.loc[
                    (
                    qtpylib.crossed_below(dataframe["close"], (dataframe[['ichimoku-spanA-futur','ichimoku-spanB-futur']].max(axis=1) + dataframe['atr'] * self.custom_sell_atr_factor.value))
                    ),
                    ["exit_long", "exit_tag"]] = (1, 'ichimoku_cloud_futur_exit')

        return dataframe

    def calculate_lowest_price_last_n_candles(self, pair: str, n_candles: int) -> float:
        """
        Calculate the lowest price from the last n candles
        :param pair: Trading pair
        :param n_candles: Number of candles to look back
        :return: Lowest price from the last n candles
        """
        dataframe, _ = self.dp.get_analyzed_dataframe(
            pair=pair, timeframe=self.timeframe
        )
        last_n_lows = dataframe["low"].iloc[-n_candles:]
        lowest_price = (
            last_n_lows.min() * self.stoploss_margin.value
        )  # 0.5% sous le plus bas
        return lowest_price

    def _calculate_stoploss_price_lower(self, dataframe: DataFrame, i: int) -> float:
        """
        Helper method to calculate lower-based stoploss price for a specific candle index
        """
        recent_lows = (
            dataframe["low"]
            .iloc[max(0, i - self.lookback_period_for_stoploss.value) : i]
            .dropna()
        )
        if len(recent_lows) > 0:
            lowest_pivot = recent_lows.min()
            return lowest_pivot * self.stoploss_margin.value
        return np.nan

    def _calculate_stoploss_price_atr(self, dataframe: DataFrame, i: int) -> float:
        """
        Helper method to calculate ATR-based stoploss price for a specific candle index
        """
        current_close = dataframe["close"].iloc[i]
        current_atr = dataframe["atr"].iloc[i] if not pd.isna(dataframe["atr"].iloc[i]) else 0
        return current_close - (self.atr_stoploss_multiplier.value * current_atr)

    def _calculate_stoploss_price_lower_and_atr(self, dataframe: DataFrame, i: int) -> float:
        """
        Helper method to calculate combined lower+ATR stoploss price for a specific candle index
        """
        stoploss_price_lower = self._calculate_stoploss_price_lower(dataframe, i)
        current_atr = dataframe["atr"].iloc[i] if not pd.isna(dataframe["atr"].iloc[i]) else 0
        
        if not pd.isna(stoploss_price_lower):
            return stoploss_price_lower - self.atr_stoploss_multiplier.value * current_atr
        return current_atr

    def calculate_stoploss_lower(self, pair: str, trade: Trade, current_rate: float) -> float:
        """
        Calculate stoploss based on the lowest price of the last n candles
        
        :param pair: Trading pair
        :param trade: Current trade
        :param current_rate: Current market rate
        :return: Stoploss ratio
        """
        # Get dataframe and use helper method for consistency
        dataframe, _ = self.dp.get_analyzed_dataframe(pair=pair, timeframe=self.timeframe)
        last_candle_index = len(dataframe) - 1
        lowest_price = self._calculate_stoploss_price_lower(dataframe, last_candle_index)

        # Convertir en ratio relatif au prix courant
        ratio = stoploss_from_absolute(
            lowest_price,
            current_rate,
            is_short=trade.is_short,
            leverage=trade.leverage,
        )
        return ratio

    def calculate_stoploss_atr(self, pair: str, trade: Trade, current_rate: float) -> float:
        """
        Calculate stoploss based on ATR (Average True Range)
        
        :param pair: Trading pair
        :param trade: Current trade
        :param current_rate: Current market rate
        :return: Stoploss ratio
        """
        # Get dataframe and use helper method for consistency
        dataframe, _ = self.dp.get_analyzed_dataframe(pair=pair, timeframe=self.timeframe)
        last_candle_index = len(dataframe) - 1
        lowest_price = self._calculate_stoploss_price_atr(dataframe, last_candle_index)
        
        ratio = stoploss_from_absolute(
            lowest_price,
            current_rate,
            is_short=trade.is_short,
            leverage=trade.leverage,
        )
        return ratio

    def calculate_stoploss_lower_and_atr(self, pair: str, trade: Trade, current_rate: float) -> float:
        """
        Calculate stoploss based on the minimum between lowest price and ATR-based price
        
        :param pair: Trading pair
        :param trade: Current trade
        :param current_rate: Current market rate
        :return: Stoploss ratio
        """
        # Get dataframe and use helper method for consistency
        dataframe, _ = self.dp.get_analyzed_dataframe(pair=pair, timeframe=self.timeframe)
        last_candle_index = len(dataframe) - 1
        lowest_price = self._calculate_stoploss_price_lower_and_atr(dataframe, last_candle_index)
        
        ratio = stoploss_from_absolute(
            lowest_price,
            current_rate,
            is_short=trade.is_short,
            leverage=trade.leverage,
        )
        return ratio

    def custom_stoploss(
        self,
        pair: str,
        trade: Trade,
        current_time: datetime,
        current_rate: float,
        current_profit: float,
        after_fill: bool,
        **kwargs,
    ) -> float | None:

        # 1. Si ce n'est pas le premier appel, ne pas toucher au stop-loss
        # if hasattr(trade, 'stop_price_ratio'):
        if self.use_custom_stoploss_param.value:
            if trade.get_custom_data("stop_price_ratio") is not None:
                return None

            # Calculate stoploss ratio based on the selected method
            if self.use_custom_stoploss_type.value == 'lower':
                ratio = self.calculate_stoploss_lower(pair, trade, current_rate)
            elif self.use_custom_stoploss_type.value == 'atr':
                ratio = self.calculate_stoploss_atr(pair, trade, current_rate)
            elif self.use_custom_stoploss_type.value == 'lower_and_atr':
                ratio = self.calculate_stoploss_lower_and_atr(pair, trade, current_rate)
            else:
                ratio = 0

            trade.set_custom_data(key="stop_price_ratio", value=ratio)
        else:
            return 0
        return ratio

    def custom_stake_amount(
        self,
        pair: str,
        current_time: datetime,
        current_rate: float,
        proposed_stake: float,
        min_stake: float,
        max_stake: float,
        **kwargs,
    ) -> float:
        
        # Get total wallet balance
        total_stake_amount = self.wallets.get_total_stake_amount()

        dataframe, _ = self.dp.get_analyzed_dataframe(
            pair=pair, timeframe=self.timeframe
        )
        
        if self.use_custom_stoploss_param.value:
            # Calculate stoploss price using existing helper methods
            if self.use_custom_stoploss_type.value == 'lower':
                stoploss_price = self.calculate_lowest_price_last_n_candles(
                    pair, self.lookback_period_for_stoploss.value
                )
            elif self.use_custom_stoploss_type.value == 'atr':
                # Use the last candle index for ATR calculation
                last_candle_index = len(dataframe) - 1
                stoploss_price = self._calculate_stoploss_price_atr(dataframe, last_candle_index)
            elif self.use_custom_stoploss_type.value == 'lower_and_atr':
                # Use the last candle index for combined calculation
                last_candle_index = len(dataframe) - 1
                stoploss_price = self._calculate_stoploss_price_lower_and_atr(dataframe, last_candle_index)
            else:
                # Fallback to default
                stoploss_price = current_rate * (1 + self.stoploss)
        else:
            stoploss_price = current_rate * (1 + self.stoploss)

        # print(f"Custom stake check for {pair} at {current_time} with current rate {current_rate}, stoploss price {stoploss_price}")

        stop_distance = current_rate - stoploss_price

        if stop_distance <= 0:
            return min_stake

        # Calculate risk per trade (2% of total portfolio)
        risk_percent = 0.02  # 2% risk per trade
        risk_amount = total_stake_amount * risk_percent

        # Calculate position size based on risk
        # risk_amount = position_size * (stop_distance / current_rate)
        # Therefore: position_size = risk_amount / (stop_distance / current_rate)
        stake = risk_amount / (stop_distance / current_rate)

        # Apply limits
        stake = max(min_stake, min(stake, max_stake))
    
        # Additional safety: never use more than 50% of available capital per trade
        max_position_size = total_stake_amount * 0.50
        stake = min(stake, max_position_size)

        # K = max_stake
        # stake = (K / 100) / stop_distance * current_rate * 2  # Risque de 2% du capital
        # # print(f"Custom stake for {pair} at {current_time} is {stake}")

        # if stake > max_stake:
        #     return max_stake

        return stake

    def custom_sell(
        self,
        pair: str,
        trade: Trade,
        current_time: "datetime",
        current_rate: float,
        current_profit: float,
        **kwargs,
    ):
        """
        Take Profit : 2 fois le risque
        """

        if current_profit <= 0:
            return None

        if self.use_custom_sell.value is False:
            return None
        # Calculer le risque initial (différence entre prix d'entrée et stoploss)
        entry_rate = trade.open_rate

        # Estimer le niveau de stoploss actuel
        # 2. Calcul du plus bas sur les 8 dernières bougies avant l'entrée
        # lowest_price = self.calculate_lowest_price_last_n_candles(pair, self.lookback_period_for_pivots.value)
        # ratio = stoploss_from_absolute(lowest_price, current_rate,
        #                                is_short=trade.is_short, leverage=trade.leverage)
        if self.use_custom_stoploss_param.value:
            ratio = trade.get_custom_data("stop_price_ratio")
        else:
            ratio = -self.stoploss
        # print(f"Custom sell check for {pair} at {current_time} with stored ratio {ratio}")
        # Convertir en prix absolu
        stoploss_rate = entry_rate * (1 - ratio)
        # print(f"Custom sell check for {pair} at {current_time} with entry {entry_rate}, stoploss {stoploss_rate}, current rate {current_rate}, current profit {current_profit}")
        # stoploss_rate = trade.get_custom_data("stop_price_ratio").value
        risk = entry_rate - stoploss_rate

        # Take profit à x fois le risque
        target_rate = entry_rate + (self.take_profit_multiplier.value * risk)
        target_profit = (target_rate - entry_rate) / entry_rate

        # print(f"Custom sell check for {pair} at {current_time} with entry {entry_rate}, stoploss {stoploss_rate}, target {target_rate}, current rate {current_rate}, current profit {current_profit}, target profit {target_profit}")

        # Si le profit actuel atteint le take profit, vendre
        if current_profit >= target_profit:
            return f"take_profit_{self.take_profit_multiplier.value}R"
        
        # ## Vendre si le prix est au dessus du nuage Ichimoku projeté + x*ATR
        # dataframe, _ = self.dp.get_analyzed_dataframe(
        #     pair=pair, timeframe=self.timeframe
        # )
        # if len(dataframe) > 0:
        #     cloud_upper_limit = (dataframe[['ichimoku-spanA-futur','ichimoku-spanB-futur']].max(axis=1) + dataframe['atr'] * self.custom_sell_atr_factor.value).iloc[-1]
        #     if current_rate > cloud_upper_limit:
        #         return "sell_ichimoku_futur_cloud"

        return None
