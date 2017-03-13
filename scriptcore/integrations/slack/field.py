
class Field(object):

    def __init__(self, title, value, short=False):
        """
        Initiate the field
        :param title:   The title
        :param value:   The value
        :param short:   Short or not
        """

        super(Field, self).__init__()

        self._title = title
        self._value = value
        self._short = short

    def get_payload(self):
        """
        Get the payload
        :return:    dict
        """

        payload = dict()

        # title
        payload['title'] = self._title

        # value
        payload['value'] = self._value

        # short
        payload['short'] = self._short

        return payload
