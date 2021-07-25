"""create unique ktp 1

Revision ID: 30938aad7ea0
Revises: 7a5aa62bce48
Create Date: 2021-07-24 16:20:31.246153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30938aad7ea0'
down_revision = '7a5aa62bce48'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('Patient', sa.Column('ktp', sa.Integer, unique=True))
    op.create_unique_constraint('unique_ktp', 'Patient', ['ktp'])
    pass


def downgrade():
    pass
