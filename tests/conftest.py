import os

import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_version', default='100.0')


@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    load_dotenv()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    browser_version = request.config.getoption('--browser_version')
    browser.config.base_url = os.getenv('selene.base_url', 'https://demoqa.com')
    browser_name = os.getenv('selene.browser_name', 'selenoid_chrome')
    browser.config.hold_browser_open = bool(
        os.getenv('selene.hold_browser_open', 'false').lower()
    )
    '''
    env -S 'selen.base_url = https://google.com' pytest tests/v1/test_practice_form.py
    '''
    browser.config.timeout = float(os.getenv('selene.timeout', '3'))
    browser.config.window_width = 1000
    browser.config.window_height = 1200

    # @pytest.fixture(autouse=True)
    # def change_test_dir_to_project_root(request, monkeypatch):
    #     monkeypatch.chdir(request.fspath.dirname)
    # https://stackoverflow.com/questions/62044541/change-pytest-working-directory-to-test-case-directory

    if browser_name == 'selenoid_chrome':

        options = Options()
        selenoid_capabilities = {
            'browserName': 'chrome',
            'browserVersion': browser_version,
            'selenoid:options': {'enableVNC': True, 'enableVideo': True},
        }
        options.capabilities.update(selenoid_capabilities)
        browser.config.driver = webdriver.Remote(
            command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
            options=options,
        )

    else:
        browser.config.browser_name = browser_name

    yield browser
