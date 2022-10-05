from selene import have, command, be
from selene.support.shared import browser

from demoqa_tests.model.pages import submission_form
from demoqa_tests.model.pages import registration_form
from demoqa_tests.utils import path

from tests.test_data.users import user


def test_submit_student_registration_form():

    # GIVEN
    registration_form.given_opened()

    # WHEN
    browser.should(have.title('ToolsQA')) # не стала выносить в Page Objects, т.к. assertions не должны быть внутри Page Objects

    registration_form.set_full_name(user.first_name, user.last_name)
    registration_form.select_date(user.birth_day, user.birth_month, user.birth_year)
    registration_form.select_gender(user.gender.value)
    registration_form.set_contact_info(user.email, user.mobile_number)
    # Вопрос: Не смогла добиться чтобы заработал второй вариант. Что делаю не так?:
    # registration_form.set_date('30 Aug 2000')

    registration_form.add_subjects_by_option(user.subjects)
    # registration_form.add_subjects_by_autocomplete('#subjectsInput', from_='Hi', to='History')
    # registration_form.add_subjects_by_autocomplete('#subjectsInput', from_='Mat', to='Maths')

    registration_form.add_hobbies(user.hobbies)
    browser.element('#uploadPicture').send_keys(path.to_resource(user.picture_file))
    browser.element('#currentAddress').type(user.current_address)
    registration_form.scroll_to_bottom()
    registration_form.set_state(user.state)
    registration_form.set_city(user.city)
    browser.element('#submit').perform(command.js.click)

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

