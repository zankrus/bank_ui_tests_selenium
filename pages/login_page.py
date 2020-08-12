import allure
from selenium.webdriver.support.wait import WebDriverWait

from locators.login_page import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
from common.LoginPageConstants import LoginPageConstants as const


class LoginPage:
    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 10)

    def username_field(self):
        return self.app.wd.find_element(*LoginPageLocators.username_field)

    def password_field(self):
        return self.app.wd.find_element(*LoginPageLocators.password_field)

    def enter_button(self):
        return self.app.wd.find_element(*LoginPageLocators.enter_button)

    @allure.step('Нажать кнопку "Войти')
    def click_enter_button(self):
        return self.enter_button().click()

    @allure.step("Ввод логина")
    def input_username(self, username):
        self.username_field().clear()
        return self.username_field().send_keys(username)

    @allure.step("Ввод пароля")
    def input_password(self, password):
        self.password_field().clear()
        return self.password_field().send_keys(password)

    def invalid_username_alert(self):
        return self.app.wd.find_element(
            *LoginPageLocators.invalid_username_password_alert
        )

    @allure.step("Проверка текста предупреждения о неверном логине/пароле")
    def text_of_ivalid_username_alert(self):
        return self.invalid_username_alert().text

    @allure.step("Проверка отображается ли предупреждение")
    def is_displayed_alert_invalid_username_or_password(self):
        return self.invalid_username_alert().is_displayed()

    def restore_access_button(self):
        return self.app.wd.find_element(*LoginPageLocators.forgot_password)

    @allure.step('Нажать на "Забыл пароль"')
    def click_on_restore_access_button(self):
        return self.restore_access_button().click()

    def reset_password_dialogue(self):
        return self.app.wd.find_element(*LoginPageLocators.reset_password_dialogue)

    @allure.step("Проверка отображения диалогового окна о забытии пароля")
    def is_displayed_rest_password_dialogue(self):
        self.wait.until(
            EC.text_to_be_present_in_element(
                LoginPageLocators.forgot_password_text, const.forget_password_text
            )
        )
        return self.reset_password_dialogue().is_enabled()

    @allure.step("Проверка текста забыл логин или пароль")
    def forgot_password_text(self):
        return self.app.wd.find_element(*LoginPageLocators.forgot_password_text).text

    def switch_lang_button(self):
        return self.app.wd.find_element(*LoginPageLocators.switch_lang)

    @allure.step("Сменить язык на eng/rus")
    def click_switch_lang(self):
        return self.switch_lang_button().click()
