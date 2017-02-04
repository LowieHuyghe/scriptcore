
from threading import Thread as BaseThread


class Thread(BaseThread):

    def __init__(self, *args, **kwargs):
        """
        Construct
        """

        super(Thread, self).__init__(*args, **kwargs)

        self._out = None
        self._err = None
        self.returncode = 0

    def run(self):
        """
        Run
        """

        self._out = None
        self._err = None
        self.returncode = 0

        try:
            self.__target
            try:
                if self.__target:
                    self._out = self.__target(*self.__args, **self.__kwargs)
            except Exception as e:
                self._err = e
                self.returncode = 1
            finally:
                # Avoid a refcycle if the thread is running a function with
                # an argument that has a member that points to the thread.
                del self.__target, self.__args, self.__kwargs
        except AttributeError:
            try:
                if self._target:
                    self._out = self._target(*self._args, **self._kwargs)
            except Exception as e:
                self._err = e
                self.returncode = 1
            finally:
                # Avoid a refcycle if the thread is running a function with
                # an argument that has a member that points to the thread.
                del self._target, self._args, self._kwargs

    def is_running(self):
        """
        Running
        :return:    Boolean
        """

        return self.isAlive()

    def communicate(self):
        """
        Communicate
        :return:    Out, err, exitcode
        """

        self.join()

        return self._out, self._err, self.returncode
