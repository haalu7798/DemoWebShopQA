import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#driver = webdriver.Chrome()
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
print(driver.title)
#driver.find_element(By.ID,"small-searchterms").send_keys("Laptop")
#driver.find_element(By.CSS_SELECTOR,"input[value='Search']").click()
#driver.find_element(By.NAME,"q").send_keys("Mobile")
#driver.find_element(By.CSS_SELECTOR,"input[value='Search']").click()
#driver.find_element(By.LINK_TEXT,"Register").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Log").click()
time.sleep(3)
driver.find_element(By.CLASS_NAME,"search-box-text").send_keys("Computer")
driver.find_element(By.CSS_SELECTOR,"input[value='Search']").click()
print(driver.title)
#input("Press Enter to close browser...")
driver.quit()


