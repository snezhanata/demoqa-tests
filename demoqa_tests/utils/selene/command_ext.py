from selene.core.wait import Command


class js:
    scroll_one_page = Command(
        'scroll one page',
        lambda element: element.execute_script(
            'window.scrollTo(0, document.body.scrollHeight)'))