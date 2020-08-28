"""Файл с классом приложения - APP"""
import logging
from typing import Any

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from common.utilities import FakeData
from common.loggin import setup
from pages.card_page import CardPage
from pages.deposits_page import DepositsPage
from pages.event_page import EventPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage
from pages.taxes_page import TaxesPage

logger = logging.getLogger()


class Application:
    """
    Класс  приложения - APP
    """

    @allure.step("Инициализация класса APP")
    def __init__(self, base_url, headless):
        setup("INFO")
        logger.setLevel("INFO")
        driver_path = ChromeDriverManager().install()
        options = Options()
        if headless:
            options.add_argument("--headless")
        self.wd = webdriver.Chrome(driver_path, options=options)
        self.base_url = base_url
        self.login_page = LoginPage(self)
        self.main_page = MainPage(self)
        self.deposit_page = DepositsPage(self)
        self.card_page = CardPage(self)
        self.fake_data = FakeData.lets_random_bitchas()
        self.taxes_page = TaxesPage(self)
        self.payment_page = PaymentPage(self)
        self.event_page = EventPage(self)


    @allure.step("Открытие страницы авторизации")
    def open_login_page(self) -> None:
        """Открытие страницы авторизации."""
        logger.info("Открытие страницы авторизации")
        self.wd.get(self.base_url)
        logger.info("Текущий URL - " + self.wd.current_url)

    @allure.step("Открытие главной страницы")
    def open_main_page(self) -> None:
        """Открытие главной страницы."""
        logger.info("Открытие главной страницы")
        self.wd.get((self.base_url + "/welcome"))
        logger.info("Текущий URL - " + self.wd.current_url)

    @allure.step("Закрытие браузера")
    def teardown(self) -> WebDriver:
        """Закрытие браузера."""
        logger.info("Закрытие браузера")
        return self.wd.quit()

    @allure.step("Создание депозита в долларах со свободным сроком")
    def open_free_term_usd_deposit(self, test_data: Any, check=False) -> None:
        """Создание депозита в долларах со свободным сроком"""
        logger.info("Создание депозита в долларах со свободным сроком")
        self.open_main_page()
        self.main_page.click_on_deposits()
        self.deposit_page.click_open_deposit()
        self.deposit_page.choose_usd()
        self.deposit_page.choose_free_term()
        self.deposit_page.choose_demo_2_deposit()
        self.deposit_page.input_to_amount_field(test_data)
        if check:
            self.deposit_page.text_of_percent_of_deposit()
        self.deposit_page.choose_end_date()
        self.deposit_page.click_next_button()

    @allure.step("Переход на страницу 'Добавление карты другого банка' ")
    def add_other_bank_card_page(self):
        self.open_main_page()
        self.main_page.click_on_cards_button()
        self.card_page.click_on_other_bank_card()
