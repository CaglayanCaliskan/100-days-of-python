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
input = driver.find_element(by=By.ID, value="twotabsearchtextbox")
nav_item = driver.find_element(
    by=By.XPATH, value='//*[@id="nav-xshop"]/a[5]')
price2 = driver.find_element(
    by=By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[1]')

print(nav_item.text)

input.click()

print("price: ", price.text)
print("price2: ", price2.text)

driver.quit()
