"""init keys

Revision ID: 08f900d9d379
Revises: e2268b2cf1dd
Create Date: 2022-12-28 17:15:23.281301

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = '08f900d9d379'
down_revision = 'e2268b2cf1dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'business', 'image', ['logo_id'], ['id'], use_alter=True)
    op.create_foreign_key(None, 'connector', 'evse', ['evse_id'], ['id'], use_alter=True)
    op.create_foreign_key(None, 'evse', 'location', ['location_id'], ['id'], use_alter=True)
    op.create_foreign_key(None, 'evse_image', 'evse', ['evse_id'], ['id'], use_alter=True)
    op.create_foreign_key(None, 'evse_image', 'image', ['image_id'], ['id'], use_alter=True)
    op.create_foreign_key(None, 'exceptional_closing_period', 'location', ['location_id'], ['id'], use_alter=True)
    op.create_foreign_key(None, 'exceptional_opening_period', 'location', ['location_id'], ['id'], use_alter=True)
    op.create_foreign_key(None, 'location', 'business', ['operator_id'], ['id'], use_alter=True)
    op.create_foreign_key(None, 'location', 'business', ['suboperator_id'], ['id'], use_alter=True)
    op.create_foreign_key(None, 'location', 'business', ['owner_id'], ['id'], use_alter=True)
    op.create_foreign_key(None, 'location_image', 'image', ['image_id'], ['id'], use_alter=True)
    op.create_foreign_key(None, 'location_image', 'location', ['location_id'], ['id'], use_alter=True)
    op.create_foreign_key(None, 'regular_hours', 'location', ['location_id'], ['id'], use_alter=True)
    op.create_foreign_key(None, 'related_resource', 'evse', ['evse_id'], ['id'], use_alter=True)
    # ### end Alembic commands ###
    if op.get_bind().engine.name == 'postgresql':
        op.execute('CREATE INDEX geometry_index ON location USING GIST (geometry);')
    else:
        op.execute('CREATE SPATIAL INDEX geometry_index ON location (geometry);')


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'related_resource', type_='foreignkey')
    op.drop_constraint(None, 'regular_hours', type_='foreignkey')
    op.drop_constraint(None, 'location_image', type_='foreignkey')
    op.drop_constraint(None, 'location_image', type_='foreignkey')
    op.drop_constraint(None, 'location', type_='foreignkey')
    op.drop_constraint(None, 'location', type_='foreignkey')
    op.drop_constraint(None, 'location', type_='foreignkey')
    op.drop_constraint(None, 'location', type_='foreignkey')
    op.drop_constraint(None, 'exceptional_opening_period', type_='foreignkey')
    op.drop_constraint(None, 'exceptional_closing_period', type_='foreignkey')
    op.drop_constraint(None, 'evse_image', type_='foreignkey')
    op.drop_constraint(None, 'evse_image', type_='foreignkey')
    op.drop_constraint(None, 'evse', type_='foreignkey')
    op.drop_constraint(None, 'connector', type_='foreignkey')
    op.drop_constraint(None, 'business', type_='foreignkey')
    # ### end Alembic commands ###
