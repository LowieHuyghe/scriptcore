
from scriptcore.config.config import Config
import os.path


class BaseScript(object):

    _current_script = None

    @staticmethod
    def current_script():
        """
        Get the current script
        :return:
        """
        return BaseScript._current_script

    def __init__(self, base_path):
        """
        Construct the script
        :param base_path:   The base path
        """

        BaseScript._current_script = self

        self._base_path = base_path
        self.config = Config()

    def get_path(self, filename):
        """
        Get path from the filename
        :param filename:
        :return:
        """

        if filename[0:1] == os.path.sep:
            filename = filename[1::]

        return os.path.join(self._base_path, filename)
