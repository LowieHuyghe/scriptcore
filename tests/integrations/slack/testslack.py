
from scriptcore.testing.testcase import TestCase
from scriptcore.integrations.slack.slack import Slack
from scriptcore.integrations.slack.message import Message
from tests.httpserver import HttpServer
import json


class TestSlack(TestCase):

    def set_up(self):
        """
        Set up the test
        :return:    void
        """

        super(TestSlack, self).set_up()

        self._server = HttpServer()
        self._server.start()

        self._web_hook_url = 'https://%s:%s' % (self._server.host, self._server.port)

    def tear_down(self):
        """
        Tear down the test case
        """

        super(TestSlack, self).tear_down()

        self._server.stop()

    def test_send(self):
        """
        Test sending
        :return:    void
        """

        data = {
            'username': 'Botty McBotFace',
            'icon': ':sheep:',
            'text': 'This is a test'
        }
        slack = Slack(self._web_hook_url, username=data['username'], icon=data['icon'])
        message = Message(data['text'])

        self.assert_true(slack.send(message))

        self.assert_equal(1, len(self._server.get_data()))
        for response_data_raw in self._server.get_data():
            response_data = json.loads(response_data_raw)

            self.assert_equal(data['username'], response_data['username'])
            self.assert_equal(data['icon'], response_data['icon_emoji'])
            self.assert_equal(data['text'], response_data['text'])

    def test_send_message(self):
        """
        Test sending message
        :return:    void
        """

        data = {
            'username': 'Botty McBotFace',
            'icon': ':sheep:',
            'text': 'This is a test',
            'sub_title': 'This is a subtitle',
            'sub_text': 'This is a subtext',
            'color': 'danger'
        }
        slack = Slack(self._web_hook_url, username=data['username'], icon=data['icon'])

        self.assert_true(slack.send_message(data['text'], sub_title=data['sub_title'], sub_text=data['sub_text'], color=data['color']))

        self.assert_equal(1, len(self._server.get_data()))
        for response_data_raw in self._server.get_data():
            response_data = json.loads(response_data_raw)

            self.assert_equal(data['username'], response_data['username'])
            self.assert_equal(data['icon'], response_data['icon_emoji'])
            self.assert_equal(data['text'], response_data['text'])

            self.assert_in('attachments', response_data)
            self.assert_equal(1, len(response_data['attachments']))
            for attachment in response_data['attachments']:
                self.assert_equal(data['sub_title'], attachment['fallback'])
                self.assert_equal(data['sub_title'], attachment['title'])
                self.assert_equal(data['sub_text'], attachment['text'])
                self.assert_equal(data['color'], attachment['color'])
