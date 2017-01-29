
class Option(object):

    def __init__(self, short, description, default=None, long=None, type=None):
        """
        Construct option
        :param short:       The short
        :param description: The description
        :param default:     The default value
        :param long:        The long
        :param type:        The type
        """

        self.short = short
        self.description = description
        self.default = default
        self.long = long
        self.given = False
        self.type = type
        if self.type == 'list':
            self._value = []
        else:
            self._value = None

    @property
    def value(self):
        if self.given:
            return self._value
        return self.default

    @value.setter
    def value(self, value):
        self._value = value
        self.given = True

    def add_value(self, value):
        if self.type == 'list':
            self._value.append(value)
        else:
            self._value = value

        self.given = True

    def reset(self):
        """
        Reset option
        :return:    void
        """

        self.given = False
        if self.type == 'list':
            self._value = []
        else:
            self._value = None
