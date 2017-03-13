
from scriptcore.testing.testcase import TestCase
from scriptcore.integrations.slack.message import Message
from scriptcore.integrations.slack.attachment import Attachment


class TestMessage(TestCase):

    def test_props_and_payload(self):
        """
        Test properties and payload
        :return:    void
        """

        data = [
            {'text': self.rand_str(), 'attachments': None},
            {'text': self.rand_str(), 'attachments': []},
            {'text': self.rand_str(), 'attachments': [{'fallback': self.rand_str(), 'color': self.rand_str(), 'pretext': self.rand_str()}]}
        ]

        for row in data:
            text = row['text']
            if not row['attachments']:
                attachments = row['attachments']
            else:
                attachments = list(map(lambda attachment: Attachment(
                    attachment['fallback'],
                    color=attachment['color'],
                    pretext=attachment['pretext']
                ), row['attachments']))

            message = Message(
                text,
                attachments=attachments
            )

            self.assert_equal(text, message._text)
            if not attachments:
                self.assert_equal([], message._attachments)
            else:
                self.assert_equal(len(attachments), len(message._attachments))
                for i in range(0, len(attachments)):
                    self.assert_equal(attachments[i]._fallback, message._attachments[i]._fallback)
                    self.assert_equal(attachments[i]._color, message._attachments[i]._color)
                    self.assert_equal(attachments[i]._pretext, message._attachments[i]._pretext)

            payload = message.get_payload()

            self.assert_equal(text, payload['text'])
            if not attachments:
                self.assert_not_in('attachments', payload)
            else:
                self.assert_equal(len(attachments), len(payload['attachments']))
                for i in range(0, len(attachments)):
                    self.assert_equal(attachments[i]._fallback, payload['attachments'][i]['fallback'])
                    self.assert_equal(attachments[i]._color, payload['attachments'][i]['color'])
                    self.assert_equal(attachments[i]._pretext, payload['attachments'][i]['pretext'])
