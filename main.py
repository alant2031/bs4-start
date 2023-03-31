from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "lxml")
# print(soup.prettify())
# print(soup.title)
# print(soup.title.string)

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    # print(tag)
    # print(tag.getText())
    # print(tag.get("href"))
    ...

heading = soup.find(name="h1", id="name")
print(heading)

selector_1 = soup.select_one(selector="p a")
selector_2 = soup.select_one(selector="#name")
print(selector_1)
print(selector_2)

headings = soup.select(selector=".heading")
print(headings)
