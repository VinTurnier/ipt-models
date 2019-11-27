"""add_customers_table

Revision ID: 0ca3f1541aff
Revises: 92290f7049b8
Create Date: 2019-11-27 17:56:31.970522

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
revision = '0ca3f1541aff'
down_revision = '92290f7049b8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("customers",
    sa.Column("id",sa.Integer,primary_key=True,autoincrement=True),
    sa.Column("phone_number",sa.String(25),nullable=False),
    sa.Column("num_media_sent", sa.Integer,nullable=False),
    sa.Column("created_at",sa.TIMESTAMP,nullable=False,server_default=text("CURRENT_TIMESTAMP")),
    sa.Column("updated_at",sa.TIMESTAMP,nullable=False,server_default=text("CURRENT_TIMESTAMP"))
    )


def downgrade():
    op.drop_table("customers")
