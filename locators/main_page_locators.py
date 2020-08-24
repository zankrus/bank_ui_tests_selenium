"""Файл для хранения локаторов главной страницы."""
from selenium.webdriver.common.by import By


class MainPageLocators:
    """Класс для хранения локаторов главной страницы."""

    DEPOSITS = (By.XPATH, "//li[@id='deposits']")
    CHANGE_LANG = (By.XPATH, "//button[@class='btn btn-text btn-toggle active']")
    CARDS = (By.ID, "cards")
    QUESTION_BUTTON = (By.ID, "faq-link")
    LOGOUT_BUTTON = (By.CLASS_NAME, "icon-close")
    WELCOME_TOUR = (By.CLASS_NAME, "restart-welcome-tour")
    WELCOME_TOUR_NEXT_BUTTON = (By.ID, "welcome-tour-next")
    BANK_OVERVIEW = (By.ID, "bank-overview")
    WELCOME_TOUR_END = (By.ID, "welcome-tour-end")
    WELCOME_TOUR_TITLE = (By.XPATH, "//div[@class='welcome-tour-title popover-title']")

    @staticmethod
    def account_number(number):
        return By.XPATH, f"//*[contains(text(),'{number}')]"
