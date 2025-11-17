from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")
search_input = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
search_input.send_keys("SkyPro")


button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()
print(button.text)

driver.quit()