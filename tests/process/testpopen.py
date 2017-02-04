
from scriptcore.testing.testcase import TestCase
from scriptcore.process.popen import Popen
import subprocess


class TestPopen(TestCase):

    def test_popen(self):
        """
        Test Popen
        :return:    void
        """

        command, exp_out, exp_err, exp_exitcode = self._get_command_and_expected()

        process = Popen(command,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        shell=True)

        out, err, exitcode = process.communicate()
        self.assert_equal_deep(exp_out, out)
        self.assert_equal_deep(exp_err, err)
        self.assert_equal_deep(exp_exitcode, exitcode)

        self.assert_false(process.is_running())

    def _get_command_and_expected(self):
        """
        Get the command and expected
        :return: tuple
        """

        out = [
            'This is one hell of a test',
            'Vraiment!',
        ]
        err = [
            'Holly molly, and error!',
            'Is this right?'
        ]
        exitcode = 0

        command = ''
        for line in out:
            command += '%secho "%s"' % ('' if command == '' else ' && ', line)
        for line in err:
            command += '%s>&2 echo "%s"' % ('' if command == '' else ' && ', line)
        command += '%sexit %i' % ('' if command == '' else ' && ', exitcode)

        return command, out, err, exitcode
