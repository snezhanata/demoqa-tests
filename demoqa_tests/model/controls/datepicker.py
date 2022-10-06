import datetime
import sys

from selene import command
from selene.support.shared import browser
from selenium.webdriver import Keys

from demoqa_tests import config


key = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL


def set_date_by_key(value: datetime.date):
    browser.element('#dateOfBirthInput').send_keys(key, 'a').type(
        value.strftime(config.datetime_format)
    ).press_enter()


def set_date_by_js_1(value: str):
    browser.element('#dateOfBirthInput').with_(set_value_by_js=True).set_value(value)


def set_date_by_js_2(value: str):
    browser.element('#dateOfBirthInput').perform(command.js.set_value(value))


def select_date(day, month: str, year):
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys(month)
    browser.element('.react-datepicker__year-select').send_keys(year)
    browser.element(
        f'.react-datepicker__day--0{day}' f':not(.react-datepicker__day--outside-month)'
    ).click()
