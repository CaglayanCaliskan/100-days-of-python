import requests
from bs4 import BeautifulSoup
import re
import os

URL = "https://www.billboard.com/charts/hot-100"

os.system('cls')
quest = input(
    'Which year do you want to travel to? Type in this format YYYY-MM-DD: ')

response = requests.get(url=f"{URL}/{quest}")

soup = BeautifulSoup(response.text, 'html.parser')

songs = soup.find_all(name='li', class_='o-chart-results-list__item')

list_of_songs = [song.getText().strip().replace(
    '\n', "").replace("\t", "") for song in songs if len(song.getText().strip().replace(
        '\n', "").replace("\t", "")) > 3]


for string in list_of_songs:
    match = re.search(r'(?i)(?<=[a-z])[A-Z][a-z]*', string)
    if match:
        sing = string[:match.start()]
        singer = string[match.start():]
        new_object = {'sing': sing, 'singer': singer}
        print(new_object)


# string = "ForevesWhitney"
# words = re.findall(r'[A-Z][a-z]*', string)
# print(words)
