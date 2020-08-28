"""Модуль тестов главной страницы."""
import allure

from common.main_page_constants import MainPageConstants as Const
from common.payment_page_constants import PaymentPageConstants as Constpayment


@allure.suite("Тесты главной страницы")
class TestMainPage:
    """Класс тестов главной страницы"""

    @allure.title("тест визуального помощника")
    @allure.tag("positive")
    def test_visual_helper(self, authorized_user):
        """
               Шаги:
                   1) Перейти на главную страницу
                   2) Справа-сверху навести на знак вопроса
                   3) Их выпадающего списка кликнуть на "Визуальный помощник"
                   ОР: Подсвечен элемент "Обзор"
                   4) Нажать "Далее"
                   ОР: Подсвечен элемент "Счета"
                   5) Нажать "Далее"
                   ОР: Подсвечен элемент "Умный перевод"
                   6) Нажать "Далее"
                   ОР: Подсвечен элемент "Перевод из истории платежа"
                   7) Нажать "Далее"
                   ОР: Подсвечен элемент "Перевод WikiPay"
                   8) Нажать "ЗавершитЬ"
                   ОР: Вернулись на главную страницу
               """
        authorized_user.open_main_page()
        authorized_user.main_page.click_question_button()
        authorized_user.main_page.click_welcome_tour()
        assert (
            authorized_user.main_page.is_displayed_bank_overview()
        ), "Элемент 'ОБЗОР' не отображен"
        for i in range(len(Const.WELCOME_TOUR_TITLE) - 1):
            assert (
                authorized_user.main_page.text_welcome_tour_title(
                    Const.WELCOME_TOUR_TITLE[i]
                )
                == Const.WELCOME_TOUR_TITLE[i]
            )
            authorized_user.main_page.click_welcome_tour_next_button()
        authorized_user.main_page.click_end_welcome_tour_button()

    @allure.title("тест оплаты налогов , через иконку на главной странице")
    @allure.tag("positive")
    def test_pay_taxes_from_main_page(self, authorized_user):
        """
        Шаги:
            1) Перейти на главную страницу
            2) Кликаем на иконку ФНС,под которой указан номер - 500100732259
            3)
        """
        authorized_user.open_main_page()
        assert authorized_user.main_page.deposits_button().is_displayed()
        assert authorized_user.wd.current_url == "https://idemo.bspb.ru/welcome"
        authorized_user.main_page.click_on_account_number()
        authorized_user.taxes_page.click_on_check_taxes_button()
        assert authorized_user.taxes_page.taxes_check_result_text_is_displayed()
        authorized_user.taxes_page.click_pay_tax_button()
        authorized_user.payment_page.click_next_button()
        assert (
            authorized_user.payment_page.text_of_error_alert()
            == Constpayment.ERROR_MESSAGE
        )

    @allure.title("Создания личного события с главной страницы")
    @allure.tag("positive")
    def test_add_and_delete_private_event(self, authorized_user):
        """
           Шаги:
               1) Перейти на главную страницу
               2) Кликаем на иконку ФНС,под которой указан номер - 500100732259
               3)
        """
        authorized_user.open_main_page()
        authorized_user.main_page.click_private_event_button()
        authorized_user.main_page.input_event_name_field(
            authorized_user.fake_data.title
        )
        authorized_user.main_page.input_event_description_field(
            authorized_user.fake_data.text
        )
        authorized_user.main_page.click_event_save_button()
        authorized_user.event_page.open_event_by_title(authorized_user.fake_data.title)
        authorized_user.event_page.click_delete_event()
        authorized_user.event_page.click_confirm_button()
        assert (
            authorized_user.event_page.element_is_displayed(
                authorized_user.event_page.event_by_title(
                    authorized_user.fake_data.title
                )
            )
            is False
        )

    @allure.title("Создания личного события без обязательных полей")
    @allure.tag("negative")
    def test_add_and_delete_private_event_with_empty_fields(self, authorized_user):
        """
           Шаги:
               1) Перейти на главную страницу
               2) Кликаем на иконку ФНС,под которой указан номер - 500100732259
               3)
        """
        authorized_user.open_main_page()
        authorized_user.main_page.click_private_event_button()
        authorized_user.main_page.clear_event_date_field()
        authorized_user.main_page.click_event_save_button()
        assert (
            authorized_user.main_page.text_of_event_alert()
            == Const.EVENT_EMPTY_FIELD_ALERT
        )
