from typing import Tuple

from selene import have, command
from selene.support.shared import browser

from demoqa_tests.model.controls import dropdown
from tests.test_data.users import Subject, Hobby


state_selector = browser.element('#state')
city_selector = browser.element('#city')


def add_subjects(values: Tuple[Subject]):
    for subject in values:
        browser.element('#subjectsInput').type(subject.value).press_enter()


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


def set_state(value: str):
    dropdown.select(state_selector, value)


def set_city(value: str):
    dropdown.select(city_selector, value)


def scroll_to_bottom():
    state_selector.perform(command.js.scroll_into_view)


