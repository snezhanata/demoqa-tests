import os
import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def browser_management():
    # browser.config.base_url = 'https://demoqa.com'
    browser.config.base_url = os.getenv(
        'selene.base_url', 'https://demoqa.com'
    )  # env -S 'selen.base_url = https://google.com' pytest tests/v1/test_practice_form.py
    # browser.config.browser_name = 'chrome'
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    browser.config.hold_browser_open = bool(
        os.getenv('selene.hold_browser_open', 'false').lower()
    )
    browser.config.timeout = float(os.getenv('selene.timeout', '3'))
    browser.config.window_width = 1000
    browser.config.window_height = 1200
    yield
    browser.close()



