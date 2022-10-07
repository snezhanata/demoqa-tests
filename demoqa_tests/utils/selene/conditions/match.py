import datetime

from selene import have

from tests.test_data import users

# По Мартину Фаулеру мы вынесли проверку даты в созданный нами кастомный кондишен "match.date" (match аналог have).


def date(value: datetime.date):
    return have.value(users.format_date)
