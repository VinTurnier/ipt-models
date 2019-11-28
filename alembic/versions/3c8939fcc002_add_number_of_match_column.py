"""add_number_of_match_column

Revision ID: 3c8939fcc002
Revises: 0ca3f1541aff
Create Date: 2019-11-27 19:04:54.711121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c8939fcc002'
down_revision = '0ca3f1541aff'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('images', sa.Column('num_of_matches',sa.Integer,nullable=False))


def downgrade():
    op.drop_column('images','num_of_matches')
