from bs4 import BeautifulSoup
import requests


url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=url)
movie_list = []

soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.find_all(name="h3", class_='title')

for title in titles:
    movie_list.append(title.getText())

movie_list = movie_list[::-1]


with open('movies.txt', 'w', encoding="utf-8") as f:
    for movie in movie_list:
        f.write(f"{movie}\n")
