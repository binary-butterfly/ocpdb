"""optimize Evse.related_resources

Revision ID: a1b2c3d4e5f6
Revises: 78708f842662
Create Date: 2026-01-30 18:30:00.000000

"""

import json

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'a1b2c3d4e5f6'
down_revision = '78708f842662'
branch_labels = None
depends_on = None


def upgrade():
    # Add new related_resources column to evse table
    with op.batch_alter_table('evse', schema=None) as batch_op:
        batch_op.add_column(sa.Column('related_resources', sa.Text(), nullable=True))

    # Migrate data from related_resource table to evse.related_resources JSON column
    connection = op.get_bind()

    # Get all related resources grouped by evse_id
    result = connection.execute(sa.text('SELECT evse_id, url, types FROM related_resource ORDER BY evse_id, id'))

    # Group by evse_id and build JSON
    evse_resources = {}
    for row in result:
        evse_id = row[0]
        url = row[1]
        types = row[2]

        if evse_id not in evse_resources:
            evse_resources[evse_id] = []

        evse_resources[evse_id].append({
            'url': url,
            'types': types,
        })

    # Update each evse with its related_resources JSON
    for evse_id, resources in evse_resources.items():
        json_data = json.dumps(resources)
        connection.execute(
            sa.text('UPDATE evse SET related_resources = :json_data WHERE id = :evse_id'),
            {'json_data': json_data, 'evse_id': evse_id},
        )

    # Drop the related_resource table
    op.drop_table('related_resource')


def downgrade():
    # Recreate related_resource table
    op.create_table(
        'related_resource',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('created', sa.DateTime(timezone=True), nullable=False),
        sa.Column('modified', sa.DateTime(timezone=True), nullable=False),
        sa.Column('evse_id', sa.BigInteger(), nullable=False),
        sa.Column('url', sa.String(length=255), nullable=True),
        sa.Column('types', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['evse_id'], ['evse.id']),
        sa.PrimaryKeyConstraint('id'),
    )

    # Create index on evse_id
    op.create_index('ix_related_resource_evse_id', 'related_resource', ['evse_id'], unique=False)

    # Migrate data back from JSON to table
    connection = op.get_bind()

    result = connection.execute(sa.text('SELECT id, related_resources FROM evse WHERE related_resources IS NOT NULL'))

    for row in result:
        evse_id = row[0]
        json_data = row[1]

        if json_data:
            resources = json.loads(json_data)
            for resource in resources:
                connection.execute(
                    sa.text(
                        'INSERT INTO related_resource (created, modified, evse_id, url, types) '
                        'VALUES (NOW(), NOW(), :evse_id, :url, :types)'
                    ),
                    {
                        'evse_id': evse_id,
                        'url': resource.get('url'),
                        'types': resource.get('types'),
                    },
                )

    # Remove related_resources column from evse table
    with op.batch_alter_table('evse', schema=None) as batch_op:
        batch_op.drop_column('related_resources')
