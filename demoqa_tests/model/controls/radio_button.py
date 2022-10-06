from selene import have
from selene.support.shared import browser

from tests.test_data.users import user, Gender


def option(value: str):
    browser.all('[for^=gender-radio]').by(have.exact_text(value)).first.click()
