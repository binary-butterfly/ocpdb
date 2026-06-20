"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2021 binary butterfly GmbH

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

import logging
import re
from logging.config import fileConfig
from typing import Iterable

from alembic import context
from alembic.operations import MigrationScript
from alembic.runtime.migration import MigrationContext
from flask import current_app
from sqlalchemy.sql.schema import SchemaItem

config = context.config

fileConfig(config.config_file_name)
logger = logging.getLogger('alembic.env')

config.set_main_option('sqlalchemy.url', str(current_app.extensions['migrate'].db.engine.url).replace('%', '%%'))
target_metadata = current_app.extensions['migrate'].db.metadata

exclude_tables = re.sub(
    r'\s+',
    '',
    config.get_section_option('alembic:exclude', 'tables'),  # replace whitespace
).split(',')


def include_object(object: SchemaItem, name: str | None, type_: str, *args, **kwargs) -> bool:
    return not (type_ == 'table' and name in exclude_tables)


def run_migrations_offline() -> None:
    url = config.get_main_option('sqlalchemy.url')
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True, include_object=include_object)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:

    def process_revision_directives(
        context: MigrationContext,
        revision: str | Iterable[str | None] | Iterable[str],
        directives: list[MigrationScript],
    ) -> None:
        if getattr(config.cmd_opts, 'autogenerate', False):
            script = directives[0]
            if script.upgrade_ops.is_empty():
                directives[:] = []
                logger.info('No changes in schema detected.')

    connectable = current_app.extensions['migrate'].db.engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            process_revision_directives=process_revision_directives,
            include_object=include_object,
            **current_app.extensions['migrate'].configure_args,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
