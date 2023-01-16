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


target = "https://www.amazon.com.tr/MSI-11UD-428XTR-Bilgisayar-I7-11800H-RTX3050TI/dp/B09PRNDK7V?ref_=Oct_DLandingS_D_d69cdc1b_60"

driver.get(target)

price = driver.find_element(by=By.CLASS_NAME, value="a-price-whole")
print("price: ", price.text)

driver.quit()
