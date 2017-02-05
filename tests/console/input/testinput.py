
from scriptcore.testing.testcase import TestCase
from scriptcore.console.input.input import Input
import mock


class TestInput(TestCase):

    @mock.patch.object(Input, '_input', return_value='e8n0dpankpdvdni3kgac')
    def test_default(self, patched_input):
        """
        Test default input
        :param patched_input:   The patched input
        :return:                void
        """

        description = self.rand_str()
        description2 = self.rand_str()

        input = Input()

        value = input(description)
        self.assert_in(description, self.stdout.getvalue())
        self.assert_equal('e8n0dpankpdvdni3kgac', value)

        value = input.text(description2)
        self.assert_in(description2, self.stdout.getvalue())
        self.assert_equal('e8n0dpankpdvdni3kgac', value)

    @mock.patch.object(Input, '_input', return_value='')
    def test_default_empty(self, patched_input):
        """
        Test default empty input
        :param patched_input:   The patched input
        :return:                void
        """

        input = Input()
        value = input('')

        self.assert_is_none(value)

    @mock.patch.object(Input, '_input', return_value='4815162342')
    def test_integer(self, patched_input):
        """
        Test integer input
        :param patched_input:   The patched input
        :return:                void
        """

        description = self.rand_str()

        input = Input()
        value = input.integer(description)

        self.assert_in(description, self.stdout.getvalue())
        self.assert_equal(4815162342, value)

    @mock.patch.object(Input, '_input', return_value='Ygritte dies')
    def test_integer_invalid(self, patched_input):
        """
        Test integer invalid input
        :param patched_input:   The patched input
        :return:                void
        """

        input = Input()
        value = input.integer('')

        self.assert_is_none(value)

    @mock.patch.object(Input, '_input', return_value='4.2')
    def test_float(self, patched_input):
        """
        Test float input
        :param patched_input:   The patched input
        :return:                void
        """

        description = self.rand_str()

        input = Input()
        value = input.float(description)

        self.assert_in(description, self.stdout.getvalue())
        self.assert_equal(4.2, value)

    @mock.patch.object(Input, '_input', return_value='Peanut butter jelly time')
    def test_float_invalid(self, patched_input):
        """
        Test float invalid input
        :param patched_input:   The patched input
        :return:                void
        """

        input = Input()
        value = input.float('')

        self.assert_is_none(value)

    @mock.patch.object(Input, '_input', return_value='y')
    def test_yes_no(self, patched_input):
        """
        Test yes_no input
        :param patched_input:   The patched input
        :return:                void
        """

        description = self.rand_str()

        input = Input()
        value = input.yes_no(description)

        self.assert_in(description, self.stdout.getvalue())
        self.assert_true(value)

    @mock.patch.object(Input, '_input', return_value='n')
    def test_yes_no_no(self, patched_input):
        """
        Test yes_no no input
        :param patched_input:   The patched input
        :return:                void
        """

        input = Input()
        value = input.yes_no('')

        self.assert_false(value)

    @mock.patch.object(Input, '_input', return_value='Indiana Jones dies in Star Wars')
    def test_yes_no_invalid(self, patched_input):
        """
        Test yes_no invalid input
        :param patched_input:   The patched input
        :return:                void
        """

        input = Input()
        value = input.yes_no('')

        self.assert_false(value)

    @mock.patch.object(Input, '_input', return_value='2')
    def test_pick(self, patched_input):
        """
        Test pick input
        :param patched_input:   The patched input
        :return:                void
        """

        description = self.rand_str()
        options = [
            'May the',
            'odds ever',
            'be in your',
            'favour'
        ]

        input = Input()
        value = input.pick(options, description)

        self.assert_in(description, self.stdout.getvalue())
        self.assert_equal(2, value)

    @mock.patch.object(Input, '_input', return_value='6')
    def test_pick_out_of_range(self, patched_input):
        """
        Test pick out of range input
        :param patched_input:   The patched input
        :return:                void
        """

        description = self.rand_str()
        options = [
            'May the',
            'odds ever',
            'be in your',
            'favour'
        ]

        input = Input()
        value = input.pick(options, description)

        self.assert_in(description, self.stdout.getvalue())
        self.assert_is_none(value)

    @mock.patch.object(Input, '_input', return_value='Scoobiedoobiedoo')
    def test_pick_invalid(self, patched_input):
        """
        Test pick invalid input
        :param patched_input:   The patched input
        :return:                void
        """

        description = self.rand_str()
        options = [
            'May the',
            'odds ever',
            'be in your',
            'favour'
        ]

        input = Input()
        value = input.pick(options, description)

        self.assert_in(description, self.stdout.getvalue())
        self.assert_is_none(value)
