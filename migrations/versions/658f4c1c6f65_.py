"""empty message

Revision ID: 658f4c1c6f65
Revises: da2c325f6fab
Create Date: 2023-12-11 21:04:14.017713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '658f4c1c6f65'
down_revision = 'da2c325f6fab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('password')

    # ### end Alembic commands ###