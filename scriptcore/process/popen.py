
from subprocess import Popen as BasePopen
from scriptcore.encoding.encoding import Encoding


class Popen(BasePopen):

    def communicate(self, input=None):
        """
        Communicate
        :param input:   Optional input
        :return:        Out, err, exitcode
        """

        out, err = super(Popen, self).communicate(input=input)

        out = Encoding.normalize(out).strip().split('\n')
        err = Encoding.normalize(err).strip().split('\n')

        return out, err, self.returncode

    def is_running(self):
        """
        Running
        :return:    Boolean
        """

        return True if self.poll() is None else False
