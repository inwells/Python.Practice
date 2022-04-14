import requests
import os

#original design was to send SMS, but I did not want to implement that.

MY_LAT = 41.881832
MY_LNG = -87.623177
OW_KEY = os.getenv("OWEATH_KEY")
SENDER = ""
RECIPIENT = ""

def check_for_rain(data):
    for hour in data["hourly"][:10]:
        if int(hour["weather"][0]["id"]) < 700:
            return True

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": OW_KEY,
    "exclude": "minutely,daily"
}

weatherresponse = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
weatherresponse.raise_for_status()
data = weatherresponse.json()

if check_for_rain(data) == True:
    print("is gon' rain!")