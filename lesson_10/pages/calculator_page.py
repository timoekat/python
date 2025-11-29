import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver, wait_timeout: int = 45):
        """
        Инициализация страницы калькулятора.

        Args:
            driver (WebDriver): драйвер браузера
            wait_timeout (int): таймаут ожидания элементов
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_timeout)

    @allure.step("Открываем страницу калькулятора")
    def open(self) -> None:
        """Открывает страницу калькулятора."""
        self.driver.get(self.URL)

    @allure.step("Устанавливаем задержку: {value} мс")
    def set_delay(self, value: int) -> None:
        """Устанавливает задержку для калькулятора.

        Args:
            value (int): миллисекунды задержки
        """
        el = self.driver.find_element(*self.DELAY_INPUT)
        el.clear()
        el.send_keys(str(value))

    @allure.step("Нажимаем кнопку: {value}")
    def click_button(self, value: str) -> None:
        """Нажимает кнопку на калькуляторе.

        Args:
            value (str): текст кнопки
        """
        btn = self.driver.find_element(By.XPATH, f"//span[text()='{value}']")
        btn.click()

    @allure.step("Ожидаем результат: {text}")
    def wait_result_text(self, text: str) -> bool:
        """Ожидает появления текста на экране калькулятора.

        Args:
            text (str): ожидаемый текст

        Returns:
            bool: True если текст появился
        """
        return self.wait.until(EC.text_to_be_present_in_element
                               (self.SCREEN, str(text)))

    @allure.step("Получаем текст с дисплея калькулятора")
    def get_display_value(self) -> str:
        """Получает текст с экрана калькулятора.

        Returns:
            str: значение на экране
        """
        return self.driver.find_element(*self.SCREEN).text
