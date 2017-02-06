
class UnknownOptionError(RuntimeError):

    def __init__(self, option):
        """
        Initiate the error
        :param option:  The option
        """

        super(UnknownOptionError, self).__init__('Unknown option "%s" given' % option)
