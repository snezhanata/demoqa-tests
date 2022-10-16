from datetime import datetime

import allure
from allure_commons.types import Severity
from selene import have, be
from selene.support.shared import browser

from demoqa_tests.model import app
from demoqa_tests.model.controls.datepicker import DatePicker
from demoqa_tests.utils import attachments
from tests.test_data.users import user, Gender, Hobby


def test_submit_student_registration_form():

    app.registration_form.open()
    browser.should(have.title('ToolsQA'))

    (
        app.registration_form.open()
        .set_name(user.first_name, user.last_name)
        .set_contacts(user.email, user.mobile_number)
        .select_gender(user.gender.value)
        .fill_date(datetime.date(2000, 8, 30))
        .set_subject(user.subjects)
        .select_hobby(user.hobbies)
        .select_picture(user.picture_file)
        .set_address(user.current_address)
        .select_state(user.state)
        .select_city(user.city)
        .submit()
    )
    browser.element('#example-modal-sizes-title-lg').should(be.visible)
    app.submission_form.should_have_table(
        ('Student Name', f'{user.first_name} {user.last_name}'),
        ('Student Email', user.email),
        ('Gender', user.gender.value),
        # ('Gender', user.gender.name),
        ('Mobile', user.mobile_number),
        ('Date of Birth', f'{user.birth_day} {user.birth_month},{user.birth_year}'),
        ('Subjects', ', '.join([subject.value for subject in user.subjects])),
        ('Hobbies', ', '.join([hobby.name for hobby in user.hobbies])),
        ('Picture', user.picture_file),
        ('Address', user.current_address),
        ('State and City', f'{user.state} {user.city}'),
    )

    # Что скрывает Python:
    # birthday = object.__new__()
    # DatePicker.__init__(birthday)
    # DatePicker.typing(birthday, datetime.date(2000, 8, 30))
    # DatePicker.assert_value(birthday, datetime.date(2000, 8, 30))

    '''
        # Steps Object:
        app.registration_form.register(
            first_name='Nyan',
            last_name='Cat',
            email='nyan.cat@gmail.com',
            mobile_number='0123401234',
        )
        '''
    '''
        registration_form.fill_gender(Gender.Female)
        '''
    '''
        app.registration_form.set_date(datetime.date(2000, 8, 30))
        app.registration_form.assert_set_date(datetime.date(2000, 8, 30))        
        app.registration_form.select_date(
            user.birth_day, user.birth_month, user.birth_year
        )
        '''
    '''
        registration_form.fill_subjects('History', 'Maths')
        registration_form.add_subjects_by_autocomplete('#subjectsInput', from_='Hi', to='History')
        registration_form.add_subjects_by_autocomplete('#subjectsInput', from_='Mat', to='Maths')
        '''
    '''
        registration_form.fill_hobbies(Hobby.Music, Hobby.Reading)
        '''
    '''
        registration_form.select_state(user.state)
        '''


# allure.dynamic.tag('blocker')
# allure.dynamic.severity(Severity.BLOCKER)
# allure.dynamic.label('owner', 'Snezhana')
# allure.dynamic.feature('Student Registration Form')
# allure.dynamic.story(
#     'Check the results of submitting  the "Student Registration Form"'
# )
# allure.dynamic.link(
#     'https://demoqa.com/automation-practice-form',
#     name='Link to the "Student Registration Form"',
# )
#
# with allure.step('Open the registration form'):
# with allure.step('Fill in the parameters'):
# with allure.step('Check the results of form submitting'):
# with allure.step('Additional info'):
#     attachments.list_(browser)
