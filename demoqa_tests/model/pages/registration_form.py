import datetime
from typing import Tuple
from selene import have, command
from selene.support.shared import browser

from demoqa_tests import utils

from demoqa_tests.model.controls import dropdown, radio_button, checkbox
from demoqa_tests.model import google
from demoqa_tests.model.controls.datepicker import DatePicker
from demoqa_tests.model.pages.submission_form import SubmissionForm
from demoqa_tests.utils import path
from tests.test_data.users import Subject, Hobby


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

    def fill_contacts(self, email: str, mobile: int):
        browser.element('#userEmail').type(email)
        browser.element('#userNumber').type(mobile)
        return self

    def fill_name(self, first_name: str, last_name: str):
        browser.element('#firstName').type(first_name)
        browser.element('#lastName').type(last_name)
        return self

    def fill_date(self, value: datetime.date):
        self.birthday.set_date(value)
        return self

    def assert_fill_date(self, value: datetime.date):
        # self.birthday.should(match.date(value))  # проверка по Мартину Фаулеру
        self.birthday.assert_value(value)  # проверка НЕ по Мартину Фаулеру
        return self

    def select_date(self, day: int, month: str, year: int):
        self.birthday.calendar(day, month, year)
        return self

    def fill_subjects(self, values: Tuple[Subject]):
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
        checkbox.option(browser.all('[id^=hobbies]'), values)
        return self

    def select_picture(self, file_name):
        browser.element('#uploadPicture').send_keys(path.to_resource(file_name))
        return self

    def fill_address(self, value: str):
        browser.element('#currentAddress').type(value)
        return self

    def select_state(self, value: str):
        utils.browser.scroll_to_view(self.state_selector)
        # utils.browser.scroll_one_page()
        dropdown.select(self.state_selector, value)
        return self

    def select_city(self, value: str):
        dropdown.select(self.city_selector, value)
        return self

    def submit(self):
        browser.element('#submit').perform(command.js.click)
        return self

    def fill_in(self, user):
        (
            self.fill_name(user.first_name, user.last_name)
            .fill_contacts(user.email, user.mobile_number)
            .select_gender(user.gender.value)
            .fill_date(user.birth_date)
            # .select_date(user.birth_day, user.birth_month, user.birth_year)
            .fill_subjects(user.subjects)
            # .add_subjects_by_autocomplete('#subjectsInput', from_='Hi', to='History')
            # .add_subjects_by_autocomplete('#subjectsInput', from_='Mat', to='Maths')
            .select_hobbies(user.hobbies)
            .select_picture(user.picture_file)
            .fill_address(user.current_address)
            .select_state(user.state)
            .select_city(user.city)
            .submit()
        )
        return self

    def check_results(self, user):
        submition_form = SubmissionForm()
        submition_form.should_have_table(
            ('Student Name', f'{user.first_name} {user.last_name}'),
            ('Student Email', user.email),
            ('Gender', user.gender.value),
            ('Mobile', user.mobile_number),
            (
                'Date of Birth',
                f'{user.birth_day} {user.birth_month},{user.birth_year}',
            ),
            ('Subjects', ', '.join([subject.value for subject in user.subjects])),
            ('Hobbies', ', '.join([hobby.name for hobby in user.hobbies])),
            ('Picture', user.picture_file),
            ('Address', user.current_address),
            ('State and City', f'{user.state} {user.city}'),
        )
        return self
