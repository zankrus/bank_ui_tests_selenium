from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage


class Application:
    def __init__(self, base_url):
        driver_path = ChromeDriverManager().install()
        self.wd = webdriver.Chrome(driver_path)
        self.base_url = base_url
        self.login_page = LoginPage(self)