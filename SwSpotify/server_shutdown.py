import threading
import requests


def shutdown_post():
    try:
        requests.post("http://127.0.0.1:5042/shutdown")
    except requests.exceptions.ConnectionError:
        pass


# first parameter is time before executing post
threading.Timer(1.3, shutdown_post).run()
