import os
from dataclasses import dataclass

import pytest
from selene import have, command
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


def given_opened_practice_form():
    """
    this function opens practice-form and removes advertisement banner if it appears
    """
    browser.open('/automation-practice-form')
    ads = browser.all('[id^=google_ads_][id$=container__],[id$=Advertisement]')
    ads.with_(timeout=10).should(have.size_greater_than_or_equal(3)).perform(
        command.js.remove
    )
    if ads.with_(timeout=2).wait_until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)


''' 
OR
    browser.open('/automation-practice-form')
    browser.execute_script('document.querySelector("#RightSide_Advertisement").remove()')
    ads = browser.all('[id^=google_ads_][id$=container__]')
    if ads.wait.until(have.size_less_than_or_equal(3)):
        ads.perform(command.js.remove)

'''
