"""Файл тестов по оплате налогов с главной страницы"""
import time
from common.main_page_constants import MainPageConstants as Const


class TestPayTaxesFromMainPage:
    """
    Класс для тестов по оплате налогов с главной страницы
    """
    def test_pay_taxes_from_main_page(self, authorized_user):
        """
        Шаги:
            1) Перейти на главную страницу
            2) Кликаем на иконку ФНС,под которой указан номер - 500100732259
            3)
        """
        authorized_user.open_main_page()
        assert authorized_user.main_page.deposits_button().is_displayed()
        assert authorized_user.wd.current_url == 'https://idemo.bspb.ru/welcome'
        authorized_user.main_page.click_on_account_number()
        authorized_user.taxes_page.click_on_check_taxes_button()
        assert authorized_user.taxes_page.taxes_check_result_text_is_displayed()
        authorized_user.taxes_page.click_pay_tax_button()



