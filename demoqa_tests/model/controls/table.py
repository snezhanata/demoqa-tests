import selene
from selene.support.shared import browser


def rows(*, inside: selene.Browser | selene.Element = browser):
    # если не пропишем, то будет просто на странице искать, по-умолчанию browser,
    # а если селен элемент передадим, то оно будет внутри селен элемента искаться
    return inside.all('tbody tr')
