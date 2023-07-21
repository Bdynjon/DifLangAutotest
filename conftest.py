import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="ru", help="Choose language: ru or es")


@pytest.fixture()
def browser(request):

    language = request.config.getoption('language')
    # if language not in ('ru', 'es'):
    #     raise pytest.UsageError("--language should be es or ru")

    options = Options()
    options.add_experimental_option('prefs', {
        'intl.accept_languages': language
    })
    browser = Chrome(options=options)

    yield browser

    browser.quit()
