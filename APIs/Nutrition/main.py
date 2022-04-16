import requests
import json
import datetime as dt

GENDER = "male"
WEIGHT_KG = 63.50
HEIGHT_CM = 176.53
AGE = 33

TODAY = dt.datetime.now().strftime("%m/%d/%Y")
TIME = dt.datetime.now().strftime("%H:%M:%S")

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

with open("api.key") as key_file:
        apikeys = json.load(key_file)

ex_text = input("Tell me which exercises you did: ")

APPID = apikeys["appid"]
KEY = apikeys["apikey"]
AUTH = apikeys["auth"]

headers = {
    "x-app-id": APPID,
    "x-app-key": KEY
}

parameters = {
 "query":ex_text,
 "gender":GENDER,
 "weight_kg":WEIGHT_KG,
 "height_cm":HEIGHT_CM,
 "age":AGE
}

response = requests.post(EXERCISE_ENDPOINT, json=parameters, headers=headers)
ex_data = response.json()

SHEETY_ENDPOINT = "https://api.sheety.co/6cd2f5c6f13474582b53d88e3ce1fd30/myWorkouts/workouts"

for exercise in ex_data["exercises"]:
    
    sheet_data = {
        "workout": {
            "Date": TODAY,
            "Time": TIME,
            "Exercise": exercise["name"].title(),
            "Duration": exercise["duration_min"],
            "Calories": exercise["nf_calories"]
        }
    } 

    sheet_header = {
        "Authorization": AUTH
    }

    print(sheet_data)
    sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_data, headers=sheet_header)
    print(sheet_response.raise_for_status)
    print(sheet_response.text)