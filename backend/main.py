from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

from app.market_data import get_market_data
from app.indicators import get_signal

app = FastAPI(
    title="TradeVision AI API"
)

# CORS
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

    signal_data = get_signal(symbol)

    return {
        "symbol": symbol.upper(),
        "signal": signal_data["signal"],
        "confidence": signal_data["confidence"],
        "prediction_horizon": "5 minutes",
        "rsi": signal_data["rsi"],
        "ema20": signal_data["ema20"],
        "ema50": signal_data["ema50"],
        "trend": signal_data["trend"]
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

        signal_data = get_signal(stock)

        results.append({
            "symbol": stock,
            "signal": signal_data["signal"],
            "confidence": signal_data["confidence"]
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

        signal_data = get_signal(stock)

        if signal_data["signal"] == "BUY":
            buy_count += 1

        elif signal_data["signal"] == "SELL":
            sell_count += 1

        else:
            hold_count += 1

    return {
        "buy_signals": buy_count,
        "sell_signals": sell_count,
        "hold_signals": hold_count
    }