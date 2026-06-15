import yfinance as yf

from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator


def get_signal(symbol="RELIANCE.NS"):

    try:
        df = yf.download(
            symbol,
            period="3mo",
            interval="1d",
            auto_adjust=True,
            progress=False
        )

        print("\n==============================")
        print("Ticker:", symbol)
        print("Rows:", len(df))
        print(df.tail())
        print("==============================\n")

        if df.empty or len(df) < 60:
            return {
                "signal": "HOLD",
                "confidence": 50,
                "rsi": 0,
                "ema20": 0,
                "ema50": 0,
                "trend": "Neutral"
            }

        close = df["Close"]

        rsi = RSIIndicator(
            close=close,
            window=14
        ).rsi()

        ema20 = EMAIndicator(
            close=close,
            window=20
        ).ema_indicator()

        ema50 = EMAIndicator(
            close=close,
            window=50
        ).ema_indicator()

        latest_rsi = round(float(rsi.iloc[-1]), 2)
        latest_ema20 = round(float(ema20.iloc[-1]), 2)
        latest_ema50 = round(float(ema50.iloc[-1]), 2)

        signal = "HOLD"
        confidence = 60

        if latest_rsi < 30 and latest_ema20 > latest_ema50:
            signal = "BUY"
            confidence = 90

        elif latest_rsi > 70 and latest_ema20 < latest_ema50:
            signal = "SELL"
            confidence = 90

        elif latest_ema20 > latest_ema50:
            signal = "BUY"
            confidence = 75

        elif latest_ema20 < latest_ema50:
            signal = "SELL"
            confidence = 75

        return {
            "signal": signal,
            "confidence": confidence,
            "rsi": latest_rsi,
            "ema20": latest_ema20,
            "ema50": latest_ema50,
            "trend": (
                "Bullish"
                if latest_ema20 > latest_ema50
                else "Bearish"
            )
        }

    except Exception as e:

        print("\n==============================")
        print("INDICATOR ERROR")
        print(e)
        print("==============================\n")

        return {
            "signal": "HOLD",
            "confidence": 50,
            "rsi": 0,
            "ema20": 0,
            "ema50": 0,
            "trend": "Neutral"
        }