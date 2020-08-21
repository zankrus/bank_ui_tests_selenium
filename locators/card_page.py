"""Файл для хранения локаторов страницы Карт."""
from selenium.webdriver.common.by import By


class CardPageLocators:
    """Класс для хранения локаторов страницы Карт."""

    OTHER_BANK_CARD = (By.ID, "other-bank-card-bind")
    OTHER_BANK_CARDHOLDER_INPUT = (By.XPATH, "//input[@name='card.holderName']")
    OTHER_BANK_CARD_NUMBER = (By.XPATH, "//input[@name='card.number']")
    OTHER_BANK_CARD_EXPIRE_MOUTH = (By.XPATH, "//input[@placeholder='ММ']")
    OTHER_BANK_CARD_EXPIRE_YEAR = (By.XPATH, "//input[@placeholder='ГГГГ']")
    OTHER_BANK_CARD_CSV = (By.XPATH, "//input[@name='card.cvv']")
    OTHER_BANK_CARD_SAVE_BUTTON = (By.XPATH, "//input[@id='bind-card']")
    CARD_HOLDER_PREVIEW = (By.XPATH, "//span[@id='card-holder-name']")
    CARD_VALIDATE = (By.XPATH, "//span[@id='card-validity']")
    IFRAME = (By.XPATH, "//iframe[@id='confirmation-frame']")
    CONFIRM_BUTTON = (By.XPATH, "//button[@id='confirm']")
    SUCCESS_ALERT = (By.XPATH, "//div[@class='alert alert-success']")
    NOT_CORRECT_FIELDS_ALERT = (By.XPATH , "//div[@class='alert alert-error hidden']")
    CARD_NUMBER_ERROR_MESSAGE = (By.XPATH, "//div[@id='other-bank-card-number']//span[@class='error-message']")
    CARD_EXPIRE_ERROR_MESSAGE = (By.XPATH, "//div[@id='other-bank-card-validity']//span[@class='error-message']")
    CSV_CODE_ERROR_MESSAGE = (By.XPATH, "//div[@id='other-bank-card-cvv']//span[@class='error-message']")

