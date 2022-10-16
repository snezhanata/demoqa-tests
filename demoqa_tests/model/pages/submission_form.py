from selene import have

from demoqa_tests.model.components import modal
from demoqa_tests.utils import common


class SubmissionForm:
    def should_have_table(self, *data):
        modal.rows.all('td').should(have.exact_texts(*common.flatten(data)))
