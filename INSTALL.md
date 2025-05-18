# Installation

## System requirements

This application is a flask application with following requirements:
* Python 3.12+
* SQLAlchemy-compatible SQL-server (e.g. MariaDB or Postgre)
* An AMQP-Queue (eg RabbitMQ)

You can deploy OCPDB via docker (recommended), or via virtual environment.

### Deploy via docker container

We provide docker containers at `ghcr.io/binary-butterfly/ocpdb` with all
[version tags](https://github.com/binary-butterfly/ocpdb/tags) as container versions. A full docker compose service
will look like this:

```
x-flask-defaults: &flask-defaults
  image: "ghcr.io/binary-butterfly/ocpdb:{{ ocpdb_api_version }}"
  user: '{{ ocpdb_api_user_uid }}'
  volumes:
    - ./config.yaml:/app/config.yaml:ro
    - ./logs:/app/logs
    - ./temp:/app/temp
    - ./data:/app/data

services:
  flask:
    <<: *flask-defaults
    restart: unless-stopped
    command: [
      "gunicorn",
      "--bind", "0.0.0.0:8000",
      "webapp.entry_point_gunicorn:app",
      "--access-logfile", "-",
      "--log-file", "-",
    ]

  worker:
    <<: *flask-defaults
    restart: unless-stopped
    command: ["celery", "-A", "webapp.entry_point_celery", "worker", "--concurrency", "2"]

  heartbeat:
    <<: *flask-defaults
    restart: unless-stopped
    command: ["celery", "-A", "webapp.entry_point_celery", "beat", "-s", "/tmp/celerybeat-schedule"]

  init:
    <<: *flask-defaults
    command: ["flask", "db", "upgrade"]

```

We use yaml anchors to define the base fields just once, and then re-use them in separate services. Following vars are
used:

* `ocpdb_api_version` is the version you want to deploy
* `ocpdb_api_user_uid` is the system user uid you want to use. It's not recommended to run services like this as root.

You will need an additional database and an additional rabbitmq.


### Deploy via virtual environment

1) Use `virtualenv venv` to create a virtual environment
2) Use `./venv/bin/pip install -r requirements.txt` to install required packages
3) Move `/config_dist_dev.yaml` zu `/config.yaml` and fill in all necessary data
4) Use `./venv/bin/flask db upgrade` to upgrade your database
5) Use `./venv/bin/gunicorn "webapp.entry_point_gunicorn:app"` to start the application
6) Use `./venv/bin/flask` to start downloads


### Development setup (via Docker)

1) Use `make first-start` to create a dev environment
2) Use `make` to start the container

The web interface will be available at http://localhost:5010.

All sources have mocked services, so you can play around with mocked data and import everything.

At `dev/api_tests` you will find some HTTP request files you can use to emulate requests.


## Configuration

There are config templates for development (`config_dist_dev.yaml`) and production (`config_dist.yaml`).

Sources can be configured by `SOURCES` config value. It has the following format:

```yaml
SOURCES:
  source_uid_with_config:
    config_key: config_value
  source_uid_no_auto_fetch:
    auto_fetch: false
  source_uid_debug:
    debug: true
  source_uid_without_config:
```

* `source_uid_with_config` is an example for a source which required config, eg user and password.
* `source_uid_no_auto_fetch` is an example for a source where the heartbeat mechanism is disabled, and therefore data
  is not fetched automatically. This can make sense for debugging or for large datasets on small servers.
* `source_uid_debug` is an example for a source where all requests are dumped for debugging.
* `source_uid_without_config` is an example for a source without any required config.

At some sources, you can use the config value `url` to point to another (base) url, which might help for de. Please
have a look at the specific importer service for more information.
