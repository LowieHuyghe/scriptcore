
from scriptcore.testing.testcase import TestCase
from scriptcore.console.asciimatics.widgets.layout import Layout
from asciimatics.widgets import Layout as ALayout


class TestLayout(TestCase):

    def test_layout(self):
        """
        Test the layout
        :return:    void
        """

        layout = Layout([1])

        self.assert_is_instance(layout, ALayout)
