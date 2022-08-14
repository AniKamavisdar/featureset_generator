from threading import Thread
import flask
from os import environ as env
from flask import redirect, request
from waitress.server import create_server
import datetime

from data.health import health_status
from main import flask_app
from main import app_config

from workflow.job import extract

# flask_app = flask.Flask(app_config.app_name)
# flask_app.url_map.strict_slashes = False
# flask_app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
# flask_app.config['JSON_SORT_KEYS'] = False
# global flask_app

OUTPUT_PATH = env['FEATURE_OUTPUT_LOC']


@flask_app.before_request
def clear_trailing():
    rp = request.path
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1])


@flask_app.route('/health')
def service_health():
    print("Health Endpoint requested")
    return flask.jsonify(health_status.get_health())


@flask_app.route('/show_distrib_map')
def show_distrib_map():
    print("Printing Map")


@flask_app.route('/shutdown')
def get_model_details():
    stop_server()
    return flask.jsonify({"Shutdown Request": "Acknowledged"})


@flask_app.route('/extract')
def extract_data():
    print(f"Starting data extraction at  : {datetime.datetime.today()}")
    data = extract()
    print(f"Data Extraction completed at : {datetime.datetime.today()}")
    return flask.jsonify(data.squeeze().to_dict())


class ServerThread(Thread):
    srv = None

    def __init__(self, app):
        Thread.__init__(self)
        print(f"Instantiating server : {app}")
        self.srv = create_server(app, host=app_config.host, port=app_config.port)

    def run(self):
        print(f"Starting web server")
        self.srv.run()

    def shutdown(self):
        self.srv.close()


def start_server():
    global server
    app_url = f'http://{app_config.host}:{app_config.port}'
    server = ServerThread(flask_app)
    server.start()
    print(f"Server thread started on {app_url}")
    health_status.update_status(status='Started', details='Server Started')


def await_server_end():
    server.join()


def stop_server():
    # global server
    print("Application server shutdown requested...")
    server.shutdown()
