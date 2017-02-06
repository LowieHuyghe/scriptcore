
from scriptcore.testing.testcase import TestCase
from scriptcore.console.output.output import Output


class TestOutput(TestCase):

    def test_title(self):
        """
        Test title-function
        :return:    void
        """

        text = self.rand_str()
        text2 = self.rand_str()

        output = Output()
        output.title(text)
        output(text2, type='title')

        self.assert_in(text, self.stdout.getvalue())
        self.assert_in(text2, self.stdout.getvalue())

    def test_subtitle(self):
        """
        Test subtitle-function
        :return:    void
        """

        text = self.rand_str()
        text2 = self.rand_str()

        output = Output()
        output.subtitle(text)
        output(text2, type='subtitle')

        self.assert_in(text, self.stdout.getvalue())
        self.assert_in(text2, self.stdout.getvalue())

    def test_success(self):
        """
        Test success-function
        :return:    void
        """

        text = self.rand_str()
        text2 = self.rand_str()

        output = Output()
        output.success(text)
        output(text2, type='success')

        self.assert_in(text, self.stdout.getvalue())
        self.assert_in(text2, self.stdout.getvalue())

    def test_error(self):
        """
        Test error-function
        :return:    void
        """

        text = self.rand_str()
        text2 = self.rand_str()

        output = Output()
        output.error(text)
        output(text2, type='error')

        self.assert_in(text, self.stdout.getvalue())
        self.assert_in(text2, self.stdout.getvalue())

    def test_warning(self):
        """
        Test warning-function
        :return:    void
        """

        text = self.rand_str()
        text2 = self.rand_str()

        output = Output()
        output.warning(text)
        output(text2, type='warning')

        self.assert_in(text, self.stdout.getvalue())
        self.assert_in(text2, self.stdout.getvalue())

    def test_info(self):
        """
        Test info-function
        :return:    void
        """

        text = self.rand_str()
        text2 = self.rand_str()

        output = Output()
        output.info(text)
        output(text2, type='info')

        self.assert_in(text, self.stdout.getvalue())
        self.assert_in(text2, self.stdout.getvalue())

    def test_default(self):
        """
        Test default-function
        :return:    void
        """

        text = self.rand_str()
        text2 = self.rand_str()

        output = Output()
        output.default(text)
        output(text2)

        self.assert_in(text, self.stdout.getvalue())
        self.assert_in(text2, self.stdout.getvalue())

    def test_no_new_line(self):
        """
        Test no new line
        :return:    void
        """

        text = self.rand_str()
        text2 = self.rand_str()

        output = Output()

        output.default(text, newline=False)
        self.assert_in(text, self.stdout.getvalue())
        self.assert_not_in(text2, self.stdout.getvalue())

        output.default(text2, newline=False)
        self.assert_in(text, self.stdout.getvalue())
        self.assert_in(text2, self.stdout.getvalue())
        self.assert_in('\r%s\r%s' % (text, text2), self.stdout.getvalue())

    def test_color(self):
        """
        Test default-function
        :return:    void
        """

        text = self.rand_str()
        colors = [
            'black',
            'gray_dark',
            'red',
            'red_light',
            'green',
            'green_light',
            'orange',
            'yellow',
            'blue',
            'blue_light',
            'purple',
            'purple_light',
            'cyan',
            'cyan_light',
            'gray_light',
            'white',
        ]

        output = Output()

        for color in colors:
            self.assert_in(text, output.color(text, color))
