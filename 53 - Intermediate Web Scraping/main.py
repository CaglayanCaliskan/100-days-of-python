from bs4 import BeautifulSoup
import requests


form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeqncZzTv5ISae5vMkw1rHn3UjeHljgIEHUCYk9ph1NKVq_TQ/viewform?usp=sf_link"
zillow_link = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.65477217626953%2C%22east%22%3A-122.21188582373047%2C%22south%22%3A37.564137318185516%2C%22north%22%3A37.985844231051246%7D%2C%22mapZoom%22%3A11%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

response = requests.get(url=zillow_link)


soup = BeautifulSoup(response.text, 'html.parser')
all_link_elements = soup.select(".list-card_building")

print(soup.prettify())
# titles = soup.find_all(
#     name="li", class_='List-c11n-8-81-1__sc-1smrmqp-0')
