import pytest
import allure
from pages.loginpage import LoginPage
from pages.productpage import ProductsPage
from pages.cartpage import CartPage
from pages.resultpage import ResultPage
from selenium import webdriver


def create_driver():
    driver = webdriver.Firefox()
    return driver


@pytest.mark.smoke
@allure.feature("Покупка товаров")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Полная покупка на сайте")
@allure.description("Проверка: логин, добавление товаров, оформление заказа")
def test_complete_purchase():
    driver = create_driver()

    try:
        login_page = LoginPage(driver)
        with allure.step("Открываем страницу логина и авторизуемся"):
            login_page.open()
            login_page.login("standard_user", "secret_sauce")

        products_page = ProductsPage(driver)
        with allure.step("Добавляем товары в корзину"):
            products_page.add_to_cart("add-to-cart-sauce-labs-backpack")
            products_page.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
            products_page.add_to_cart("add-to-cart-sauce-labs-onesie")
            products_page.go_to_cart()

        cart_page = CartPage(driver)
        with allure.step("Переходим к оформлению заказа"):
            cart_page.checkout()

        result_page = ResultPage(driver)
        with allure.step("Заполняем форму заказа"):
            result_page.fill_form()

        with allure.step("Проверяем итоговую цену"):
            assert result_page.final_price() == 58.29

    finally:
        driver.quit()
