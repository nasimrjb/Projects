import requests
from bs4 import BeautifulSoup
import csv

http = "https://www.rithmschool.com/blog/"
response = requests.get(http)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")
print(articles)
