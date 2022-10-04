# radio buttons, dropdown lists and so on
from selene import have, command
from selene.support.shared import browser


def select(element, option):
    element.click()
    browser.all('[id^=react-select][id*=-option-]').by(
        have.exact_text(option)
    ).first.click()  # react-select-3-option-2