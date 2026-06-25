import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://demowebshop.tricentis.com/")

print(driver.title)

time.sleep(5)

driver.quit()