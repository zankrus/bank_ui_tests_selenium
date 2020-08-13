import time

import allure


@allure.suite("Операции с картами")
class TestCards:
    @allure.title("Тест на добавление карты другого банка")
    @allure.tag("positive")
    def test_add_other_bank_card(self, authorized_user):
        authorized_user.main_page.click_on_cards_button()
        authorized_user.card_page.click_on_other_bank_card()
        authorized_user.card_page.add_other_bank_card(authorized_user.fake_data)
        time.sleep(5)