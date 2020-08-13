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
        assert authorized_user.card_page.card_holder_preview_text() == authorized_user.fake_data.name
        assert authorized_user.card_page.card_expiring_preview_text() \
               == authorized_user.fake_data.credit_card_expire_date
        authorized_user.card_page.confirm_button_click()
        time.sleep(5)


