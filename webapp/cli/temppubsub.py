"""
Giro-e OCPI
Copyright (c) 2024, binary butterfly GmbH
All rights reserved.
"""
import click as click
from flask.cli import AppGroup, with_appcontext
from webapp.models.connector import ConnectorStatus

from webapp.dependencies import dependencies

cli_connector = AppGroup('connector')


@cli_connector.command('set-status', help='set connector status')
@click.argument('connector_uid', type=str)
@click.argument('connector_status', type=click.Choice([item.value for item in ConnectorStatus]))
def set_connector_status(connector_uid: str, connector_status: str):
    pubsub_client = dependencies.get_pubsub_client()
    pubsub_client.sub('connector')
    print(str(pubsub_client))
    pubsub_client.pub(f'CONNECTOR.{connector_uid.upper()}.STATUS', connector_status)
    print('done')
