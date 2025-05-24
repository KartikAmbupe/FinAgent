import os
from dotenv import load_dotenv
from agents.identify_ticker import identify_ticker
from agents.ticker_price_change import get_price_change
from agents.ticker_news import get_recent_news
from agents.ticker_analysis import analyze_ticker_movement

import re

def extract_days_from_query(query):
    """
    Try to extract timeframe like '7 days', 'today', 'last week' from the query.
    Defaults to 7 if unclear.
    """
    query = query.lower()
    if "today" in query:
        return 1
    if "yesterday" in query:
        return 1
    if "week" in query:
        return 7
    if "month" in query:
        return 30
    match = re.search(r"(\d+)\s*(day|days)", query)
    if match:
        return int(match.group(1))
    return 7 

def main():
    load_dotenv()
    API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
    if not API_KEY:
        print("API key not found. Please set ALPHAVANTAGE_API_KEY in your .env file.")
        return

    # Ask user for input
    query = input("📝 Ask your stock-related question: ")

    # Identify the ticker
    ticker, ticker_msg = identify_ticker(query, API_KEY)
    print("🔍", ticker_msg)
    if not ticker:
        return

    # Extract number of days
    days = extract_days_from_query(query)
    print(f"🕒 Timeframe detected: last {days} day(s)")

    # Get price change
    price_change_info, price_msg = get_price_change(ticker, days, API_KEY)
    print("📉", price_msg)
    if not price_change_info:
        return

    # Get news
    news_headlines, news_msg = get_recent_news(ticker, API_KEY)
    print("🗞️", news_msg)
    if not news_headlines:
        news_headlines = []

    # Analyze
    summary = analyze_ticker_movement(ticker, price_change_info, news_headlines)
    print("\n📊 Analysis Summary:")
    print(summary)

if __name__ == "__main__":
    main()
