
class Option(object):

    type_list = 'list'

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
        self.long = long
        self.given = False
        self.type = type
        if self.type == Option.type_list and default is None:
            self.default = []
        elif self.type == Option.type_list and not isinstance(default, list):
            self.default = [default]
        else:
            self.default = default
        if self.type == Option.type_list:
            self._value = []
        else:
            self._value = None

    @property
    def value(self):
        if self.given and self._value:
            return self._value
        return self.default

    @value.setter
    def value(self, value):
        self._value = value
        self.given = True

    def add_value(self, value):
        if self.type == Option.type_list:
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
        if self.type == Option.type_list:
            self._value = []
            if self.default is None:
                self.default = []
            elif not isinstance(self.default, list):
                self.default = [self.default]
        else:
            self._value = None
            if not self.default:
                self.default = None
            elif isinstance(self.default, list):
                self.default = self.default[0]
