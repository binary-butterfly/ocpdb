"""location geography index

Adds a gist index on (geometry::geography) so the radius search in fetch_locations() can use ST_DWithin instead of
ST_DistanceSphere(...) < radius. The latter is a plain function comparison that the planner cannot index, so it
seq-scanned the whole location table on every ?lat&lon&radius request.

PostGIS only, the index is skipped on other dialects.

Revision ID: a3f1c8d92b47
Revises: 76e048ecbc17
Create Date: 2026-07-26 00:00:00.000000

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = 'a3f1c8d92b47'
down_revision = '76e048ecbc17'
branch_labels = None
depends_on = None


def upgrade():
    if op.get_bind().dialect.name != 'postgresql':
        return

    op.execute('CREATE INDEX geography_index ON location USING gist ((geometry::geography))')


def downgrade():
    if op.get_bind().dialect.name != 'postgresql':
        return

    op.execute('DROP INDEX geography_index')
