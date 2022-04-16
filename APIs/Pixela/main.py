import requests
import datetime as dt
import json 
#https://pixe.la/@cybertime


with open("api.key") as key_file:
        keydata = json.load(key_file)
TOKEN = keydata["apikey"]
USERNAME = keydata["username"]
ID = keydata["id"]

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": ID,
    "name": "Drawing Graph",
    "unit": "mins",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#create graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

tracker_endpoint = f"{graph_endpoint}/{ID}"
now = dt.datetime.now()

quantity = "30"

pixela_data = {
    "date": now.strftime("%Y%m%d"),
    "quantity": quantity,
}
print(pixela_data)
response = requests.post(url=tracker_endpoint, json=pixela_data, headers=headers)
print(response.text)