
from __future__ import absolute_import
from asciimatics.widgets import PopUpDialog as APopUpDialog


class PopUpDialog(APopUpDialog):

    def __init__(self,
                 screen,
                 text,
                 buttons,
                 on_click=None,
                 on_close=None):

        super(PopUpDialog, self).__init__(screen,
                                          text,
                                          buttons,
                                          on_close=lambda x: self._on_parent_click(x),
                                          has_shadow=True)
        self._on_click = on_click
        self._on_close = on_close

    def _on_parent_click(self, selected):
        """
        On parent click
        :param selected:
        :return:
        """

        if self._on_click:
            self._on_click(selected)

        if self._on_close:
            self._on_close()

    def close(self):
        """
        Close the popup
        :return:
        """

        if self in self._scene.effects:
            self._scene.remove_effect(self)

        if self._on_close:
            self._on_close()
