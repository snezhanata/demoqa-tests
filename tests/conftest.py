import os
import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from demoqa_tests.utils import attach


@pytest.fixture(scope='function', autouse=True)
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

    # @pytest.fixture(autouse=True)
    # def change_test_dir_to_project_root(request, monkeypatch):
    #     monkeypatch.chdir(request.fspath.dirname)
    # https://stackoverflow.com/questions/62044541/change-pytest-working-directory-to-test-case-directory

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }
    options.capabilities.update(selenoid_capabilities)

    # login = os.getenv('user1')
    # password = os.getenv('1234')

    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options,
    )
    browser.config.driver = driver

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
