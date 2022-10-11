import allure
from allure_commons.types import Severity
from selene import have, be
from selene.support.shared import browser

from demoqa_tests.model import app
from demoqa_tests.utils import attach
from tests.test_data.users import user, Gender, Hobby


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
        browser.should(have.title('ToolsQA'))

    with allure.step('Fill in the parameters'):
        app.registration_form.set_name(user.first_name, user.last_name)
        app.registration_form.set_contacts(user.email, user.mobile_number)
        app.registration_form.select_gender(user.gender.value)
        '''
        registration_form.fill_gender(Gender.Female)
        '''
        app.registration_form.select_date(
            user.birth_day, user.birth_month, user.birth_year
        )
        '''
        registration_form.set_date(datetime.date(2000, 8, 30))
        registration_form.assert_set_date(datetime.date(2000, 8, 30))
        '''
        app.registration_form.set_subject(user.subjects)
        '''
        registration_form.fill_subjects('History', 'Maths')
        registration_form.add_subjects_by_autocomplete('#subjectsInput', from_='Hi', to='History')
        registration_form.add_subjects_by_autocomplete('#subjectsInput', from_='Mat', to='Maths')
        '''
        app.registration_form.select_hobby(user.hobbies)
        '''
        registration_form.fill_hobbies(Hobby.Music, Hobby.Reading)
        '''
        app.registration_form.select_picture(user.picture_file)
        app.registration_form.set_address(user.current_address)
        '''
        registration_form.select_state(user.state)
        '''
        app.registration_form.select_state(user.state)
        app.registration_form.select_city(user.city)
        app.registration_form.submit()

    with allure.step('Check the results of form submitting'):
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

    with allure.step('Additional info)'):
        attach.add_html(browser)
        attach.add_screenshot(browser)
        attach.add_logs(browser)
        attach.add_video(browser)
        browser.driver.close()
