from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
waiter = WebDriverWait(driver, 40, 0.1)
picture3 = waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#award")))

print(picture3.get_attribute("src"))

driver.quit()
