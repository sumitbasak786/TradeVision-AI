from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(
    title="TradeVision AI API"
)

# =========================
# CORS Configuration
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# Home Endpoint
# =========================

@app.get("/")
def home():
    return {
        "message": "TradeVision AI Backend Running"
    }

# =========================
# Prediction Endpoint
# =========================

@app.get("/prediction/{symbol}")
def prediction(symbol: str):

    signals = ["BUY", "SELL", "HOLD"]

    return {
        "symbol": symbol.upper(),
        "signal": random.choice(signals),
        "confidence": round(random.uniform(65, 95), 2),
        "prediction_horizon": "5 minutes"
    }

# =========================
# Market Data Endpoint
# =========================

@app.get("/market-data/{symbol}")
def market_data(symbol: str):

    return {
        "symbol": symbol.upper(),
        "price": round(random.uniform(2200, 2800), 2),
        "volume": random.randint(100000, 900000),
        "change_percent": round(random.uniform(-5, 5), 2)
    }

# =========================
# Multi Stock Scanner
# =========================

@app.get("/scanner")
def scanner():

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

    signals = ["BUY", "SELL", "HOLD"]

    results = []

    for stock in stocks:
        results.append({
            "symbol": stock,
            "signal": random.choice(signals),
            "confidence": round(random.uniform(65, 95), 2)
        })

    return results