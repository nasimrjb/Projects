import requests
term = input("what would you like to search for? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(url)
print(res.text)
