

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
sum = 0
count = 0

tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)
    sum = int(tag.contents[0]) + sum
    count = count + 1
   # sum=int(tag.contents[0])+sum
print ('count', count)
print ('sum',sum)