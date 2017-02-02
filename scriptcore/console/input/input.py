
from scriptcore.console.output.output import Output


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
            print description

        return raw_input(self._output.color('> ', 'yellow'))

    def pick(self, options, description):
        """
        Pick an option
        :param options:     List of options
        :param description: Description
        :return:            Index
        """

        if description:
            print description

        for i in range(0, len(options)):
            print '[%i] %s' % (i, options[i])

        return self.integer(None)

    def integer(self, description):
        """
        Integer input
        :param description: Description
        :return:            Integer
        """

        if description:
            print description

        result = raw_input(self._output.color('> ', 'yellow'))

        try:
            return int(result)
        except ValueError:
            return None

    def yes_no(self, description):
        """
        Yes no input
        :param description: Description
        :return:            Integer
        """

        result = raw_input('%s %s ' % (description, self._output.color('(y/n)', 'yellow')))

        return result == 'y'
