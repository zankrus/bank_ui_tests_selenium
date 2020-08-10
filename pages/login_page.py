from locators.login_page import LoginPageLocators


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
