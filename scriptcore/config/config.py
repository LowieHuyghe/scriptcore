
try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser
import json
from scriptcore.encoding.encoding import Encoding


class Config(object):

    def __init__(self):
        """
        Construct the config instance
        """

        self._config = {}

    def __call__(self, key, default=None):
        """
        Call instance
        :param key:     The key
        :param default: The default value
        :return:        The value
        """

        return self.get(key, default)

    def get(self, key, default=None):
        """
        Get a config value
        :param key:     The key
        :param default: The default value
        :return:        The value
        """

        parts = key.split('.')

        value = self._config
        for part in parts:
            if part in value:
                value = value[part]
            else:
                return default

        return value

    def load_from_ini(self, filename, namespace=None):
        """
        Load config from ini-file
        :param filename:    The file name
        :param namespace:   A optional namespace
        :return:
        """

        config = ConfigParser.ConfigParser()
        config.read(filename)

        if namespace is not None:
            if namespace.lower() not in self._config:
                self._config[namespace.lower()] = {}

        for section in config.sections():
            for option in config.options(section):
                if namespace is None:
                    if section.lower() not in self._config:
                        self._config[section.lower()] = {}
                else:
                    if section.lower() not in self._config[namespace.lower()]:
                        self._config[namespace.lower()][section.lower()] = {}

                try:
                    value = config.getint(section, option)
                except ValueError:
                    try:
                        value = config.getfloat(section, option)
                    except ValueError:
                        try:
                            value = config.getboolean(section, option)
                        except ValueError:
                            value = config.get(section, option)

                if namespace is None:
                    self._config[section.lower()][option.lower()] = value
                else:
                    self._config[namespace.lower()][section.lower()][option.lower()] = value

    def load_from_json(self, filename, namespace=None):
        """
        Load config from json-file
        :param filename:    The file name
        :param namespace:   A optional namespace
        :return:
        """

        with open(filename) as json_file:
            json_content = Encoding.to_ascii(json.load(json_file))

        if namespace is not None:
            if namespace.lower() not in self._config:
                self._config[namespace.lower()] = {}

        for key in json_content:
            if namespace is None:
                self._config[key] = json_content[key]
            else:
                self._config[namespace.lower()][key] = json_content[key]
