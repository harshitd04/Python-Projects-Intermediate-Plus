import requests
from twilio.rest import Client
from datetime import date, timedelta


# Function to get the most recent trading day
def get_recent_trading_date(api_data, start_date):
    """Find the closest previous trading day available in API data."""
    while start_date not in api_data["Time Series (Daily)"]:
        start_date = str(date.fromisoformat(start_date) - timedelta(days=1))
    return start_date


# Get today's and yesterday's date
date_today = str(date.today())
date_yesterday = str(date.today() - timedelta(days=1))

# Stock data API
stock_endpoint = "https://www.alphavantage.co/query"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": "",
}

stock_response = requests.get(url=stock_endpoint, params=stock_parameters)
stock_response.raise_for_status()
stock_json_data = stock_response.json()

big_change = False

try:
    # Get closest available trading dates
    date_today = get_recent_trading_date(stock_json_data, date_today)
    date_yesterday = get_recent_trading_date(stock_json_data, date_yesterday)

    # Convert string values to float before calculating difference
    today_close = float(stock_json_data["Time Series (Daily)"][date_today]["4. close"])
    yesterday_close = float(stock_json_data["Time Series (Daily)"][date_yesterday]["4. close"])

    difference = today_close - yesterday_close
    percentage_change = (difference / yesterday_close) * 100

    if abs(percentage_change) >= 10:
        big_change = True

except KeyError:
    print("Error: Could not retrieve stock data. Ensure the API key is valid and stock market data is available.")
except Exception as e:
    print(f"Unexpected error: {e}")

if True:
    news_endpoint = "https://newsapi.org/v2/everything"
    news_parameters = {
        "q": "Tesla|tesla|Elon|elon",
        "searchIn": "title",
        "apiKey": "",
        "sortBy": "popularity",
    }

    news_response = requests.get(url=news_endpoint, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()

    if "articles" in news_data and len(news_data["articles"]) > 0:
        news_title = news_data["articles"][0]["title"]
        # print(f"News: {news_title}")

        # Twilio API for sending SMS
        account_sid = ""
        auth_token = ""



        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"TSLA Stock Alert 🚀\nChange: {percentage_change:.2f}%\nLatest News: "
                 f"\n{news_data["articles"][0]["title"]}",
            from_="+1 9895107531",
            to="+91 9958983873"
        )
        print(f"Message Sent! Status: {message.status}")
        print(f"Message Body:{message.body}")



# Output:
# Message Sent! Status: queued
# Message Body:Sent from your Twilio trial account - TSLA Stock Alert 🚀
# Change: 0.00%
# Latest News:
# Elon Musk’s Toxicity Could Spell Disaster for Tesla