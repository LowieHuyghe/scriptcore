
import subprocess


class Execute(object):

    def __call__(self, command):
        """
        Call
        :param command: Command to call
        :return:
        """

        return self.execute(command)

    def execute(self, command):
        """
        Execute
        :param command: The command
        :return:        Out, err, exitcode
        """

        process = subprocess.Popen(command,
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   shell=True)

        out, err = process.communicate()

        out = out.strip().split('\n')
        err = err.strip().split('\n')
        exitcode = process.returncode

        return out, err, exitcode
