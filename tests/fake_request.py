import requests


class PingStatus:
    status = None


def send_fake_request():
    data = '''{"title": "Hello","artist": "Adele","playState": "Pause"}'''
    s = requests.session()
    s.headers.update({"Content-type": "application/json"})
    s.post("http://127.0.0.1:5043/getSong", data, True)


def send_ping():
    req = requests.get("http://127.0.0.1:5043/ping")
    PingStatus.status = req.ok