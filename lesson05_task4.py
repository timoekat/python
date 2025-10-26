from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()


driver.get("https://www.mozilla.org")

sleep(5)


driver.get("http://the-internet.herokuapp.com/login")

sleep(5)

search_input = driver.find_element(By.ID, "username")
search_input.send_keys("tomsmith")
search_input = driver.find_element(By.ID, "password")
search_input.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()

flash_message = driver.find_element(By.ID, "flash")
print(flash_message.text)

sleep(3)
driver.quit()




