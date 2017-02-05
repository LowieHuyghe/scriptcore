
from scriptcore.testing.testcase import TestCase
from scriptcore.console.asciimatics.widgets.divider import Divider
from asciimatics.widgets import Divider as ADivider


class TestDivider(TestCase):

    def test_divider(self):
        """
        Test the divider
        :return:    void
        """

        divider = Divider()

        self.assert_is_instance(divider, ADivider)
