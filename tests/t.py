import os
from dotenv import load_dotenv
import pytest
from selene.support.shared import browser
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from utils import attach_evidence


# @pytest.fixture(scope='function')
# def browser_management():
#     browser.config.timeout = 5
#     # browser.config.wait_for_no_overlap_found_by_js = True  # Ждет скрытия оверлеев при открытии окна. Не работает с невидимыми полями ввода например при загрузке файла через input
#     browser.config.base_url = os.getenv('selene.base_url', 'https://demoqa.com')
#     browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
#     browser.config.window_width = 1900
#     browser.config.window_height = 1300
#
#     yield


'''
Яша, [05.10.2022 10:12]
[In reply to Vladimir Sarychev]
у тебя тут в разных фикстурах вероятно разные браузеры
в первой ты используешь объект браузера пресозданный в селен, который from selene.support.shared import browser
а во второй ты используешь созданнный тобой браузер через Browser(Config(driver)), тот который from selene import Browser, Config
не будет так оно работать, надо одно что-то использовать, либо первое, либо второе...
используй пока первое, соотвтетственно передавай твой селеноидский драйвер не как Browser(Config(driver)) а как browser.config.driver = driver
и нет тут смысла делать разные фикстуры, речь идет об одном и том же - о настройке браузера, так что незачем раскидывать это по разным местам...
Яша, [05.10.2022 10:16]
или если ты хочешь в некоторых тестах сохранить те настройки что в первой фикстуре - типа сделать их общими...
но в некоторых использовать селеноидовские... и там уже не юзають autouse=True, а явно указывать эту фикстуру с селеноидом...
то тогда можно две фикстуры
просто во второй я бы переиспользовал первую... несмотря на то что первая и так автоматом запускаться будет.. 
то есть def chrome_setup(browser_management)
вот так
только имя дай нормальное, это же не просто хроум, это хроум в селеноиде... 
ну и код внутри второй - все равно должен быть browser.config.driver = ...
Яша, [05.10.2022 10:17]
в реальном проекте так все равно не делали бы... 
была бы одна фикстура browser_management
и в зависимости от параметров (считанных с тех же переменных окружений например) - ты ифом либо дополнительно прописывал бы browser.config.driver = webdriver.Remote(...) либо нет...
в options урл не передается
он передается в конфиг: Browser(Config(base_url=..., driver = webdriver.Remote(remote_url, options=options))
это если ты кастомный браузер свой создаешь
'''
'''
но пиши browser.config.driver = 
browser.config.base_url = ...

так будет пока проще

по поводу "не очень понятно":

browser_name = os.getenv('selene.browser_name', 'chrome'))
if browser_name = 'selenoid_chrome': 
    browser.config.driver = webdriver.remote(..., options=...)
else:
    browser.config.browser_name = browser_name

и тогда если ты при запуске тестов укажешь значение системной переменной как 'selenoid_chrome' то тесты побегут на селеноиде
иначе - побегут локально
'''


def pytest_addoption(parser):
    parser.addoption('--browser_version', default='100.0')
    '''
    pytest ./form/test_registration_form.py --browser_version=99
    '''


@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    load_dotenv()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    browser_version = request.config.getoption('--browser_version')
    browser_name = os.getenv('selene_browser_name', 'chrome')
    browser.config.window_width = 1900
    browser.config.window_height = 1300
    browser.config.base_url = os.getenv('selene.base_url', 'https://demoqa.com')
    '''
    export selene_browser_name='local'

    '''
    if browser_name == 'local':
        browser.config.browser_name = 'chrome'
    else:
        options = Options()
        selenoid_capabilities = {
            'browserName': 'chrome',
            'browserVersion': browser_version,
            'selenoid:options': {'enableVNC': True, 'enableVideo': True},
        }

        options.capabilities.update(selenoid_capabilities)
        driver = webdriver.Remote(
            command_executor=f'https://{login}:{password}@selenoid.autotests.cloud//wd/hub',
            options=options,
        )
        browser.config.timeout = 5
        browser.config.driver = driver

    yield

    # attach_evidence.add_video(browser)
    # attach_evidence.add_logs(browser)
    # attach_evidence.add_html(browser)
    # attach_evidence.add_screenshot(browser)
    browser.quit()
