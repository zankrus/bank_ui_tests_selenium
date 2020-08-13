from selenium.webdriver.common.by import By


class DepositsPageLocators:
    usd = (By.XPATH, "//input[@value='USD']")
    free_term = (By.XPATH, "//input[@value='-1']")
    open_deposit = (By.ID, "btn-show-rates")
    demo_2_deposit_open = (
        By.XPATH,
        "//a[@class='btn btn-mini btn-primary place-deposit']",
    )
    end_date = (By.XPATH, "//input[@id='endDate']")
    date_31_august = (By.XPATH, "//td[@class='day new'][contains(text(),'6')]")
    amouth = (By.ID, "amount")
    next_button = (By.XPATH, "//button[@id='submit-button']")
    agree_condition = (By.NAME, "condition.newDepositConditions")
    confirm_button = (By.ID, "confirm")
    succes_deposit = (By.XPATH, "//div[@class='alert alert-success']")
    percent_of_deposit = (By.ID, "estimated-interest")
    invalid_amouth_alert = (By.XPATH, "//div[@class='tooltip fade right in']")


