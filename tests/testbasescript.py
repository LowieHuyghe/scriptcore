
from scriptcore.testing.testcase import TestCase
from scriptcore.basescript import BaseScript
from scriptcore.console.command import Command
from scriptcore.console.option import Option
from scriptcore.console.errors.unknowncommanderror import UnknownCommandError
from scriptcore.console.errors.unknownoptionerror import UnknownOptionError
import os.path
import sys
if sys.version_info < (3, 0):
    from cStringIO import StringIO
else:
    from io import StringIO
import types


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

        # Add / to the end
        base_path = '%s%s' % (self.base_path, os.path.sep)
        # Construct the script
        script = TestScript(base_path, self.rand_str(), self.rand_str())

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
            Option('c', 'is cn option', default=['defcult c'], long='cccc', type=Option.type_list),
        ]
        for option in options[:-1]:
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
                                        if option == options[-1] or option2 == options[-1]:
                                            if (provide and option == options[-1]) or (provide2 and option2 == options[-1]):
                                                with self.assert_raises(UnknownOptionError):
                                                    script._analyze_arguments()
                                            continue
                                        else:
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

    def test_run_basic(self):
        """
        Test the run basic functions
        :return:    void
        """

        title = self.rand_str()
        description = self.rand_str()
        option = Option('a', 'is an option', default=None, long='aaaa', type=None)
        script = TestScript(self.base_path, title, description, arguments=['-%s' % option.short])
        script._register_option(option.short, option.description, option.default, option.long, option.type)

        # Not analyzed yet
        self.assert_false(script._has_option(option.short))
        self.assert_not_in(title, self.stdout.getvalue())
        self.assert_not_in(description, self.stdout.getvalue())

        script.run()

        # Analyzed and printed help
        self.assert_true(script._has_option(option.short))
        self.assert_in(title, self.stdout.getvalue())
        self.assert_in(description, self.stdout.getvalue())

    def test_run_commands(self):
        """
        Test the run commands
        :return:    void
        """

        command_callback_check = []

        def command_callback(arguments=None):
            command_callback_check.append(arguments)

        commands = [
            Command('this', 'is a command', command_callback),
            Command('second', 'command this is', TestSubScript),
            Command('third', 'this one won\'t be registered', TestSubScript),
        ]
        title = self.rand_str()
        description = self.rand_str()

        for command in commands:
            for command2 in commands:
                for provide in [True, False]:
                    for provide2 in [True, False]:
                        # Skip if same command
                        if command is not None and command2 is not None and command == command2:
                            continue

                        # Setup arguments
                        arguments = []
                        if provide:
                            arguments.append(command.command)
                        if provide2:
                            arguments.append(command2.command)

                        # Clear output
                        self.stdout = sys.stdout = StringIO()
                        command_callback_check = []
                        TestSubScript.command_callback_check = []

                        # Construct script
                        script = TestScript(self.base_path, title, description, arguments=arguments)
                        if command != commands[-1]:
                            script._register_command(command.command, command.description, command.callback)
                        if command2 != commands[-1]:
                            script._register_command(command2.command, command2.description, command2.callback)

                        # Run
                        if command == commands[-1] or command2 == commands[-1]:
                            if (provide and command == commands[-1]) or (not provide and provide2 and command2 == commands[-1]):
                                with self.assert_raises(UnknownCommandError):
                                    script.run()
                            continue
                        else:
                            script.run()

                        if not provide and not provide2:
                            self.assert_in(title, self.stdout.getvalue())
                            self.assert_in(description, self.stdout.getvalue())
                        else:
                            self.assert_not_in(title, self.stdout.getvalue())
                            self.assert_not_in(description, self.stdout.getvalue())

                            # Check if command given
                            self.assert_equal(provide, script._has_command(command.command))
                            # Second command won't run if first was given
                            self.assert_equal(not provide and provide2, script._has_command(command2.command))

                            if provide:
                                if isinstance(command.callback, types.FunctionType):
                                    self.assert_equal(1, len(command_callback_check))
                                    self.assert_equal_deep(arguments[1:], command_callback_check[0])
                                else:
                                    self.assert_equal(1, len(TestSubScript.command_callback_check))
                                    self.assert_equal_deep(arguments[1:], TestSubScript.command_callback_check[0])
                                if isinstance(command2.callback, types.FunctionType):
                                    self.assert_equal(0, len(command_callback_check))
                                else:
                                    self.assert_equal(0, len(TestSubScript.command_callback_check))
                            elif provide2:
                                if isinstance(command2.callback, types.FunctionType):
                                    self.assert_equal(1, len(command_callback_check))
                                    self.assert_equal_deep(arguments[1:], command_callback_check[0])
                                else:
                                    self.assert_equal(1, len(TestSubScript.command_callback_check))
                                    self.assert_equal_deep(arguments[1:], TestSubScript.command_callback_check[0])
                                if isinstance(command.callback, types.FunctionType):
                                    self.assert_equal(0, len(command_callback_check))
                                else:
                                    self.assert_equal(0, len(TestSubScript.command_callback_check))

    def test_run_natural(self):
        """
        Test natural run behaviour
        :return:    void
        """

        def callback_keyboard_interrupt(arguments=None):
            raise KeyboardInterrupt('keyboardinterrupt')

        callback_unhandlederror_message = self.rand_str()

        def callback_unhandlederror(arguments=None):
            raise RuntimeError(callback_unhandlederror_message)

        commands = [
            Command('keyboardinterrupt', 'keyboardinterrupt', callback_keyboard_interrupt),
            Command('unhandlederror', 'unhandlederror', callback_unhandlederror),
        ]

        # Keyboard interrupt should be catched
        script = TestScriptNatural(self.base_path, self.rand_str(), self.rand_str(), arguments=['keyboardinterrupt'])
        for command in commands:
            script._register_command(command.command, command.description, command.callback)
            with self.assert_raises(SystemExit):
                script.run()

        # Unhandled error
        script = TestScriptNatural(self.base_path, self.rand_str(), self.rand_str(), arguments=['unhandlederror'])
        for command in commands:
            script._register_command(command.command, command.description, command.callback)
        with self.assert_raises(SystemExit):
            script.run()
        self.assert_in(callback_unhandlederror_message, self.stdout.getvalue())


class TestScript(BaseScript):

    def run(self):
        self._analyze_arguments()
        self._run()


class TestSubScript(BaseScript):

    command_callback_check = []

    def __init__(self, base_path, arguments=None):
        super(TestSubScript, self).__init__(base_path, 'Test sub script', 'Test sub description', arguments=arguments)

    def run(self):
        self._run()

    def _run(self):
        """
        Run the script
        :return:    void
        """

        TestSubScript.command_callback_check.append(self._arguments)
        self.help()


class TestScriptNatural(BaseScript):
    pass
