# pragma pylint: disable=missing-docstring, invalid-name, pointless-string-statement
# flake8: noqa: F401
# isort: skip_file
# --- Do not remove these libs ---
import datetime
import numpy as np  # noqa
import pandas as pd  # noqa
from pandas import DataFrame

from freqtrade.strategy import (BooleanParameter, CategoricalParameter, DecimalParameter,
                                IStrategy, IntParameter, Trade, stoploss_from_absolute)

# --------------------------------
# Add your lib to import here
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib


class RSIDivergenceBullishStrategy(IStrategy):
    """
    Stratégie basée sur la divergence RSI haussière
    - Achat : divergence RSI bullish + bougie verte importante
    - Stop Loss : sous la bougie la plus basse ayant créé la divergence
    - Take Profit : 2 fois le risque (ratio 1:2)
    """
    
    # Strategy interface version - allow new iterations of the strategy interface.
    INTERFACE_VERSION = 3

    # Optimal timeframe for the strategy.
    timeframe = '1h'

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
    rsi_period = IntParameter(10, 20, default=14, space="buy")
    rsi_oversold = IntParameter(20, 40, default=30, space="buy")
    # candle_size_threshold = DecimalParameter(0.02, 0.08, default=0.04, space="buy")
    lookback_period_for_pivots = IntParameter(3, 20, default=10, space="buy")
    pivot_confirmation_period = IntParameter(1, 10, default=1, space="buy")
    lookback_period_for_divergence = IntParameter(20, 100, default=60, space="buy")
    use_custom_stoploss_param = BooleanParameter(default=False, space="sell")
    lookback_period_for_stoploss = IntParameter(3, 10, default=5, space="sell")
    take_profit_multiplier = CategoricalParameter([1, 1.5, 2, 2.5, 3], default=2, space="sell")
    stoploss_margin = DecimalParameter(0.990, 0.999, default=0.995, space="sell")
    # fix_stoploss_value_param = CategoricalParameter([-0.20, -0.15, -0.10, -0.05, -0.02, -0.01], default=-0.10, space="sell")

    use_custom_stoploss = use_custom_stoploss_param.value

    
    # Optimal stoploss designed for the strategy.
    stoploss = -0.1  # Stoploss initial de -10% (sera ajusté dynamiquement)
    # stoploss = -fix_stoploss_value_param.value  # Stoploss initial de -10% (sera ajusté dynamiquement)

    # Plotting configuration
    plot_config = {
        'main_plot': {
            'stoploss_prices': {'color': 'red', 'linestyle': 'dotted'},  # Ajout du stoploss effectif
            # 'ema_20': {'color': 'blue'},
            'bb_lowerband': {'color': 'cyan'},
            # 'bb_middleband': {'color': 'blue'},
            'bb_upperband': {'color': 'cyan'},
        },
        'subplots': {
            "RSI": {
                'rsi': {'color': 'purple'},
                'rsi_oversold': {'color': 'red', 'linestyle': 'dashed'},
            },
            "Pivots": {
                'high_pivot_ffill': {'color': 'green', 'type': 'bar'},
                'low_pivot_ffill': {'color': 'red', 'type': 'bar'},
            },
            "Divergence": {
                'bullish_divergence': {'color': 'white', 'type': 'bar'},
            }
        }
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
        
        # RSI
        dataframe['rsi'] = ta.RSI(dataframe, timeperiod=self.rsi_period.value)
        
        # Highs et Lows pour la détection de divergence
        # dataframe['high_pivot'] = self.find_pivots_high(dataframe['close'], self.lookback_period_for_pivots.value)
        # dataframe['low_pivot'] = self.find_pivots_low(dataframe['close'], self.lookback_period_for_pivots.value)

        # Pivots avec confirmation (sans lookahead bias)
        dataframe['high_pivot'] = self.find_pivots_high_confirmed(
            dataframe['close'], 
            self.lookback_period_for_pivots.value,
            self.pivot_confirmation_period.value
        )
        dataframe['low_pivot'] = self.find_pivots_low_confirmed(
            dataframe['close'], 
            self.lookback_period_for_pivots.value,
            self.pivot_confirmation_period.value
        )

        dataframe['high_pivot_ffill'] = dataframe['high_pivot'].fillna(value=0)
        dataframe['low_pivot_ffill'] = dataframe['low_pivot'].fillna(value=0)
        
        # Taille de la bougie (en pourcentage)
        # dataframe['candle_size'] = (dataframe['close'] - dataframe['open']) / dataframe['open']
        
        # Moyenne mobile pour confirmation de tendance
        dataframe['ema_20'] = ta.EMA(dataframe, timeperiod=20)
        # dataframe['ema_50'] = ta.EMA(dataframe, timeperiod=50)

        # dataframe['sma_200'] = ta.SMA(dataframe, timeperiod=200)

        # Bollinger Bands
        bollinger = qtpylib.bollinger_bands(qtpylib.typical_price(dataframe), window=20, stds=2)
        dataframe["bb_lowerband"] = bollinger["lower"]
        dataframe["bb_middleband"] = bollinger["mid"]
        dataframe["bb_upperband"] = bollinger["upper"]
        dataframe["bb_percent"] = (dataframe["close"] - dataframe["bb_lowerband"]) / (
            dataframe["bb_upperband"] - dataframe["bb_lowerband"]
        )
        dataframe["bb_width"] = (dataframe["bb_upperband"] - dataframe["bb_lowerband"]) / dataframe[
            "bb_middleband"
        ]
        
        # Volume moyen pour confirmation
        dataframe['volume_sma'] = dataframe['volume'].rolling(window=20).mean()
        
        # Détection de divergence haussière
        dataframe['bullish_divergence'] = self.detect_bullish_divergence(dataframe)

        # Calcul du stoploss effectif pour chaque bougie
        if self.use_custom_stoploss_param.value:
            stoploss_prices = []
            for i in range(len(dataframe)):
                if i < self.lookback_period_for_stoploss.value:
                    stoploss_prices.append(np.nan)
                else:
                    recent_lows = dataframe['low'].iloc[max(0, i - self.lookback_period_for_stoploss.value):i].dropna()
                    if len(recent_lows) > 0:
                        lowest_pivot = recent_lows.min()
                        stoploss_price = lowest_pivot * self.stoploss_margin.value  # 0.5% sous le pivot
                        stoploss_prices.append(stoploss_price)
                    else:
                        stoploss_prices.append(np.nan)
            dataframe['stoploss_prices'] = stoploss_prices
        else:
            dataframe['stoploss_prices'] = dataframe['close'] * (1 + self.stoploss)



        # Ajouter des filtres de qualité
        
        # ATR pour mesurer la volatilité
        dataframe['atr'] = ta.ATR(dataframe, timeperiod=14)
        
        # Support/Résistance simple
        dataframe['support'] = dataframe['low'].rolling(20).min()
        dataframe['resistance'] = dataframe['high'].rolling(20).max()
        
        # Trend strength (ADX)
        dataframe['adx'] = ta.ADX(dataframe, timeperiod=14)
        
        # Market structure (Higher Lows confirmation)
        dataframe['higher_low'] = (dataframe['low'] > dataframe['low'].shift(5)) & (dataframe['low'].shift(5) > dataframe['low'].shift(10))


        """
        Signaux d'achat améliorés avec confirmations multiples
        """
        
        # Momentum RSI (changement sur les 3 dernières bougies)
        dataframe['rsi_momentum'] = dataframe['rsi'] - dataframe['rsi'].shift(3)
        
        # Force de la bougie haussière
        dataframe['bullish_strength'] = ((dataframe['close'] - dataframe['low']) / 
                                    (dataframe['high'] - dataframe['low']) * 100)
        
        # Ratio de volume
        dataframe['volume_ratio'] = dataframe['volume'] / dataframe['volume_sma']

        return dataframe

    def find_pivots_high_confirmed(self, series: pd.Series, window: int, confirmation: int = 3) -> pd.Series:
        """Trouve les pivots hauts avec période de confirmation SANS lookahead bias"""
        pivots = pd.Series(index=series.index, dtype=float)
        
        for i in range(window + confirmation, len(series)):
            # Le pivot potentiel était à i-confirmation périodes
            pivot_idx = i - confirmation
            
            if pivot_idx < window:
                continue
            
            # Vérifier si c'était un maximum local AU MOMENT du pivot
            window_data = series.iloc[pivot_idx-window:pivot_idx+1]  # Seulement jusqu'au pivot
            
            if len(window_data) > 0 and series.iloc[pivot_idx] == window_data.max():
                # Confirmer que depuis le pivot, aucun prix n'a dépassé ce niveau
                # (ceci utilise seulement les données disponibles progressivement)
                confirmation_data = series.iloc[pivot_idx+1:i+1]  # Données après le pivot
                
                if len(confirmation_data) == 0 or series.iloc[pivot_idx] >= confirmation_data.max():
                    pivots.iloc[i] = series.iloc[pivot_idx]
        
        return pivots

    def find_pivots_low_confirmed(self, series: pd.Series, window: int, confirmation: int = 3) -> pd.Series:
        """Trouve les pivots bas avec période de confirmation SANS lookahead bias"""
        pivots = pd.Series(index=series.index, dtype=float)
        
        for i in range(window + confirmation, len(series)):
            pivot_idx = i - confirmation
            
            if pivot_idx < window:
                continue
            
            # Vérifier si c'était un minimum local AU MOMENT du pivot
            window_data = series.iloc[pivot_idx-window:pivot_idx+1]
            
            if len(window_data) > 0 and series.iloc[pivot_idx] == window_data.min():
                # Confirmer que depuis le pivot, aucun prix n'est descendu sous ce niveau
                confirmation_data = series.iloc[pivot_idx+1:i+1]
                
                if len(confirmation_data) == 0 or series.iloc[pivot_idx] <= confirmation_data.min():
                    # le rsi était descendant au moins 3 périodes avant le pivot
                    if (series.iloc[pivot_idx - confirmation] > series.iloc[pivot_idx - confirmation + 1] > series.iloc[pivot_idx - confirmation + 2]):
                        pivots.iloc[i] = series.iloc[pivot_idx]
        
        return pivots


    # def find_pivots_high(self, series: pd.Series, window: int) -> pd.Series:
    #     """Trouve les pivots hauts"""
    #     pivots = pd.Series(index=series.index, dtype=float)
    #     for i in range(window, len(series) - window):
    #         if series.iloc[i-1] == series.iloc[i-window:i+window].max():
    #             pivots.iloc[i] = series.iloc[i]
    #     return pivots
    
    def find_pivots_high(self, series: pd.Series, window: int) -> pd.Series:
        """Trouve les pivots hauts sans lookahead bias"""
        pivots = pd.Series(index=series.index, dtype=float)
        for i in range(window, len(series)):
            # Only look at past and current data: i-window to i (inclusive)
            if series.iloc[i] == series.iloc[i-window:i+1].max():
                pivots.iloc[i] = series.iloc[i]
        return pivots

    # def find_pivots_low(self, series: pd.Series, window: int) -> pd.Series:
    #     """Trouve les pivots bas"""
    #     pivots = pd.Series(index=series.index, dtype=float)
    #     for i in range(window, len(series) - window):
    #         if series.iloc[i-1] == series.iloc[i-window:i+window].min():
    #             pivots.iloc[i] = series.iloc[i]
    #     return pivots
    
    def find_pivots_low(self, series: pd.Series, window: int) -> pd.Series:
        """Trouve les pivots bas sans lookahead bias"""
        pivots = pd.Series(index=series.index, dtype=float)
        for i in range(window, len(series)):
            # Only look at past and current data: i-window to i (inclusive)
            if series.iloc[i] == series.iloc[i-window:i+1].min():
                pivots.iloc[i] = series.iloc[i]
        return pivots

    def detect_bullish_divergence(self, dataframe: DataFrame) -> pd.Series:
        """
        Détecte une divergence haussière RSI avec conditions améliorées
        """
        divergence = pd.Series(False, index=dataframe.index)
    
        for i in range(self.lookback_period_for_divergence.value, len(dataframe)):
            # Cherche les 2 derniers pivots bas dans les prix
            recent_lows = dataframe['low_pivot'].iloc[i-self.lookback_period_for_divergence.value:i+1].dropna()
            
            if len(recent_lows) >= 2:
                # Prendre les 2 derniers pivots bas
                low_values = recent_lows.tail(2)
                low_indices = low_values.index
                
                if len(low_indices) >= 2:
                    first_low_idx = low_indices[-2]
                    second_low_idx = low_indices[-1]
                    
                    # Distance minimum entre pivots (éviter les faux signaux)
                    if second_low_idx - first_low_idx < 5:
                        continue
                    
                    # Vérifier si le prix fait un plus bas significatif (au moins 1%)
                    price_difference = (dataframe.loc[first_low_idx, 'low'] - dataframe.loc[second_low_idx, 'low']) / dataframe.loc[first_low_idx, 'low']
                    price_lower_low = price_difference > 0.01  # Au moins 1% de différence

                    # l'un des 2 plus bas au moins doit être sous la BB inférieure
                    bb_condition = (dataframe.loc[first_low_idx, 'low'] < dataframe.loc[first_low_idx, 'bb_lowerband']) or (dataframe.loc[second_low_idx, 'low'] < dataframe.loc[second_low_idx, 'bb_lowerband'])
                    if not bb_condition:
                        continue

                    # Le volume doit être au-dessus de la moyenne sur au moins l'un des 2 pivots
                    volume_condition = (dataframe.loc[first_low_idx, 'volume'] > dataframe.loc[first_low_idx, 'volume_sma']) or (dataframe.loc[second_low_idx, 'volume'] > dataframe.loc[second_low_idx, 'volume_sma'])
                    if not volume_condition:
                        continue
                    
                    # Vérifier si le RSI fait un plus haut (divergence)
                    # rsi_difference = dataframe.loc[second_low_idx, 'rsi'] - dataframe.loc[first_low_idx, 'rsi']
                    # rsi_higher_low = rsi_difference > 3  # Au moins 3 points de différence RSI
                    
                    # Confirmer que le RSI était en zone de survente
                    # rsi_oversold_condition = (dataframe.loc[first_low_idx, 'rsi'] < self.rsi_oversold.value and 
                    #                         dataframe.loc[second_low_idx, 'rsi'] < 50)
                    
                    # if price_lower_low and rsi_higher_low and rsi_oversold_condition:
                    #     # Marquer la divergence seulement si on est proche du pivot
                    #     if abs(i - second_low_idx) <= 3:
                    #         divergence.iloc[i] = True
                    if price_lower_low:
                        # Marquer la divergence seulement si on est proche du pivot
                        if abs(i - second_low_idx) <= 1:
                            divergence.iloc[i] = True
        
        return divergence

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Signaux d'achat basés sur divergence RSI haussière + bougie verte importante
        """
        
        dataframe.loc[
            (
                # Divergence haussière détectée
                (dataframe['bullish_divergence'].shift(1)) &
                
                # Bougie verte importante (au moins X% de hausse)
                # (dataframe['candle_size'] > self.candle_size_threshold.value) &
                (dataframe['close'] > dataframe['open']) &
                
                # Confirmation de tendance
                # (dataframe['close'] > dataframe['ema_20']) &
                
                # Volume au-dessus de la moyenne
                # (dataframe['volume'] > dataframe['volume_sma']) &
                
                # RSI pas en zone de surachat
                (dataframe['rsi'] < 70)
            ),
            'enter_long'] = 1

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Signaux de vente (optionnel, la stratégie utilise principalement ROI et stoploss)
        """
        
        # dataframe.loc[
        #     (
                # RSI en zone de surachat
                # (dataframe['rsi'] > 75) |
                
                # Cassure sous EMA 20
                # (dataframe['close'] < dataframe['ema_20'])
            # ),
            # 'exit_long'] = 1

        return dataframe


    def calculate_lowest_price_last_n_candles(self, pair: str, n_candles: int) -> float:
        """
        Calculate the lowest price from the last n candles
        :param pair: Trading pair
        :param n_candles: Number of candles to look back
        :return: Lowest price from the last n candles
        """
        dataframe, _ = self.dp.get_analyzed_dataframe(pair=pair, timeframe=self.timeframe)
        last_n_lows = dataframe['low'].iloc[-n_candles:]
        lowest_price = last_n_lows.min() * self.stoploss_margin.value  # 0.5% sous le plus bas
        return lowest_price

    use_custom_stoploss = True

    # Custom stoploss: Set the stoploss based on the lowest low of the last 8 candles before entry
    def custom_stoploss(self, pair: str, trade: Trade, current_time: datetime,
                        current_rate: float, current_profit: float, after_fill: bool, 
                        **kwargs) -> float | None:

        # 1. Si ce n'est pas le premier appel, ne pas toucher au stop-loss
        # if hasattr(trade, 'stop_price_ratio'):
        if self.use_custom_stoploss_param.value:
            if trade.get_custom_data("stop_price_ratio") is not None:
                return None

            # 2. Calcul du plus bas sur les 8 dernières bougies avant l'entrée
            lowest_price = self.calculate_lowest_price_last_n_candles(pair, self.lookback_period_for_stoploss.value)

            # 3. Convertir en ratio relatif au prix courant
            ratio = stoploss_from_absolute(lowest_price, current_rate,
                                        is_short=trade.is_short, leverage=trade.leverage)

            # 4. Stocker pour ne pas changer ensuite
            # setattr(trade, 'stop_price_ratio', ratio)
            trade.set_custom_data(key="stop_price_ratio", value=ratio)
            # print(f"Custom stoploss for {pair} at {current_time} is {trade.get_custom_data('stop_price_ratio')}")

        else:
            ratio = None
        # print(f"Custom stoploss for {pair} at {current_time} is {ratio}")
        return ratio

    def custom_stake_amount(self, pair: str, current_time: datetime, current_rate: float,
                            proposed_stake: float, min_stake: float, max_stake: float,
                            **kwargs) -> float:
        dataframe, _ = self.dp.get_analyzed_dataframe(pair=pair, timeframe=self.timeframe)
        if self.use_custom_stoploss_param.value:
            stoploss_price = self.calculate_lowest_price_last_n_candles(pair, self.lookback_period_for_pivots.value)
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
        
    
    def custom_sell(self, pair: str, trade: Trade, current_time: 'datetime', current_rate: float,
                    current_profit: float, **kwargs):
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