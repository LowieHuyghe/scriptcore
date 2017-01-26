
from __future__ import absolute_import
from asciimatics.exceptions import NextScene


class FrameLogic(object):
    """
    Frame logic
    """

    def __init__(self, screen):
        """
        Constructor
        :param screen:
        """

        self._screen = screen

    def _change_scene(self, name):
        """
        Change scene
        :param name:
        :return:
        """

        raise NextScene(name)
