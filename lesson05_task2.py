from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com")

sleep(5)

driver.get("http://uitestingplayground.com/classattr")

sleep(5)


button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")

button.click()

sleep(5)