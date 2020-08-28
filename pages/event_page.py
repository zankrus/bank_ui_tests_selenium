"""Модуль страницы События."""
import logging

import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.event_page_locators import EvenPageLocators as Loc

logger = logging.getLogger()


class EventPage:
    """Класс страницы События."""

    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 10)

    def event_by_title(self, text):
        try:
            self.wait.until(
                EC.visibility_of_element_located(Loc.event_contains_text(text))
            )
            return self.app.wd.find_element(*Loc.event_contains_text(text))
        except Exception:
            return False

    @allure.step("Выбираем в календаре события с названием - {text}")
    def open_event_by_title(self, text):
        logger.info(
            f"Видимость элемента - Cобытие с заголовком -{text}  - "
            + str(
                self.app.wd.find_element(*Loc.event_contains_text(text)).is_displayed()
            )
        )
        self.wait.until(EC.visibility_of_element_located(Loc.event_contains_text(text)))
        return self.event_by_title(text).click()

    def delete_event_button(self):
        return self.app.wd.find_element(*Loc.DELETE_EVENT_BUTTON)

    @allure.step("Нажимаем Удалить ")
    def click_delete_event(self):
        logger.info(
            "Видимость элемента - Кнопка удалить  - "
            + str(self.delete_event_button().is_displayed())
        )
        self.wait.until(EC.visibility_of_element_located(Loc.DELETE_EVENT_BUTTON))
        return self.delete_event_button().click()

    def confirm_delete_button(self):
        self.wait.until(EC.visibility_of_element_located(Loc.CONFIRM_DELETE_BUTTON))
        return self.app.wd.find_element(*Loc.CONFIRM_DELETE_BUTTON)

    @allure.step("Нажимаем ДА ")
    def click_confirm_button(self):
        logger.info(
            "Видимость элемента - Кнопка ДА  - "
            + str(self.confirm_delete_button().is_displayed())
        )
        self.wait.until(EC.visibility_of_element_located(Loc.CONFIRM_DELETE_BUTTON))
        return self.confirm_delete_button().click()

    @staticmethod
    def element_is_displayed(element):
        try:
            return element.is_displayed()
        except Exception:
            return False
