"""Модуль страницы Авторизации."""
import logging

import allure

from common.login_page_constants import LoginPageConstants as Const
from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger()

class LoginPage:
    """Класс страницы авторизации"""

    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 10)

    def username_field(self):
        return self.app.wd.find_element(*LoginPageLocators.USERNAME_FIELD)

    def password_field(self):
        return self.app.wd.find_element(*LoginPageLocators.PASSWORD_FIELD)

    def enter_button(self):
        return self.app.wd.find_element(*LoginPageLocators.ENTER_BUTTON)

    @allure.step('Нажать кнопку "Войти')
    def click_enter_button(self):
        logger.info(
            "Видимость элемента - Кнопка Войти - "
            + str(self.enter_button().is_displayed())
        )
        return self.enter_button().click()

    @allure.step("Ввод логина")
    def input_username(self, username):
        self.username_field().clear()
        logger.info(
            "Видимость элемента - Поле - username - "
            + str(self.username_field().is_displayed())
        )
        return self.username_field().send_keys(username)

    @allure.step("Ввод пароля")
    def input_password(self, password):
        self.password_field().clear()
        logger.info(
            "Видимость элемента - Поле - password - "
            + str(self.password_field().is_displayed())
        )
        return self.password_field().send_keys(password)

    def invalid_username_alert(self):
        return self.app.wd.find_element(
            *LoginPageLocators.INVALID_USERNAME_PASSWORD_ALERT
        )

    @allure.step("Проверка текста предупреждения о неверном логине/пароле")
    def text_of_invalid_username_alert(self):
        return self.invalid_username_alert().text

    @allure.step("Проверка отображается ли предупреждение")
    def is_displayed_alert_invalid_username_or_password(self):
        return self.invalid_username_alert().is_displayed()

    def restore_access_button(self):
        return self.app.wd.find_element(*LoginPageLocators.FORGOT_PASSWORD)

    @allure.step('Нажать на "Забыл пароль"')
    def click_on_restore_access_button(self):
        return self.restore_access_button().click()

    def reset_password_dialogue(self):
        return self.app.wd.find_element(*LoginPageLocators.RESET_PASSWORD_DIALOGUE)

    @allure.step("Проверка отображения диалогового окна о забытии пароля")
    def is_displayed_rest_password_dialogue(self):
        self.wait.until(
            EC.text_to_be_present_in_element(
                LoginPageLocators.FORGOT_PASSWORD_TEXT, Const.FORGET_PASSWORD_TEXT
            )
        )
        return self.reset_password_dialogue().is_enabled()

    @allure.step("Проверка текста забыл логин или пароль")
    def forgot_password_text(self):
        return self.app.wd.find_element(*LoginPageLocators.FORGOT_PASSWORD_TEXT).text

    def switch_lang_button(self):
        return self.app.wd.find_element(*LoginPageLocators.SWITCH_LANG)

    @allure.step("Сменить язык на eng/rus")
    def click_switch_lang(self):
        return self.switch_lang_button().click()
