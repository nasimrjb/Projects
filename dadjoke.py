import requests
term = input("what would you like to search for? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url, headers={'Accept': "application/json"}, params={"term": term}).json()
num = len(res["results"])
if num == 0:
    print(f"there are no results for {term}")
if num == 1:
    print(f"there are 1 results for {term}")

print("number1: " + res["results"][0]['joke'])
print("number2: " + res["results"][1]['joke'])
print("number3: " + res["results"][2]['joke'])
print("number4: " + res["results"][3]['joke'])
