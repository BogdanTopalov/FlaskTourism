"""Change price_per_night to Integer

Revision ID: 5a2b0796eec0
Revises: c875f4e238cb
Create Date: 2023-04-22 11:49:28.668374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a2b0796eec0'
down_revision = 'c875f4e238cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hotel', schema=None) as batch_op:
        batch_op.alter_column('price_per_night',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.Integer(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hotel', schema=None) as batch_op:
        batch_op.alter_column('price_per_night',
               existing_type=sa.Integer(),
               type_=sa.DOUBLE_PRECISION(precision=53),
               existing_nullable=False)

    # ### end Alembic commands ###