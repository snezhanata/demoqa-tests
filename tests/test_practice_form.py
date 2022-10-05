from selene import have, command, be
from selene.support.shared import browser

from demoqa_tests.model.pages import submission_form
from demoqa_tests.model.pages import registration_form
from demoqa_tests.utils import path

from tests.test_data.users import user


def test_submit_student_registration_form():

    # GIVEN
    registration_form.given_opened()
    # THEN
    browser.should(have.title('ToolsQA'))  # т.к. assertions не должны быть внутри Page Objects, поэтому не стала выносить
    # WHEN
    registration_form.fill_full_name(user.first_name, user.last_name)
    registration_form.select_date(user.birth_day, user.birth_month, user.birth_year) # вариант с выбором даты в календаре
    # registration_form.fill_date('30 Aug 2000') # вариант с простановкой даты
    registration_form.select_gender(user.gender.value)
    registration_form.fill_contact_info(user.email, user.mobile_number)


    registration_form.add_subjects_by_option(user.subjects)
    # Вопрос: Подскажите, как здесь можно избежать повтора кода?
    # registration_form.add_subjects_by_autocomplete('#subjectsInput', from_='Hi', to='History')
    # registration_form.add_subjects_by_autocomplete('#subjectsInput', from_='Mat', to='Maths')

    registration_form.add_hobbies(user.hobbies)
    registration_form.upload_file(user.picture_file)
    registration_form.fill_address(user.current_address)
    registration_form.scroll_to_bottom()
    registration_form.fill_state(user.state)
    registration_form.fill_city(user.city)
    registration_form.submit_form()

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

