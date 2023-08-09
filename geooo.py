import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input ('Enter url: ')
print('Retrieving', url)
sum = 0
cnt = 0
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
lst = tree.findall ('comments/comment')
for item in lst:
    cnt = cnt + 1
    t = item.find ('count').text
    sum = sum + float (t)  
print ('Count:', cnt)
print ('Sum:' , sum)