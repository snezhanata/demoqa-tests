from selene import have, command
from selene.support.shared import browser


def select(element, option):
    element.click()
    browser.all('[id^=react-select][id*=-option-]').by(
        have.exact_text(option)
    ).first.click()  # react-select-3-option-2


# def select(element, option, autocomplete: bool = False):
# def autocomplete(selector: str, from_: str, to: str = None):
#     browser.element(selector).click().type(from_)
#     if to is not None:
#         browser.element('#state').element_by(have.text(to)).perform(command.js.click)
#     else:
#         browser.element('#state').element_by(have.text(from_)).perform(command.js.click)
