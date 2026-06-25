import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demowebshop.tricentis.com/login")
driver.maximize_window()

time.sleep(2)

driver.find_element(By.NAME, "Email").send_keys("hardik0@yopmail.com")
driver.find_element(By.ID, "Password").send_keys("123456")
driver.find_element(By.NAME, "RememberMe").click()
driver.find_element(By.CSS_SELECTOR, "input[value='Log in']").click()

actual_text = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text

print(actual_text)

assert "Login was unsuccessful" in actual_text

print("Test Passed")


#TC_02 blank id and blank password

driver.find_element(By.NAME, "Email").clear()
driver.find_element(By.CSS_SELECTOR, "input[value='Log in']").click()
actual_text = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text
print(actual_text)
assert "Login was unsuccessful" in actual_text
print("Test Passed")




input("Press Enter to close browser...")