from locators.deposits_page import DepositsPageLocators

class DepositsPage:
    def __init__(self, app):
        self.app = app

    def open_deposit(self):
        return self.app.wd.find_element(*DepositsPageLocators.open_deposit)

    def click_open_deposit(self):
        return self.open_deposit().click()

    def usd_button(self):
        return self.app.wd.find_element(*DepositsPageLocators.usd)

    def choose_usd(self):
        return self.usd_button().click()

    def free_term_button(self):
        return self.app.wd.find_element(*DepositsPageLocators.free_term)

    def choose_free_term(self):
        return self.free_term_button().click()

    def demo_2_deposit(self):
        return self.app.wd.find_element(*DepositsPageLocators.demo_2_deposit_open)

    def choose_demo_2_deposit(self):
        return self.demo_2_deposit().click()

    def end_date(self):
        return self.app.wd.find_element(*DepositsPageLocators.end_date)

    def choose_end_date(self):
        self.end_date().click()
        self.app.wd.find_element(*DepositsPageLocators.date_31_august).click()
        return self.end_date()

    def amouth_field(self):
        return self.app.wd.find_element(*DepositsPageLocators.amouth)

    def input_to_amouth_field(self, keys):
        return self.amouth_field().send_keys(keys)

    def next_button(self):
        return self.app.wd.find_element(*DepositsPageLocators.next_button)

    def click_next_button(self):
        return self.next_button().click()

    def agree_condition(self):
        return self.app.wd.find_element(*DepositsPageLocators.agree_condition)

    def click_agree_condition(self):
        return self.agree_condition().click()

    def confirm_button(self):
        return self.app.wd.find_element(*DepositsPageLocators.confirm_button)

    def click_cofrim_button(self):
        return self.confirm_button().click()

    def success_logo(self):
        return self.app.wd.find_element(*DepositsPageLocators.succes_deposit)

    def is_displayed_success_logo(self):
        return self.success_logo().is_displayed()
