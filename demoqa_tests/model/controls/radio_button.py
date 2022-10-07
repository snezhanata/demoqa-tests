import selene
from selene import have
from selene.support.shared import browser

from tests.test_data.users import user, Gender


def option(element: selene.Element, value: str):
    element.by(have.exact_text(value)).first.click()
