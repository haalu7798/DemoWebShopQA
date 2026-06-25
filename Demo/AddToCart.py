import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demowebshop.tricentis.com/login")
driver.maximize_window()

time.sleep(2)

driver.find_element(By.NAME, "Email").send_keys("hardik0@yopmail.com")
driver.find_element(By.ID, "Password").send_keys("321654987")
driver.find_element(By.NAME, "RememberMe").click()
driver.find_element(By.CSS_SELECTOR, "input[value='Log in']").click()
driver.find_element(By.CSS_SELECTOR,"#small-searchterms").send_keys("Laptop")
driver.find_element(By.CSS_SELECTOR,"input[class='button-1 search-box-button']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@value='Add to cart']").click()
driver.find_element(By.CSS_SELECTOR,"li[id='topcartlink'] a[class='ico-cart']").click()




input("Press Enter to close browser...")