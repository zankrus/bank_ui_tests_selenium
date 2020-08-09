import pytest

from pages.application import Application


@pytest.fixture(scope="session")
def app(request):
    base_url = "http://automationpractice.com/"
    fixture = Application(base_url)
    fixture.wd.implicitly_wait(10)
    fixture.wd.maximize_window()
    yield fixture
    fixture.wd.quit()