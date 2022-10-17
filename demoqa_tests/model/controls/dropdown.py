import selene
from selene import have, command
from selene.support.shared import browser


class Dropdown:
    def __init__(self, element: selene.Element):
        self.element = element

    def scroll_to_view(self):
        self.element.perform(command.js.scroll_into_view)
        return self

    def select(self, option):
        self.element.click()
        browser.all('[id^=react-select][id*=-option-]').by(
            have.exact_text(option)
        ).first.click()  # react-select-3-option-2
        return self
