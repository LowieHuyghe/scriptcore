
class Encoding(object):

    @staticmethod
    def to_ascii(value):
        """
        To ascii
        :param value:   The value
        :return:        The processed value
        """

        # Dict
        if isinstance(value, dict):
            processed_value = {}
            for key in value:
                if isinstance(key, unicode):
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
        elif isinstance(value, unicode):
            processed_value = value.encode('ascii')

        else:
            processed_value = value

        return processed_value
