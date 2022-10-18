import selene
from selene import have
from selene.support.shared import browser

from tests.test_data.users import student_1, Gender


class RadioButton:
    def __init__(self, element: selene.Element):
        self.element = element

    def option(
        self, value: Gender
    ):  # type hint о том, что нельзя передавать что угодно, а только Gender
        self.element.by(have.exact_text(value)).first.click()  # noqa

    # def set_option(label_prefix: str, number: int):
    #     browser.element(f'[for={label_prefix}-radio-{number}]').click()
