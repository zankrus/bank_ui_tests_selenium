import allure

from locators.main_page import MainPageLocators


class MainPage:
    def __init__(self, app):
        self.app = app

    def deposits_button(self):
        return self.app.wd.find_element(*MainPageLocators.deposits)

    @allure.step("Нажатие на кнопку Вклады")
    def click_on_deposits(self):
        return self.deposits_button().click()

    def change_lang_button(self):
        return self.app.wd.find_element(*MainPageLocators.change_lang)

    @allure.step("Смена языка")
    def change_lang(self):
        return self.change_lang().click()