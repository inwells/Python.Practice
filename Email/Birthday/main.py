import smtplib
import datetime as dt
import pandas
import random

USERNAME = "apikey"
with open("..\\..\\api.key") as key_file:
    PASSWORD = key_file.read()

now = dt.datetime.now()
today = (now.month, now.day)

def send_mail(email, content):
    with smtplib.SMTP_SSL("smtp.sendgrid.net", 465) as connection:
        connection.ehlo()
        connection.login(USERNAME,PASSWORD)
        connection.sendmail(
            "Johann <johann@itwells.com>",
            email,
            f"from:johann@itwells.com\nSubject:Hello\n\n{content}."
        )

    ##################### Extra Hard Starting Project ######################

data = pandas.read_csv("birthdays.csv")

#use add value to overlapping birthdays into an array
birth_dict = {(data_row["month"], data_row["day"]):{"fname":data_row["firstname"], "lname":data_row["lastname"], "email":data_row["email"]} for (index, data_row) in data.iterrows()}


if today in birth_dict:
    num = random.randrange(1,3)
    letter = f"letter_templates\letter_{num}.txt"
    with open(letter) as letter_file:
        contents = letter_file.read()
        fname = birth_dict[today]["fname"]
        lname = birth_dict[today]["lname"]
        contents.replace("[NAME]",f"{fname} {lname}")
        send_mail(birth_dict[today]["email"], contents)




# 4. Send the letter generated in step 3 to that person's email address.
