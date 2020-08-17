from typing import Any

import allure
from selenium.webdriver.remote.webelement import WebElement

from locators.main_page import MainPageLocators


class MainPage:
    def __init__(self, app):
        self.app = app

    def deposits_button(self) -> WebElement:
        return self.app.wd.find_element(*MainPageLocators.DEPOSITS)

    @allure.step("Нажатие на кнопку Вклады")
    def click_on_deposits(self) -> Any:
        self.app.wait.until(self.app.ex.element_to_be_clickable(MainPageLocators.DEPOSITS))
        return self.deposits_button().click()

    def change_lang_button(self) -> WebElement:
        return self.app.wd.find_element(*MainPageLocators.CHANGE_LANG)

    @allure.step("Смена языка")
    def change_lang(self) -> Any:
        return self.change_lang().click()

    def cards_button(self) -> WebElement:
        return self.app.wd.find_element(*MainPageLocators.CARDS)

    @allure.step("Нажать на кнопку Карты")
    def click_on_cards_button(self) -> Any:
        self.app.wait.until(self.app.ex.element_to_be_clickable(MainPageLocators.CARDS))
        return self.cards_button().click()

    def logout_button(self) -> WebElement:
        return self.app.wd.find_element(*MainPageLocators.LOGOUT_BUTTON)

    @allure.step("Нажимаем кнопку разлогина")
    def click_on_logout_button(self) -> Any:
        return self.logout_button().click()
