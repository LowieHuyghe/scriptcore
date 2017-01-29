
class Output(object):

    def __init__(self):
        """
        Construct
        """

        self._colors = {
            'n': '\033[0m',
            'black': '\033[0;30m',
            'gray_dark': '\033[1;30m',
            'red': '\033[0;31m',
            'red_light': '\033[1;31m',
            'green': '\033[0;32m',
            'green_light': '\033[1;32m',
            'orange': '\033[0;33m',
            'yellow': '\033[1;33m',
            'blue': '\033[0;34m',
            'blue_light': '\033[1;34m',
            'purple': '\033[0;35m',
            'purple_light': '\033[1;35m',
            'cyan': '\033[0;36m',
            'cyan_light': '\033[1;36m',
            'gray_light': '\033[0;37m',
            'white': '\033[1;37m',
        }

    def __call__(self, text, type=None):
        """
        Call the output
        :param text:    The text to print
        :param type:    The type of text
        :return:        void
        """

        if type == 'title':
            self.print_title(text)

        elif type == 'subtitle':
            self.print_subtitle(text)

        elif type == 'error':
            self.print_error(text)

        else:
            self.print_default(text)

    def print_title(self, text):
        """
        Print title
        :param text:    Text to print
        :return:        void
        """

        print_text = '#  %s  #' % text

        print self.color('#' * len(print_text), 'blue')
        print self.color(print_text, 'blue')
        print self.color('#' * len(print_text), 'blue')

    def print_subtitle(self, text):
        """
        Print subtitle
        :param text:    Text to print
        :return:        void
        """

        print '# %s' % text

    def print_error(self, text):
        """
        Print error
        :param text:    Text to print
        :return:        void
        """

        print self.color(text, 'red')

    def print_default(self, text):
        """
        Print default text
        :param text:    Text to print
        :return:        void
        """

        print text

    def color(self, text, color):
        """
        Return colored text
        :param text:    Text to convert
        :param color:   Color
        :return:        Converted text
        """

        return '%s%s%s' % (self._colors[color], text, self._colors['n'])
