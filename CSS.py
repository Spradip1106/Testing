from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://login.salesforce.com/")
driver.find_element(By.CSS_SELECTOR,"input#username").send_keys("Pradip")
driver.find_element(By.PARTIAL_LINK_TEXT,'Forgot Your Password?').click()
driver.find_element(By.NAME,"cancel").click()