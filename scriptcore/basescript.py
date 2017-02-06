
from __future__ import absolute_import
from scriptcore.config.config import Config
from scriptcore.console.output.output import Output
from scriptcore.console.input.input import Input
from scriptcore.console.command import Command
from scriptcore.process.execute import Execute
from scriptcore.console.option import Option
from abc import ABCMeta
import traceback
import os.path
import types
import sys


class BaseScript(object):

    __metaclass__ = ABCMeta

    _current_script = None

    @staticmethod
    def current_script():
        """
        Get the current script
        :return:
        """
        return BaseScript._current_script

    def __init__(self, base_path, title, description, arguments=None):
        """
        Construct the script
        :param base_path:   The base path
        :param title:       The title
        :param description: The description
        :param arguments:   The arguments
        """

        BaseScript._current_script = self

        if base_path[-1:1] == os.path.sep:
            base_path = base_path[:-1]
        self._base_path = base_path
        self.config = Config()

        self._title = title
        self._description = description
        self._arguments = arguments if arguments is not None else sys.argv[1::]
        self._analyzed_arguments = False

        self.output = Output()
        self.input = Input()
        self.execute = Execute(self.output)
        self._commands = {}
        self._options = {}

    def get_path(self, filename):
        """
        Get path from the filename
        :param filename:
        :return:
        """

        if not filename:
            return self._base_path

        if filename[0:1] == os.path.sep:
            filename = filename[1::]

        return os.path.join(self._base_path, filename)

    def _analyze_arguments(self):
        """
        Analyze the arguments
        :return:    void
        """

        # Reset
        self._reset_arguments()

        # Loop arguments
        last_option = None
        for i in range(0, len(self._arguments)):
            argument = self._arguments[i]

            # Check commands
            for command in self._commands.values():
                if command.command == argument:
                    command.arguments = self._arguments[i + 1::]
                    command.given = True
                    return

            # Check long options
            if argument[:2] == '--':
                option_given = False
                for option in self._options.values():
                    if option.long == argument[2:]:
                        option.given = True
                        last_option = option
                        option_given = True
                        break
                if not option_given:
                    raise RuntimeError('Unknown option "%s" given' % argument)

            elif argument[:1] == '-':
                option_given = False
                for option in self._options.values():
                    if option.short == argument[1:]:
                        option.given = True
                        last_option = option
                        option_given = True
                        break
                if not option_given:
                    raise RuntimeError('Unknown option "%s" given' % argument)

            elif last_option:
                last_option.add_value(argument)
                if not last_option.type == Option.type_list:
                    last_option = None

            else:
                raise RuntimeError('Unknown command "%s" given' % argument)

    def _reset_arguments(self):
        """
        Reset the arguments
        :return:    void
        """

        for option in self._options.values():
            option.reset()
        for command in self._commands.values():
            command.reset()

    def _has_command(self, command):
        """
        Check if has command
        :param command: The command
        :return:        Has command
        """

        return self._commands[command].given

    def _has_option(self, short):
        """
        Check if has option
        :param short:   Short option
        :return:        Has option
        """

        return self._options[short].given

    def _get_option(self, short):
        """
        Get option value
        :param short:   Short option
        :return:        The value
        """

        return self._options[short].value

    def _register_command(self, command, description, callback):
        """
        Register a command
        :param command:     Command to type
        :param description: Description
        :param callback:    Callback function
        :return:            void
        """

        self._commands[command] = Command(command, description, callback)

    def _register_option(self, short, description, default=None, long=None, type=None):
        """
        Register an option
        :param short:       Option in short
        :param description: Description
        :param default:     The default value
        :param long:        Option in long
        :param type:        Type of option
        :return:            void
        """

        self._options[short] = Option(short, description, default=default, long=long, type=type)

    def run(self):
        """
        Run the script
        """

        try:
            self._analyze_arguments()
            self._run()

        except KeyboardInterrupt:
            sys.exit(1)

        except Exception as e:
            ex_type, ex, tb = sys.exc_info()
            e_tb = '\n'.join(traceback.format_tb(tb))
            del tb

            self.output.error('Error: %s\n%s' % (e, e_tb))
            self.output('')

    def _run(self):
        """
        Actually run the script
        """

        for command in self._commands.values():
            if command.given:
                if isinstance(command.callback, types.FunctionType):
                    command.callback(arguments=command.arguments)
                else:
                    subcommand = command.callback(self._base_path, arguments=command.arguments)
                    subcommand.run()
                return

        self.help()

    def help(self):
        """
        Print the help
        :return:    void
        """

        title = '%s ~ %s' % (self._title, self._description)
        self.output(title, type='title')
        self.output('')

        # Minimum length
        first_column_min_length = 0
        for command in self._commands.values():
            first_column_min_length = max(first_column_min_length, len(command.command))
        for option in self._options.values():
            first_column_min_length = max(first_column_min_length, len(option.short) + 1)
            if option.long is not None:
                first_column_min_length = max(first_column_min_length, len(option.long) + 2)

        # Print commands
        if len(self._commands):
            self.output('Commands')

            for command in self._commands.values():
                print_command = self.output.color(command.command, 'green')
                print_command = '%s%s' % (print_command, ' ' * (first_column_min_length - len(command.command)))
                self.output('    %s    %s' % (print_command, command.description))

            self.output('')

        # Print options
        if len(self._options):
            self.output('Options')

            for option in self._options.values():
                print_option = self.output.color('-%s' % option.short, 'green')
                print_option = '%s%s' % (print_option, ' ' * (first_column_min_length - len(option.short)))
                print_option_default = ' (default: %s)' % option.default if option.default is not None else ''
                print_option_type = '(%s) ' % option.type if option.type is not None else ''
                self.output('    %s   %s%s%s' % (print_option, print_option_type, option.description, print_option_default))
                if option.long is not None:
                    self.output('    --%s' % option.long)

            self.output('')

        # No commands or options
        if not len(self._commands) and not len(self._options):
            self.output('No commands or options registered')
            self.output('')
