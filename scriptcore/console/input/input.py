
from scriptcore.console.output.output import Output
import sys


class Input(object):

    def __init__(self):
        """
        Construct
        """

        self._output = Output()

    def __call__(self, description):
        """
        Call the instance
        :param description: Description
        :return:            Value
        """

        return self.text(description)

    def text(self, description):
        """
        Raw input
        :param description: Description
        :return:            Value
        """

        if description:
            print(description)

        result = self._input(self._output.color('> ', 'yellow'))

        if result:
            return result
        return None

    def pick(self, options, description):
        """
        Pick an option
        :param options:     List of options
        :param description: Description
        :return:            Index
        """

        if description:
            print(description)

        for i in range(0, len(options)):
            print('[%i] %s' % (i, options[i]))

        result = self.integer(None)

        if result is not None and result < len(options):
            return result
        return None

    def integer(self, description):
        """
        Integer input
        :param description: Description
        :return:            Integer
        """

        if description:
            print(description)

        result = self._input(self._output.color('> ', 'yellow'))

        try:
            return int(result)
        except ValueError:
            return None

    def float(self, description):
        """
        Float input
        :param description: Description
        :return:            Integer
        """

        if description:
            print(description)

        result = self._input(self._output.color('> ', 'yellow'))

        try:
            return float(result)
        except ValueError:
            return None

    def yes_no(self, description):
        """
        Yes no input
        :param description: Description
        :return:            Integer
        """

        if description:
            sys.stdout.write('%s ' % description)
            sys.stdout.flush()

        result = self._input(self._output.color('(y/n) ', 'yellow'))

        return result == 'y'

    def _input(self, description):
        """
        Input from user
        :param description: The description
        :return:            The user input
        """

        try:
            return raw_input(description)
        except NameError:
            return input(description)
