import datetime
import sys

import selene
from selene import command
from selene.support.shared import browser
from selenium.webdriver import Keys

from demoqa_tests import config
from demoqa_tests.utils.selene.conditions import match
from tests.test_data import users


def typing(element: selene.Element, value: datetime.date):
    key = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
    element.send_keys(key, 'a').type(users.format_date(value)).press_enter()


# # проверка по Мартину Фаулеру, мы создали свой метод "match.date" (match аналог have)
# def assert_value(element: selene.Element, value: datetime.date):
#     element.should(match.date(value))


'''
OR
def set_date_by_js_with(element: selene.Element, value: str):
    element.with_(set_value_by_js=True).set_value(value)


def set_date_by_js_perform(element: selene.Element, value: str):
    element.perform(command.js.set_value(value))
'''


def calendar(
    element: selene.Element,
    element_month: selene.Element,
    element_year: selene.Element,
    element_day: selene.Element,
    month: str,
    year: int,
):
    element.click()
    element_month.send_keys(month)
    element_year.send_keys(year)
    element_day.click()
