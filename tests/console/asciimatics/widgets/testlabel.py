
from scriptcore.testing.testcase import TestCase
from scriptcore.console.asciimatics.widgets.label import Label
from asciimatics.widgets import Label as ALabel


class TestLabel(TestCase):

    def test_label(self):
        """
        Test the label
        :return:    void
        """

        label = Label(self.rand_str())

        self.assert_is_instance(label, ALabel)
