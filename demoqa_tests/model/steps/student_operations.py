from selene.support.shared import browser

from demoqa_tests.model import google
from demoqa_tests.model.pages.registration_form import RegistrationForm
from demoqa_tests.model.pages.submission_form import SubmissionForm


class StudentOperations:
    def open(self):
        browser.open('/automation-practice-form')
        google.ads_remove(amount=4, timeout=5)
        return self

    def enrollment(self, user):
        (
            RegistrationForm()
            .fill_name(user.first_name, user.last_name)
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

    def assert_enrollment(self, user):
        SubmissionForm().should_have_table(
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
