
from threading import Thread as BaseThread


class Thread(BaseThread):

    def __init__(self, *args, **kwargs):
        """
        Construct
        """

        super(Thread, self).__init__(*args, **kwargs)

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

    def join(self):
        """
        Join
        :return:    The return value
        """

        super(Thread, self).join()

        return self._return
