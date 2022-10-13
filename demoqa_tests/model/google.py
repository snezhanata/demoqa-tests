from selene import command, have
from selene.support.shared import browser

ads = browser.all('[id^=google_ads_][id$=container__],[id$=Advertisement]')


def ads_remove(*, amount, timeout):
    if ads.with_(timeout=timeout).wait_until(have.size_greater_than_or_equal(amount)):
        ads.perform(command.js.remove)
