import requests
from bs4 import BeautifulSoup
import csv

http = "https://books.toscrape.com//"
response = requests.get(http)
soup = BeautifulSoup(response.text, "html.parser")
