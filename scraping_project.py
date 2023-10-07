import requests
from bs4 import BeautifulSoup
import csv

http = "https://quotes.toscrape.com/"
response = requests.get(http)
soup = BeautifulSoup(response.text, "html.parser")

lst = []

quotes = soup.find_all(class_="quote")
for quote in quotes:
    lst.append({"text": quote.find(class_="text").get_text(),
               "author": quote.find(itemprop="author").get_text(),
                "link": quote.find("a").attrs})

print(lst)
