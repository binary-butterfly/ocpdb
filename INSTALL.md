# Installation

## Systemvoraussetzungen

Bei der Anwendung handelt es sich um eine Flask-basierte Webanwendung mit folgenden Voraussetzungen:
* Python 3.7+
* SQLAlchemy-kompatibler SQL-Server (z.B. MariaDB)
* Eine AMQP-Queue (z.B. RabbitMQ)


## Produktiv-Version auf einem Server

1) Mit `virtualenv -p python3 venv` ein Virtual Environment erstellen
2) Mit `./venv/bin/pip install -r requirements.txt` die nötigen Python-Pakete installieren
3) `/webapp/config_dist_dev.py` zu `/webapp/config.py` umbenennen und anpassen  
4) Mit `./venv/bin/flask db upgrade` die Datenbank initialisieren 
5) Mit `./venv/bin/gunicorn "webapp.entry_point_gunicorn:app"` die Anwendung starten.
6) Mit `./venv/bin/flask` OCHP- oder OCPI-Downloads anstossen 


## Entwicklungs-Version via docker

1) `/webapp/config_dist_dev.py` zu `/webapp/config.py` umbenennen und anpassen
2) Mit `make` die Container bauen und starten
3) Mit `make migrate` die Datenbank initialisieren
