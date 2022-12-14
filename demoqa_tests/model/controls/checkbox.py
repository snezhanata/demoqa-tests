from typing import Tuple
from selene import have
import selene

from tests.test_data.users import Hobby


class Checkbox:
    def __init__(self, element: selene.Element):
        self.element = element

    def option(self, values: Tuple[Hobby]):
        for hobby in values:
            self.element.by(have.value(hobby.value)).first.element('..').click()  # noqa


# def check_options(elements, *options: str):
#     for option in options:
#         elements.by(have.exact_text(option)).first.element('..').click()
