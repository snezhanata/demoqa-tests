import datetime
import sys

import selene
from selene.support.shared import browser
from selenium.webdriver import Keys

from tests.test_data import users


def typing(element: selene.Element, value: datetime.date):
    key = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
    element.send_keys(key, 'a').type(users.format_date(value)).press_enter()


# Проверка по Мартину Фаулеру
# def assert_value(element: selene.Element, value: datetime.date):
#     element.should(match.date(value))

# проверка НЕ по Мартину Фаулеру
# def assert_value(element:selene.Element, date: datetime.date):
#     element.should(have.value(users.format_date(date)))

'''
OR
def typing_by_js_with(element: selene.Element, value: str):
    element.with_(set_value_by_js=True).set_value(value)


def set_date_by_js_perform(element: selene.Element, value: str):
    element.perform(command.js.set_value(value))
'''


def calendar(
    element: selene.Element,
    day: int,
    month: str,
    year: int,
):
    element.click()
    browser.element('.react-datepicker__month-select').send_keys(month)
    browser.element('.react-datepicker__year-select').send_keys(year)
    browser.element(
        f'.react-datepicker__day--0{day}' f':not(.react-datepicker__day--outside-month)'
    ).click()
