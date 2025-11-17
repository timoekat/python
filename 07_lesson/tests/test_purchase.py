import pytest
from selenium import webdriver
from pages.loginpage import LoginPage
from pages.productpage import ProductsPage
from pages.cartpage import CartPage
from pages.resultpage import ResultPage


def create_driver():
    driver = webdriver.Firefox()
    return driver


@pytest.mark.smoke
def test_complete_purchase():
    driver = create_driver()

    try:

        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        products_page = ProductsPage(driver)
        products_page.add_to_cart("add-to-cart-sauce-labs-backpack")
        products_page.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
        products_page.add_to_cart("add-to-cart-sauce-labs-onesie")

        products_page.go_to_cart()

        cart_page = CartPage(driver)
        cart_page.checkout()

        result_page = ResultPage(driver)
        result_page.fill_form()

        assert result_page.final_price() == 58.29

    finally:
        driver.quit()
