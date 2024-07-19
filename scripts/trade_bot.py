import requests
import pandas as pd

ROBINHOOD_API_URL = "https://api.robinhood.com"
ACCESS_TOKEN = "your_robinhood_access_token"

def place_order(symbol, quantity, order_type="market", side="buy"):
    url = f"{ROBINHOOD_API_URL}/orders/"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "account": "your_account_url",
        "instrument": {
            "symbol": symbol
        },
        "quantity": quantity,
        "side": side,
        "type": order_type,
        "time_in_force": "gfd"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

if __name__ == "__main__":
    symbol = 'AAPL'
    quantity = 1
    response = place_order(symbol, quantity)
    print(response)
