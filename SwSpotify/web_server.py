from flask import Flask, request, jsonify
from flask_cors import CORS
from SwSpotify import WebData
import logging
import requests
import threading


app = Flask(__name__)
CORS(app)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


def run():
    app = Flask(__name__)
    CORS(app)
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    timer = threading.Timer(0.5, shutdown_post)
    timer.daemon = True
    timer.start()
    start()


def shutdown_post():
    try:
        requests.post("http://127.0.0.1:5043/shutdown")
    except (requests.exceptions.ConnectionError, KeyboardInterrupt):
        pass


@app.route('/ping', methods=['GET'])
def pong():
    return "Pong"


@app.route('/shutdown', methods=['POST'])
def shutdown_server():
    shutdown()
    return 'Server shutting down...'


def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


def start():
    app.run(port=5043)


@app.route('/getSong', methods=['POST'])
def get_song():
    data = request.get_json()
    WebData.set_song(data)
    shutdown()
    return jsonify({'message': data})


if __name__ == '__main__':
    run()
