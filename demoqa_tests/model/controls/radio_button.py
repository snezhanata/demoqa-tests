import selene
from selene import have
from selene.support.shared import browser

from tests.test_data.users import user, Gender


class RadioButton:
    def __init__(self, element: selene.Element):
        self.element = element

    def option(self, value: str):
        self.element.by(have.exact_text(value)).first.click()  # noqa

    # def set_option(label_prefix: str, number: int):
    #     browser.element(f'[for={label_prefix}-radio-{number}]').click()
