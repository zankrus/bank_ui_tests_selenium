from selenium.webdriver.common.by import By


class LoginPageLocators:
    username_field = (By.XPATH, '//input[@name="username"]')
    password_field = (By.XPATH, '//input[@name="password"]')
