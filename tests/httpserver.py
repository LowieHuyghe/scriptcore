
import sys
if sys.version_info < (3, 0):
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer as OriginalHTTPServer
else:
    from http.server import HTTPServer as OriginalHTTPServer, SimpleHTTPRequestHandler
from scriptcore.encoding.encoding import Encoding
import os.path
import ssl
import threading
from time import sleep


class HttpServer(object):

    def __init__(self, host='0.0.0.0', port=18888):
        """
        Initiate the server object
        :param host:    The host
        :type  host:    str
        :param port:    The port
        :type  port:    int
        """

        self.host = host
        self.port = port

        self._server = None
        self._thread = None
        self._data = []

    def start(self):
        """
        Start the server
        """

        if self._thread:
            return False

        self._data = []

        self._server = HTTPServer((self.host, self.port), HttpServerHandler)

        dir_path = os.path.dirname(os.path.realpath(__file__))
        key_file = os.path.join(dir_path, 'httpserver-cert.key')
        cert_file = os.path.join(dir_path, 'httpserver-cert.crt')
        self._server.socket = ssl.wrap_socket(self._server.socket,
                                              keyfile=key_file,
                                              certfile=cert_file,
                                              server_side=True)
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context

        self._thread = threading.Thread(target=self._server.serve_forever)
        self._thread.start()

        return True

    def stop(self):
        """
        Stop the server
        """

        if not self._thread:
            return False

        sleep(0.01)
        self._data = self._server.data

        self._server.shutdown()
        self._thread = None
        self._server = None

        return True

    def get_data(self):
        """
        Get the data
        """

        if self._server:
            sleep(0.01)
            return self._server.data
        else:
            return self._data


class HTTPServer(OriginalHTTPServer, object):

    def __init__(self, *args, **kwargs):
        """
        Initiate the server
        """

        super(HTTPServer, self).__init__(*args, **kwargs)

        self.data = []


class HttpServerHandler(SimpleHTTPRequestHandler, object):

    def do_POST(self):
        f = self.send_head()

        data = Encoding.normalize(self.rfile.read(int(self.headers['Content-Length'])))
        self.server.data.append(data)

        if f:
            try:
                self.copyfile(f, self.wfile)
            finally:
                f.close()
