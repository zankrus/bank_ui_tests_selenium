from selenium.webdriver.common.by import By


class MainPageLocators:
    deposits = (By.XPATH, "//li[@id='deposits']")
    change_lang = (By.XPATH,
                   "//button[@class='btn btn-text btn-toggle active']")
    cards = (By.ID, 'cards')

    logout_button = (By.CLASS_NAME, "icon-close")
