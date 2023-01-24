from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


path = "C:\Development\chromedriver_win32\chromedriver.exe"

service = Service(executable_path=path)

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=service, options=chrome_options)

target = "https://www.speedtest.net/"
target2 = "https://twitter.com/home"

driver.get(target)

time.sleep(1)
go_button = driver.find_element(
    by=By.CSS_SELECTOR, value='.start-text')
go_button.click()
print("time starts")
time.sleep(60)
print("60 seconds end")

dl_speed = go_button = driver.find_element(
    by=By.CSS_SELECTOR, value='.download-speed')
ul_speed = go_button = driver.find_element(
    by=By.CSS_SELECTOR, value='.upload-speed')

driver.quit()
time.sleep(1)
driver.get(target2)


twitter_input = go_button = driver.find_element(
    by=By.CSS_SELECTOR, value='.public-DraftStyleDefault-block public-DraftStyleDefault-ltr')

twitter_input.send_keys(f'download: {dl_speed} upload: {ul_speed}')


# go_button.click()
