from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()


driver.get("https://www.mozilla.org")

sleep(5)

driver.get("http://the-internet.herokuapp.com/inputs")

sleep(5)

search_input = driver.find_element(By.CSS_SELECTOR, "input[type='number']")

sleep(5)
search_input.send_keys("Sky", Keys.RETURN)


sleep(5)

search_input.clear()

sleep(5)
search_input.send_keys("Pro", Keys.RETURN)
sleep(5)


driver.quit() 

