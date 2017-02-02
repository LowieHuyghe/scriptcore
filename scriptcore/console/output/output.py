
import sys


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
        self._emoticons = {
            'check': '\xE2\x9C\x85 ',
            'cross': '\xE2\x9D\x8C ',
            'bell': '\xF0\x9F\x94\x94 ',
            'info': '\xF0\x9F\x92\xAC '
        }

        self._last_no_newline_length = 0

    def __call__(self, text, type=None, newline=True):
        """
        Call the output
        :param text:    The text to print
        :param type:    The type of text
        :param newline: Newline at the end
        :return:        void
        """

        if type == 'title':
            self.title(text, newline=newline)

        elif type == 'subtitle':
            self.subtitle(text, newline=newline)

        elif type == 'success':
            self.success(text, newline=newline)

        elif type == 'warning':
            self.warning(text, newline=newline)

        elif type == 'info':
            self.info(text, newline=newline)

        elif type == 'error':
            self.error(text, newline=newline)

        else:
            self.default(text, newline=newline)

    def title(self, text, newline=True):
        """
        Print title
        :param text:    Text to print
        :param newline: Newline at the end
        :return:        void
        """

        print_text = '#  %s  #' % text

        self.default('%s\n%s\n%s' % (
            self.color('#' * len(print_text), 'blue'),
            self.color(print_text, 'blue'),
            self.color('#' * len(print_text), 'blue')
        ), newline=newline)

    def subtitle(self, text, newline=True):
        """
        Print subtitle
        :param text:    Text to print
        :param newline: Newline at the end
        :return:        void
        """

        self.default('# %s' % text, newline=newline)

    def success(self, text, newline=True):
        """
        Print success
        :param text:    Text to print
        :param newline: Newline at the end
        :return:        void
        """

        self.default('%s %s' % (self._emoticons['check'], self.color(text, 'green')), newline=newline)

    def warning(self, text, newline=True):
        """
        Print warning
        :param text:    Text to print
        :param newline: Newline at the end
        :return:        void
        """

        self.default('%s %s' % (self._emoticons['bell'], self.color(text, 'yellow')), newline=newline)

    def error(self, text, newline=True):
        """
        Print error
        :param text:    Text to print
        :param newline: Newline at the end
        :return:        void
        """

        self.default('%s %s' % (self._emoticons['cross'], self.color(text, 'red')), newline=newline)

    def info(self, text, newline=True):
        """
        Print info
        :param text:    Text to print
        :param newline: Newline at the end
        :return:        void
        """

        self.default('%s %s' % (self._emoticons['info'], text), newline=newline)

    def default(self, text, newline=True):
        """
        Print default text
        :param text:    Text to print
        :param newline: Newline at the end
        :return:        void
        """

        # Calculate the text length
        text_length = text
        for color in self._colors.values():
            text_length = text_length.replace(color, '')
        for emoticon in self._emoticons.values():
            text_length = text_length.replace(emoticon, ' ')
        text_length = len(text_length)

        # Make the text to print
        spaces = ' ' * max(self._last_no_newline_length - text_length, 0)
        text = '\r%s%s' % (text, spaces)

        if newline:
            print text

            self._last_no_newline_length = 0
        else:
            sys.stdout.write(text)
            sys.stdout.flush()

            self._last_no_newline_length = text_length

    def color(self, text, color):
        """
        Return colored text
        :param text:    Text to convert
        :param color:   Color
        :return:        Converted text
        """

        return '%s%s%s' % (self._colors[color], text, self._colors['n'])
