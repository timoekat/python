import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        """
        Инициализация страницы корзины.

        Args:
            driver (WebDriver): драйвер браузера
        """
        self.driver = driver

    @allure.step("Нажимаем кнопку оформления заказа")
    def checkout(self) -> None:
        """Нажимает кнопку Checkout и ждет появления страницы."""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located
                   ((By.CSS_SELECTOR, "#checkout")))
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
