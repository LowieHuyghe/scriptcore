
from scriptcore.process.popen import Popen
from scriptcore.process.thread import Thread
from scriptcore.console.output.output import Output
import subprocess
import time
import types


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

    def __call__(self, command_target, arguments=()):
        """
        Call
        :param command_target:  The command or target
        :param arguments:       Arguments for target
        :return:                Out, err, exitcode
        """

        return self.execute(command_target, arguments=arguments)

    def execute(self, command_target, arguments=(), return_process=False):
        """
        Execute
        :param command_target:  The command or target
        :param arguments:       Arguments for target
        :param return_process:  The callback if command should be ran in the background
        :return:                Out, err, exitcode
        """

        if isinstance(command_target, types.FunctionType) or isinstance(command_target, types.MethodType):
            process = Thread(target=command_target, args=arguments)
            process.start()
        else:
            process = Popen(command_target,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True)

        if return_process:
            return process
        else:
            return process.communicate()

    def process(self, command_target, arguments=()):
        """
        Get the process
        :param command_target:  The command or target
        :param arguments:       Arguments for target
        :return:                Popen or Thread
        """

        return self.execute(command_target, arguments=arguments, return_process=True)

    def spinner(self, command_target, description, arguments=(), success=None, error=None):
        """
        Execute with spinner
        :param command_target:  The command or target
        :param description:     Description
        :param arguments:       Arguments for target
        :param success:         Success-message
        :param error:           Error-message
        :return:                Out, err, exitcode
        """

        process = self.process(command_target, arguments=arguments)

        spinner_index = 0
        while process.is_running():
            spinner = ['-', '\\', '|', '/'][spinner_index % 4]

            self._output('%s: %s' % (description, spinner), newline=False)

            spinner_index += 1
            time.sleep(0.1)

        if success and error:
            if process.returncode == 0:
                self._output.success(success)
            else:
                self._output.error(error)

        return process.communicate()
