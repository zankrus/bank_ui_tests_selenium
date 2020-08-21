"""Модуль тестов главной страницы."""
import time

import allure
from common.main_page_constants import MainPageConstants as Const


@allure.suite("Тесты главной страницы")
class TestMainPage:
    """Класс тестов главной страницы"""

    @allure.title("тест визуального помощника")
    @allure.tag("positive")
    def test_visual_helper(self, authorized_user):
        authorized_user.open_main_page()
        time.sleep(4)
        authorized_user.main_page.click_question_button()
        authorized_user.main_page.click_welcome_tour()
        assert authorized_user.main_page.is_displayed_bank_overview(), "Элемент 'ОБЗОР' не отображен"
        for i in range(len(Const.WELCOME_TOUR_TITLE) -1):
            assert authorized_user.main_page.text_welcome_tour_title(Const.WELCOME_TOUR_TITLE[i]) == \
            Const.WELCOME_TOUR_TITLE[i]
            authorized_user.main_page.click_welcome_tour_next_button()
        authorized_user.main_page.click_end_welcome_tour_button()
