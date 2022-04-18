import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

movie_titles = [movie.getText() for movie in soup.find_all(name="h3", class_= "title")]
movies = movie_titles[::-1]
#or
# for n in range(len(movie_titles) - 1, -1, -1):
#   print(movie_titles[n])

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")