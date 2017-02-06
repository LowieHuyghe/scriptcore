
from scriptcore.testing.testcase import TestCase
from scriptcore.basescript import BaseScript
from scriptcore.console.command import Command
from scriptcore.console.option import Option
import os.path
try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO
import sys


class TestBaseScript(TestCase):

    def set_up(self):
        """
        Set up the test
        :return:    void
        """

        super(TestBaseScript, self).set_up()

        BaseScript._current_script = None
        self.base_path = os.path.dirname(os.path.realpath(__file__))

    def test_current_script(self):
        """
        Test the current script function
        :return:    void
        """

        self.assert_is_none(TestScript.current_script())
        self.assert_equal(BaseScript.current_script(), TestScript.current_script())

        script = TestScript(self.base_path, self.rand_str(), self.rand_str())

        self.assert_equal(script, TestScript.current_script())
        self.assert_equal(BaseScript.current_script(), TestScript.current_script())

    def test_get_path(self):
        """
        Test get path function
        :return:    void
        """

        script = TestScript(self.base_path, self.rand_str(), self.rand_str())

        self.assert_equal(self.base_path, script.get_path(''))
        self.assert_equal(os.path.join(self.base_path, 'test.txt'), script.get_path('test.txt'))
        self.assert_equal(os.path.join(self.base_path, 'test.txt'), script.get_path('/test.txt'))
        self.assert_equal(os.path.join(self.base_path, 'subdir/test.txt'), script.get_path('subdir/test.txt'))

    def test_commands(self):
        """
        Test the commands
        :return:    void
        """

        def command_callback(arguments=None):
            pass
        commands = [
            Command('this', 'is a command', command_callback),
            Command('second', 'command this is', TestSubScript)
        ]
        script = TestScript(self.base_path, self.rand_str(), self.rand_str())
        for command in commands:
            script._register_command(command.command, command.description, command.callback)

        self.assert_equal(len(commands), len(script._commands))
        for command in commands:
            self.assert_equal(command.command, script._commands[command.command].command)
            self.assert_equal(command.description, script._commands[command.command].description)
            self.assert_equal(command.callback, script._commands[command.command].callback)
            self.assert_false(script._commands[command.command].given)
            self.assert_is_none(script._commands[command.command].arguments)

    def test_options(self):
        """
        Test the options
        :return:    void
        """

        options = [
            Option('a', 'is an option', default=None, long='aaaa', type=None),
            Option('b', 'is bn option', default=['defbult b'], long='bbbb', type=Option.type_list),
        ]
        script = TestScript(self.base_path, self.rand_str(), self.rand_str())
        for option in options:
            script._register_option(option.short, option.description, option.default, option.long, option.type)

        self.assert_equal(len(options), len(script._options))
        for option in options:
            self.assert_equal(option.short, script._options[option.short].short)
            self.assert_equal(option.description, script._options[option.short].description)
            self.assert_equal(option.default, script._options[option.short].default)
            self.assert_equal(option.long, script._options[option.short].long)
            self.assert_equal(option.type, script._options[option.short].type)

    def test_help(self):
        """
        Test the help function
        :return:    void
        """

        title = self.rand_str()
        description = self.rand_str()
        commands = [
            Command('this', 'is a command', TestSubScript),
            Command('second', 'command this is', TestSubScript)
        ]
        options = [
            Option('a', 'is an option', default=None, long='aaaa', type=None),
            Option('b', 'is bn option', default=['defbult b'], long='bbbb', type=Option.type_list),
        ]

        for provide_commands in [True, False]:
            for provide_options in [True, False]:

                # Setup script
                script = TestScript(self.base_path, title, description)
                if provide_commands:
                    for command in commands:
                        script._register_command(command.command, command.description, command.callback)
                if provide_options:
                    for option in options:
                        script._register_option(option.short, option.description, option.default, option.long, option.type)
                # Clear output
                self.stdout = sys.stdout = StringIO()

                # Test output
                script.help()
                self.assert_in(title, self.stdout.getvalue())
                self.assert_in(description, self.stdout.getvalue())
                if provide_commands:
                    for command in commands:
                        self.assert_in(command.command, self.stdout.getvalue())
                        self.assert_in(command.description, self.stdout.getvalue())
                if provide_options:
                    for option in options:
                        self.assert_in('-%s' % option.short, self.stdout.getvalue())
                        self.assert_in(option.description, self.stdout.getvalue())
                        if option.default is not None:
                            if isinstance(option.default, list):
                                for default in option.default:
                                    self.assert_in(default, self.stdout.getvalue())
                            else:
                                self.assert_in(option.default, self.stdout.getvalue())
                        self.assert_in('--%s' % option.long, self.stdout.getvalue())
                        if option.type is not None:
                            self.assert_in(option.type, self.stdout.getvalue())

    def test_arguments(self):
        """
        Test argument function
        :return:    void
        """

        script = TestScript(self.base_path, self.rand_str(), self.rand_str())
        options = [
            Option('a', 'is an option', default=None, long='aaaa', type=None),
            Option('b', 'is bn option', default=['defbult b'], long='bbbb', type=Option.type_list),
        ]
        for option in options:
            script._register_option(option.short, option.description, option.default, option.long, option.type)

        for option in options:
            for option2 in options:
                for short in [True, False]:
                    for short2 in [True, False]:
                        for provide in [True, False]:
                            for provide2 in [True, False]:
                                for value in [None, self.rand_str()]:
                                    for value2 in [None, self.rand_str()]:
                                        # Skip if same option
                                        if option is not None and option2 is not None and option == option2:
                                            continue

                                        # Compose arguments
                                        arguments = []
                                        if provide:
                                            if short:
                                                arguments.append('-%s' % option.short)
                                            else:
                                                arguments.append('--%s' % option.long)
                                            if value is not None:
                                                arguments.append(value)
                                        if provide2:
                                            if short2:
                                                arguments.append('-%s' % option2.short)
                                            else:
                                                arguments.append('--%s' % option2.long)
                                            if value2:
                                                arguments.append(value2)

                                        # Add and analyze
                                        script._arguments = arguments
                                        script._analyze_arguments()

                                        # Check provided
                                        self.assert_equal(provide, script._has_option(option.short))
                                        self.assert_equal(provide2, script._has_option(option2.short))
                                        # Check value
                                        if provide and value is not None:
                                            if option.type is Option.type_list:
                                                self.assert_equal([value], script._get_option(option.short))
                                            else:
                                                self.assert_equal(value, script._get_option(option.short))
                                        else:
                                            self.assert_equal_deep(option.default, script._get_option(option.short))
                                        if provide2 and value2 is not None:
                                            if option2.type is Option.type_list:
                                                self.assert_equal([value2], script._get_option(option2.short))
                                            else:
                                                self.assert_equal(value2, script._get_option(option2.short))
                                        else:
                                            self.assert_equal(option2.default, script._get_option(option2.short))

                                        # Test rest arguments
                                        script._reset_arguments()
                                        self.assert_equal(option.default, script._get_option(option.short))
                                        self.assert_equal(option2.default, script._get_option(option2.short))


class TestScript(BaseScript):
    pass


class TestSubScript(BaseScript):
    pass
