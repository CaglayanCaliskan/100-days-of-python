import datetime
from dotenv import load_dotenv
import os
import requests

load_dotenv()
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.getenv('ALPHAVANTAGE_API')
NEWS_API_KEY = os.getenv('NEWSAPI_API')


# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
ereyesterdat = today - datetime.timedelta(days=2)

yesterday_close_price = response.json(
)["Time Series (Daily)"][str(yesterday)]["4. close"]

print(yesterday_close_price)


# TODO 2. - Get the day before yesterday's closing stock price

ereyesterday_close_price = response.json(
)["Time Series (Daily)"][str(ereyesterdat)]["4. close"]

print(ereyesterday_close_price)


# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = abs(float(yesterday_close_price) -
                 float(ereyesterday_close_price))
print(difference)


# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

diff_percent = difference / float(yesterday_close_price) * 100
print(diff_percent)


# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

def getNews():
    stock_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "searchIn": "title"
    }

    response = requests.get(NEWS_ENDPOINT, params=stock_params)
    return response.json()


if diff_percent > 2:
    print("Get News")
    news = getNews()["articles"]
    print(news[:3])

else:
    print("low price")

# STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
#Done in todo5

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
