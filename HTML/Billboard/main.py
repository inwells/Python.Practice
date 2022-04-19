import requests
from bs4 import BeautifulSoup
import datetime as dt
import json
import spotipy

with open("api.key") as key_file:
        keydata = json.load(key_file)
ID = keydata["id"]
SECRET = keydata["secret"]

URL_BASE = "https://www.billboard.com/charts/hot-100/"

#date_input = input("Which year, month, and day do you want to travel to?")
date_input = "1989-02-14"
URL = f"{URL_BASE}{date_input}"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

hot100 = soup.find_all("div", class_="o-chart-results-list-row-container")

song_titles = []
song_artists = []
for hot in hot100:
    song_title = hot.find("h3").getText().strip()
    song_titles.append(song_title)
    song_artist = hot.find("span", class_="a-no-trucate").getText().strip()
    song_artists.append(song_artist)