import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language')


@pytest.fixture(scope='function')
def browser(request):
    browser_language = request.config.getoption('language')
    options = Options()
    service = Service('C:/chromedriver.exe')
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    browser = webdriver.Chrome(service=service, options=options)
    yield browser
    browser.quit()
