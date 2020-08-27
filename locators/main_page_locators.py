"""Файл для хранения локаторов главной страницы."""
from selenium.webdriver.common.by import By


class MainPageLocators:
    """Класс для хранения локаторов главной страницы."""
    DEPOSITS = (By.XPATH, "//li[@id='deposits']")
    CHANGE_LANG = (By.XPATH, "//button[@class='btn btn-text btn-toggle active']")
    CARDS = (By.ID, "cards")
    QUESTION_BUTTON = (By.CSS_SELECTOR, "#faq-link")
    LOGOUT_BUTTON = (By.CLASS_NAME, "icon-close")
    WELCOME_TOUR = (By.CLASS_NAME, "restart-welcome-tour")
    WELCOME_TOUR_NEXT_BUTTON = (By.ID, "welcome-tour-next")
    BANK_OVERVIEW = (By.ID, "bank-overview")
    WELCOME_TOUR_END = (By.ID, "welcome-tour-end")
    WELCOME_TOUR_TITLE = (By.XPATH, "//div[@class='welcome-tour-title popover-title']")
    TESING = (By.XPATH, "//div[contains(text(),'500100732259')]")
    PRIVATE_EVENT = (By.XPATH, "//div[@class='calendar-event event-add']")
    EVENT_NAME = (By.XPATH, "//input[@name='event.name']")
    EVENT_NAME_DESCRIPTION = (By.XPATH, "//textarea[@name='event.description']")
    EVENT_NAME_SAVE_BUTTON = (By.XPATH, '//*[contains(text(),"Сохранить")]')
