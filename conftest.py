import pytest

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


@pytest.fixture(scope="module")
def auhorized_user(app):
    app.open_login_page()
    app.login_page.click_enter_button()
    app.login_page.click_enter_button()
    app.open_main_page()
    yield app
    app.wd.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://idemo.bspb.ru",
        help="enter base_url",
    ),
    parser.addoption(
        "--headless",
        action="store",
        default=False,
        help="launching browser without gui",
    )