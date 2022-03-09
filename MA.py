from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
action = ActionChains(driver)
menu = driver.find_element(By.ID, "mousehover")
action.move_to_element(menu).perform()
option1 = driver.find_element(By.LINK_TEXT,"Top")
action.move_to_element(option1).click().perform()