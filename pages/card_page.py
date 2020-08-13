"""Модуль для хранения страницы Карты."""
import time
from typing import Any

import allure
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common.Utilities import FakeData
from locators.card_page import CardPageLocators


class CardPage:
    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 10)

    def other_bank_card(self) -> WebElement:
        return self.app.wd.find_element(*CardPageLocators.other_bank_card)

    @allure.step('Нажатие на кнопку Добавить карту другого банка')
    def click_on_other_bank_card(self) -> Any:
        return self.other_bank_card().click()

    def other_bank_input_cardholder_field(self) -> WebElement:
        return self.app.wd.find_element(*CardPageLocators.other_bank_cardholder_input)

    @allure.step('Вводим имя владельца карты другого банка')
    def other_bank_input_cardholder_input_name(self, keys: str) -> Any:
        self.wait.until(EC.element_to_be_clickable(CardPageLocators.other_bank_cardholder_input))
        return self.other_bank_input_cardholder_field().send_keys(keys)

    def other_bank_card_number_field(self) -> WebElement:
        return self.app.wd.find_element(*CardPageLocators.other_bank_card_number)

    @allure.step('Вводим номер карты другого банка')
    def other_bank_card_number_field_input_number(self, keys: str) -> Any:
        return self.other_bank_card_number_field().send_keys(keys)

    def other_bank_card_expire_mouth_field(self) -> WebElement:
        return self.app.wd.find_element(*CardPageLocators.other_bank_card_expire_mouth)

    @allure.step('Вводим месяц  карты другого банка')
    def other_bank_card_expire_mouth_input(self, keys: str) -> Any:
        return self.other_bank_card_expire_mouth_field().send_keys(keys)

    def other_bank_card_expire_year_field(self) -> WebElement:
        return self.app.wd.find_element(*CardPageLocators.other_bank_card_expire_year)

    @allure.step('Вводим год  карты другого банка')
    def other_bank_card_expire_year_input(self, keys: str) -> Any:
        return self.other_bank_card_expire_year_field().send_keys(keys)

    def other_bank_card_csv_field(self) -> WebElement:
        return self.app.wd.find_element(*CardPageLocators.other_bank_card_csv)

    @allure.step('Вводим код CSV  карты другого банка')
    def other_bank_card_csv_field_input(self, keys: str) -> Any:
        return self.other_bank_card_csv_field().send_keys(keys)

    def other_bank_card_save_button(self) -> WebElement:
        return self.app.wd.find_element(*CardPageLocators.other_bank_card_save_button)

    @allure.step('Нажимаем Сохранить')
    def other_bank_card_save_button_click(self) -> Any:
        return self.other_bank_card_save_button().click()

    @allure.step('Заполняем данные карты другого банка')
    def add_other_bank_card(self, card_data: FakeData) -> Any:
        self.other_bank_input_cardholder_field().clear()
        self.other_bank_input_cardholder_input_name(card_data.name)
        self.other_bank_card_number_field_input_number(card_data.credit_card)
        self.other_bank_card_expire_mouth_input(card_data.credit_card_expire_mouth)
        self.other_bank_card_expire_year_input(card_data.credit_card_expire_year)
        self.other_bank_card_csv_field_input(card_data.csv)
        self.other_bank_card_save_button_click()

    def card_holder_preview(self) -> WebElement:
        self.wait.until(EC.visibility_of_element_located(CardPageLocators.card_holder_preview))
        return self.app.wd.find_element(*CardPageLocators.card_holder_preview)

    @allure.step("Проверка владельца карты на превью")
    def card_holder_preview_text(self) -> str:
        return self.card_holder_preview().text

    def card_expiring_preview(self) -> WebElement:
        return self.app.wd.find_element(*CardPageLocators.card_validity)

    @allure.step("Проверка даты окончания карты на превью")
    def card_expiring_preview_text(self) -> str:
        return self.card_expiring_preview().text

    def confirm_button(self) -> WebElement:
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(CardPageLocators.iframe))
        try:
            return self.app.wd.find_element(*CardPageLocators.confirm_button)
        except NoSuchWindowException:
            time.sleep(4)
            return self.app.wd.find_element(*CardPageLocators.confirm_button)

    # @allure.step("Нажатие кнопки подтвердить")
    # def confirm_button_click(self) -> Any:
    #     try:
    #         self.confirm_button().click()
    #         return self.app.wd.switch_to.default_content()
    #     except NoSuchWindowException:
    #         time.sleep(4)
    #         self.confirm_button().click()
    #         return self.app.wd.switch_to.default_content()


    @allure.step("Нажатие кнопки подтвердить")
    def confirm_button_click(self) -> Any:
        self.confirm_button().click()
        return self.app.wd.switch_to.default_content()


    def success_alert(self) -> WebElement:
        return self.app.wd.find_element(*CardPageLocators.success_alert)

    @allure.step("Проверка отображения сообщения о успехе")
    def success_alert_is_displayed(self):
        return self.success_alert().is_displayed()
