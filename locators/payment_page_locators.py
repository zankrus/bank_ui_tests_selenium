"""Файл для локаторов страницы Платежи."""
from selenium.webdriver.common.by import By


class PaymentPageLocators:
    NEXT_BUTTON = (By.XPATH, "//button[@id='forward']")
    ERROR_MESSAGE = (By.XPATH, "//span[@class='error-message']")
