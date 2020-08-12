import pytest
from common.LoginPageConstants import LoginPageConstants as const
from pages.application import Application


@pytest.fixture(scope="session")
def app(request):
    base_url = request.config.getoption("--base-url")
    headless = request.config.getoption("--headless")
    fixture = Application(base_url, headless)
    fixture.wd.implicitly_wait(10)
    fixture.wd.maximize_window()
    yield fixture
    fixture.wd.quit()


@pytest.fixture(scope="session")
def authorized_user(app, request):
    fixture = app
    fixture.open_login_page()
    fixture.login_page.click_enter_button()
    fixture.login_page.click_enter_button()
    fixture.open_main_page()
    if fixture.wd.title == const.title_eng :
        fixture.main_page.change_lang()
        assert app.wd.title == const.title_rus
    yield fixture
    fixture.wd.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://idemo.bspb.ru",
        help="enter base_url",
    ),
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="launching browser without gui",
    )