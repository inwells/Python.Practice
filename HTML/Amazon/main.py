import requests
import lxml
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/Tamashi-Nations-Iron-Blooded-Orphans-Barbatos/dp/B091DSGPG9"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,es;q=0.8"
}

response = requests.get(URL,headers=header)

soup = BeautifulSoup(response.content, "lxml")

#print(soup.prettify())

whole = soup.find("span", class_="a-price-whole")
fraction = soup.find("span", class_="a-price-fraction")
price = float(f"{whole.getText()}{fraction.getText()}")
print(price)

#Add Email function for lowest price