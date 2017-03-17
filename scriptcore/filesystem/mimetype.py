
import mimetypes


class MimeType(object):

    _initiated = False

    @staticmethod
    def guess_type(filename):
        """
        Guess type
        :param filename:    File name
        :return:            tuple(type, encoding)
        """

        MimeType._initiate()

        return mimetypes.guess_type('dummy.%s' % filename)

    @staticmethod
    def _initiate():
        """
        Initiate
        :return:    void
        """

        if MimeType._initiated:
            return

        mimetypes.init()
        mimetypes.add_type('application/vnd.google-apps.document', '.gdoc')
        mimetypes.add_type('application/vnd.google-apps.drawing', '.gdraw')
        mimetypes.add_type('application/vnd.google-apps.spreadsheet', '.gsheet')
        mimetypes.add_type('application/vnd.google-apps.form', '.gform')
        mimetypes.add_type('application/vnd.google-apps.site', '.gsite')
        mimetypes.add_type('application/vnd.google-apps.map', '.gmap')
        mimetypes.add_type('application/vnd.google-apps.presentation', '.gslides')
        mimetypes.add_type('application/vnd.openxmlformats-officedocument.wordprocessingml.document', '.docx')
        mimetypes.add_type('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', '.xslx')
        mimetypes.add_type('application/vnd.openxmlformats-officedocument.presentationml.presentation', '.pptx')
        mimetypes.add_type('application/vnd.google-earth.kml+xml', '.kml')

        MimeType._initiated = True
