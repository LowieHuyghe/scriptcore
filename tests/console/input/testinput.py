
from scriptcore.testing.testcase import TestCase
from scriptcore.console.input.input import Input
import mock
import sys


class TestInput(TestCase):

    def test_default(self):
        """
        Test default input
        :return:    void
        """

        description = self.rand_str()
        description2 = self.rand_str()

        input = Input()

        with mock.patch(self._get_pathable_input(), return_value='e8n0dpankpdvdni3kgac'):
            value = input(description)
        self.assert_in(description, self.stdout.getvalue())
        self.assert_equal('e8n0dpankpdvdni3kgac', value)

        with mock.patch(self._get_pathable_input(), return_value='e8n0dpankpdvdni3kgac'):
            value = input.text(description2)
        self.assert_in(description2, self.stdout.getvalue())
        self.assert_equal('e8n0dpankpdvdni3kgac', value)

    def test_default_empty(self):
        """
        Test default empty input
        :return:    void
        """

        input = Input()
        with mock.patch(self._get_pathable_input(), return_value=''):
            value = input('')

        self.assert_is_none(value)

    def test_integer(self):
        """
        Test integer input
        :return:    void
        """

        description = self.rand_str()

        input = Input()
        with mock.patch(self._get_pathable_input(), return_value='4815162342'):
            value = input.integer(description)

        self.assert_in(description, self.stdout.getvalue())
        self.assert_equal(4815162342, value)

    def test_integer_invalid(self):
        """
        Test integer invalid input
        :return:    void
        """

        input = Input()
        with mock.patch(self._get_pathable_input(), return_value='Ygritte dies'):
            value = input.integer('')

        self.assert_is_none(value)

    def test_float(self):
        """
        Test float input
        :return:    void
        """

        description = self.rand_str()

        input = Input()
        with mock.patch(self._get_pathable_input(), return_value='4.2'):
            value = input.float(description)

        self.assert_in(description, self.stdout.getvalue())
        self.assert_equal(4.2, value)

    def test_float_invalid(self):
        """
        Test float invalid input
        :return:    void
        """

        input = Input()
        with mock.patch(self._get_pathable_input(), return_value='Peanut butter jelly time'):
            value = input.float('')

        self.assert_is_none(value)

    def test_yes_no(self):
        """
        Test yes_no input
        :return:    void
        """

        description = self.rand_str()

        input = Input()
        with mock.patch(self._get_pathable_input(), return_value='y'):
            value = input.yes_no(description)

        self.assert_in(description, self.stdout.getvalue())
        self.assert_true(value)

    def test_yes_no_no(self):
        """
        Test yes_no no input
        :return:    void
        """

        input = Input()
        with mock.patch(self._get_pathable_input(), return_value='n'):
            value = input.yes_no('')

        self.assert_false(value)

    def test_yes_no_invalid(self):
        """
        Test yes_no invalid input
        :return:    void
        """

        input = Input()
        with mock.patch(self._get_pathable_input(), return_value='Indiana Jones dies in Star Wars'):
            value = input.yes_no('')

        self.assert_false(value)

    def test_pick(self):
        """
        Test pick input
        :return:    void
        """

        description = self.rand_str()
        options = [
            'May the',
            'odds ever',
            'be in your',
            'favour'
        ]

        input = Input()
        with mock.patch(self._get_pathable_input(), return_value='2'):
            value = input.pick(options, description)

        self.assert_in(description, self.stdout.getvalue())
        self.assert_equal(2, value)

    def test_pick_out_of_range(self):
        """
        Test pick out of range input
        :return:    void
        """

        description = self.rand_str()
        options = [
            'May the',
            'odds ever',
            'be in your',
            'favour'
        ]

        input = Input()
        with mock.patch(self._get_pathable_input(), return_value='6'):
            value = input.pick(options, description)

        self.assert_in(description, self.stdout.getvalue())
        self.assert_is_none(value)

    def test_pick_invalid(self):
        """
        Test pick invalid input
        :return:    void
        """

        description = self.rand_str()
        options = [
            'May the',
            'odds ever',
            'be in your',
            'favour'
        ]

        input = Input()
        with mock.patch(self._get_pathable_input(), return_value='Scoobiedoobiedoo'):
            value = input.pick(options, description)

        self.assert_in(description, self.stdout.getvalue())
        self.assert_is_none(value)

    def _get_pathable_input(self):
        """
        Get the patchable input
        :return:    Patchable input
        """

        if sys.version_info < (3, 0):
            return '__builtin__.raw_input'
        else:
            return 'builtins.input'
