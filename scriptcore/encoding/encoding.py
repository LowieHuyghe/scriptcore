
class Encoding(object):

    @staticmethod
    def normalize(value):
        """
        Normalize value
        :param value:   The value
        :return:        The processed value
        """

        # Python 2 vs Python 3
        try:
            unicode
        except NameError:
            return value

        return Encoding.to_ascii(value)

    @staticmethod
    def to_ascii(value):
        """
        To ascii
        :param value:   The value
        :return:        The processed value
        """

        # Python 2 vs Python 3
        try:
            unicode_or_str = unicode
        except NameError:
            unicode_or_str = str

        # Dict
        if isinstance(value, dict):
            processed_value = {}
            for key in value:
                if isinstance(key, unicode_or_str):
                    processed_key = key.encode('ascii')
                else:
                    processed_key = key
                processed_value[processed_key] = Encoding.to_ascii(value[key])

        # List
        elif isinstance(value, list):
            processed_value = []
            for value in value:
                processed_value.append(Encoding.to_ascii(value))

        # Unicode
        elif isinstance(value, unicode_or_str):
            processed_value = value.encode('ascii')

        else:
            processed_value = value

        return processed_value
