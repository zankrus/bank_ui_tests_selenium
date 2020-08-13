from typing import Any

import allure
from selenium.webdriver.remote.webelement import WebElement

from locators.main_page import MainPageLocators


class MainPage:
    def __init__(self, app):
        self.app = app

    def deposits_button(self) -> WebElement:
        return self.app.wd.find_element(*MainPageLocators.deposits)

    @allure.step("Нажатие на кнопку Вклады")
    def click_on_deposits(self) -> Any:
        return self.deposits_button().click()

    def change_lang_button(self) -> WebElement:
        return self.app.wd.find_element(*MainPageLocators.change_lang)

    @allure.step("Смена языка")
    def change_lang(self) -> Any:
        return self.change_lang().click()

    def cards_button(self) -> WebElement:
        return self.app.wd.find_element(*MainPageLocators.cards)

    @allure.step("Нажать на кнопку Карты")
    def click_on_cards_button(self) -> Any:
        return self.cards_button().click()