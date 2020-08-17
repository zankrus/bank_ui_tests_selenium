from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_FIELD = (By.XPATH, '//input[@name="username"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name="password"]')
    ENTER_BUTTON = (By.XPATH, "//button")
    INVALID_USERNAME_PASSWORD_ALERT = (By.XPATH,
                                       '//div[@class ="alert alert-error"]')
    FORGOT_PASSWORD = (By.XPATH, "//a[@class='chevron']")
    RESET_PASSWORD_DIALOGUE = (By.XPATH, "//div[@id='reset-password-dialog']")
    FORGOT_PASSWORD_TEXT = (By.XPATH, "//h3")
    SWITCH_LANG = (By.XPATH, "//a[@class='chevron locale inline-block']")
