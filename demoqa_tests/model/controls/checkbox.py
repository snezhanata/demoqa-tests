from typing import Tuple
from selene import have
import selene

from tests.test_data.users import Hobby


def option(element: selene.Element, values: Tuple[Hobby]):
    for hobby in values:
        element.by(have.value(hobby.value)).first.element('..').click()
