import json, urllib.request

address = input("input url link:")
print('Retrieving', address)
with urllib.request.urlopen(address) as url:
    data = json.loads(url.read().decode())

print('User count:', len(data))

print('Retrieved', len(str(data)), 'characters')
data = data.get("comments")
#print(data)
num = total = 0
for i in range(len(data)):
    tmp = data[i]
    value = tmp.get("count")
    num = num + 1
    total = total + int(value)
print("Count:",num)
print("Sum:",total)