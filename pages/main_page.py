"""Модуль главной страницы."""
from typing import Any

import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page import MainPageLocators


class MainPage:
    """Класс главной страницы."""

    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 10)

    def deposits_button(self) -> WebElement:
        return self.app.wd.find_element(*MainPageLocators.DEPOSITS)

    @allure.step("Нажатие на кнопку Вклады")
    def click_on_deposits(self) -> Any:
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.DEPOSITS))
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
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.CARDS))
        return self.cards_button().click()

    def logout_button(self) -> WebElement:
        return self.app.wd.find_element(*MainPageLocators.LOGOUT_BUTTON)

    @allure.step("Нажимаем кнопку разлогина")
    def click_on_logout_button(self) -> Any:
        return self.logout_button().click()
