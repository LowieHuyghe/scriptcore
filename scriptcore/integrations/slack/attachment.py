
class Attachment(object):

    def __init__(self,
                 fallback,
                 color=None,
                 pretext=None,
                 text=None,
                 author_name=None,
                 author_link=None,
                 author_icon=None,
                 title=None,
                 fields=None,
                 image_url=None,
                 thumb_url=None,
                 footer=None,
                 footer_icon=None,
                 ts=None):
        """
        Initiate the attachment
        :param fallback:    The fallback message
        :param color:       The color
        :param pretext:     The pretext
        :param text:        The text
        :param author_name: The author name
        :param author_link: The author link
        :param author_icon: The author icon
        :param title:       The title
        :param fields:      The fields
        :param image_url:   The image url
        :param thumb_url:   The thumbnail url
        :param footer:      The footer
        :param footer_icon: The footer icon
        :param ts:          The timestamp
        """

        super(Attachment, self).__init__()

        self._fallback = fallback

        self._color = color
        self._pretext = pretext
        self._text = text
        self._author_name = author_name
        self._author_link = author_link
        self._author_icon = author_icon
        self._title = title
        self._image_url = image_url
        self._thumb_url = thumb_url
        self._footer = footer
        self._footer_icon = footer_icon
        self._ts = ts

        if fields is None:
            fields = []
        self._fields = fields

    def add_field(self, field):
        """
        Add an field
        :param field:  The field
        :return:    void
        """

        self._fields.append(field)

    def get_payload(self):
        """
        Get the payload
        :return:    dict
        """

        payload = dict()

        # fallback
        payload['fallback'] = self._fallback

        # color
        if self._color is not None:
            payload['color'] = self._color

        # pretext
        if self._pretext is not None:
            payload['pretext'] = self._pretext

        # text
        if self._text is not None:
            payload['text'] = self._text

        # author_name
        if self._author_name is not None:
            payload['author_name'] = self._author_name

        # author_link
        if self._author_link is not None:
            payload['author_link'] = self._author_link

        # author_icon
        if self._author_icon is not None:
            payload['author_icon'] = self._author_icon

        # title
        if self._title is not None:
            payload['title'] = self._title

        # image_url
        if self._image_url is not None:
            payload['image_url'] = self._image_url

        # thumb_url
        if self._thumb_url is not None:
            payload['thumb_url'] = self._thumb_url

        # footer
        if self._footer is not None:
            payload['footer'] = self._footer

        # footer_icon
        if self._footer_icon is not None:
            payload['footer_icon'] = self._footer_icon

        # ts
        if self._ts is not None:
            payload['ts'] = self._ts

        # fields
        if self._fields:
            payload['fields'] = []
            for field in self._fields:
                payload['fields'].append(field.get_payload())

        return payload
