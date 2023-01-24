from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:\Development\chromedriver_win32\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):

        self.driver = webdriver.Chrome(
            executable_path=driver_path, options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        go_button = self.driver.find_element(
            by=By.CSS_SELECTOR, value='.start-text')
        go_button.click()
        print("time starts")
        time.sleep(60)
        print("60 seconds end")
        self.down = self.driver.find_element(
            by=By.CSS_SELECTOR, value='.download-speed').text
        self.up = self.driver.find_element(
            by=By.CSS_SELECTOR, value='.upload-speed').text

    def tweet_at_provider(self):
        print("down: ", self.down, "up: ", self.up)
        print("i passed this task")
        pass


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
