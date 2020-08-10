from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from common.loggin import setup
from pages.login_page import LoginPage

import logging

logger = logging.getLogger()


class Application:
    def __init__(self, base_url):
        setup('INFO')
        logger.setLevel('INFO')
        driver_path = ChromeDriverManager().install()
        self.wd = webdriver.Chrome(driver_path)
        self.base_url = base_url
        self.login_page = LoginPage(self)

    def open_login_page(self):
        logger.info('Open Login Page')
        return self.wd.get(self.base_url)
