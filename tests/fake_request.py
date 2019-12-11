import threading
import requests


def send_fake_request():
    data = '''{"title": "Hello","artist": "Adele","playState": "Pause"}'''
    s = requests.session()
    s.headers.update({"Content-type": "application/json"})
    s.post("http://127.0.0.1:5043/getSong", data, True)


# first parameter is time before executing post
threading.Timer(0.1, send_fake_request).run()
