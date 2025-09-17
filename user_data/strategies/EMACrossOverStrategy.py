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


class EMACrossOverStrategy(IStrategy):
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
    trailing_stop = True

    # Hyperopt parameters
    # rsi_entry_max = IntParameter(30, 70, default=50, space="buy", optimize=True)
    # rsi_entry_min = IntParameter(10, 50, default=20, space="buy", optimize=True)
    # volume_factor = DecimalParameter(0.1, 3, default=0.1, space="buy", optimize=False)
    # window_macd_cross = IntParameter(3, 10, default=5, space="buy", optimize=True)
    # macd_threshold = IntParameter(-200, 0, default=0, space="buy", optimize=False)

    use_custom_stoploss_param = BooleanParameter(default=False, space="sell", optimize=False)
    lookback_period_for_stoploss = IntParameter(0, 10, default=5, space="sell", optimize=False)
    take_profit_multiplier = CategoricalParameter([1, 1.5, 2, 2.5, 3], default=2, space="sell", optimize=False)
    stoploss_margin = DecimalParameter(0.990, 1, default=0.999, space="sell", optimize=False)

    threshold_percentage = IntParameter(0, 10, default=1, space="sell", optimize=False)

    use_custom_stoploss = use_custom_stoploss_param.value

    # Optimal stoploss designed for the strategy.
    stoploss = -0.15  # Stoploss initial de -15% (sera ajusté dynamiquement)
    # stoploss = -fix_stoploss_value_param.value  # Stoploss initial de -10% (sera ajusté dynamiquement)

    # Plotting configuration
    plot_config = {
        "main_plot": {
            'ema': {'color': 'purple'},
            "stoploss_prices": {
                "color": "grey",
                "linestyle": "dotted",
            },
        },
        "subplots": {
            "MACD": {
                "macd": {"color": "blue"},
                "macd_signal": {"color": "orange"},
                "macd_hist": {"color": "green", "type": "bar"},
            },
            "RSI": {
                "rsi": {"color": "purple"},
            },
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

        # EMAs 8, 13 and 21
        # dataframe['ema8'] = ta.EMA(dataframe, timeperiod=8)
        # dataframe['ema13'] = ta.EMA(dataframe, timeperiod=13)
        # dataframe['ema21'] = ta.EMA(dataframe, timeperiod=21)
        dataframe['ema'] = ta.EMA(dataframe, timeperiod=800)

        # EMA threshold
        dataframe['ema_threshold'] = dataframe['ema'] * (100 - self.threshold_percentage.value) / 100

        # RSI
        dataframe['rsi'] = ta.RSI(dataframe, timeperiod=14)

        # MACD
        macd = ta.MACD(dataframe)
        dataframe['macd'] = macd['macd']
        dataframe['macd_signal'] = macd['macdsignal']
        dataframe['macd_hist'] = macd['macdhist']

        # MACD crossover detection - True when MACD crossed above signal within last 5 candles
        dataframe['macd_cross_above'] = qtpylib.crossed_above(dataframe['macd'], dataframe['macd_signal'])
        # dataframe['macd_cross_above_last_X'] = dataframe['macd_cross_above'].rolling(window=self.window_macd_cross.value).max().astype(bool)

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

        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Signaux d'achat basés sur croisement MACD + EMA + volume
        - MACD sous zéro et croise au-dessus de sa ligne de signal
        - Bougie haussière
        - EMA 8 au-dessus de EMA 13 et EMA 13 au-dessus de EMA 21
        - Volume supérieur à la moyenne
        """

        dataframe.loc[
            (
                # Close price crossed above EMA
                (qtpylib.crossed_above(dataframe['close'], dataframe['ema'])) &
                # Ensure this candle had volume (important for backtesting)
                (dataframe['volume'] > 0)
            ),
            "enter_long",
        ] = 1

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Signaux de vente (optionnel, la stratégie utilise principalement ROI et stoploss)
        """

        dataframe.loc[
            (
                # Close price crossed below EMA threshold
                (qtpylib.crossed_below(dataframe["close"], dataframe["ema_threshold"]))
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

    use_custom_stoploss = True

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

            # 4. Stocker pour ne pas changer ensuite
            # setattr(trade, 'stop_price_ratio', ratio)
            trade.set_custom_data(key="stop_price_ratio", value=ratio)
            # print(f"Custom stoploss for {pair} at {current_time} is {trade.get_custom_data('stop_price_ratio')}")

        else:
            ratio = None
        # print(f"Custom stoploss for {pair} at {current_time} is {ratio}")
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
