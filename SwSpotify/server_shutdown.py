import threading
import requests


def shutdown_post():
    try:
        requests.post("http://127.0.0.1:5043/shutdown")
    except (requests.exceptions.ConnectionError, KeyboardInterrupt):
        pass


# first parameter is time before executing post
try:
    threading.Timer(0.5, shutdown_post).run()
except KeyboardInterrupt:
    pass
