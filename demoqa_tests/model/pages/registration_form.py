import datetime
from typing import Tuple

from selene import have, command
from selene.support.shared import browser

from demoqa_tests import utils
from demoqa_tests.model.controls import dropdown, datepicker, radio_button, checkbox
from demoqa_tests.utils import path
from demoqa_tests.utils.selene.conditions import match
from tests.test_data.users import Subject, Hobby, user, Gender

state_selector = browser.element('#state')
city_selector = browser.element('#city')
birthday_selector = browser.element('#dateOfBirthInput')


def select_gender(value: str):
    radio_button.option(browser.all('[for^=gender-radio]'), value)


# def fill_gender(value: Gender):
#     radio_button.set_option('gender', value.value)  # noqa


def set_contact_info(email: str, mobile: int):
    browser.element('#userEmail').type(email)
    browser.element('#userNumber').type(mobile)


def set_name(first_name: str, last_name: str):
    browser.element('#firstName').type(first_name)
    browser.element('#lastName').type(last_name)


def set_date(value: datetime.date):
    datepicker.typing(birthday_selector, value)


def assert_set_date(value: datetime.date):
    birthday_selector.should(match.date(value))  # проверка по Мартину Фаулеру
    # datepicker.assert_value(birthday_selector, value) # проверка НЕ по Мартину Фаулеру


def select_date(day: int, month: str, year: int):
    datepicker.calendar(birthday_selector, day, month, year)


def set_subject(values: Tuple[Subject]):
    for subject in values:
        browser.element('#subjectsInput').type(subject.value).press_enter()


def autocomplete_subject(selector: str, /, *, from_: str, to: str = None):
    browser.element(selector).type(from_)
    if to is not None:
        browser.all('.subjects-auto-complete__option').element_by(
            have.text(to)
        ).perform(command.js.click)
    else:
        browser.all('.subjects-auto-complete__option').element_by(
            have.text(from_)
        ).perform(command.js.click)


def select_hobby(values: Tuple[Hobby]):
    checkbox.option(browser.all('[id^=hobbies]'), values)


# def fill_hobbies(*options: Hobby):
#     checkbox.check_options(
#         browser.all('[for^=hobbies-checkbox]'), *[option.value for option in options]
#     )


def given_opened():
    browser.open('/automation-practice-form')
    ads = browser.all('[id^=google_ads_][id$=container__],[id$=Advertisement]')
    ads.with_(timeout=10).should(have.size_greater_than_or_equal(4)).perform(
        command.js.remove
    )
    if ads.with_(timeout=2).wait_until(have.size_less_than_or_equal(4)):
        ads.perform(command.js.remove)


def set_address(value: str):
    browser.element('#currentAddress').type(value)


def select_state(value: str):
    utils.browser.scroll_to_view(state_selector)
    # utils.browser.scroll_one_page()
    dropdown.select(state_selector, value)


def select_city(value: str):
    dropdown.select(city_selector, value)


def submit():
    browser.element('#submit').perform(command.js.click)


def upload_file(file_name):
    browser.element('#uploadPicture').send_keys(path.to_resource(user.picture_file))
