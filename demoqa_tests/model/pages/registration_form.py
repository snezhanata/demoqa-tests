from typing import Tuple

from selene import have, command
from selene.support.shared import browser

from demoqa_tests.model.controls import dropdown
from demoqa_tests.utils import path
from tests.test_data.users import Subject, Hobby, user

state_selector = browser.element('#state')
city_selector = browser.element('#city')


def select_gender(value:str):
    browser.all('[for^=gender-radio]').by(
        have.exact_text(value)
    ).first.click()


def fill_contact_info(email: str, mobile: int):
    browser.element('#userEmail').type(email)
    browser.element('#userNumber').type(mobile)


def fill_full_name(first_name: str, last_name: str):
    browser.element('#firstName').type(first_name)
    browser.element('#lastName').type(last_name)


def fill_date(value: str):
    browser.element('#dateOfBirthInput').perform(command.js.set_value(value))


def select_date(day, month: str, year):
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys(month)
    browser.element('.react-datepicker__year-select').send_keys(year)
    browser.element(
        f'.react-datepicker__day--0{day}'
        f':not(.react-datepicker__day--outside-month)'
    ).click()


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
        browser.all('[id^=hobbies]').by(have.value(hobby.value)).first.element('..').click()


def given_opened():
    browser.open('/automation-practice-form')
    ads = browser.all('[id^=google_ads_][id$=container__],[id$=Advertisement]')
    ads.with_(timeout=10).should(have.size_greater_than_or_equal(3)).perform(
        command.js.remove
    )
    if ads.with_(timeout=2).wait_until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)


def fill_address(value: str):
    browser.element('#currentAddress').type(value)


def fill_state(value: str):
    dropdown.select(state_selector, value)


def fill_city(value: str):
    dropdown.select(city_selector, value)


def submit_form():
    browser.element('#submit').perform(command.js.click)


def upload_file(file_name):
    browser.element('#uploadPicture').send_keys(path.to_resource(user.picture_file))


def scroll_to_bottom():
    state_selector.perform(command.js.scroll_into_view)


