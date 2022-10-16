import datetime
import sys

import selene
from selene.support.shared import browser
from selenium.webdriver import Keys

from demoqa_tests.utils.selene.conditions import match
from tests.test_data import users


class DatePicker:
    # formatting = '%d %b %Y'  # поле класса
    def __init__(self, element: selene.Element):
        self.element = element  # поле объекта класса

    def set_date(self, value: datetime.date):  # метод объекта класса
        key = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
        self.element.send_keys(key, 'a').type(
            users.format_input_date(value)
            # date.strftime(DatePicker.formatting)
        ).press_enter()
        return self

    # Проверка по Мартину Фаулеру
    # def assert_value(self, value: datetime.date):
    #     self.element.should(match.date(value))
    #     return self

    # проверка НЕ по Мартину Фаулеру
    def assert_value(self, date: datetime.date):
        self.element.should(match.value(users.format_input_date(date)))

    def calendar(
        self,
        day: int,
        month: str,
        year: int,
    ):
        self.element.click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element(
            f'.react-datepicker__day--0{day}'
            f':not(.react-datepicker__day--outside-month)'
        ).click()
