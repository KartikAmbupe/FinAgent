# agents/ticker_price.py

import os
import requests

def get_current_price(ticker, api_key):
    """
    Fetches the latest intraday price for a given stock ticker.
    """
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": ticker,
        "interval": "5min",
        "outputsize": "compact",
        "apikey": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    try:
        time_series = data["Time Series (5min)"]
        latest_timestamp = sorted(time_series.keys())[0]  # Most recent entry
        latest_data = time_series[latest_timestamp]
        latest_price = latest_data["4. close"]
        return float(latest_price), f"Price of {ticker} as of {latest_timestamp} is ${latest_price}"
    except KeyError:
        return None, f"Could not retrieve price for {ticker}."

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
    if not API_KEY:
        print("API key not found. Please set ALPHAVANTAGE_API_KEY in your .env file.")
        exit(1)

    ticker = input("Enter a stock ticker (e.g., TSLA): ").upper()
    price, message = get_current_price(ticker, API_KEY)
    print(message)
    if price:
        print("Current Price: $", price)
