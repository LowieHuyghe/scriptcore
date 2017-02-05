
from scriptcore.testing.testcase import TestCase
from scriptcore.console.asciimatics.widgets.button import Button
from asciimatics.widgets import Button as AButton


class TestButton(TestCase):

    def test_button(self):
        """
        Test the button
        :return:    void
        """

        button = Button(self.rand_str(), lambda x: x)

        self.assert_is_instance(button, AButton)
