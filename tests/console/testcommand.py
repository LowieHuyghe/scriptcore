
from scriptcore.testing.testcase import TestCase
from scriptcore.console.command import Command


class TestCommand(TestCase):

    def test_constructor(self):
        """
        Test constructor
        :return:    void
        """

        prop_command = 'command'
        prop_description = 'this is a description'
        prop_callback = max

        command = Command(prop_command, prop_description, prop_callback)

        self.assert_equal(prop_command, command.command)
        self.assert_equal(prop_description, command.description)
        self.assert_equal(prop_callback, command.callback)

    def test_properties(self):
        """
        Test properties
        :return:    void
        """

        prop_command = 'command'
        prop_description = 'this is a description'
        prop_callback = max
        prop_given = True
        prop_arguments = [1, 2, 3, 4]

        command = Command(None, None, None)
        command.command = prop_command
        command.description = prop_description
        command.callback = prop_callback
        command.given = prop_given
        command.arguments = prop_arguments

        self.assert_equal(prop_command, command.command)
        self.assert_equal(prop_description, command.description)
        self.assert_equal(prop_callback, command.callback)
        self.assert_equal(prop_given, command.given)
        self.assert_equal_deep(prop_arguments, command.arguments)

    def test_reset(self):
        """
        Test properties
        :return:    void
        """

        prop_command = 'command'
        prop_description = 'this is a description'
        prop_callback = max
        prop_given = True
        prop_arguments = [1, 2, 3, 4]

        command = Command(prop_command, prop_description, prop_callback)
        command.given = prop_given
        command.arguments = prop_arguments

        self.assert_equal(prop_given, command.given)
        self.assert_equal_deep(prop_arguments, command.arguments)

        command.reset()

        self.assert_equal(False, command.given)
        self.assert_equal(None, command.arguments)
