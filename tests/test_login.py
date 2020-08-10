"""Файл с тестами страницы авторизации"""
import time

from common.LoginPageConstants import LoginPageConstants as const

import pytest


class TestLoginPage:
    def test_login(self, app):
        """Тест на успешную авторизацию пользователя
        Шаги:
            1. Перейти по ссылке https://idemo.bspb.ru/auth
            ОР:  'Интернет банк - Банк Санкт-Петербург в шапке, произошел редирект
            2. Логин и пароль автозополнились , нажать "Войти"
            3. СМС код автозаполнился - нажать "Войти"
            ОР: Оказались на главной странице личного кабинета
            URL - https://idemo.bspb.ru/welcome
        """
        app.open_login_page()
        app.login_page.click_switch_lang()
        assert const.title in app.wd.title
        assert const.redirect_url in app.wd.current_url
        app.login_page.click_enter_button()
        app.login_page.click_enter_button()
        assert const.main_page_url in app.wd.current_url

    @pytest.mark.parametrize("login, password", const.auth_data)
    def test_negative_login(self, app, login, password):
        """Тест на неуспешную авторизацию
               Шаги:
               1. Перейти по ссылке https://idemo.bspb.ru/auth
               ОР:  'Интернет банк - Банк Санкт-Петербург в шапке, произошел редирект
               2. Cтереть логин по умолчанию, ввести свой логин
               3. Стереть пароль по умолчанию, ввести свой пароль
               4. Нажать "Войти"
               ОР: Появилось предепреждение "Неверные данные пользователя (осталось 2 попытки)"
               URL - https://idemo.bspb.ru/auth/login
         """
        app.open_login_page()
        app.login_page.click_switch_lang()
        app.login_page.input_username(login)
        app.login_page.input_password(password)
        app.login_page.click_enter_button()
        assert app.login_page.is_displayed_alert_invalid_username_or_password()
        assert const.wrong_password_or_login_alert in app.login_page.text_of_ivalid_username_alert()
        assert const.wrong_login_url in app.wd.current_url

    def test_forgot_login_password(self, app):
        """
        Тест на появление окна "Забыли логин или пароль"
        Шаги:
            1.Перейти по ссылке https://idemo.bspb.ru/auth
            2.Нажать "Восстановить доступ"
            ОР : Появилось окно с информацией по восстановлению логина или пароля
        """
        app.open_login_page()
        app.login_page.click_switch_lang()
        app.login_page.click_on_restore_access_button()
        assert app.login_page.is_displayed_rest_password_dialogue()
        assert const.forget_password_text == app.login_page.forgot_password_text()



