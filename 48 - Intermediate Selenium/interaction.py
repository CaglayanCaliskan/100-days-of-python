from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# number = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")

# view_source_link = driver.find_element(by=By.LINK_TEXT, value="View source")

search = driver.find_element(by=By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
