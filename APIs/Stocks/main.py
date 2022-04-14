import json
import requests
import smtplib
import datetime as dt
import os

TODAY = dt.datetime.now()
DATE = TODAY.date()
if TODAY.weekday() == 6:
    YST_MOD = 2
elif TODAY.weekday() == 0:
    YST_MOD = 3
else: YST_MOD = 1
YESTERDAY = TODAY - dt.timedelta(days = YST_MOD)
YESTERDAY_DATE = str(YESTERDAY.date())
if TODAY.weekday() == 1:
    B4_MOD = YST_MOD + 3
else: B4_MOD = YST_MOD + 1
DAY_B4 = TODAY - dt.timedelta(days = B4_MOD)
DAY_B4_DATE = str(DAY_B4.date())
print(YESTERDAY_DATE)
print(DAY_B4_DATE)

SYMBOL = "UPST"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

with open("api.key") as key_file:
        APIKEYS = json.load(key_file)

SG_KEY = os.getenv("SG_KEY")
EMAIL = os.getenv("W_Mail")

def send_mail(subject, body):
    with smtplib.SMTP_SSL("smtp.sendgrid.net", 465) as connection:
        connection.ehlo()
        connection.login("apikey",SG_KEY)
        msg = f"from:{EMAIL}\nSubject:{subject}\n\n{body}."
        connection.sendmail(
            EMAIL,
            EMAIL,
            msg.encode("utf8")
        )

def process_news():
    parameters = {
        "q": COMPANY_NAME,
        "searchIn": "description,content",
        "from": TODAY,
        "sortBy": "publishedAt",
        "totalResults": "10",
        "apikey": APIKEYS["NewsAPI"],
    }

    news_data = requests.get(NEWS_ENDPOINT, params=parameters)
    news_data.raise_for_status()
    news_dict = news_data.json()
    news = news_dict["articles"]

    for article in news[:1]:
        send_mail(article["title"], article["description"])

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": SYMBOL,
    "datatype": "json",
    "outputsize": "compact",
    "apikey": APIKEYS["AlphaVantage"],
}

stock_data = requests.get(STOCK_ENDPOINT, params=parameters)
stock_data.raise_for_status()
stock_dict = stock_data.json()
stock = stock_dict["Time Series (Daily)"]

if float(stock[DAY_B4_DATE]["4. close"]) >= float(stock[YESTERDAY_DATE]["4. close"]) * 1.05:
    print("🔺5%")
    process_news()
elif float(stock[DAY_B4_DATE]["4. close"]) <= float(stock[YESTERDAY_DATE]["4. close"]) * 0.95:
    print("🔻5%")
    process_news()



