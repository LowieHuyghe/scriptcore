
from scriptcore.testing.testcase import TestCase
from scriptcore.integrations.slack.attachment import Attachment
from scriptcore.integrations.slack.field import Field


class TestAttachment(TestCase):

    def test_props_and_payload(self):
        """
        Test properties and payload
        :return:    void
        """

        data = [
            {'fallback': self.rand_str(), 'color': self.rand_str(), 'pretext': self.rand_str(), 'text': self.rand_str(), 'author_name': self.rand_str(), 'author_link': self.rand_str(), 'author_icon': self.rand_str(), 'title': self.rand_str(), 'fields': None, 'image_url': self.rand_str(), 'thumb_url': self.rand_str(), 'footer': self.rand_str(), 'footer_icon': self.rand_str(), 'ts': self.rand_int(0, 1489063373)},
            {'fallback': self.rand_str(), 'color': self.rand_str(), 'pretext': self.rand_str(), 'text': self.rand_str(), 'author_name': self.rand_str(), 'author_link': self.rand_str(), 'author_icon': self.rand_str(), 'title': self.rand_str(), 'fields': [], 'image_url': self.rand_str(), 'thumb_url': self.rand_str(), 'footer': self.rand_str(), 'footer_icon': self.rand_str(), 'ts': self.rand_int(0, 1489063373)},
            {'fallback': self.rand_str(), 'color': self.rand_str(), 'pretext': self.rand_str(), 'text': self.rand_str(), 'author_name': self.rand_str(), 'author_link': self.rand_str(), 'author_icon': self.rand_str(), 'title': self.rand_str(), 'fields': [{'title': self.rand_str(), 'value': self.rand_str(), 'short': True}], 'image_url': self.rand_str(), 'thumb_url': self.rand_str(), 'footer': self.rand_str(), 'footer_icon': self.rand_str(), 'ts': self.rand_int(0, 1489063373)}
        ]

        for row in data:
            fallback = row['fallback']
            color = row['color']
            pretext = row['pretext']
            text = row['text']
            author_name = row['author_name']
            author_link = row['author_link']
            author_icon = row['author_icon']
            title = row['title']
            image_url = row['image_url']
            thumb_url = row['thumb_url']
            footer = row['footer']
            footer_icon = row['footer_icon']
            ts = row['ts']
            if not row['fields']:
                fields = row['fields']
            else:
                fields = list(map(lambda field: Field(
                    field['title'],
                    field['value'],
                    short=field['short']
                ), row['fields']))

            attachment = Attachment(
                fallback,
                color=color,
                pretext=pretext,
                text=text,
                author_name=author_name,
                author_link=author_link,
                author_icon=author_icon,
                title=title,
                fields=fields,
                image_url=image_url,
                thumb_url=thumb_url,
                footer=footer,
                footer_icon=footer_icon,
                ts=ts
            )

            self.assert_equal(fallback, attachment._fallback)
            self.assert_equal(color, attachment._color)
            self.assert_equal(pretext, attachment._pretext)
            self.assert_equal(text, attachment._text)
            self.assert_equal(author_name, attachment._author_name)
            self.assert_equal(author_link, attachment._author_link)
            self.assert_equal(author_icon, attachment._author_icon)
            self.assert_equal(title, attachment._title)
            self.assert_equal(image_url, attachment._image_url)
            self.assert_equal(thumb_url, attachment._thumb_url)
            self.assert_equal(footer, attachment._footer)
            self.assert_equal(footer_icon, attachment._footer_icon)
            self.assert_equal(ts, attachment._ts)
            if not fields:
                self.assert_equal([], attachment._fields)
            else:
                self.assert_equal(len(fields), len(attachment._fields))
                for i in range(0, len(fields)):
                    self.assert_equal(fields[i]._title, attachment._fields[i]._title)
                    self.assert_equal(fields[i]._value, attachment._fields[i]._value)
                    self.assert_equal(fields[i]._short, attachment._fields[i]._short)

            payload = attachment.get_payload()

            self.assert_equal(fallback, payload['fallback'])
            self.assert_equal(color, payload['color'])
            self.assert_equal(pretext, payload['pretext'])
            self.assert_equal(text, payload['text'])
            self.assert_equal(author_name, payload['author_name'])
            self.assert_equal(author_link, payload['author_link'])
            self.assert_equal(author_icon, payload['author_icon'])
            self.assert_equal(title, payload['title'])
            self.assert_equal(image_url, payload['image_url'])
            self.assert_equal(thumb_url, payload['thumb_url'])
            self.assert_equal(footer, payload['footer'])
            self.assert_equal(footer_icon, payload['footer_icon'])
            self.assert_equal(ts, payload['ts'])
            if not fields:
                self.assert_not_in('fields', payload)
            else:
                self.assert_equal(len(fields), len(payload['fields']))
                for i in range(0, len(fields)):
                    self.assert_equal(fields[i]._title, payload['fields'][i]['title'])
                    self.assert_equal(fields[i]._value, payload['fields'][i]['value'])
                    self.assert_equal(fields[i]._short, payload['fields'][i]['short'])
