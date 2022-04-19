import requests
from bs4 import BeautifulSoup
import datetime as dt
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


URL_BASE = "https://www.billboard.com/charts/hot-100/"

#date_input = input("Which year, month, and day do you want to travel to?")
date_input = "1989-02-14"
URL = f"{URL_BASE}{date_input}"
USER = sp.current_user()

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

hot100 = soup.find_all("div", class_="o-chart-results-list-row-container")

song_uris = []

def playlist_uri(playlist):
    sp.playlist

for hot in hot100:
    song_title = hot.find("h3").getText().strip()
    #song_titles.append(song_title)
    song_artist = hot.find("span", class_="a-no-trucate").getText().strip()
    #song_artists.append(song_artist)
    song = sp.search(q=f"track:{song_title} artist:{song_artist}", type="track")
    try:
        uri = song["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"The song {song_title} by {song_artist} does not exist in Spotify. Skipped.")

playlists = sp.user_playlists('spotify')
playlist_name = f"{date_input} Billboard 100"

if date_input in playlists:
   pass
else: 
    playlist = sp.user_playlist_create(user=USER["id"], name=playlist_name, public=False)
    sp.user_playlist_add_tracks(user=USER["id"], playlist_id=playlist["id"], tracks=song_uris)
