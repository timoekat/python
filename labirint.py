from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.labirint.ru/")

sleep(5)

search = "#search-field"

search_input = driver.find_element(By.CSS_SELECTOR, search)
search_input.send_keys("Python", Keys.RETURN)
book_locator = "div.product-card"

sleep(5)

books = driver.find_elements(By.CSS_SELECTOR, book_locator)

for book in books:
    
    title = book.find_element(By.CSS_SELECTOR, 'a.product-card__name').text
    price = book.find_element(By.CSS_SELECTOR, 'div.product-card__price-current').text
    author = ''

    try: 
        author = book.find_element(By.CSS_SELECTOR, 'div.product-card__author').text
        
    except: 
        author = "Автор не указан"

    print(author + "/t" + title + "/t" + price)
sleep(5)