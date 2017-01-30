
from scriptcore.process.popen import Popen
from scriptcore.console.output.output import Output
import subprocess
import time


class Execute(object):

    def __init__(self, output=None):
        """
        Construct
        :param output:  The output
        """

        if output is None:
            self._output = Output()
        else:
            self._output = output

    def __call__(self, command):
        """
        Call
        :param command: Command to call
        :return:        Out, err, exitcode
        """

        return self.execute(command)

    def execute(self, command, return_process=False):
        """
        Execute
        :param command:         The command
        :param return_process:  The callback if command should be ran in the background
        :return:                Out, err, exitcode
        """

        process = Popen(command,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        shell=True)

        if return_process:
            return process
        else:
            return process.communicate()

    def process(self, command):
        """
        Get the process
        :param command: The command
        :return:        Popen
        """

        return self.execute(command, return_process=True)

    def spinner(self, command, description, success=None, error=None):
        """
        Execute with spinner
        :param command:     Command
        :param description: Description
        :param success:     Success-message
        :param error:       Error-message
        :return:            Out, err, exitcode
        """

        process = self.process(command)

        spinner_index = 0
        while process.is_running():
            spinner = ['-', '\\', '|', '/'][spinner_index % 4]

            self._output.info('%s: %s' % (description, spinner), newline=False)

            spinner_index += 1
            time.sleep(0.1)

        if success and error:
            if process.returncode == 0:
                self._output.success(success)
            else:
                self._output.error(error)

        return process.communicate()
