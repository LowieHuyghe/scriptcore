
class UnknownCommandError(RuntimeError):

    def __init__(self, command):
        """
        Initiate the error
        :param command:  The command
        """

        super(UnknownCommandError, self).__init__('Unknown command "%s" given' % command)
