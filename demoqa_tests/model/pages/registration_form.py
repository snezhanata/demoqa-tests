import datetime
from typing import Tuple
from selene import have, command
from selene.support.shared import browser

from demoqa_tests import utils
from demoqa_tests.model.controls import dropdown, datepicker, radio_button, checkbox
from demoqa_tests.model import google
from demoqa_tests.model.controls.datepicker import DatePicker
from demoqa_tests.utils import path
from demoqa_tests.utils.selene.conditions import match
from tests.test_data.users import Subject, Hobby, user, Gender


class RegistrationForm:
    def __init__(self):
        self.state_selector = browser.element('#state')
        self.city_selector = browser.element('#city')
        self.birthday = DatePicker(browser.element('#dateOfBirthInput'))

    def open(self):
        browser.open('/automation-practice-form')
        google.ads_remove(amount=4, timeout=5)
        return self

    def select_gender(self, value: str):
        radio_button.option(browser.all('[for^=gender-radio]'), value)
        return self

    # def fill_gender(value: Gender):
    #     radio_button.set_option('gender', value.value)  # noqa

    def set_contacts(self, email: str, mobile: int):
        browser.element('#userEmail').type(email)
        browser.element('#userNumber').type(mobile)
        return self

    def set_name(self, first_name: str, last_name: str):
        browser.element('#firstName').type(first_name)
        browser.element('#lastName').type(last_name)
        return self

    def fill_date(self, value: datetime.date):
        self.birthday.set_date(value)
        return self

    def assert_fill_date(self, value: datetime.date):
        self.birthday.should(match.date(value))  # проверка по Мартину Фаулеру
        # datepicker.assert_value(birthday_selector, value) # проверка НЕ по Мартину Фаулеру
        return self

    def select_date(self, day: int, month: str, year: int):
        self.birthday.calendar(day, month, year)
        return self

    def set_subject(self, values: Tuple[Subject]):
        for subject in values:
            browser.element('#subjectsInput').type(subject.value).press_enter()

        return self

    '''
    def fill_subjects(*subjects: str):
        for item in subjects:
            browser.element('#subjectsInput').type(item).press_enter()
    '''

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

    def select_hobby(self, values: Tuple[Hobby]):
        checkbox.option(browser.all('[id^=hobbies]'), values)
        return self

    '''
    def fill_hobbies(*options: Hobby):
        checkbox.check_options(
            browser.all('[for^=hobbies-checkbox]'),
            *[option.value for option in options]
            # checkbox.check_options(
            #     browser.all('[for^=hobbies-checkbox]'), *map(lambda option: option.value, options)
        )
    '''

    def set_address(self, value: str):
        browser.element('#currentAddress').type(value)
        return self

    # допиши автокомплит
    def select_state(self, value: str):
        utils.browser.scroll_to_view(self.state_selector)
        # utils.browser.scroll_one_page()
        dropdown.select(self.state_selector, value)
        return self

    # допиши автокомплит
    def select_city(self, value: str):
        dropdown.select(self.city_selector, value)
        return self

    def submit(self):
        browser.element('#submit').perform(command.js.click)
        return self

    def select_picture(self, file_name):
        browser.element('#uploadPicture').send_keys(path.to_resource(user.picture_file))
        return self
