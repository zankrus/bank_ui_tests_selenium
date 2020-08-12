from selenium.webdriver.common.by import By


class LoginPageLocators:
    username_field = (By.XPATH, '//input[@name="username"]')
    password_field = (By.XPATH, '//input[@name="password"]')
    enter_button = (By.XPATH, "//button")
    invalid_username_password_alert = (By.XPATH,
                                       '//div[@class ="alert alert-error"]')
    forgot_password = (By.XPATH, "//a[@class='chevron']")
    reset_password_dialogue = (By.XPATH, "//div[@id='reset-password-dialog']")
    forgot_password_text = (By.XPATH, "//h3")
    switch_lang = (By.XPATH, "//a[@class='chevron locale inline-block']")
