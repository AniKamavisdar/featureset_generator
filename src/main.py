import threading
import datetime
import time
import getopt
import sys
import flask

# Imports from custom lib
import web_servers.server
from data.health import health_status
from configs.app_configs import app_config

# Defining Flask App and config at global level
flask_app = flask.Flask(app_config.app_name)
flask_app.url_map.strict_slashes = False
flask_app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
flask_app.config['JSON_SORT_KEYS'] = False


def run(from_date, to_date):
    while True:
        print(f"Batch range {from_date} - {to_date}")
        change_verification()

        print("Verification Completed")
        health_status.update_status(status='Complete', details=f'Task Completed at {datetime.date.today()}')
        time.sleep(30)
        break
    print("Stopping Threaded function")
    return None


def change_verification():
    print("Sleeping for 1-minutes")
    health_status.update_status(status='In Progress', details=f'Task In Progress, update at: {datetime.date.today()}')
    time.sleep(30)


def __main():
    print("------------------------------------------------------------------")
    print("Application Initialisation Started")
    to_date = datetime.date.today()
    from_date = to_date-datetime.timedelta(days=30)
    # Start server as thread
    web_servers.server.start_server()
    # Start main modelling process as a thread
    threading.Thread(target=run, args=(from_date, to_date), daemon=True).start()
    web_servers.server.await_server_end()
    web_servers.server.stop_server()
    print("Application Ends")
    print("------------------------------------------------------------------")


if __name__ == '__main__':
    __main()