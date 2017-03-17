

from scriptcore.testing.testcase import TestCase
from scriptcore.filesystem.mimetype import MimeType


class TestMimeType(TestCase):

    def test_guess_type(self):
        """
        Test guess type
        :return:    void
        """

        data = [
            ('.pdf',        'application/pdf'),
            ('.gdoc',       'application/vnd.google-apps.document'),
            ('.gdraw',      'application/vnd.google-apps.drawing'),
            ('.gsheet',     'application/vnd.google-apps.spreadsheet'),
            ('.gform',      'application/vnd.google-apps.form'),
            ('.gsite',      'application/vnd.google-apps.site'),
            ('.gmap',       'application/vnd.google-apps.map'),
            ('.gslides',    'application/vnd.google-apps.presentation'),
            ('.docx',       'application/vnd.openxmlformats-officedocument.wordprocessingml.document'),
            ('.xslx',       'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
            ('.pptx',       'application/vnd.openxmlformats-officedocument.presentationml.presentation'),
            ('.kml',        'application/vnd.google-earth.kml+xml')
        ]

        for extension, exp_mime_type in data:

            mime_type, encoding = MimeType.guess_type(extension)
            self.assert_equal(exp_mime_type, mime_type)

            mime_type, encoding = MimeType.guess_type('dummy.%s' % extension)
            self.assert_equal(exp_mime_type, mime_type)
