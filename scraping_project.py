import requests
from bs4 import BeautifulSoup
import csv
from random import choice

lnk_short = "https://quotes.toscrape.com/"
lnk = "page/1"
lst = []

while lnk:
    http = f"{lnk_short}{lnk}"
    response = requests.get(http)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all(class_="quote")

    for quote in quotes:
        lst.append({"text": quote.find(class_="text").get_text(),
                    "author": quote.find(itemprop="author").get_text(),
                    "link": quote.find("a")["href"]})

    if soup.find(class_="next"):
        lnk = soup.find(class_="next").find("a")["href"]
    else:
        None
# random_quote = choice(lst)
# print(random_quote)
print(lst['text'])
