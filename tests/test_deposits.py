import time

import allure
import pytest

from common.depost_page_constants import DepositPageConstants as Const


@allure.suite("Депозиты")
class TestsDeposit:
    @allure.title("Тест на успешное открытие депозита")
    @allure.tag("positive")
    def test_create_deposits(self, authorized_user):
        """
        Тест на успешное добавление карты другого банка
        Шаги:
            1. Нажать на вкладку "Вклады"
            ОР:  Перешли на страницу "Вклады"
            URL - https://idemo.bspb.ru/deposits
            2. Нажать "Открыть вклад"
            ОР: Открылась страница "Открыть новый вклад"
            URL - https://idemo.bspb.ru/deposits/rates
            3. Выбрать валюту - USD, срок - свободный срок
            ОР: Стал доступен единственны вклад " Демо депозит №2"
            4. Нажать "Открыть вклад"
            ОР: Перешли на страницу "Вклады Открыть новый вклад""
            URL - https://idemo.bspb.ru/deposits/form/10170?days=15
            5. В поле сумма ввести - 5000
            ОР: сумма валидная, без предупреждений
            Оценочный доход стал равен - 5.64 $
            6. Выбрать дату окончания через календарь - 06.09.2020
            ОР: Оценочный доход  изменился (Каждый день кол-во дней вклада до 6.09.20
            уменьшается, поэтому цифра будет меняться)
            7. Нажать "Дальше"
            ОР: Открылась страница превью вклада
            URL - https://idemo.bspb.ru/deposits/preview
            8. Нажать "Ознакомлен"
            ОР: Кнопка "Подтвердить" стала доступной
            9. Нажать "Подвердить"
            ОР: Перешли на страницу "Вклады" , появилось предупреждение
            о успешном добавлении вклада
            URL - https://idemo.bspb.ru/deposits
        """
        authorized_user.open_free_term_usd_deposit(Const.AMOUNT)
        # authorized_user.open_main_page()
        # authorized_user.main_page.click_on_deposits()
        # authorized_user.deposit_page.click_open_deposit()
        # authorized_user.deposit_page.choose_usd()
        # authorized_user.deposit_page.choose_free_term()
        # authorized_user.deposit_page.choose_demo_2_deposit()
        # authorized_user.deposit_page.input_to_amount_field(Const.AMOUNT)
        # authorized_user.deposit_page.choose_end_date()
        # authorized_user.deposit_page.click_next_button()
        time.sleep(4)
        authorized_user.deposit_page.click_agree_condition()
        authorized_user.deposit_page.click_confirm_button()
        assert authorized_user.deposit_page.is_displayed_success_logo()

    @allure.title("тест на негативную сумму депозита")
    @allure.tag("negative")
    @pytest.mark.parametrize("test_data", Const.TEST_DATA_FOR_AMOUNT)
    def test_invalid_amount(self, authorized_user, test_data):
        authorized_user.open_free_term_usd_deposit(test_data)
        assert authorized_user.deposit_page.invalid_amount_alert_is_visible()
