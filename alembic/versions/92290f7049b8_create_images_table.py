"""create_images_table

Revision ID: 92290f7049b8
Revises: 
Create Date: 2019-10-30 19:06:57.392456

"""
from alembic import op
from sqlalchemy.sql import text
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92290f7049b8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('images',
    sa.Column('id',sa.Integer,primary_key=True,autoincrement=True),
    sa.Column('url',sa.String(150),nullable=False),
    sa.Column('timestamp',sa.DateTime,server_default=text('CURRENT_TIMESTAMP'),nullable=True)
    )


def downgrade():
    op.drop_table('images')
