"""Модуль тестов с Картами."""
import allure

from common.card_page_constants import CardPageConstants as Const

@allure.suite("Операции с картами")
class TestCards:
    """Класс тестов с Картами"""

    @allure.title("Тест на добавление карты другого банка")
    @allure.tag("positive")
    def test_add_other_bank_card(self, authorized_user):
        """
        Тест на успешное добавление карты другого банка
        Шаги:
            1. Нажать на вкладку "Карты"
            ОР:  Перешли на страницу "Карты"
            URL - https://idemo.bspb.ru/cards
            2. Внизу страницы нажать на кнопку " Добавить карту другого банка"
            ОР: Перешли на страницу "Добавить карту другого банка"
            URL - https://idemo.bspb.ru/other-bank-cards/new
            3. Заполняем поля валидными данными из класса FakeData
            4. Нажать "Сохранить"
            ОР: Перешли на страницу превью с вводом смс-кода
            URL - https://idemo.bspb.ru/other-bank-cards/preview
            5. Нажать "Подтвердить"
            ОР: Оказались на странице обзора карт. Появилось сообщение
            "Карта ХХХХХ добавлена"
        """
        authorized_user.add_other_bank_card_page()
        authorized_user.card_page.add_other_bank_card(authorized_user.fake_data)
        assert (
            authorized_user.card_page.card_holder_preview_text()
            == authorized_user.fake_data.name
        )
        assert (
            authorized_user.card_page.card_expiring_preview_text()
            == authorized_user.fake_data.credit_card_expire_date
        )
        authorized_user.card_page.confirm_button_click()
        assert authorized_user.card_page.success_alert_is_displayed()

    @allure.title("Тест на добавление карты другого банка c незаполненными полями")
    @allure.tag("negative")
    def test_add_other_bank_card_with_empty_field(self, authorized_user):
        """
               Тест на успешное добавление карты другого банка
               Шаги:
                   1. Нажать на вкладку "Карты"
                   ОР:  Перешли на страницу "Карты"
                   URL - https://idemo.bspb.ru/cards
                   2. Внизу страницы нажать на кнопку " Добавить карту другого банка"
                   ОР: Перешли на страницу "Добавить карту другого банка"
                   URL - https://idemo.bspb.ru/other-bank-cards/new
                   3. Нажать "Сохранить"
                   ОР: Появились предупреждения "Обязательное поле" .
               """
        authorized_user.add_other_bank_card_page()
        authorized_user.card_page.other_bank_card_save_button_click()
        assert authorized_user.card_page.text_empty_card_number_error() == Const.EMPTY_FIELD_ERROR_MESSAGE
        assert authorized_user.card_page.text_empty_card_expire_error() == Const.EMPTY_FIELD_ERROR_MESSAGE
        assert authorized_user.card_page.text_empty_card_csv_error() == Const.EMPTY_FIELD_ERROR_MESSAGE
        assert authorized_user.card_page.text_not_correct_fields_error() == Const.NOT_CORRECT_FIELDS_ALERT


