from bs4 import BeautifulSoup
import requests
url = "https://news.ycombinator.com/"

response = requests.get(url=url)

all_titles = []
all_hrefs = []
all_scores = []


soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all(name="span", class_='titleline')
scores = soup.find_all(class_='score')

for title in titles:
    all_titles.append(title.getText())
    all_hrefs.append(title.find(name='a').get("href"))

for score in scores:
    all_scores.append(int(score.getText().split(" ")[0]))

max_index = all_scores.index(max(all_scores))

print(all_titles[max_index])
print(all_hrefs[max_index])
print(all_scores[max_index])
