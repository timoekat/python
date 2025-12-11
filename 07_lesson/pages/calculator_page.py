from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver, wait_timeout=45):

        self.driver = driver
        self.wait = WebDriverWait(driver, wait_timeout)

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, value):
        el = self.driver.find_element(*self.DELAY_INPUT)
        el.clear()
        el.send_keys(str(value))

    def click_button(self, value):
        btn = self.driver.find_element(By.XPATH, f"//span[text()='{value}']")
        btn.click()

    def wait_result_text(self, text):

        return self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, str(text)))

    def get_display_value(self):

        return self.driver.find_element(*self.SCREEN).text
