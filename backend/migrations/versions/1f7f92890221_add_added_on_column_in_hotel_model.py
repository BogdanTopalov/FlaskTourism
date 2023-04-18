"""Add added_on column in Hotel model

Revision ID: 1f7f92890221
Revises: 22ea827f7008
Create Date: 2023-04-09 15:16:25.841066

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f7f92890221'
down_revision = '22ea827f7008'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hotel', schema=None) as batch_op:
        batch_op.add_column(sa.Column('added_on', sa.DateTime(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hotel', schema=None) as batch_op:
        batch_op.drop_column('added_on')

    # ### end Alembic commands ###