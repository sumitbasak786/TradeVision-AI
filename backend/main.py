from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    return {
        "symbol": symbol.upper(),
        "signal": "HOLD",
        "confidence": 62.34,
        "prediction_horizon": "5 minutes"
    }