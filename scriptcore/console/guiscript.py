
from __future__ import absolute_import
from abc import ABCMeta, abstractmethod
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.exceptions import ResizeScreenError


class GuiScript(object):

    __metaclass__ = ABCMeta

    def __init__(self, stop_on_resize=True, catch_interrupt=True):
        """
        Construct the object
        """

        self._screen = None
        self._scenes = []
        self._last_scene = None
        self._stop_on_resize = stop_on_resize
        self._catch_interrupt = catch_interrupt

    def _on_screen_made(self, screen):
        """
        The screen has been made
        :param screen:  The screen
        :type  screen:  Screen
        :return:        void
        """

        self._screen = screen
        self._scenes = []
        self._init()
        self._screen.play(self._scenes, stop_on_resize=self._stop_on_resize, start_scene=self._last_scene)

    def run(self):
        """
        Run the script
        """

        try:
            Screen.wrapper(self._on_screen_made, catch_interrupt=self._catch_interrupt)
        except ResizeScreenError as e:
            self._last_scene = e.scene

            self.run()

    def _add_scene(self, effects, duration=-1, name=None):
        """
        Add a scene
        :param effects:     The effects
        :param duration:    The duration
        :param name:        The name
        :return:            void
        """

        self._scenes.append(Scene(effects, duration=duration, name=name))

    @abstractmethod
    def _init(self):
        """
        Initiate the screen
        """
        pass
