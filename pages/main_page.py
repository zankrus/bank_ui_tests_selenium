"""Модуль главной страницы."""
import time
from typing import Any

import allure
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


from locators.main_page_locators import MainPageLocators

class MainPage:
    """Класс главной страницы."""

    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 4)

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

    def question_button(self):
        self.wait.until(EC.text_to_be_present_in_element(MainPageLocators.QUESTION_BUTTON, '?'))
        return self.app.wd.find_element(*MainPageLocators.QUESTION_BUTTON)

    @allure.step("Нажимаем кнопку - ВОПРОС")
    def click_question_button(self) -> Any:
        try:
            return self.question_button().click()
        except TimeoutException:
            return self.question_button().click()

    def welcome_tour(self) -> WebElement:
        return self.app.wd.find_element(*MainPageLocators.WELCOME_TOUR)

    @allure.step("Нажимаем кнопку - Визуальный помощник")
    def click_welcome_tour(self) -> Any:
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.WELCOME_TOUR))
        return self.welcome_tour().click()

    def welcome_tour_next_button(self):
        return self.app.wd.find_element(*MainPageLocators.WELCOME_TOUR_NEXT_BUTTON)

    @allure.step("Нажимаем кнопку - Далее")
    def click_welcome_tour_next_button(self):
        try:
            self.wait.until(EC.presence_of_element_located(MainPageLocators.WELCOME_TOUR_NEXT_BUTTON))
            return self.welcome_tour_next_button().click()
        except StaleElementReferenceException:
            return self.welcome_tour_next_button().click()

    def bank_overview(self):
        self.wait.until(EC.presence_of_element_located(MainPageLocators.BANK_OVERVIEW))
        return self.app.wd.find_element(*MainPageLocators.BANK_OVERVIEW)

    @allure.step("Проверка отображения блока - ОБЗОР")
    def is_displayed_bank_overview(self):
        return self.bank_overview().is_displayed()

    def end_welcome_tour_button(self):
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.WELCOME_TOUR_END))
        return self.app.wd.find_element(*MainPageLocators.WELCOME_TOUR_END)

    @allure.step("Нажатие на кнопк - Завершить")
    def click_end_welcome_tour_button(self):
        return self.end_welcome_tour_button().click()

    def welcome_tour_title(self):
        self.wait.until(EC.presence_of_element_located(MainPageLocators.WELCOME_TOUR_TITLE))
        return self.app.wd.find_element(*MainPageLocators.WELCOME_TOUR_TITLE)

    @allure.step("Проверка текста заголовка Welcome Tour")
    def text_welcome_tour_title(self, text):
        self.wait.until(EC.text_to_be_present_in_element(MainPageLocators.WELCOME_TOUR_TITLE, text))
        return self.welcome_tour_title().text

    def account_number(self, number):
        try:
            return self.app.wd.find_element(*MainPageLocators.account_number(number))
        except NoSuchElementException:
            self.wait.until(EC.text_to_be_present_in_element(MainPageLocators.account_number(number),
                                                             str(number)))
            return self.app.wd.find_element(*MainPageLocators.account_number(number))

    @allure.step("Кликаем на номер выбранный номер счета")
    def click_on_account_number(self, number):
        time.sleep(4)
        return self.account_number(number).click()
