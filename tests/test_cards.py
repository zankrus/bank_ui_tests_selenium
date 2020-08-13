import time

import allure


@allure.suite("Операции с картами")
class TestCards:
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
        :param authorized_user: фикстура авторизованного юзера
        :return: None
        """
        authorized_user.open_main_page()
        authorized_user.main_page.click_on_cards_button()
        authorized_user.card_page.click_on_other_bank_card()
        authorized_user.card_page.add_other_bank_card(authorized_user.fake_data)
        assert authorized_user.card_page.card_holder_preview_text() == authorized_user.fake_data.name
        assert authorized_user.card_page.card_expiring_preview_text() \
               == authorized_user.fake_data.credit_card_expire_date
        time.sleep(4)
        authorized_user.card_page.confirm_button_click()
        assert authorized_user.card_page.success_alert_is_displayed()
