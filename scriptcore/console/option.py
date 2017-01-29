
class Option(object):

    def __init__(self, short, description, default=None, long=None):
        """
        Construct option
        :param short:       The short
        :param description: The description
        :param default:     The default value
        :param long:        The long
        """

        self.short = short
        self.description = description
        self.default = default
        self.long = long
        self.given = False
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
        if self._value is None:
            self._value = value
        else:
            if not isinstance(self._value, list):
                self._value = [self._value]
            self._value.append(value)
        self.given = True

    def reset(self):
        """
        Reset option
        :return:    void
        """

        self.given = False
        self._value = None
