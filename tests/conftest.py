import os

import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_version', default='99.0')


@pytest.fixture(scope='session', autouse=True)
def browser_management(request):
    browser_name = os.getenv('selene.browser_name', 'selenoid')
    browser.config.window_width = 1000
    browser.config.window_height = 1200
    browser.config.base_url = os.getenv('selene.base_url', 'https://demoqa.com')
    # env -S 'selen.base_url = https://google.com' pytest tests/v1/test_practice_form.py
    browser.config.hold_browser_open = bool(
        os.getenv('selene.hold_browser_open', 'true')
    )
    # browser.config.timeout = float(os.getenv('selene.timeout', '3'))

    if browser_name != 'selenoid':
        browser.config.browser_name = browser_name

    else:
        load_dotenv()
        login = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')
        options = Options()
        browser_version = request.config.getoption('--browser_version')
        selenoid_capabilities = {
            'browserName': 'chrome',
            'browserVersion': browser_version,
            'selenoid:options': {'enableVNC': True, 'enableVideo': True},
        }
        options.capabilities.update(selenoid_capabilities)
        driver = webdriver.Remote(
            command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
            options=options,
        )
        browser.config.driver = driver
    yield browser
    browser.driver.close()
