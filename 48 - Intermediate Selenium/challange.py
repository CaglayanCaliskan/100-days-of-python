from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


path = "C:\Development\chromedriver_win32\chromedriver.exe"

service = Service(executable_path=path)

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=service, options=chrome_options)

target = "https://www.python.org/"


driver.get(target)

event_times = driver.find_elements(
    by=By.CSS_SELECTOR, value='.event-widget time')

event_names = driver.find_elements(
    by=By.CSS_SELECTOR, value='.event-widget li a')

events = {}


for n in range(len(event_times)):
    events[n] = {
        "time": "2023-" + event_times[n].text,
        "name": event_names[n].text
    }

print(events)
