import threading, requests


def shutdown_post():
    try:
        requests.post("http://127.0.0.1:5042/shutdown")
    except:
        pass


threading.Timer(2, shutdown_post).run()
