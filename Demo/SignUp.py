import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com/register")
driver.maximize_window()
driver.find_element(By.ID,"gender-male").click()
driver.find_element(By.ID,"FirstName").send_keys("Jone")
driver.find_element(By.ID,"LastName").send_keys("Mack")
driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("hardik0@yopmail.com")
driver.find_element(By.NAME,"Password").send_keys("321654987")
driver.find_element(By.NAME,"ConfirmPassword").send_keys("321654987")
driver.find_element(By.XPATH,"//input[@id='register-button']").click()

actual_text = driver.find_element(By.CLASS_NAME, "result").text
assert "Your registration completed" in actual_text

print("Verification Pass!")





input("Press Enter to close browser...")