"""optimize opening times

Revision ID: b2c3d4e5f6a7
Revises: a1b2c3d4e5f6
Create Date: 2026-01-30 19:30:00.000000

"""

import json

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'b2c3d4e5f6a7'
down_revision = 'a1b2c3d4e5f6'
branch_labels = None
depends_on = None


def upgrade():
    # Add new columns to location table
    with op.batch_alter_table('location', schema=None) as batch_op:
        batch_op.add_column(sa.Column('regular_hours', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('exceptional_openings', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('exceptional_closings', sa.Text(), nullable=True))

    connection = op.get_bind()

    # Migrate regular_hours data
    result = connection.execute(
        sa.text('SELECT location_id, weekday, period_begin, period_end FROM regular_hours ORDER BY location_id, id')
    )

    location_regular_hours = {}
    for row in result:
        location_id = row[0]
        if location_id not in location_regular_hours:
            location_regular_hours[location_id] = []

        location_regular_hours[location_id].append({
            'weekday': row[1],
            'period_begin': row[2],
            'period_end': row[3],
        })

    for location_id, regular_hours in location_regular_hours.items():
        json_data = json.dumps(regular_hours)
        connection.execute(
            sa.text('UPDATE location SET regular_hours = :json_data WHERE id = :location_id'),
            {'json_data': json_data, 'location_id': location_id},
        )

    # Migrate exceptional_opening_period data
    result = connection.execute(
        sa.text('SELECT location_id, period_begin, period_end FROM exceptional_opening_period ORDER BY location_id, id')
    )

    location_exceptional_openings = {}
    for row in result:
        location_id = row[0]
        if location_id not in location_exceptional_openings:
            location_exceptional_openings[location_id] = []

        location_exceptional_openings[location_id].append({
            'period_begin': row[1].isoformat() if row[1] else None,
            'period_end': row[2].isoformat() if row[2] else None,
        })

    for location_id, exceptional_openings in location_exceptional_openings.items():
        json_data = json.dumps(exceptional_openings)
        connection.execute(
            sa.text('UPDATE location SET exceptional_openings = :json_data WHERE id = :location_id'),
            {'json_data': json_data, 'location_id': location_id},
        )

    # Migrate exceptional_closing_period data
    result = connection.execute(
        sa.text('SELECT location_id, period_begin, period_end FROM exceptional_closing_period ORDER BY location_id, id')
    )

    location_exceptional_closings = {}
    for row in result:
        location_id = row[0]
        if location_id not in location_exceptional_closings:
            location_exceptional_closings[location_id] = []

        location_exceptional_closings[location_id].append({
            'period_begin': row[1].isoformat() if row[1] else None,
            'period_end': row[2].isoformat() if row[2] else None,
        })

    for location_id, exceptional_closings in location_exceptional_closings.items():
        json_data = json.dumps(exceptional_closings)
        connection.execute(
            sa.text('UPDATE location SET exceptional_closings = :json_data WHERE id = :location_id'),
            {'json_data': json_data, 'location_id': location_id},
        )

    # Drop the old tables
    op.drop_table('regular_hours')
    op.drop_table('exceptional_opening_period')
    op.drop_table('exceptional_closing_period')


def downgrade():
    # Recreate the tables
    op.create_table(
        'regular_hours',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('created', sa.DateTime(timezone=True), nullable=False),
        sa.Column('modified', sa.DateTime(timezone=True), nullable=False),
        sa.Column('location_id', sa.BigInteger(), nullable=False),
        sa.Column('weekday', sa.SmallInteger(), nullable=False),
        sa.Column('period_begin', sa.Integer(), nullable=False),
        sa.Column('period_end', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['location_id'], ['location.id']),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index('ix_regular_hours_location_id', 'regular_hours', ['location_id'], unique=False)

    op.create_table(
        'exceptional_opening_period',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('created', sa.DateTime(timezone=True), nullable=False),
        sa.Column('modified', sa.DateTime(timezone=True), nullable=False),
        sa.Column('location_id', sa.BigInteger(), nullable=False),
        sa.Column('period_begin', sa.DateTime(timezone=True), nullable=False),
        sa.Column('period_end', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['location_id'], ['location.id']),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(
        'ix_exceptional_opening_period_location_id', 'exceptional_opening_period', ['location_id'], unique=False
    )

    op.create_table(
        'exceptional_closing_period',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('created', sa.DateTime(timezone=True), nullable=False),
        sa.Column('modified', sa.DateTime(timezone=True), nullable=False),
        sa.Column('location_id', sa.BigInteger(), nullable=False),
        sa.Column('period_begin', sa.DateTime(timezone=True), nullable=False),
        sa.Column('period_end', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['location_id'], ['location.id']),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(
        'ix_exceptional_closing_period_location_id', 'exceptional_closing_period', ['location_id'], unique=False
    )

    # Migrate data back
    connection = op.get_bind()

    # Migrate regular_hours back
    result = connection.execute(sa.text('SELECT id, regular_hours FROM location WHERE regular_hours IS NOT NULL'))

    for row in result:
        location_id = row[0]
        json_data = row[1]
        if json_data:
            regular_hours_list = json.loads(json_data)
            for rh in regular_hours_list:
                connection.execute(
                    sa.text(
                        'INSERT INTO regular_hours (created, modified, location_id, weekday, period_begin, period_end) '
                        'VALUES (NOW(), NOW(), :location_id, :weekday, :period_begin, :period_end)'
                    ),
                    {
                        'location_id': location_id,
                        'weekday': rh.get('weekday'),
                        'period_begin': rh.get('period_begin'),
                        'period_end': rh.get('period_end'),
                    },
                )

    # Migrate exceptional_openings back
    result = connection.execute(
        sa.text('SELECT id, exceptional_openings FROM location WHERE exceptional_openings IS NOT NULL')
    )

    for row in result:
        location_id = row[0]
        json_data = row[1]
        if json_data:
            exceptional_openings_list = json.loads(json_data)
            for eo in exceptional_openings_list:
                connection.execute(
                    sa.text(
                        'INSERT INTO exceptional_opening_period (created, modified, location_id, period_begin, period_end) '
                        'VALUES (NOW(), NOW(), :location_id, :period_begin, :period_end)'
                    ),
                    {
                        'location_id': location_id,
                        'period_begin': eo.get('period_begin'),
                        'period_end': eo.get('period_end'),
                    },
                )

    # Migrate exceptional_closings back
    result = connection.execute(
        sa.text('SELECT id, exceptional_closings FROM location WHERE exceptional_closings IS NOT NULL')
    )

    for row in result:
        location_id = row[0]
        json_data = row[1]
        if json_data:
            exceptional_closings_list = json.loads(json_data)
            for ec in exceptional_closings_list:
                connection.execute(
                    sa.text(
                        'INSERT INTO exceptional_closing_period (created, modified, location_id, period_begin, period_end) '
                        'VALUES (NOW(), NOW(), :location_id, :period_begin, :period_end)'
                    ),
                    {
                        'location_id': location_id,
                        'period_begin': ec.get('period_begin'),
                        'period_end': ec.get('period_end'),
                    },
                )

    # Remove columns from location table
    with op.batch_alter_table('location', schema=None) as batch_op:
        batch_op.drop_column('regular_hours')
        batch_op.drop_column('exceptional_openings')
        batch_op.drop_column('exceptional_closings')
