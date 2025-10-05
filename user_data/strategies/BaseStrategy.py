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


class BaseStrategy(IStrategy):
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
    rsi_entry_max = IntParameter(50, 100, default=70, space="buy", optimize=False)
    rsi_entry_min = IntParameter(0, 50, default=10, space="buy", optimize=False)
    volume_factor = CategoricalParameter([0, 0.25, 0.5, 1, 1.5, 2, 2.5, 3], default=0.5, space="buy", optimize=True)
    entry_adx_threshold = CategoricalParameter([0, 5, 10, 15, 20, 25, 30, 40, 50], default=5, space="buy", optimize=False)

    use_custom_stoploss_param = BooleanParameter(default=True, space="sell", optimize=False)
    lookback_period_for_stoploss = IntParameter(1, 10, default=5, space="sell", optimize=False)
    take_profit_multiplier = CategoricalParameter([1, 1.5, 2, 2.5, 3], default=2, space="sell", optimize=False)
    stoploss_margin = DecimalParameter(0.990, 1, default=0.999, space="sell", optimize=False)
    use_custom_stoploss_type = CategoricalParameter(['lower', 'atr', 'lower_and_atr', 'none'], default='lower', space="sell", optimize=False)
    use_custom_sell = BooleanParameter(default=True, space="sell", optimize=False)
    use_sell_signal_param = BooleanParameter(default=True, space="sell", optimize=False)
    atr_stoploss_multiplier = CategoricalParameter([0.5, 1, 1.5, 2, 2.5, 3], default=1.5, space="sell", optimize=False)
    custom_sell_atr_factor = CategoricalParameter([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6], default=4.5, space="sell", optimize=False)
    trailing_custom_stop = BooleanParameter(default=True, space="sell", optimize=False)

    use_custom_stoploss = use_custom_stoploss_param.value

    # Strategy configuration - plain boolean values expected by Freqtrade
    use_exit_signal = use_sell_signal_param.value

    # Optimal stoploss designed for the strategy.
    stoploss = -0.1  # Stoploss initial de -10% (sera ajusté dynamiquement)
    # stoploss = -fix_stoploss_value_param.value  # Stoploss initial de -10% (sera ajusté dynamiquement)

    # Plotting configuration
    plot_config = {
        "main_plot": {
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
            "Volume": {
                "volume": {"color": "blue", "type": "bar"},
                "volume_sma": {"color": "orange"},
            },
            "rsi": {
                "rsi": {"color": "purple"},
            },
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
        return dataframe

    @informative('4h')
    # @informative('1d', 'BTC/{stake}', fmt='{base}_{column}_{timeframe}')
    def populate_indicators_4h(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        return dataframe

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Ajoute les indicateurs techniques nécessaires
        """

        # Volume moyen pour confirmation
        dataframe["volume_sma"] = dataframe["volume"].rolling(window=20).mean()
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
        # indicators to help debugging and strategy tuning
        dataframe['rsi'] = ta.RSI(dataframe, timeperiod=14)
        dataframe['adx'] = ta.ADX(dataframe, timeperiod=14)

        return dataframe

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

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Signaux de vente (optionnel, la stratégie utilise principalement ROI et stoploss)
        """
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
            .iloc[max(0, i - self.lookback_period_for_stoploss.value) : i+1]
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
            return stoploss_price_lower - (self.atr_stoploss_multiplier.value * current_atr)
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
