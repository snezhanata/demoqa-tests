import allure
from allure_commons.types import Severity
from selene.support.shared import browser

from demoqa_tests.model import app
from demoqa_tests.utils import attachments

from tests.test_data import users


# Steps Object
def test_student_registration():
    allure.dynamic.tag('blocker')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.label('owner', 'Snezhana')
    allure.dynamic.feature('Student Registration Form')
    allure.dynamic.story(
        'Check the results of submitting the "Student Registration Form"'
    )
    allure.dynamic.link(
        'https://demoqa.com/automation-practice-form',
        name='Link to the "Student Registration Form"',
    )

    with allure.step('Check student registration operation'):
        (
            app.sign_up.open_registration_form()
            .registered(users.student_2)
            .should_be_registered(users.student_2)
        )

    with allure.step('Additional info'):
        attachments.list_(browser)


# Fluent Page Object
def test_submit_student_registration_form():

    allure.dynamic.tag('blocker')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.label('owner', 'Snezhana')
    allure.dynamic.feature('Student Registration Form')
    allure.dynamic.story(
        'Check the "Student Registration Form" opening, fill in data and results of submitting'
    )
    allure.dynamic.link(
        'https://demoqa.com/automation-practice-form',
        name='Link to the "Student Registration Form"',
    )

    with allure.step('Open the registration form'):
        app.registration_form.open()

    with allure.step('Fill in the parameters'):
        (
            app.registration_form.fill_name(
                users.student_1.first_name, users.student_1.last_name
            )
            .fill_contacts(users.student_1.email, users.student_1.mobile_number)
            .select_gender(users.student_1.gender.value)
            .fill_date(users.student_1.birth_date)
            # .select_date(user.birth_day, user.birth_month, user.birth_year)
            .fill_subjects(users.student_1.subjects)
            # .add_subjects_by_autocomplete('#subjectsInput', from_='Hi', to='History')
            # .add_subjects_by_autocomplete('#subjectsInput', from_='Mat', to='Maths')
            .select_hobbies(users.student_1.hobbies)
            .select_picture(users.student_1.picture_file)
            .fill_address(users.student_1.current_address)
            .select_state(users.student_1.state)
            # .autocomplete_state('Uttar')
            .select_city(users.student_1.city)
            .submit()
        )

    with allure.step('Check the results of form submitting'):
        app.submission_form.should_have_table(
            (
                'Student Name',
                f'{users.student_1.first_name} {users.student_1.last_name}',
            ),
            ('Student Email', users.student_1.email),
            ('Gender', users.student_1.gender.value),
            ('Mobile', users.student_1.mobile_number),
            (
                'Date of Birth',
                f'{users.student_1.birth_day} {users.student_1.birth_month},{users.student_1.birth_year}',
            ),
            (
                'Subjects',
                ', '.join([subject.value for subject in users.student_1.subjects]),
            ),
            ('Hobbies', ', '.join([hobby.name for hobby in users.student_1.hobbies])),
            ('Picture', users.student_1.picture_file),
            ('Address', users.student_1.current_address),
            ('State and City', f'{users.student_1.state} {users.student_1.city}'),
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
