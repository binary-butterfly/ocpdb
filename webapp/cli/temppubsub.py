"""
Giro-e OCPI
Copyright (c) 2024, binary butterfly GmbH
All rights reserved.
"""
import click as click
from flask.cli import AppGroup, with_appcontext
from webapp.models.connector import ConnectorStatus
from webapp.services.pub_sub_services.subscrption_service import PubSubService
from webapp.dependencies import dependencies

cli_connector = AppGroup('connector')


@cli_connector.command('set-status', help='set connector status')
@click.argument('connector_uid', type=str)
@click.argument('connector_status', type=click.Choice([item.value for item in ConnectorStatus]))
def set_connector_status(connector_uid: str, connector_status: str):
    pubsub_client = dependencies.get_pubsub_client()
    pubsub_client.pub(f'CONNECTOR.{connector_uid.upper()}.STATUS', connector_status)
    print('done')


@cli_connector.command('subscribe', help='set connector status')
def subscribe_connectors():
    pub_sub_connector_service = PubSubService(
        dependencies.get_evse_repository(),
        dependencies.get_pubsub_client(),
        **dependencies.get_base_service_dependencies(),
    )
    pub_sub_connector_service.register()
    pub_sub_connector_service.listen_for_updates()
