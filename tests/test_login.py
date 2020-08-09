import time


class Test:

    def test_login(self, app):
        app.wd.get('https://idemo.bspb.ru/')
        time.sleep(5)
        app.login_page.username_field().clear()
        app.login_page.password_field().clear()
        time.sleep(5)
