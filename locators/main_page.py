from selenium.webdriver.common.by import By


class MainPageLocators:
    DEPOSITS = (By.XPATH, "//li[@id='deposits']")
    CHANGE_LANG = (By.XPATH,
                   "//button[@class='btn btn-text btn-toggle active']")
    CARDS = (By.ID, 'cards')

    LOGOUT_BUTTON = (By.CLASS_NAME, "icon-close")
