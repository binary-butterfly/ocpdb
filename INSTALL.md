# Installation

## System requirements

This application is a flask application with following requirements:
* Python 3.12+
* SQLAlchemy-compatible SQL-server (e.g. MariaDB)
* An AMQP-Queue (eg RabbitMQ)


## Production version (legacy)

1) Use `virtualenv -p python3 venv` to create a virtual environment
2) Use `./venv/bin/pip install -r requirements.txt` to install required packages
3) Move `/config_dist_dev.yaml` zu `/config.yaml` and fill in all necessary data
4) Use `./venv/bin/flask db upgrade` to upgrade your database
5) Use `./venv/bin/gunicorn "webapp.entry_point_gunicorn:app"` to start the application
6) Use `./venv/bin/flask` to start downloads


## Production setup (via Docker)

This is the recommended way of installation now.

*TODO: add instructions here*


## Development setup (via Docker)

1) Use `make first-start` to create a dev environment
2) Use `make` to start the container

The web interface will be available at http://localhost:5010.

All sources have mocked services, so you can play around with mocked data and import everything.

At `dev/api_tests` you will find some HTTP request files you can use to emulate requests.
