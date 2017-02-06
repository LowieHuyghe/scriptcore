
from scriptcore.testing.testcase import TestCase
from scriptcore.basescript import BaseScript
from scriptcore.cuiscript import CuiScript
import os.path


class TestCuiScript(TestCase):

    def set_up(self):
        """
        Set up the test
        :return:    void
        """

        super(TestCuiScript, self).set_up()

        BaseScript._current_script = None
        self.base_path = os.path.dirname(os.path.realpath(__file__))

    def test_script(self):
        """
        Test the script
        :return:    void
        """

        script = TestScript(self.base_path, self.rand_str(), self.rand_str())

        self.assert_is_instance(script, BaseScript)


class TestScript(CuiScript):
    pass
