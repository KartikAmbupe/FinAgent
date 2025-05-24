import os
import requests

def get_recent_news(ticker, api_key):
    """
    Fetches recent news articles about the given stock ticker.
    """
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "NEWS_SENTIMENT",
        "tickers": ticker,
        "apikey": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    try:
        news_items = data["feed"][:5]  # Get top 5 recent news
        summaries = [
            f"{item['title']} ({item['source']}) - {item['url']}"
            for item in news_items
        ]
        return summaries, f"Fetched {len(summaries)} news articles for {ticker}"
    except KeyError:
        return None, f"No recent news found for {ticker}."

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
    if not API_KEY:
        print("API key not found. Please set ALPHAVANTAGE_API_KEY in your .env file.")
        exit(1)

    ticker = input("Enter stock ticker for news (e.g., TSLA): ").upper()
    news_list, message = get_recent_news(ticker, API_KEY)

    print(message)
    if news_list:
        print("\nRecent News Headlines:")
        for i, news in enumerate(news_list, 1):
            print(f"{i}. {news}")
