"""create unique ktp

Revision ID: 7a5aa62bce48
Revises: ddcc9f1b58e1
Create Date: 2021-07-24 16:11:44.970863

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a5aa62bce48'
down_revision = 'ddcc9f1b58e1'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('Patient', sa.Column('ktp', sa.Integer, unique=True))
    pass


def downgrade():
    pass
