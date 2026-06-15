import random


def generate_ai_prediction(symbol: str):

    confidence = round(random.uniform(70, 95), 2)

    signals = ["BUY", "SELL", "HOLD"]

    signal = random.choice(signals)

    return {
        "symbol": symbol.upper(),
        "signal": signal,
        "confidence": confidence,
        "model": "TradeVision-AI-v1"
    }