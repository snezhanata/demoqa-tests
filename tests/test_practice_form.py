import datetime

from selene import have, be
from selene.support.shared import browser

from demoqa_tests.model.pages import submission_form
from demoqa_tests.model.pages import registration_form
from tests.test_data.users import user, Gender, Hobby


def test_submit_student_registration_form():

    # GIVEN
    registration_form.given_opened()

    # THEN
    browser.should(have.title('ToolsQA'))

    # WHEN
    registration_form.set_name(user.first_name, user.last_name)
    registration_form.set_contact_info(user.email, user.mobile_number)
    registration_form.select_gender(user.gender.value)
    # registration_form.set_date(datetime.date(2000, 8, 30))
    # registration_form.assert_set_date(datetime.date(2000, 8, 30))
    registration_form.select_date(user.birth_day, user.birth_month, user.birth_year)
    registration_form.set_subject(user.subjects)
    # registration_form.add_subjects_by_autocomplete('#subjectsInput', from_='Hi', to='History')
    # registration_form.add_subjects_by_autocomplete('#subjectsInput', from_='Mat', to='Maths')
    registration_form.select_hobby(user.hobbies)
    # registration_form.fill_hobbies(Hobby.Music, Hobby.Reading)
    registration_form.upload_file(user.picture_file)
    registration_form.set_address(user.current_address)
    registration_form.select_state(user.state)
    registration_form.select_city(user.city)
    registration_form.submit()

    # THEN
    browser.element('#example-modal-sizes-title-lg').should(be.visible)
    submission_form.should_have_table(
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
