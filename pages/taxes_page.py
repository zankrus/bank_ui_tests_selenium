"""Файл страницы Проверки налоговых задолженностей"""
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.tax_page_constants import TaxPageConstants as Const
from locators.tax_page_locators import TaxPageLocators


class TaxesPage:
    """
    Класс налоговых задолженностей
    """

    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 10)

    def check_taxes_button(self):
        return self.app.wd.find_element(*TaxPageLocators.CHECK_TAXES_BUTTON)

    @allure.step("Кликаем на кнопку Проверить налоги")
    def click_on_check_taxes_button(self):
        self.wait.until(EC.presence_of_element_located(TaxPageLocators.CHECK_TAXES_BUTTON))
        return self.check_taxes_button().click()

    def taxes_check_result_message(self):
        self.wait.until(EC.text_to_be_present_in_element(TaxPageLocators.TAXES_CHECK_RESULT,
                                                         Const.TAXES_CHECK_RESULT_TEXT))
        return self.app.wd.find_element(*TaxPageLocators.TAXES_CHECK_RESULT)

    @allure.step("Проверка - Появились ли результаты из Гос.Инф.Системы")
    def taxes_check_result_text_is_displayed(self):
        return self.taxes_check_result_message().is_displayed()

    def pay_tax_button(self):
        self.wait.until(EC.presence_of_element_located(TaxPageLocators.PAY_TAX_BUTTON))
        return self.app.wd.find_element(*TaxPageLocators.PAY_TAX_BUTTON)

    @allure.step("Нажимаем оплатить")
    def click_pay_tax_button(self):
        return self.pay_tax_button().click()

