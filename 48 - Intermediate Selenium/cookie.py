from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

url = "http://orteil.dashnet.org/experiments/cookie/"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=chrome_options)

driver.get(url=url)

cookie = driver.find_element(by=By.ID, value="cookie")

for n in range(100):
    cookie.click()
