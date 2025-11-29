import pytest
import allure
from pages.calculator_page import CalculatorPage


@pytest.mark.smoke
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка сложения чисел")
@allure.description("Проверяет сложение 2 чисел на калькуляторе с задержкой")
def test_calculator_addition(driver):
    calc = CalculatorPage(driver)

    with allure.step("Открываем калькулятор"):
        calc.open()
    with allure.step("Устанавливаем задержку 45 мс"):
        calc.set_delay(45)
    with allure.step("Вводим числа и операцию 7 + 8"):
        calc.click_button("7")
        calc.click_button("+")
        calc.click_button("8")
        calc.click_button("=")
    with allure.step("Ожидаем результат 15"):
        calc.wait_result_text("15")
    with allure.step("Проверяем значение на дисплее"):
        assert calc.get_display_value() == "15"
