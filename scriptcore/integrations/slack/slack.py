
from scriptcore.integrations.slack.message import Message
from scriptcore.integrations.slack.attachment import Attachment
from scriptcore.encoding.encoding import Encoding
import sys
if sys.version_info < (3, 0):
    from urllib2 import Request, urlopen
else:
    from urllib.request import Request, urlopen
import json


class Slack(object):

    def __init__(self, web_hook_url, channel=None, username=None, icon=None):
        """
        Initiate the object
        :param web_hook_url:    The webhook url
        :param channel:         A custom channel
        :param username:        A custom username
        :param icon:            A custom icon
        """

        super(Slack, self).__init__()

        self._web_hook_url = web_hook_url
        self._channel = channel
        self._username = username
        self._icon = icon

    def send(self, message):
        """
        Send a message
        :param message: An instance of a message
        :return:        Success
        """

        payload = self._get_payload(message)

        data = json.dumps(payload).encode('utf-8')
        request = Request(self._web_hook_url, data=data)
        response = urlopen(request)

        return response.getcode() == 200

    def _get_payload(self, message):
        """
        Get the payload
        :param message: Message to send
        :return:        dict
        """

        payload = message.get_payload()

        # channel
        if self._channel is not None:
            payload['channel'] = self._channel

        # username
        if self._username is not None:
            payload['username'] = self._username

        # icon
        if self._icon is not None:
            if self._icon.startswith(':') and self._icon.endswith(':'):
                payload['icon_emoji'] = self._icon
            else:
                payload['icon_url'] = self._icon

        return payload

    def send_message(self, text, sub_title=None, sub_text=None, color=None):
        """
        Send a simple message
        :param text:            The text to send
        :param sub_title:       The title of the attachment
        :param sub_text:        The text of the attachment
        :param color:           The color when subtext is set
        :return:                Success
        """

        message = Message(text)

        if sub_title is not None or sub_text is not None:
            attachment = Attachment(sub_title, title=sub_title, text=sub_text, color=color)
            message.add_attachment(attachment)

        return self.send(message)
