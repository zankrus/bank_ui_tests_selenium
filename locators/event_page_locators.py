"""Файл для локаторов страницы Событий"""
from selenium.webdriver.common.by import By


class EvenPageLocators:
    DELETE_EVENT_BUTTON = (By.XPATH, "//a[@class='btn post']")
    CONFIRM_DELETE_BUTTON = (By.XPATH, "//button[@class='confirm btn btn-primary']")

    @staticmethod
    def event_contains_text(text: str) -> tuple:
        return By.XPATH, f"//*[contains(text(),'{text}')]"
