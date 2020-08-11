from locators.main_page import MainPageLocators


class MainPage:
    def __init__(self, app):
        self.app = app

    def deposits_button(self):
        return self.app.wd.find_element(*MainPageLocators.deposits)

    def click_on_deposits(self):
        return self.deposits_button().click()