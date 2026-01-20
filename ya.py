from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window
# driver.get("https://www.google.com")
driver.get("https://ya.ru")
# driver.get("https://vk.com")
# driver.back()
# driver.forward()
# driver.refresh()

sleep(5)
driver.fullscreen_window()
sleep(5)
driver.save_screenshot('.ya.png')

# driver.set_window_size(640, 480)

# sleep (50)
