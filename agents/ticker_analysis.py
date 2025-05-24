import os
from dotenv import load_dotenv
from ticker_price_change import get_price_change
from ticker_news import get_recent_news

def analyze_ticker_movement(ticker, price_change_info, news_headlines):
    """
    Combines price change info and news to give a basic reason summary.
    """
    direction = price_change_info["direction"]
    percent = price_change_info["percent"]
    change = price_change_info["change"]

    keywords_negative = ["miss", "lawsuit", "delay", "recall", "down", "cut", "crash", "regulator", "investigation"]
    keywords_positive = ["beats", "record", "surge", "rise", "growth", "deal", "approval", "launch", "expansion"]

    positive_hits = []
    negative_hits = []

    for headline in news_headlines:
        lower = headline.lower()
        if any(word in lower for word in keywords_positive):
            positive_hits.append(headline)
        elif any(word in lower for word in keywords_negative):
            negative_hits.append(headline)

    if direction == "increased" and positive_hits:
        reason = f"The stock has risen by {abs(percent):.2f}% likely due to positive news such as: {positive_hits[0]}"
    elif direction == "decreased" and negative_hits:
        reason = f"The stock has dropped by {abs(percent):.2f}% possibly due to: {negative_hits[0]}"
    elif news_headlines:
        reason = f"The stock has {direction} by {abs(percent):.2f}%, but the cause is unclear. Recent news includes: {news_headlines[0]}"
    else:
        reason = f"{ticker} has {direction} by {abs(percent):.2f}% over the recent period. No major news found."

    return reason


if __name__ == "__main__":
    load_dotenv()
    API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

    if not API_KEY:
        print("API key not found. Please set ALPHAVANTAGE_API_KEY in your .env file.")
        exit(1)

    ticker = input("Enter stock ticker (e.g., TSLA): ").strip().upper()
    days_input = input("Enter number of days to analyze (e.g., 7): ").strip()

    try:
        days = int(days_input)
    except ValueError:
        print("Invalid number of days.")
        exit(1)

    # Get price change info
    price_change_info, price_msg = get_price_change(ticker, days, API_KEY)
    print(price_msg)
    if not price_change_info:
        exit(1)

    # Get news
    news_headlines, news_msg = get_recent_news(ticker, API_KEY)
    print(news_msg)
    if not news_headlines:
        news_headlines = []

    # Get analysis summary
    summary = analyze_ticker_movement(ticker, price_change_info, news_headlines)
    print("\nAnalysis Summary:")
    print(summary)
