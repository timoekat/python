import allure
from selenium.webdriver.common.by import By


class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        """
        Инициализация страницы логина.

        Args:
            driver (WebDriver): драйвер браузера
        """
        self.driver = driver

    @allure.step("Открываем страницу логина")
    def open(self) -> None:
        """Открывает страницу логина."""
        self.driver.get(self.URL)

    @allure.step("Логинимся пользователем {username}")
    def login(self, username: str, password: str) -> None:
        """Выполняет авторизацию пользователя.

        Args:
            username (str): имя пользователя
            password (str): пароль
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
