
from scriptcore.testing.testcase import TestCase
from scriptcore.integrations.slack.field import Field


class TestField(TestCase):

    def test_props_and_payload(self):
        """
        Test properties and payload
        :return:    void
        """

        data = [
            {'title': self.rand_str(), 'value': self.rand_str(), 'short': True},
            {'title': self.rand_str(), 'value': self.rand_str(), 'short': False},
            {'title': self.rand_str(), 'value': self.rand_str(), 'short': True}
        ]

        for row in data:
            title = row['title']
            value = row['value']
            short = row['short']

            field = Field(
                title,
                value,
                short=short
            )

            self.assert_equal(title, field._title)
            self.assert_equal(value, field._value)
            self.assert_equal(short, field._short)

            payload = field.get_payload()

            self.assert_equal(title, payload['title'])
            self.assert_equal(value, payload['value'])
            self.assert_equal(short, payload['short'])
