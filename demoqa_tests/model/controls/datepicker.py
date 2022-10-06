import datetime

from selene import command
from selene.support.shared import browser

from demoqa_tests import config
from demoqa_tests.model.pages.registration_form import key


def set_date_by_key(value: str):
    browser.element('#dateOfBirthInput').send_keys(key, 'a').type(value).press_enter()


def set_date_by_js_1(value: str):
    browser.element('#dateOfBirthInput').with_(set_value_by_js=True).set_value(value)


def set_date_by_js_2(value: str):
    browser.element('#dateOfBirthInput').perform(command.js.set_value(value))


def set_date_by_js_3(value: datetime.date):
    browser.element('#dateOfBirthInput').perform(
        command.js.set_value(value.strftime(config.datetime_format))
    )


def select_date(day, month: str, years):
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys(month)
    browser.element('.react-datepicker__year-select').send_keys(year)
    browser.element(
        f'.react-datepicker__day--0{day}' f':not(.react-datepicker__day--outside-month)'
    ).click()
