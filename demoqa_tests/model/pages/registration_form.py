import datetime
from typing import Tuple

from selene import have, command
from selene.support.shared import browser

from demoqa_tests import utils
from demoqa_tests.model.controls import dropdown, datepicker, radio_button
from demoqa_tests.utils import path
from tests.test_data.users import Subject, Hobby, user, Gender

state_selector = browser.element('#state')
city_selector = browser.element('#city')
birthday_selector = browser.element('#dateOfBirthInput')


def select_gender(value: str):
    radio_button.option(value)


def fill_contact_info(email: str, mobile: int):
    browser.element('#userEmail').type(email)
    browser.element('#userNumber').type(mobile)


def set_name(first_name: str, last_name: str):
    browser.element('#firstName').type(first_name)
    browser.element('#lastName').type(last_name)


def set_date(value: datetime.date):
    datepicker.typing(birthday_selector, value)


def select_date(day: int, month: str, year: int):
    datepicker.calendar(
        birthday_selector,
        browser.element('.react-datepicker__month-select'),
        browser.element('.react-datepicker__year-select'),
        browser.element(
            f'.react-datepicker__day--0{day}'
            f':not(.react-datepicker__day--outside-month)'
        ),
        month,
        year,
    )


def add_subjects_by_option(values: Tuple[Subject]):
    for subject in values:
        browser.element('#subjectsInput').type(subject.value).press_enter()


def add_subjects_by_autocomplete(selector: str, /, *, from_: str, to: str = None):
    browser.element(selector).type(from_)
    if to is not None:
        browser.all('.subjects-auto-complete__option').element_by(
            have.text(to)
        ).perform(command.js.click)
    else:
        browser.all('.subjects-auto-complete__option').element_by(
            have.text(from_)
        ).perform(command.js.click)


def add_hobbies(values: Tuple[Hobby]):
    for hobby in values:
        browser.all('[id^=hobbies]').by(have.value(hobby.value)).first.element(
            '..'
        ).click()


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
