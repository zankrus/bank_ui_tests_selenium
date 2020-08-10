"""Файл для хранения констант страницы авторизации"""


class LoginPageConstants:
    auth_data = [(11111, 23232323), ('roben', 'roben'), ('роберт', 1234), ('', '')]
    main_page_url = "https://idemo.bspb.ru/welcome"
    redirect_url = "https://idemo.bspb.ru/auth" \
                   "?response_type=code&client_id" \
                   "=1&redirect_uri=https%3A%2F%2F" \
                   "idemo.bspb.ru%2Flogin%2Fsuccess" \
                   "&prefetch_uri=https%3A%2F%2Fidemo" \
                   ".bspb.ru%2Flogin%2Fprefetch&force_" \
                   "new_session=true"
    wrong_login_url = "https://idemo.bspb.ru/auth/login"
    title = 'Bank Saint-Petersburg'
    wrong_password_or_login_alert = 'Invalid login credentials (2 attempts left)'
    forget_password_text = 'Forgot username or password?'
