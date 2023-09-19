import requests
# url = "https://news.ycombinator.com/"
# response = requests.get(url)
# print(
#     f"your request to {url} came back with status code {response.status_code}")
# print(response.text)


#############################################################################
# url = "https://icanhazdadjoke.com/"
# #response = requests.get(url, headers={"Accept": "text/plain"})
# response = requests.get(url, headers={"Accept": "application/json"})
# #print(response.text)
# data = response.json() #python dictionary
# print(data['joke'])


#############################################################################

url = "https://icanhazdadjoke.com/search"
response = requests.get(url, headers={
                        "Accept": "application/json"}, params={"term": "cat", "limit": 1})
data = response.json()
print(data['results'][['joke']])
