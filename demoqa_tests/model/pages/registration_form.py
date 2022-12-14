import datetime
from typing import Tuple
from selene import have, command
from selene.support.shared import browser

from demoqa_tests.model import google
from demoqa_tests.model.controls.datepicker import DatePicker
from demoqa_tests.model.controls.dropdown import Dropdown
from demoqa_tests.model.controls.checkbox import Checkbox
from demoqa_tests.model.controls.radio_button import RadioButton
from demoqa_tests.utils import path
from tests.test_data.users import Subject, Hobby, Gender


class RegistrationForm:
    def __init__(self):
        # сюда выносим либо вобще все элементы, либо только те, которые повторяются несколько раз
        self.state_selector = Dropdown(browser.element('#state'))
        self.city_selector = Dropdown(browser.element('#city'))
        self.birthday_selector = DatePicker(browser.element('#dateOfBirthInput'))
        self.hobbies_selector = Checkbox(browser.all('[id^=hobbies]'))
        self.gender_selector = RadioButton(browser.all('[for^=gender-radio]'))

    def open(self):
        browser.open('/automation-practice-form')
        google.ads_remove(amount=4, timeout=5)
        return self

    def select_gender(self, value: Gender):
        self.gender_selector.option(value)
        return self

    def fill_contacts(self, email: str, mobile: int):
        browser.element('#userEmail').type(email)
        browser.element('#userNumber').type(mobile)
        return self

    def fill_name(self, first_name: str, last_name: str):
        browser.element('#firstName').type(first_name)
        browser.element('#lastName').type(last_name)
        return self

    def fill_date(self, value: datetime.date):
        self.birthday_selector.set_date(value)
        return self

    def assert_fill_date(self, value: datetime.date):
        # self.birthday.should(match.date(value))  # проверка по Мартину Фаулеру
        self.birthday_selector.assert_value(value)  # проверка НЕ по Мартину Фаулеру
        return self

    def select_date(self, day: int, month: str, year: int):
        self.birthday_selector.calendar(day, month, year)
        return self

    def fill_subjects(self, values: Tuple[Subject]):  # type hint
        for subject in values:
            browser.element('#subjectsInput').type(subject.value).press_enter()
        return self

    def autocomplete_subject(self, selector: str, /, *, from_: str, to: str = None):
        browser.element(selector).type(from_)
        if to is not None:
            browser.all('.subjects-auto-complete__option').element_by(
                have.text(to)
            ).perform(command.js.click)
        else:
            browser.all('.subjects-auto-complete__option').element_by(
                have.text(from_)
            ).perform(command.js.click)
        return self

    def select_hobbies(self, values: Tuple[Hobby]):
        self.hobbies_selector.option(values)
        return self

    def select_picture(self, file_name):
        browser.element('#uploadPicture').send_keys(path.to_resource(file_name))
        return self

    def fill_address(self, value: str):
        browser.element('#currentAddress').type(value)
        return self

    def select_state(self, value: str):
        self.state_selector.scroll_to_view()
        self.state_selector.select(value)
        return self

    def autocomplete_state(self, value: str):
        self.state_selector.scroll_to_view()
        self.state_selector.autocomplete(value)
        return self

    def select_city(self, value: str):
        self.city_selector.select(value)
        return self

    def submit(self):
        browser.element('#submit').perform(command.js.click)
        return self
