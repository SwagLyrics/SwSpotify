import json
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

"""
Module to collect the current track data from the chrome extension if open as dict, else return None
"""


class Server(HTTPServer):

    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True):
        super().__init__(server_address, RequestHandlerClass, bind_and_activate=True)
        self.data = {}

    def finish_request(self, request, client_address):
        # override finish_request to capture the data from the post request
        self.data = self.RequestHandlerClass(request, client_address, self).data


class RequestHandler(BaseHTTPRequestHandler):
    """
    create a request handler to tell the HTTPServer how to respond to different requests
    """

    def _set_headers(self):
        self.send_response(200)  # send response ok
        # CORS headers
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Methods", "OPTIONS, POST")
        self.send_header("Access-Control-Allow-Origin", "chrome-extension://bobgjepgcclcojkiolmcjehhmmhnpcic")
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()
        self.data = {}  # set data to empty on preflight request

    def do_POST(self):
        # Handled posted data
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.data = json.loads(post_data)  # load json string into dict
        # Send response to cleanup request and not error client
        self._set_headers()
        self.wfile.write(b'ok')  # send bytestring to client

    def log_message(self, *args):
        # override logging requests to stderr for smooth interface
        pass


def server():
    # setup server and receive 2 requests
    server_address = ('localhost', 5043)

    httpd = Server(server_address, RequestHandler)
    httpd.socket.settimeout(1.3)

    httpd.handle_request()  # receive OPTIONS request for preflight
    httpd.handle_request()  # receive POST from client: will be collected

    # check weather the dict is empty if it is return None
    if len(httpd.data) == 0:
        return None
    return httpd.data  # return data object to wrapper function


def wrapper(func, data):
    data.append(func())  # Append the return value of the web server to the list


def run():
    """
    Entry point for spotify.py
    """
    data = []
    t = threading.Thread(target=wrapper, args=(server, data))  # Spawn wrapper thread to run web server
    t.start()
    t.join()  # Sync the threads so we can exit cleanly
    return data[0]  # Return none or the dictionary


if __name__ == "__main__":
    x = run()
    print(x)
