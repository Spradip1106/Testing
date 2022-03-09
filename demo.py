from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.find_element(By.ID,"email").send_keys("pradipsaudar@gmail.com")
driver.find_element(By.NAME,"login").click()
driver.i