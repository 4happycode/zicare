"""delete table user is def upgrade

Revision ID: 172031b11c29
Revises: f516fd97de1a
Create Date: 2021-07-25 13:18:06.976935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '172031b11c29'
down_revision = 'f516fd97de1a'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('users')
    pass


def downgrade():
    pass
