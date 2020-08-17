import logging

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from common.Utilities import FakeData
from common.loggin import setup
from pages.card_page import CardPage
from pages.deposits_page import DepositsPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

logger = logging.getLogger()


class Application:
    """
    Класс всего приложения - APP
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
        self.fake_data = FakeData(self).lets_random_bitchas()

    @allure.step("Открытие страницы авторизации")
    def open_login_page(self) -> WebDriver:
        logger.info("Открытие страницы авторизации")
        return self.wd.get(self.base_url)

    @allure.step("Открытие главной страницы")
    def open_main_page(self) -> WebDriver:
        logger.info("Открытие главной страницы")
        return self.wd.get((self.base_url + "/welcome"))

    @allure.step("Закрытие браузера")
    def teardown(self) -> WebDriver:
        logger.info("Закрытие браузера")
        return self.wd.quit()

    @allure.step("Создание депозита в долларах со свободным сроком")
    def open_free_term_usd_deposit(self, test_data, check):
        logger.info('Создание депозита в долларах со свободным сроком')
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


