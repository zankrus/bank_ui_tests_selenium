from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from common.loggin import setup
from pages.login_page import LoginPage

import logging

from pages.main_page import MainPage

logger = logging.getLogger()


class Application:
    def __init__(self, base_url, headless):
        setup('INFO')
        logger.setLevel('INFO')
        driver_path = ChromeDriverManager().install()
        options = Options()
        options.headless = headless
        self.wd = webdriver.Chrome(driver_path, options=options)
        self.base_url = base_url
        self.login_page = LoginPage(self)
        self.main_page = MainPage(self)

    def open_login_page(self):
        logger.info('Open Login Page')
        return self.wd.get(self.base_url)

    def open_main_page(self):
        logger.info('Open Main Page')
        return self.wd.get((self.base_url + '/welcome'))