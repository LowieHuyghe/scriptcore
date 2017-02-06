
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

        self.assert_is_instance(checkbox, ACheckBox)
        for value in [True, False, True]:
            previous_count = len(changed_checkbox)
            checkbox.value = value
            self.assert_equal(previous_count + 1, len(changed_checkbox))
            self.assert_equal(checkbox, changed_checkbox[-1])
