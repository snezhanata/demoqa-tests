import selene
from selene import have, command
from selene.support.shared import browser


class Dropdown:  # можно без класса обойтись, как микроскопом гвозди забивать
    def __init__(self, element: selene.Element):
        self.element = element
        self.input = element.element('[id^=react-select][id$=-input]')
        self.options = browser.all('[id^=react-select][id*=-option-]')

    def scroll_to_view(self):
        self.element.perform(command.js.scroll_into_view)
        return self

    def option(self, text: str):
        return self.options.by(have.exact_text(text)).first

    def open(self):
        self.element.click()
        return self

    def choose(self, option: str):
        self.option(option).click()
        return self

    def select(self, option: str):
        return self.open().choose(option)

    # Равносильно записи optin + open + choose + select:
    # def select(self, option:str):
    #     self.element.click()
    #     self.options.by(have.exact_text(option)).first.click()  # react-select-3-option-2
    #     return self

    def autocomplete(self, option_text: str):
        self.input.type(option_text).press_enter()
        return self
