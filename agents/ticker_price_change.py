import os
import requests
from datetime import datetime, timedelta

def get_price_change(ticker, days, api_key):
    """
    Returns price change (absolute and %) for the given stock ticker over N days.
    """
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": ticker,
        "apikey": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    try:
        daily_data = data["Time Series (Daily)"]
        dates = sorted(daily_data.keys(), reverse=True)

        if len(dates) <= days:
            return None, f"Not enough trading data to compute a {days}-day change."

        latest_date = dates[0]
        old_date_actual = dates[days]

        latest_price = float(daily_data[latest_date]["4. close"])
        old_price = float(daily_data[old_date_actual]["4. close"])
        change = latest_price - old_price
        percent = (change / old_price) * 100
        direction = "increased" if change > 0 else "decreased"


        return {
            "start_date": old_date_actual,
            "end_date": latest_date,
            "old_price": old_price,
            "latest_price": latest_price,
            "change": change,
            "percent": percent,
            "direction": direction
        }, f"{ticker} has {direction} by {abs(percent):.2f}% over the last {days} day(s)."
        
    except KeyError:
        return None, f"Price change info not available for {ticker}."

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
    if not API_KEY:
        print("API key not found. Please set ALPHAVANTAGE_API_KEY in your .env file.")
        exit(1)

    ticker = input("Enter stock ticker (e.g., TSLA): ").upper()
    days_input = input("Enter days for price change (e.g., 7): ").strip()

    try:
        days = int(days_input)
        result, message = get_price_change(ticker, days, API_KEY)
        print(message)

        if result:
            print(f"""
                    Price on {result['start_date']}: ${result['old_price']:.2f}
                    Price on {result['end_date']}: ${result['latest_price']:.2f}
                    Change: ${result['change']:.2f} ({result['percent']:.2f}%)
                    """)
    except ValueError:
        print("Invalid number of days.")
