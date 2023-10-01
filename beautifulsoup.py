from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
# print(soup.body.div)
# g = soup.find("div")
# m = soup.find(id="first")
# mm = soup.select("#first")[0]
# h = soup.find_all("div")
# j = soup.find_all(attrs={"data-example": "yes"})
# jj = soup.select("[data-example]")
# n = soup.find_all(class_="special")
# nn = soup.select(".special")
# d = soup.select("[data-example]")
# for el in soup.select(".special"):
#     print(el.get_text())
#     print(el.name)
#     print(el.attrs)
# attr = soup.find("h3")["data-example"]
# attr2 = soup.find("div")["id"]
# print(attr2)

############################################################################
# data = soup.body.contents[1].contents[1]
# data = soup.body.contents[1].next_sibling.next_sibling
# data = soup.find(class_="special").parent
data = soup.find(class_="special").find_next_sibling(class_="special")
# data = soup.find(id="first").find_next_sibling()
# data = soup.select("[data-example]")[1].find_previous_sibling()
print(data)
