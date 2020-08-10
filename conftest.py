import pytest

from pages.application import Application


@pytest.fixture(scope="session")
def app(request):
    base_url = "https://idemo.bspb.ru/"
    fixture = Application(base_url)
    fixture.wd.implicitly_wait(10)
    fixture.wd.maximize_window()
    yield fixture
    fixture.wd.quit()


@pytest.fixture(scope="module")
def auhorized_user(app):
    app.open_login_page()
    app.login_page.click_enter_button()
    app.login_page.click_enter_button()
    yield app
    app.wd.quit()
