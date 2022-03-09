import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
dd = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dd.select_by_index(1)
time.sleep(2)
dd.select_by_visible_text('Male')