import requests
from bs4 import BeautifulSoup
import csv
from random import choice
lnk = "page/1"

while lnk:
    lnk_short = "https://quotes.toscrape.com/"
    http = f"{lnk_short}{lnk}"
    response = requests.get(http)
    soup = BeautifulSoup(response.text, "html.parser")

    lst = []
    quotes = soup.find_all(class_="quote")
    for quote in quotes:
        lst.append({"text": quote.find(class_="text").get_text(),
                    "author": quote.find(itemprop="author").get_text(),
                    "link": quote.find("a")["href"]})

    if soup.find(class_="next"):
        lnk = soup.find(class_="next").find("a")["href"]
    else:
        None


print(lst)
