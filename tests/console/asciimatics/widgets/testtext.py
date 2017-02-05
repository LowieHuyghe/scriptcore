
from scriptcore.testing.testcase import TestCase
from scriptcore.console.asciimatics.widgets.text import Text
from asciimatics.widgets import Text as AText


class TestText(TestCase):

    def test_text(self):
        """
        Test the text
        :return:    void
        """

        text = Text()

        self.assert_is_instance(text, AText)
