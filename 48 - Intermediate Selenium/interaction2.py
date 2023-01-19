from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

url = "https://www.appbrewery.co/p/newsletter"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=chrome_options)

driver.get(url=url)

search = driver.find_element(by=By.ID, value="member_email")
search.send_keys("Python@bla.com")
search.send_keys(Keys.ENTER)
