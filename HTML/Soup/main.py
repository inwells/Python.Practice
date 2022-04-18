from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title.string)

articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
article_upvotes =[]
for article in articles:
    article_text = article.getText()
    article_link = article.get("href")
    article_links.append(article_link)
    article_texts.append(article_text)

article_upvotes = [upvote.getText().split()[0] for upvote in soup.find_all(class_="score")]

largest_num = max(article_upvotes)
largest_index = article_upvotes.index(largest_num)

print(article_texts[largest_index])
print(article_links[largest_index])
print(article_upvotes[largest_index])



# with open("website.html") as file:
#     contents = file.read()

# #print(soup.title.string)

# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     #print(tag.get.Text())
#     print(tag.get("href")) #strip just the links

# company_url = soup.select_one(selector="p a")
# print (company_url)

# h3_heading = soup.find_all("h3", class_="heading")
# print(h3_heading)

# headings = soup.select(".heading")
# print(headings)

# form_tag = soup.find("input")
# max_length = form_tag.get("maxlength")
# print(max_length)