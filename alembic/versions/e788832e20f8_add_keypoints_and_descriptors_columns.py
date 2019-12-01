"""add_keypoints_and_descriptors_columns

Revision ID: e788832e20f8
Revises: 3c8939fcc002
Create Date: 2019-11-30 21:46:08.716923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e788832e20f8'
down_revision = '3c8939fcc002'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('images', sa.Column('key_points',sa.String(255),nullable=False))
    op.add_column('images', sa.Column('descriptors',sa.String(255),nullable=False))

def downgrade():
    op.drop_column('images','key_points')
    op.drop_column('images','descriptors')
