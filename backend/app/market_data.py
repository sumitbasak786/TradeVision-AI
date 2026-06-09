import random

def get_stock_data(symbol: str):
    return {
        "symbol": symbol.upper(),
        "price": round(random.uniform(1000, 3000), 2),
        "volume": random.randint(100000, 5000000),
        "change_percent": round(random.uniform(-5, 5), 2)
    }