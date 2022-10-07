import datetime

from selene import have

from tests.test_data import users


def date(value: datetime.date):
    return have.value(users.format_date)
