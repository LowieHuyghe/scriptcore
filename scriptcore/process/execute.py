
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
        :return:
        """

        process = subprocess.Popen(command.split(' '),
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

        out, err = process.communicate()

        return out.strip().split('\n')
