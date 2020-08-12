import time
from common.DepostPageConstants import DepositPageConstants as const


class TestsDeposit:
    def test_create_deposits(self, authorized_user):
        authorized_user.main_page.click_on_deposits()
        authorized_user.deposit_page.click_open_deposit()
        authorized_user.deposit_page.choose_usd()
        authorized_user.deposit_page.choose_free_term()
        authorized_user.deposit_page.choose_demo_2_deposit()
        authorized_user.deposit_page.input_to_amouth_field(const.amouth)
        authorized_user.deposit_page.choose_end_date()
        authorized_user.deposit_page.click_next_button()
        authorized_user.deposit_page.click_agree_condition()
        authorized_user.deposit_page.click_cofrim_button()
        assert authorized_user.deposit_page.is_displayed_success_logo()
