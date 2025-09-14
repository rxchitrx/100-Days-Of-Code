import requests
import newsapi
from datetime import datetime, timedelta
from twilio.rest import Client





STOCK_DATA_API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
STOCK_API = "https://www.alphavantage.co/query"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
account_sid = "YOUR_TWILIO_ACCOUNT_SID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"

newsapi = newsapi.NewsApiClient(api_key=NEWS_API_KEY)

companies = [
    {"symbol" : "AAPL", "name" : "Apple Inc"},
    {"symbol": "MSFT", "name": "Microsoft Corp"},
    {"symbol": "GOOGL", "name": "Alphabet Inc"},
    {"symbol": "AMZN", "name": "Amazon.com Inc"},
    {"symbol": "META", "name": "Meta Platforms Inc"},
    {"symbol": "TSLA", "name": "Tesla Inc"},
    {"symbol": "NVDA", "name": "NVIDIA Corp"},
    {"symbol": "BRK.B", "name": "Berkshire Hathaway Inc"},
    {"symbol": "JPM", "name": "JP Morgan Chase"},
    {"symbol": "V", "name": "Visa Inc"}
]

for c in companies:
    stock_params = {
        "function" : "TIME_SERIES_DAILY",
        "symbol": c["symbol"],
        "datatype": "json",
        "apikey": STOCK_DATA_API_KEY,
    }

    response = requests.get(url=STOCK_API, params=stock_params)
    response.raise_for_status()
    data = response.json()

    if "Time Series (Daily)" not in data:
        print(f"Stock data not available for {c['name']}")
        continue

    available_dates = list(data["Time Series (Daily)"])

    date_before_yest = available_dates[1]
    date_yest = available_dates[0]
    closing_data_day_before = float(data["Time Series (Daily)"][date_before_yest]["4. close"])
    opening_data_yesterday = float(data["Time Series (Daily)"][date_yest]["1. open"])
    percentage_change = ((opening_data_yesterday - closing_data_day_before)/closing_data_day_before) * 100


    top_headlines = newsapi.get_everything(q=c['name'])
    articles = top_headlines["articles"][:3]

    news_text = ""
    for article in articles:
        news_text += (
            f"Headline: {article['title']}\n"
            f"Brief: {article['description']}\n"
        )


    client = Client(account_sid, auth_token)
    message = client.messages.create(
                from_="whatsapp:YOUR_TWILIO_NUMBER",
        body=f"{c['name']} : {'🔺' if percentage_change > 0 else '🔻'} {percentage_change:.2f}%\n{news_text}",
        to="whatsapp:DESTINATION_NUMBER"
    )