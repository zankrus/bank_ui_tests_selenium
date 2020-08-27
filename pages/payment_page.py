"""Файл для класса страницы Переводы."""
import logging

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.payment_page_locators import PaymentPageLocators

logger = logging.getLogger()


class PaymentPage:
    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 10)

    def next_button(self):
        return self.app.wd.find_element(*PaymentPageLocators.NEXT_BUTTON)

    @allure.step("Нажатие кнопки Дальше")
    def click_next_button(self):
        logger.info("Видимость элемента - кнопка Дальше - "
                    + str(self.next_button().is_displayed())
                    )
        return self.next_button().click()

    def error_alert(self):
        return self.app.wd.find_element(*PaymentPageLocators.ERROR_MESSAGE)

    @allure.step("Проверка текста предупреждения")
    def text_of_error_alert(self):
        self.wait.until(EC.visibility_of_element_located(PaymentPageLocators.ERROR_MESSAGE))
        logger.info("Видимость элемента - предупреждение 'В демо-версии переводы не разрешены' - "
                    + str(self.error_alert().is_displayed())
                    )
        return self.error_alert().text