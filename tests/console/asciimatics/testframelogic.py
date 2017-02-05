
from scriptcore.testing.testcase import TestCase
from scriptcore.console.asciimatics.framelogic import FrameLogic
from asciimatics.exceptions import NextScene


class TestFrameLogic(TestCase):

    def test_frame_logic(self):
        """
        Test the frame_logic
        :return:    void
        """

        screen = self.rand_str()

        frame_logic = FrameLogic(screen)

        self.assert_equal(screen, frame_logic._screen)
        with self.assert_raises(NextScene):
            frame_logic._change_scene(self.rand_str())
