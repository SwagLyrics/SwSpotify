import threading
import requests


def shutdown_post():
    try:
        requests.post("http://127.0.0.1:5042/shutdown")
    except requests.exceptions.ConnectionError:
        pass


threading.Timer(2, shutdown_post).run()
