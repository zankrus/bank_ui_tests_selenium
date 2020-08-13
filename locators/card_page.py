from selenium.webdriver.common.by import By


class CardPageLocators:
    other_bank_card = (By.ID, "other-bank-card-bind")
    other_bank_cardholder_input = (By.XPATH, "//input[@name='card.holderName']")
    other_bank_card_number = (By.XPATH, "//input[@name='card.number']")
    other_bank_card_expire_mouth = (By.XPATH, "//input[@placeholder='ММ']")
    other_bank_card_expire_year = (By.XPATH, "//input[@placeholder='ГГГГ']")
    other_bank_card_csv = (By.XPATH, "//input[@name='card.cvv']")
    other_bank_card_save_button = (By.XPATH, "//input[@id='bind-card']")
    card_holder_preview = (By.XPATH, "//span[@id='card-holder-name']")
    card_validity = (By.XPATH, "//span[@id='card-validity']")
    iframe = (By.XPATH, "//iframe[@id='confirmation-frame']")
    confirm_button = (By.XPATH, "//button[@id='confirm']")