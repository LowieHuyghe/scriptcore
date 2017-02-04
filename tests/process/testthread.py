
from scriptcore.testing.testcase import TestCase
from scriptcore.process.thread import Thread


class TestThread(TestCase):

    def test_thread(self):
        """
        Test Thread
        :return:    void
        """

        target, exp_out, exp_err, exp_exitcode = self._get_target_and_expected()

        thread = Thread(target=target, args=())

        self.assert_false(thread.is_running())
        thread.start()

        out, err, exitcode = thread.communicate()
        self.assert_equal_deep(exp_out, out)
        self.assert_equal_deep(exp_err, err)
        self.assert_equal_deep(exp_exitcode, exitcode)

        self.assert_false(thread.is_running())

    def _get_target_and_expected(self):
        """
        Get the target and expected
        :return: tuple
        """

        out = [
            'This is one hell of a test',
            'Vraiment!',
        ]
        err = None
        exitcode = 0

        def my_target():
            return out

        return my_target, out, err, exitcode
