"""Модуль для хранения страницы Карты."""
from typing import Any

import allure
from selenium.webdriver.remote.webelement import WebElement

from common.Utilities import FakeData
from locators.card_page import CardPageLocators


class CardPage:
    def __init__(self, app):
        self.app = app

    def other_bank_card(self) -> WebElement:
        return self.app.wd.find_element(*CardPageLocators.other_bank_card)

    @allure.step('Нажатие на кнопку Добавить карту другого банка')
    def click_on_other_bank_card(self) -> Any:
        return self.other_bank_card().click()

    def other_bank_input_cardholder_field(self) -> WebElement:
        return self.app.wd.find_element(*CardPageLocators.other_bank_cardholder_input)

    @allure.step('Вводим имя владельца карты другого банка')
    def other_bank_input_cardholder_input_name(self, keys: str) -> Any:
        return self.other_bank_input_cardholder_field().send_keys(keys)

    def other_bank_card_number_field(self)-> WebElement:
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
    def add_other_bank_card(self,  card_data: FakeData) -> Any:
        self.other_bank_input_cardholder_field().clear()
        self.other_bank_input_cardholder_input_name(card_data.name)
        self.other_bank_card_number_field_input_number(card_data.credit_card)
        self.other_bank_card_expire_mouth_input(card_data.credit_card_expire_mouth)
        self.other_bank_card_expire_year_input(card_data.credit_card_expire_year)
        self.other_bank_card_csv_field_input(card_data.csv)
        self.other_bank_card_save_button_click()