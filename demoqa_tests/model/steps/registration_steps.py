from selene.support.shared import browser

from demoqa_tests.model import google
from demoqa_tests.model.pages.registration_form import RegistrationForm
from demoqa_tests.model.pages.submission_form import SubmissionForm
from tests.test_data.users import User


class RegistrationSteps:
    def __init__(self):
        self.registration_form = RegistrationForm()
        self.submission_form = SubmissionForm()

    def open_registration_form(self):
        self.registration_form.open()
        return self

    def registered(self, user: User):  # User = type hint
        (
            self.registration_form.fill_name(user.first_name, user.last_name)
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

    def should_be_registered(self, user):
        self.submission_form.should_have_table(
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
