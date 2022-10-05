from selene import have

from demoqa_tests.model.controls import dialog
from demoqa_tests.utils import common


def should_have_table(*data):
    rows = dialog.content.all('tbody tr')
    rows.all('td').should(
        have.exact_texts(*common.flatten(data))
    )
