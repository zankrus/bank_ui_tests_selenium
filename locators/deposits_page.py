from selenium.webdriver.common.by import By


class DepositsPageLocators:
    USD = (By.XPATH, "//input[@value='USD']")
    FREE_TERM = (By.XPATH, "//input[@value='-1']")
    OPEN_DEPOSIT = (By.ID, "btn-show-rates")
    DEMO_2_DEPOSIT_OPEN = (
        By.XPATH,
        "//a[@class='btn btn-mini btn-primary place-deposit']",
    )
    END_DATE = (By.XPATH, "//input[@id='endDate']")
    DATE_06_SEPTEMBER = (By.XPATH, "//td[@class='day new'][contains(text(),'6')]")
    AMOUNT = (By.ID, "amount")
    NEXT_BUTTON = (By.XPATH, "//button[@id='submit-button']")
    AGREE_CONDITION = (By.XPATH, "//input[@name='condition.newDepositConditions']")
    CONFIRM_BUTTON = (By.ID, "confirm")
    SUCCESS_DEPOSIT = (By.XPATH, "//div[@class='alert alert-success']")
    PERCENT_OF_DEPOSIT = (By.ID, "estimated-interest")
    INVALID_AMOUNT_ALERT = (By.XPATH, "//div[@class='tooltip fade right in']")
