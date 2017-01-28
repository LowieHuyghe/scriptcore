
from __future__ import absolute_import
from asciimatics.widgets import Frame as AFrame
from scriptcore.console.asciimatics.widgets.divider import Divider
from scriptcore.console.asciimatics.widgets.label import Label
from scriptcore.console.asciimatics.widgets.layout import Layout


class Frame(AFrame):

    def __init__(self, screen, title, on_load=None):
        """
        Initiate the frame
        :param screen:
        :param title:
        :param on_load:
        """
        super(Frame, self).__init__(screen,
                                    screen.height / 5 * 4,
                                    screen.width / 5 * 4,
                                    title=title,
                                    on_load=on_load)

    def _add_header(self, label):
        """
        Add a header
        :param label:
        :return:
        """

        header = Layout([1])
        self.add_layout(header)
        header.add_widget(Label(label))

    def _add_divider(self):
        """
        Add a divider
        :return:
        """

        divider = Layout([1])
        self.add_layout(divider)
        divider.add_widget(Divider())

    def add_effect_to_scene(self, effect):
        """
        Add an Effect to the scene.
        :param effect: The Effect to be added.
        """

        self._scene.add_effect(effect)
