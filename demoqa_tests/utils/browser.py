from selene import command

from demoqa_tests.model.pages.registration_form import state_selector


def scroll_to_view():
    state_selector.perform(command.js.scroll_into_view)


def scroll_one_page():
    state_selector.perform(command.js.scroll_into_view)