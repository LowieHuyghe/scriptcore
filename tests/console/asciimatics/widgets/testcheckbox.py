
from scriptcore.testing.testcase import TestCase
from scriptcore.console.asciimatics.widgets.checkbox import CheckBox
from asciimatics.widgets import CheckBox as ACheckBox


class TestCheckBox(TestCase):

    def test_checkbox(self):
        """
        Test the checkbox
        :return:    void
        """

        changed_checkbox = []

        def change_handler(checkbox):
            changed_checkbox.append(checkbox)

        checkbox = CheckBox(self.rand_str(), on_change=change_handler)
        checkbox.value = True

        self.assert_is_instance(checkbox, ACheckBox)
        self.assert_equal(checkbox, changed_checkbox[0])
