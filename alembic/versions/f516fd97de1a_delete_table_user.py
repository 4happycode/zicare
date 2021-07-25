"""delete table user

Revision ID: f516fd97de1a
Revises: 30938aad7ea0
Create Date: 2021-07-25 13:15:54.877785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f516fd97de1a'
down_revision = '30938aad7ea0'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    op.drop_table('users')
    pass
