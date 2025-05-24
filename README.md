# FinAgent

# 📊 Stock Analysis Multi-Agent System

A modular multi-agent system that answers stock-related questions using real-time data and news analysis. It fetches ticker symbols, price trends, recent news, and gives intelligent explanations — all from natural language queries.

---

## 🚀 Features

- ✅ Detect stock ticker from natural queries
- 📈 Fetch latest price and change over N days
- 🗞️ Retrieve recent news headlines
- 🧠 Analyze likely cause of price movement
- 💬 Understand natural language and structured inputs

---

## 🧠 Example Queries

- "Why did Tesla stock drop today?"
- "What’s going on with Apple this month?"
- "How has Microsoft performed in the last 10 days?"
- "Tell me about Palantir stock this week."

---

## 🧰 Subagents Used

| Agent Name          | Role                                                       |
|---------------------|------------------------------------------------------------|
| `identify_ticker`   | Extracts stock ticker from user input                      |
| `ticker_price`      | Retrieves current stock price (optional for future use)    |
| `ticker_price_change` | Calculates % and $ change over a given timeframe        |
| `ticker_news`       | Retrieves recent news headlines using Alpha Vantage API    |
| `ticker_analysis`   | Summarizes reason for stock movement using data + news     |

---

## 🛠️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/KartikAmbupe/FinAgent.git
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your API key

Create a `.env` file in the root directory:

```
ALPHAVANTAGE_API_KEY=your_api_key
```

Get a free API key from 👉 [Alpha Vantage](https://www.alphavantage.co/support/#api-key)

---

## 🧪 Running the Project

```bash
python main.py
```

You’ll be prompted to enter a natural language query like:

```
📝 Ask your stock-related question: Why did Tesla stock drop this week?
```

Then the system will:
- Detect the ticker
- Extract timeframe
- Fetch price change and news
- Provide a summary analysis

---

## 🧪 Sample Output

```
🔍 Identified Tesla Inc as TSLA
🕒 Timeframe detected: last 7 day(s)
📉 TSLA has decreased by 3.42% over the last 7 day(s).
🗞️ Fetched 5 news articles for TSLA

📊 Analysis Summary:
The stock has dropped by 3.42% possibly due to: Tesla misses Q1 earnings expectations
```

---

## 🧠 Agent Modularity

Each agent is written as a separate module and can be extended or replaced without affecting the system. You can:
- Swap news APIs (e.g., use NewsAPI instead of Alpha Vantage)
- Use NLP libraries (spaCy/NLTK) to improve ticker detection
- Add real-time trading features or sentiment scoring

---

## 📦 Requirements

- Python 3.7+
- `requests`
- `python-dotenv`

---



