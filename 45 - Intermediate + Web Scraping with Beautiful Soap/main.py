from bs4 import BeautifulSoup


with open('./website.html', encoding="utf8") as file:
    contents = file.read()


soup = BeautifulSoup(contents, 'html.parser')
all_anchor_tags = soup.find_all(name="a")


# heading = soup.find(name="h1", id='name')
heading = soup.find(class_='heading')
select_one = soup.select_one(selector="p strong a")
select_class = soup.select('.test')
print(select_class)


for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    pass
