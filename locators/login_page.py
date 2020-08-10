from selenium.webdriver.common.by import By


class LoginPageLocators:
    username_field = (By.XPATH, '//input[@name="username"]')
    password_field = (By.XPATH, '//input[@name="password"]')
    enter_button = (By.XPATH, "//button")
    invalid_username_password_alert = (By.XPATH, '//div[@class ="alert alert-error"]')
