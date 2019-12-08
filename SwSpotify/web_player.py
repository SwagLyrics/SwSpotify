import ctypes
import json
import threading
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

global data

"""
Module to collect the current track data from the chrome extension if open.
"""


class StoppableThread(threading.Thread):
    """
    Thread class with stop method
    """

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        server()

    def get_id(self):
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                                                         ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()

    def do_POST(self):
        global data
        # Handled posted data
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        # Send response
        self._set_headers()
        self.wfile.write(b'test')
        raise SystemExit


def server():
    server_address = ('localhost', 5042)
    httpd = HTTPServer(server_address, S)
    httpd.serve_forever()


def run():
    """
    Returns track information to spotify.py
    """
    global data
    t1 = StoppableThread("Thread 1")
    t1.start()
    time.sleep(2)
    return data['title'], data['artist']
