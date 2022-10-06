from selene import have
from selene.support.shared import browser

from tests.test_data.users import user


def radio_button(value: str):
    browser.all('[for^=gender-radio]').by(have.exact_text(value)).first.click()
