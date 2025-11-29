import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    def __init__(self, driver):
        """
        Инициализация страницы продуктов.

        Args:
            driver (WebDriver): драйвер браузера
        """
        self.driver = driver

    @allure.step("Добавляем товар в корзину: {product_id}")
    def add_to_cart(self, product_id: str) -> None:
        """Добавляет товар в корзину по ID.

        Args:
            product_id (str): ID кнопки добавления
        """
        self.driver.find_element(By.ID, product_id).click()

    @allure.step("Переходим в корзину")
    def go_to_cart(self) -> None:
        """Переходит в корзину и ожидает загрузку страницы."""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_contains("cart"))
