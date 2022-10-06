from selene import command
from selene.core.wait import Command
from selene.support.shared import browser

from demoqa_tests.model.pages.registration_form import state_selector
from demoqa_tests.utils.selene import command_ext


def scroll_to_view():
    state_selector.perform(command.js.scroll_into_view)


def scroll_one_page():
    browser.perform(command_ext.js.scroll_one_page)
