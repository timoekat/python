from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultPage:

    def __init__(self, driver):
        self.driver = driver

    def fill_form(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "#first-name")))

        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys("Екатерина")
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys("Тимофеева")
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys("96100")

        self.driver.find_element(
            By.CSS_SELECTOR, "#continue").click()

    def final_price(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, ".summary_total_label")))

        text = self.driver.find_element(
            By.CSS_SELECTOR, ".summary_total_label").text
        text = text.replace("Total: $", "")
        return float(text)
