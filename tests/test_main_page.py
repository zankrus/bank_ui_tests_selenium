"""Модуль тестов главной страницы."""
import allure
from common.main_page_constants import MainPageConstants as Const


@allure.suite("Операции с картами")
class TestMainPage:
    """Класс тестов главной страницы"""

    @allure.title("тест визуального помощника")
    @allure.tag("positive")
    def test_visual_helper(self, authorized_user):
        authorized_user.open_main_page()
        authorized_user.main_page.click_question_button()
        authorized_user.main_page.click_welcome_tour()
        assert authorized_user.main_page.is_displayed_bank_overview(), "Элемент 'ОБЗОР' не отображен"
        assert authorized_user.main_page.text_welcome_tour_title(Const.WELCOME_TOUR_TITLE[0]) \
               == Const.WELCOME_TOUR_TITLE[0]
        authorized_user.main_page.click_welcome_tour_next_button()
        assert authorized_user.main_page.text_welcome_tour_title(Const.WELCOME_TOUR_TITLE[1]) == \
               Const.WELCOME_TOUR_TITLE[1]
        authorized_user.main_page.click_welcome_tour_next_button()
        assert authorized_user.main_page.text_welcome_tour_title(Const.WELCOME_TOUR_TITLE[2]) == \
               Const.WELCOME_TOUR_TITLE[2]
        authorized_user.main_page.click_welcome_tour_next_button()
        assert authorized_user.main_page.text_welcome_tour_title(Const.WELCOME_TOUR_TITLE[3]) == \
               Const.WELCOME_TOUR_TITLE[3]
        authorized_user.main_page.click_welcome_tour_next_button()
        assert authorized_user.main_page.text_welcome_tour_title(Const.WELCOME_TOUR_TITLE[4]) == \
               Const.WELCOME_TOUR_TITLE[4]
        authorized_user.main_page.click_end_welcome_tour_button()
