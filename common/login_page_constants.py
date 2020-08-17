"""Файл для хранения констант страницы авторизации"""


class LoginPageConstants:
    AUTH_DATA = [
        (111, 2322),
        ("roben", "roben"),
        ("роберт", 1234),
        ("", "")
    ]
    BASE_URL = "https://idemo.bspb.ru"
    MAIN_PAGE_URL = BASE_URL + "/welcome"
    REDIRECT_URL = BASE_URL + \
                   "/auth" \
                   "?response_type=code&client_id" \
                   "=1&redirect_uri=https%3A%2F%2F" \
                   "idemo.bspb.ru%2Flogin%2Fsuccess" \
                   "&prefetch_uri=https%3A%2F%2Fidemo" \
                   ".bspb.ru%2Flogin%2Fprefetch&force_" \
                   "new_session=true"

    WRONG_LOGIN_URL = "https://idemo.bspb.ru/auth/login"
    TITLE_ENG = "Bank Saint-Petersburg"
    TITLE_RUS = "Интернет банк - Банк Санкт-Петербург"
    WRONG_PASSWORD_OR_LOGIN_ALERT = "Неверные данные пользователя (осталось 2 попытки)"
    FORGET_PASSWORD_TEXT = "Забыли логин или пароль?"
