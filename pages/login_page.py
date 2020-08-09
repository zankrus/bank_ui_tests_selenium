from locators.login_page import LoginPageLocators


class LoginPage:
    def __init__(self, app):
        self.app = app

    def username_field(self):
        return self.app.wd.find_element(*LoginPageLocators.username_field)

    def password_field(self):
        return self.app.wd.find_element(*LoginPageLocators.password_field)
