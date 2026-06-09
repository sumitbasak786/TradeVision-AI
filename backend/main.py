from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import yfinance as yf

app = FastAPI(
    title="TradeVision AI API"
)

# =========================
# CORS
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
# Home
# =========================

@app.get("/")
def home():
    return {
        "message": "TradeVision AI Backend Running"
    }

# =========================
# Market Data
# =========================

@app.get("/market/{symbol}")
def market_data(symbol: str):

    ticker = yf.Ticker(f"{symbol.upper()}.NS")

    info = ticker.info

    return {
        "symbol": symbol.upper(),
        "price": round(info.get("currentPrice", 0), 2),
        "volume": info.get("volume", 0),
        "change_percent": round(info.get("regularMarketChangePercent", 0), 2)
    }

# =========================
# Prediction
# =========================

@app.get("/prediction/{symbol}")
def prediction(symbol: str):

    ticker = yf.Ticker(f"{symbol.upper()}.NS")

    info = ticker.info

    change_percent = info.get("regularMarketChangePercent", 0)

    if change_percent > 2:
        signal = "BUY"
        confidence = 88.0

    elif change_percent < -2:
        signal = "SELL"
        confidence = 85.0

    else:
        signal = "HOLD"
        confidence = 70.0

    return {
        "symbol": symbol.upper(),
        "signal": signal,
        "confidence": confidence,
        "prediction_horizon": "5 minutes",
        "market_change_percent": round(change_percent, 2)
    }