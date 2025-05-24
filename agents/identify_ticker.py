import os
import requests

def identify_ticker(query, api_key):
    """
    Extracts company name from user query and returns its stock ticker.
    """

    words = query.split()
    potential_company = None
    for word in words:
        if word[0].isupper() and word.lower() not in ["what", "why", "has", "with", "stock", "today"]:
            potential_company = word
            break

    if not potential_company:
        return None, "Could not identify the company name in query."

    url = "https://www.alphavantage.co/query"
    params = {
        "function": "SYMBOL_SEARCH",
        "keywords": potential_company,
        "apikey": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    try:
        best_match = data['bestMatches'][0]
        symbol = best_match['1. symbol']
        name = best_match['2. name']
        return symbol, f"Identified {name} as {symbol}"
    except (KeyError, IndexError):
        return None, "No matching ticker found."

if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

    if not API_KEY:
        print("API key not found. Please set ALPHAVANTAGE_API_KEY in your .env file.")
        exit(1)

    user_query = input("Enter a company name to identify its stock Ticker: ")
    ticker, message = identify_ticker(user_query, API_KEY)
    print(message)
    if ticker:
        print("Stock Ticker:", ticker)
