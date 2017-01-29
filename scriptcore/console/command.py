
class Command(object):

    def __init__(self, command, description, callback):
        """
        Construct command
        :param command:     The command
        :param description: The description
        :param callback:    The callback
        """

        self.command = command
        self.description = description
        self.callback = callback
        self.given = False
        self.arguments = None

    def reset(self):
        """
        Reset option
        :return:    void
        """

        self.given = False
        self.arguments = None
