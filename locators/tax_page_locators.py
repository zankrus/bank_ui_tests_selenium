"""Файл страницы локаторов Проверки налоговых задолженностей"""
from selenium.webdriver.common.by import By


class TaxPageLocators:
    """
    Класс локаторов страницы Проверки налоговых задолженностей
    """

    CHECK_TAXES_BUTTON = (By.XPATH, "//*[contains(text(),'Проверить налоги')]")
    TAXES_CHECK_RESULT = (
        By.XPATH,
        "//*[contains(text(),'Результат из Государственной информационной системы')]",
    )
    PAY_TAX_BUTTON = (By.XPATH, "//tr//a")
