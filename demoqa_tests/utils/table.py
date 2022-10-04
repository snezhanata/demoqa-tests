from selene import have
from selene.support.shared import browser

from demoqa_tests.utils import common


def should_have_view(*data):
    dialog = browser.element('.modal-content')
    rows = dialog.all('tbody tr')
    rows.all('td').should(
        have.exact_texts(*common.flatten(data))
    )  # вторая * распаковывает изнутри и передает значения


'''
OR
def should_have_view(*data):
    dialog = browser.element('.modal-content')
    rows = dialog.all('tbody tr')
    for index, (name, value) in enumerate(data):
        row_cells = rows[index].all('td')
        row_cells[0].should(have.exact_text(name))
        row_cells[1].should(have.exact_text(value))

OR
def should_have_view(*data):
    dialog = browser.element('.modal-content')
    rows = dialog.all('tbody tr')
    for name, value in data:
        rows.by(have.text(name)).first.all('td')[1].should(have.exact_text(value))

OR
def should_have_view(*data):
    dialog = browser.element('.modal-content')
    rows = dialog.all('tbody tr')
    for name, value in data:
        rows.all('td').element_by(have.exact_text(name)).element('./following-sibling::td').should(have.exact_text(value))

OR
def should_have_view(*data):
    dialog = browser.element('.modal-content')
    rows = dialog.all('tbody tr')
    values = [value for row in data for value in row[1::2]]
    rows.all('td').even.should(have.exact_texts(*values))
    #same but more self-documented:
    even = slice(1, None, 2)
    values = [value for row in data for value in row[even]]
    rows.all('td').even.should(have.exact_texts(*values))

'''


def cells_of_row_should_have_texts(index, *texts):
    browser.element('.modal-dialog').all('table tr')[index].all('td')[1].should(
        have.exact_texts(*texts)
    )
