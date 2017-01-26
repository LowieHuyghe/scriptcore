
from __future__ import absolute_import
from asciimatics.widgets import CheckBox as ACheckBox


class CheckBox(ACheckBox):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        # Only trigger the notification after we've changed the value.
        old_value = self._value
        self._value = new_value if new_value else False
        if old_value != self._value and self._on_change:
            self._on_change(self)
