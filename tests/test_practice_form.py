import datetime

import allure
from allure_commons.types import Severity
from selene.support.shared import browser

from demoqa_tests.model import app
from demoqa_tests.utils import attachments

from tests.test_data.users import user, User, Gender, Subject, Hobby

# Steps Object

eren = User(
    first_name='Eren',
    gender=Gender.Male,
    last_name='Yeager',
    email='eren.yeager@gmail.com',
    mobile_number='0123401234',
    birth_date=datetime.date(1993, 5, 19),
    birth_day='19',
    birth_month='May',
    birth_year='1993',
    subjects=(
        Subject.History,
        Subject.Maths,
    ),
    hobbies=(Hobby.Sports, Hobby.Music),
    picture_file='pic_2.png',
    current_address='Shiganshina',
    state='Uttar Pradesh',
    city='Agra',
)


def test_submit_student_registration_form_business_step():
    app.registration_form.enrollment(eren).assert_enrollment(eren)


# Fluent Page Object
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
            # .autocomplete_state('Uttar')
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
        birthday = DatePicker()
        birthday.element = browser.element('#dateOfBirthInput')
        birthday.typing(datetime.date(2000, 8, 30))
        birthday.assert_value(datetime.date(2000, 8, 30))

        # Что под капотом, откуда берется self:
        birthday = object.__new__(DatePicker) # можно и так вызвать: DatePicker.__new__(DatePicker)
        DatePicker.__init__(birthday)
        DatePicker.set_date(birthday, datetime.date(2000, 8, 30))
        DatePicker.assert_value(birthday, datetime.date(2000, 8, 30))
    '''
