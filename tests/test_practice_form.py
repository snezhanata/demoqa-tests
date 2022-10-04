from selene import have, command, be
from selene.support.shared import browser

import demoqa_tests.model.pages.registartion_form
import tests.conftest
from demoqa_tests.model import controls
from demoqa_tests.model.pages import registartion_form
from tests.test_data.users import user
from demoqa_tests.utils import path, table


def test_submit_student_registration_form():

    # GIVEN
    registartion_form.given_opened()

    # WHEN
    browser.should(have.title('ToolsQA'))
    browser.element('#firstName').type(user.name)
    browser.element('#lastName').type(user.last_name)
    browser.element('#userEmail').type(user.email)
    browser.all('[for^=gender-radio]').by(
        have.exact_text(user.gender.value)
    ).first.click()
    browser.element('#userNumber').type(user.mobile_number)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys(user.birth_month)
    browser.element('.react-datepicker__year-select').send_keys(user.birth_year)
    browser.element(
        f'.react-datepicker__day--0{user.birth_day}'
        f':not(.react-datepicker__day--outside-month)'
    ).click()
    registartion_form.add_subjects(user.subjects)
    registartion_form.add_hobbies(user.hobbies)
    browser.element('#uploadPicture').send_keys(path.to_resource(user.picture_file))
    browser.element('#currentAddress').type(user.current_address)
    state = browser.element('#state')
    state.perform(command.js.scroll_into_view)
    controls.dropdown.select(state, user.state)
    city = browser.element('#city')
    controls.dropdown.select(city, user.city)
    browser.element('#submit').perform(command.js.click)

    # THEN
    browser.element('#example-modal-sizes-title-lg').should(be.visible)
    table.should_have_view(
        ('Student Name', f'{user.name} {user.last_name}'),
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

