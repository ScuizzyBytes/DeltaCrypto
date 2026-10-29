import requests

prices = {}

def get_prices():
    url = "https://api.binance.com/api/v3/ticker/price"
    symbols = ["BTCUSDT","ETHUSDT","BNBUSDT","TONUSDT"]

    for symbol in symbols:
        response = requests.get(url, params={"symbol": symbol}, timeout=5)
        price = float(response.json()["price"])
        prices[symbol] = price
    return prices