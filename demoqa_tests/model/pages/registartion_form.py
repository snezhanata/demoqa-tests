from typing import Tuple

from selene import have, command
from selene.support.shared import browser

from tests.test_data.users import Subject, Hobby


def subject_values(values: Tuple[Subject]):
    for subject in values:
        browser.element('#subjectsInput').type(subject.value).press_enter()


def hobby_values(values: Tuple[Hobby]):
    for hobby in values:
        browser.all('[id^=hobbies]').by(have.value(hobby.value)).first.element('..').click()


def given_opened_practice_form():
    browser.open('/automation-practice-form')
    ads = browser.all('[id^=google_ads_][id$=container__],[id$=Advertisement]')
    ads.with_(timeout=10).should(have.size_greater_than_or_equal(3)).perform(
        command.js.remove
    )
    if ads.with_(timeout=2).wait_until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)