import smtplib
import requests
import datetime as dt

MY_LAT = 41.881832
MY_LNG = -87.623177
SENDER = ""
RECIPIENT = ""

def iss_overhead_check():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()["iss_position"]

    iss_lat = float(data["latitude"])
    iss_lng = float(data["longitude"])

    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LNG-5 <= iss_lng <=MY_LNG+5:
        return True
    else:
        return False

def night_check():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    sunresponse = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sunresponse.raise_for_status()
    data = sunresponse.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    current_hour = dt.datetime.now().hour

    if sunset <= current_hour < 24 or current_hour < sunrise:
        return True

def cloud_check():
    with open("api.key") as key:
        apikey = key.read()

    parameters = {
        "lat": MY_LAT,
        "lon": MY_LNG,
        "appid": apikey,
    }

    weatherresponse = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
    weatherresponse.raise_for_status()
    data = weatherresponse.json()

    return int(data["clouds"]["all"])

if iss_overhead_check() and night_check() and cloud_check() < 40:
    USERNAME = "apikey"
    with open("..\\..\\api.key") as key_file:
        PASSWORD = key_file.read()

    now = dt.datetime.now()
    today = (now.month, now.day)

    with smtplib.SMTP_SSL("smtp.sendgrid.net", 465) as connection:
        connection.ehlo()
        connection.login(USERNAME,PASSWORD)
        connection.sendmail(
            SENDER,
            RECIPIENT,
            f"from:{SENDER}\nSubject:ISS\n\nISS is overhead and the sky is visible."
        )