from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.example.com = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.ID, "myElement")))
element.click()
