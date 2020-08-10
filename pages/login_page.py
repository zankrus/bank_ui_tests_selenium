from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from locators.login_page import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
from common.LoginPageConstants import LoginPageConstants as const


class LoginPage:
    def __init__(self, app):
        self.app = app

    def username_field(self):
        return self.app.wd.find_element(*LoginPageLocators.username_field)

    def password_field(self):
        return self.app.wd.find_element(*LoginPageLocators.password_field)

    def enter_button(self):
        return self.app.wd.find_element(*LoginPageLocators.enter_button)

    def click_enter_button(self):
        return self.enter_button().click()

    def input_username(self, username):
        self.username_field().clear()
        return self.username_field().send_keys(username)

    def input_password(self, password):
        self.password_field().clear()
        return self.password_field().send_keys(password)

    def invalid_username_alert(self):
        return self.app.wd.find_element(
            *LoginPageLocators.invalid_username_password_alert
        )

    def text_of_ivalid_username_alert(self):
        return self.invalid_username_alert().text

    def is_displayed_alert_invalid_username_or_password(self):
        return self.invalid_username_alert().is_displayed()

    def restore_access_button(self):
        return self.app.wd.find_element(*LoginPageLocators.forgot_password)

    def click_on_restore_access_button(self):
        return self.restore_access_button().click()

    def reset_password_dialogue(self):
        return self.app.wd.find_element(*LoginPageLocators.reset_password_dialogue)

    def is_displayed_rest_password_dialogue(self):
        wait = WebDriverWait(self.app.wd, 10)
        wait.until(EC.text_to_be_present_in_element(LoginPageLocators.forgot_password_text,
                                                    const.forget_password_text))
        return self.reset_password_dialogue().is_enabled()

    def forgot_password_text(self):
        return self.app.wd.find_element(*LoginPageLocators.forgot_password_text).text

    def switch_lang_button(self):
        return self.app.wd.find_element(*LoginPageLocators.switch_lang)

    def click_switch_lang(self):
        return self.switch_lang_button().click()