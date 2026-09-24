"""public api indices

Adds indices for the filters of the public APIs and the realtime exports (DATEX realtime API and Mobilithek push):
- status_last_updated on evse, for evse_status_last_updated_since, which is used for delta pulls and pushes.
- last_updated on connector, tariff and tariff_association, for the last_updated_since filters.
- postal_code and official_region_code on location, for the equality filters. The existing index on
  (country, official_region_code) cannot serve official_region_code on its own.

PostgreSQL only:
- a partial index on evse.charging_station_id for non-STATIC EVSEs, matching exclude_evse_status=[STATIC]. The existing
  index on status cannot serve status <> 'STATIC'.
- covering indices on charging_station.location_id and evse.charging_station_id, which include the columns the tiles
  need, so the tiles query can be answered by index-only scans. They replace the plain indices of the same name.
- a partial gist index on location.geometry for non-duplicate locations, which the tiles filter by default.
- trigram indices on location.name, location.address, location.city and business.name for the substring filters.

Revision ID: 5e2b9c4d7a13
Revises: a3f1c8d92b47
Create Date: 2026-09-24 00:00:00.000000

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '5e2b9c4d7a13'
down_revision = 'a3f1c8d92b47'
branch_labels = None
depends_on = None


TRIGRAM_INDICES: list[tuple[str, str, str]] = [
    ('ix_location_name_trgm', 'location', 'name'),
    ('ix_location_address_trgm', 'location', 'address'),
    ('ix_location_city_trgm', 'location', 'city'),
    ('ix_business_name_trgm', 'business', 'name'),
]


def upgrade():
    op.create_index('ix_evse_status_last_updated', 'evse', ['status_last_updated'], unique=False)
    op.create_index('ix_connector_last_updated', 'connector', ['last_updated'], unique=False)
    op.create_index('ix_tariff_last_updated', 'tariff', ['last_updated'], unique=False)
    op.create_index('ix_tariff_association_last_updated', 'tariff_association', ['last_updated'], unique=False)
    op.create_index('ix_location_postal_code', 'location', ['postal_code'], unique=False)
    op.create_index('ix_location_official_region_code', 'location', ['official_region_code'], unique=False)

    if op.get_bind().dialect.name != 'postgresql':
        return

    op.create_index(
        'ix_evse_charging_station_id_non_static',
        'evse',
        ['charging_station_id'],
        unique=False,
        postgresql_where=sa.text("status <> 'STATIC'"),
    )

    op.drop_index('ix_charging_station_location_id', table_name='charging_station')
    op.create_index(
        'ix_charging_station_location_id',
        'charging_station',
        ['location_id'],
        unique=False,
        postgresql_include=['id'],
    )

    op.drop_index('ix_evse_charging_station_id', table_name='evse')
    op.create_index(
        'ix_evse_charging_station_id',
        'evse',
        ['charging_station_id'],
        unique=False,
        postgresql_include=['status', 'parking_restrictions'],
    )

    op.execute(
        'CREATE INDEX ix_location_geometry_non_duplicate ON location USING gist (geometry) '
        'WHERE dynamic_location_id IS NULL'
    )

    op.execute('CREATE EXTENSION IF NOT EXISTS pg_trgm')
    for index_name, table_name, column_name in TRIGRAM_INDICES:
        op.execute(f'CREATE INDEX {index_name} ON {table_name} USING gin ({column_name} gin_trgm_ops)')


def downgrade():
    if op.get_bind().dialect.name == 'postgresql':
        for index_name, table_name, _column_name in TRIGRAM_INDICES:
            op.drop_index(index_name, table_name=table_name)

        op.drop_index('ix_location_geometry_non_duplicate', table_name='location')

        op.drop_index('ix_evse_charging_station_id', table_name='evse')
        op.create_index('ix_evse_charging_station_id', 'evse', ['charging_station_id'], unique=False)

        op.drop_index('ix_charging_station_location_id', table_name='charging_station')
        op.create_index('ix_charging_station_location_id', 'charging_station', ['location_id'], unique=False)

        op.drop_index('ix_evse_charging_station_id_non_static', table_name='evse')

    op.drop_index('ix_location_official_region_code', table_name='location')
    op.drop_index('ix_location_postal_code', table_name='location')
    op.drop_index('ix_tariff_association_last_updated', table_name='tariff_association')
    op.drop_index('ix_tariff_last_updated', table_name='tariff')
    op.drop_index('ix_connector_last_updated', table_name='connector')
    op.drop_index('ix_evse_status_last_updated', table_name='evse')
