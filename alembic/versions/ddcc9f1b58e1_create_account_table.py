"""create account table

Revision ID: ddcc9f1b58e1
Revises: 7972a23eaea8
Create Date: 2021-07-24 15:47:58.373204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddcc9f1b58e1'
down_revision = '7972a23eaea8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Patient',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('ktp', sa.Integer, nullable=False),
        sa.Column('full_name', sa.String(150), nullable=False),
        sa.Column('first_name', sa.String(50), nullable=False),
        sa.Column('last_name', sa.String(50), nullable=False),
        sa.Column('address', sa.Text),
        sa.Column('created_date', sa.DateTime(), nullable=False),
        sa.Column('modified_date', sa.DateTime(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    pass


def downgrade():
    pass
