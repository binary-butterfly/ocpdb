"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2024 binary butterfly GmbH

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
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


@cli_connector.command('subscribe', help='set connector status')
def subscribe_connectors():
    pub_sub_connector_service = PubSubService(
        evse_repository=dependencies.get_evse_repository(),
        pubsub_client=dependencies.get_pubsub_client(),
        **dependencies.get_base_service_dependencies(),
    )
    pub_sub_connector_service.register()
    pub_sub_connector_service.listen_for_updates()
