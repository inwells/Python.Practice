import smtplib
import datetime as dt
import random


USERNAME = "apikey"
PASSWORD = ""

now = dt.datetime.now()
weekday = now.weekday()


if weekday == 0:
    with open("quotes.txt") as quote_files:
        quotes = quote_files.readlines()
        quote = random.choice(quotes)

    print(quote)

    with smtplib.SMTP_SSL("smtp.sendgrid.net", 465) as connection:
        connection.ehlo()
        connection.login(USERNAME,PASSWORD)
        connection.sendmail(
            "Johann <johann@itwells.com>",
            "",
            f"from:johann@itwells.com\nSubject:Monday Motivation\n\n{quote}"
        )