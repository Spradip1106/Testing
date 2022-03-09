from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
child = driver.window_handles[1]
driver.switch_to.window(child)
print(driver.find_element(By.TAG_NAME,'h3').text)
driver.close()
driver.switch_to.window(driver.window_handles[0])
assert driver.find_element(By.TAG_NAME,'h3').text == "Opening a new window"
