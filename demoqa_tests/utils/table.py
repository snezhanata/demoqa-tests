from selene import have
from selene.support.shared import browser

from demoqa_tests.utils import common


def should_have_view(*data):
    dialog = browser.element('.modal-content')
    rows = dialog.all('tbody tr')
    rows.all('td').should(
        have.exact_texts(*common.flatten(data))
    )  # вторая * распаковывает изнутри и передает значения