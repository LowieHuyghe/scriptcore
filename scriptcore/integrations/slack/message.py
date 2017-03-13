
class Message(object):

    def __init__(self, text=None, attachments=None):
        """
        Initiate the message
        :param text:        The text to display
        :param attachments: The attachments
        """

        super(Message, self).__init__()

        self._text = text

        if attachments is None:
            attachments = []
        self._attachments = attachments

    def add_attachment(self, attachment):
        """
        Add an attachment
        :param attachment:  The attachment
        :return:    void
        """

        self._attachments.append(attachment)

    def get_payload(self):
        """
        Get the payload to send
        :return:    dict
        """

        payload = dict()

        # text
        if self._text is not None:
            payload['text'] = self._text

        # attachments
        if self._attachments:
            payload['attachments'] = []
            for attachment in self._attachments:
                payload['attachments'].append(attachment.get_payload())

        return payload
