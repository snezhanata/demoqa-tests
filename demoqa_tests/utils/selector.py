from selene import have, command
from selene.support.shared import browser


def autocomplete(selector: str, /, *, from_: str, to: str = None):
    browser.element(selector).type(from_)
    if to is not None:
        browser.all('.subjects-auto-complete__option').element_by(
            have.text(to)
        ).perform(command.js.click)
    else:
        browser.all('.subjects-auto-complete__option').element_by(
            have.text(from_)
        ).perform(command.js.click)


'''
OR
def autocomplete(selector: str, /, *, from_: str, to: str = None):
    browser.element(selector).type(from_)
    browser.all('.subjects-auto-complete__option').element_by(have.exact_text(
        to if to is not None else from_
    )).perform(command.js.click)

OR
def autocomplete(selector: str, /, *, from_: str, to: str = None):
    browser.element(selector).type(from_)
    browser.all('.subjects-auto-complete__option').element_by(have.exact_text(
        to or from_
    )).perform(command.js.click)

OR
def autocomplete(selector: str, /, *, from_: str, to: str = None):
    browser.element(selector).type(from_)
    browser.all('.subjects-auto-complete__option').element_by(have.exact_text(
        to if to else from_
    )).perform(command.js.click)

'''
