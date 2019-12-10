from flask import Flask, request, jsonify
from flask_cors import CORS
from SwSpotify.web_data import WebData
import logging


app = Flask(__name__)
CORS(app)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


def run():
    app = Flask(__name__)
    CORS(app)
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    start()


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
    app.run(port=5042)


@app.route('/getsong', methods=['POST'])
def get_song():
    data = request.get_json()
    WebData.set_song(data)
    shutdown()
    return jsonify({'message': data})


if __name__ == '__main__':
    run()
