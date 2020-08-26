# """Файл с тестами страницы авторизации."""
# import allure
# import pytest
# import time
# from common.login_page_constants import LoginPageConstants as Const
#
# @allure.suite("Авторизация")
# class TestLoginPage:
#     @allure.title("тест на успешную авторизацию")
#     @allure.tag("positive")
#     def test_login(self, app):
#         """
#         Тест на успешную авторизацию пользователя
#         Шаги:
#             1. Перейти по ссылке https://idemo.bspb.ru/auth
#             ОР:  'Интернет банк - Банк Санкт-Петербург в шапке, произошел редирект
#             2. Логин и пароль автозополнились , нажать "Войти"
#             3. СМС код автозаполнился - нажать "Войти"
#             ОР: Оказались на главной странице личного кабинета
#             URL - https://idemo.bspb.ru/welcome
#             4. Выйти из аккаунта
#             ОР: Оказались на странице логина
#         """
#         app.open_login_page()
#         assert Const.REDIRECT_URL in app.wd.current_url, "Не произошел редирект"
#         app.login_page.click_enter_button()
#         app.login_page.click_enter_button()
#         assert Const.MAIN_PAGE_URL in app.wd.current_url, "Урл отличается"
#         app.open_main_page()
#         app.main_page.click_on_logout_button()

    #
    # @allure.title("тест на негативную авторизацию")
    # @allure.tag("negative")
    # @pytest.mark.parametrize("login, password", Const.AUTH_DATA)
    # def test_negative_login(self, app, login, password):
    #     """
    #     Тест на неуспешную авторизацию
    #            Шаги:
    #            1. Перейти по ссылке https://idemo.bspb.ru/auth
    #            ОР:  'Интернет банк - Банк Санкт-Петербург в шапке, произошел редирект
    #            2. Cтереть логин по умолчанию, ввести свой логин
    #            3. Стереть пароль по умолчанию, ввести свой пароль
    #            4. Нажать "Войти"
    #            ОР: Появилось предепреждение "Неверные данные пользователя (осталось 2 попытки)"
    #            URL - https://idemo.bspb.ru/auth/login
    #      """
    #     app.open_login_page()
    #     app.login_page.input_username(login)
    #     app.login_page.input_password(password)
    #     app.login_page.click_enter_button()
    #     assert (
    #         app.login_page.is_displayed_alert_invalid_username_or_password()
    #     ), "Предупреждение отсутствует"
    #     assert (
    #         Const.WRONG_PASSWORD_OR_LOGIN_ALERT
    #         in app.login_page.text_of_invalid_username_alert()
    #     ), "текст предупреждения отличается"
    #     assert Const.WRONG_LOGIN_URL in app.wd.current_url, "URL отличается"

    # @allure.title("тест на появления окна восстановления пароля")
    # @allure.tag("positive")
    # def test_forgot_login_password(self, app):
    #     """
    #     Тест на появление окна "Забыли логин или пароль"
    #     Шаги:
    #         1.Перейти по ссылке https://idemo.bspb.ru/auth
    #         2.Нажать "Восстановить доступ"
    #         ОР : Появилось окно с информацией по восстановлению логина или пароля
    #     """
    #     app.open_login_page()
    #     app.login_page.click_on_restore_access_button()
    #     assert (
    #         app.login_page.is_displayed_rest_password_dialogue()
    #     ), "Диалог сброса пароля не отображается "
    #     assert (
    #         Const.FORGET_PASSWORD_TEXT == app.login_page.forgot_password_text()
    #     ), " текст отличается"
