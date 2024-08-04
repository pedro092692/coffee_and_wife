"""add slug to coffee table

Revision ID: 8244d92b5ab9
Revises: ac7ba14c19ed
Create Date: 2024-08-03 23:56:35.431882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8244d92b5ab9'
down_revision = 'ac7ba14c19ed'
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
