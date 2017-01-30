
from threading import Thread as BaseThread


class Thread(BaseThread):

    def __init__(self, *args, **kwargs):
        """
        Construct
        """

        super(Thread, self).__init__(*args, **kwargs)

        self.returncode = 0
        self._return = None

    def run(self):
        """
        Run
        """

        self._return = None

        try:
            if self.__target:
                self._return = self.__target(*self.__args, **self.__kwargs)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self.__target, self.__args, self.__kwargs

    def is_running(self):
        """
        Running
        :return:    Boolean
        """

        return True if self.isAlive() else False

    def communicate(self):
        """
        Communicate
        :return:    Out, err, exitcode
        """

        self.join()

        return self._return, None, self.returncode
