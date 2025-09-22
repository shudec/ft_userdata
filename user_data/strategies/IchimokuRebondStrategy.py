# pragma pylint: disable=missing-docstring, invalid-name, pointless-string-statement
# flake8: noqa: F401
# isort: skip_file
# --- Do not remove these libs ---
import datetime
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

    # Trailing stoploss
    trailing_stop = False

    # Hyperopt parameters
    # rsi_entry_max = IntParameter(30, 70, default=50, space="buy", optimize=False)
    # rsi_entry_min = IntParameter(10, 50, default=20, space="buy", optimize=False)
    # volume_factor = DecimalParameter(0.5, 3, default=0.5, space="buy", optimize=False)
    # entry_kinjun_sup_tenkan = BooleanParameter(default=False, space="buy", optimize=False)
    # entry_sma200 = BooleanParameter(default=False, space="buy", optimize=False)
    # entry_span_futur = BooleanParameter(default=False, space="buy", optimize=False)
    # entry_spanA_sup_spanB = BooleanParameter(default=False, space="buy", optimize=False)
    # entry_kinjun_sup_spanA = BooleanParameter(default=False, space="buy", optimize=False)
    # entry_kinjun_sup_spanB = BooleanParameter(default=False, space="buy", optimize=False)
    hammer_body_threshold = DecimalParameter(0.1, 1, default=0.2, space="buy", optimize=True)
    hammer_head_threshold = DecimalParameter(0.01, 0.99, default=0.1, space="buy", optimize=True)
    hammer_strength_threshold = DecimalParameter(0.001, 0.05, default=0.01, space="buy", optimize=True)
    engulfing_size_threshold = CategoricalParameter([1.1, 1.2, 1.5, 2, 2.5, 3], default=2, space="buy", optimize=True)
    engulfing_size_threshold = CategoricalParameter([1.1, 1.2, 1.5, 2, 2.5, 3], default=2, space="buy", optimize=True)
    confirmation_candle = BooleanParameter(default=True, space="buy", optimize=True)
    flat_kinjun_threshold = IntParameter(0, 20, default=4, space="buy", optimize=True)
    kinjun_proximity_threshold = DecimalParameter(0, 0.002, default=0.001, space="buy", optimize=True)
    tenkan_proximity_threshold = DecimalParameter(0, 0.002, default=0.001, space="buy", optimize=True)
    confirmation_chiku = BooleanParameter(default=True, space="buy", optimize=True)
    bullish_engulfing_upper_wick_threshold = DecimalParameter(0.01, 0.5, default=0.25, space="buy", optimize=True)

    use_custom_stoploss_param = BooleanParameter(default=True, space="sell", optimize=False)
    lookback_period_for_stoploss = IntParameter(0, 10, default=5, space="sell", optimize=False)
    take_profit_multiplier = CategoricalParameter([1, 1.5, 2, 2.5, 3], default=2, space="sell", optimize=False)
    stoploss_margin = DecimalParameter(0.990, 1, default=0.999, space="sell", optimize=False)
    kinjun_threshold = DecimalParameter(0.995, 1, default=1, space="sell", optimize=False)
    # fix_stoploss_value_param = CategoricalParameter([-0.20, -0.15, -0.10, -0.05, -0.02, -0.01], default=-0.10, space="sell")
    use_sell_signal_param = BooleanParameter(default=True, space="sell", optimize=True)
    previous_low_stoploss = BooleanParameter(default=True, space="sell", optimize=True)
    atr_stoploss = BooleanParameter(default=False, space="sell", optimize=True)
    atr_stoploss_multiplier = CategoricalParameter([0.5, 1, 1.5, 2, 2.5, 3], default=1.5, space="sell", optimize=True)

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
            # 'sma200': {'color': 'lightblue'},
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
        },
        "subplots": {
            "engulfing": {
                "engulfing": {"color": "white", "type": "bar"},
            },
            "Proximities": {
                # "kinjun_proximity": {"color": "blue", "type": "bar"},
                # "tenkan_proximity": {"color": "orange", "type": "bar"},
                "proximity": {"color": "green", "type": "bar"},
            },
            "Ichimoku Future": {
                "ichimoku-futur": {"color": "green", "type": "bar"},
            },
            "Tenkan/Kinjun Increasing": {
                "tenkan_kinjun_increasing": {"color": "green", "type": "bar"},
            },
            # "Last Candle Under Cloud": {
            #     "last_candle_under_cloud": {"color": "red", "type": "bar"},
            # },
            "Ichimoku Chikou Free": {
                "ichimoku-chiku-free": {"color": "purple", "type": "bar"},
            },
            # "rsi": {
            #     "rsi": {"color": "purple"},
            # },
            "Volume": {
                "volume": {"color": "blue", "type": "bar"},
                "volume_sma": {"color": "orange"},
            },
        },
    }

    def informative_pairs(self):
        """
        Define additional, informative pair/interval combinations to be cached from the exchange.
        """
        return []

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

        # Calcul du stoploss effectif pour chaque bougie
        if self.use_custom_stoploss_param.value:
            stoploss_prices = []
            for i in range(len(dataframe)):
                if i < self.lookback_period_for_stoploss.value:
                    stoploss_prices.append(np.nan)
                else:
                    recent_lows = (
                        dataframe["low"]
                        .iloc[max(0, i - self.lookback_period_for_stoploss.value) : i]
                        .dropna()
                    )
                    if len(recent_lows) > 0:
                        lowest_pivot = recent_lows.min()
                        stoploss_price = (
                            lowest_pivot * self.stoploss_margin.value
                        )  # 0.5% sous le pivot
                        stoploss_prices.append(stoploss_price)
                    else:
                        stoploss_prices.append(np.nan)
            dataframe["stoploss_prices"] = stoploss_prices
        else:
            dataframe["stoploss_prices"] = dataframe["close"] * (1 + self.stoploss)

        dataframe['kinjun_threshold'] = dataframe["ichimoku-kinjun"] * self.kinjun_threshold.value
        dataframe['kinjun_proximity'] = ((dataframe[["close","open"]].min(axis=1) - dataframe["ichimoku-kinjun"]) / dataframe["ichimoku-kinjun"]).abs()
        dataframe['tenkan_proximity'] = ((dataframe[["close","open"]].min(axis=1) - dataframe["ichimoku-tenkan"]) / dataframe["ichimoku-tenkan"]).abs()

        dataframe['proximity'] = ((dataframe['kinjun_proximity'] < self.kinjun_proximity_threshold.value)) | ((dataframe['tenkan_proximity'] < self.tenkan_proximity_threshold.value))

        dataframe['sma200'] = ta.SMA(dataframe, timeperiod=200)
        dataframe['rsi'] = ta.RSI(dataframe, timeperiod=14)
        dataframe['atr'] = ta.ATR(dataframe, timeperiod=14)

        dataframe['engulfing'] = self.is_bullish_engulfing(dataframe['open'].shift(1), dataframe['close'].shift(1), dataframe['open'], dataframe['close'])
        dataframe['ichimoku-futur'] = (dataframe['ichimoku-spanA-futur'] > dataframe['ichimoku-spanB-futur'])
        dataframe["tenkan_kinjun_increasing"] = (
            (dataframe["ichimoku-tenkan"] >= dataframe["ichimoku-kinjun"])
            & (dataframe["ichimoku-tenkan"].shift(1) < dataframe["ichimoku-tenkan"])
            & (dataframe["ichimoku-kinjun"].shift(1) <= dataframe["ichimoku-kinjun"])
        )

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

        dataframe['ichimoku-chiku-free'] = ((dataframe['ichimoku-chiku'] > dataframe['close'].shift(26)) & (dataframe['ichimoku-chiku'] > dataframe['ichimoku-spanA'].shift(26)) & (dataframe['ichimoku-chiku'] > dataframe['ichimoku-spanB'].shift(26)))

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
        lower_wick = close_price.combine(open_price, min) - low_price
        upper_wick = high_price - close_price.combine(open_price, max)
        total_range = high_price - low_price

        # Taille du corps par rapport à la mèche basse
        body_vs_lower_wick = body_size < lower_wick * self.hammer_body_threshold.value

        # Mèche de la tête par rapport au corps
        upper_wick_vs_body = upper_wick < body_size * self.hammer_head_threshold.value

        # Bougie importante (range significatif)
        significant_candle = (total_range / low_price) > self.hammer_strength_threshold.value

        return body_vs_lower_wick & upper_wick_vs_body & significant_candle

    def is_bullish_engulfing(self, prev_open, prev_close, curr_open, curr_close) -> bool:
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
        # La bougie précédente doit être baissière (rouge)
        prev_is_bearish = prev_close < prev_open

        # La bougie actuelle doit être haussière (verte)
        curr_is_bullish = curr_close > curr_open

        # La bougie actuelle doit englober complètement le corps de la précédente
        curr_engulfs_prev = (curr_open <= prev_close) & (curr_close > prev_open)

        # la taille de la bougie doit être x fois supérieure à la précédente
        curr_is_big = (curr_close - curr_open) > (prev_open - prev_close) * self.engulfing_size_threshold.value

        return prev_is_bearish & curr_is_bullish & curr_engulfs_prev & curr_is_big

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

    @informative('1d')
    # @informative('1d', 'BTC/{stake}', fmt='{base}_{column}_{timeframe}')
    def populate_indicators_1d(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # Ichimoku
        dataframe['sma200'] = ta.SMA(dataframe, timeperiod=200)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Signaux d'achat basés sur divergence RSI haussière + bougie verte importante
        """
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

        dataframe.loc[
            (
                # Conditions sur la bougie précédente (setup du rebond)
                (rebond_tenkan >= rebond_kinjun) &
                # (rebond_close < rebond_tenkan) &
                # (rebond_open < rebond_tenkan) &
                (rebond_close > rebond_kinjun) &
                # (rebond_open > rebond_kinjun) &
                (
                    ((kinjun_proximity > 0) & (kinjun_proximity < self.kinjun_proximity_threshold.value)) |
                    ((tenkan_proximity > 0) & (tenkan_proximity < self.tenkan_proximity_threshold.value))
                ) &
                # la tenkan doit être ascendante et la kinjun plate ou ascendante
                (
                    (rebond_tenkan.shift(1) < rebond_tenkan) &
                    (rebond_kinjun.shift(1) <= rebond_kinjun)
                ) &
                (
                    # hammer
                    (
                        # plat kinjun sur les 4 dernièreres bougies (bougie précédente)
                        # (rebond_kinjun.rolling(window=self.flat_kinjun_threshold.value).std() < 0.001) &
                        # low sous la kinjun
                        # (rebond_low < rebond_kinjun) &
                        # hammer
                        (self.is_hammer_candle(rebond_open, rebond_high, rebond_low, rebond_close)) &
                        # confirmation bougie actuelle verte (sans biais)
                        (rebond_close > rebond_open if self.confirmation_candle.value else True)
                    )
                ) &

                (rebond_kinjun_spanA_futur > rebond_kinjun_spanB_futur) &
                (rebond_close > rebond_spanA) &
                (rebond_close > rebond_spanB) &
                (dataframe['ichimoku-chiku-free'] if self.confirmation_chiku.value else True) &
                (rebond_volume > 0)
            ),
            ['enter_long', 'enter_tag']] = (1, 'hammer_rebond')

        dataframe.loc[
        (
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
                (self.is_bullish_engulfing(dataframe['open'].shift(1), dataframe['close'].shift(1), dataframe['open'], dataframe['close']))
            ) &

            (dataframe['ichimoku-spanA-futur'] > dataframe['ichimoku-spanB-futur']) &
            (dataframe['close'] > dataframe['ichimoku-spanA']) &
            (dataframe['close'] > dataframe['ichimoku-spanB']) &
            (dataframe['ichimoku-chiku-free'] if self.confirmation_chiku.value else True) &
            (dataframe['volume'] > 0)
        ),
        ['enter_long', 'enter_tag']] = (1, 'engulfing_rebond')

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Signaux de vente (optionnel, la stratégie utilise principalement ROI et stoploss)
        """

        if self.use_sell_signal_param.value:
            dataframe.loc[
                (
                    qtpylib.crossed_below(dataframe["close"], dataframe["ichimoku-kinjun"] * self.kinjun_threshold.value)
                ),
                "exit_long",
            ] = 1

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

    # Custom stoploss: Set the stoploss based on the lowest low of the last 8 candles before entry
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

            if self.previous_low_stoploss.value:
                # 2. Calcul du plus bas sur les 8 dernières bougies avant l'entrée
                lowest_price = self.calculate_lowest_price_last_n_candles(
                    pair, self.lookback_period_for_stoploss.value
                )

                # 3. Convertir en ratio relatif au prix courant
                ratio = stoploss_from_absolute(
                    lowest_price,
                    current_rate,
                    is_short=trade.is_short,
                    leverage=trade.leverage,
                )
                trade.set_custom_data(key="stop_price_ratio", value=ratio)
            elif self.atr_stoploss.value:
                dataframe, _ = self.dp.get_analyzed_dataframe(
                    pair=pair, timeframe=self.timeframe
                )
                atr = dataframe['atr'].iloc[-1]
                lowest_price = current_rate - self.atr_stoploss_multiplier.value * atr
                ratio = stoploss_from_absolute(
                    lowest_price,
                    current_rate,
                    is_short=trade.is_short,
                    leverage=trade.leverage,
                )
                trade.set_custom_data(key="stop_price_ratio", value=ratio)
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
        dataframe, _ = self.dp.get_analyzed_dataframe(
            pair=pair, timeframe=self.timeframe
        )
        if self.use_custom_stoploss_param.value:
            stoploss_price = self.calculate_lowest_price_last_n_candles(
                pair, self.lookback_period_for_stoploss.value
            )
        else:
            stoploss_price = current_rate + self.stoploss * current_rate

        # print(f"Custom stake check for {pair} at {current_time} with current rate {current_rate}, stoploss price {stoploss_price}")

        stop_distance = current_rate - stoploss_price

        if stop_distance <= 0:
            return min_stake
        K = max_stake
        stake = (K / 100) / stop_distance * current_rate * 2  # Risque de 2% du capital
        # print(f"Custom stake for {pair} at {current_time} is {stake}")

        if stake > max_stake:
            return max_stake

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

        # Take profit à 2 fois le risque
        target_rate = entry_rate + (self.take_profit_multiplier.value * risk)
        target_profit = (target_rate - entry_rate) / entry_rate

        # print(f"Custom sell check for {pair} at {current_time} with entry {entry_rate}, stoploss {stoploss_rate}, target {target_rate}, current rate {current_rate}, current profit {current_profit}, target profit {target_profit}")

        # Si le profit actuel atteint le take profit, vendre
        if current_profit >= target_profit:
            return f"take_profit_{self.take_profit_multiplier.value}R"

        return None
