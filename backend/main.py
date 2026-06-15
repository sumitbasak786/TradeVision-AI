from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.market_data import get_market_data
from app.indicators import get_signal
from app.ml_engine import generate_ai_prediction

app = FastAPI(
    title="TradeVision AI API"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "TradeVision AI Backend Running"
    }


@app.get("/prediction/{symbol}")
def prediction(symbol: str):

    symbol_map = {
        "reliance": "RELIANCE.NS",
        "tcs": "TCS.NS",
        "infy": "INFY.NS",
        "hdfcbank": "HDFCBANK.NS",
        "icicibank": "ICICIBANK.NS",
        "sbin": "SBIN.NS",
        "itc": "ITC.NS",
        "lt": "LT.NS"
    }

    ticker = symbol_map.get(
        symbol.lower(),
        f"{symbol.upper()}.NS"
    )

    signal_data = get_signal(ticker)

    return {
        "symbol": symbol.upper(),
        "signal": signal_data.get("signal", "HOLD"),
        "confidence": signal_data.get("confidence", 50),
        "prediction_horizon": "5 minutes",
        "rsi": signal_data.get("rsi", 0),
        "ema20": signal_data.get("ema20", 0),
        "ema50": signal_data.get("ema50", 0),
        "trend": signal_data.get("trend", "Neutral")
    }


@app.get("/market/{symbol}")
def market(symbol: str):
    return get_market_data(symbol)


@app.get("/top-signals")
def top_signals():

    stocks = [
        "RELIANCE",
        "TCS",
        "INFY",
        "HDFCBANK",
        "ICICIBANK",
        "SBIN",
        "ITC",
        "LT"
    ]

    results = []

    for stock in stocks:

        ticker = f"{stock}.NS"

        signal_data = get_signal(ticker)

        results.append({
            "symbol": stock,
            "signal": signal_data.get("signal", "HOLD"),
            "confidence": signal_data.get("confidence", 50)
        })

    return results


@app.get("/dashboard-summary")
def dashboard_summary():

    buy_count = 0
    sell_count = 0
    hold_count = 0

    stocks = [
        "RELIANCE",
        "TCS",
        "INFY",
        "HDFCBANK",
        "ICICIBANK",
        "SBIN",
        "ITC",
        "LT"
    ]

    for stock in stocks:

        ticker = f"{stock}.NS"

        signal_data = get_signal(ticker)

        signal = signal_data.get("signal", "HOLD")

        if signal == "BUY":
            buy_count += 1

        elif signal == "SELL":
            sell_count += 1

        else:
            hold_count += 1

    return {
        "buy_signals": buy_count,
        "sell_signals": sell_count,
        "hold_signals": hold_count
    }


@app.get("/ai-prediction/{symbol}")
def ai_prediction(symbol: str):

    return generate_ai_prediction(symbol)