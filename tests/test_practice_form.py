import datetime

import allure
from allure_commons.types import Severity
from selene.support.shared import browser

from demoqa_tests.model import app
from demoqa_tests.utils import attachments
from tests.test_data.users import user


def test_submit_student_registration_form():

    allure.dynamic.tag('blocker')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.label('owner', 'Snezhana')
    allure.dynamic.feature('Student Registration Form')
    allure.dynamic.story(
        'Check the results of submitting  the "Student Registration Form"'
    )
    allure.dynamic.link(
        'https://demoqa.com/automation-practice-form',
        name='Link to the "Student Registration Form"',
    )

    with allure.step('Open the registration form'):
        app.registration_form.open()

    with allure.step('Fill in the parameters'):
        (
            app.registration_form.fill_name(user.first_name, user.last_name)
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

    with allure.step('Check the results of form submitting'):
        app.submission_form.should_have_table(
            ('Student Name', f'{user.first_name} {user.last_name}'),
            ('Student Email', user.email),
            ('Gender', user.gender.value),
            ('Mobile', user.mobile_number),
            ('Date of Birth', f'{user.birth_day} {user.birth_month},{user.birth_year}'),
            ('Subjects', ', '.join([subject.value for subject in user.subjects])),
            ('Hobbies', ', '.join([hobby.name for hobby in user.hobbies])),
            ('Picture', user.picture_file),
            ('Address', user.current_address),
            ('State and City', f'{user.state} {user.city}'),
        )

    with allure.step('Additional info'):
        attachments.list_(browser)

    '''    
        # Steps Object:
        app.registration_form.register(
            first_name='Nyan',
            last_name='Cat',
            email='nyan.cat@gmail.com',
            mobile_number='0123401234',
        )
        birthday = DatePicker()
        birthday.element = browser.element('#dateOfBirthInput')
        birthday.typing(datetime.date(2000, 8, 30))
        birthday.assert_value(datetime.date(2000, 8, 30))
        
        # Как обрабатывает внутри Python:
        birthday = object.__new__()
        DatePicker.__init__(birthday)
        DatePicker.typing(birthday, datetime.date(2000, 8, 30))
        DatePicker.assert_value(birthday, datetime.date(2000, 8, 30))
    '''
