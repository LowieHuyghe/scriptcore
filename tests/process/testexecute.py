
from scriptcore.testing.testcase import TestCase
from scriptcore.process.execute import Execute
try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO
import sys


class TestExecute(TestCase):

    def test_execute_command(self):
        """
        Test execute command function
        :return:    void
        """

        command, exp_out, exp_err, exp_exitcode = self._get_command_and_expected()

        execute = Execute()

        out, err, exitcode = execute.execute(command)
        self.assert_equal_deep(exp_out, out)
        self.assert_equal_deep(exp_err, err)
        self.assert_equal_deep(exp_exitcode, exitcode)

        out, err, exitcode = execute(command)
        self.assert_equal_deep(exp_out, out)
        self.assert_equal_deep(exp_err, err)
        self.assert_equal_deep(exp_exitcode, exitcode)

    def test_execute_target(self):
        """
        Test execute target function
        :return:    void
        """

        target, exp_out, exp_err, exp_exitcode = self._get_target_and_expected()

        execute = Execute()

        out, err, exitcode = execute.execute(target)
        self.assert_equal_deep(exp_out, out)
        self.assert_equal_deep(exp_err, err)
        self.assert_equal_deep(exp_exitcode, exitcode)

        out, err, exitcode = execute(target)
        self.assert_equal_deep(exp_out, out)
        self.assert_equal_deep(exp_err, err)
        self.assert_equal_deep(exp_exitcode, exitcode)

    def test_execute_target_err(self):
        """
        Test execute target err function
        :return:    void
        """

        target, exp_out, exp_err, exp_exitcode = self._get_target_err_and_expected()

        execute = Execute()

        out, err, exitcode = execute.execute(target)
        self.assert_equal_deep(exp_out, out)
        self.assert_equal_deep(exp_err, err)
        self.assert_equal_deep(exp_exitcode, exitcode)
        self.assert_equal(str(exp_err), str(err))

        out, err, exitcode = execute(target)
        self.assert_equal_deep(exp_out, out)
        self.assert_equal_deep(exp_err, err)
        self.assert_equal_deep(exp_exitcode, exitcode)
        self.assert_equal(str(exp_err), str(err))

    def test_execute_target_args(self):
        """
        Test execute target args function
        :return:    void
        """

        target, args, exp_out, exp_err, exp_exitcode = self._get_target_args_and_expected()

        execute = Execute()

        out, err, exitcode = execute.execute(target, arguments=args)
        self.assert_equal_deep(exp_out, out)
        self.assert_equal_deep(exp_err, err)
        self.assert_equal_deep(exp_exitcode, exitcode)

        out, err, exitcode = execute.execute(target, arguments=args)
        self.assert_equal_deep(exp_out, out)
        self.assert_equal_deep(exp_err, err)
        self.assert_equal_deep(exp_exitcode, exitcode)

    def test_process(self):
        """
        Test process function
        :return:    void
        """

        command, exp_out, exp_err, exp_exitcode = self._get_command_and_expected()

        execute = Execute()

        process = execute.process(command)
        out, err, exitcode = process.communicate()
        self.assert_equal_deep(exp_out, out)
        self.assert_equal_deep(exp_err, err)
        self.assert_equal_deep(exp_exitcode, exitcode)

    def test_spinner(self):
        """
        Test spinner function
        :return:    void
        """

        command, exp_out, exp_err, exp_exitcode = self._get_command_and_expected()

        execute = Execute()

        out, err, exitcode = execute.spinner(command, 'Spinner test')
        self.assert_equal_deep(exp_out, out)
        self.assert_equal_deep(exp_err, err)
        self.assert_equal_deep(exp_exitcode, exitcode)

    def test_spinner_success_error(self):
        """
        Test spinner success and error function
        :return:    void
        """

        success = self.rand_str()
        error = self.rand_str()

        execute = Execute()

        # Success message
        command, exp_out, exp_err, exp_exitcode = self._get_command_and_expected()
        execute.spinner(command, 'Spinner test', success=success, error=error)
        self.assert_in(success, self.stdout.getvalue())
        self.assert_not_in(error, self.stdout.getvalue())

        # Reset
        self.stdout = sys.stdout = StringIO()

        # Error message
        command, exp_out, exp_err, exp_exitcode = self._get_command_err_and_expected()
        execute.spinner(command, 'Spinner test', success=success, error=error)
        self.assert_not_in(success, self.stdout.getvalue())
        self.assert_in(error, self.stdout.getvalue())

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

    def _get_command_err_and_expected(self):
        """
        Get the command err and expected
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
        exitcode = 1

        command = ''
        for line in out:
            command += '%secho "%s"' % ('' if command == '' else ' && ', line)
        for line in err:
            command += '%s>&2 echo "%s"' % ('' if command == '' else ' && ', line)
        command += '%sexit %i' % ('' if command == '' else ' && ', exitcode)

        return command, out, err, exitcode

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

    def _get_target_err_and_expected(self):
        """
        Get the target err and expected
        :return: tuple
        """

        out = None
        err = RuntimeError('Holly molly, and error!')
        exitcode = 1

        def my_target():
            raise err

        return my_target, out, err, exitcode

    def _get_target_args_and_expected(self):
        """
        Get the target args and expected
        :return: tuple
        """

        args = (
            [
                'This is one hell of a test',
                'Vraiment!',
            ],
            1,
            True,
        )
        out = args
        err = None
        exitcode = 0

        def my_target(arg1, arg2, arg3):
            return (arg1, arg2, arg3)

        return my_target, args, out, err, exitcode
