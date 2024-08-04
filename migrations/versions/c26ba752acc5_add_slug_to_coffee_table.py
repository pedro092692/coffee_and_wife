"""add slug to coffee table

Revision ID: c26ba752acc5
Revises: 8351f0691c1c
Create Date: 2024-08-04 00:02:45.211114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c26ba752acc5'
down_revision = '8351f0691c1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cafe', schema=None) as batch_op:
        batch_op.add_column(sa.Column('slug', sa.String(), nullable=False))
        batch_op.create_unique_constraint('slug', ['slug'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cafe', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('slug')

    # ### end Alembic commands ###
