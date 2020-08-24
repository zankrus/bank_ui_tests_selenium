"""Модуль страницы Депозиты."""
import allure
from common.depost_page_constants import DepositPageConstants as Const

from locators.deposits_page_locators import DepositsPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DepositsPage:
    """Класс страницы Депозиты."""

    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 10)

    def open_deposit(self):
        return self.app.wd.find_element(*DepositsPageLocators.OPEN_DEPOSIT)

    @allure.step("Нажатие Открыть депозит")
    def click_open_deposit(self):
        return self.open_deposit().click()

    def usd_button(self):
        return self.app.wd.find_element(*DepositsPageLocators.USD)

    @allure.step("Выбрать валюту - USD")
    def choose_usd(self):
        return self.usd_button().click()

    def free_term_button(self):
        return self.app.wd.find_element(*DepositsPageLocators.FREE_TERM)

    @allure.step("Выбрать Свободный срок")
    def choose_free_term(self):
        return self.free_term_button().click()

    def demo_2_deposit(self):
        return self.app.wd.find_element(*DepositsPageLocators.DEMO_2_DEPOSIT_OPEN)

    @allure.step("Выбрать депозит ДЕМО2 ")
    def choose_demo_2_deposit(self):
        return self.demo_2_deposit().click()

    def end_date(self):
        return self.app.wd.find_element(*DepositsPageLocators.END_DATE)

    @allure.step("Выбрать Дату завершения 31 августа 2020 ")
    def choose_end_date(self):
        self.end_date().click()
        self.app.wd.find_element(*DepositsPageLocators.DATE_06_SEPTEMBER).click()
        return self.end_date()

    def amount_field(self):
        return self.app.wd.find_element(*DepositsPageLocators.AMOUNT)

    @allure.step("Ввод суммы депозита")
    def input_to_amount_field(self, keys):
        return self.amount_field().send_keys(keys)

    def next_button(self):
        return self.app.wd.find_element(*DepositsPageLocators.NEXT_BUTTON)

    @allure.step("Нажатие кнопки Далее")
    def click_next_button(self):
        return self.next_button().click()

    def agree_condition(self):
        return self.app.wd.find_element(*DepositsPageLocators.AGREE_CONDITION)

    @allure.step("Нажатие кнопки Согласен")
    def click_agree_condition(self):
        return self.agree_condition().click()

    def confirm_button(self):
        return self.app.wd.find_element(*DepositsPageLocators.CONFIRM_BUTTON)

    @allure.step("Нажатие кнопки Подтвердить")
    def click_confirm_button(self):
        return self.confirm_button().click()

    def success_logo(self):
        return self.app.wd.find_element(*DepositsPageLocators.SUCCESS_DEPOSIT)

    @allure.step("Проверка отрображения иконки успешного создания депозита")
    def is_displayed_success_logo(self):
        return self.success_logo().is_displayed()

    def percent_of_deposit(self):
        return self.app.wd.find_element(*DepositsPageLocators.PERCENT_OF_DEPOSIT)

    @allure.step("Проверка появления предупреждени о не валидной сумме")
    def invalid_amount(self):
        self.wait.until(
            EC.visibility_of_element_located(DepositsPageLocators.INVALID_AMOUNT_ALERT)
        )
        return self.app.wd.find_element(*DepositsPageLocators.INVALID_AMOUNT_ALERT)

    def invalid_amount_alert_is_visible(self):
        return self.invalid_amount().is_displayed()

    def alert_about_percents(self):
        return self.app.wd.find_element(*DepositsPageLocators.ALERT_TEXT)

    def text_of_alert_about_percents(self) -> str:
        self.wait.until(
            EC.text_to_be_present_in_element(
                DepositsPageLocators.ALERT_TEXT, Const.TEXT_OF_ALERT_PERCENTS
            )
        )
        return self.alert_about_percents().text

    @allure.step("Проверка суммый дохода от депозита")
    def text_of_percent_of_deposit(self):
        self.wait.until(
            EC.text_to_be_present_in_element(
                DepositsPageLocators.PERCENT_OF_DEPOSIT, Const.deposit_percents
            )
        )
        return self.percent_of_deposit().text
